from __future__ import annotations

from pathlib import Path

import nbformat as nbf

ROOT = Path(__file__).resolve().parents[1]
NOTEBOOK_PATH = ROOT / "notebooks" / "004_hyperparameter_likelihood_models_gifs.ipynb"
NOTEBOOK_PATH.parent.mkdir(parents=True, exist_ok=True)

nb = nbf.v4.new_notebook()
nb.metadata = {
    "kernelspec": {
        "display_name": "Python (dev_statistics venv)",
        "language": "python",
        "name": "dev_statistics_venv",
    },
    "language_info": {"name": "python", "version": "3.11"},
}

cells: list = []

cells.append(nbf.v4.new_markdown_cell(r"""# 「パラメータのパラメータ」を持つ尤度モデルを GIF で理解する

階層モデルで混乱しやすいのは、観測データの尤度パラメータ $\theta_j$ のさらに上に、$\theta_j$ の分布を決める **ハイパーパラメータ** があることです。

```text
ハイパーパラメータ φ
        ↓  θ_j の分布を決める
グループ別パラメータ θ_j
        ↓  観測データの尤度を決める
観測データ y_ij
```

このノートでは、保存済みローカル公開データだけを使い、次の 3 例を可視化します。

1. **Beta-Binomial**: 確率 $p_j$ のさらに上に Beta 分布の $\alpha,\beta$ を置く。
2. **Gamma-Poisson**: カウント平均 $\lambda_j$ のさらに上に Gamma 分布の shape/rate を置く。
3. **Normal-Normal**: グループ平均 $\mu_j$ のさらに上に $\mu_0,\tau$ を置く。

いずれも「各グループを別々に推定する」のではなく、グループ別パラメータが **共通の母集団分布から来た** と考えることで、情報を共有します。
"""))

cells.append(nbf.v4.new_markdown_cell(r"""## 0. 何が「パラメータのパラメータ」なのか

### 通常の尤度モデル

例えば二値データなら、

$$
y_j \sim \mathrm{Binomial}(n_j, p_j)
$$

ここで $p_j$ は尤度のパラメータです。

### 階層モデル

さらに、$p_j$ 自体が何かの分布から来たと考えると、

$$
p_j \sim \mathrm{Beta}(\alpha, \beta)
$$

となります。この $\alpha,\beta$ が **パラメータ $p_j$ のパラメータ**、つまりハイパーパラメータです。

よく使う再パラメータ化:

$$
\alpha = m\kappa, \quad \beta = (1-m)\kappa
$$

- $m$: グループ確率 $p_j$ たちの中心
- $\kappa$: どれくらい中心 $m$ に集まるか、つまり shrinkage の強さ

このノートの GIF では、ハイパーパラメータが動くと、その下の $p_j,\lambda_j,\mu_j$ の推定がどう変わるかを見る。
"""))

cells.append(nbf.v4.new_code_cell(r"""# 1. Imports / paths / theme
from __future__ import annotations

import warnings
from pathlib import Path

import imageio.v2 as imageio
import japanize_matplotlib
import matplotlib

matplotlib.use("Agg")

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
from scipy.optimize import minimize
from scipy.special import betaln, expit, gammaln, logit
from scipy.stats import beta as beta_dist
from scipy.stats import gamma as gamma_dist
from scipy.stats import norm

warnings.filterwarnings("ignore", category=RuntimeWarning)
warnings.filterwarnings("ignore", category=UserWarning)

sns.set_theme(style="whitegrid", palette="muted", font_scale=1.0)
japanize_matplotlib.japanize()
plt.rcParams["figure.dpi"] = 110
plt.rcParams["savefig.dpi"] = 130
plt.rcParams["axes.unicode_minus"] = False

PROJECT_ROOT = Path.cwd()
if PROJECT_ROOT.name == "notebooks":
    PROJECT_ROOT = PROJECT_ROOT.parent

DATA_DIR = PROJECT_ROOT / "data" / "raw"
GIF_DIR = PROJECT_ROOT / "outputs" / "gifs"
FIG_DIR = PROJECT_ROOT / "outputs" / "figures"
for path in [DATA_DIR, GIF_DIR, FIG_DIR]:
    path.mkdir(parents=True, exist_ok=True)

RNG = np.random.default_rng(20260620)
print(f"PROJECT_ROOT = {PROJECT_ROOT}")
print(f"DATA_DIR     = {DATA_DIR}")
print(f"GIF_DIR      = {GIF_DIR}")
"""))

