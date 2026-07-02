# -*- coding: utf-8 -*-
"""01_golf_putting.ipynb を生成するスクリプト。"""
import nbformat as nbf

md = []
code = []
cells = []


def M(s):
    cells.append(nbf.v4.new_markdown_cell(s.strip()))


def C(s):
    cells.append(nbf.v4.new_code_cell(s.strip()))


# ============================================================
M(r"""
# ゴルフパッティングのモデル構築と拡張 — PyMC によるベイズワークフロー

このノートブックは、Bayesian Workflow 論文 (Gelman et al. 2020, [arXiv:2011.01808](https://arxiv.org/abs/2011.01808)) で紹介されているゴルフパッティングの例を、**公式の Stan ケーススタディに準拠して PyMC で再実装**したものです。

- 原典: Andrew Gelman, ["Model building and expansion for golf putting"](https://mc-stan.org/users/documentation/case-studies/golf.html)
- 公式ソース (Rmd + Stan): [stan-dev/example-models/knitr/golf](https://github.com/stan-dev/example-models/tree/master/knitr/golf)

Stan 版の流れ(モデルの逐次拡張)を忠実に再現しつつ、ベイズワークフローとして必要な処理 —
**事前予測チェック (prior predictive check)・MCMC 収束診断・事後予測チェック (posterior predictive check)・モデル比較 (LOO-CV)・残差分析** —
をすべて解説付きで実行します。原典に含まれない補足ステップには「**ワークフロー補足**」と明記します。

## このノートブックで辿るワークフロー

1. **データの観察** — プロゴルファーのパット成功率 vs 距離
2. **モデル 1: ロジスティック回帰** — 定番の出発点。フィット・診断・事後予測チェック
3. **モデル 2: 第一原理(幾何)モデル** — 角度の物理からモデルを構築。1 パラメータでロジスティックに圧勝
4. **新データによるモデルチェック** — 既存モデルが新データで破綻することを確認
5. **モデル 3: 角度 + 距離モデル(二項尤度)** — 収束が悪化。「統計計算のフォーク定理」
6. **モデル 4: 正規近似 + 独立誤差項** — モデルの不完全さを認める誤差項で解決
7. **残差分析・モデル 5(過剰パラメータ化の実験)** — モデル拡張の限界を知る

> **Stan → PyMC の対応について**: 各モデルの直前に原典の Stan コードを掲載し、PyMC コードとの対応を説明します。
> サンプラーは Stan と同じ NUTS(No-U-Turn Sampler)を使います。この環境では
> `pymc.sampling.jax.sample_jax_nuts`(numpyro バックエンド)を利用します。
""")

C(r"""
import os
# この Windows 環境には 64bit C++ コンパイラが無いため、PyTensor の C バックエンドを無効化する。
# 勾配計算と NUTS サンプリングは JAX (numpyro) 経由で JIT コンパイルされるので性能上の問題はない。
os.environ.setdefault("PYTENSOR_FLAGS", "cxx=")

import warnings
warnings.filterwarnings("ignore", category=UserWarning, module="pytensor")
warnings.filterwarnings("ignore", category=FutureWarning)

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats

import pymc as pm
import pytensor.tensor as pt
import arviz as az
from pymc.sampling.jax import sample_jax_nuts

RANDOM_SEED = 1234
rng = np.random.default_rng(RANDOM_SEED)
plt.rcParams["figure.figsize"] = (7, 4.5)
plt.rcParams["axes.grid"] = True
plt.rcParams["grid.alpha"] = 0.3

print(f"PyMC {pm.__version__} / ArviZ {az.__version__} / NumPy {np.__version__}")
""")

C(r'''
def run_nuts(model, draws=1000, tune=1000, chains=4, seed=RANDOM_SEED, **kwargs):
    """Stan の stan() 呼び出しに相当: NUTS を chains 本走らせて InferenceData を返す。

    Stan のデフォルト (iter=2000, warmup=1000, chains=4) に合わせている。
    chain_method="vectorized" は全チェーンを 1 つの JAX プログラムで回す設定。
    """
    return sample_jax_nuts(
        model=model, nuts_sampler="numpyro",
        draws=draws, tune=tune, chains=chains,
        random_seed=seed, chain_method="vectorized",
        progressbar=False, **kwargs,
    )


def check_sampling(idata, var_names=None):
    """MCMC の基本診断をまとめて表示するヘルパー。

    - divergences: NUTS の発散遷移。事後分布の幾何が悪い(曲率が高い)兆候
    - max tree depth 到達: ステップサイズが小さすぎる/事後分布が広すぎる兆候
    - R-hat: チェーン間・チェーン内の分散比較による収束診断 (1.01 以下が目安)
    - ESS: 実効サンプルサイズ (bulk/tail とも十分大きいこと; 目安はチェーンあたり 100 以上)
    """
    ss = idata.sample_stats
    n_div = int(ss["diverging"].sum())
    summ = az.summary(idata, var_names=var_names)
    # ArviZ 1.x の summary は表示用に整形された文字列を返すことがあるため数値化する
    num = summ.apply(pd.to_numeric, errors="coerce")
    print(f"divergences: {n_div}")
    print(f"max R-hat  : {num['r_hat'].max():.4f}   (< 1.01 が目安)")
    print(f"min ESS    : bulk {num['ess_bulk'].min():.0f} / tail {num['ess_tail'].min():.0f}")
    return summ
''')

# ============================================================
M(r"""
## 1. データ

Berry (1996) によるプロゴルファーのパットデータです。各行が「距離 $x_j$ (フィート)、試行数 $n_j$、成功数 $y_j$」の集計値になっています。

グラフの誤差棒は各点の古典的な標準誤差 $\sqrt{\hat p_j (1-\hat p_j)/n_j}$($\hat p_j = y_j/n_j$)です。
モデルを書く前にまず生データを可視化する — これがワークフローの出発点です。距離とともに成功率が単調に下がる、
という明確な構造が見えます。
""")

