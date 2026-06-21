from __future__ import annotations

from pathlib import Path

import nbformat as nbf

ROOT = Path(__file__).resolve().parents[1]
NOTEBOOK_PATH = ROOT / "notebooks" / "003_hierarchical_statistical_modeling_gifs.ipynb"
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

cells.append(nbf.v4.new_markdown_cell(r"""# 緑本・代表的統計モデリングを理解するための階層/GLM GIF ノート

- **目的**: 「データ解析のための統計モデリング入門（いわゆる緑本）」で中心になる GLM と、その先にある階層モデル/部分プーリングを、固定データ上でモデルがデータへ合っていくアニメーションとして確認する。
- **作成環境**: `D:/dev/dev_statistics/venv` の venv kernel (`Python (dev_statistics venv)`)。
- **データ**: 前ノートで保存済みのローカル公開データ `data/raw/*.csv` のみを読む。外部 URL にはアクセスしない。
- **作成物**:
  - `outputs/gifs/07_poisson_glm_count_fit.gif`
  - `outputs/gifs/08_logistic_glm_binary_fit.gif`
  - `outputs/gifs/09_hierarchical_normal_partial_pooling.gif`
  - `outputs/gifs/10_hierarchical_regression_partial_pooling.gif`
  - `outputs/figures/hierarchical_modeling_contact_sheet.png`

ここでの不確実性帯は説明用の軽量近似（ブートストラップ、正規近似、経験ベイズ的な shrinkage）です。本格的なベイズ推論では PyMC/Stan などで事後分布・事後予測分布をサンプリングします。
"""))

cells.append(nbf.v4.new_markdown_cell(r"""## 0. 統計マンがまず押さえたい代表的な手法マップ

参考として確認した情報:

- 久保拓弥『データ解析のための統計モデリング入門』岩波書店ページ: 書名は「データ解析のための統計モデリング入門」。緑本として GLM/階層ベイズへの入口としてよく読まれる。
- `seaborn-data`: seaborn examples 用の公開データリポジトリ。今回の実行では保存済みローカル CSV を使用。

| レベル | 知っておくべきもの | 何を表すか | このノートでの可視化 |
|---|---|---|---|
| 1 | 分布 + 尤度 + 最尤推定 | データ生成分布のパラメータを推定する | 前ノートの正規分布フィット |
| 2 | 線形回帰 | 連続値の平均構造を説明する | 前ノートの単回帰 |
| 3 | **GLM: Poisson 回帰** | カウントデータを log link でモデル化する | 07 |
| 4 | **GLM: Binomial/Logistic 回帰** | 確率・比率・二値結果を logit link でモデル化する | 08 |
| 5 | 過分散・負の二項・混合モデル | Poisson/Binomial で説明しきれないばらつきや多峰性 | 前ノートの混合モデル、発展候補 |
| 6 | **階層モデル / 部分プーリング** | グループ別推定を「全体」と「各群」の間で縮約する | 09, 10 |
| 7 | GLMM / 階層ベイズ | GLM に random effect を入れる。個体差・地域差・種差など | 10 の直感版 |
| 8 | モデル比較・予測チェック | AIC/WAIC/LOO、posterior predictive check、残差診断 | 発展候補 |
| 9 | 時系列/状態空間/生存/因果 | 時間依存、打ち切り、介入効果など | 発展候補 |

このノートでは **GLM と階層モデルの直感** を優先し、以下の 4 本を作る。

1. **Poisson GLM**: カウントデータに指数曲線がフィットしていく。
2. **Logistic GLM**: 二値データの確率曲線が S 字にフィットしていく。
3. **階層 Normal モデル**: グループ平均が完全プーリングから部分プーリングへ移動する。
4. **階層回帰/ランダム係数の直感**: 種別回帰線が全体線からカテゴリ別線へ、ただし行き過ぎずに縮約される。
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
from scipy.special import expit

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
    "penguins": DATA_DIR / "penguins.csv",
    "tips": DATA_DIR / "tips.csv",
}


def load_local_csv(name: str) -> pd.DataFrame:
    path = DATA_FILES[name]
    if not path.exists():
        raise FileNotFoundError(
            f"{path} が見つかりません。前ノートの手順で公開データをローカル保存してください。"
        )
    print(f"{name:<8} <- {path.relative_to(PROJECT_ROOT).as_posix()}")
    return pd.read_csv(path)


penguins = load_local_csv("penguins")
tips = load_local_csv("tips")

print("penguins", penguins.shape, list(penguins.columns))
print("tips    ", tips.shape, list(tips.columns))
"""))