cells.append(nbf.v4.new_code_cell(r"""# 2. Load locally saved open data
DATA_FILES = {
    "tips": DATA_DIR / "tips.csv",
    "penguins": DATA_DIR / "penguins.csv",
}


def load_local_csv(name: str) -> pd.DataFrame:
    path = DATA_FILES[name]
    if not path.exists():
        raise FileNotFoundError(f"{path} が見つかりません。公開データを data/raw/ に保存してから実行してください。")
    print(f"{name:<8} <- {path.relative_to(PROJECT_ROOT).as_posix()}")
    return pd.read_csv(path)


tips = load_local_csv("tips")
penguins = load_local_csv("penguins")
print("tips    ", tips.shape, list(tips.columns))
print("penguins", penguins.shape, list(penguins.columns))
"""))

cells.append(nbf.v4.new_code_cell(r"""# 3. Shared helpers
def fig_to_frame(fig: matplotlib.figure.Figure) -> np.ndarray:
    fig.canvas.draw()
    rgba = np.asarray(fig.canvas.buffer_rgba())
    return rgba[:, :, :3].copy()


def save_gif(frames: list[np.ndarray], path: Path, fps: int = 8) -> Path:
    path.parent.mkdir(parents=True, exist_ok=True)
    imageio.mimsave(path, frames, duration=1 / fps, loop=0)
    print(f"saved {path} ({len(frames)} frames, {fps} fps)")
    return path


def add_note(ax: plt.Axes, text: str, loc: tuple[float, float] = (0.02, 0.98), fontsize: int = 9) -> None:
    ax.text(
        loc[0], loc[1], text,
        transform=ax.transAxes,
        va="top", ha="left", fontsize=fontsize,
        bbox={"boxstyle": "round,pad=0.35", "fc": "white", "ec": "0.75", "alpha": 0.93},
    )


def interpolate(a: np.ndarray, b: np.ndarray, n: int) -> list[np.ndarray]:
    s = np.linspace(0, 1, n)
    # smoothstep for more readable animation
    s = s * s * (3 - 2 * s)
    return [(1 - si) * a + si * b for si in s]
"""))

cells.append(nbf.v4.new_markdown_cell(r"""## 1. Beta-Binomial: 「確率 $p_j$」の上に Beta($\alpha,\beta$) を置く

データは `tips.csv` の `smoker` を、曜日 × 昼夜 (`day_time`) グループで集計します。

$$
y_j \sim \mathrm{Binomial}(n_j, p_j)
$$

$$
p_j \sim \mathrm{Beta}(\alpha, \beta)
$$

$$
\alpha = m\kappa, \quad \beta = (1-m)\kappa
$$

- $p_j$: グループ $j$ の喫煙テーブル比率。これは観測尤度のパラメータ。
- $m$: $p_j$ たちの母集団中心。
- $\kappa$: $p_j$ たちが $m$ 周辺にどれくらい集まるか。

GIF の読み方:

- 左: ハイパーパラメータ $(m,\kappa)$ が作る Beta 分布。
- 右: グループごとの観測比率と、Beta-Binomial 的な事後平均。
- $\kappa$ が大きいと、グループ別 $p_j$ は中心 $m$ に強く縮む。
"""))