C(r'''
golf = pd.read_csv("data/golf_data.txt", skiprows=2, sep=r"\s+")
x, n, y = golf["x"].to_numpy(float), golf["n"].to_numpy(), golf["y"].to_numpy()
J = len(golf)

# ボールとカップの半径 (フィート)。直径はそれぞれ 1.68 インチ、4.25 インチ。
r_ball = (1.68 / 2) / 12
R_hole = (4.25 / 2) / 12

p_hat = y / n
se_hat = np.sqrt(p_hat * (1 - p_hat) / n)
golf.head()
''')

C(r'''
def plot_golf_data(ax, x, y, n, color="C0", label=None):
    p = y / n
    se = np.sqrt(p * (1 - p) / n)
    ax.errorbar(x, p, yerr=se, fmt="o", ms=4, color=color, lw=0.8, label=label)
    ax.set_xlabel("Distance from hole (feet)")
    ax.set_ylabel("Probability of success")
    ax.set_ylim(0, 1.02)

fig, ax = plt.subplots()
plot_golf_data(ax, x, y, n)
for xi, yi, ni in zip(x, y, n):
    ax.annotate(f"{yi}/{ni}", (xi, yi / ni), textcoords="offset points",
                xytext=(6, 6), fontsize=7, color="gray")
ax.set_xlim(0, 1.1 * x.max())
ax.set_title("Data on putts in pro golf")
plt.show()
''')

# ============================================================
M(r"""
## 2. モデル 1: ロジスティック回帰

統計の定石どおり、まずはロジスティック回帰から始めます:

$$
y_j \sim \mathrm{binomial}\bigl(n_j,\ \mathrm{logit}^{-1}(a + b x_j)\bigr), \quad j=1,\dots,J.
$$

原典の Stan コード (`golf_logistic.stan`):

```stan
data {
  int J;
  array[J] int n;
  vector[J] x;
  array[J] int y;
}
parameters {
  real a;
  real b;
}
model {
  y ~ binomial_logit(n, a + b * x);
}
```

**Stan → PyMC の対応**

| Stan | PyMC |
|---|---|
| `parameters { real a; }`(事前分布の記述なし = 暗黙の一様事前分布) | `pm.Flat("a")` |
| `y ~ binomial_logit(n, a + b*x)` | `pm.Binomial("y", n=n, p=pm.math.invlogit(a + b*x), observed=y)` |

Stan では `parameters` ブロックに宣言しただけのパラメータは(非正則な)フラット事前分布を持ちます。
PyMC でこれに忠実に対応するのは `pm.Flat` です。
なお `binomial_logit` は数値安定化された二項ロジットですが、このデータでは通常の `p` 指定で問題ありません。

> **ワークフローの観点**: フラット事前分布は「事前予測チェックができない」(事前分布からサンプルできない)
> という代償を伴います。このモデルはデータが十分あるので問題になりませんが、
> 後のモデルでは弱情報事前分布を置き、事前予測チェックを実演します。
""")

C(r'''
coords = {"distance": x}

with pm.Model(coords=coords) as logistic_model:
    a = pm.Flat("a")
    b = pm.Flat("b")
    p = pm.Deterministic("p", pm.math.invlogit(a + b * x), dims="distance")
    pm.Binomial("y", n=n, p=p, observed=y, dims="distance")

idata_logistic = run_nuts(logistic_model)
''')

M(r"""
### 2.1 サンプリング結果と収束診断

Stan の `print(fit)` に相当するのが `az.summary()` です。列の読み方:

- **mean / sd**: 事後平均と事後標準偏差
- **mcse_mean**: 事後平均のモンテカルロ標準誤差。十分小さければ「シミュレーションを十分回した」ことを意味する
- **ess_bulk / ess_tail**: 実効サンプルサイズ。分布の中心部(bulk)と裾(tail)それぞれの推定精度の指標
- **r_hat**: Gelman-Rubin 統計量 $\widehat R$ の改良版 (Vehtari et al. 2021)。チェーン間で分布が一致していれば 1 に近づく。**1.01 以下**が目安

Stan 版の結果は $a = 2.23 \pm 0.06$、$b = -0.26 \pm 0.01$ でした。同じ値が再現されるはずです。
""")

C(r'''
check_sampling(idata_logistic, var_names=["a", "b"])
''')

M(r"""
### 2.2 ワークフロー補足: 収束診断の可視化

$\widehat R$ の数値だけでなく、必ず可視化でも確認します。

- **トレースプロット**: 各チェーンの軌跡。チェーン同士が重なり合い、白色雑音のように見えれば良好
- **ランクプロット**: 全チェーンを混ぜて順位づけしたときの各チェーンの順位ヒストグラム。一様なら混合良好($\widehat R$ より鋭敏な診断)
- **エネルギープロット**: HMC のエネルギー遷移分布と周辺エネルギー分布の比較。両者が大きくずれる(BFMI が低い)と裾の探索が不十分
""")

C(r'''
az.plot_trace(idata_logistic, var_names=["a", "b"]);
''')

C(r'''
az.plot_rank(idata_logistic, var_names=["a", "b"]);
''')

C(r'''
az.plot_energy(idata_logistic);
''')

M(r"""
### 2.3 フィットの可視化

黒線が事後中央値、緑の細線が事後分布からの 10 ドロー分の曲線です。データ点が多いため事後の不確実性は小さく、
以降のモデルでは(原典と同じく)事後中央値の曲線のみを描きます。
""")

