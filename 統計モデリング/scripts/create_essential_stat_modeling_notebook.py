from __future__ import annotations

from pathlib import Path

import nbformat as nbf

ROOT = Path(__file__).resolve().parents[1]
NOTEBOOK_PATH = ROOT / "notebooks" / "003_essential_statistical_modeling_gifs.ipynb"
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

cells.append(nbf.v4.new_markdown_cell(r"""# 統計マンが知っておきたい統計モデリングの動き：GLM・過分散・階層モデルGIF

- **目的**: 緑本（久保『データ解析のための統計モデリング入門』）で重要になる GLM と、発展として必須になる階層モデル/部分プーリングを、固定データに対する推論・収縮の動きとして GIF 化する。
- **作成環境**: `D:/dev/dev_statistics/venv` の venv kernel (`Python (dev_statistics venv)`)。
- **データ**: 教育用に生成した合成データを `data/simulated/essential_stat_modeling_demo.csv` に保存してから読み込む。外部 URL には依存しない。
- **作成物**:
  - `outputs/gifs/07_poisson_glm_fit.gif`
  - `outputs/gifs/08_logistic_glm_fit.gif`
  - `outputs/gifs/09_negative_binomial_overdispersion_fit.gif`
  - `outputs/gifs/10_hierarchical_normal_partial_pooling.gif`
  - `outputs/gifs/11_hierarchical_varying_slope_regression.gif`
"""))

cells.append(nbf.v4.new_markdown_cell(r"""## 0. どの手法を押さえるべきか

緑本や代表的な統計モデリングの流れで、まず可視化して理解したいものは次の順番。

| レベル | 手法 | 何を理解するか | このノートの可視化 |
|---|---|---|---|
| 1 | 正規分布・線形回帰 | 連続量を平均・分散・直線で説明する | 前ノート `001`, `002` |
| 2 | **GLM: Poisson 回帰** | カウントデータを $\log \lambda = X\beta$ で扱う。平均は正になる | GIF 07 |
| 3 | **GLM: ロジスティック回帰** | 0/1・成功確率を $\mathrm{logit}^{-1}(X\beta)$ で扱う | GIF 08 |
| 4 | **過分散と負の二項分布** | Poisson の「平均=分散」が破れるとき、ばらつきを別パラメータで持つ | GIF 09 |
| 5 | **階層モデル/ランダム効果** | 群ごとの推定値を、全体平均へ適度に縮める部分プーリング | GIF 10 |
| 6 | **階層回帰/ varying intercept & slope** | 群ごとに切片・傾きを持たせつつ、データが少ない群は全体傾向へ寄せる | GIF 11 |

このノートでは MCMC そのものではなく、**「尤度・正則化・経験ベイズ的な収縮が、図の上でどう見えるか」**を重視する。ベイズ階層モデルとして本格的に推定する場合は Stan/PyMC で同じ構造を事後分布として推定する。

参考:
- 久保拓弥『データ解析のための統計モデリング入門』著者サポートページ: https://kuboweb.github.io/-kubo/ce/IwanamiBook.html
- Stan User's Guide: https://mc-stan.org/docs/stan-users-guide/index.html
- statsmodels GLM documentation: https://www.statsmodels.org/stable/glm.html
"""))

cells.append(nbf.v4.new_code_cell(r"""# 1. Imports / paths / theme
from __future__ import annotations

import json
import math
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
from scipy.special import expit, gammaln
from scipy.stats import norm

warnings.filterwarnings("ignore", category=RuntimeWarning)
warnings.filterwarnings("ignore", category=UserWarning)

sns.set_theme(style="whitegrid", palette="muted", font_scale=1.0)
japanize_matplotlib.japanize()
plt.rcParams["figure.dpi"] = 110
plt.rcParams["savefig.dpi"] = 120
plt.rcParams["axes.unicode_minus"] = False

PROJECT_ROOT = Path.cwd()
if PROJECT_ROOT.name == "notebooks":
    PROJECT_ROOT = PROJECT_ROOT.parent

DATA_DIR = PROJECT_ROOT / "data" / "simulated"
GIF_DIR = PROJECT_ROOT / "outputs" / "gifs"
FIG_DIR = PROJECT_ROOT / "outputs" / "figures"
for path in [DATA_DIR, GIF_DIR, FIG_DIR]:
    path.mkdir(parents=True, exist_ok=True)

RNG = np.random.default_rng(20260620)
print(f"PROJECT_ROOT = {PROJECT_ROOT}")
print(f"DATA_DIR     = {DATA_DIR.relative_to(PROJECT_ROOT)}")
print(f"GIF_DIR      = {GIF_DIR.relative_to(PROJECT_ROOT)}")
"""))

