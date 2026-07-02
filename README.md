# Bayesian Workflow の例題を PyMC で — ゴルフパッティングと惑星運動

Bayesian Workflow 論文 (Gelman et al. 2020, [arXiv:2011.01808](https://arxiv.org/abs/2011.01808)) で紹介されている
2 つのケーススタディを、公式の Stan 版 (Rmd + Stan) に準拠して PyMC で再実装した Jupyter ノートブック集です。

## ノートブック

| ノートブック | 原典 | 内容 |
|---|---|---|
| [01_golf_putting.ipynb](01_golf_putting.ipynb) | Gelman, [Model building and expansion for golf putting](https://mc-stan.org/users/documentation/case-studies/golf.html) | ロジスティック回帰 → 幾何(第一原理)モデル → 新データでのモデルチェック → 角度+距離モデル(収束失敗とフォーク定理) → 正規近似+誤差項 → 残差分析 → 過剰拡張の実験 |
| [02_planetary_motion.ipynb](02_planetary_motion.ipynb) | Margossian & Gelman, [Bayesian Model of Planetary Motion](https://mc-stan.org/learn-stan/case-studies/planetary_motion.html) | ODE モデルの多峰性。単純化モデルへの後退、チェーン別 PPC、対数結合密度のグリッド計算、モード発生機構の解剖、初期値のチューニング、フルモデルの事前分布設計と条件付き尤度 |

どちらのノートブックも、事前予測チェック・MCMC 収束診断 (R-hat / ESS / divergence / トレース / ランクプロット /
エネルギープロット)・事後予測チェック・LOO によるモデル比較・残差分析といった、
ベイズワークフローの実行に必要な処理を解説付きで含みます。
原典に無い補足ステップには「ワークフロー補足」と明記しています。

## セットアップと実行

[uv](https://docs.astral.sh/uv/) で管理しています (Python 3.12)。

```powershell
uv sync                 # 仮想環境の作成と依存関係のインストール
uv run jupyter lab      # JupyterLab を起動してノートブックを開く
```

コマンドラインから再実行する場合:

```powershell
uv run jupyter nbconvert --to notebook --execute --inplace 01_golf_putting.ipynb
uv run jupyter nbconvert --to notebook --execute --inplace 02_planetary_motion.ipynb
```

### 実装上の注意 (Windows 環境)

- この環境には 64bit C++ コンパイラが無いため、ノートブック冒頭で `PYTENSOR_FLAGS=cxx=` を設定し
  PyTensor の C バックエンドを無効化しています。NUTS サンプリングは JAX (numpyro) 経由で JIT コンパイル
  されるため性能上の問題はありません (`pymc.sampling.jax.sample_jax_nuts` を使用)。
- Stan の適応刻み ODE ソルバー (`integrate_ode_rk45` / `bdf`) の代わりに、惑星運動ノートブックでは
  `pytensor.scan` による固定刻み RK4 を実装しています。この違いが結果に与える影響はノートブック内で
  検証・解説しています。

## ディレクトリ構成

```
├── 01_golf_putting.ipynb        # ゴルフパッティング (実行済み)
├── 02_planetary_motion.ipynb    # 惑星運動 (実行済み)
├── data/                        # ゴルフのデータ (原典リポジトリより)
├── original/                    # 参照用: 公式の Rmd / Stan / データ一式
│   ├── golf/                    #   stan-dev/example-models/knitr/golf
│   └── planetary_motion/        #   stan-dev/example-models/knitr/planetary_motion
└── src/                         # ノートブックを生成するスクリプト
    ├── build_golf.py
    └── build_planetary.py
```

## ライセンス

原典のコードは BSD 3-clause、テキストは CC-BY-NC 4.0 でライセンスされています
([stan-dev/example-models](https://github.com/stan-dev/example-models))。