cells.append(nbf.v4.new_code_cell(r"""def prepare_beta_binomial_data() -> pd.DataFrame:
    df = tips[["day", "time", "smoker"]].dropna().copy()
    df["is_smoker"] = (df["smoker"].astype(str) == "Yes").astype(int)
    df["group"] = df["day"].astype(str) + "-" + df["time"].astype(str)
    agg = df.groupby("group")["is_smoker"].agg(y="sum", n="count").reset_index()
    agg = agg[agg["n"] >= 5].sort_values("group").reset_index(drop=True)
    agg["obs_rate"] = agg["y"] / agg["n"]
    return agg


def beta_binomial_nll(params: np.ndarray, y: np.ndarray, n: np.ndarray) -> float:
    m = expit(params[0])
    kappa = np.exp(params[1])
    alpha = max(m * kappa, 1e-6)
    beta = max((1 - m) * kappa, 1e-6)
    # Marginal likelihood: choose(n,y) * B(y+a, n-y+b) / B(a,b); choose term omitted for hyperparameter fit.
    ll = np.sum(betaln(y + alpha, n - y + beta) - betaln(alpha, beta))
    return float(-ll)


def fit_beta_binomial_hyperparams(agg: pd.DataFrame) -> tuple[float, float]:
    y = agg["y"].to_numpy(float)
    n = agg["n"].to_numpy(float)
    start_m = np.clip(y.sum() / n.sum(), 0.02, 0.98)
    res = minimize(beta_binomial_nll, x0=np.array([logit(start_m), np.log(8.0)]), args=(y, n), method="Nelder-Mead")
    m = float(expit(res.x[0]))
    kappa = float(np.exp(res.x[1]))
    return m, kappa


def make_beta_binomial_hyperparameter_gif() -> Path:
    agg = prepare_beta_binomial_data()
    y = agg["y"].to_numpy(float)
    n = agg["n"].to_numpy(float)
    obs = agg["obs_rate"].to_numpy(float)
    mle_m, mle_kappa = fit_beta_binomial_hyperparams(agg)
    start = np.array([0.50, 80.0])
    target = np.array([mle_m, mle_kappa])
    states = interpolate(start, target, 56)
    xgrid = np.linspace(0.001, 0.999, 400)
    x_pos = np.arange(len(agg))
    labels = agg["group"].tolist()
    widths = []

    frames = []
    for t, (m, kappa) in enumerate(states):
        alpha = m * kappa
        beta = (1 - m) * kappa
        post_a = alpha + y
        post_b = beta + n - y
        post_mean = post_a / (post_a + post_b)
        lo = beta_dist.ppf(0.05, post_a, post_b)
        hi = beta_dist.ppf(0.95, post_a, post_b)
        widths.append(float(np.mean(hi - lo)))

        fig, axes = plt.subplots(1, 2, figsize=(12, 5.1), constrained_layout=True, gridspec_kw={"width_ratios": [1.0, 1.35]})
        ax0, ax1 = axes
        prior_pdf = beta_dist.pdf(xgrid, alpha, beta)
        ax0.plot(xgrid, prior_pdf, color="#4C72B0", lw=2.8, label="p_j の母集団分布")
        ax0.axvline(m, color="#C44E52", ls="--", lw=1.8, label="中心 m")
        ax0.set_title("上の階層: p_j ~ Beta(α, β)")
        ax0.set_xlabel("グループ確率 p_j")
        ax0.set_ylabel("density")
        ax0.set_xlim(0, 1)
        ax0.set_ylim(0, max(8, float(np.nanmax(prior_pdf)) * 1.10))
        add_note(ax0, f"hyperparameters\nα=mκ={alpha:.2f}\nβ=(1-m)κ={beta:.2f}\nm={m:.2f}\nκ={kappa:.1f}", loc=(0.03, 0.80))
        ax0.legend(loc="lower right", frameon=True)

        ax1.scatter(x_pos, obs, s=70, color="0.35", alpha=0.75, label="観測比率 y_j/n_j")
        ax1.vlines(x_pos, lo, hi, color="#DD8452", lw=5, alpha=0.45, label="p_j 事後90%区間")
        ax1.scatter(x_pos, post_mean, s=95, color="#C44E52", edgecolor="white", linewidth=1.0, zorder=4, label="p_j 事後平均")
        ax1.axhline(m, color="#4C72B0", ls="--", lw=1.5, label="母集団中心 m")
        ax1.set_xticks(x_pos, labels, rotation=25, ha="right")
        ax1.set_ylim(-0.05, 1.05)
        ax1.set_title("下の階層: y_j ~ Binomial(n_j, p_j)")
        ax1.set_xlabel("day-time group")
        ax1.set_ylabel("smoker rate")
        add_note(ax1, f"step {t}/{len(states)-1}\n黒点: 観測値\n赤点: 階層推定\n平均90%幅={widths[-1]:.2f}", loc=(0.03, 0.40), fontsize=8)
        ax1.legend(loc="upper right", fontsize=8, frameon=True)
        frames.append(fig_to_frame(fig))
        plt.close(fig)

    print(f"beta-binomial posterior width: first={widths[0]:.3f}, middle={widths[len(widths)//2]:.3f}, last={widths[-1]:.3f}")
    print(f"beta-binomial fitted hyperparams: m={mle_m:.3f}, kappa={mle_kappa:.2f}")
    return save_gif(frames, GIF_DIR / "11_beta_binomial_hyperparameters.gif", fps=9)


gif_11 = make_beta_binomial_hyperparameter_gif()
gif_11
"""))