cells.append(nbf.v4.new_code_cell(r"""# 2. Create/load local synthetic educational data
DATA_PATH = DATA_DIR / "essential_stat_modeling_demo.csv"
META_PATH = DATA_DIR / "essential_stat_modeling_demo_meta.json"


def make_demo_data(seed: int = 20260620) -> pd.DataFrame:
    rng = np.random.default_rng(seed)
    rows = []

    # A. Poisson GLM: counts with exposure
    n = 90
    x = rng.uniform(-2.2, 2.2, n)
    exposure = rng.uniform(0.6, 1.8, n)
    eta = 0.45 + 0.75 * x + np.log(exposure)
    y = rng.poisson(np.exp(eta))
    rows += [
        {"dataset": "poisson_glm", "group": "all", "x": xi, "y": yi, "exposure": ei}
        for xi, yi, ei in zip(x, y, exposure)
    ]

    # B. Logistic GLM: binary response
    n = 120
    x = rng.uniform(-3.0, 3.0, n)
    p = expit(-0.25 + 1.25 * x)
    y = rng.binomial(1, p)
    rows += [
        {"dataset": "logistic_glm", "group": "all", "x": xi, "y": yi, "exposure": np.nan}
        for xi, yi in zip(x, y)
    ]

    # C. Negative-binomial overdispersed count distribution
    n = 260
    mu, alpha = 5.2, 0.75
    r = 1.0 / alpha
    p_nb = r / (r + mu)
    y = rng.negative_binomial(r, p_nb, n)
    rows += [
        {"dataset": "neg_binom", "group": "all", "x": np.nan, "y": yi, "exposure": np.nan}
        for yi in y
    ]

    # D. Hierarchical normal: many groups with uneven sample sizes
    group_sizes = [4, 6, 8, 10, 14, 18, 26, 38]
    mu0, tau, sigma = 55.0, 8.0, 6.0
    for g, n_g in enumerate(group_sizes):
        theta_g = rng.normal(mu0, tau)
        y = rng.normal(theta_g, sigma, n_g)
        rows += [
            {"dataset": "hier_normal", "group": f"G{g+1}", "x": np.nan, "y": yi, "exposure": np.nan}
            for yi in y
        ]

    # E. Hierarchical regression: varying intercept and slope, uneven groups
    group_sizes = [5, 7, 9, 13, 20, 34]
    base_a, base_b = 2.0, 1.35
    for g, n_g in enumerate(group_sizes):
        a_g = rng.normal(base_a, 1.1)
        b_g = rng.normal(base_b, 0.55)
        x = rng.uniform(-2.5, 2.5, n_g)
        y = a_g + b_g * x + rng.normal(0, 0.9, n_g)
        rows += [
            {"dataset": "hier_regression", "group": f"R{g+1}", "x": xi, "y": yi, "exposure": np.nan}
            for xi, yi in zip(x, y)
        ]

    return pd.DataFrame(rows)


if not DATA_PATH.exists():
    demo = make_demo_data()
    demo.to_csv(DATA_PATH, index=False)
    META_PATH.write_text(
        json.dumps(
            {
                "description": "Synthetic educational data for GLM, overdispersion, and hierarchical modeling visualizations.",
                "seed": 20260620,
                "note": "Generated locally; not public/PII data.",
            },
            ensure_ascii=False,
            indent=2,
        ),
        encoding="utf-8",
    )
else:
    demo = pd.read_csv(DATA_PATH)

print(f"loaded: {DATA_PATH.relative_to(PROJECT_ROOT).as_posix()} {demo.shape}")
print(demo.groupby("dataset").size())
"""))