cells.append(nbf.v4.new_code_cell(r"""# 3. Shared helper functions
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


def standardize(x: np.ndarray) -> tuple[np.ndarray, float, float]:
    center = float(np.mean(x))
    scale = float(np.std(x, ddof=1))
    return (x - center) / scale, center, scale


def adam_trace(theta0: np.ndarray, grad_loss_fn, n_iter: int, lr: float) -> list[tuple[np.ndarray, float]]:
    theta = theta0.astype(float).copy()
    m = np.zeros_like(theta)
    v = np.zeros_like(theta)
    beta1, beta2, eps = 0.9, 0.999, 1e-8
    trace: list[tuple[np.ndarray, float]] = []
    for step in range(n_iter + 1):
        loss, grad = grad_loss_fn(theta)
        trace.append((theta.copy(), float(loss)))
        m = beta1 * m + (1 - beta1) * grad
        v = beta2 * v + (1 - beta2) * (grad**2)
        m_hat = m / (1 - beta1 ** (step + 1))
        v_hat = v / (1 - beta2 ** (step + 1))
        theta -= lr * m_hat / (np.sqrt(v_hat) + eps)
    return trace
"""))

cells.append(nbf.v4.new_markdown_cell(r"""## 1. Poisson GLM: カウントデータを log link でフィットする

- **データ**: `tips.csv` の `total_bill` と `size`。1 行は飲食テーブル 1 件、`size` は人数カウント。
- **モデル**: $y_i \sim \mathrm{Poisson}(\lambda_i)$, $\log \lambda_i = \alpha + \beta x_i$。
- **見方**: 通常の線形回帰ではなく、平均人数 $\lambda$ が正になるように指数曲線で表す。step が進むにつれて、カウントの中心を通る曲線へ近づく。
- **不確実性**: ブートストラップで各 iteration の平均曲線の 90% 帯を出す。
"""))