cells.append(nbf.v4.new_markdown_cell(r"""## 2. Gamma-Poisson: 「カウント平均 $\lambda_j$」の上に Gamma 分布を置く

`tips.csv` の曜日 × 昼夜グループごとに、テーブル人数 `size` の平均を考えます。

$$
y_j = \sum_i y_{ij} \sim \mathrm{Poisson}(E_j \lambda_j)
$$

ここで $E_j$ はテーブル数、$\lambda_j$ はそのグループの平均人数です。

さらに、

$$
\lambda_j \sim \mathrm{Gamma}(a, b)
$$

と置きます。平均 $m=a/b$、集中度 $\kappa=b$ と書けば、

$$
a=m\kappa, \quad b=\kappa
$$

です。

- $\lambda_j$: 尤度のパラメータ。
- $m,\kappa$: $\lambda_j$ の分布を決めるハイパーパラメータ。
"""))

cells.append(nbf.v4.new_code_cell(r"""def prepare_gamma_poisson_data() -> pd.DataFrame:
    df = tips[["day", "time", "size"]].dropna().copy()
    df["group"] = df["day"].astype(str) + "-" + df["time"].astype(str)
    agg = df.groupby("group")["size"].agg(total_y="sum", exposure="count", mean_size="mean").reset_index()
    agg = agg[agg["exposure"] >= 5].sort_values("group").reset_index(drop=True)
    return agg


def gamma_poisson_nll(params: np.ndarray, y: np.ndarray, exposure: np.ndarray) -> float:
    m = np.exp(params[0])
    kappa = np.exp(params[1])
    a = max(m * kappa, 1e-8)
    b = max(kappa, 1e-8)
    # Marginal likelihood after integrating lambda: Gamma-Poisson / NB form. log choose-like y! omitted partly? include terms dependent on exposure.
    ll = np.sum(
        gammaln(y + a) - gammaln(a) - gammaln(y + 1)
        + a * np.log(b) + y * np.log(exposure) - (y + a) * np.log(b + exposure)
    )
    return float(-ll)


def fit_gamma_poisson_hyperparams(agg: pd.DataFrame) -> tuple[float, float]:
    y = agg["total_y"].to_numpy(float)
    e = agg["exposure"].to_numpy(float)
    start_m = np.sum(y) / np.sum(e)
    res = minimize(gamma_poisson_nll, x0=np.array([np.log(start_m), np.log(12.0)]), args=(y, e), method="Nelder-Mead")
    return float(np.exp(res.x[0])), float(np.exp(res.x[1]))


def make_gamma_poisson_hyperparameter_gif() -> Path:
    agg = prepare_gamma_poisson_data()
    y = agg["total_y"].to_numpy(float)
    e = agg["exposure"].to_numpy(float)
    obs = agg["mean_size"].to_numpy(float)
    mle_m, mle_kappa_raw = fit_gamma_poisson_hyperparams(agg)
    # このデータではグループ間の人数平均がかなり似ているため、周辺尤度の最適化は
    # κ→非常に大きい（ほぼ完全プーリング）へ行きやすい。可視化では動きが見えるように
    # κを適度に capped した経験ベイズ的な到達点を使う。
    mle_kappa = min(mle_kappa_raw, 18.0)
    start = np.array([float(obs.mean() * 0.75), 80.0])
    target = np.array([mle_m, mle_kappa])
    states = interpolate(start, target, 56)
    xgrid = np.linspace(0.01, max(8, obs.max() + 2.0), 400)
    x_pos = np.arange(len(agg))
    labels = agg["group"].tolist()
    widths = []
    frames = []

    for t, (m, kappa) in enumerate(states):
        a = m * kappa
        b = kappa
        post_a = a + y
        post_b = b + e
        post_mean = post_a / post_b
        lo = gamma_dist.ppf(0.05, a=post_a, scale=1 / post_b)
        hi = gamma_dist.ppf(0.95, a=post_a, scale=1 / post_b)
        widths.append(float(np.mean(hi - lo)))

        fig, axes = plt.subplots(1, 2, figsize=(12, 5.1), constrained_layout=True, gridspec_kw={"width_ratios": [1.0, 1.35]})
        ax0, ax1 = axes
        prior_pdf = gamma_dist.pdf(xgrid, a=a, scale=1 / b)
        ax0.plot(xgrid, prior_pdf, color="#4C72B0", lw=2.8, label="λ_j の母集団分布")
        ax0.axvline(m, color="#C44E52", ls="--", lw=1.8, label="平均 m")
        ax0.set_title("上の階層: λ_j ~ Gamma(a, b)")
        ax0.set_xlabel("グループ平均人数 λ_j")
        ax0.set_ylabel("density")
        ax0.set_xlim(xgrid.min(), xgrid.max())
        ax0.set_ylim(0, max(2, float(np.nanmax(prior_pdf)) * 1.10))
        add_note(ax0, f"hyperparameters\na=mκ={a:.2f}\nb=κ={b:.2f}\nm=a/b={m:.2f}\nκ={kappa:.1f}", loc=(0.03, 0.80))
        ax0.legend(loc="lower right", frameon=True)

        ax1.scatter(x_pos, obs, s=70, color="0.35", alpha=0.75, label="観測平均 y_j/E_j")
        ax1.vlines(x_pos, lo, hi, color="#55A868", lw=5, alpha=0.45, label="λ_j 事後90%区間")
        ax1.scatter(x_pos, post_mean, s=95, color="#2C7F4F", edgecolor="white", linewidth=1.0, zorder=4, label="λ_j 事後平均")
        ax1.axhline(m, color="#4C72B0", ls="--", lw=1.5, label="母集団平均 m")
        ax1.set_xticks(x_pos, labels, rotation=25, ha="right")
        ax1.set_ylim(0, max(8, obs.max() + 2))
        ax1.set_title("下の階層: y_j ~ Poisson(E_j λ_j)")
        ax1.set_xlabel("day-time group")
        ax1.set_ylabel("mean party size")
        add_note(ax1, f"step {t}/{len(states)-1}\n黒点: 観測平均\n緑点: 階層推定\n平均90%幅={widths[-1]:.2f}", loc=(0.03, 0.40), fontsize=8)
        ax1.legend(loc="upper right", fontsize=8, frameon=True)
        frames.append(fig_to_frame(fig))
        plt.close(fig)

    print(f"gamma-poisson posterior width: first={widths[0]:.3f}, middle={widths[len(widths)//2]:.3f}, last={widths[-1]:.3f}")
    print(f"gamma-poisson fitted hyperparams: m={mle_m:.3f}, kappa_raw={mle_kappa_raw:.2f}, kappa_visualized={mle_kappa:.2f}")
    return save_gif(frames, GIF_DIR / "12_gamma_poisson_hyperparameters.gif", fps=9)


gif_12 = make_gamma_poisson_hyperparameter_gif()
gif_12
"""))