cells.append(nbf.v4.new_code_cell(r"""# 3. Shared helpers

def fig_to_frame(fig: matplotlib.figure.Figure) -> np.ndarray:
    fig.canvas.draw()
    rgba = np.asarray(fig.canvas.buffer_rgba())
    return rgba[:, :, :3].copy()


def save_gif(frames: list[np.ndarray], path: Path, fps: int = 8) -> Path:
    path.parent.mkdir(parents=True, exist_ok=True)
    imageio.mimsave(path, frames, duration=1 / fps, loop=0)
    print(f"saved {path.relative_to(PROJECT_ROOT)} ({len(frames)} frames, {fps} fps)")
    return path


def add_note(ax: plt.Axes, text: str, loc: tuple[float, float] = (0.02, 0.98)) -> None:
    ax.text(
        loc[0], loc[1], text,
        transform=ax.transAxes, va="top", ha="left", fontsize=9,
        bbox={"boxstyle": "round,pad=0.35", "fc": "white", "ec": "0.7", "alpha": 0.92},
    )


def adam_trace(theta0: np.ndarray, loss_grad_fn, n_iter: int = 45, lr: float = 0.08) -> list[tuple[np.ndarray, float]]:
    theta = np.array(theta0, dtype=float)
    m = np.zeros_like(theta)
    v = np.zeros_like(theta)
    beta1, beta2, eps = 0.9, 0.999, 1e-8
    trace: list[tuple[np.ndarray, float]] = []
    for t in range(n_iter + 1):
        loss, grad = loss_grad_fn(theta)
        trace.append((theta.copy(), float(loss)))
        m = beta1 * m + (1 - beta1) * grad
        v = beta2 * v + (1 - beta2) * (grad**2)
        mh = m / (1 - beta1 ** (t + 1))
        vh = v / (1 - beta2 ** (t + 1))
        theta = theta - lr * mh / (np.sqrt(vh) + eps)
    return trace


def finite_diff_grad(loss_fn, theta: np.ndarray, eps: float = 1e-4) -> np.ndarray:
    grad = np.zeros_like(theta, dtype=float)
    for j in range(len(theta)):
        step = np.zeros_like(theta, dtype=float)
        step[j] = eps
        grad[j] = (loss_fn(theta + step) - loss_fn(theta - step)) / (2 * eps)
    return grad
"""))

cells.append(nbf.v4.new_markdown_cell(r"""## 1. GLM: Poisson 回帰

カウントデータでは平均 $\lambda$ が負になってはいけないので、線形予測子をそのまま平均にせず、

$$
 y_i \sim \mathrm{Poisson}(\lambda_i),\quad
 \log \lambda_i = \alpha + \beta x_i + \log(\mathrm{exposure}_i)
$$

のように **log link** を使う。ここでは Adam による最尤推定の各 step を描く。
"""))

cells.append(nbf.v4.new_code_cell(r"""def poisson_loss_grad_factory(x: np.ndarray, y: np.ndarray, exposure: np.ndarray):
    def loss_grad(theta: np.ndarray) -> tuple[float, np.ndarray]:
        a, b = theta
        eta = a + b * x + np.log(exposure)
        lam = np.exp(np.clip(eta, -20, 20))
        loss = float(np.mean(lam - y * eta))
        grad = np.array([np.mean(lam - y), np.mean((lam - y) * x)], dtype=float)
        return loss, grad
    return loss_grad


def make_poisson_glm_gif() -> Path:
    df = demo.query("dataset == 'poisson_glm'").copy()
    x = df["x"].to_numpy(float)
    y = df["y"].to_numpy(float)
    exposure = df["exposure"].to_numpy(float)
    grid = np.linspace(x.min() - 0.2, x.max() + 0.2, 220)
    n_iter = 45
    trace = adam_trace(np.array([-1.4, -0.8]), poisson_loss_grad_factory(x, y, exposure), n_iter=n_iter, lr=0.09)

    # bootstrap traces for per-step 90% bands at exposure=1
    rng = np.random.default_rng(707)
    pred_by_iter = [[] for _ in range(n_iter + 1)]
    for _ in range(70):
        idx = rng.integers(0, len(x), len(x))
        tr = adam_trace(np.array([-1.4, -0.8]), poisson_loss_grad_factory(x[idx], y[idx], exposure[idx]), n_iter=n_iter, lr=0.09)
        for t, (theta, _loss) in enumerate(tr):
            pred_by_iter[t].append(np.exp(theta[0] + theta[1] * grid))
    bands = [(np.quantile(np.vstack(p), 0.05, axis=0), np.mean(np.vstack(p), axis=0), np.quantile(np.vstack(p), 0.95, axis=0)) for p in pred_by_iter]
    widths = [float(np.mean(hi - lo)) for lo, _m, hi in bands]
    print(f"Poisson band width: first={widths[0]:.2f}, middle={widths[len(widths)//2]:.2f}, last={widths[-1]:.2f}")

    frames = []
    for t, (theta, loss) in enumerate(trace):
        a, b = theta
        mu = np.exp(a + b * grid)
        lo, mid, hi = bands[t]
        fig, ax = plt.subplots(figsize=(8.8, 5.2), constrained_layout=True)
        ax.scatter(x, y / exposure, s=42, color="#4C72B0", alpha=0.75, edgecolor="white", linewidth=0.35, label="固定データ: count/exposure")
        ax.fill_between(grid, lo, hi, color="#4C72B0", alpha=0.18, label="このstepの90%帯")
        ax.plot(grid, mu, color="#1f4e79", lw=2.8, label="現在の $E[y|x, exposure=1]$")
        ax.set_title("07. Poisson GLM: log link でカウント平均をフィット")
        ax.set_xlabel("x")
        ax.set_ylabel("count / exposure")
        ax.set_xlim(grid.min(), grid.max())
        ax.set_ylim(bottom=0)
        add_note(ax, f"step {t}/{n_iter}\nlog λ = α + βx + log exposure\nα={a:.2f}, β={b:.2f}\nNLL/obs={loss:.3f}\n90%帯平均幅={widths[t]:.2f}")
        ax.legend(loc="upper left", frameon=True)
        frames.append(fig_to_frame(fig)); plt.close(fig)
    return save_gif(frames, GIF_DIR / "07_poisson_glm_fit.gif", fps=9)


gif_07 = make_poisson_glm_gif()
gif_07
"""))