cells.append(nbf.v4.new_code_cell(r"""def poisson_loss_grad(x_std: np.ndarray, y: np.ndarray):
    def fn(theta: np.ndarray) -> tuple[float, np.ndarray]:
        eta = np.clip(theta[0] + theta[1] * x_std, -8, 8)
        lam = np.exp(eta)
        # constants log(y!) are omitted; they do not affect fitting.
        loss = float(np.mean(lam - y * eta))
        resid = lam - y
        grad = np.array([np.mean(resid), np.mean(resid * x_std)], dtype=float)
        return loss, grad
    return fn


def poisson_trace(x_std: np.ndarray, y: np.ndarray, n_iter: int = 48) -> list[tuple[np.ndarray, float]]:
    start = np.array([np.log(max(y.mean(), 0.1)) - 0.7, -0.85])
    return adam_trace(start, poisson_loss_grad(x_std, y), n_iter=n_iter, lr=0.075)


def poisson_predict(x_grid_raw: np.ndarray, x_center: float, x_scale: float, theta: np.ndarray) -> np.ndarray:
    xg = (x_grid_raw - x_center) / x_scale
    return np.exp(np.clip(theta[0] + theta[1] * xg, -8, 8))


def poisson_bootstrap_bands(x_raw: np.ndarray, y: np.ndarray, x_grid: np.ndarray, x_center: float, x_scale: float, n_iter: int, n_boot: int = 45):
    rng = np.random.default_rng(710)
    n = len(y)
    preds_by_iter = [[] for _ in range(n_iter + 1)]
    for _ in range(n_boot):
        idx = rng.integers(0, n, size=n)
        xb = (x_raw[idx] - x_center) / x_scale
        tr = poisson_trace(xb, y[idx], n_iter=n_iter)
        for t, (theta, _loss) in enumerate(tr):
            preds_by_iter[t].append(poisson_predict(x_grid, x_center, x_scale, theta))
    bands = []
    for preds in preds_by_iter:
        arr = np.vstack(preds)
        bands.append((np.quantile(arr, 0.05, axis=0), np.mean(arr, axis=0), np.quantile(arr, 0.95, axis=0)))
    return bands


def make_poisson_glm_gif() -> Path:
    df = tips[["total_bill", "size"]].dropna().copy()
    x_raw = df["total_bill"].to_numpy(float)
    y = df["size"].to_numpy(float)
    x_std, x_center, x_scale = standardize(x_raw)
    n_iter = 48
    trace = poisson_trace(x_std, y, n_iter=n_iter)
    x_grid = np.linspace(x_raw.min() - 2, x_raw.max() + 2, 260)
    bands = poisson_bootstrap_bands(x_raw, y, x_grid, x_center, x_scale, n_iter=n_iter)
    widths = [float(np.mean(hi - lo)) for lo, _mid, hi in bands]
    print(f"poisson band width: first={widths[0]:.3f}, middle={widths[len(widths)//2]:.3f}, last={widths[-1]:.3f}")

    frames = []
    jitter = RNG.normal(0, 0.045, size=len(y))
    for t, (theta, loss) in enumerate(trace):
        pred = poisson_predict(x_grid, x_center, x_scale, theta)
        lo, mid, hi = bands[t]
        fig, ax = plt.subplots(figsize=(8.8, 5.2), constrained_layout=True)
        ax.scatter(x_raw, y + jitter, s=32, alpha=0.55, color="#4C72B0", edgecolor="white", linewidth=0.3, label="固定データ（人数count）")
        ax.fill_between(x_grid, lo, hi, color="#DD8452", alpha=0.23, label="このiterationの90%帯")
        ax.plot(x_grid, pred, color="#C44E52", lw=2.8, label="現在の Poisson 平均 λ")
        ax.set_title("3. Poisson GLM: log linkでカウント平均をフィット")
        ax.set_xlabel("total_bill")
        ax.set_ylabel("size / E[size]")
        ax.set_xlim(x_grid.min(), x_grid.max())
        ax.set_ylim(0, max(8, y.max() + 1))
        add_note(ax, f"step {t}/{n_iter}\nlog λ = α + βx\nα={theta[0]:.2f}, β={theta[1]:.2f}\nNLL/obs={loss:.3f}\n90%帯平均幅={widths[t]:.2f}", loc=(0.03, 0.42), fontsize=8)
        ax.legend(loc="upper right", frameon=True)
        frames.append(fig_to_frame(fig))
        plt.close(fig)
    return save_gif(frames, GIF_DIR / "07_poisson_glm_count_fit.gif", fps=9)


gif_07 = make_poisson_glm_gif()
gif_07
"""))

cells.append(nbf.v4.new_markdown_cell(r"""## 2. Logistic GLM: 二値結果の確率曲線をフィットする

- **データ**: `penguins.csv`。`species == "Adelie"` を 1、それ以外を 0 とし、`bill_length_mm` から確率を説明する。
- **モデル**: $y_i \sim \mathrm{Bernoulli}(p_i)$, $\mathrm{logit}(p_i)=\alpha+\beta x_i$。
- **見方**: 二値データそのものは 0/1 に散らばるが、モデルは「1 になる確率」$p$ を S 字曲線として表す。
- **不確実性**: ブートストラップで各 iteration の確率曲線の 90% 帯を出す。
"""))