C(r'''
post_log = idata_logistic.posterior
a_hat = float(post_log["a"].median())
b_hat = float(post_log["b"].median())

def invlogit(z):
    return 1 / (1 + np.exp(-z))

x_grid_plot = np.linspace(0, 1.1 * x.max(), 200)

fig, ax = plt.subplots()
# 事後分布から 10 ドロー
a_draws = post_log["a"].values.ravel()
b_draws = post_log["b"].values.ravel()
idx = rng.choice(a_draws.size, 10, replace=False)
for i in idx:
    ax.plot(x_grid_plot, invlogit(a_draws[i] + b_draws[i] * x_grid_plot),
            color="green", lw=0.5, alpha=0.7)
ax.plot(x_grid_plot, invlogit(a_hat + b_hat * x_grid_plot), color="black")
plot_golf_data(ax, x, y, n)
ax.set_xlim(0, 1.1 * x.max())
ax.set_title("Fitted logistic regression")
ax.text(11, 0.57, f"Logistic regression,\n a = {a_hat:.2f}, b = {b_hat:.2f}")
plt.show()
''')

M(r"""
### 2.4 ワークフロー補足: 事後予測チェック (PPC)

Stan の `generated quantities` で `binomial_rng` を書くことに相当するのが `pm.sample_posterior_predictive` です。
「フィットしたモデルからデータを複製生成し、実データと比べる」ことで、モデルがデータのどの側面を再現できて
いないかを調べます。ここでは各距離での複製成功率 $y^{\rm rep}_j/n_j$ の 50%/95% 区間と観測値を重ねます。

観測点が区間から系統的に外れる箇所(特に中距離で観測が区間の外に出る傾向)に注目してください —
ロジスティック曲線の形がデータと合っていないことが分かります。
""")

C(r'''
with logistic_model:
    ppc_logistic = pm.sample_posterior_predictive(
        idata_logistic, random_seed=RANDOM_SEED, progressbar=False)

def plot_ppc_intervals(ax, ppc, x, y, n, var="y", color="C0"):
    """複製データ y_rep/n の 50% / 95% 区間と観測値を距離ごとに描く。"""
    yrep = ppc.posterior_predictive[var].values.reshape(-1, len(x))  # (draws, J)
    prep = yrep / n
    q = np.percentile(prep, [2.5, 25, 75, 97.5], axis=0)
    ax.vlines(x, q[0], q[3], color=color, alpha=0.3, lw=2, label="95% PPC interval")
    ax.vlines(x, q[1], q[2], color=color, alpha=0.7, lw=4, label="50% PPC interval")
    ax.plot(x, y / n, "ko", ms=4, zorder=5, label="observed")
    ax.set_xlabel("Distance from hole (feet)")
    ax.set_ylabel("Probability of success")
    ax.legend()

fig, ax = plt.subplots()
plot_ppc_intervals(ax, ppc_logistic, x, y, n)
ax.set_title("Posterior predictive check: logistic regression")
plt.show()
''')

# ============================================================
M(r"""
## 3. モデル 2: 第一原理からの幾何モデル

ロジスティック回帰の代わりに、**パットの物理**からモデルを組み立てます。

半径 $r$ のボールが半径 $R$ のカップに入るには、ショットの角度が閾値
$\theta_j = \sin^{-1}\bigl((R-r)/x_j\bigr)$ より小さくなければなりません。
ゴルファーはまっすぐ打とうとするが小さな誤差が入る、として実際の角度を
平均 0、標準偏差 $\sigma$ の正規分布でモデル化すると、成功確率は

$$
p_j = \Pr\bigl(|\mathrm{angle}| < \theta_j\bigr)
    = 2\Phi\!\left(\frac{\sin^{-1}((R-r)/x_j)}{\sigma}\right) - 1
$$

($\Phi$ は標準正規の累積分布関数)。モデル全体は

$$
y_j \sim \mathrm{binomial}(n_j, p_j), \qquad
p_j = 2\Phi\!\left(\frac{\sin^{-1}((R-r)/x_j)}{\sigma}\right) - 1.
$$

未知パラメータは $\sigma$ ただ 1 つです。
""")

C(r'''
# 幾何の模式図 (原典の図の再現; 縮尺は誇張)
fig, ax = plt.subplots(figsize=(8, 2.2))
dist = 2.0
ax.add_patch(plt.Circle((0, 0), r_ball, fill=False))
ax.add_patch(plt.Circle((dist, 0), R_hole, fill=False))
ax.add_patch(plt.Circle((dist, 0), R_hole - r_ball, fill=False, ls="--"))
ax.plot([0, dist], [0, 0], "k-", lw=0.8)
ax.plot([0, dist], [0, (R_hole - r_ball)], "k--", lw=0.8)
ax.plot([0, dist], [0, -(R_hole - r_ball)], "k--", lw=0.8)
ax.annotate("", xy=(dist, -0.3), xytext=(0, -0.3),
            arrowprops=dict(arrowstyle="<->", lw=0.8))
ax.text(dist / 2, -0.42, "x", ha="center")
ax.text(dist + 0.25, 0.05, "R")
ax.text(-0.02, 0.12, "r")
ax.set_xlim(-0.3, dist + 0.6)
ax.set_ylim(-0.55, 0.4)
ax.set_aspect("equal")
ax.axis("off")
ax.set_title("Geometry of the golf shot (not to scale)")
plt.show()
''')

M(r"""
$\sigma$ をいくつか仮置きして成功確率曲線を描いてみます(**これは事前予測チェックの発想そのもの**です:
パラメータの各値がどんなデータ生成過程を意味するかをフィット前に把握しておく)。
$\sigma = 0.5°$ なら 10 フィートのパットを 80% 以上沈める超人、$\sigma = 20°$ なら 2 フィートすら半分外す、
という具合に、パラメータが物理的に解釈できます。
""")