cells.append(nbf.v4.new_markdown_cell(r"""## 2. GLM: ロジスティック回帰

0/1 データや成功/失敗データでは、予測値は $0$ から $1$ の確率でなければならない。

$$
 y_i \sim \mathrm{Bernoulli}(p_i),\quad
 \mathrm{logit}(p_i)=\log\frac{p_i}{1-p_i}=\alpha+\beta x_i
$$

S字曲線が、固定された 0/1 データの成功確率に沿っていく様子を見る。
"""))

cells.append(nbf.v4.new_code_cell(r"""def logistic_loss_grad_factory(x: np.ndarray, y: np.ndarray):
    def loss_grad(theta: np.ndarray) -> tuple[float, np.ndarray]:
        a, b = theta
        eta = a + b * x
        p = expit(eta)
        loss = float(np.mean(np.logaddexp(0, eta) - y * eta))
        grad = np.array([np.mean(p - y), np.mean((p - y) * x)], dtype=float)
        return loss, grad
    return loss_grad


def binned_rate(x: np.ndarray, y: np.ndarray, bins: np.ndarray) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    centers, rates, sizes = [], [], []
    for lo, hi in zip(bins[:-1], bins[1:]):
        mask = (x >= lo) & (x < hi)
        if mask.sum() > 0:
            centers.append((lo + hi) / 2)
            rates.append(y[mask].mean())
            sizes.append(mask.sum())
    return np.array(centers), np.array(rates), np.array(sizes)


def make_logistic_glm_gif() -> Path:
    df = demo.query("dataset == 'logistic_glm'").copy()
    x = df["x"].to_numpy(float)
    y = df["y"].to_numpy(float)
    grid = np.linspace(x.min() - 0.3, x.max() + 0.3, 240)
    n_iter = 45
    trace = adam_trace(np.array([1.4, -1.0]), logistic_loss_grad_factory(x, y), n_iter=n_iter, lr=0.10)

    rng = np.random.default_rng(808)
    pred_by_iter = [[] for _ in range(n_iter + 1)]
    for _ in range(80):
        idx = rng.integers(0, len(x), len(x))
        tr = adam_trace(np.array([1.4, -1.0]), logistic_loss_grad_factory(x[idx], y[idx]), n_iter=n_iter, lr=0.10)
        for t, (theta, _loss) in enumerate(tr):
            pred_by_iter[t].append(expit(theta[0] + theta[1] * grid))
    bands = [(np.quantile(np.vstack(p), 0.05, axis=0), np.mean(np.vstack(p), axis=0), np.quantile(np.vstack(p), 0.95, axis=0)) for p in pred_by_iter]
    widths = [float(np.mean(hi - lo)) for lo, _m, hi in bands]
    print(f"Logistic band width: first={widths[0]:.3f}, middle={widths[len(widths)//2]:.3f}, last={widths[-1]:.3f}")

    bins = np.linspace(x.min(), x.max(), 9)
    bx, br, bs = binned_rate(x, y, bins)
    jitter = (np.random.default_rng(123).uniform(-0.025, 0.025, len(y)))
    frames = []
    for t, (theta, loss) in enumerate(trace):
        p = expit(theta[0] + theta[1] * grid)
        lo, mid, hi = bands[t]
        fig, ax = plt.subplots(figsize=(8.8, 5.2), constrained_layout=True)
        ax.scatter(x, y + jitter, s=28, color="0.45", alpha=0.35, label="固定データ 0/1")
        ax.scatter(bx, br, s=bs * 8, color="#DD8452", alpha=0.85, edgecolor="white", linewidth=0.6, label="ビンごとの成功率")
        ax.fill_between(grid, lo, hi, color="#DD8452", alpha=0.20, label="このstepの90%帯")
        ax.plot(grid, p, color="#B85C1E", lw=2.8, label="現在の成功確率")
        ax.set_title("08. Logistic GLM: 0/1データに成功確率曲線をフィット")
        ax.set_xlabel("x")
        ax.set_ylabel("Pr(y=1)")
        ax.set_xlim(grid.min(), grid.max())
        ax.set_ylim(-0.08, 1.08)
        add_note(ax, f"step {t}/{n_iter}\nlogit(p)=α+βx\nα={theta[0]:.2f}, β={theta[1]:.2f}\n交差エントロピー={loss:.3f}\n90%帯平均幅={widths[t]:.3f}")
        ax.legend(loc="upper left", frameon=True)
        frames.append(fig_to_frame(fig)); plt.close(fig)
    return save_gif(frames, GIF_DIR / "08_logistic_glm_fit.gif", fps=9)


gif_08 = make_logistic_glm_gif()
gif_08
"""))