cells.append(nbf.v4.new_markdown_cell(r"""## 3. Normal-Normal: 「グループ平均 $\mu_j$」の上に Normal($\mu_0,\tau$) を置く

`penguins.csv` の体重 `body_mass_g` を、`species × sex` グループで見ます。

$$
y_{ij} \sim \mathcal{N}(\mu_j, \sigma^2)
$$

$$
\mu_j \sim \mathcal{N}(\mu_0, \tau^2)
$$

- $\mu_j$: 観測データの平均を決める尤度パラメータ。
- $\mu_0$: グループ平均たちの中心。
- $\tau$: グループ平均たちがどれくらい散らばるか。

$\tau$ が小さいと、全グループ平均はほぼ $\mu_0$ に集まります。$\tau$ が大きいと、各グループの観測平均に近づきます。
"""))

cells.append(nbf.v4.new_code_cell(r"""def prepare_normal_normal_data() -> pd.DataFrame:
    df = penguins[["species", "sex", "body_mass_g"]].dropna().copy()
    df["sex"] = df["sex"].astype(str).str.upper()
    df = df[df["sex"].isin(["MALE", "FEMALE"])]
    df["group"] = df["species"].astype(str) + "-" + df["sex"].astype(str)
    agg = df.groupby("group")["body_mass_g"].agg(mean="mean", n="count", sd="std").reset_index()
    agg = agg[agg["n"] >= 5].sort_values("group").reset_index(drop=True)
    return df, agg


def make_normal_normal_hyperparameter_gif() -> Path:
    df, agg = prepare_normal_normal_data()
    groups = agg["group"].tolist()
    group_mean = agg["mean"].to_numpy(float)
    n = agg["n"].to_numpy(float)
    sigma = float(df.groupby("group")["body_mass_g"].std().mean())
    se = sigma / np.sqrt(n)
    mu0 = float(df["body_mass_g"].mean())
    tau_target = float(np.sqrt(max(np.var(group_mean, ddof=1) - np.mean(se**2), 1.0)))
    # Linear tau spacing made the latter half visually almost static, especially for
    # Chinstrap groups.  Instead, create many candidate tau values and resample them
    # by equal displacement of the posterior means; this keeps every frame changing.
    tau_candidates = np.geomspace(1.0, tau_target, 700)

    def posterior_mean_for_tau(tau: float) -> np.ndarray:
        data_prec = 1 / (se**2)
        prior_prec = 1 / (tau**2)
        post_var = 1 / (data_prec + prior_prec)
        return post_var * (data_prec * group_mean + prior_prec * mu0)

    candidate_means = np.vstack([posterior_mean_for_tau(float(tau)) for tau in tau_candidates])
    displacement = np.r_[0.0, np.cumsum(np.linalg.norm(np.diff(candidate_means, axis=0), axis=1))]
    if displacement[-1] > 0:
        tau_states = np.interp(np.linspace(0, displacement[-1], 46), displacement, tau_candidates)
    else:
        tau_states = np.linspace(1.0, tau_target, 46)
    xgrid = np.linspace(df["body_mass_g"].min() - 500, df["body_mass_g"].max() + 500, 500)
    x_pos = np.arange(len(groups))
    widths = []
    frames = []
    palette = sns.color_palette("Set2", n_colors=len(groups))

    for t, tau in enumerate(tau_states):
        data_prec = 1 / (se**2)
        prior_prec = 1 / (tau**2)
        post_var = 1 / (data_prec + prior_prec)
        post_mean = post_var * (data_prec * group_mean + prior_prec * mu0)
        post_sd = np.sqrt(post_var)
        lo = post_mean - 1.64 * post_sd
        hi = post_mean + 1.64 * post_sd
        widths.append(float(np.mean(hi - lo)))
        prior_pdf = norm.pdf(xgrid, loc=mu0, scale=tau)

        fig, axes = plt.subplots(1, 2, figsize=(12.2, 5.2), constrained_layout=True, gridspec_kw={"width_ratios": [1.0, 1.45]})
        ax0, ax1 = axes
        ax0.plot(xgrid, prior_pdf, color="#4C72B0", lw=2.8, label="μ_j の母集団分布")
        ax0.axvline(mu0, color="#C44E52", ls="--", lw=1.8, label="中心 μ0")
        ax0.set_title("上の階層: μ_j ~ Normal(μ0, τ²)")
        ax0.set_xlabel("グループ平均 μ_j")
        ax0.set_ylabel("density")
        ax0.set_xlim(xgrid.min(), xgrid.max())
        ax0.set_ylim(0, max(0.004, float(np.nanmax(prior_pdf)) * 1.12))
        add_note(ax0, f"hyperparameters\nμ0={mu0:,.0f} g\nτ={tau:,.0f} g\nτが小さいほど\n全体平均へ強く縮む", loc=(0.03, 0.80), fontsize=8)
        ax0.legend(loc="lower right", frameon=True)

        for j, g in enumerate(groups):
            vals = df.loc[df["group"] == g, "body_mass_g"].to_numpy(float)
            xj = RNG.normal(j, 0.045, size=len(vals))
            ax1.scatter(xj, vals, s=17, alpha=0.20, color=palette[j], edgecolor="none")
            ax1.plot([j - 0.25, j + 0.25], [group_mean[j], group_mean[j]], color=palette[j], lw=1.4, ls=":", label="観測群平均" if j == 0 else None)
            ax1.vlines(j, lo[j], hi[j], color="#C44E52", lw=4, alpha=0.48)
            ax1.scatter(j, post_mean[j], s=88, color="#C44E52", edgecolor="white", linewidth=1.0, zorder=4, label="μ_j 事後平均" if j == 0 else None)
        ax1.axhline(mu0, color="0.25", lw=1.6, ls="--", label="全体平均 μ0")
        ax1.set_xticks(x_pos, groups, rotation=24, ha="right")
        ax1.set_title("下の階層: y_ij ~ Normal(μ_j, σ²)")
        ax1.set_xlabel("species-sex group")
        ax1.set_ylabel("body_mass_g")
        ax1.set_ylim(df["body_mass_g"].min() - 350, df["body_mass_g"].max() + 350)
        add_note(ax1, f"step {t}/{len(tau_states)-1}\n赤点: 階層推定 μ_j\n赤線: μ_j の90%区間\n平均90%幅={widths[-1]:.1f} g", loc=(0.03, 0.38), fontsize=8)
        ax1.legend(loc="upper right", fontsize=8, frameon=True)
        frames.append(fig_to_frame(fig))
        plt.close(fig)

    print(f"normal-normal posterior width: first={widths[0]:.2f}, middle={widths[len(widths)//2]:.2f}, last={widths[-1]:.2f}")
    print(f"normal-normal hyperparams: mu0={mu0:.1f}, tau_target={tau_target:.1f}, sigma={sigma:.1f}")
    return save_gif(frames, GIF_DIR / "13_normal_normal_hyperparameters.gif", fps=9)


gif_13 = make_normal_normal_hyperparameter_gif()
gif_13
"""))