C(r'''
def p_angle_np(x_grid, sigma_rad):
    """幾何モデルの成功確率 (numpy 版)。x < R-r では必ず成功 (p=1)。"""
    x_grid = np.asarray(x_grid, float)
    p = np.ones_like(x_grid)
    far = x_grid > (R_hole - r_ball)
    p[far] = 2 * stats.norm.cdf(np.arcsin((R_hole - r_ball) / x_grid[far]) / sigma_rad) - 1
    return p

x_grid = np.linspace(1e-4, 1.1 * x.max(), 300)
fig, ax = plt.subplots()
for sd_deg, x_text in zip([0.5, 1, 2, 5, 20], [15, 10, 6, 4, 2]):
    sigma_rad = np.deg2rad(sd_deg)
    ax.plot(x_grid, p_angle_np(x_grid, sigma_rad), "k-", lw=1)
    ax.text(x_text + 0.7, p_angle_np([x_text], sigma_rad)[0], f"$\\sigma={sd_deg}°$")
ax.set_xlim(0, 1.1 * x.max()); ax.set_ylim(0, 1.02)
ax.set_xlabel("Distance from hole (feet)")
ax.set_ylabel("Probability of success")
ax.set_title("Modeled Pr(success) for different values of $\\sigma$")
plt.show()
''')

M(r"""
原典の Stan コード (`golf_angle.stan`):

```stan
data {
  int J;
  array[J] int n;
  vector[J] x;
  array[J] int y;
  real r;
  real R;
}
transformed data {
  vector[J] threshold_angle = asin((R - r) ./ x);
}
parameters {
  real<lower=0> sigma;
}
model {
  vector[J] p = 2 * Phi(threshold_angle / sigma) - 1;
  y ~ binomial(n, p);
}
generated quantities {
  real sigma_degrees = sigma * 180 / pi();
}
```

**Stan → PyMC の対応**

| Stan | PyMC |
|---|---|
| `transformed data`(データから決まる定数) | モデル外で numpy により計算 |
| `real<lower=0> sigma;`(事前分布なし = 正の範囲の暗黙フラット事前分布) | `pm.HalfFlat("sigma")` |
| `Phi(z)`(標準正規 CDF) | `pm.math.invprobit(z)` |
| `generated quantities` の `sigma_degrees` | `pm.Deterministic("sigma_degrees", ...)` |
""")

C(r'''
threshold_angle = np.arcsin((R_hole - r_ball) / x)

with pm.Model(coords=coords) as angle_model:
    sigma = pm.HalfFlat("sigma")
    p = pm.Deterministic(
        "p", 2 * pm.math.invprobit(threshold_angle / sigma) - 1, dims="distance")
    pm.Binomial("y", n=n, p=p, observed=y, dims="distance")
    pm.Deterministic("sigma_degrees", sigma * 180 / np.pi)

idata_angle = run_nuts(angle_model)
check_sampling(idata_angle, var_names=["sigma", "sigma_degrees"])
''')

C(r'''
az.plot_trace(idata_angle, var_names=["sigma", "sigma_degrees"]);
''')

M(r"""
Stan 版では $\sigma = 0.0267$ rad(= $1.53°$)、事後標準偏差 $0.02°$ という非常にシャープな推定が得られました。
データ数が多く 1 パラメータのモデルなので当然です。上の要約が再現していることを確認してください。

2 つのモデルのフィットを重ねると、**幾何モデルが圧倒的に良い**ことが一目で分かります。
物理を 1 行の式に落としただけの 1 パラメータモデルが、2 パラメータの汎用回帰モデルに勝つ —
「第一原理からのモデル構築」の威力です。
""")

C(r'''
sigma_hat = float(idata_angle.posterior["sigma"].median())

fig, ax = plt.subplots()
plot_golf_data(ax, x, y, n)
ax.plot(x_grid_plot, invlogit(a_hat + b_hat * x_grid_plot), "k-", label="Logistic regression")
ax.plot(x_grid, p_angle_np(x_grid, sigma_hat), "C0-", label="Geometry-based model")
ax.set_xlim(0, 1.1 * x.max())
ax.legend()
ax.set_title("Two models fit to the golf putting data")
plt.show()
''')

M(r"""
### 3.1 ワークフロー補足: PSIS-LOO によるモデル比較

視覚的な比較を、**leave-one-out 交差検証 (PSIS-LOO)** で定量化します。
`elpd_loo`(期待対数予測密度)が高いほど、新しいデータ点に対する予測が良いモデルです。

注意点:

- 比較するモデルは**同じ観測データ・同じ尤度の単位**を持つ必要があります(ここでは両モデルとも同じ 19 個の二項観測なので OK)
- `pareto_k` 診断が悪い (> 0.7) 点があれば LOO 近似自体が信頼できません
""")

C(r'''
idata_logistic = pm.compute_log_likelihood(idata_logistic, model=logistic_model, progressbar=False)
idata_angle = pm.compute_log_likelihood(idata_angle, model=angle_model, progressbar=False)

comp = az.compare({"logistic": idata_logistic, "geometry (angle)": idata_angle})
comp
''')

C(r'''
az.plot_compare(comp);
''')