cells.append(nbf.v4.new_markdown_cell(r"""## 3. 過分散: Poisson から負の二項分布へ

Poisson 分布は $E[y]=\mathrm{Var}(y)=\lambda$ という強い仮定を持つ。実データでは、個体差・場所差・未観測要因により分散が平均より大きい **過分散** がよく起きる。

負の二項分布は、

$$
 E[y]=\mu,\quad \mathrm{Var}(y)=\mu + \alpha \mu^2
$$

のように、平均 $\mu$ とは別に分散の強さ $\alpha$ を持つ。緑本で Poisson GLM を学んだ後に必ず見ておきたい拡張。
"""))

cells.append(nbf.v4.new_code_cell(r"""def nb_nll(y: np.ndarray, theta: np.ndarray) -> float:
    log_mu, log_alpha = theta
    mu = float(np.exp(np.clip(log_mu, -8, 8)))
    alpha = float(np.exp(np.clip(log_alpha, -6, 3)))
    r = 1.0 / alpha
    p = r / (r + mu)
    ll = gammaln(y + r) - gammaln(r) - gammaln(y + 1) + r * np.log(p) + y * np.log1p(-p)
    return float(-np.mean(ll))


def nb_pmf_grid(k: np.ndarray, log_mu: float, log_alpha: float) -> np.ndarray:
    mu = float(np.exp(np.clip(log_mu, -8, 8)))
    alpha = float(np.exp(np.clip(log_alpha, -6, 3)))
    r = 1.0 / alpha
    p = r / (r + mu)
    logpmf = gammaln(k + r) - gammaln(r) - gammaln(k + 1) + r * np.log(p) + k * np.log1p(-p)
    return np.exp(logpmf)


def make_negative_binomial_gif() -> Path:
    y = demo.query("dataset == 'neg_binom'")["y"].to_numpy(float)
    k = np.arange(0, int(max(22, y.max() + 3)))
    n_iter = 38

    def loss_grad(theta: np.ndarray) -> tuple[float, np.ndarray]:
        loss = nb_nll(y, theta)
        return loss, finite_diff_grad(lambda th: nb_nll(y, th), theta)

    trace = adam_trace(np.array([np.log(1.4), np.log(0.03)]), loss_grad, n_iter=n_iter, lr=0.10)

    rng = np.random.default_rng(909)
    pmf_by_iter = [[] for _ in range(n_iter + 1)]
    for _ in range(60):
        sample = rng.choice(y, len(y), replace=True)
        def lg(th: np.ndarray, s=sample) -> tuple[float, np.ndarray]:
            loss = nb_nll(s, th)
            return loss, finite_diff_grad(lambda theta: nb_nll(s, theta), th)
        tr = adam_trace(np.array([np.log(1.4), np.log(0.03)]), lg, n_iter=n_iter, lr=0.10)
        for t, (theta, _loss) in enumerate(tr):
            pmf_by_iter[t].append(nb_pmf_grid(k, theta[0], theta[1]))
    bands = [(np.quantile(np.vstack(p), 0.05, axis=0), np.mean(np.vstack(p), axis=0), np.quantile(np.vstack(p), 0.95, axis=0)) for p in pmf_by_iter]
    widths = [float(np.sum(hi - lo)) for lo, _m, hi in bands]
    print(f"NB band total width: first={widths[0]:.3f}, middle={widths[len(widths)//2]:.3f}, last={widths[-1]:.3f}")

    frames = []
    hist_counts = np.bincount(y.astype(int), minlength=len(k)) / len(y)
    poisson_mu = y.mean()
    poisson_pmf = np.exp(-poisson_mu) * poisson_mu**k / np.array([math.factorial(int(kk)) for kk in k], dtype=float)
    for t, (theta, loss) in enumerate(trace):
        pmf = nb_pmf_grid(k, theta[0], theta[1])
        lo, mid, hi = bands[t]
        mu = np.exp(theta[0]); alpha = np.exp(theta[1])
        fig, ax = plt.subplots(figsize=(8.8, 5.2), constrained_layout=True)
        ax.bar(k, hist_counts[:len(k)], width=0.86, color="0.78", alpha=0.70, label="固定データの相対頻度")
        ax.fill_between(k, lo, hi, step="mid", color="#55A868", alpha=0.22, label="このstepの90%帯")
        ax.plot(k, pmf, marker="o", color="#2C7F4F", lw=2.4, label="現在の負の二項分布")
        ax.plot(k, poisson_pmf, color="0.25", ls=":", lw=1.7, label="Poisson比較")
        ax.set_title("09. 過分散: 負の二項分布が太い裾へフィット")
        ax.set_xlabel("count")
        ax.set_ylabel("probability")
        ax.set_xlim(k.min() - 0.5, k.max() + 0.5)
        ax.set_ylim(bottom=0)
        add_note(ax, f"step {t}/{n_iter}\nVar(y)=μ+αμ²\nμ={mu:.2f}, α={alpha:.2f}\nNLL/obs={loss:.3f}\n90%帯総幅={widths[t]:.3f}")
        ax.legend(loc="upper right", frameon=True)
        frames.append(fig_to_frame(fig)); plt.close(fig)
    return save_gif(frames, GIF_DIR / "09_negative_binomial_overdispersion_fit.gif", fps=8)


gif_09 = make_negative_binomial_gif()
gif_09
"""))