cells.append(nbf.v4.new_code_cell(r"""def logistic_loss_grad(x_std: np.ndarray, y: np.ndarray):
    def fn(theta: np.ndarray) -> tuple[float, np.ndarray]:
        eta = np.clip(theta[0] + theta[1] * x_std, -35, 35)
        p = expit(eta)
        eps = 1e-9
        loss = float(-np.mean(y * np.log(p + eps) + (1 - y) * np.log(1 - p + eps)))
        resid = p - y
        grad = np.array([np.mean(resid), np.mean(resid * x_std)], dtype=float)
        return loss, grad
    return fn


def logistic_trace(x_std: np.ndarray, y: np.ndarray, n_iter: int = 52) -> list[tuple[np.ndarray, float]]:
    start = np.array([0.2, 1.2])  # deliberately wrong direction for Adelie vs bill length
    return adam_trace(start, logistic_loss_grad(x_std, y), n_iter=n_iter, lr=0.11)


def logistic_predict(x_grid_raw: np.ndarray, x_center: float, x_scale: float, theta: np.ndarray) -> np.ndarray:
    xg = (x_grid_raw - x_center) / x_scale
    return expit(np.clip(theta[0] + theta[1] * xg, -35, 35))


def logistic_bootstrap_bands(x_raw: np.ndarray, y: np.ndarray, x_grid: np.ndarray, x_center: float, x_scale: float, n_iter: int, n_boot: int = 45):
    rng = np.random.default_rng(810)
    n = len(y)
    preds_by_iter = [[] for _ in range(n_iter + 1)]
    for _ in range(n_boot):
        idx = rng.integers(0, n, size=n)
        xb = (x_raw[idx] - x_center) / x_scale
        tr = logistic_trace(xb, y[idx], n_iter=n_iter)
        for t, (theta, _loss) in enumerate(tr):
            preds_by_iter[t].append(logistic_predict(x_grid, x_center, x_scale, theta))
    bands = []
    for preds in preds_by_iter:
        arr = np.vstack(preds)
        bands.append((np.quantile(arr, 0.05, axis=0), np.mean(arr, axis=0), np.quantile(arr, 0.95, axis=0)))
    return bands


def make_logistic_glm_gif() -> Path:
    df = penguins[["species", "bill_length_mm"]].dropna().copy()
    df["is_adelie"] = (df["species"] == "Adelie").astype(float)
    x_raw = df["bill_length_mm"].to_numpy(float)
    y = df["is_adelie"].to_numpy(float)
    x_std, x_center, x_scale = standardize(x_raw)
    n_iter = 52
    trace = logistic_trace(x_std, y, n_iter=n_iter)
    x_grid = np.linspace(x_raw.min() - 1.5, x_raw.max() + 1.5, 260)
    bands = logistic_bootstrap_bands(x_raw, y, x_grid, x_center, x_scale, n_iter=n_iter)
    widths = [float(np.mean(hi - lo)) for lo, _mid, hi in bands]
    print(f"logistic band width: first={widths[0]:.3f}, middle={widths[len(widths)//2]:.3f}, last={widths[-1]:.3f}")

    frames = []
    jitter = RNG.normal(0, 0.035, size=len(y))
    for t, (theta, loss) in enumerate(trace):
        pred = logistic_predict(x_grid, x_center, x_scale, theta)
        lo, mid, hi = bands[t]
        fig, ax = plt.subplots(figsize=(8.8, 5.2), constrained_layout=True)
        colors = np.where(y == 1, "#4C72B0", "#999999")
        ax.scatter(x_raw, y + jitter, s=30, alpha=0.55, color=colors, edgecolor="white", linewidth=0.25, label="固定データ（Adelie=1）")
        ax.fill_between(x_grid, lo, hi, color="#55A868", alpha=0.23, label="このiterationの90%帯")
        ax.plot(x_grid, pred, color="#2C7F4F", lw=2.8, label="現在の Pr(Adelie)")
        ax.set_title("4. Logistic GLM: logit linkで二値確率をフィット")
        ax.set_xlabel("bill_length_mm")
        ax.set_ylabel("Pr(species = Adelie)")
        ax.set_xlim(x_grid.min(), x_grid.max())
        ax.set_ylim(-0.12, 1.12)
        add_note(ax, f"step {t}/{n_iter}\nlogit(p)=α+βx\nα={theta[0]:.2f}, β={theta[1]:.2f}\nNLL/obs={loss:.3f}\n90%帯平均幅={widths[t]:.2f}", loc=(0.03, 0.42), fontsize=8)
        ax.legend(loc="lower right", frameon=True)
        frames.append(fig_to_frame(fig))
        plt.close(fig)
    return save_gif(frames, GIF_DIR / "08_logistic_glm_binary_fit.gif", fps=9)


gif_08 = make_logistic_glm_gif()
gif_08
"""))