M(r"""
`elpd_diff` は幾何モデル優位(差はおよそ 2 `dse`)で、重み (`weight`) も幾何モデルに大きく割り当てられています。

ただし出力の `k̂ > 0.70` 列に注意してください — 両モデルとも Pareto-$\hat k$ 診断に引っかかる観測点があります。
$n_j$ が大きい二項観測は 1 点 1 点の影響が大きく、PSIS-LOO の重要度サンプリング近似が不安定になりやすいのです。
このような場合、LOO の数値は「参考値」に格下げし、視覚的なフィットの比較・事後予測チェックと合わせて判断します
(今回はどの証拠も幾何モデルを支持しており、結論は変わりません)。診断が警告を出したときに数値を鵜呑みにしない —
これもワークフローの一部です。

### 3.2 幾何モデルの事後予測チェック
""")

C(r'''
with angle_model:
    ppc_angle = pm.sample_posterior_predictive(
        idata_angle, random_seed=RANDOM_SEED, progressbar=False)

fig, ax = plt.subplots()
plot_ppc_intervals(ax, ppc_angle, x, y, n)
ax.set_title("Posterior predictive check: geometry-based model")
plt.show()
''')

M(r"""
ロジスティック回帰よりはるかに良いものの、よく見るといくつかの距離で観測値が 95% 区間の外に出ています。
$n_j$ が大きいため二項分布の分散が小さく、わずかな系統誤差でも「統計的には」検出されるのです。
この伏線は新データで一気に顕在化します。

## 4. 新データでモデルをチェックする

Mark Broadie による新しい大規模データ(最長 75 フィート、試行数は桁違いに多い)が手に入りました。
**既にフィット済みのモデルを新データと照合する**のは最も厳しいモデルチェックです。
""")

C(r'''
golf_new = pd.read_csv("data/golf_data_new.txt", skiprows=2, sep=r"\s+")
x_new = golf_new["x"].to_numpy(float)
n_new = golf_new["n"].to_numpy()
y_new = golf_new["y"].to_numpy()
J_new = len(golf_new)

x_grid_new = np.linspace(1e-4, 1.1 * x_new.max(), 400)

fig, ax = plt.subplots()
ax.plot(x_grid_new, p_angle_np(x_grid_new, sigma_hat), "C0-", label="Geometry model (fit to old data)")
ax.plot(x, y / n, "o", color="C0", ms=4, label="Old data")
ax.plot(x_new, y_new / n_new, "o", color="C3", ms=4, label="New data")
ax.set_xlim(0, 1.1 * x_new.max()); ax.set_ylim(0, 1.02)
ax.set_xlabel("Distance from hole (feet)")
ax.set_ylabel("Probability of success")
ax.set_title("Checking already-fit model to new data")
ax.legend()
plt.show()
''')

M(r"""
観察されること(原典の議論):

- **0–20 フィート**: 短いパットの成功率が旧データより明らかに高い。旧データの距離測定が粗かった可能性や、ゴルファーの技術向上が考えられる
- **20 フィート以遠**: 実際の成功率はモデルの予測より低い。距離が伸びると角度の精度だけでは説明できない難しさがある

→ **角度だけでなく「打つ強さ」もモデル化する必要がある**、という結論に至ります。

## 5. モデル 3: 打つ強さ(距離コントロール)を加える

Broadie のモデル: ショットが(カップが無ければ)進む距離を $u$ とし、

- 角度条件: これまでと同じ
- 距離条件: $u \in [x, x+3]$(カップに届き、かつ 3 フィート以上通り過ぎない)

ゴルファーはカップの 1 フィート先を狙い、距離には相対誤差が乗るとして
$u \sim \mathrm{normal}\bigl(x+1,\ (x+1)\sigma_{\rm distance}\bigr)$。距離条件を満たす確率は

$$
\Phi\!\left(\frac{2}{(x+1)\sigma_{\rm distance}}\right) - \Phi\!\left(\frac{-1}{(x+1)\sigma_{\rm distance}}\right)
$$

成功確率は角度確率との積になります。原典の Stan コード (`golf_angle_distance_2.stan`):

```stan
data {
  ...
  real overshot;            // = 1
  real distance_tolerance;  // = 3
}
transformed data {
  vector[J] threshold_angle = asin((R - r) ./ x);
}
parameters {
  real<lower=0> sigma_angle;
  real<lower=0> sigma_distance;
}
model {
  vector[J] p_angle = 2 * Phi(threshold_angle / sigma_angle) - 1;
  vector[J] p_distance = Phi((distance_tolerance - overshot)
                             ./ ((x + overshot) * sigma_distance))
                         - Phi((-overshot) ./ ((x + overshot) * sigma_distance));
  vector[J] p = p_angle .* p_distance;
  y ~ binomial(n, p);
  [sigma_angle, sigma_distance] ~ normal(0, 1);
}
```

今回は計算を安定させるため、スケールパラメータに**弱情報事前分布** half-normal(0, 1) が置かれています
(`<lower=0>` 制約 + `normal(0,1)` = PyMC の `pm.HalfNormal(sigma=1)`)。
""")

C(r'''
overshot = 1.0
distance_tolerance = 3.0

def p_success_pt(x_arr, sigma_angle, sigma_distance):
    """角度 + 距離モデルの成功確率 (PyTensor 版)。Stan の model ブロックと同じ式。"""
    thr = np.arcsin((R_hole - r_ball) / x_arr)
    p_angle = 2 * pm.math.invprobit(thr / sigma_angle) - 1
    denom = (x_arr + overshot) * sigma_distance
    p_distance = (pm.math.invprobit((distance_tolerance - overshot) / denom)
                  - pm.math.invprobit(-overshot / denom))
    return p_angle * p_distance

def p_success_np(x_grid, sigma_angle, sigma_distance):
    """同 (numpy 版、プロット用)。x < R-r では p_angle = 1。"""
    pa = p_angle_np(x_grid, sigma_angle)
    denom = (np.asarray(x_grid) + overshot) * sigma_distance
    pd_ = (stats.norm.cdf((distance_tolerance - overshot) / denom)
           - stats.norm.cdf(-overshot / denom))
    return pa * pd_
''')