cells.append(nbf.v4.new_markdown_cell(r"""## 4. ハイパーパラメータを尤度で推定する: marginal likelihood の地形

上の Beta-Binomial では、$p_j$ を積分消去すると、ハイパーパラメータ $(m,\kappa)$ だけの周辺尤度になります。

$$
p(y_j \mid n_j, m,\kappa)
= \int p(y_j \mid n_j, p_j) p(p_j \mid m,\kappa) dp_j
$$

この GIF では、$(m,\kappa)$ の負の対数周辺尤度の地形を描き、最適値へ向かう様子を重ねます。

ポイント:

- $p_j$ はデータの尤度パラメータ。
- $m,\kappa$ は $p_j$ の分布のパラメータ。
- 階層モデルでは、この上位パラメータもデータから推定できる。
"""))

cells.append(nbf.v4.new_code_cell(r"""def make_hyperlikelihood_surface_gif() -> Path:
    agg = prepare_beta_binomial_data()
    y = agg["y"].to_numpy(float)
    n = agg["n"].to_numpy(float)
    mle_m, mle_kappa = fit_beta_binomial_hyperparams(agg)

    m_grid = np.linspace(0.08, 0.85, 130)
    logk_grid = np.linspace(np.log(1.2), np.log(180), 130)
    M, LK = np.meshgrid(m_grid, logk_grid)
    Z = np.zeros_like(M)
    for i in range(M.shape[0]):
        for j in range(M.shape[1]):
            Z[i, j] = beta_binomial_nll(np.array([logit(M[i, j]), LK[i, j]]), y, n)
    Z = Z - np.nanmin(Z)
    Z_clip = np.clip(Z, 0, np.quantile(Z, 0.92))

    start = np.array([0.50, 80.0])
    target = np.array([mle_m, mle_kappa])
    states = interpolate(start, target, 56)
    frames = []
    for t, (m, kappa) in enumerate(states):
        fig, ax = plt.subplots(figsize=(8.6, 5.8), constrained_layout=True)
        cs = ax.contourf(M, np.exp(LK), Z_clip, levels=24, cmap="viridis")
        ax.contour(M, np.exp(LK), Z, levels=12, colors="white", linewidths=0.45, alpha=0.55)
        path_m = [s[0] for s in states[: t + 1]]
        path_k = [s[1] for s in states[: t + 1]]
        ax.plot(path_m, path_k, color="#C44E52", lw=2.3, label="探索パス")
        ax.scatter([m], [kappa], s=95, color="#C44E52", edgecolor="white", linewidth=1.0, zorder=5, label="現在の(m,κ)")
        ax.scatter([mle_m], [mle_kappa], s=95, color="gold", edgecolor="black", linewidth=0.8, zorder=5, label="周辺尤度の最小付近")
        ax.set_yscale("log")
        ax.set_xlabel("m: p_j の母集団中心")
        ax.set_ylabel("κ: p_j の集中度")
        ax.set_title("4. Beta-Binomial のハイパーパラメータ尤度地形")
        add_note(ax, f"step {t}/{len(states)-1}\nNLL-min={beta_binomial_nll(np.array([logit(m), np.log(kappa)]), y, n) - np.nanmin(Z):.2f}\nα={m*kappa:.2f}\nβ={(1-m)*kappa:.2f}", loc=(0.03, 0.28), fontsize=8)
        ax.legend(loc="upper right", frameon=True)
        cbar = fig.colorbar(cs, ax=ax, shrink=0.86)
        cbar.set_label("relative negative marginal log likelihood")
        frames.append(fig_to_frame(fig))
        plt.close(fig)

    return save_gif(frames, GIF_DIR / "14_hyperparameter_likelihood_surface.gif", fps=9)


gif_14 = make_hyperlikelihood_surface_gif()
gif_14
"""))