cells.append(nbf.v4.new_markdown_cell(r"""## 4. 階層正規モデル: 群平均の部分プーリング

群ごとの平均を推定するとき、

- **完全プーリング**: 全群が同じ平均だとみなす。群差を無視しすぎる。
- **非プーリング**: 各群を完全に別々に推定する。サンプルの少ない群が不安定。
- **部分プーリング**: 群ごとの推定値を、データ量とばらつきに応じて全体平均へ縮める。

階層正規モデルの典型形は、

$$
 y_{ij}\sim \mathcal{N}(\theta_j,\sigma^2),\quad
 \theta_j\sim \mathcal{N}(\mu,\tau^2)
$$

で、群平均 $\theta_j$ が全体分布から来ると考える。
"""))

cells.append(nbf.v4.new_code_cell(r"""def make_hierarchical_normal_gif() -> Path:
    df = demo.query("dataset == 'hier_normal'").copy()
    stats = df.groupby("group")["y"].agg(["mean", "count", "std"]).reset_index()
    stats["se"] = stats["std"] / np.sqrt(stats["count"])
    global_mean = df["y"].mean()
    sigma2 = float(df.groupby("group")["y"].var().mean())
    # 教育用に、経験ベイズの群間分散をやや保守的に置く。
    # こうすると少数データ群の「全体平均へ縮む」動きが図で見えやすい。
    tau2_raw = float(max(stats["mean"].var(ddof=1) - sigma2 / stats["count"].mean(), 1.0))
    tau2 = max(8.0, tau2_raw * 0.45)
    w = tau2 / (tau2 + sigma2 / stats["count"].to_numpy(float))
    stats["partial"] = global_mean + w * (stats["mean"] - global_mean)
    stats["post_sd"] = np.sqrt(1.0 / (stats["count"].to_numpy(float) / sigma2 + 1.0 / tau2))

    n_iter = 44
    frames = []
    order = np.arange(len(stats))
    widths = []
    for t in range(n_iter + 1):
        rho = t / n_iter
        current = (1 - rho) * stats["mean"].to_numpy(float) + rho * stats["partial"].to_numpy(float)
        current_sd = (1 - rho) * stats["se"].fillna(stats["se"].median()).to_numpy(float) + rho * stats["post_sd"].to_numpy(float)
        lo, hi = current - 1.64 * current_sd, current + 1.64 * current_sd
        widths.append(float(np.mean(hi - lo)))
        fig, ax = plt.subplots(figsize=(8.8, 5.4), constrained_layout=True)
        sns.stripplot(data=df, x="group", y="y", ax=ax, color="0.55", alpha=0.45, jitter=0.18, size=4)
        ax.axhline(global_mean, color="0.25", ls=":", lw=1.5, label="完全プーリング平均")
        ax.errorbar(order, stats["mean"], yerr=1.64 * stats["se"], fmt="o", color="#C44E52", alpha=0.35, label="非プーリング平均")
        ax.errorbar(order, current, yerr=[current - lo, hi - current], fmt="o", color="#4C72B0", lw=2.2, capsize=4, label="現在の部分プーリング推定")
        for i, row in stats.iterrows():
            ax.plot([i, i], [row["mean"], row["partial"]], color="#4C72B0", alpha=0.25)
        ax.set_title("10. 階層正規モデル: 群平均が全体平均へ適度に縮む")
        ax.set_xlabel("group")
        ax.set_ylabel("y")
        ax.set_ylim(df["y"].min() - 8, df["y"].max() + 8)
        add_note(ax, f"step {t}/{n_iter}\nρ={rho:.2f}: 非プーリング → 部分プーリング\nサンプル数が少ない群ほど大きく縮む\n90%区間平均幅={widths[-1]:.2f}")
        ax.legend(loc="upper left", frameon=True)
        frames.append(fig_to_frame(fig)); plt.close(fig)
    print(f"Hier normal interval width: first={widths[0]:.2f}, middle={widths[len(widths)//2]:.2f}, last={widths[-1]:.2f}")
    return save_gif(frames, GIF_DIR / "10_hierarchical_normal_partial_pooling.gif", fps=8)


gif_10 = make_hierarchical_normal_gif()
gif_10
"""))