M(r"""
### 5.1 ワークフロー補足: 事前予測チェック

事前分布が意味のあるデータ生成過程を含意しているかを、**フィット前に**確認します。
half-normal(0,1) 事前分布から $(\sigma_{\rm angle}, \sigma_{\rm distance})$ を引き、
含意される成功確率曲線を描きます。

見るべきポイント:

- 曲線群が「もっともらしい世界」(単調減少、近距離ほど成功率が高い)を広くカバーしているか
- ありえない世界(全距離で成功率 0 や 1 に張り付くなど)ばかりに事前確率を割いていないか

$\sigma_{\rm angle} \sim {\rm half\text{-}normal}(0,1)$ はラジアン単位で最大 57° 程度の巨大な角度誤差まで許す、
かなり緩い事前分布であることが分かります。それでも曲線の形は幾何によって強く制約されています。
""")

C(r'''
prior_sa = np.abs(rng.normal(0, 1, 100))
prior_sd = np.abs(rng.normal(0, 1, 100))

fig, ax = plt.subplots()
for sa, sd_ in zip(prior_sa, prior_sd):
    ax.plot(x_grid_new, p_success_np(x_grid_new, sa, sd_), color="C2", alpha=0.2, lw=0.7)
ax.plot(x_new, y_new / n_new, "o", color="C3", ms=3, zorder=5, label="New data")
ax.set_xlim(0, 1.1 * x_new.max()); ax.set_ylim(0, 1.02)
ax.set_xlabel("Distance from hole (feet)")
ax.set_ylabel("Probability of success")
ax.set_title("Prior predictive check: implied success curves\n(100 draws from the half-normal(0,1) priors)")
ax.legend()
plt.show()
''')

M(r"""
### 5.2 新データへのフィット — 収束の失敗

新データにこのモデルをフィットします。原典では**ここで収束が悪化**します
($\widehat R$ が 1 を大きく超える)。

> "Problems with computation often indicate underlying problems with the model being fit.
> That's the **folk theorem of statistical computing**."
> (計算の問題は、フィットしようとしているモデル自体の問題を示していることが多い — 統計計算のフォーク定理)
""")

C(r'''
coords_new = {"distance": x_new}

with pm.Model(coords=coords_new) as angle_distance_2:
    sigma_angle = pm.HalfNormal("sigma_angle", 1)
    sigma_distance = pm.HalfNormal("sigma_distance", 1)
    p = pm.Deterministic("p", p_success_pt(x_new, sigma_angle, sigma_distance),
                         dims="distance")
    pm.Binomial("y", n=n_new, p=p, observed=y_new, dims="distance")
    pm.Deterministic("sigma_degrees", sigma_angle * 180 / np.pi)

idata_ad2 = run_nuts(angle_distance_2)
summ_ad2 = check_sampling(idata_ad2, var_names=["sigma_angle", "sigma_distance", "sigma_degrees"])
summ_ad2
''')

C(r'''
az.plot_trace(idata_ad2, var_names=["sigma_angle", "sigma_distance"]);
''')

M(r"""
診断を確認してください。この問題の症状はサンプラーの実装により多少異なりますが
(Stan 版では $\widehat R \approx 1.5$ 程度の明確な混合不良)、
divergence・低い ESS・チェーン間の不一致など、**何らかの計算上の悲鳴**が上がるはずです。

とりあえずの(信頼できない)フィットを描いて何が起きているか見てみます:
""")

C(r'''
sa_hat = float(idata_ad2.posterior["sigma_angle"].median())
sd_hat = float(idata_ad2.posterior["sigma_distance"].median())

fig, ax = plt.subplots()
ax.plot(x_grid_new, p_success_np(x_grid_new, sa_hat, sd_hat), "C3-", label="Provisional fit")
ax.plot(x_new, y_new / n_new, "o", color="C3", ms=4)
ax.set_xlim(0, 1.1 * x_new.max()); ax.set_ylim(0, 1.02)
ax.set_xlabel("Distance from hole (feet)")
ax.set_ylabel("Probability of success")
ax.set_title("Checking (provisional) model fit")
ax.legend()
plt.show()
''')

C(r'''
golf_new.head()
''')

M(r"""
**中距離帯でフィットが系統的にずれています**。原因はデータの先頭数行を見ると分かります:
$n_j$ が数万〜数十万と巨大なため、二項尤度は最初の数点(短距離)を**ほぼ完璧に**フィットすることを強要し、
それがモデル全体のフィットを歪めているのです。曲線が最短距離の点に張り付いていることに注目してください。

モデルは近似にすぎないのに、尤度が「モデルは正確である」と主張してしまっている —
これがフォーク定理の言う「モデルの問題」です。

## 6. モデル 4: 正規近似 + 独立誤差項

解決策として、二項データ分布を正規分布で近似し、**モデルの誤設定を吸収する独立誤差 $\sigma_y$** を加えます:

$$
y_j/n_j \sim \mathrm{normal}\!\left(p_j,\ \sqrt{p_j(1-p_j)/n_j + \sigma_y^2}\right)
$$

(ベータ二項分布による過分散化では分散が $n_j$ に比例したままなので目的に合わない、という原典の議論に注意。)

原典の Stan コード (`golf_angle_distance_3.stan`) の要点:

```stan
transformed data {
  vector[J] raw_proportions = to_vector(y) ./ to_vector(n);
}
parameters {
  real<lower=0> sigma_angle;
  real<lower=0> sigma_distance;
  real<lower=0> sigma_y;
}
model {
  ...
  raw_proportions ~ normal(p, sqrt(p .* (1 - p) ./ to_vector(n) + sigma_y ^ 2));
  [sigma_angle, sigma_distance, sigma_y] ~ normal(0, 1);
}
```

PyMC では観測値を連続量 `raw_proportions` にした `pm.Normal` になります。
残差分析のため、原典の `golf_angle_distance_3_with_resids.stan` と同様に
残差 $y_j/n_j - p_j$ も `Deterministic` として保存しておきます。
""")