cells.append(nbf.v4.new_markdown_cell(r"""## 3. 階層 Normal モデル: グループ平均の部分プーリング

- **データ**: `penguins.csv` の `body_mass_g` を `species` ごとに見る。
- **非階層の極端**:
  - 完全プーリング: 種差を無視して全体平均 1 本だけ。
  - ノープーリング: 種ごとに独立に平均を推定。
- **階層モデルの考え方**: 種ごとの平均 $\mu_j$ は、全体平均 $\mu_0$ からばらつくと考える。
  $\mu_j \sim \mathcal{N}(\mu_0, \tau^2)$。
- **見方**: 情報が少ない群やノイズが大きい群の推定値は、群平均そのものではなく全体平均へ縮む。これが **部分プーリング**。
"""))

cells.append(nbf.v4.new_code_cell(r"""def make_hierarchical_normal_gif() -> Path:
    df = penguins[["species", "body_mass_g"]].dropna().copy()
    groups = list(df["species"].unique())
    groups.sort()
    y_all = df["body_mass_g"].to_numpy(float)
    global_mean = float(y_all.mean())
    sigma = float(df.groupby("species")["body_mass_g"].std().mean())
    stats = df.groupby("species")["body_mass_g"].agg(["mean", "count", "std"]).reindex(groups)
    raw_means = stats["mean"].to_numpy(float)
    ns = stats["count"].to_numpy(float)
    se = sigma / np.sqrt(ns)
    tau_hat = float(np.std(raw_means, ddof=1))

    # Equal tau spacing made later frames visually static.  Resample the tau path
    # by equal movement of posterior group means so every frame changes.
    tau_candidates = np.geomspace(1.0, max(tau_hat, 1.0), 500)

    def posterior_mean_for_tau(tau: float) -> np.ndarray:
        prior_prec = 1.0 / max(tau**2, 1e-9)
        data_prec = 1.0 / np.maximum(se**2, 1e-9)
        w_data = data_prec / (data_prec + prior_prec)
        return (1 - w_data) * global_mean + w_data * raw_means

    candidate_means = np.vstack([posterior_mean_for_tau(float(tau)) for tau in tau_candidates])
    displacement = np.r_[0.0, np.cumsum(np.linalg.norm(np.diff(candidate_means, axis=0), axis=1))]
    if displacement[-1] > 0:
        tau_trace = np.r_[0.0, np.interp(np.linspace(0, displacement[-1], 45), displacement, tau_candidates)]
    else:
        tau_trace = np.linspace(0.0, tau_hat, 46)
    n_iter = len(tau_trace) - 1
    estimates = []
    intervals = []
    for tau in tau_trace:
        # Normal-normal posterior mean for group mean with prior centered at global_mean.
        # tau=0 gives complete pooling; larger tau allows group means to move away.
        prior_prec = 1.0 / max(tau**2, 1e-9)
        data_prec = 1.0 / np.maximum(se**2, 1e-9)
        w_data = data_prec / (data_prec + prior_prec)
        mu_post = (1 - w_data) * global_mean + w_data * raw_means
        sd_post = np.sqrt(1.0 / (data_prec + prior_prec))
        estimates.append(mu_post)
        intervals.append((mu_post - 1.64 * sd_post, mu_post + 1.64 * sd_post))
    widths = [float(np.mean(hi - lo)) for lo, hi in intervals]
    print(f"hierarchical normal interval width: first={widths[0]:.2f}, middle={widths[len(widths)//2]:.2f}, last={widths[-1]:.2f}")

    colors = sns.color_palette("Set2", n_colors=len(groups))
    x_positions = np.arange(len(groups))
    frames = []
    for t, tau in enumerate(tau_trace):
        mu_post = estimates[t]
        lo, hi = intervals[t]
        fig, ax = plt.subplots(figsize=(8.8, 5.2), constrained_layout=True)
        for j, g in enumerate(groups):
            vals = df.loc[df["species"] == g, "body_mass_g"].to_numpy(float)
            xj = RNG.normal(j, 0.045, size=len(vals))
            ax.scatter(xj, vals, s=20, alpha=0.23, color=colors[j], edgecolor="none")
            ax.plot([j - 0.26, j + 0.26], [raw_means[j], raw_means[j]], color=colors[j], lw=1.5, ls=":", label="群平均（ノープーリング）" if j == 0 else None)
            ax.vlines(j, lo[j], hi[j], color="#C44E52", lw=4, alpha=0.55)
            ax.scatter(j, mu_post[j], s=110, color="#C44E52", edgecolor="white", linewidth=1.1, zorder=5, label="階層モデル推定" if j == 0 else None)
        ax.axhline(global_mean, color="0.25", lw=1.7, ls="--", label="全体平均（完全プーリング）")
        ax.set_xticks(x_positions, groups)
        ax.set_title("5. 階層Normalモデル: 群平均が全体平均から部分プーリングへ動く")
        ax.set_xlabel("species")
        ax.set_ylabel("body_mass_g")
        ax.set_ylim(y_all.min() - 350, y_all.max() + 350)
        add_note(ax, f"step {t}/{n_iter}\nμ_j ~ Normal(μ0, τ²)\nτ={tau:.0f} g\n赤点: 部分プーリング平均\n90%区間平均幅={widths[t]:.1f} g", loc=(0.03, 0.38), fontsize=8)
        ax.legend(loc="upper right", frameon=True)
        frames.append(fig_to_frame(fig))
        plt.close(fig)
    return save_gif(frames, GIF_DIR / "09_hierarchical_normal_partial_pooling.gif", fps=9)


gif_09 = make_hierarchical_normal_gif()
gif_09
"""))