cells.append(nbf.v4.new_markdown_cell(r"""## 5. 階層回帰: varying intercept & varying slope

カテゴリごとの回帰では、群ごとに切片と傾きを別々に推定したくなる。しかし群ごとのデータ数が少ないと、線が極端になりやすい。

階層回帰では、

$$
 y_{ij}\sim\mathcal{N}(\alpha_j+\beta_j x_{ij},\sigma^2),\quad
 \begin{pmatrix}\alpha_j\\\beta_j\end{pmatrix}
 \sim \mathcal{N}\left(
 \begin{pmatrix}\alpha_0\\\beta_0\end{pmatrix},\Sigma
 \right)
$$

のように、群別の切片・傾きが全体分布から来ると考える。ここでは、群別 OLS から全体 OLS への収縮を「部分プーリングの見た目」として描く。
"""))

cells.append(nbf.v4.new_code_cell(r"""def fit_ols(x: np.ndarray, y: np.ndarray) -> np.ndarray:
    X = np.column_stack([np.ones_like(x), x])
    return np.linalg.lstsq(X, y, rcond=None)[0]


def make_hierarchical_regression_gif() -> Path:
    df = demo.query("dataset == 'hier_regression'").copy()
    groups = sorted(df["group"].unique())
    colors = dict(zip(groups, sns.color_palette("colorblind", len(groups))))
    global_coef = fit_ols(df["x"].to_numpy(float), df["y"].to_numpy(float))
    rows = []
    for g in groups:
        sub = df[df["group"] == g]
        coef = fit_ols(sub["x"].to_numpy(float), sub["y"].to_numpy(float))
        n_g = len(sub)
        shrink_w = n_g / (n_g + 10.0)
        partial = global_coef + shrink_w * (coef - global_coef)
        rows.append({"group": g, "n": n_g, "a_np": coef[0], "b_np": coef[1], "a_pp": partial[0], "b_pp": partial[1], "w": shrink_w})
    coefs = pd.DataFrame(rows)
    grid = np.linspace(df["x"].min() - 0.2, df["x"].max() + 0.2, 160)
    n_iter = 44
    frames = []
    mean_band_widths = []
    for t in range(n_iter + 1):
        rho = t / n_iter
        fig, ax = plt.subplots(figsize=(8.8, 5.4), constrained_layout=True)
        band_width_this = []
        for g in groups:
            sub = df[df["group"] == g]
            c = colors[g]
            ax.scatter(sub["x"], sub["y"], s=34, color=c, alpha=0.65, edgecolor="white", linewidth=0.35)
            row = coefs[coefs["group"] == g].iloc[0]
            a = (1 - rho) * row["a_np"] + rho * row["a_pp"]
            b = (1 - rho) * row["b_np"] + rho * row["b_pp"]
            # approximate current uncertainty: noisy group-specific band, shrinking toward partial-pooling band
            se = 1.7 / np.sqrt(row["n"])
            pp_se = 0.9 / np.sqrt(row["n"] + 4)
            cur_se = (1 - rho) * se + rho * pp_se
            yhat = a + b * grid
            lo, hi = yhat - 1.64 * cur_se, yhat + 1.64 * cur_se
            band_width_this.append(float(np.mean(hi - lo)))
            ax.fill_between(grid, lo, hi, color=c, alpha=0.08)
            ax.plot(grid, yhat, color=c, lw=2.0, label=f"{g} (n={int(row['n'])})")
            ax.plot(grid, row["a_pp"] + row["b_pp"] * grid, color=c, lw=1.0, ls=":", alpha=0.6)
        ax.plot(grid, global_coef[0] + global_coef[1] * grid, color="0.15", lw=2.0, ls="--", label="全体OLS")
        ax.set_title("11. 階層回帰: 群別の切片・傾きが全体傾向へ部分プーリング")
        ax.set_xlabel("x")
        ax.set_ylabel("y")
        ax.set_xlim(grid.min(), grid.max())
        ax.set_ylim(df["y"].min() - 1.2, df["y"].max() + 1.2)
        mean_band_widths.append(float(np.mean(band_width_this)))
        add_note(ax, f"step {t}/{n_iter}\nρ={rho:.2f}: 群別OLS → 部分プーリング\n点線=到達先の部分プーリング線\n90%帯平均幅={mean_band_widths[-1]:.2f}")
        ax.legend(loc="upper left", ncols=2, fontsize=8, frameon=True)
        frames.append(fig_to_frame(fig)); plt.close(fig)
    print(f"Hier regression band width: first={mean_band_widths[0]:.2f}, middle={mean_band_widths[len(mean_band_widths)//2]:.2f}, last={mean_band_widths[-1]:.2f}")
    return save_gif(frames, GIF_DIR / "11_hierarchical_varying_slope_regression.gif", fps=8)


gif_11 = make_hierarchical_regression_gif()
gif_11
"""))