C(r'''
raw_proportions = y_new / n_new

with pm.Model(coords=coords_new) as angle_distance_3:
    sigma_angle = pm.HalfNormal("sigma_angle", 1)
    sigma_distance = pm.HalfNormal("sigma_distance", 1)
    sigma_y = pm.HalfNormal("sigma_y", 1)
    p = pm.Deterministic("p", p_success_pt(x_new, sigma_angle, sigma_distance),
                         dims="distance")
    sd_total = pm.math.sqrt(p * (1 - p) / n_new + sigma_y**2)
    pm.Normal("obs_prop", mu=p, sigma=sd_total, observed=raw_proportions, dims="distance")
    pm.Deterministic("sigma_degrees", sigma_angle * 180 / np.pi)
    pm.Deterministic("residual", raw_proportions - p, dims="distance")

idata_ad3 = run_nuts(angle_distance_3)
check_sampling(idata_ad3, var_names=["sigma_angle", "sigma_distance", "sigma_y", "sigma_degrees"])
''')

C(r'''
az.plot_trace(idata_ad3, var_names=["sigma_angle", "sigma_distance", "sigma_y"]);
''')

M(r"""
今度は診断がすべてクリーンなはずです。Stan 版の推定値と比べてみましょう:

- $\sigma_{\rm angle} \approx 0.018$ rad → $\sigma_{\rm degrees} \approx 1.0°$。角度だけのモデル ($1.53°$) より小さくなった。
  距離誤差がモデルに入ったことで、ミスの全てを角度で説明する必要がなくなったため
- $\sigma_{\rm distance} \approx 0.08$: 距離の相対誤差は標準偏差 8%
- $\sigma_y \approx 0.003$: 集計データを 0.3 パーセントポイントの精度でフィットしている
""")

C(r'''
post3 = idata_ad3.posterior
sa3 = float(post3["sigma_angle"].median())
sd3 = float(post3["sigma_distance"].median())

fig, ax = plt.subplots()
ax.plot(x_grid_new, p_success_np(x_grid_new, sa3, sd3), "C3-", label="Fitted model")
ax.plot(x_new, y_new / n_new, "o", color="C3", ms=4)
ax.set_xlim(0, 1.1 * x_new.max()); ax.set_ylim(0, 1.02)
ax.set_xlabel("Distance from hole (feet)")
ax.set_ylabel("Probability of success")
ax.set_title("Checking model fit (normal approx. + error term)")
ax.legend()
plt.show()
''')

M(r"""
### 6.1 残差プロット

`Deterministic` に保存した残差 $y_j/n_j - p_j$ の事後平均を距離に対して描きます。
""")

C(r'''
resid_mean = post3["residual"].mean(dim=("chain", "draw")).values

fig, ax = plt.subplots()
ax.axhline(0, color="gray", ls="--", lw=0.8)
ax.plot(x_new, resid_mean, "o-", ms=4)
ax.set_xlabel("Distance from hole (feet)")
ax.set_ylabel("y/n - fitted E(y/n)")
ax.set_title("Residuals from fitted model")
plt.show()
''')

M(r"""
残差は小さく($y$ 軸のスケールに注意)、明確なパターンもありません。モデルが完璧という意味ではなく、
**このデータからこれ以上モデルを発展させる手がかりが無い**、ということです。

### 6.2 事後予測チェック

正規尤度モデルの複製データ $\,(y/n)^{\rm rep}$ を生成して観測と比べます。
今回は観測点がほぼすべて区間内に収まるはずです。
""")

C(r'''
with angle_distance_3:
    ppc_ad3 = pm.sample_posterior_predictive(
        idata_ad3, random_seed=RANDOM_SEED, progressbar=False)

prep = ppc_ad3.posterior_predictive["obs_prop"].values.reshape(-1, J_new)
q = np.percentile(prep, [2.5, 25, 75, 97.5], axis=0)

fig, ax = plt.subplots()
ax.vlines(x_new, q[0], q[3], color="C1", alpha=0.4, lw=2, label="95% PPC interval")
ax.vlines(x_new, q[1], q[2], color="C1", alpha=0.9, lw=4, label="50% PPC interval")
ax.plot(x_new, raw_proportions, "ko", ms=3, zorder=5, label="observed")
ax.set_xlabel("Distance from hole (feet)")
ax.set_ylabel("Probability of success")
ax.set_title("Posterior predictive check: model with error term")
ax.legend()
plt.show()
''')

M(r"""
> **注意 (ワークフロー補足)**: モデル 3(二項尤度)とモデル 4(正規尤度)は**観測データの定義が異なる**
> (整数カウント vs 比率)ため、LOO/WAIC で直接比較することはできません。
> 尤度の単位が変わるモデル改訂では、比較は予測チェックと残差のような実質的な基準で行います。
> これはワークフローでやりがちな失敗ポイントです。

## 7. モデルの問題点と、あえてやってみる拡張(モデル 5)

誤差項 $\sigma_y$ は「ハック」です。系統誤差を独立誤差として扱うのは正しくありませんが、
誤差が 1 パーセントポイント未満と小さいため実害はありません。

固定していた `overshot`(狙いの行き過ぎ距離 = 1 フィート)と `distance_tolerance`(許容範囲 = 3 フィート)を
**データから推定したらどうなるか**、原典は「just for laughs(お遊びで)」試しています。
`golf_angle_distance_4.stan` では 2 つを parameters ブロックに移し、弱い事前分布を置きます:

```stan
parameters {
  ...
  real<lower=0> overshot;
  real<lower=0> distance_tolerance;
}
model {
  ...
  overshot ~ normal(1, 5);
  distance_tolerance ~ normal(3, 5);
}
```

モデルは既にデータをほぼ完璧にフィットしているので、追加パラメータを推定する情報はもう残っていません。
**収束が悪化し、得るものは何もない**はず — 確かめます。
""")