cells.append(nbf.v4.new_markdown_cell(r"""## 4. 階層回帰 / ランダム係数: 種別回帰線の部分プーリング

- **データ**: `penguins.csv` の `flipper_length_mm` と `body_mass_g` を `species` ごとに見る。
- **完全プーリング**: 種別を無視し、全データに 1 本の回帰線。
- **ノープーリング**: 種ごとに完全に別々の回帰線。
- **階層回帰の直感**: 種別ごとの切片・傾きは、全体の切片・傾きからのズレとして扱う。各群の線は全体線と群別線の中間へ縮む。

ここでは軽量化のため、ランダム係数モデルの厳密推論ではなく、ブートストラップつきの shrinkage path として可視化する。
"""))

cells.append(nbf.v4.new_code_cell(r"""def fit_ols_raw(x: np.ndarray, y: np.ndarray) -> np.ndarray:
    X = np.column_stack([np.ones_like(x), x])
    return np.linalg.lstsq(X, y, rcond=None)[0]


def predict_ols(x_grid: np.ndarray, coef: np.ndarray) -> np.ndarray:
    return coef[0] + coef[1] * x_grid


def make_hierarchical_regression_gif() -> Path:
    df = penguins[["species", "flipper_length_mm", "body_mass_g"]].dropna().copy()
    groups = sorted(df["species"].unique())
    colors = dict(zip(groups, sns.color_palette("Set2", n_colors=len(groups))))
    x_all = df["flipper_length_mm"].to_numpy(float)
    y_all = df["body_mass_g"].to_numpy(float)
    global_coef = fit_ols_raw(x_all, y_all)
    sep_coefs = {}
    ns = {}
    for g in groups:
        dfg = df[df["species"] == g]
        sep_coefs[g] = fit_ols_raw(dfg["flipper_length_mm"].to_numpy(float), dfg["body_mass_g"].to_numpy(float))
        ns[g] = len(dfg)

    # k decreases: very strong pooling -> weaker but still nonzero pooling.
    # Resample by equal movement of the group coefficient vector so late frames do
    # not become visually redundant.
    k_candidates = np.geomspace(800.0, 18.0, 500)

    def coefficient_state_for_k(k: float) -> np.ndarray:
        vals = []
        for g in groups:
            w = ns[g] / (ns[g] + k)
            vals.append((1 - w) * global_coef + w * sep_coefs[g])
        return np.concatenate(vals)

    candidate_coefs = np.vstack([coefficient_state_for_k(float(k)) for k in k_candidates])
    displacement = np.r_[0.0, np.cumsum(np.linalg.norm(np.diff(candidate_coefs, axis=0), axis=1))]
    if displacement[-1] > 0:
        k_trace = np.interp(np.linspace(0, displacement[-1], 46), displacement, k_candidates)
    else:
        k_trace = np.geomspace(800.0, 18.0, 46)
    n_iter = len(k_trace) - 1
    x_grid = np.linspace(x_all.min() - 4, x_all.max() + 4, 260)

    rng = np.random.default_rng(1010)
    n_boot = 45
    preds_by_iter = {g: [[] for _ in range(n_iter + 1)] for g in groups}
    for _ in range(n_boot):
        idx_all = rng.integers(0, len(df), size=len(df))
        boot_all = df.iloc[idx_all]
        gcoef_b = fit_ols_raw(boot_all["flipper_length_mm"].to_numpy(float), boot_all["body_mass_g"].to_numpy(float))
        sep_b = {}
        for g in groups:
            dfg = df[df["species"] == g]
            idx = rng.integers(0, len(dfg), size=len(dfg))
            boot_g = dfg.iloc[idx]
            sep_b[g] = fit_ols_raw(boot_g["flipper_length_mm"].to_numpy(float), boot_g["body_mass_g"].to_numpy(float))
        for t, k in enumerate(k_trace):
            for g in groups:
                w = ns[g] / (ns[g] + k)
                coef = (1 - w) * gcoef_b + w * sep_b[g]
                preds_by_iter[g][t].append(predict_ols(x_grid, coef))

    bands = {g: [] for g in groups}
    for g in groups:
        for t in range(n_iter + 1):
            arr = np.vstack(preds_by_iter[g][t])
            bands[g].append((np.quantile(arr, 0.05, axis=0), np.mean(arr, axis=0), np.quantile(arr, 0.95, axis=0)))
    width_diag = [float(np.mean([np.mean(bands[g][t][2] - bands[g][t][0]) for g in groups])) for t in range(n_iter + 1)]
    print(f"hierarchical regression band width: first={width_diag[0]:.2f}, middle={width_diag[len(width_diag)//2]:.2f}, last={width_diag[-1]:.2f}")

    frames = []
    for t, k in enumerate(k_trace):
        fig, ax = plt.subplots(figsize=(8.8, 5.2), constrained_layout=True)
        ax.plot(x_grid, predict_ols(x_grid, global_coef), color="0.25", lw=1.6, ls="--", label="全体線（完全プーリング）")
        for g in groups:
            dfg = df[df["species"] == g]
            ax.scatter(dfg["flipper_length_mm"], dfg["body_mass_g"], s=25, alpha=0.42, color=colors[g], edgecolor="white", linewidth=0.25, label="固定データ" if g == groups[0] else None)
            w = ns[g] / (ns[g] + k)
            coef = (1 - w) * global_coef + w * sep_coefs[g]
            lo, mid, hi = bands[g][t]
            ax.fill_between(x_grid, lo, hi, color=colors[g], alpha=0.12)
            ax.plot(x_grid, predict_ols(x_grid, coef), color=colors[g], lw=2.5, label=f"{g} 部分プーリング線")
        ax.set_title("6. 階層回帰: 種別回帰線が全体線から部分プーリングへ動く")
        ax.set_xlabel("flipper_length_mm")
        ax.set_ylabel("body_mass_g")
        ax.set_xlim(x_grid.min(), x_grid.max())
        ax.set_ylim(y_all.min() - 500, y_all.max() + 500)
        mean_w = float(np.mean([ns[g] / (ns[g] + k) for g in groups]))
        add_note(ax, f"step {t}/{n_iter}\n係数_j=(1-w)全体+w群別\n平均w={mean_w:.2f}\nこのiterationの90%帯\n平均幅={width_diag[t]:.1f} g", loc=(0.03, 0.38), fontsize=8)
        ax.legend(loc="upper left", bbox_to_anchor=(1.01, 1.0), fontsize=8, frameon=True)
        frames.append(fig_to_frame(fig))
        plt.close(fig)
    return save_gif(frames, GIF_DIR / "10_hierarchical_regression_partial_pooling.gif", fps=9)


gif_10 = make_hierarchical_regression_gif()
gif_10
"""))