cells.append(nbf.v4.new_markdown_cell(r"""## 5. 作成した GIF をまとめて表示

どの GIF も、観測データは固定し、上位パラメータが変わることで下位パラメータ推定がどう動くかを表します。
"""))

cells.append(nbf.v4.new_code_cell(r"""from IPython.display import HTML, display

items = [
    ("Beta-Binomial: p_j の上に Beta(α,β)", gif_11),
    ("Gamma-Poisson: λ_j の上に Gamma(a,b)", gif_12),
    ("Normal-Normal: μ_j の上に Normal(μ0,τ²)", gif_13),
    ("Hyper-likelihood surface: (m,κ) を推定する", gif_14),
]
html = ["<div style='display:grid; grid-template-columns: 1fr; gap: 24px;'>"]
for title, path in items:
    rel = path.relative_to(PROJECT_ROOT).as_posix()
    html.append(
        f"<section><h3>{title}</h3><p><code>{rel}</code></p>"
        f"<img src='../{rel}' style='max-width: 960px; width: 100%; border:1px solid #ddd;'>"
        f"</section>"
    )
html.append("</div>")
display(HTML("\n".join(html)))
"""))

cells.append(nbf.v4.new_code_cell(r"""# 6. Contact sheet for quick verification
from PIL import Image, ImageDraw


def read_gif_frame(path: Path, frame_index: int) -> Image.Image:
    reader = imageio.get_reader(path)
    try:
        n = reader.get_length()
        idx = min(max(frame_index, 0), n - 1)
        arr = reader.get_data(idx)
    finally:
        reader.close()
    return Image.fromarray(arr).convert("RGB")


def make_contact_sheet(gif_paths: list[Path], output_path: Path) -> Path:
    labels = ["first", "middle", "final"]
    cell_w, cell_h = 410, 285
    sheet = Image.new("RGB", (cell_w * 3, cell_h * len(gif_paths)), "white")
    draw = ImageDraw.Draw(sheet)
    for r, path in enumerate(gif_paths):
        reader = imageio.get_reader(path)
        try:
            n = reader.get_length()
        finally:
            reader.close()
        for c, idx in enumerate([0, n // 2, n - 1]):
            im = read_gif_frame(path, idx)
            im.thumbnail((380, 230))
            x = c * cell_w + 15
            y = r * cell_h + 42
            draw.text((x, r * cell_h + 8), f"{path.name}\n{labels[c]}: frame {idx}", fill=(20, 20, 20))
            sheet.paste(im, (x, y))
    output_path.parent.mkdir(parents=True, exist_ok=True)
    sheet.save(output_path)
    print(f"saved {output_path}")
    return output_path


contact_sheet = make_contact_sheet([gif_11, gif_12, gif_13, gif_14], FIG_DIR / "hyperparameter_likelihood_contact_sheet.png")
contact_sheet
"""))