C(r'''
with pm.Model(coords=coords_new) as angle_distance_4:
    sigma_angle = pm.HalfNormal("sigma_angle", 1)
    sigma_distance = pm.HalfNormal("sigma_distance", 1)
    sigma_y = pm.HalfNormal("sigma_y", 1)
    overshot_p = pm.TruncatedNormal("overshot", mu=1, sigma=5, lower=0)
    dtol_p = pm.TruncatedNormal("distance_tolerance", mu=3, sigma=5, lower=0)

    thr = np.arcsin((R_hole - r_ball) / x_new)
    p_angle = 2 * pm.math.invprobit(thr / sigma_angle) - 1
    denom = (x_new + overshot_p) * sigma_distance
    p_dist = (pm.math.invprobit((dtol_p - overshot_p) / denom)
              - pm.math.invprobit(-overshot_p / denom))
    p = pm.Deterministic("p", p_angle * p_dist, dims="distance")
    sd_total = pm.math.sqrt(p * (1 - p) / n_new + sigma_y**2)
    pm.Normal("obs_prop", mu=p, sigma=sd_total, observed=raw_proportions, dims="distance")

idata_ad4 = run_nuts(angle_distance_4)
check_sampling(idata_ad4, var_names=["sigma_angle", "sigma_distance", "sigma_y",
                                     "overshot", "distance_tolerance"])
''')

C(r'''
az.plot_trace(idata_ad4, var_names=["overshot", "distance_tolerance"]);
''')

C(r'''
# パラメータ間の相関を見る: 弱識別性の可視化
az.plot_pair(idata_ad4, var_names=["sigma_distance", "overshot", "distance_tolerance"]);
''')

M(r"""
ペアプロットを見ると、`overshot`・`distance_tolerance`・`sigma_distance` の間に強い依存構造があり、
データがこれらを個別に識別できていないことが分かります。推定値はノイズまみれで不安定
(事前分布が弱ければ)か、事前分布に強く依存する(事前分布が強ければ)かのどちらかで、
どちらにしても得るものがありません。

> **ワークフローの教訓**: モデル拡張は「できるから」ではなく「データが情報を持っているから」行う。
> 予測チェックと残差が「これ以上手がかりなし」と言っているときに追加したパラメータは、
> 計算の不安定化という形で仕返ししてくる(フォーク定理ふたたび)。

## 8. まとめ

| モデル | データ | 尤度 | パラメータ | 結果 |
|---|---|---|---|---|
| `golf_logistic` | 旧 | binomial-logit | $a, b$ | 収束OK、フィット不良 |
| `golf_angle` | 旧 | binomial | $\sigma$ | 収束OK、良好($\sigma \approx 1.53°$) |
| `golf_angle`(チェック) | 新 | — | — | 長距離で破綻 → 拡張の動機 |
| `golf_angle_distance_2` | 新 | binomial | $\sigma_{\rm angle}, \sigma_{\rm distance}$ | **収束不良**(巨大 $n$ + モデル誤設定) |
| `golf_angle_distance_3` | 新 | normal 近似 + $\sigma_y$ | 3 個 | 収束OK、フィット良好 |
| `golf_angle_distance_4` | 新 | 同上 + 2 パラメータ推定 | 5 個 | **収束不良**、得るものなし |

このケーススタディに凝縮されたワークフローの原則:

1. **可視化から始める** — モデルの前にデータを見る
2. **第一原理のモデルは強い** — 解釈可能なパラメータ、少ない自由度、良い外挿
3. **新データはモデルチェックの金の基準** — 内挿の良さは外挿の良さを保証しない
4. **計算の失敗はモデルの警告**(フォーク定理) — divergence や $\widehat R$ を「邪魔なエラー」でなく診断情報として読む
5. **モデルの不完全さを明示的にモデル化する**($\sigma_y$)ことで、巨大データの尤度の暴走を抑える
6. **拡張には限界がある** — データが答えられない質問をモデルにさせない

### 参考文献

- Gelman, A. et al. (2020). Bayesian Workflow. [arXiv:2011.01808](https://arxiv.org/abs/2011.01808)
- Berry, D. (1996). *Statistics: A Bayesian Perspective*. Duxbury Press.(旧データの出典)
- Broadie, M. (2018). Two simple putting models in golf.(新データとモデルの出典)
- Gelman, A. and Nolan, D. (2002). A probability model for golf putting. *Teaching Statistics* 50, 151–153.
- Vehtari, A. et al. (2021). Rank-normalization, folding, and localization: An improved $\widehat R$. *Bayesian Analysis*.

原典のコードは BSD 3-clause、テキストは CC-BY-NC 4.0 でライセンスされています。
""")

nb = nbf.v4.new_notebook()
nb.cells = cells
nb.metadata["kernelspec"] = {
    "name": "python3", "display_name": "Python 3 (ipykernel)", "language": "python"}
nb.metadata["language_info"] = {"name": "python"}

out = "01_golf_putting.ipynb"
nbf.write(nb, out)
print(f"written: {out} ({len(cells)} cells)")