cells.append(nbf.v4.new_code_cell(r"""# 6. Contact sheet for quick visual verification
from PIL import Image, ImageDraw

items = [
    ("07 Poisson GLM", gif_07),
    ("08 Logistic GLM", gif_08),
    ("09 Negative Binomial", gif_09),
    ("10 Hierarchical Normal", gif_10),
    ("11 Hierarchical Regression", gif_11),
]
thumbs = []
for title, path in items:
    frames = imageio.mimread(path)
    selected = [frames[0], frames[len(frames)//2], frames[-1]]
    for label, frame in zip(["first", "middle", "last"], selected):
        img = Image.fromarray(frame).resize((320, 190))
        canvas = Image.new("RGB", (320, 220), "white")
        canvas.paste(img, (0, 30))
        d = ImageDraw.Draw(canvas)
        d.text((8, 8), f"{title} / {label}", fill=(20, 20, 20))
        thumbs.append(canvas)

sheet = Image.new("RGB", (320 * 3, 220 * len(items)), "white")
for i, img in enumerate(thumbs):
    row, col = divmod(i, 3)
    sheet.paste(img, (col * 320, row * 220))
contact_path = FIG_DIR / "essential_stat_modeling_contact_sheet.png"
sheet.save(contact_path)
print(contact_path.relative_to(PROJECT_ROOT))
"""))

cells.append(nbf.v4.new_code_cell(r"""# 7. Display GIFs in the notebook
from IPython.display import HTML, display

items = [
    ("07. Poisson GLM", gif_07),
    ("08. Logistic GLM", gif_08),
    ("09. Negative Binomial / Overdispersion", gif_09),
    ("10. Hierarchical Normal Partial Pooling", gif_10),
    ("11. Hierarchical Varying-slope Regression", gif_11),
]
html = ["<div style='display:grid; grid-template-columns: 1fr; gap: 24px;'>"]
for title, path in items:
    rel = path.relative_to(PROJECT_ROOT).as_posix()
    html.append(
        f"<section><h3>{title}</h3><p><code>{rel}</code></p>"
        f"<img src='../{rel}' style='max-width: 920px; width: 100%; border:1px solid #ddd;'>"
        f"</section>"
    )
html.append("</div>")
display(HTML("\n".join(html)))
"""))

cells.append(nbf.v4.new_markdown_cell(r"""## 8. まとめ: 次に学ぶとよいもの

このノートの 5 本の GIF は、緑本から階層モデルへ進むための橋渡しとして選んだ。

1. **Poisson GLM**: カウントデータでは log link を使う。
2. **Logistic GLM**: 0/1 データでは logit link を使う。
3. **負の二項分布**: Poisson よりデータがばらつくときの基本拡張。
4. **階層正規モデル**: 群平均は非プーリングでも完全プーリングでもなく、部分プーリングする。
5. **階層回帰**: 群ごとの切片・傾きも部分プーリングできる。

さらに進むなら、次を別ノートで可視化するとよい。

- **ゼロ過剰モデル**: 0 が多すぎるカウントデータ。
- **生存時間モデル**: 打ち切りを含む時間データ。
- **状態空間モデル**: 時系列の潜在状態と観測ノイズ。
- **MCMC 診断**: warmup, chain, R-hat, 有効サンプルサイズ。
- **事後予測チェック**: モデルが再現するデータと実データの比較。
"""))

nb["cells"] = cells
nbf.write(nb, NOTEBOOK_PATH)
print(NOTEBOOK_PATH)