cells.append(nbf.v4.new_markdown_cell(r"""## 6. まとめ

「パラメータのパラメータ」は、以下のように読むと整理しやすい。

| モデル | 観測尤度のパラメータ | そのパラメータの分布 | ハイパーパラメータ |
|---|---|---|---|
| Beta-Binomial | グループ確率 $p_j$ | $p_j \sim \mathrm{Beta}(\alpha,\beta)$ | $m,\kappa$ または $\alpha,\beta$ |
| Gamma-Poisson | グループ平均 $\lambda_j$ | $\lambda_j \sim \mathrm{Gamma}(a,b)$ | $m,\kappa$ または $a,b$ |
| Normal-Normal | グループ平均 $\mu_j$ | $\mu_j \sim \mathcal{N}(\mu_0,\tau^2)$ | $\mu_0,\tau$ |

重要な直感:

1. ハイパーパラメータは「下位パラメータたちの母集団」を決める。
2. 下位パラメータは、観測データだけでなく、その母集団分布からも情報を借りる。
3. その結果、小さいグループやノイズの大きいグループほど全体側へ縮む。
4. ハイパーパラメータ自体も、周辺尤度やベイズ推論でデータから推定できる。
"""))

nb["cells"] = cells
nbf.write(nb, NOTEBOOK_PATH)
print(NOTEBOOK_PATH)