cells.append(nbf.v4.new_markdown_cell(r"""## 5. 作成した GIF をまとめて表示

4 本とも、データは全フレーム固定し、モデル状態とその iteration の不確実性帯だけが変わる。
"""))

cells.append(nbf.v4.new_code_cell(r"""from IPython.display import HTML, display

items = [
    ("3. Poisson GLM: カウント", gif_07),
    ("4. Logistic GLM: 二値確率", gif_08),
    ("5. 階層Normal: 部分プーリング", gif_09),
    ("6. 階層回帰: 種別線の縮約", gif_10),
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

cells.append(nbf.v4.new_code_cell(r"""# 6. Contact sheet for quick verification
from PIL import Image, ImageDraw, ImageFont


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
    thumbs = []
    for path in gif_paths:
        reader = imageio.get_reader(path)
        try:
            n = reader.get_length()
        finally:
            reader.close()
        indices = [0, n // 2, n - 1]
        row = []
        for idx in indices:
            im = read_gif_frame(path, idx)
            im.thumbnail((360, 220))
            row.append((im.copy(), f"{path.name}\n{labels[len(row)]}: frame {idx}"))
        thumbs.append(row)

    cell_w, cell_h = 390, 270
    sheet = Image.new("RGB", (cell_w * 3, cell_h * len(thumbs)), "white")
    draw = ImageDraw.Draw(sheet)
    for r, row in enumerate(thumbs):
        for c, (im, label) in enumerate(row):
            x = c * cell_w + 15
            y = r * cell_h + 35
            draw.text((x, r * cell_h + 8), label, fill=(20, 20, 20))
            sheet.paste(im, (x, y))
    output_path.parent.mkdir(parents=True, exist_ok=True)
    sheet.save(output_path)
    print(f"saved {output_path}")
    return output_path


contact_sheet = make_contact_sheet([gif_07, gif_08, gif_09, gif_10], FIG_DIR / "hierarchical_modeling_contact_sheet.png")
contact_sheet
"""))

cells.append(nbf.v4.new_markdown_cell(r"""## 6. まとめと次に学ぶとよいもの

- **緑本の中核**は、確率分布・尤度・GLM・個体差/過分散・階層ベイズの考え方。
- **Poisson GLM** はカウント、**Logistic GLM** は二値/比率を扱う基本形。
- **階層モデル**は、カテゴリ別推定をノープーリングにせず、全体情報を借りる。小さい群ほど全体へ縮みやすい。
- **ランダム切片/ランダム傾き**は、カテゴリごとの切片・傾きを階層化する GLMM/階層ベイズの入口。

この次に可視化すると理解が進みやすい候補:

1. **過分散**: Poisson で説明できないばらつきを負の二項分布で表す。
2. **ゼロ過剰モデル**: 0 が多すぎるカウントデータを「構造的 0」と「Poisson 由来 0」に分ける。
3. **posterior predictive check**: 推定後、モデルから疑似データを生成し、観測データらしさを確認する。
4. **WAIC/LOO/AIC**: 予測性能でモデル比較する。
5. **状態空間モデル**: 時系列の潜在状態が更新される様子を可視化する。
"""))

nb["cells"] = cells
nbf.write(nb, NOTEBOOK_PATH)
print(NOTEBOOK_PATH)
