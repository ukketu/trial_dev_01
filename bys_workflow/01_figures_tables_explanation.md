# Bayesian Workflow：図表抽出ベースの実務解説

## 0. 出典・権利方針

- 公式公開サイト: <https://avehtari.github.io/Bayesian-Workflow/>
- 公式リポジトリ: <https://github.com/avehtari/Bayesian-Workflow> / 確認コミット `eb00fa4397314ef7d90203382542bd44c590e289`
- 公式サイトの `index.qmd` は `Published by CRC Press in 2026. Copyright by the authors.` と明記している。リポジトリ直下に本文・図表再配布を許す明示LICENSEは見つからなかった。
- そのため、このMarkdownではCRC Press版/公式サイトの画像バイナリをコピーせず、公式ページへのリンク・図表ID・caption/周辺文脈・実務上の読み方を記録する。
- 本ファイルは翻訳本文ではなく、図表カタログと実務解説である。逐語本文訳は `02_four_line_chunk_translation_arxiv2011.md` 側で、CC-BY 4.0 のarXiv論文版を対象にした。

## 1. 抽出サマリー

- 調査ページ数: **29ページ**
- 図: **384件**
- 単独画像: **1件**
- HTML表: **78件**
- 合計: **463件**
- 機械可読カタログ: [`data/official_site_figures_tables_catalogue.csv`](data/official_site_figures_tables_catalogue.csv)
- 元インベントリJSON: [`figure_table_inventory.json`](figure_table_inventory.json)

## 2. 図表から逆算した Bayesian Workflow の実務構造

| フェーズ | 件数 | 実務での読み方 | MLflowで紐づけるもの |
|---|---:|---|---|
| EDA / observed data | 130 | モデル化前に、観測単位・外れ値・欠測・群構造・時系列性・上限/下限などを確認する。MLflowではデータ版と前処理版を固定する。 | `dataset_uri, dataset_hash, preprocessing_version, n_obs, group_count` |
| Posterior summary / effect interpretation | 109 | 推定効果・不確実性・派生量を意思決定に接続する。平均だけでなく区間・分布・実務閾値超過確率を残す。 | `posterior_draws_uri, model_code_hash, ci_width, decision_threshold_prob` |
| Posterior predictive checking / calibration | 93 | モデルが再現すべき特徴を外していないか確認する。PPC統計量と図をartifact化し、モデル改善の根拠にする。 | `ppc_stat_*, loo_pit_ecdf_maxdev, calibration_error, replicated_seed` |
| Model development / debugging | 51 | 小さいモデルから始め、失敗runを観察しながらモデル族・prior・データ処理を段階的に拡張する。 | `iteration_id, change_reason, failure_mode, hypothesis, next_action` |
| MCMC / computation diagnostics | 33 | 推論結果を解釈する前に、R-hat、ESS、divergence、treedepth、BFMI、trace/pairsを確認する。悪いrunは比較表から除外せず失敗として記録する。 | `rhat_max, ess_bulk_min, ess_tail_min, divergences, treedepth_hits, bfmi_min` |
| LOO-CV / model comparison | 18 | elpd差だけでなくSEとPareto-kを読み、勝敗より『どのデータ点で負けるか』を確認する。 | `loo_elpd, loo_elpd_diff, loo_se_diff, pareto_k_gt_0_7, reloo_count` |
| Prior / prior predictive | 12 | 事前分布が現実的なデータ範囲を生成するかを見る。現場導入前に、あり得ない予測の比率をゲート化する。 | `prior_spec_id, prior_predictive_seed, simulated_n, implausible_rate` |
| Prior-likelihood sensitivity | 9 | 結論がpriorに依存していないか、またpriorとlikelihoodが衝突していないか確認する。 | `priorsense_*, power_scaling_delta, prior_conflict_flag` |
| Unclassified / inspect manually | 8 | captionが薄い図表。前後の本文・コードchunk・公式ソースを確認して役割を確定する。 | `source_page_url, source_repo_url, manual_review_status` |

## 3. ケーススタディ別の図表量

| ページ | 図 | 単独画像 | 表 | 主な用途 |
|---|---:|---:|---:|---|
| [Bayesian Workflow book: Website](https://avehtari.github.io/Bayesian-Workflow/index.html) | 0 | 1 | 0 | Unclassified / inspect manually |
| [Bayesian Workflow book: Case studies](https://avehtari.github.io/Bayesian-Workflow/casestudies.html) | 0 | 0 | 1 | Unclassified / inspect manually |
| [Bioassay case study](https://avehtari.github.io/Bayesian-Workflow/bioassay/bioassay.html) | 13 | 0 | 0 | Posterior summary / effect interpretation |
| [Modeling performance on a multiple choice exam](https://avehtari.github.io/Bayesian-Workflow/multiple_choice/multiple_choice.html) | 24 | 0 | 0 | EDA / observed data |
| [Uncertainty in Bayesian LOO-CV Model Comparison](https://avehtari.github.io/Bayesian-Workflow/loo_comparison/loo_comparison.html) | 6 | 0 | 7 | LOO-CV / model comparison |
| [How many iterations to run and how many digits to report](https://avehtari.github.io/Bayesian-Workflow/digits/digits.html) | 2 | 0 | 8 | Posterior summary / effect interpretation |
| [Illustration of simple problematic posteriors](https://avehtari.github.io/Bayesian-Workflow/problems/problems.html) | 26 | 0 | 0 | Posterior summary / effect interpretation |
| [Declining exponentials](https://avehtari.github.io/Bayesian-Workflow/declining_exponentials/declining_exponentials.html) | 6 | 0 | 0 | EDA / observed data |
| [Coding a series of models: Simulated data of movie ratings](https://avehtari.github.io/Bayesian-Workflow/movies/movies.html) | 10 | 0 | 0 | EDA / observed data |
| [Prior specification for regression models: Reanalysis of a sleep study](https://avehtari.github.io/Bayesian-Workflow/sleep_study/sleep_study.html) | 34 | 0 | 0 | Posterior summary / effect interpretation |
| [Predictive model checking and comparison: Clinical trial](https://avehtari.github.io/Bayesian-Workflow/nabiximols/nabiximols.html) | 31 | 0 | 4 | Posterior predictive checking / calibration |
| [Building up to a hierarchical model: Coronavirus testing](https://avehtari.github.io/Bayesian-Workflow/coronavirus/coronavirus.html) | 8 | 0 | 0 | Prior-likelihood sensitivity |
| [Using a fitted model for decision analysis: Mixture model for time series competition](https://avehtari.github.io/Bayesian-Workflow/timeseries/timeseries.html) | 3 | 0 | 0 | MCMC / computation diagnostics |
| [Posterior predictive checking: Stochastic learning in dogs](https://avehtari.github.io/Bayesian-Workflow/dogs/dogs.html) | 15 | 0 | 8 | Posterior predictive checking / calibration |
| [Posterior predictive checking: Stochastic learning in dogs](https://avehtari.github.io/Bayesian-Workflow/dogs/dogs_stan.html) | 8 | 0 | 0 | Posterior predictive checking / calibration |
| [Incremental development and testing: Black cat adoptions](https://avehtari.github.io/Bayesian-Workflow/cat_adoptions/cat_adoptions.html) | 18 | 0 | 0 | EDA / observed data |
| [Debugging a model: World Cup football](https://avehtari.github.io/Bayesian-Workflow/world_cup/world_cup.html) | 11 | 0 | 0 | Posterior predictive checking / calibration |
| [Leave-one-out cross validation model checking and comparison: Roaches](https://avehtari.github.io/Bayesian-Workflow/roaches/roaches.html) | 28 | 0 | 0 | Posterior predictive checking / calibration |
| [Model building and expansion: Golf putting](https://avehtari.github.io/Bayesian-Workflow/golf/golf.html) | 22 | 0 | 0 | EDA / observed data |
| [Model building with latent variables: Markov models for animal movement](https://avehtari.github.io/Bayesian-Workflow/sharks/sharks.html) | 10 | 0 | 0 | Model development / debugging |
| [Model building: Time-series decomposition for birthdays](https://avehtari.github.io/Bayesian-Workflow/birthdays/birthdays.html) | 46 | 0 | 46 | Model development / debugging |
| [Models for regression coefficients and variable selection: Student grades](https://avehtari.github.io/Bayesian-Workflow/variable_selection/variable_selection.html) | 19 | 0 | 4 | Posterior summary / effect interpretation |
| [Sampling problems with latent variables: No vehicles in the park](https://avehtari.github.io/Bayesian-Workflow/park_rule/park_rule.html) | 11 | 0 | 0 | MCMC / computation diagnostics |
| [Challenge of multimodality: Differential equation for planetary motion](https://avehtari.github.io/Bayesian-Workflow/planetary_motion/planetary_motion.html) | 10 | 0 | 0 | MCMC / computation diagnostics |
| [Simulation-based calibration checking in model development workflow](https://avehtari.github.io/Bayesian-Workflow/sbc/sbc.html) | 23 | 0 | 0 | Posterior predictive checking / calibration |

## 4. 全図表カタログと実務メモ

各項目は `local_id` を安定参照IDとして使う。captionが `Figure N` だけの項目は、見出し・直前文・コードchunk由来の文脈で意味づけしている。

### Bayesian Workflow book: Website

- ページ: <https://avehtari.github.io/Bayesian-Workflow/index.html>
- ソース候補: <https://github.com/avehtari/Bayesian-Workflow/blob/eb00fa4397314ef7d90203382542bd44c590e289/index.qmd>

#### `index/standalone_image-001`

- 種別: `standalone_image` / 公式ID: `(none)` / ページ内順序: 1
- caption/列: Cover of the Bayesian Workflow book
- 周辺文脈（EN）: BibTeX entry:
- 周辺文脈（JA, 自動訳）: 情報 / BibTeX エントリー:
- Workflowフェーズ: **Unclassified / inspect manually**
- 実務での読み方: captionが薄い図表。前後の本文・コードchunk・公式ソースを確認して役割を確定する。
- MLflow連携: `source_page_url, source_repo_url, manual_review_status`
- 参照: [公式ページ](https://avehtari.github.io/Bayesian-Workflow/index.html) / [ソース候補](https://github.com/avehtari/Bayesian-Workflow/blob/eb00fa4397314ef7d90203382542bd44c590e289/index.qmd)

### Bayesian Workflow book: Case studies

- ページ: <https://avehtari.github.io/Bayesian-Workflow/casestudies.html>
- ソース候補: <https://github.com/avehtari/Bayesian-Workflow/blob/eb00fa4397314ef7d90203382542bd44c590e289/casestudies.qmd>

#### `casestudies/tinytable_soq0jv2fyl6t7naf3y46`

- 種別: `table` / 公式ID: `tinytable_soq0jv2fyl6t7naf3y46` / ページ内順序: 1
- caption/列: Package; Version; Description; arm; 1.15-3; Functions to accompany A. Gelman and J. Hill, Data Analysis Using Regression and Multilevel/Hierarchical Models, Cambridge University Press, 2007.; assertthat; 0.2.1
- 周辺文脈（EN）: We list here all the software packages used in the case studies and the versions used when rendering the case study web pages 2026-01-08.
- 周辺文脈（JA, 自動訳）: ソフトウェア バージョン / ここには、ケース スタディで使用されたすべてのソフトウェア パッケージと、2026 年 1 月 8 日にケース スタディ Web ページをレンダリングするときに使用されたバージョンがリストされます。
- Workflowフェーズ: **Unclassified / inspect manually**
- 実務での読み方: captionが薄い図表。前後の本文・コードchunk・公式ソースを確認して役割を確定する。
- MLflow連携: `source_page_url, source_repo_url, manual_review_status`
- 参照: [公式ページ](https://avehtari.github.io/Bayesian-Workflow/casestudies.html#tinytable_soq0jv2fyl6t7naf3y46) / [ソース候補](https://github.com/avehtari/Bayesian-Workflow/blob/eb00fa4397314ef7d90203382542bd44c590e289/casestudies.qmd)

### Bioassay case study

- ページ: <https://avehtari.github.io/Bayesian-Workflow/bioassay/bioassay.html>
- ソース候補: <https://github.com/avehtari/Bayesian-Workflow/blob/eb00fa4397314ef7d90203382542bd44c590e289/bioassay/bioassay.R>

#### `bioassay-bioassay/fig-bioassay-data-plot`

- 種別: `figure` / 公式ID: `fig-bioassay-data-plot` / ページ内順序: 1
- caption/列: Figure 1
- 周辺文脈（EN）: Data plotted with base R
- 周辺文脈（JA, 自動訳）: 2 バイオアッセイデータ / 塩基 R でプロットされたデータ
- Workflowフェーズ: **EDA / observed data**
- 実務での読み方: モデル化前に、観測単位・外れ値・欠測・群構造・時系列性・上限/下限などを確認する。MLflowではデータ版と前処理版を固定する。
- MLflow連携: `dataset_uri, dataset_hash, preprocessing_version, n_obs, group_count`
- 参照: [公式ページ](https://avehtari.github.io/Bayesian-Workflow/bioassay/bioassay.html#fig-bioassay-data-plot) / [ソース候補](https://github.com/avehtari/Bayesian-Workflow/blob/eb00fa4397314ef7d90203382542bd44c590e289/bioassay/bioassay.R)

#### `bioassay-bioassay/fig-bioassay-data-ggplot`

- 種別: `figure` / 公式ID: `fig-bioassay-data-ggplot` / ページ内順序: 2
- caption/列: Figure 2
- 周辺文脈（EN）: Data plotted with ggplot
- 周辺文脈（JA, 自動訳）: 2 バイオアッセイデータ / ggplot でプロットされたデータ
- Workflowフェーズ: **EDA / observed data**
- 実務での読み方: モデル化前に、観測単位・外れ値・欠測・群構造・時系列性・上限/下限などを確認する。MLflowではデータ版と前処理版を固定する。
- MLflow連携: `dataset_uri, dataset_hash, preprocessing_version, n_obs, group_count`
- 参照: [公式ページ](https://avehtari.github.io/Bayesian-Workflow/bioassay/bioassay.html#fig-bioassay-data-ggplot) / [ソース候補](https://github.com/avehtari/Bayesian-Workflow/blob/eb00fa4397314ef7d90203382542bd44c590e289/bioassay/bioassay.R)

#### `bioassay-bioassay/fig-bioassay-posterior-plot`

- 種別: `figure` / 公式ID: `fig-bioassay-posterior-plot` / ページ内順序: 3
- caption/列: Figure 3
- 周辺文脈（EN）: Plot with base plot: data, 20 logistic curves given 20 posterior draws, and one logistic given the posterior mean
- 周辺文脈（JA, 自動訳）: 4 事後サマリー / ベース プロットを含むプロット: データ、20 の事後描画を与えられた 20 のロジスティック曲線、および事後平均を与えられた 1 つのロジスティック
- Workflowフェーズ: **EDA / observed data**
- 実務での読み方: モデル化前に、観測単位・外れ値・欠測・群構造・時系列性・上限/下限などを確認する。MLflowではデータ版と前処理版を固定する。
- MLflow連携: `dataset_uri, dataset_hash, preprocessing_version, n_obs, group_count`
- 参照: [公式ページ](https://avehtari.github.io/Bayesian-Workflow/bioassay/bioassay.html#fig-bioassay-posterior-plot) / [ソース候補](https://github.com/avehtari/Bayesian-Workflow/blob/eb00fa4397314ef7d90203382542bd44c590e289/bioassay/bioassay.R)

#### `bioassay-bioassay/fig-bioassay-posterior-ggplot`

- 種別: `figure` / 公式ID: `fig-bioassay-posterior-ggplot` / ページ内順序: 4
- caption/列: Figure 4
- 周辺文脈（EN）: Plot with ggplot: data, 20 logistic curves given 20 posterior draws, and one logistic given the posterior mean
- 周辺文脈（JA, 自動訳）: 4 事後サマリー / ggplot によるプロット: データ、20 の事後描画を与えられた 20 のロジスティック曲線、および事後平均を与えられた 1 つのロジスティック
- Workflowフェーズ: **EDA / observed data**
- 実務での読み方: モデル化前に、観測単位・外れ値・欠測・群構造・時系列性・上限/下限などを確認する。MLflowではデータ版と前処理版を固定する。
- MLflow連携: `dataset_uri, dataset_hash, preprocessing_version, n_obs, group_count`
- 参照: [公式ページ](https://avehtari.github.io/Bayesian-Workflow/bioassay/bioassay.html#fig-bioassay-posterior-ggplot) / [ソース候補](https://github.com/avehtari/Bayesian-Workflow/blob/eb00fa4397314ef7d90203382542bd44c590e289/bioassay/bioassay.R)

#### `bioassay-bioassay/fig-bioassay-LD50-quantile-dots`

- 種別: `figure` / 公式ID: `fig-bioassay-LD50-quantile-dots` / ページ内順序: 5
- caption/列: Figure 5
- 周辺文脈（EN）: Quantile dot plot of the LD50 (mg/ml) posterior
- 周辺文脈（JA, 自動訳）: 5 事後 LD50 (mg/ml) の導出量 / 四分位点プロット
- Workflowフェーズ: **Posterior summary / effect interpretation**
- 実務での読み方: 推定効果・不確実性・派生量を意思決定に接続する。平均だけでなく区間・分布・実務閾値超過確率を残す。
- MLflow連携: `posterior_draws_uri, model_code_hash, ci_width, decision_threshold_prob`
- 参照: [公式ページ](https://avehtari.github.io/Bayesian-Workflow/bioassay/bioassay.html#fig-bioassay-LD50-quantile-dots) / [ソース候補](https://github.com/avehtari/Bayesian-Workflow/blob/eb00fa4397314ef7d90203382542bd44c590e289/bioassay/bioassay.R)

#### `bioassay-bioassay/fig-bioassay-LD50-KDE`

- 種別: `figure` / 公式ID: `fig-bioassay-LD50-KDE` / ページ内順序: 6
- caption/列: Figure 6
- 周辺文脈（EN）: Kernel density plot of the LD50 (mg/ml) posterior
- 周辺文脈（JA, 自動訳）: 5 事後 LD50 (mg/ml) の導出量 / カーネル密度プロット
- Workflowフェーズ: **Posterior summary / effect interpretation**
- 実務での読み方: 推定効果・不確実性・派生量を意思決定に接続する。平均だけでなく区間・分布・実務閾値超過確率を残す。
- MLflow連携: `posterior_draws_uri, model_code_hash, ci_width, decision_threshold_prob`
- 参照: [公式ページ](https://avehtari.github.io/Bayesian-Workflow/bioassay/bioassay.html#fig-bioassay-LD50-KDE) / [ソース候補](https://github.com/avehtari/Bayesian-Workflow/blob/eb00fa4397314ef7d90203382542bd44c590e289/bioassay/bioassay.R)

#### `bioassay-bioassay/fig-bioassay-posterior-ggplot-brms`

- 種別: `figure` / 公式ID: `fig-bioassay-posterior-ggplot-brms` / ページ内順序: 7
- caption/列: Figure 7
- 周辺文脈（EN）: Plot data, 20 logistic curves given 20 posterior draws, and one logistic given the posterior mean
- 周辺文脈（JA, 自動訳）: 6 つの brms モデルと推論 / プロット データ、20 の事後描画を与えられた 20 のロジスティック曲線、および事後平均を与えられた 1 つのロジスティック
- Workflowフェーズ: **EDA / observed data**
- 実務での読み方: モデル化前に、観測単位・外れ値・欠測・群構造・時系列性・上限/下限などを確認する。MLflowではデータ版と前処理版を固定する。
- MLflow連携: `dataset_uri, dataset_hash, preprocessing_version, n_obs, group_count`
- 参照: [公式ページ](https://avehtari.github.io/Bayesian-Workflow/bioassay/bioassay.html#fig-bioassay-posterior-ggplot-brms) / [ソース候補](https://github.com/avehtari/Bayesian-Workflow/blob/eb00fa4397314ef7d90203382542bd44c590e289/bioassay/bioassay.R)

#### `bioassay-bioassay/fig-bioassay-posterior-conditional_effects-brms`

- 種別: `figure` / 公式ID: `fig-bioassay-posterior-conditional_effects-brms` / ページ内順序: 8
- caption/列: Figure 8
- 周辺文脈（EN）: brms provides also shortcut for plotting the posterior mean and uncertainty. We use plot=FALSE and [[1]] to return a ggplot object, so that we can modify the axes labels.
- 周辺文脈（JA, 自動訳）: 6 brms モデルと推論 / brms は、事後平均と不確実性をプロットするためのショートカットも提供します。軸のラベルを変更できるように、plot=FALSE と [[1]] を使用して ggplot オブジェクトを返します。
- Workflowフェーズ: **Posterior summary / effect interpretation**
- 実務での読み方: 推定効果・不確実性・派生量を意思決定に接続する。平均だけでなく区間・分布・実務閾値超過確率を残す。
- MLflow連携: `posterior_draws_uri, model_code_hash, ci_width, decision_threshold_prob`
- 参照: [公式ページ](https://avehtari.github.io/Bayesian-Workflow/bioassay/bioassay.html#fig-bioassay-posterior-conditional_effects-brms) / [ソース候補](https://github.com/avehtari/Bayesian-Workflow/blob/eb00fa4397314ef7d90203382542bd44c590e289/bioassay/bioassay.R)

#### `bioassay-bioassay/fig-bioassay-posterior-conditional_effects-data-brms`

- 種別: `figure` / 公式ID: `fig-bioassay-posterior-conditional_effects-data-brms` / ページ内順序: 9
- caption/列: Figure 9
- 周辺文脈（EN）: We can add data points with ggplot::geom_point() .
- 周辺文脈（JA, 自動訳）: 6 brms モデルと推論 / ggplot::geom_point() を使用してデータポイントを追加できます。
- Workflowフェーズ: **EDA / observed data**
- 実務での読み方: モデル化前に、観測単位・外れ値・欠測・群構造・時系列性・上限/下限などを確認する。MLflowではデータ版と前処理版を固定する。
- MLflow連携: `dataset_uri, dataset_hash, preprocessing_version, n_obs, group_count`
- 参照: [公式ページ](https://avehtari.github.io/Bayesian-Workflow/bioassay/bioassay.html#fig-bioassay-posterior-conditional_effects-data-brms) / [ソース候補](https://github.com/avehtari/Bayesian-Workflow/blob/eb00fa4397314ef7d90203382542bd44c590e289/bioassay/bioassay.R)

#### `bioassay-bioassay/fig-bioassay-posterior-conditional_effects-spaghetti-brms`

- 種別: `figure` / 公式ID: `fig-bioassay-posterior-conditional_effects-spaghetti-brms` / ページ内順序: 10
- caption/列: Figure 10
- 周辺文脈（EN）: We can draw also individual posterior curves with spaghetti=TRUE, ndraws=20 , but then the posterior mean would be computed only from 20 curves. Increasing ndraws would make the pl
- 周辺文脈（JA, 自動訳）: 6 brms モデルと推論 / spaghetti=TRUE, nddraws=20 を使用して個々の事後曲線を描くこともできますが、その場合、事後平均は 20 個の曲線からのみ計算されます。 nddraws を増やすと、PL が増加します。
- Workflowフェーズ: **Posterior summary / effect interpretation**
- 実務での読み方: 推定効果・不確実性・派生量を意思決定に接続する。平均だけでなく区間・分布・実務閾値超過確率を残す。
- MLflow連携: `posterior_draws_uri, model_code_hash, ci_width, decision_threshold_prob`
- 参照: [公式ページ](https://avehtari.github.io/Bayesian-Workflow/bioassay/bioassay.html#fig-bioassay-posterior-conditional_effects-spaghetti-brms) / [ソース候補](https://github.com/avehtari/Bayesian-Workflow/blob/eb00fa4397314ef7d90203382542bd44c590e289/bioassay/bioassay.R)

#### `bioassay-bioassay/fig-bioassay-posterior-marginaleffects-brms`

- 種別: `figure` / 公式ID: `fig-bioassay-posterior-marginaleffects-brms` / ページ内順序: 11
- caption/列: Figure 11
- 周辺文脈（EN）: marginaleffects package also provides function for plotting the posterior prediction and uncertainty. By default it predicts on the scale of actual outcome, but as all batch sizes
- 周辺文脈（JA, 自動訳）: 6 brms モデルと推論/周辺効果パッケージは、事後予測と不確実性をプロットする機能も提供します。デフォルトでは、実際の結果のスケールに基づいて予測しますが、すべてのバッチ サイズと同様に予測します。
- Workflowフェーズ: **Posterior summary / effect interpretation**
- 実務での読み方: 推定効果・不確実性・派生量を意思決定に接続する。平均だけでなく区間・分布・実務閾値超過確率を残す。
- MLflow連携: `posterior_draws_uri, model_code_hash, ci_width, decision_threshold_prob`
- 参照: [公式ページ](https://avehtari.github.io/Bayesian-Workflow/bioassay/bioassay.html#fig-bioassay-posterior-marginaleffects-brms) / [ソース候補](https://github.com/avehtari/Bayesian-Workflow/blob/eb00fa4397314ef7d90203382542bd44c590e289/bioassay/bioassay.R)

#### `bioassay-bioassay/fig-bioassay-LD50-quantile-dots-brms`

- 種別: `figure` / 公式ID: `fig-bioassay-LD50-quantile-dots-brms` / ページ内順序: 12
- caption/列: Figure 12
- 周辺文脈（EN）: Quantile dot plot of the LD50 (mg/ml) posterior.
- 周辺文脈（JA, 自動訳）: 7 事後 LD50 / 事後 LD50 (mg/ml) の四分位点プロット。
- Workflowフェーズ: **Posterior summary / effect interpretation**
- 実務での読み方: 推定効果・不確実性・派生量を意思決定に接続する。平均だけでなく区間・分布・実務閾値超過確率を残す。
- MLflow連携: `posterior_draws_uri, model_code_hash, ci_width, decision_threshold_prob`
- 参照: [公式ページ](https://avehtari.github.io/Bayesian-Workflow/bioassay/bioassay.html#fig-bioassay-LD50-quantile-dots-brms) / [ソース候補](https://github.com/avehtari/Bayesian-Workflow/blob/eb00fa4397314ef7d90203382542bd44c590e289/bioassay/bioassay.R)

#### `bioassay-bioassay/fig-bioassay-LD50-KDE-brms`

- 種別: `figure` / 公式ID: `fig-bioassay-LD50-KDE-brms` / ページ内順序: 13
- caption/列: Figure 13
- 周辺文脈（EN）: Kernel density plot of the LD50 (mg/ml) posterior.
- 周辺文脈（JA, 自動訳）: 7 事後 LD50 / 事後 LD50 (mg/ml) のカーネル密度プロット。
- Workflowフェーズ: **Posterior summary / effect interpretation**
- 実務での読み方: 推定効果・不確実性・派生量を意思決定に接続する。平均だけでなく区間・分布・実務閾値超過確率を残す。
- MLflow連携: `posterior_draws_uri, model_code_hash, ci_width, decision_threshold_prob`
- 参照: [公式ページ](https://avehtari.github.io/Bayesian-Workflow/bioassay/bioassay.html#fig-bioassay-LD50-KDE-brms) / [ソース候補](https://github.com/avehtari/Bayesian-Workflow/blob/eb00fa4397314ef7d90203382542bd44c590e289/bioassay/bioassay.R)

### Modeling performance on a multiple choice exam

- ページ: <https://avehtari.github.io/Bayesian-Workflow/multiple_choice/multiple_choice.html>
- ソース候補: <https://github.com/avehtari/Bayesian-Workflow/blob/eb00fa4397314ef7d90203382542bd44c590e289/multiple_choice/multiple_choice.R>

#### `multiple-choice-multiple-choice/fig-final_exams_1`

- 種別: `figure` / 公式ID: `fig-final_exams_1` / ページ内順序: 1
- caption/列: Figure 1
- 周辺文脈（EN）: Read in data and construct score for each student
- 周辺文脈（JA, 自動訳）: 4.1 基本モデル logit_0 / データを読み込み、各生徒のスコアを構築する
- Workflowフェーズ: **EDA / observed data**
- 実務での読み方: モデル化前に、観測単位・外れ値・欠測・群構造・時系列性・上限/下限などを確認する。MLflowではデータ版と前処理版を固定する。
- MLflow連携: `dataset_uri, dataset_hash, preprocessing_version, n_obs, group_count`
- 参照: [公式ページ](https://avehtari.github.io/Bayesian-Workflow/multiple_choice/multiple_choice.html#fig-final_exams_1) / [ソース候補](https://github.com/avehtari/Bayesian-Workflow/blob/eb00fa4397314ef7d90203382542bd44c590e289/multiple_choice/multiple_choice.R)

#### `multiple-choice-multiple-choice/fig-final_exams_2`

- 種別: `figure` / 公式ID: `fig-final_exams_2` / ページ内順序: 2
- caption/列: Figure 2
- 周辺文脈（EN）: Read in data and construct score for each student
- 周辺文脈（JA, 自動訳）: 4.2 事前分布の追加 / データを読み込み、各生徒のスコアを構築する
- Workflowフェーズ: **EDA / observed data**
- 実務での読み方: モデル化前に、観測単位・外れ値・欠測・群構造・時系列性・上限/下限などを確認する。MLflowではデータ版と前処理版を固定する。
- MLflow連携: `dataset_uri, dataset_hash, preprocessing_version, n_obs, group_count`
- 参照: [公式ページ](https://avehtari.github.io/Bayesian-Workflow/multiple_choice/multiple_choice.html#fig-final_exams_2) / [ソース候補](https://github.com/avehtari/Bayesian-Workflow/blob/eb00fa4397314ef7d90203382542bd44c590e289/multiple_choice/multiple_choice.R)

#### `multiple-choice-multiple-choice/fig-final_exams_2b`

- 種別: `figure` / 公式ID: `fig-final_exams_2b` / ページ内順序: 3
- caption/列: Figure 3
- 周辺文脈（EN）: Read in data and construct score for each student
- 周辺文脈（JA, 自動訳）: 4.2 事前分布の追加 / データを読み込み、各生徒のスコアを構築する
- Workflowフェーズ: **EDA / observed data**
- 実務での読み方: モデル化前に、観測単位・外れ値・欠測・群構造・時系列性・上限/下限などを確認する。MLflowではデータ版と前処理版を固定する。
- MLflow連携: `dataset_uri, dataset_hash, preprocessing_version, n_obs, group_count`
- 参照: [公式ページ](https://avehtari.github.io/Bayesian-Workflow/multiple_choice/multiple_choice.html#fig-final_exams_2b) / [ソース候補](https://github.com/avehtari/Bayesian-Workflow/blob/eb00fa4397314ef7d90203382542bd44c590e289/multiple_choice/multiple_choice.R)

#### `multiple-choice-multiple-choice/fig-final_exams_2_challenge`

- 種別: `figure` / 公式ID: `fig-final_exams_2_challenge` / ページ内順序: 4
- caption/列: Figure 4
- 周辺文脈（EN）: Read in data and construct score for each student
- 周辺文脈（JA, 自動訳）: 4.2 事前分布の追加 / データを読み込み、各生徒のスコアを構築する
- Workflowフェーズ: **EDA / observed data**
- 実務での読み方: モデル化前に、観測単位・外れ値・欠測・群構造・時系列性・上限/下限などを確認する。MLflowではデータ版と前処理版を固定する。
- MLflow連携: `dataset_uri, dataset_hash, preprocessing_version, n_obs, group_count`
- 参照: [公式ページ](https://avehtari.github.io/Bayesian-Workflow/multiple_choice/multiple_choice.html#fig-final_exams_2_challenge) / [ソース候補](https://github.com/avehtari/Bayesian-Workflow/blob/eb00fa4397314ef7d90203382542bd44c590e289/multiple_choice/multiple_choice.R)

#### `multiple-choice-multiple-choice/fig-final_exams_3`

- 種別: `figure` / 公式ID: `fig-final_exams_3` / ページ内順序: 5
- caption/列: Figure 5
- 周辺文脈（EN）: Read in data and construct score for each student
- 周辺文脈（JA, 自動訳）: 4.3 データの問題を修正する / データを読み込み、各生徒のスコアを作成する
- Workflowフェーズ: **EDA / observed data**
- 実務での読み方: モデル化前に、観測単位・外れ値・欠測・群構造・時系列性・上限/下限などを確認する。MLflowではデータ版と前処理版を固定する。
- MLflow連携: `dataset_uri, dataset_hash, preprocessing_version, n_obs, group_count`
- 参照: [公式ページ](https://avehtari.github.io/Bayesian-Workflow/multiple_choice/multiple_choice.html#fig-final_exams_3) / [ソース候補](https://github.com/avehtari/Bayesian-Workflow/blob/eb00fa4397314ef7d90203382542bd44c590e289/multiple_choice/multiple_choice.R)

#### `multiple-choice-multiple-choice/fig-final_exams_4`

- 種別: `figure` / 公式ID: `fig-final_exams_4` / ページ内順序: 6
- caption/列: Figure 6
- 周辺文脈（EN）: Read in data and construct score for each student
- 周辺文脈（JA, 自動訳）: 4.4 推測を許可する / データを読み込んで各生徒のスコアを作成する
- Workflowフェーズ: **EDA / observed data**
- 実務での読み方: モデル化前に、観測単位・外れ値・欠測・群構造・時系列性・上限/下限などを確認する。MLflowではデータ版と前処理版を固定する。
- MLflow連携: `dataset_uri, dataset_hash, preprocessing_version, n_obs, group_count`
- 参照: [公式ページ](https://avehtari.github.io/Bayesian-Workflow/multiple_choice/multiple_choice.html#fig-final_exams_4) / [ソース候補](https://github.com/avehtari/Bayesian-Workflow/blob/eb00fa4397314ef7d90203382542bd44c590e289/multiple_choice/multiple_choice.R)

#### `multiple-choice-multiple-choice/fig-final_exams_5-1`

- 種別: `figure` / 公式ID: `fig-final_exams_5-1` / ページ内順序: 7
- caption/列: Figure 7
- 周辺文脈（EN）: In preparation for multilevel model, create long dataset
- 周辺文脈（JA, 自動訳）: 5.1 マルチレベルモデル / マルチレベルモデルの準備として長いデータセットを作成する
- Workflowフェーズ: **EDA / observed data**
- 実務での読み方: モデル化前に、観測単位・外れ値・欠測・群構造・時系列性・上限/下限などを確認する。MLflowではデータ版と前処理版を固定する。
- MLflow連携: `dataset_uri, dataset_hash, preprocessing_version, n_obs, group_count`
- 参照: [公式ページ](https://avehtari.github.io/Bayesian-Workflow/multiple_choice/multiple_choice.html#fig-final_exams_5-1) / [ソース候補](https://github.com/avehtari/Bayesian-Workflow/blob/eb00fa4397314ef7d90203382542bd44c590e289/multiple_choice/multiple_choice.R)

#### `multiple-choice-multiple-choice/fig-final_exams_5-2`

- 種別: `figure` / 公式ID: `fig-final_exams_5-2` / ページ内順序: 8
- caption/列: Figure 8
- 周辺文脈（EN）: In preparation for multilevel model, create long dataset
- 周辺文脈（JA, 自動訳）: 5.1 マルチレベルモデル / マルチレベルモデルの準備として長いデータセットを作成する
- Workflowフェーズ: **EDA / observed data**
- 実務での読み方: モデル化前に、観測単位・外れ値・欠測・群構造・時系列性・上限/下限などを確認する。MLflowではデータ版と前処理版を固定する。
- MLflow連携: `dataset_uri, dataset_hash, preprocessing_version, n_obs, group_count`
- 参照: [公式ページ](https://avehtari.github.io/Bayesian-Workflow/multiple_choice/multiple_choice.html#fig-final_exams_5-2) / [ソース候補](https://github.com/avehtari/Bayesian-Workflow/blob/eb00fa4397314ef7d90203382542bd44c590e289/multiple_choice/multiple_choice.R)

#### `multiple-choice-multiple-choice/fig-final_exams_6-1`

- 種別: `figure` / 公式ID: `fig-final_exams_6-1` / ページ内順序: 9
- caption/列: Figure 9
- 周辺文脈（EN）: In preparation for multilevel model, create long dataset
- 周辺文脈（JA, 自動訳）: 5.2 相関関係のある多値モデル / 多値モデルの準備として長いデータセットを作成する
- Workflowフェーズ: **EDA / observed data**
- 実務での読み方: モデル化前に、観測単位・外れ値・欠測・群構造・時系列性・上限/下限などを確認する。MLflowではデータ版と前処理版を固定する。
- MLflow連携: `dataset_uri, dataset_hash, preprocessing_version, n_obs, group_count`
- 参照: [公式ページ](https://avehtari.github.io/Bayesian-Workflow/multiple_choice/multiple_choice.html#fig-final_exams_6-1) / [ソース候補](https://github.com/avehtari/Bayesian-Workflow/blob/eb00fa4397314ef7d90203382542bd44c590e289/multiple_choice/multiple_choice.R)

#### `multiple-choice-multiple-choice/fig-final_exams_6-2`

- 種別: `figure` / 公式ID: `fig-final_exams_6-2` / ページ内順序: 10
- caption/列: Figure 10
- 周辺文脈（EN）: In preparation for multilevel model, create long dataset
- 周辺文脈（JA, 自動訳）: 5.2 相関関係のある多値モデル / 多値モデルの準備として長いデータセットを作成する
- Workflowフェーズ: **EDA / observed data**
- 実務での読み方: モデル化前に、観測単位・外れ値・欠測・群構造・時系列性・上限/下限などを確認する。MLflowではデータ版と前処理版を固定する。
- MLflow連携: `dataset_uri, dataset_hash, preprocessing_version, n_obs, group_count`
- 参照: [公式ページ](https://avehtari.github.io/Bayesian-Workflow/multiple_choice/multiple_choice.html#fig-final_exams_6-2) / [ソース候補](https://github.com/avehtari/Bayesian-Workflow/blob/eb00fa4397314ef7d90203382542bd44c590e289/multiple_choice/multiple_choice.R)

#### `multiple-choice-multiple-choice/fig-final_exams_7-1`

- 種別: `figure` / 公式ID: `fig-final_exams_7-1` / ページ内順序: 11
- caption/列: Figure 11
- 周辺文脈（EN）: In preparation for multilevel model, create long dataset
- 周辺文脈（JA, 自動訳）: 5.3 Choleskyを用いた相関のある多値モデル / 多値モデルの準備として長いデータセットを作成する
- Workflowフェーズ: **EDA / observed data**
- 実務での読み方: モデル化前に、観測単位・外れ値・欠測・群構造・時系列性・上限/下限などを確認する。MLflowではデータ版と前処理版を固定する。
- MLflow連携: `dataset_uri, dataset_hash, preprocessing_version, n_obs, group_count`
- 参照: [公式ページ](https://avehtari.github.io/Bayesian-Workflow/multiple_choice/multiple_choice.html#fig-final_exams_7-1) / [ソース候補](https://github.com/avehtari/Bayesian-Workflow/blob/eb00fa4397314ef7d90203382542bd44c590e289/multiple_choice/multiple_choice.R)

#### `multiple-choice-multiple-choice/fig-final_exams_7-2`

- 種別: `figure` / 公式ID: `fig-final_exams_7-2` / ページ内順序: 12
- caption/列: Figure 12
- 周辺文脈（EN）: In preparation for multilevel model, create long dataset
- 周辺文脈（JA, 自動訳）: 5.3 Choleskyを用いた相関のある多値モデル / 多値モデルの準備として長いデータセットを作成する
- Workflowフェーズ: **EDA / observed data**
- 実務での読み方: モデル化前に、観測単位・外れ値・欠測・群構造・時系列性・上限/下限などを確認する。MLflowではデータ版と前処理版を固定する。
- MLflow連携: `dataset_uri, dataset_hash, preprocessing_version, n_obs, group_count`
- 参照: [公式ページ](https://avehtari.github.io/Bayesian-Workflow/multiple_choice/multiple_choice.html#fig-final_exams_7-2) / [ソース候補](https://github.com/avehtari/Bayesian-Workflow/blob/eb00fa4397314ef7d90203382542bd44c590e289/multiple_choice/multiple_choice.R)

#### `multiple-choice-multiple-choice/fig-final_exams_11`

- 種別: `figure` / 公式ID: `fig-final_exams_11` / ページ内順序: 13
- caption/列: Figure 13
- 周辺文脈（EN）: In preparation for multilevel model, create long dataset
- 周辺文脈（JA, 自動訳）: 6.1 項目応答モデル / 多段階モデルの準備として長いデータセットを作成する
- Workflowフェーズ: **EDA / observed data**
- 実務での読み方: モデル化前に、観測単位・外れ値・欠測・群構造・時系列性・上限/下限などを確認する。MLflowではデータ版と前処理版を固定する。
- MLflow連携: `dataset_uri, dataset_hash, preprocessing_version, n_obs, group_count`
- 参照: [公式ページ](https://avehtari.github.io/Bayesian-Workflow/multiple_choice/multiple_choice.html#fig-final_exams_11) / [ソース候補](https://github.com/avehtari/Bayesian-Workflow/blob/eb00fa4397314ef7d90203382542bd44c590e289/multiple_choice/multiple_choice.R)

#### `multiple-choice-multiple-choice/fig-final_exams_12`

- 種別: `figure` / 公式ID: `fig-final_exams_12` / ページ内順序: 14
- caption/列: Figure 14
- 周辺文脈（EN）: In preparation for multilevel model, create long dataset
- 周辺文脈（JA, 自動訳）: 6.2 識別パラメータを備えた項目応答モデル / 多値モデルの準備として長いデータセットを作成する
- Workflowフェーズ: **EDA / observed data**
- 実務での読み方: モデル化前に、観測単位・外れ値・欠測・群構造・時系列性・上限/下限などを確認する。MLflowではデータ版と前処理版を固定する。
- MLflow連携: `dataset_uri, dataset_hash, preprocessing_version, n_obs, group_count`
- 参照: [公式ページ](https://avehtari.github.io/Bayesian-Workflow/multiple_choice/multiple_choice.html#fig-final_exams_12) / [ソース候補](https://github.com/avehtari/Bayesian-Workflow/blob/eb00fa4397314ef7d90203382542bd44c590e289/multiple_choice/multiple_choice.R)

#### `multiple-choice-multiple-choice/fig-final_exams_13`

- 種別: `figure` / 公式ID: `fig-final_exams_13` / ページ内順序: 15
- caption/列: Figure 15
- 周辺文脈（EN）: In preparation for multilevel model, create long dataset
- 周辺文脈（JA, 自動訳）: 6.3 initによる判別パラメータ付き項目応答モデル / 多値モデルの準備として長いデータセットを作成
- Workflowフェーズ: **EDA / observed data**
- 実務での読み方: モデル化前に、観測単位・外れ値・欠測・群構造・時系列性・上限/下限などを確認する。MLflowではデータ版と前処理版を固定する。
- MLflow連携: `dataset_uri, dataset_hash, preprocessing_version, n_obs, group_count`
- 参照: [公式ページ](https://avehtari.github.io/Bayesian-Workflow/multiple_choice/multiple_choice.html#fig-final_exams_13) / [ソース候補](https://github.com/avehtari/Bayesian-Workflow/blob/eb00fa4397314ef7d90203382542bd44c590e289/multiple_choice/multiple_choice.R)

#### `multiple-choice-multiple-choice/fig-irt_displays_1`

- 種別: `figure` / 公式ID: `fig-irt_displays_1` / ページ内順序: 16
- caption/列: Figure 16
- 周辺文脈（EN）: IRT plots
- 周辺文脈（JA, 自動訳）: 6.3 Item-response model with discrimination parameters with init / IRT plots
- Workflowフェーズ: **Unclassified / inspect manually**
- 実務での読み方: captionが薄い図表。前後の本文・コードchunk・公式ソースを確認して役割を確定する。
- MLflow連携: `source_page_url, source_repo_url, manual_review_status`
- 参照: [公式ページ](https://avehtari.github.io/Bayesian-Workflow/multiple_choice/multiple_choice.html#fig-irt_displays_1) / [ソース候補](https://github.com/avehtari/Bayesian-Workflow/blob/eb00fa4397314ef7d90203382542bd44c590e289/multiple_choice/multiple_choice.R)

#### `multiple-choice-multiple-choice/fig-irt_displays_2`

- 種別: `figure` / 公式ID: `fig-irt_displays_2` / ページ内順序: 17
- caption/列: Figure 17
- 周辺文脈（EN）: IRT plots
- 周辺文脈（JA, 自動訳）: 6.3 Item-response model with discrimination parameters with init / IRT plots
- Workflowフェーズ: **Unclassified / inspect manually**
- 実務での読み方: captionが薄い図表。前後の本文・コードchunk・公式ソースを確認して役割を確定する。
- MLflow連携: `source_page_url, source_repo_url, manual_review_status`
- 参照: [公式ページ](https://avehtari.github.io/Bayesian-Workflow/multiple_choice/multiple_choice.html#fig-irt_displays_2) / [ソース候補](https://github.com/avehtari/Bayesian-Workflow/blob/eb00fa4397314ef7d90203382542bd44c590e289/multiple_choice/multiple_choice.R)

#### `multiple-choice-multiple-choice/fig-multiplechoice_prior_predictive_1`

- 種別: `figure` / 公式ID: `fig-multiplechoice_prior_predictive_1` / ページ内順序: 18
- caption/列: Figure 18
- 周辺文脈（EN）: IRT plots
- 周辺文脈（JA, 自動訳）: 7 事前の予測シミュレーション / IRT プロット
- Workflowフェーズ: **Prior / prior predictive**
- 実務での読み方: 事前分布が現実的なデータ範囲を生成するかを見る。現場導入前に、あり得ない予測の比率をゲート化する。
- MLflow連携: `prior_spec_id, prior_predictive_seed, simulated_n, implausible_rate`
- 参照: [公式ページ](https://avehtari.github.io/Bayesian-Workflow/multiple_choice/multiple_choice.html#fig-multiplechoice_prior_predictive_1) / [ソース候補](https://github.com/avehtari/Bayesian-Workflow/blob/eb00fa4397314ef7d90203382542bd44c590e289/multiple_choice/multiple_choice.R)

#### `multiple-choice-multiple-choice/fig-multiplechoice_prior_predictive_2`

- 種別: `figure` / 公式ID: `fig-multiplechoice_prior_predictive_2` / ページ内順序: 19
- caption/列: Figure 19
- 周辺文脈（EN）: IRT plots
- 周辺文脈（JA, 自動訳）: 7 事前の予測シミュレーション / IRT プロット
- Workflowフェーズ: **Prior / prior predictive**
- 実務での読み方: 事前分布が現実的なデータ範囲を生成するかを見る。現場導入前に、あり得ない予測の比率をゲート化する。
- MLflow連携: `prior_spec_id, prior_predictive_seed, simulated_n, implausible_rate`
- 参照: [公式ページ](https://avehtari.github.io/Bayesian-Workflow/multiple_choice/multiple_choice.html#fig-multiplechoice_prior_predictive_2) / [ソース候補](https://github.com/avehtari/Bayesian-Workflow/blob/eb00fa4397314ef7d90203382542bd44c590e289/multiple_choice/multiple_choice.R)

#### `multiple-choice-multiple-choice/fig-multiplechoice_prior_predictive_3`

- 種別: `figure` / 公式ID: `fig-multiplechoice_prior_predictive_3` / ページ内順序: 20
- caption/列: Figure 20
- 周辺文脈（EN）: IRT plots
- 周辺文脈（JA, 自動訳）: 7 事前の予測シミュレーション / IRT プロット
- Workflowフェーズ: **Prior / prior predictive**
- 実務での読み方: 事前分布が現実的なデータ範囲を生成するかを見る。現場導入前に、あり得ない予測の比率をゲート化する。
- MLflow連携: `prior_spec_id, prior_predictive_seed, simulated_n, implausible_rate`
- 参照: [公式ページ](https://avehtari.github.io/Bayesian-Workflow/multiple_choice/multiple_choice.html#fig-multiplechoice_prior_predictive_3) / [ソース候補](https://github.com/avehtari/Bayesian-Workflow/blob/eb00fa4397314ef7d90203382542bd44c590e289/multiple_choice/multiple_choice.R)

#### `multiple-choice-multiple-choice/fig-break_1`

- 種別: `figure` / 公式ID: `fig-break_1` / ページ内順序: 21
- caption/列: Figure 21
- 周辺文脈（EN）: Simulate data
- 周辺文脈（JA, 自動訳）: 8 モデルの破壊 / データのシミュレーション
- Workflowフェーズ: **EDA / observed data**
- 実務での読み方: モデル化前に、観測単位・外れ値・欠測・群構造・時系列性・上限/下限などを確認する。MLflowではデータ版と前処理版を固定する。
- MLflow連携: `dataset_uri, dataset_hash, preprocessing_version, n_obs, group_count`
- 参照: [公式ページ](https://avehtari.github.io/Bayesian-Workflow/multiple_choice/multiple_choice.html#fig-break_1) / [ソース候補](https://github.com/avehtari/Bayesian-Workflow/blob/eb00fa4397314ef7d90203382542bd44c590e289/multiple_choice/multiple_choice.R)

#### `multiple-choice-multiple-choice/fig-break_2`

- 種別: `figure` / 公式ID: `fig-break_2` / ページ内順序: 22
- caption/列: Figure 22
- 周辺文脈（EN）: Simulate data
- 周辺文脈（JA, 自動訳）: 8 モデルの破壊 / データのシミュレーション
- Workflowフェーズ: **EDA / observed data**
- 実務での読み方: モデル化前に、観測単位・外れ値・欠測・群構造・時系列性・上限/下限などを確認する。MLflowではデータ版と前処理版を固定する。
- MLflow連携: `dataset_uri, dataset_hash, preprocessing_version, n_obs, group_count`
- 参照: [公式ページ](https://avehtari.github.io/Bayesian-Workflow/multiple_choice/multiple_choice.html#fig-break_2) / [ソース候補](https://github.com/avehtari/Bayesian-Workflow/blob/eb00fa4397314ef7d90203382542bd44c590e289/multiple_choice/multiple_choice.R)

#### `multiple-choice-multiple-choice/fig-final_exams_break_1-1`

- 種別: `figure` / 公式ID: `fig-final_exams_break_1-1` / ページ内順序: 23
- caption/列: Figure 23
- 周辺文脈（EN）: Simulate data
- 周辺文脈（JA, 自動訳）: 8 モデルの破壊 / データのシミュレーション
- Workflowフェーズ: **EDA / observed data**
- 実務での読み方: モデル化前に、観測単位・外れ値・欠測・群構造・時系列性・上限/下限などを確認する。MLflowではデータ版と前処理版を固定する。
- MLflow連携: `dataset_uri, dataset_hash, preprocessing_version, n_obs, group_count`
- 参照: [公式ページ](https://avehtari.github.io/Bayesian-Workflow/multiple_choice/multiple_choice.html#fig-final_exams_break_1-1) / [ソース候補](https://github.com/avehtari/Bayesian-Workflow/blob/eb00fa4397314ef7d90203382542bd44c590e289/multiple_choice/multiple_choice.R)

#### `multiple-choice-multiple-choice/fig-final_exams_break_1-2`

- 種別: `figure` / 公式ID: `fig-final_exams_break_1-2` / ページ内順序: 24
- caption/列: Figure 24
- 周辺文脈（EN）: Simulate data
- 周辺文脈（JA, 自動訳）: 8 モデルの破壊 / データのシミュレーション
- Workflowフェーズ: **EDA / observed data**
- 実務での読み方: モデル化前に、観測単位・外れ値・欠測・群構造・時系列性・上限/下限などを確認する。MLflowではデータ版と前処理版を固定する。
- MLflow連携: `dataset_uri, dataset_hash, preprocessing_version, n_obs, group_count`
- 参照: [公式ページ](https://avehtari.github.io/Bayesian-Workflow/multiple_choice/multiple_choice.html#fig-final_exams_break_1-2) / [ソース候補](https://github.com/avehtari/Bayesian-Workflow/blob/eb00fa4397314ef7d90203382542bd44c590e289/multiple_choice/multiple_choice.R)

### Uncertainty in Bayesian LOO-CV Model Comparison

- ページ: <https://avehtari.github.io/Bayesian-Workflow/loo_comparison/loo_comparison.html>
- ソース候補: <https://github.com/avehtari/Bayesian-Workflow/blob/eb00fa4397314ef7d90203382542bd44c590e289/loo_comparison/loo_comparison.R>

#### `loo-comparison-loo-comparison/figure-001`

- 種別: `figure` / 公式ID: `(none)` / ページ内順序: 1
- caption/列: figure 1
- 周辺文脈（EN）: Although we can get more accurate elpd and elpd_diff estimates with more computation, the accuracy of the normal approximation for the uncertainty in the difference can still be co
- 周辺文脈（JA, 自動訳）: 3 睡眠研究 / より多くの計算を行うことでより正確な elpd および elpd_diff 推定値を取得できますが、差の不確実性に対する正規近似の精度は依然として同等である可能性があります。
- Workflowフェーズ: **LOO-CV / model comparison**
- 実務での読み方: elpd差だけでなくSEとPareto-kを読み、勝敗より『どのデータ点で負けるか』を確認する。
- MLflow連携: `loo_elpd, loo_elpd_diff, loo_se_diff, pareto_k_gt_0_7, reloo_count`
- 参照: [公式ページ](https://avehtari.github.io/Bayesian-Workflow/loo_comparison/loo_comparison.html) / [ソース候補](https://github.com/avehtari/Bayesian-Workflow/blob/eb00fa4397314ef7d90203382542bd44c590e289/loo_comparison/loo_comparison.R)

#### `loo-comparison-loo-comparison/figure-002`

- 種別: `figure` / 公式ID: `(none)` / ページ内順序: 2
- caption/列: figure 2
- 周辺文脈（EN）: Although we can get more accurate elpd and elpd_diff estimates with more computation, the accuracy of the normal approximation for the uncertainty in the difference can still be co
- 周辺文脈（JA, 自動訳）: 3 睡眠研究 / より多くの計算を行うことでより正確な elpd および elpd_diff 推定値を取得できますが、差の不確実性に対する正規近似の精度は依然として同等である可能性があります。
- Workflowフェーズ: **LOO-CV / model comparison**
- 実務での読み方: elpd差だけでなくSEとPareto-kを読み、勝敗より『どのデータ点で負けるか』を確認する。
- MLflow連携: `loo_elpd, loo_elpd_diff, loo_se_diff, pareto_k_gt_0_7, reloo_count`
- 参照: [公式ページ](https://avehtari.github.io/Bayesian-Workflow/loo_comparison/loo_comparison.html) / [ソース候補](https://github.com/avehtari/Bayesian-Workflow/blob/eb00fa4397314ef7d90203382542bd44c590e289/loo_comparison/loo_comparison.R)

#### `loo-comparison-loo-comparison/figure-003`

- 種別: `figure` / 公式ID: `(none)` / ページ内順序: 3
- caption/列: figure 3
- 周辺文脈（EN）: If we examine the pointwise differences, we see that model 3 is almost always better, but outliers cause couple values with big magnitude, making it more likely that the normal app
- 周辺文脈（JA, 自動訳）: 3 睡眠の研究 / 点ごとの違いを調べると、モデル 3 がほぼ常に優れていることがわかりますが、外れ値によってカップルの値が大きくなり、通常のアプリの方が問題が発生する可能性が高くなります。
- Workflowフェーズ: **LOO-CV / model comparison**
- 実務での読み方: elpd差だけでなくSEとPareto-kを読み、勝敗より『どのデータ点で負けるか』を確認する。
- MLflow連携: `loo_elpd, loo_elpd_diff, loo_se_diff, pareto_k_gt_0_7, reloo_count`
- 参照: [公式ページ](https://avehtari.github.io/Bayesian-Workflow/loo_comparison/loo_comparison.html) / [ソース候補](https://github.com/avehtari/Bayesian-Workflow/blob/eb00fa4397314ef7d90203382542bd44c590e289/loo_comparison/loo_comparison.R)

#### `loo-comparison-loo-comparison/figure-004`

- 種別: `figure` / 公式ID: `(none)` / ページ内順序: 4
- caption/列: figure 4
- 周辺文脈（EN）: LOO predictive intervals look now better.
- 周辺文脈（JA, 自動訳）: 3 睡眠調査/LOO 予測間隔が改善されました。
- Workflowフェーズ: **Posterior predictive checking / calibration**
- 実務での読み方: モデルが再現すべき特徴を外していないか確認する。PPC統計量と図をartifact化し、モデル改善の根拠にする。
- MLflow連携: `ppc_stat_*, loo_pit_ecdf_maxdev, calibration_error, replicated_seed`
- 参照: [公式ページ](https://avehtari.github.io/Bayesian-Workflow/loo_comparison/loo_comparison.html) / [ソース候補](https://github.com/avehtari/Bayesian-Workflow/blob/eb00fa4397314ef7d90203382542bd44c590e289/loo_comparison/loo_comparison.R)

#### `loo-comparison-loo-comparison/figure-005`

- 種別: `figure` / 公式ID: `(none)` / ページ内順序: 5
- caption/列: figure 5
- 周辺文脈（EN）: LOO predictive intervals look now better.
- 周辺文脈（JA, 自動訳）: 3 睡眠調査/LOO 予測間隔が改善されました。
- Workflowフェーズ: **Posterior predictive checking / calibration**
- 実務での読み方: モデルが再現すべき特徴を外していないか確認する。PPC統計量と図をartifact化し、モデル改善の根拠にする。
- MLflow連携: `ppc_stat_*, loo_pit_ecdf_maxdev, calibration_error, replicated_seed`
- 参照: [公式ページ](https://avehtari.github.io/Bayesian-Workflow/loo_comparison/loo_comparison.html) / [ソース候補](https://github.com/avehtari/Bayesian-Workflow/blob/eb00fa4397314ef7d90203382542bd44c590e289/loo_comparison/loo_comparison.R)

#### `loo-comparison-loo-comparison/figure-006`

- 種別: `figure` / 公式ID: `(none)` / ページ内順序: 6
- caption/列: figure 6
- 周辺文脈（EN）: If we examine the pointwise differences, we see that model 3 is almost always better, and as there are no outliers, the distribution of pointwise elpd differences is such that the
- 周辺文脈（JA, 自動訳）: 3 睡眠研究 / 点ごとの違いを調べると、モデル 3 がほぼ常に優れていることがわかります。外れ値がないため、点ごとの elpd の差の分布は次のようになります。
- Workflowフェーズ: **EDA / observed data**
- 実務での読み方: モデル化前に、観測単位・外れ値・欠測・群構造・時系列性・上限/下限などを確認する。MLflowではデータ版と前処理版を固定する。
- MLflow連携: `dataset_uri, dataset_hash, preprocessing_version, n_obs, group_count`
- 参照: [公式ページ](https://avehtari.github.io/Bayesian-Workflow/loo_comparison/loo_comparison.html) / [ソース候補](https://github.com/avehtari/Bayesian-Workflow/blob/eb00fa4397314ef7d90203382542bd44c590e289/loo_comparison/loo_comparison.R)

#### `loo-comparison-loo-comparison/tinytable_vm6zqjuq3nvs9tyohneu`

- 種別: `table` / 公式ID: `tinytable_vm6zqjuq3nvs9tyohneu` / ページ内順序: 1
- caption/列: model; elpd_diff; se_diff; p; M_4; 0; 0; -
- 周辺文脈（EN）: We add the probability that a model has worse predictive performance than the model with the best predictive performance using the normal approximation.
- 周辺文脈（JA, 自動訳）: 2 霊長類のミルク / 正規近似を使用して、モデルの予測パフォーマンスが最高の予測パフォーマンスを持つモデルよりも悪い確率を追加します。
- Workflowフェーズ: **LOO-CV / model comparison**
- 実務での読み方: elpd差だけでなくSEとPareto-kを読み、勝敗より『どのデータ点で負けるか』を確認する。
- MLflow連携: `loo_elpd, loo_elpd_diff, loo_se_diff, pareto_k_gt_0_7, reloo_count`
- 参照: [公式ページ](https://avehtari.github.io/Bayesian-Workflow/loo_comparison/loo_comparison.html#tinytable_vm6zqjuq3nvs9tyohneu) / [ソース候補](https://github.com/avehtari/Bayesian-Workflow/blob/eb00fa4397314ef7d90203382542bd44c590e289/loo_comparison/loo_comparison.R)

#### `loo-comparison-loo-comparison/tinytable_1s2zcdbymhpkymyxm444`

- 種別: `table` / 公式ID: `tinytable_1s2zcdbymhpkymyxm444` / ページ内順序: 2
- caption/列: model; elpd_diff; se_diff; p; M_1; 0; 0; -
- 周辺文脈（EN）: In the paper, we the comparison was reported using the M_1 as the baseline, and the probability that a model has better predictive performance than the baseline.
- 周辺文脈（JA, 自動訳）: 2 霊長類のミルク / 論文では、ベースラインとして M_1 を使用し、モデルの予測パフォーマンスがベースラインよりも優れている確率を使用して比較が報告されました。
- Workflowフェーズ: **LOO-CV / model comparison**
- 実務での読み方: elpd差だけでなくSEとPareto-kを読み、勝敗より『どのデータ点で負けるか』を確認する。
- MLflow連携: `loo_elpd, loo_elpd_diff, loo_se_diff, pareto_k_gt_0_7, reloo_count`
- 参照: [公式ページ](https://avehtari.github.io/Bayesian-Workflow/loo_comparison/loo_comparison.html#tinytable_1s2zcdbymhpkymyxm444) / [ソース候補](https://github.com/avehtari/Bayesian-Workflow/blob/eb00fa4397314ef7d90203382542bd44c590e289/loo_comparison/loo_comparison.R)

#### `loo-comparison-loo-comparison/tinytable_roxh3yw7eew3hw13lt8n`

- 種別: `table` / 公式ID: `tinytable_roxh3yw7eew3hw13lt8n` / ページ内順序: 3
- caption/列: model; elpd_diff; se_diff; p; M_3; 0; 0; -
- 周辺文脈（EN）: We compare the models \mathrm{M}_1, \mathrm{M}_2,\mathrm{M}_3,\mathrm{M}_4
- 周辺文脈（JA, 自動訳）: 3 睡眠研究 / モデル \mathrm{M}_1, \mathrm{M}_2,\mathrm{M}_3,\mathrm{M}_4 を比較します
- Workflowフェーズ: **LOO-CV / model comparison**
- 実務での読み方: elpd差だけでなくSEとPareto-kを読み、勝敗より『どのデータ点で負けるか』を確認する。
- MLflow連携: `loo_elpd, loo_elpd_diff, loo_se_diff, pareto_k_gt_0_7, reloo_count`
- 参照: [公式ページ](https://avehtari.github.io/Bayesian-Workflow/loo_comparison/loo_comparison.html#tinytable_roxh3yw7eew3hw13lt8n) / [ソース候補](https://github.com/avehtari/Bayesian-Workflow/blob/eb00fa4397314ef7d90203382542bd44c590e289/loo_comparison/loo_comparison.R)

#### `loo-comparison-loo-comparison/tinytable_5s8v26cggvewoucqfhxt`

- 種別: `table` / 公式ID: `tinytable_5s8v26cggvewoucqfhxt` / ページ内順序: 4
- caption/列: model; elpd_diff; se_diff; p; M_3t; 0; 0; -
- 周辺文脈（EN）: We first compare \mathrm{M}_{3} and \mathrm{M}_{3t} to see whether a Student’s t model is more appropriate.
- 周辺文脈（JA, 自動訳）: 3 睡眠の研究 / まず \mathrm{M}_{3} と \mathrm{M}_{3t} を比較して、Student の t モデルがより適切であるかどうかを確認します。
- Workflowフェーズ: **LOO-CV / model comparison**
- 実務での読み方: elpd差だけでなくSEとPareto-kを読み、勝敗より『どのデータ点で負けるか』を確認する。
- MLflow連携: `loo_elpd, loo_elpd_diff, loo_se_diff, pareto_k_gt_0_7, reloo_count`
- 参照: [公式ページ](https://avehtari.github.io/Bayesian-Workflow/loo_comparison/loo_comparison.html#tinytable_5s8v26cggvewoucqfhxt) / [ソース候補](https://github.com/avehtari/Bayesian-Workflow/blob/eb00fa4397314ef7d90203382542bd44c590e289/loo_comparison/loo_comparison.R)

#### `loo-comparison-loo-comparison/tinytable_x0hbb1e67wrox7g8nm3a`

- 種別: `table` / 公式ID: `tinytable_x0hbb1e67wrox7g8nm3a` / ページ内順序: 5
- caption/列: model; elpd_diff; se_diff; p; M_3t; 0; 0; -
- 周辺文脈（EN）: Although in this comparison \mathrm{M}_3 is misspecified, the better specified model \mathrm{M}_{3t} shows much better predictive performance, and as we can expect \seHatPlain to b
- 周辺文脈（JA, 自動訳）: 3 睡眠研究 / この比較では \mathrm{M}_3 の指定が間違っていますが、より適切に指定されたモデル \mathrm{M}_{3t} ははるかに優れた予測パフォーマンスを示しており、期待できるように \seHatPlain は b
- Workflowフェーズ: **LOO-CV / model comparison**
- 実務での読み方: elpd差だけでなくSEとPareto-kを読み、勝敗より『どのデータ点で負けるか』を確認する。
- MLflow連携: `loo_elpd, loo_elpd_diff, loo_se_diff, pareto_k_gt_0_7, reloo_count`
- 参照: [公式ページ](https://avehtari.github.io/Bayesian-Workflow/loo_comparison/loo_comparison.html#tinytable_x0hbb1e67wrox7g8nm3a) / [ソース候補](https://github.com/avehtari/Bayesian-Workflow/blob/eb00fa4397314ef7d90203382542bd44c590e289/loo_comparison/loo_comparison.R)

#### `loo-comparison-loo-comparison/tinytable_h48yz71dtzxi1mxz2u5h`

- 種別: `table` / 公式ID: `tinytable_h48yz71dtzxi1mxz2u5h` / ページ内順序: 6
- caption/列: model; elpd_diff; se_diff; p; M_3; 0; 0; -
- 周辺文脈（EN）: For the Poisson model we re-ran MCMC for all LOO-folds with high Pareto- \hat{k} diagnostic value (>0.7) (with reloo=TRUE in brms ), and for negative-binomial and zero-inflated neg
- 周辺文脈（JA, 自動訳）: 4 ゴキブリ / ポアソン モデルの場合、パレート \hat{k} 診断値が高い (>0.7) (brms の reloo=TRUE を使用) および負の二項およびゼロインフレート負をもつすべての LOO フォールドに対して MCMC を再実行しました。
- Workflowフェーズ: **LOO-CV / model comparison**
- 実務での読み方: elpd差だけでなくSEとPareto-kを読み、勝敗より『どのデータ点で負けるか』を確認する。
- MLflow連携: `loo_elpd, loo_elpd_diff, loo_se_diff, pareto_k_gt_0_7, reloo_count`
- 参照: [公式ページ](https://avehtari.github.io/Bayesian-Workflow/loo_comparison/loo_comparison.html#tinytable_h48yz71dtzxi1mxz2u5h) / [ソース候補](https://github.com/avehtari/Bayesian-Workflow/blob/eb00fa4397314ef7d90203382542bd44c590e289/loo_comparison/loo_comparison.R)

#### `loo-comparison-loo-comparison/tinytable_329ya6x7wykmsf1mg66f`

- 種別: `table` / 公式ID: `tinytable_329ya6x7wykmsf1mg66f` / ページ内順序: 7
- caption/列: model; elpd_diff; se_diff; p; M_4; 0; 0; -
- 周辺文脈（EN）: As we had used an ad-hoc square root transformation of pre-treatment number of roaches, we fitted a model \mathrm{M}_4 replacing the latent linear term for the square root of pre-t
- 周辺文脈（JA, 自動訳）: 4 ゴキブリ / 処理前のゴキブリ数のアドホック平方根変換を使用したため、事前 t の平方根の潜在線形項を置き換えるモデル \mathrm{M}_4 を当てはめました。
- Workflowフェーズ: **LOO-CV / model comparison**
- 実務での読み方: elpd差だけでなくSEとPareto-kを読み、勝敗より『どのデータ点で負けるか』を確認する。
- MLflow連携: `loo_elpd, loo_elpd_diff, loo_se_diff, pareto_k_gt_0_7, reloo_count`
- 参照: [公式ページ](https://avehtari.github.io/Bayesian-Workflow/loo_comparison/loo_comparison.html#tinytable_329ya6x7wykmsf1mg66f) / [ソース候補](https://github.com/avehtari/Bayesian-Workflow/blob/eb00fa4397314ef7d90203382542bd44c590e289/loo_comparison/loo_comparison.R)

### How many iterations to run and how many digits to report

- ページ: <https://avehtari.github.io/Bayesian-Workflow/digits/digits.html>
- ソース候補: <https://github.com/avehtari/Bayesian-Workflow/blob/eb00fa4397314ef7d90203382542bd44c590e289/digits/digits.R>

#### `digits-digits/figure-001`

- 種別: `figure` / 公式ID: `(none)` / ページ内順序: 1
- caption/列: figure 1
- 周辺文脈（EN）: Plot the data
- 周辺文脈（JA, 自動訳）: 3.1 キルピスヤルヴィのデータとモデル / データのプロット
- Workflowフェーズ: **EDA / observed data**
- 実務での読み方: モデル化前に、観測単位・外れ値・欠測・群構造・時系列性・上限/下限などを確認する。MLflowではデータ版と前処理版を固定する。
- MLflow連携: `dataset_uri, dataset_hash, preprocessing_version, n_obs, group_count`
- 参照: [公式ページ](https://avehtari.github.io/Bayesian-Workflow/digits/digits.html) / [ソース候補](https://github.com/avehtari/Bayesian-Workflow/blob/eb00fa4397314ef7d90203382542bd44c590e289/digits/digits.R)

#### `digits-digits/fig-kilpisjarvi_fit`

- 種別: `figure` / 公式ID: `fig-kilpisjarvi_fit` / ページ内順序: 2
- caption/列: Figure 1
- 周辺文脈（EN）: Plot the linear fit with 90% posterior interval
- 周辺文脈（JA, 自動訳）: 3.3 収束診断を実行 / 90% 事後間隔で線形近似をプロットする
- Workflowフェーズ: **Posterior summary / effect interpretation**
- 実務での読み方: 推定効果・不確実性・派生量を意思決定に接続する。平均だけでなく区間・分布・実務閾値超過確率を残す。
- MLflow連携: `posterior_draws_uri, model_code_hash, ci_width, decision_threshold_prob`
- 参照: [公式ページ](https://avehtari.github.io/Bayesian-Workflow/digits/digits.html#fig-kilpisjarvi_fit) / [ソース候補](https://github.com/avehtari/Bayesian-Workflow/blob/eb00fa4397314ef7d90203382542bd44c590e289/digits/digits.R)

#### `digits-digits/tinytable_1im3pxiljsnn0ptnjwbw`

- 種別: `table` / 公式ID: `tinytable_1im3pxiljsnn0ptnjwbw` / ページ内順序: 1
- caption/列: variable; mean; median; sd; mad; q5; q95; rhat
- 周辺文脈（EN）: We check \widehat{R} end ESS values, which in this case all look good.
- 周辺文脈（JA, 自動訳）: 3.3 収束診断を実行する / \widehat{R} エンド ESS 値をチェックします。この場合、すべて良好であることがわかります。
- Workflowフェーズ: **MCMC / computation diagnostics**
- 実務での読み方: 推論結果を解釈する前に、R-hat、ESS、divergence、treedepth、BFMI、trace/pairsを確認する。悪いrunは比較表から除外せず失敗として記録する。
- MLflow連携: `rhat_max, ess_bulk_min, ess_tail_min, divergences, treedepth_hits, bfmi_min`
- 参照: [公式ページ](https://avehtari.github.io/Bayesian-Workflow/digits/digits.html#tinytable_1im3pxiljsnn0ptnjwbw) / [ソース候補](https://github.com/avehtari/Bayesian-Workflow/blob/eb00fa4397314ef7d90203382542bd44c590e289/digits/digits.R)

#### `digits-digits/tinytable_0o8yyunp7xv9kufpt5ge`

- 種別: `table` / 公式ID: `tinytable_0o8yyunp7xv9kufpt5ge` / ページ内順序: 2
- caption/列: variable; mean; 5%; 95%; beta; 0.019; 0.0067; 0.032
- 周辺文脈（EN）: We start looking at the mean and 90% interval for the slope parameter beta
- 周辺文脈（JA, 自動訳）: 3.4 事後不確実性に基づいて報告する桁数 / 傾きパラメータ ベータの平均と 90% 間隔を調べ始めます
- Workflowフェーズ: **Posterior summary / effect interpretation**
- 実務での読み方: 推定効果・不確実性・派生量を意思決定に接続する。平均だけでなく区間・分布・実務閾値超過確率を残す。
- MLflow連携: `posterior_draws_uri, model_code_hash, ci_width, decision_threshold_prob`
- 参照: [公式ページ](https://avehtari.github.io/Bayesian-Workflow/digits/digits.html#tinytable_0o8yyunp7xv9kufpt5ge) / [ソース候補](https://github.com/avehtari/Bayesian-Workflow/blob/eb00fa4397314ef7d90203382542bd44c590e289/digits/digits.R)

#### `digits-digits/tinytable_4vyetdd9xgb1gpf2r263`

- 種別: `table` / 公式ID: `tinytable_4vyetdd9xgb1gpf2r263` / ページ内順序: 3
- caption/列: variable; mean; 5%; 95%; beta100; 1.9; 0.67; 3.2
- 周辺文脈（EN）: Let’s look at the mean and 90% interval for the expected temperature increase per 100 years.
- 周辺文脈（JA, 自動訳）: 3.4 事後不確実性に基づいて報告する桁数 / 100 年あたりの予想気温上昇の平均値と 90% 間隔を見てみましょう。
- Workflowフェーズ: **Posterior summary / effect interpretation**
- 実務での読み方: 推定効果・不確実性・派生量を意思決定に接続する。平均だけでなく区間・分布・実務閾値超過確率を残す。
- MLflow連携: `posterior_draws_uri, model_code_hash, ci_width, decision_threshold_prob`
- 参照: [公式ページ](https://avehtari.github.io/Bayesian-Workflow/digits/digits.html#tinytable_4vyetdd9xgb1gpf2r263) / [ソース候補](https://github.com/avehtari/Bayesian-Workflow/blob/eb00fa4397314ef7d90203382542bd44c590e289/digits/digits.R)

#### `digits-digits/tinytable_1ktag8ymx17fxo6w78xg`

- 種別: `table` / 公式ID: `tinytable_1ktag8ymx17fxo6w78xg` / ページ内順序: 4
- caption/列: variable; mean; 5%; 95%; beta100; 1.9; 0.67; 3.2
- 周辺文脈（EN）: which make each cell to show 2 significant digits, which is most often enough. Without tt() the output of summarize_draws() is a tibble, which looks like this
- 周辺文脈（JA, 自動訳）: 3.4 事後不確実性に基づいて報告する桁数 / 各セルに有効数字 2 桁が表示されるようになります。ほとんどの場合、これで十分です。 tt() を使用しない場合、summary_draws() の出力は次のようなティブルになります。
- Workflowフェーズ: **Posterior summary / effect interpretation**
- 実務での読み方: 推定効果・不確実性・派生量を意思決定に接続する。平均だけでなく区間・分布・実務閾値超過確率を残す。
- MLflow連携: `posterior_draws_uri, model_code_hash, ci_width, decision_threshold_prob`
- 参照: [公式ページ](https://avehtari.github.io/Bayesian-Workflow/digits/digits.html#tinytable_1ktag8ymx17fxo6w78xg) / [ソース候補](https://github.com/avehtari/Bayesian-Workflow/blob/eb00fa4397314ef7d90203382542bd44c590e289/digits/digits.R)

#### `digits-digits/tinytable_l5xwfw7pb74c8buca2a1`

- 種別: `table` / 公式ID: `tinytable_l5xwfw7pb74c8buca2a1` / ページ内順序: 5
- caption/列: variable; mcse_mean; mcse_q5; mcse_q95; beta100; 0.012; 0.028; 0.025
- 周辺文脈（EN）: Instead of repeating the estimation many times we can estimate the accuracy of the original sampling by computing Monte Carlo standard error (MCSE) that takes into account the quan
- 周辺文脈（JA, 自動訳）: 3.5 モンテカルロ標準誤差に基づいて報告する桁数 / 推定を何度も繰り返す代わりに、量を考慮したモンテカルロ標準誤差 (MCSE) を計算することで、元のサンプリングの精度を推定できます。
- Workflowフェーズ: **Unclassified / inspect manually**
- 実務での読み方: captionが薄い図表。前後の本文・コードchunk・公式ソースを確認して役割を確定する。
- MLflow連携: `source_page_url, source_repo_url, manual_review_status`
- 参照: [公式ページ](https://avehtari.github.io/Bayesian-Workflow/digits/digits.html#tinytable_l5xwfw7pb74c8buca2a1) / [ソース候補](https://github.com/avehtari/Bayesian-Workflow/blob/eb00fa4397314ef7d90203382542bd44c590e289/digits/digits.R)

#### `digits-digits/tinytable_q2yhdw8rys4z0683fof6`

- 種別: `table` / 公式ID: `tinytable_q2yhdw8rys4z0683fof6` / ページ内順序: 6
- caption/列: variable; ess_mean; ess_q5; ess_q95; beta100; 3945; 2843; 3247
- 周辺文脈（EN）: We show also the ESS values for mean and quantiles, to illustrate that the ESS values can be different for different quantities, but also that the same ESS doesn’t lead to the same
- 周辺文脈（JA, 自動訳）: 3.5 モンテカルロ標準誤差に基づいて報告する桁数 / ESS 値が量によって異なる可能性があることを示すために、平均値と分位点の ESS 値も示しますが、同じ ESS が同じ結果をもたらすわけではないことも示しています
- Workflowフェーズ: **MCMC / computation diagnostics**
- 実務での読み方: 推論結果を解釈する前に、R-hat、ESS、divergence、treedepth、BFMI、trace/pairsを確認する。悪いrunは比較表から除外せず失敗として記録する。
- MLflow連携: `rhat_max, ess_bulk_min, ess_tail_min, divergences, treedepth_hits, bfmi_min`
- 参照: [公式ページ](https://avehtari.github.io/Bayesian-Workflow/digits/digits.html#tinytable_q2yhdw8rys4z0683fof6) / [ソース候補](https://github.com/avehtari/Bayesian-Workflow/blob/eb00fa4397314ef7d90203382542bd44c590e289/digits/digits.R)

#### `digits-digits/tinytable_mllar4vkmd9un3uloji7`

- 種別: `table` / 公式ID: `tinytable_mllar4vkmd9un3uloji7` / ページ内順序: 7
- caption/列: variable; mean; mcse; beta0p; 0.99; 0.0011
- 周辺文脈（EN）: We can also report the probability that the temperature change is positive.
- 周辺文脈（JA, 自動訳）: 3.5 モンテカルロ標準誤差に基づいて報告する桁数 / 温度変化が正である確率も報告できます。
- Workflowフェーズ: **Unclassified / inspect manually**
- 実務での読み方: captionが薄い図表。前後の本文・コードchunk・公式ソースを確認して役割を確定する。
- MLflow連携: `source_page_url, source_repo_url, manual_review_status`
- 参照: [公式ページ](https://avehtari.github.io/Bayesian-Workflow/digits/digits.html#tinytable_mllar4vkmd9un3uloji7) / [ソース候補](https://github.com/avehtari/Bayesian-Workflow/blob/eb00fa4397314ef7d90203382542bd44c590e289/digits/digits.R)

#### `digits-digits/tinytable_6h59wihgzlf0w8b7txo1`

- 種別: `table` / 公式ID: `tinytable_6h59wihgzlf0w8b7txo1` / ページ内順序: 8
- caption/列: variable; mean; mcse; ESS; beta1p; 0.88; 0.006; 2960
- 周辺文脈（EN）: We additionaly compute probabilities that the temperature increase is more than 1, 2, 3 or 4 degrees, and corresponding MCSEs and ESSs.
- 周辺文脈（JA, 自動訳）: 3.5 モンテカルロ標準誤差に基づいて報告する桁数 / さらに、温度上昇が 1、2、3、または 4 度を超える確率と、対応する MCSE および ESS を計算します。
- Workflowフェーズ: **MCMC / computation diagnostics**
- 実務での読み方: 推論結果を解釈する前に、R-hat、ESS、divergence、treedepth、BFMI、trace/pairsを確認する。悪いrunは比較表から除外せず失敗として記録する。
- MLflow連携: `rhat_max, ess_bulk_min, ess_tail_min, divergences, treedepth_hits, bfmi_min`
- 参照: [公式ページ](https://avehtari.github.io/Bayesian-Workflow/digits/digits.html#tinytable_6h59wihgzlf0w8b7txo1) / [ソース候補](https://github.com/avehtari/Bayesian-Workflow/blob/eb00fa4397314ef7d90203382542bd44c590e289/digits/digits.R)

### Illustration of simple problematic posteriors

- ページ: <https://avehtari.github.io/Bayesian-Workflow/problems/problems.html>
- ソース候補: <https://github.com/avehtari/Bayesian-Workflow/blob/eb00fa4397314ef7d90203382542bd44c590e289/problems/problems.R>

#### `problems-problems/fig-separable_data`

- 種別: `figure` / 公式ID: `fig-separable_data` / ページ内順序: 1
- caption/列: Figure 1
- 周辺文脈（EN）: Univariate continous predictor x , binary target y , and the two classes are completely separable, which leads to unbounded likelihood.
- 周辺文脈（JA, 自動訳）: 2.1 データ / 単変量連続予測子 x 、バイナリ ターゲット y 、および 2 つのクラスは完全に分離可能であるため、無限尤度が得られます。
- Workflowフェーズ: **EDA / observed data**
- 実務での読み方: モデル化前に、観測単位・外れ値・欠測・群構造・時系列性・上限/下限などを確認する。MLflowではデータ版と前処理版を固定する。
- MLflow連携: `dataset_uri, dataset_hash, preprocessing_version, n_obs, group_count`
- 参照: [公式ページ](https://avehtari.github.io/Bayesian-Workflow/problems/problems.html#fig-separable_data) / [ソース候補](https://github.com/avehtari/Bayesian-Workflow/blob/eb00fa4397314ef7d90203382542bd44c590e289/problems/problems.R)

#### `problems-problems/fig-separable_pairs`

- 種別: `figure` / 公式ID: `fig-separable_pairs` / ページ内順序: 2
- caption/列: Figure 2
- 周辺文脈（EN）: The following Figure shows the posterior draws as marginal histograms and joint scatterplots. The range of the values is huge, which is typical for improper posterior, but the valu
- 周辺文脈（JA, 自動訳）: 2.3 収束診断 / 次の図は、事後描画を周辺ヒストグラムと結合散布図として示しています。値の範囲が非常に大きく、これは不適切な事後分布の典型ですが、値
- Workflowフェーズ: **Posterior summary / effect interpretation**
- 実務での読み方: 推定効果・不確実性・派生量を意思決定に接続する。平均だけでなく区間・分布・実務閾値超過確率を残す。
- MLflow連携: `posterior_draws_uri, model_code_hash, ci_width, decision_threshold_prob`
- 参照: [公式ページ](https://avehtari.github.io/Bayesian-Workflow/problems/problems.html#fig-separable_pairs) / [ソース候補](https://github.com/avehtari/Bayesian-Workflow/blob/eb00fa4397314ef7d90203382542bd44c590e289/problems/problems.R)

#### `problems-problems/fig-separable_prior_pairs`

- 種別: `figure` / 公式ID: `fig-separable_prior_pairs` / ページ内順序: 3
- caption/列: Figure 3
- 周辺文脈（EN）: The following figure shows the more reasonable marginal histograms and joint scatterplots of the posterior sample.
- 周辺文脈（JA, 自動訳）: 2.6 収束診断 / 次の図は、後方サンプルのより合理的な周辺ヒストグラムと結合散布図を示しています。
- Workflowフェーズ: **Posterior summary / effect interpretation**
- 実務での読み方: 推定効果・不確実性・派生量を意思決定に接続する。平均だけでなく区間・分布・実務閾値超過確率を残す。
- MLflow連携: `posterior_draws_uri, model_code_hash, ci_width, decision_threshold_prob`
- 参照: [公式ページ](https://avehtari.github.io/Bayesian-Workflow/problems/problems.html#fig-separable_prior_pairs) / [ソース候補](https://github.com/avehtari/Bayesian-Workflow/blob/eb00fa4397314ef7d90203382542bd44c590e289/problems/problems.R)

#### `problems-problems/fig-unusedparam_pairs`

- 種別: `figure` / 公式ID: `fig-unusedparam_pairs` / ページ内順序: 4
- caption/列: Figure 4
- 周辺文脈（EN）: \widehat{R} , Bulk-ESS, and Tail-ESS look good for alpha and beta, but really bad for gamma , clearly pointing where to look for problems in the model code. The histogram of gamma`
- 周辺文脈（JA, 自動訳）: 3.2 収束診断 / \widehat{R} 、Bulk-ESS、および Tail-ESS は、 alpha と beta には適しているように見えますが、 gamma には非常に悪く、モデル コード内で問題を探す場所を明確に示しています。ガンマ`のヒストグラム
- Workflowフェーズ: **Posterior summary / effect interpretation**
- 実務での読み方: 推定効果・不確実性・派生量を意思決定に接続する。平均だけでなく区間・分布・実務閾値超過確率を残す。
- MLflow連携: `posterior_draws_uri, model_code_hash, ci_width, decision_threshold_prob`
- 参照: [公式ページ](https://avehtari.github.io/Bayesian-Workflow/problems/problems.html#fig-unusedparam_pairs) / [ソース候補](https://github.com/avehtari/Bayesian-Workflow/blob/eb00fa4397314ef7d90203382542bd44c590e289/problems/problems.R)

#### `problems-problems/fig-unusedparam_trace`

- 種別: `figure` / 公式ID: `fig-unusedparam_trace` / ページ内順序: 5
- caption/列: Figure 5
- 周辺文脈（EN）: Non-mixing is well diagnosed by \widehat{R} and ESS, but the following Figure shows one of the rare cases where trace plots are useful to illustrate the type of non-mixing in case
- 周辺文脈（JA, 自動訳）: 3.2 収束診断 / 非混合は \widehat{R} と ESS によって適切に診断されますが、次の図は、トレース プロットが非混合のタイプを説明するのに役立つ稀なケースの 1 つを示しています。
- Workflowフェーズ: **Posterior summary / effect interpretation**
- 実務での読み方: 推定効果・不確実性・派生量を意思決定に接続する。平均だけでなく区間・分布・実務閾値超過確率を残す。
- MLflow連携: `posterior_draws_uri, model_code_hash, ci_width, decision_threshold_prob`
- 参照: [公式ページ](https://avehtari.github.io/Bayesian-Workflow/problems/problems.html#fig-unusedparam_trace) / [ソース候補](https://github.com/avehtari/Bayesian-Workflow/blob/eb00fa4397314ef7d90203382542bd44c590e289/problems/problems.R)

#### `problems-problems/fig-competing_params_pairs`

- 種別: `figure` / 公式ID: `fig-competing_params_pairs` / ページ内順序: 6
- caption/列: Figure 6
- 周辺文脈（EN）: The following figure shows marginal histograms and joint scatterplots, and we can see that alpha and beta[1] are highly correlated.
- 周辺文脈（JA, 自動訳）: 4.3 収束診断 / 次の図は周辺ヒストグラムと結合散布図を示しており、アルファとベータ[1]が高度に相関していることがわかります。
- Workflowフェーズ: **Posterior summary / effect interpretation**
- 実務での読み方: 推定効果・不確実性・派生量を意思決定に接続する。平均だけでなく区間・分布・実務閾値超過確率を残す。
- MLflow連携: `posterior_draws_uri, model_code_hash, ci_width, decision_threshold_prob`
- 参照: [公式ページ](https://avehtari.github.io/Bayesian-Workflow/problems/problems.html#fig-competing_params_pairs) / [ソース候補](https://github.com/avehtari/Bayesian-Workflow/blob/eb00fa4397314ef7d90203382542bd44c590e289/problems/problems.R)

#### `problems-problems/fig-kilpisjarvi_data`

- 種別: `figure` / 公式ID: `fig-kilpisjarvi_data` / ページ内順序: 7
- caption/列: Figure 7
- 周辺文脈（EN）: The data are Kilpisjärvi summer month temperatures 1952-2013 measured by Finnish Meteorological Institute.
- 周辺文脈（JA, 自動訳）: 5.1 データ / データは、フィンランド気象研究所が測定した 1952 年から 2013 年のキルピスヤルビの夏月の気温です。
- Workflowフェーズ: **EDA / observed data**
- 実務での読み方: モデル化前に、観測単位・外れ値・欠測・群構造・時系列性・上限/下限などを確認する。MLflowではデータ版と前処理版を固定する。
- MLflow連携: `dataset_uri, dataset_hash, preprocessing_version, n_obs, group_count`
- 参照: [公式ページ](https://avehtari.github.io/Bayesian-Workflow/problems/problems.html#fig-kilpisjarvi_data) / [ソース候補](https://github.com/avehtari/Bayesian-Workflow/blob/eb00fa4397314ef7d90203382542bd44c590e289/problems/problems.R)

#### `problems-problems/fig-correlating_params_pairs`

- 種別: `figure` / 公式ID: `fig-correlating_params_pairs` / ページ内順序: 8
- caption/列: Figure 8
- 周辺文脈（EN）: ESS estimates are above the diagnostic threshold, but lower than we would expect for such a low dimensional model, unless there are strong posterior correlations. The following Fig
- 周辺文脈（JA, 自動訳）: 5.3 収束診断/ESS 推定値は診断閾値を上回っていますが、強い事後相関がない限り、このような低次元モデルで予想されるよりも低くなります。次の図
- Workflowフェーズ: **Posterior summary / effect interpretation**
- 実務での読み方: 推定効果・不確実性・派生量を意思決定に接続する。平均だけでなく区間・分布・実務閾値超過確率を残す。
- MLflow連携: `posterior_draws_uri, model_code_hash, ci_width, decision_threshold_prob`
- 参照: [公式ページ](https://avehtari.github.io/Bayesian-Workflow/problems/problems.html#fig-correlating_params_pairs) / [ソース候補](https://github.com/avehtari/Bayesian-Workflow/blob/eb00fa4397314ef7d90203382542bd44c590e289/problems/problems.R)

#### `problems-problems/fig-uncorrelating_params_pairs`

- 種別: `figure` / 公式ID: `fig-uncorrelating_params_pairs` / ページ内順序: 9
- caption/列: Figure 9
- 周辺文脈（EN）: The following figure shows the scatter plot.
- 周辺文脈（JA, 自動訳）: 5.5 収束診断 / 次の図は散布図を示しています。
- Workflowフェーズ: **Posterior summary / effect interpretation**
- 実務での読み方: 推定効果・不確実性・派生量を意思決定に接続する。平均だけでなく区間・分布・実務閾値超過確率を残す。
- MLflow連携: `posterior_draws_uri, model_code_hash, ci_width, decision_threshold_prob`
- 参照: [公式ページ](https://avehtari.github.io/Bayesian-Workflow/problems/problems.html#fig-uncorrelating_params_pairs) / [ソース候補](https://github.com/avehtari/Bayesian-Workflow/blob/eb00fa4397314ef7d90203382542bd44c590e289/problems/problems.R)

#### `problems-problems/fig-bimodal1_hist`

- 種別: `figure` / 公式ID: `fig-bimodal1_hist` / ページ内順序: 10
- caption/列: Figure 10
- 周辺文脈（EN）: The \widehat{R} values for mu are large and ESS values for mu are small indicating convergence problems. The following figure shows the histogram and trace plots of the posterior d
- 周辺文脈（JA, 自動訳）: 6.3 収束診断 / mu の \widehat{R} 値は大きく、mu の ESS 値は小さいので、収束の問題を示しています。次の図は、事後 d のヒストグラムとトレース プロットを示しています。
- Workflowフェーズ: **Posterior summary / effect interpretation**
- 実務での読み方: 推定効果・不確実性・派生量を意思決定に接続する。平均だけでなく区間・分布・実務閾値超過確率を残す。
- MLflow連携: `posterior_draws_uri, model_code_hash, ci_width, decision_threshold_prob`
- 参照: [公式ページ](https://avehtari.github.io/Bayesian-Workflow/problems/problems.html#fig-bimodal1_hist) / [ソース候補](https://github.com/avehtari/Bayesian-Workflow/blob/eb00fa4397314ef7d90203382542bd44c590e289/problems/problems.R)

#### `problems-problems/fig-bimodal2_hist`

- 種別: `figure` / 公式ID: `fig-bimodal2_hist` / ページ内順序: 11
- caption/列: Figure 11
- 周辺文脈（EN）: Two modes are visible.
- 周辺文脈（JA, 自動訳）: 7.1 コンバージェンス診断 / 2 つのモードが表示されます。
- Workflowフェーズ: **Posterior summary / effect interpretation**
- 実務での読み方: 推定効果・不確実性・派生量を意思決定に接続する。平均だけでなく区間・分布・実務閾値超過確率を残す。
- MLflow連携: `posterior_draws_uri, model_code_hash, ci_width, decision_threshold_prob`
- 参照: [公式ページ](https://avehtari.github.io/Bayesian-Workflow/problems/problems.html#fig-bimodal2_hist) / [ソース候補](https://github.com/avehtari/Bayesian-Workflow/blob/eb00fa4397314ef7d90203382542bd44c590e289/problems/problems.R)

#### `problems-problems/fig-bimodal2_trace`

- 種別: `figure` / 公式ID: `fig-bimodal2_trace` / ページ内順序: 12
- caption/列: Figure 12
- 周辺文脈（EN）: Trace plot is not very useful. It shows the chains are jumping between modes, but it’s difficult to see whether the jumps happen often enough and chains are mixing well.
- 周辺文脈（JA, 自動訳）: 7.1 収束診断/トレースプロットはあまり役に立ちません。これはチェーンがモード間をジャンプしていることを示していますが、ジャンプが十分な頻度で発生し、チェーンが適切に混合されているかどうかを確認するのは困難です。
- Workflowフェーズ: **Posterior summary / effect interpretation**
- 実務での読み方: 推定効果・不確実性・派生量を意思決定に接続する。平均だけでなく区間・分布・実務閾値超過確率を残す。
- MLflow連携: `posterior_draws_uri, model_code_hash, ci_width, decision_threshold_prob`
- 参照: [公式ページ](https://avehtari.github.io/Bayesian-Workflow/problems/problems.html#fig-bimodal2_trace) / [ソース候補](https://github.com/avehtari/Bayesian-Workflow/blob/eb00fa4397314ef7d90203382542bd44c590e289/problems/problems.R)

#### `problems-problems/fig-bimodal2_rank_ecdf_diff`

- 種別: `figure` / 公式ID: `fig-bimodal2_rank_ecdf_diff` / ページ内順序: 13
- caption/列: Figure 13
- 周辺文脈（EN）: Rank ECDF plot ( Säilynoja, Bürkner, and Vehtari 2022 ) indicates good mixing as all chains have their lines inside the envelope (the envelope assumes no autocorrelation, which is
- 周辺文脈（JA, 自動訳）: 7.1 収束診断 / ランク ECDF プロット ( Säilynoja、Bürkner、および Vehtari 2022 ) は、すべてのチェーンのラインがエンベロープ内にあるため、良好な混合を示しています (エンベロープは自己相関がないと仮定しています。
- Workflowフェーズ: **Posterior summary / effect interpretation**
- 実務での読み方: 推定効果・不確実性・派生量を意思決定に接続する。平均だけでなく区間・分布・実務閾値超過確率を残す。
- MLflow連携: `posterior_draws_uri, model_code_hash, ci_width, decision_threshold_prob`
- 参照: [公式ページ](https://avehtari.github.io/Bayesian-Workflow/problems/problems.html#fig-bimodal2_rank_ecdf_diff) / [ソース候補](https://github.com/avehtari/Bayesian-Workflow/blob/eb00fa4397314ef7d90203382542bd44c590e289/problems/problems.R)

#### `problems-problems/fig-poisson_data`

- 種別: `figure` / 公式ID: `fig-poisson_data` / ページ内順序: 14
- caption/列: Figure 14
- 周辺文脈（EN）: We intentionally generate the data so that there are initialization problems, but the same problem is common with real data when the scale of the predictors is large or small compa
- 周辺文脈（JA, 自動訳）: 8.1 データ / 初期化問題が発生するように意図的にデータを生成していますが、予測子の規模が大きいか小さい場合、同じ問題が実際のデータでもよく発生します。
- Workflowフェーズ: **EDA / observed data**
- 実務での読み方: モデル化前に、観測単位・外れ値・欠測・群構造・時系列性・上限/下限などを確認する。MLflowではデータ版と前処理版を固定する。
- MLflow連携: `dataset_uri, dataset_hash, preprocessing_version, n_obs, group_count`
- 参照: [公式ページ](https://avehtari.github.io/Bayesian-Workflow/problems/problems.html#fig-poisson_data) / [ソース候補](https://github.com/avehtari/Bayesian-Workflow/blob/eb00fa4397314ef7d90203382542bd44c590e289/problems/problems.R)

#### `problems-problems/fig-poisson_pairs`

- 種別: `figure` / 公式ID: `fig-poisson_pairs` / ページ内順序: 15
- caption/列: Figure 15
- 周辺文脈（EN）: \widehat{R} values are large and ESS values are small, indicating bad mixing. Marginal histograms and joint scatterplots of the posterior draws in the figure below clearly show tha
- 周辺文脈（JA, 自動訳）: 8.3 収束診断 / \widehat{R} 値が大きく、ESS 値が小さい場合は、混合が不良であることを示します。以下の図の事後描画の周辺ヒストグラムと結合散布図は、次のことを明確に示しています。
- Workflowフェーズ: **Posterior summary / effect interpretation**
- 実務での読み方: 推定効果・不確実性・派生量を意思決定に接続する。平均だけでなく区間・分布・実務閾値超過確率を残す。
- MLflow連携: `posterior_draws_uri, model_code_hash, ci_width, decision_threshold_prob`
- 参照: [公式ページ](https://avehtari.github.io/Bayesian-Workflow/problems/problems.html#fig-poisson_pairs) / [ソース候補](https://github.com/avehtari/Bayesian-Workflow/blob/eb00fa4397314ef7d90203382542bd44c590e289/problems/problems.R)

#### `problems-problems/fig-poisson_data2`

- 種別: `figure` / 公式ID: `fig-poisson_data2` / ページ内順序: 16
- caption/列: Figure 16
- 周辺文脈（EN）: Sometimes an easy option is to change the initialization range. For example, in this the sampling succeeds if the initial values are drawn from the range (-0.001, 0.001) . Alternat
- 周辺文脈（JA, 自動訳）: 8.4 スケーリングされたデータ / 場合によっては、初期化範囲を変更するのが簡単なオプションです。たとえば、この例では、初期値が (-0.001, 0.001) の範囲から抽出された場合、サンプリングは成功します。代替品
- Workflowフェーズ: **EDA / observed data**
- 実務での読み方: モデル化前に、観測単位・外れ値・欠測・群構造・時系列性・上限/下限などを確認する。MLflowではデータ版と前処理版を固定する。
- MLflow連携: `dataset_uri, dataset_hash, preprocessing_version, n_obs, group_count`
- 参照: [公式ページ](https://avehtari.github.io/Bayesian-Workflow/problems/problems.html#fig-poisson_data2) / [ソース候補](https://github.com/avehtari/Bayesian-Workflow/blob/eb00fa4397314ef7d90203382542bd44c590e289/problems/problems.R)

#### `problems-problems/fig-thick_tail_pairs`

- 種別: `figure` / 公式ID: `fig-thick_tail_pairs` / ページ内順序: 17
- caption/列: Figure 17
- 周辺文脈（EN）: The rounded \widehat{R} values look good, ESS values are low. Looking at the marginal histograms and joint scatterplots of the posterior draws in the following figure show a thick
- 周辺文脈（JA, 自動訳）: 9.2 収束診断 / 丸められた \widehat{R} 値は良好に見えますが、ESS 値は低いです。次の図の事後描画の周辺ヒストグラムと結合散布図を見ると、太い
- Workflowフェーズ: **Posterior summary / effect interpretation**
- 実務での読み方: 推定効果・不確実性・派生量を意思決定に接続する。平均だけでなく区間・分布・実務閾値超過確率を残す。
- MLflow連携: `posterior_draws_uri, model_code_hash, ci_width, decision_threshold_prob`
- 参照: [公式ページ](https://avehtari.github.io/Bayesian-Workflow/problems/problems.html#fig-thick_tail_pairs) / [ソース候補](https://github.com/avehtari/Bayesian-Workflow/blob/eb00fa4397314ef7d90203382542bd44c590e289/problems/problems.R)

#### `problems-problems/fig-thick_tail_rank_ecdf_diff`

- 種別: `figure` / 公式ID: `fig-thick_tail_rank_ecdf_diff` / ページ内順序: 18
- caption/列: Figure 18
- 周辺文脈（EN）: Rank ECDF plot indicates good mixing as all chains have their lines inside the envelope (the envelope assumes no autocorrelation, which is the reason to thin the draws here)
- 周辺文脈（JA, 自動訳）: 9.2 収束診断 / ランク ECDF プロットは、すべてのチェーンのラインがエンベロープ内にあるため、良好な混合を示しています (エンベロープは自己相関を想定していないため、ここで描画を薄くする理由です)。
- Workflowフェーズ: **Posterior summary / effect interpretation**
- 実務での読み方: 推定効果・不確実性・派生量を意思決定に接続する。平均だけでなく区間・分布・実務閾値超過確率を残す。
- MLflow連携: `posterior_draws_uri, model_code_hash, ci_width, decision_threshold_prob`
- 参照: [公式ページ](https://avehtari.github.io/Bayesian-Workflow/problems/problems.html#fig-thick_tail_rank_ecdf_diff) / [ソース候補](https://github.com/avehtari/Bayesian-Workflow/blob/eb00fa4397314ef7d90203382542bd44c590e289/problems/problems.R)

#### `problems-problems/fig-thick_tail_rank_ecdf_diff_more`

- 種別: `figure` / 公式ID: `fig-thick_tail_rank_ecdf_diff_more` / ページ内順序: 19
- caption/列: Figure 19
- 周辺文脈（EN）: More iterations confirm a reasonable mixing.
- 周辺文脈（JA, 自動訳）: 9.2 収束診断 / さらなる反復により、適切な混合が確認されます。
- Workflowフェーズ: **Posterior summary / effect interpretation**
- 実務での読み方: 推定効果・不確実性・派生量を意思決定に接続する。平均だけでなく区間・分布・実務閾値超過確率を残す。
- MLflow連携: `posterior_draws_uri, model_code_hash, ci_width, decision_threshold_prob`
- 参照: [公式ページ](https://avehtari.github.io/Bayesian-Workflow/problems/problems.html#fig-thick_tail_rank_ecdf_diff_more) / [ソース候補](https://github.com/avehtari/Bayesian-Workflow/blob/eb00fa4397314ef7d90203382542bd44c590e289/problems/problems.R)

#### `problems-problems/figure-020`

- 種別: `figure` / 公式ID: `(none)` / ページ内順序: 20
- caption/列: figure 20
- 周辺文脈（EN）: Plot scatter plot of \mu_1 vs \log\sigma_0 with divergences shown in red (bayesplot)
- 周辺文脈（JA, 自動訳）: 10 ファンネル / \mu_1 対 \log\sigma_0 の散布図 (発散は赤で表示) (bayesplot)
- Workflowフェーズ: **Posterior summary / effect interpretation**
- 実務での読み方: 推定効果・不確実性・派生量を意思決定に接続する。平均だけでなく区間・分布・実務閾値超過確率を残す。
- MLflow連携: `posterior_draws_uri, model_code_hash, ci_width, decision_threshold_prob`
- 参照: [公式ページ](https://avehtari.github.io/Bayesian-Workflow/problems/problems.html) / [ソース候補](https://github.com/avehtari/Bayesian-Workflow/blob/eb00fa4397314ef7d90203382542bd44c590e289/problems/problems.R)

#### `problems-problems/figure-021`

- 種別: `figure` / 公式ID: `(none)` / ページ内順序: 21
- caption/列: figure 21
- 周辺文脈（EN）: Plot scatter plot of \mu_1 vs \log\sigma_0 with divergences shown in red (ggplot)
- 周辺文脈（JA, 自動訳）: 10 ファンネル / \mu_1 対 \log\sigma_0 の散布図 (発散は赤で表示) (ggplot)
- Workflowフェーズ: **Posterior summary / effect interpretation**
- 実務での読み方: 推定効果・不確実性・派生量を意思決定に接続する。平均だけでなく区間・分布・実務閾値超過確率を残す。
- MLflow連携: `posterior_draws_uri, model_code_hash, ci_width, decision_threshold_prob`
- 参照: [公式ページ](https://avehtari.github.io/Bayesian-Workflow/problems/problems.html) / [ソース候補](https://github.com/avehtari/Bayesian-Workflow/blob/eb00fa4397314ef7d90203382542bd44c590e289/problems/problems.R)

#### `problems-problems/figure-022`

- 種別: `figure` / 公式ID: `(none)` / ページ内順序: 22
- caption/列: figure 22
- 周辺文脈（EN）: Plot scatter plot of \mu_1 vs \log\sigma_0 with divergences shown in red (bayesplot)
- 周辺文脈（JA, 自動訳）: 10 ファンネル / \mu_1 対 \log\sigma_0 の散布図 (発散は赤で表示) (bayesplot)
- Workflowフェーズ: **Posterior summary / effect interpretation**
- 実務での読み方: 推定効果・不確実性・派生量を意思決定に接続する。平均だけでなく区間・分布・実務閾値超過確率を残す。
- MLflow連携: `posterior_draws_uri, model_code_hash, ci_width, decision_threshold_prob`
- 参照: [公式ページ](https://avehtari.github.io/Bayesian-Workflow/problems/problems.html) / [ソース候補](https://github.com/avehtari/Bayesian-Workflow/blob/eb00fa4397314ef7d90203382542bd44c590e289/problems/problems.R)

#### `problems-problems/figure-023`

- 種別: `figure` / 公式ID: `(none)` / ページ内順序: 23
- caption/列: figure 23
- 周辺文脈（EN）: Plot scatter plot of \mu_1 vs \log\sigma_0 with divergences shown in red (ggplot)
- 周辺文脈（JA, 自動訳）: 10 ファンネル / \mu_1 対 \log\sigma_0 の散布図 (発散は赤で表示) (ggplot)
- Workflowフェーズ: **Posterior summary / effect interpretation**
- 実務での読み方: 推定効果・不確実性・派生量を意思決定に接続する。平均だけでなく区間・分布・実務閾値超過確率を残す。
- MLflow連携: `posterior_draws_uri, model_code_hash, ci_width, decision_threshold_prob`
- 参照: [公式ページ](https://avehtari.github.io/Bayesian-Workflow/problems/problems.html) / [ソース候補](https://github.com/avehtari/Bayesian-Workflow/blob/eb00fa4397314ef7d90203382542bd44c590e289/problems/problems.R)

#### `problems-problems/figure-024`

- 種別: `figure` / 公式ID: `(none)` / ページ内順序: 24
- caption/列: figure 24
- 周辺文脈（EN）: Plot scatter plot of \mu_1 vs \log\sigma_0 with divergences shown in red (bayesplot)
- 周辺文脈（JA, 自動訳）: 10 ファンネル / \mu_1 対 \log\sigma_0 の散布図 (発散は赤で表示) (bayesplot)
- Workflowフェーズ: **Posterior summary / effect interpretation**
- 実務での読み方: 推定効果・不確実性・派生量を意思決定に接続する。平均だけでなく区間・分布・実務閾値超過確率を残す。
- MLflow連携: `posterior_draws_uri, model_code_hash, ci_width, decision_threshold_prob`
- 参照: [公式ページ](https://avehtari.github.io/Bayesian-Workflow/problems/problems.html) / [ソース候補](https://github.com/avehtari/Bayesian-Workflow/blob/eb00fa4397314ef7d90203382542bd44c590e289/problems/problems.R)

#### `problems-problems/figure-025`

- 種別: `figure` / 公式ID: `(none)` / ページ内順序: 25
- caption/列: figure 25
- 周辺文脈（EN）: Plot scatter plot of \mu_1 vs \log\sigma_0 with divergences shown in red (ggplot)
- 周辺文脈（JA, 自動訳）: 10 ファンネル / \mu_1 対 \log\sigma_0 の散布図 (発散は赤で表示) (ggplot)
- Workflowフェーズ: **Posterior summary / effect interpretation**
- 実務での読み方: 推定効果・不確実性・派生量を意思決定に接続する。平均だけでなく区間・分布・実務閾値超過確率を残す。
- MLflow連携: `posterior_draws_uri, model_code_hash, ci_width, decision_threshold_prob`
- 参照: [公式ページ](https://avehtari.github.io/Bayesian-Workflow/problems/problems.html) / [ソース候補](https://github.com/avehtari/Bayesian-Workflow/blob/eb00fa4397314ef7d90203382542bd44c590e289/problems/problems.R)

#### `problems-problems/fig-kilpis-funnel`

- 種別: `figure` / 公式ID: `fig-kilpis-funnel` / ページ内順序: 26
- caption/列: Figure 20
- 周辺文脈（EN）: If we compare the scatter plots side by side, we clearly see that increasing adapt_delta and getting rid of divergences did not solve the funnel problem and the posterior estimates
- 周辺文脈（JA, 自動訳）: 10 ファネル / 散布図を並べて比較すると、adapt_delta を増やして発散を取り除いても、ファネルの問題と事後推定値は解決されなかったことがはっきりとわかります。
- Workflowフェーズ: **Posterior summary / effect interpretation**
- 実務での読み方: 推定効果・不確実性・派生量を意思決定に接続する。平均だけでなく区間・分布・実務閾値超過確率を残す。
- MLflow連携: `posterior_draws_uri, model_code_hash, ci_width, decision_threshold_prob`
- 参照: [公式ページ](https://avehtari.github.io/Bayesian-Workflow/problems/problems.html#fig-kilpis-funnel) / [ソース候補](https://github.com/avehtari/Bayesian-Workflow/blob/eb00fa4397314ef7d90203382542bd44c590e289/problems/problems.R)

### Declining exponentials

- ページ: <https://avehtari.github.io/Bayesian-Workflow/declining_exponentials/declining_exponentials.html>
- ソース候補: <https://github.com/avehtari/Bayesian-Workflow/blob/eb00fa4397314ef7d90203382542bd44c590e289/declining_exponentials/declining_exponentials.R>

#### `declining-exponentials-declining-exponentials/fig-true-and-simulated`

- 種別: `figure` / 公式ID: `fig-true-and-simulated` / ページ内順序: 1
- caption/列: Figure 1
- 周辺文脈（EN）: Here is a graph of the true curve and the simulated data:
- 周辺文脈（JA, 自動訳）: 2.1 シミュレートされたデータ / 以下は、真の曲線とシミュレートされたデータのグラフです。
- Workflowフェーズ: **EDA / observed data**
- 実務での読み方: モデル化前に、観測単位・外れ値・欠測・群構造・時系列性・上限/下限などを確認する。MLflowではデータ版と前処理版を固定する。
- MLflow連携: `dataset_uri, dataset_hash, preprocessing_version, n_obs, group_count`
- 参照: [公式ページ](https://avehtari.github.io/Bayesian-Workflow/declining_exponentials/declining_exponentials.html#fig-true-and-simulated) / [ソース候補](https://github.com/avehtari/Bayesian-Workflow/blob/eb00fa4397314ef7d90203382542bd44c590e289/declining_exponentials/declining_exponentials.R)

#### `declining-exponentials-declining-exponentials/fig-10-data-points`

- 種別: `figure` / 公式ID: `fig-10-data-points` / ページ内順序: 2
- caption/列: Figure 2
- 周辺文脈（EN）: With weaker data, though, the constraints could make a difference. We could experiment on this by doing the same simulation but with just N=10 data points:
- 周辺文脈（JA, 自動訳）: 2.2 小規模なシミュレーション データ / ただし、データが弱い場合は、制約によって違いが生じる可能性があります。これについては、N=10 個のデータ ポイントだけを使用して同じシミュレーションを実行することで実験できます。
- Workflowフェーズ: **EDA / observed data**
- 実務での読み方: モデル化前に、観測単位・外れ値・欠測・群構造・時系列性・上限/下限などを確認する。MLflowではデータ版と前処理版を固定する。
- MLflow連携: `dataset_uri, dataset_hash, preprocessing_version, n_obs, group_count`
- 参照: [公式ページ](https://avehtari.github.io/Bayesian-Workflow/declining_exponentials/declining_exponentials.html#fig-10-data-points) / [ソース候補](https://github.com/avehtari/Bayesian-Workflow/blob/eb00fa4397314ef7d90203382542bd44c590e289/declining_exponentials/declining_exponentials.R)

#### `declining-exponentials-declining-exponentials/fig-positive-true-and-simulated`

- 種別: `figure` / 公式ID: `fig-positive-true-and-simulated` / ページ内順序: 3
- caption/列: Figure 3
- 周辺文脈（EN）: As before, we can simulate fake data from this model:
- 周辺文脈（JA, 自動訳）: 2.3 正のシミュレートされたデータ / 前と同様に、このモデルから偽のデータをシミュレートできます。
- Workflowフェーズ: **EDA / observed data**
- 実務での読み方: モデル化前に、観測単位・外れ値・欠測・群構造・時系列性・上限/下限などを確認する。MLflowではデータ版と前処理版を固定する。
- MLflow連携: `dataset_uri, dataset_hash, preprocessing_version, n_obs, group_count`
- 参照: [公式ページ](https://avehtari.github.io/Bayesian-Workflow/declining_exponentials/declining_exponentials.html#fig-positive-true-and-simulated) / [ソース候補](https://github.com/avehtari/Bayesian-Workflow/blob/eb00fa4397314ef7d90203382542bd44c590e289/declining_exponentials/declining_exponentials.R)

#### `declining-exponentials-declining-exponentials/fig-sumexp-true-and-simulated`

- 種別: `figure` / 公式ID: `fig-sumexp-true-and-simulated` / ページ内順序: 4
- caption/列: Figure 4
- 周辺文脈（EN）: Here is a graph of the true curve and the simulated data:
- 周辺文脈（JA, 自動訳）: 3 減少する指数関数の合計 / これは、真の曲線とシミュレートされたデータのグラフです。
- Workflowフェーズ: **EDA / observed data**
- 実務での読み方: モデル化前に、観測単位・外れ値・欠測・群構造・時系列性・上限/下限などを確認する。MLflowではデータ版と前処理版を固定する。
- MLflow連携: `dataset_uri, dataset_hash, preprocessing_version, n_obs, group_count`
- 参照: [公式ページ](https://avehtari.github.io/Bayesian-Workflow/declining_exponentials/declining_exponentials.html#fig-sumexp-true-and-simulated) / [ソース候補](https://github.com/avehtari/Bayesian-Workflow/blob/eb00fa4397314ef7d90203382542bd44c590e289/declining_exponentials/declining_exponentials.R)

#### `declining-exponentials-declining-exponentials/fig-sumexp-true-model`

- 種別: `figure` / 公式ID: `fig-sumexp-true-model` / ページ内順序: 5
- caption/列: Figure 5
- 周辺文脈（EN）: What happened?? It turns out that these two declining exponentials are very hard to detect. Look: here’s a graph of the two-component model for the expected data, y=1.0e^{-0.1x}+0.
- 周辺文脈（JA, 自動訳）: 3 減少する指数関数の合計 / 何が起こった??これら 2 つの指数関数的減少は、検出するのが非常に難しいことがわかります。見てください。これは、予想されるデータ y=1.0e^{-0.1x}+0 の 2 成分モデルのグラフです。
- Workflowフェーズ: **EDA / observed data**
- 実務での読み方: モデル化前に、観測単位・外れ値・欠測・群構造・時系列性・上限/下限などを確認する。MLflowではデータ版と前処理版を固定する。
- MLflow連携: `dataset_uri, dataset_hash, preprocessing_version, n_obs, group_count`
- 参照: [公式ページ](https://avehtari.github.io/Bayesian-Workflow/declining_exponentials/declining_exponentials.html#fig-sumexp-true-model) / [ソース候補](https://github.com/avehtari/Bayesian-Workflow/blob/eb00fa4397314ef7d90203382542bd44c590e289/declining_exponentials/declining_exponentials.R)

#### `declining-exponentials-declining-exponentials/fig-sumexp-true-and-one-component`

- 種別: `figure` / 公式ID: `fig-sumexp-true-and-one-component` / ページ内順序: 6
- caption/列: Figure 6
- 周辺文脈（EN）: And now we’ll overlay a graph of a particular one-component model, y=1.8e^{-0.135x} :
- 周辺文脈（JA, 自動訳）: 3 減少する指数関数の合計 / 次に、特定の 1 成分モデル y=1.8e^{-0.135x} のグラフを重ね合わせます。
- Workflowフェーズ: **Unclassified / inspect manually**
- 実務での読み方: captionが薄い図表。前後の本文・コードchunk・公式ソースを確認して役割を確定する。
- MLflow連携: `source_page_url, source_repo_url, manual_review_status`
- 参照: [公式ページ](https://avehtari.github.io/Bayesian-Workflow/declining_exponentials/declining_exponentials.html#fig-sumexp-true-and-one-component) / [ソース候補](https://github.com/avehtari/Bayesian-Workflow/blob/eb00fa4397314ef7d90203382542bd44c590e289/declining_exponentials/declining_exponentials.R)

### Coding a series of models: Simulated data of movie ratings

- ページ: <https://avehtari.github.io/Bayesian-Workflow/movies/movies.html>
- ソース候補: <https://github.com/avehtari/Bayesian-Workflow/blob/eb00fa4397314ef7d90203382542bd44c590e289/movies/movies.R>

#### `movies-movies/fig-movies_1`

- 種別: `figure` / 公式ID: `fig-movies_1` / ページ内順序: 1
- caption/列: Figure 1
- 周辺文脈（EN）: Posterior summary
- 周辺文脈（JA, 自動訳）: 3 J 映画へのモデルの拡張 / 事後要約
- Workflowフェーズ: **EDA / observed data**
- 実務での読み方: モデル化前に、観測単位・外れ値・欠測・群構造・時系列性・上限/下限などを確認する。MLflowではデータ版と前処理版を固定する。
- MLflow連携: `dataset_uri, dataset_hash, preprocessing_version, n_obs, group_count`
- 参照: [公式ページ](https://avehtari.github.io/Bayesian-Workflow/movies/movies.html#fig-movies_1) / [ソース候補](https://github.com/avehtari/Bayesian-Workflow/blob/eb00fa4397314ef7d90203382542bd44c590e289/movies/movies.R)

#### `movies-movies/fig-gg-movies_1`

- 種別: `figure` / 公式ID: `fig-gg-movies_1` / ページ内順序: 2
- caption/列: Figure 2
- 周辺文脈（EN）: ggplot version
- 周辺文脈（JA, 自動訳）: 3 モデルを J ムービー / ggplot バージョンに拡張する
- Workflowフェーズ: **EDA / observed data**
- 実務での読み方: モデル化前に、観測単位・外れ値・欠測・群構造・時系列性・上限/下限などを確認する。MLflowではデータ版と前処理版を固定する。
- MLflow連携: `dataset_uri, dataset_hash, preprocessing_version, n_obs, group_count`
- 参照: [公式ページ](https://avehtari.github.io/Bayesian-Workflow/movies/movies.html#fig-gg-movies_1) / [ソース候補](https://github.com/avehtari/Bayesian-Workflow/blob/eb00fa4397314ef7d90203382542bd44c590e289/movies/movies.R)

#### `movies-movies/fig-movies_2`

- 種別: `figure` / 公式ID: `fig-movies_2` / ページ内順序: 3
- caption/列: Figure 3
- 周辺文脈（EN）: ggplot version
- 周辺文脈（JA, 自動訳）: 3 モデルを J ムービー / ggplot バージョンに拡張する
- Workflowフェーズ: **EDA / observed data**
- 実務での読み方: モデル化前に、観測単位・外れ値・欠測・群構造・時系列性・上限/下限などを確認する。MLflowではデータ版と前処理版を固定する。
- MLflow連携: `dataset_uri, dataset_hash, preprocessing_version, n_obs, group_count`
- 参照: [公式ページ](https://avehtari.github.io/Bayesian-Workflow/movies/movies.html#fig-movies_2) / [ソース候補](https://github.com/avehtari/Bayesian-Workflow/blob/eb00fa4397314ef7d90203382542bd44c590e289/movies/movies.R)

#### `movies-movies/fig-gg-movies_2`

- 種別: `figure` / 公式ID: `fig-gg-movies_2` / ページ内順序: 4
- caption/列: Figure 4
- 周辺文脈（EN）: ggplot version
- 周辺文脈（JA, 自動訳）: 3 モデルを J ムービー / ggplot バージョンに拡張する
- Workflowフェーズ: **EDA / observed data**
- 実務での読み方: モデル化前に、観測単位・外れ値・欠測・群構造・時系列性・上限/下限などを確認する。MLflowではデータ版と前処理版を固定する。
- MLflow連携: `dataset_uri, dataset_hash, preprocessing_version, n_obs, group_count`
- 参照: [公式ページ](https://avehtari.github.io/Bayesian-Workflow/movies/movies.html#fig-gg-movies_2) / [ソース候補](https://github.com/avehtari/Bayesian-Workflow/blob/eb00fa4397314ef7d90203382542bd44c590e289/movies/movies.R)

#### `movies-movies/fig-movies_3`

- 種別: `figure` / 公式ID: `fig-movies_3` / ページ内順序: 5
- caption/列: Figure 5
- 周辺文脈（EN）: Posterior summary
- 周辺文脈（JA, 自動訳）: 4.1 バランスのとれたデータ/事後サマリー
- Workflowフェーズ: **EDA / observed data**
- 実務での読み方: モデル化前に、観測単位・外れ値・欠測・群構造・時系列性・上限/下限などを確認する。MLflowではデータ版と前処理版を固定する。
- MLflow連携: `dataset_uri, dataset_hash, preprocessing_version, n_obs, group_count`
- 参照: [公式ページ](https://avehtari.github.io/Bayesian-Workflow/movies/movies.html#fig-movies_3) / [ソース候補](https://github.com/avehtari/Bayesian-Workflow/blob/eb00fa4397314ef7d90203382542bd44c590e289/movies/movies.R)

#### `movies-movies/fig-gg-movies_3`

- 種別: `figure` / 公式ID: `fig-gg-movies_3` / ページ内順序: 6
- caption/列: Figure 6
- 周辺文脈（EN）: ggplot version
- 周辺文脈（JA, 自動訳）: 4.1 バランスのとれたデータ/ggplot バージョン
- Workflowフェーズ: **EDA / observed data**
- 実務での読み方: モデル化前に、観測単位・外れ値・欠測・群構造・時系列性・上限/下限などを確認する。MLflowではデータ版と前処理版を固定する。
- MLflow連携: `dataset_uri, dataset_hash, preprocessing_version, n_obs, group_count`
- 参照: [公式ページ](https://avehtari.github.io/Bayesian-Workflow/movies/movies.html#fig-gg-movies_3) / [ソース候補](https://github.com/avehtari/Bayesian-Workflow/blob/eb00fa4397314ef7d90203382542bd44c590e289/movies/movies.R)

#### `movies-movies/fig-movies_4`

- 種別: `figure` / 公式ID: `fig-movies_4` / ページ内順序: 7
- caption/列: Figure 7
- 周辺文脈（EN）: Posterior summary
- 周辺文脈（JA, 自動訳）: 4.2 不均衡データ/事後サマリー
- Workflowフェーズ: **EDA / observed data**
- 実務での読み方: モデル化前に、観測単位・外れ値・欠測・群構造・時系列性・上限/下限などを確認する。MLflowではデータ版と前処理版を固定する。
- MLflow連携: `dataset_uri, dataset_hash, preprocessing_version, n_obs, group_count`
- 参照: [公式ページ](https://avehtari.github.io/Bayesian-Workflow/movies/movies.html#fig-movies_4) / [ソース候補](https://github.com/avehtari/Bayesian-Workflow/blob/eb00fa4397314ef7d90203382542bd44c590e289/movies/movies.R)

#### `movies-movies/fig-gg-movies_4`

- 種別: `figure` / 公式ID: `fig-gg-movies_4` / ページ内順序: 8
- caption/列: Figure 8
- 周辺文脈（EN）: ggplot version
- 周辺文脈（JA, 自動訳）: 4.2 不均衡データ / ggplot バージョン
- Workflowフェーズ: **EDA / observed data**
- 実務での読み方: モデル化前に、観測単位・外れ値・欠測・群構造・時系列性・上限/下限などを確認する。MLflowではデータ版と前処理版を固定する。
- MLflow連携: `dataset_uri, dataset_hash, preprocessing_version, n_obs, group_count`
- 参照: [公式ページ](https://avehtari.github.io/Bayesian-Workflow/movies/movies.html#fig-gg-movies_4) / [ソース候補](https://github.com/avehtari/Bayesian-Workflow/blob/eb00fa4397314ef7d90203382542bd44c590e289/movies/movies.R)

#### `movies-movies/fig-movies_5`

- 種別: `figure` / 公式ID: `fig-movies_5` / ページ内順序: 9
- caption/列: Figure 9
- 周辺文脈（EN）: ggplot version
- 周辺文脈（JA, 自動訳）: 5 単純なデータ平均化/ggplot バージョンとの比較
- Workflowフェーズ: **EDA / observed data**
- 実務での読み方: モデル化前に、観測単位・外れ値・欠測・群構造・時系列性・上限/下限などを確認する。MLflowではデータ版と前処理版を固定する。
- MLflow連携: `dataset_uri, dataset_hash, preprocessing_version, n_obs, group_count`
- 参照: [公式ページ](https://avehtari.github.io/Bayesian-Workflow/movies/movies.html#fig-movies_5) / [ソース候補](https://github.com/avehtari/Bayesian-Workflow/blob/eb00fa4397314ef7d90203382542bd44c590e289/movies/movies.R)

#### `movies-movies/fig-gg-movies_5`

- 種別: `figure` / 公式ID: `fig-gg-movies_5` / ページ内順序: 10
- caption/列: Figure 10
- 周辺文脈（EN）: ggplot version
- 周辺文脈（JA, 自動訳）: 5 単純なデータ平均化/ggplot バージョンとの比較
- Workflowフェーズ: **EDA / observed data**
- 実務での読み方: モデル化前に、観測単位・外れ値・欠測・群構造・時系列性・上限/下限などを確認する。MLflowではデータ版と前処理版を固定する。
- MLflow連携: `dataset_uri, dataset_hash, preprocessing_version, n_obs, group_count`
- 参照: [公式ページ](https://avehtari.github.io/Bayesian-Workflow/movies/movies.html#fig-gg-movies_5) / [ソース候補](https://github.com/avehtari/Bayesian-Workflow/blob/eb00fa4397314ef7d90203382542bd44c590e289/movies/movies.R)

### Prior specification for regression models: Reanalysis of a sleep study

- ページ: <https://avehtari.github.io/Bayesian-Workflow/sleep_study/sleep_study.html>
- ソース候補: <https://github.com/avehtari/Bayesian-Workflow/blob/eb00fa4397314ef7d90203382542bd44c590e289/sleep_study/sleep_study.R>

#### `sleep-study-sleep-study/fig-sleepstudy-data`

- 種別: `figure` / 公式ID: `fig-sleepstudy-data` / ページ内順序: 1
- caption/列: Figure 1
- 周辺文脈（EN）: Plot the data
- 周辺文脈（JA, 自動訳）: 2 睡眠研究データ / データをプロットする
- Workflowフェーズ: **EDA / observed data**
- 実務での読み方: モデル化前に、観測単位・外れ値・欠測・群構造・時系列性・上限/下限などを確認する。MLflowではデータ版と前処理版を固定する。
- MLflow連携: `dataset_uri, dataset_hash, preprocessing_version, n_obs, group_count`
- 参照: [公式ページ](https://avehtari.github.io/Bayesian-Workflow/sleep_study/sleep_study.html#fig-sleepstudy-data) / [ソース候補](https://github.com/avehtari/Bayesian-Workflow/blob/eb00fa4397314ef7d90203382542bd44c590e289/sleep_study/sleep_study.R)

#### `sleep-study-sleep-study/fig-sleepstudy-conditional_effects-fit_lin_base`

- 種別: `figure` / 公式ID: `fig-sleepstudy-conditional_effects-fit_lin_base` / ページ内順序: 2
- caption/列: Figure 2
- 周辺文脈（EN）: Posterior conditional effects
- 周辺文脈（JA, 自動訳）: 3 単純な線形モデル / 事後条件効果
- Workflowフェーズ: **Posterior summary / effect interpretation**
- 実務での読み方: 推定効果・不確実性・派生量を意思決定に接続する。平均だけでなく区間・分布・実務閾値超過確率を残す。
- MLflow連携: `posterior_draws_uri, model_code_hash, ci_width, decision_threshold_prob`
- 参照: [公式ページ](https://avehtari.github.io/Bayesian-Workflow/sleep_study/sleep_study.html#fig-sleepstudy-conditional_effects-fit_lin_base) / [ソース候補](https://github.com/avehtari/Bayesian-Workflow/blob/eb00fa4397314ef7d90203382542bd44c590e289/sleep_study/sleep_study.R)

#### `sleep-study-sleep-study/fig-sleepstudy-pp_check-fit1_prior`

- 種別: `figure` / 公式ID: `fig-sleepstudy-pp_check-fit1_prior` / ページ内順序: 3
- caption/列: Figure 3
- 周辺文脈（EN）: Prior predictive checking
- 周辺文脈（JA, 自動訳）: 4 単純な線形モデル (中心予測子) / 事前予測チェック
- Workflowフェーズ: **Prior / prior predictive**
- 実務での読み方: 事前分布が現実的なデータ範囲を生成するかを見る。現場導入前に、あり得ない予測の比率をゲート化する。
- MLflow連携: `prior_spec_id, prior_predictive_seed, simulated_n, implausible_rate`
- 参照: [公式ページ](https://avehtari.github.io/Bayesian-Workflow/sleep_study/sleep_study.html#fig-sleepstudy-pp_check-fit1_prior) / [ソース候補](https://github.com/avehtari/Bayesian-Workflow/blob/eb00fa4397314ef7d90203382542bd44c590e289/sleep_study/sleep_study.R)

#### `sleep-study-sleep-study/fig-sleepstudy-conditional_effects-fit1`

- 種別: `figure` / 公式ID: `fig-sleepstudy-conditional_effects-fit1` / ページ内順序: 4
- caption/列: Figure 4
- 周辺文脈（EN）: Posterior conditional effects
- 周辺文脈（JA, 自動訳）: 4 単純な線形モデル (中心予測子) / 事後条件効果
- Workflowフェーズ: **Posterior summary / effect interpretation**
- 実務での読み方: 推定効果・不確実性・派生量を意思決定に接続する。平均だけでなく区間・分布・実務閾値超過確率を残す。
- MLflow連携: `posterior_draws_uri, model_code_hash, ci_width, decision_threshold_prob`
- 参照: [公式ページ](https://avehtari.github.io/Bayesian-Workflow/sleep_study/sleep_study.html#fig-sleepstudy-conditional_effects-fit1) / [ソース候補](https://github.com/avehtari/Bayesian-Workflow/blob/eb00fa4397314ef7d90203382542bd44c590e289/sleep_study/sleep_study.R)

#### `sleep-study-sleep-study/fig-sleepstudy-pp_check-fit1`

- 種別: `figure` / 公式ID: `fig-sleepstudy-pp_check-fit1` / ページ内順序: 5
- caption/列: Figure 5
- 周辺文脈（EN）: Posterior predictive checking
- 周辺文脈（JA, 自動訳）: 4 単純な線形モデル (中心予測子) / 事後予測チェック
- Workflowフェーズ: **Posterior predictive checking / calibration**
- 実務での読み方: モデルが再現すべき特徴を外していないか確認する。PPC統計量と図をartifact化し、モデル改善の根拠にする。
- MLflow連携: `ppc_stat_*, loo_pit_ecdf_maxdev, calibration_error, replicated_seed`
- 参照: [公式ページ](https://avehtari.github.io/Bayesian-Workflow/sleep_study/sleep_study.html#fig-sleepstudy-pp_check-fit1) / [ソース候補](https://github.com/avehtari/Bayesian-Workflow/blob/eb00fa4397314ef7d90203382542bd44c590e289/sleep_study/sleep_study.R)

#### `sleep-study-sleep-study/fig-sleepstudy-priorsense-fit1`

- 種別: `figure` / 公式ID: `fig-sleepstudy-priorsense-fit1` / ページ内順序: 6
- caption/列: Figure 6
- 周辺文脈（EN）: Prior sensitivity analysis
- 周辺文脈（JA, 自動訳）: 4 単純な線形モデル (中心予測子) / 事前感度分析
- Workflowフェーズ: **MCMC / computation diagnostics**
- 実務での読み方: 推論結果を解釈する前に、R-hat、ESS、divergence、treedepth、BFMI、trace/pairsを確認する。悪いrunは比較表から除外せず失敗として記録する。
- MLflow連携: `rhat_max, ess_bulk_min, ess_tail_min, divergences, treedepth_hits, bfmi_min`
- 参照: [公式ページ](https://avehtari.github.io/Bayesian-Workflow/sleep_study/sleep_study.html#fig-sleepstudy-priorsense-fit1) / [ソース候補](https://github.com/avehtari/Bayesian-Workflow/blob/eb00fa4397314ef7d90203382542bd44c590e289/sleep_study/sleep_study.R)

#### `sleep-study-sleep-study/fig-sleepstudy-conditional_effects-fit2`

- 種別: `figure` / 公式ID: `fig-sleepstudy-conditional_effects-fit2` / ページ内順序: 7
- caption/列: Figure 7
- 周辺文脈（EN）: Posterior conditional effects
- 周辺文脈（JA, 自動訳）: 5 単純な線形モデル (有益な事前分布) / 事後条件効果
- Workflowフェーズ: **Posterior summary / effect interpretation**
- 実務での読み方: 推定効果・不確実性・派生量を意思決定に接続する。平均だけでなく区間・分布・実務閾値超過確率を残す。
- MLflow連携: `posterior_draws_uri, model_code_hash, ci_width, decision_threshold_prob`
- 参照: [公式ページ](https://avehtari.github.io/Bayesian-Workflow/sleep_study/sleep_study.html#fig-sleepstudy-conditional_effects-fit2) / [ソース候補](https://github.com/avehtari/Bayesian-Workflow/blob/eb00fa4397314ef7d90203382542bd44c590e289/sleep_study/sleep_study.R)

#### `sleep-study-sleep-study/fig-sleepstudy-priorsense-fit2`

- 種別: `figure` / 公式ID: `fig-sleepstudy-priorsense-fit2` / ページ内順序: 8
- caption/列: Figure 8
- 周辺文脈（EN）: Prior sensitivity analysis
- 周辺文脈（JA, 自動訳）: 5 単純な線形モデル (有益な事前確率) / 事前感度分析
- Workflowフェーズ: **MCMC / computation diagnostics**
- 実務での読み方: 推論結果を解釈する前に、R-hat、ESS、divergence、treedepth、BFMI、trace/pairsを確認する。悪いrunは比較表から除外せず失敗として記録する。
- MLflow連携: `rhat_max, ess_bulk_min, ess_tail_min, divergences, treedepth_hits, bfmi_min`
- 参照: [公式ページ](https://avehtari.github.io/Bayesian-Workflow/sleep_study/sleep_study.html#fig-sleepstudy-priorsense-fit2) / [ソース候補](https://github.com/avehtari/Bayesian-Workflow/blob/eb00fa4397314ef7d90203382542bd44c590e289/sleep_study/sleep_study.R)

#### `sleep-study-sleep-study/fig-sleepstudy-conditional_effects-fit2b`

- 種別: `figure` / 公式ID: `fig-sleepstudy-conditional_effects-fit2b` / ページ内順序: 9
- caption/列: Figure 9
- 周辺文脈（EN）: Posterior conditional effects
- 周辺文脈（JA, 自動訳）: 6 単純な線形モデル (ファットテールを持つ有益な事前分布) / 事後条件効果
- Workflowフェーズ: **Posterior summary / effect interpretation**
- 実務での読み方: 推定効果・不確実性・派生量を意思決定に接続する。平均だけでなく区間・分布・実務閾値超過確率を残す。
- MLflow連携: `posterior_draws_uri, model_code_hash, ci_width, decision_threshold_prob`
- 参照: [公式ページ](https://avehtari.github.io/Bayesian-Workflow/sleep_study/sleep_study.html#fig-sleepstudy-conditional_effects-fit2b) / [ソース候補](https://github.com/avehtari/Bayesian-Workflow/blob/eb00fa4397314ef7d90203382542bd44c590e289/sleep_study/sleep_study.R)

#### `sleep-study-sleep-study/fig-sleepstudy-priorsense-fit2b`

- 種別: `figure` / 公式ID: `fig-sleepstudy-priorsense-fit2b` / ページ内順序: 10
- caption/列: Figure 10
- 周辺文脈（EN）: Prior sensitivity analysis
- 周辺文脈（JA, 自動訳）: 6 単純な線形モデル (ファットテールを備えた有益な事前確率) / 事前感度分析
- Workflowフェーズ: **MCMC / computation diagnostics**
- 実務での読み方: 推論結果を解釈する前に、R-hat、ESS、divergence、treedepth、BFMI、trace/pairsを確認する。悪いrunは比較表から除外せず失敗として記録する。
- MLflow連携: `rhat_max, ess_bulk_min, ess_tail_min, divergences, treedepth_hits, bfmi_min`
- 参照: [公式ページ](https://avehtari.github.io/Bayesian-Workflow/sleep_study/sleep_study.html#fig-sleepstudy-priorsense-fit2b) / [ソース候補](https://github.com/avehtari/Bayesian-Workflow/blob/eb00fa4397314ef7d90203382542bd44c590e289/sleep_study/sleep_study.R)

#### `sleep-study-sleep-study/fig-compare-normal-student-density`

- 種別: `figure` / 公式ID: `fig-compare-normal-student-density` / ページ内順序: 11
- caption/列: Figure 11
- 周辺文脈（EN）: Illustrate difference between normal and Student-t prior:
- 周辺文脈（JA, 自動訳）: 6 単純な線形モデル (ファットテールを持つ有益な事前分布) / 通常の事前分布と Student-t 事前分布の違いを示します。
- Workflowフェーズ: **MCMC / computation diagnostics**
- 実務での読み方: 推論結果を解釈する前に、R-hat、ESS、divergence、treedepth、BFMI、trace/pairsを確認する。悪いrunは比較表から除外せず失敗として記録する。
- MLflow連携: `rhat_max, ess_bulk_min, ess_tail_min, divergences, treedepth_hits, bfmi_min`
- 参照: [公式ページ](https://avehtari.github.io/Bayesian-Workflow/sleep_study/sleep_study.html#fig-compare-normal-student-density) / [ソース候補](https://github.com/avehtari/Bayesian-Workflow/blob/eb00fa4397314ef7d90203382542bd44c590e289/sleep_study/sleep_study.R)

#### `sleep-study-sleep-study/fig-sleepstudy-conditional_effects-1-fit3`

- 種別: `figure` / 公式ID: `fig-sleepstudy-conditional_effects-1-fit3` / ページ内順序: 12
- caption/列: Figure 12
- 周辺文脈（EN）: Posterior conditional effects
- 周辺文脈（JA, 自動訳）: 7 線形可変切片モデル / 事後条件効果
- Workflowフェーズ: **Posterior summary / effect interpretation**
- 実務での読み方: 推定効果・不確実性・派生量を意思決定に接続する。平均だけでなく区間・分布・実務閾値超過確率を残す。
- MLflow連携: `posterior_draws_uri, model_code_hash, ci_width, decision_threshold_prob`
- 参照: [公式ページ](https://avehtari.github.io/Bayesian-Workflow/sleep_study/sleep_study.html#fig-sleepstudy-conditional_effects-1-fit3) / [ソース候補](https://github.com/avehtari/Bayesian-Workflow/blob/eb00fa4397314ef7d90203382542bd44c590e289/sleep_study/sleep_study.R)

#### `sleep-study-sleep-study/fig-sleepstudy-conditional_effects-2-fit3`

- 種別: `figure` / 公式ID: `fig-sleepstudy-conditional_effects-2-fit3` / ページ内順序: 13
- caption/列: Figure 13
- 周辺文脈（EN）: Posterior conditional effects
- 周辺文脈（JA, 自動訳）: 7 線形可変切片モデル / 事後条件効果
- Workflowフェーズ: **Posterior summary / effect interpretation**
- 実務での読み方: 推定効果・不確実性・派生量を意思決定に接続する。平均だけでなく区間・分布・実務閾値超過確率を残す。
- MLflow連携: `posterior_draws_uri, model_code_hash, ci_width, decision_threshold_prob`
- 参照: [公式ページ](https://avehtari.github.io/Bayesian-Workflow/sleep_study/sleep_study.html#fig-sleepstudy-conditional_effects-2-fit3) / [ソース候補](https://github.com/avehtari/Bayesian-Workflow/blob/eb00fa4397314ef7d90203382542bd44c590e289/sleep_study/sleep_study.R)

#### `sleep-study-sleep-study/fig-sleepstudy-conditional_effects-1-fit4`

- 種別: `figure` / 公式ID: `fig-sleepstudy-conditional_effects-1-fit4` / ページ内順序: 14
- caption/列: Figure 14
- 周辺文脈（EN）: Posterior conditional effects
- 周辺文脈（JA, 自動訳）: 8 線形変化切片および傾きモデル / 事後条件効果
- Workflowフェーズ: **Posterior summary / effect interpretation**
- 実務での読み方: 推定効果・不確実性・派生量を意思決定に接続する。平均だけでなく区間・分布・実務閾値超過確率を残す。
- MLflow連携: `posterior_draws_uri, model_code_hash, ci_width, decision_threshold_prob`
- 参照: [公式ページ](https://avehtari.github.io/Bayesian-Workflow/sleep_study/sleep_study.html#fig-sleepstudy-conditional_effects-1-fit4) / [ソース候補](https://github.com/avehtari/Bayesian-Workflow/blob/eb00fa4397314ef7d90203382542bd44c590e289/sleep_study/sleep_study.R)

#### `sleep-study-sleep-study/fig-sleepstudy-pp_check-fit4`

- 種別: `figure` / 公式ID: `fig-sleepstudy-pp_check-fit4` / ページ内順序: 15
- caption/列: Figure 15
- 周辺文脈（EN）: Posterior predictive checking
- 周辺文脈（JA, 自動訳）: 8 線形変化切片および傾きモデル / 事後予測チェック
- Workflowフェーズ: **Posterior predictive checking / calibration**
- 実務での読み方: モデルが再現すべき特徴を外していないか確認する。PPC統計量と図をartifact化し、モデル改善の根拠にする。
- MLflow連携: `ppc_stat_*, loo_pit_ecdf_maxdev, calibration_error, replicated_seed`
- 参照: [公式ページ](https://avehtari.github.io/Bayesian-Workflow/sleep_study/sleep_study.html#fig-sleepstudy-pp_check-fit4) / [ソース候補](https://github.com/avehtari/Bayesian-Workflow/blob/eb00fa4397314ef7d90203382542bd44c590e289/sleep_study/sleep_study.R)

#### `sleep-study-sleep-study/fig-sleepstudy-conditional_effects-2-fit4`

- 種別: `figure` / 公式ID: `fig-sleepstudy-conditional_effects-2-fit4` / ページ内順序: 16
- caption/列: Figure 16
- 周辺文脈（EN）: Posterior conditional effects
- 周辺文脈（JA, 自動訳）: 8 線形変化切片および傾きモデル / 事後条件効果
- Workflowフェーズ: **Posterior summary / effect interpretation**
- 実務での読み方: 推定効果・不確実性・派生量を意思決定に接続する。平均だけでなく区間・分布・実務閾値超過確率を残す。
- MLflow連携: `posterior_draws_uri, model_code_hash, ci_width, decision_threshold_prob`
- 参照: [公式ページ](https://avehtari.github.io/Bayesian-Workflow/sleep_study/sleep_study.html#fig-sleepstudy-conditional_effects-2-fit4) / [ソース候補](https://github.com/avehtari/Bayesian-Workflow/blob/eb00fa4397314ef7d90203382542bd44c590e289/sleep_study/sleep_study.R)

#### `sleep-study-sleep-study/fig-sleepstudy-LKJ1`

- 種別: `figure` / 公式ID: `fig-sleepstudy-LKJ1` / ページ内順序: 17
- caption/列: Figure 17
- 周辺文脈（EN）: Illustrate the marginal LKJ(1) prior for different dimensions.
- 周辺文脈（JA, 自動訳）: 8 線形に変化する切片と傾きのモデル / さまざまな次元に対する事前の限界 LKJ(1) を示します。
- Workflowフェーズ: **MCMC / computation diagnostics**
- 実務での読み方: 推論結果を解釈する前に、R-hat、ESS、divergence、treedepth、BFMI、trace/pairsを確認する。悪いrunは比較表から除外せず失敗として記録する。
- MLflow連携: `rhat_max, ess_bulk_min, ess_tail_min, divergences, treedepth_hits, bfmi_min`
- 参照: [公式ページ](https://avehtari.github.io/Bayesian-Workflow/sleep_study/sleep_study.html#fig-sleepstudy-LKJ1) / [ソース候補](https://github.com/avehtari/Bayesian-Workflow/blob/eb00fa4397314ef7d90203382542bd44c590e289/sleep_study/sleep_study.R)

#### `sleep-study-sleep-study/fig-sleepstudy-pp_check-fit_ln1_prior`

- 種別: `figure` / 公式ID: `fig-sleepstudy-pp_check-fit_ln1_prior` / ページ内順序: 18
- caption/列: Figure 18
- 周辺文脈（EN）: Prior predictive checking
- 周辺文脈（JA, 自動訳）: 8.1 対数線形事前限定モデル / 事前予測チェック
- Workflowフェーズ: **Prior / prior predictive**
- 実務での読み方: 事前分布が現実的なデータ範囲を生成するかを見る。現場導入前に、あり得ない予測の比率をゲート化する。
- MLflow連携: `prior_spec_id, prior_predictive_seed, simulated_n, implausible_rate`
- 参照: [公式ページ](https://avehtari.github.io/Bayesian-Workflow/sleep_study/sleep_study.html#fig-sleepstudy-pp_check-fit_ln1_prior) / [ソース候補](https://github.com/avehtari/Bayesian-Workflow/blob/eb00fa4397314ef7d90203382542bd44c590e289/sleep_study/sleep_study.R)

#### `sleep-study-sleep-study/fig-sleepstudy-pp_check-fit_ln2_prior`

- 種別: `figure` / 公式ID: `fig-sleepstudy-pp_check-fit_ln2_prior` / ページ内順序: 19
- caption/列: Figure 19
- 周辺文脈（EN）: Prior predictive checking
- 周辺文脈（JA, 自動訳）: 8.1 対数線形事前限定モデル / 事前予測チェック
- Workflowフェーズ: **Prior / prior predictive**
- 実務での読み方: 事前分布が現実的なデータ範囲を生成するかを見る。現場導入前に、あり得ない予測の比率をゲート化する。
- MLflow連携: `prior_spec_id, prior_predictive_seed, simulated_n, implausible_rate`
- 参照: [公式ページ](https://avehtari.github.io/Bayesian-Workflow/sleep_study/sleep_study.html#fig-sleepstudy-pp_check-fit_ln2_prior) / [ソース候補](https://github.com/avehtari/Bayesian-Workflow/blob/eb00fa4397314ef7d90203382542bd44c590e289/sleep_study/sleep_study.R)

#### `sleep-study-sleep-study/fig-sleepstudy-pp_check-fit_ln1_ln2_prior`

- 種別: `figure` / 公式ID: `fig-sleepstudy-pp_check-fit_ln1_ln2_prior` / ページ内順序: 20
- caption/列: Figure 20
- 周辺文脈（EN）: Prior predictive checking comparing priors ln1 and ln2
- 周辺文脈（JA, 自動訳）: 8.1 対数線形事前のみモデル / 事前確率 ln1 と ln2 を比較する事前予測チェック
- Workflowフェーズ: **Prior / prior predictive**
- 実務での読み方: 事前分布が現実的なデータ範囲を生成するかを見る。現場導入前に、あり得ない予測の比率をゲート化する。
- MLflow連携: `prior_spec_id, prior_predictive_seed, simulated_n, implausible_rate`
- 参照: [公式ページ](https://avehtari.github.io/Bayesian-Workflow/sleep_study/sleep_study.html#fig-sleepstudy-pp_check-fit_ln1_ln2_prior) / [ソース候補](https://github.com/avehtari/Bayesian-Workflow/blob/eb00fa4397314ef7d90203382542bd44c590e289/sleep_study/sleep_study.R)

#### `sleep-study-sleep-study/fig-sleepstudy-conditional_effects-1-ln2`

- 種別: `figure` / 公式ID: `fig-sleepstudy-conditional_effects-1-ln2` / ページ内順序: 21
- caption/列: Figure 21
- 周辺文脈（EN）: Posterior conditional effects
- 周辺文脈（JA, 自動訳）: 8.1 対数線形事前限定モデル / 事後条件効果
- Workflowフェーズ: **Prior / prior predictive**
- 実務での読み方: 事前分布が現実的なデータ範囲を生成するかを見る。現場導入前に、あり得ない予測の比率をゲート化する。
- MLflow連携: `prior_spec_id, prior_predictive_seed, simulated_n, implausible_rate`
- 参照: [公式ページ](https://avehtari.github.io/Bayesian-Workflow/sleep_study/sleep_study.html#fig-sleepstudy-conditional_effects-1-ln2) / [ソース候補](https://github.com/avehtari/Bayesian-Workflow/blob/eb00fa4397314ef7d90203382542bd44c590e289/sleep_study/sleep_study.R)

#### `sleep-study-sleep-study/fig-sleepstudy-priorsense-fit_ln2`

- 種別: `figure` / 公式ID: `fig-sleepstudy-priorsense-fit_ln2` / ページ内順序: 22
- caption/列: Figure 22
- 周辺文脈（EN）: Prior sensitivity analysis
- 周辺文脈（JA, 自動訳）: 8.1 Log-Linear事前専用モデル/事前感度分析
- Workflowフェーズ: **Prior / prior predictive**
- 実務での読み方: 事前分布が現実的なデータ範囲を生成するかを見る。現場導入前に、あり得ない予測の比率をゲート化する。
- MLflow連携: `prior_spec_id, prior_predictive_seed, simulated_n, implausible_rate`
- 参照: [公式ページ](https://avehtari.github.io/Bayesian-Workflow/sleep_study/sleep_study.html#fig-sleepstudy-priorsense-fit_ln2) / [ソース候補](https://github.com/avehtari/Bayesian-Workflow/blob/eb00fa4397314ef7d90203382542bd44c590e289/sleep_study/sleep_study.R)

#### `sleep-study-sleep-study/fig-sleepstudy-conditional_effects-fit5`

- 種別: `figure` / 公式ID: `fig-sleepstudy-conditional_effects-fit5` / ページ内順序: 23
- caption/列: Figure 23
- 周辺文脈（EN）: Posterior conditional effects
- 周辺文脈（JA, 自動訳）: 9 対数線形変化切片および傾きモデル / 事後条件効果
- Workflowフェーズ: **Posterior summary / effect interpretation**
- 実務での読み方: 推定効果・不確実性・派生量を意思決定に接続する。平均だけでなく区間・分布・実務閾値超過確率を残す。
- MLflow連携: `posterior_draws_uri, model_code_hash, ci_width, decision_threshold_prob`
- 参照: [公式ページ](https://avehtari.github.io/Bayesian-Workflow/sleep_study/sleep_study.html#fig-sleepstudy-conditional_effects-fit5) / [ソース候補](https://github.com/avehtari/Bayesian-Workflow/blob/eb00fa4397314ef7d90203382542bd44c590e289/sleep_study/sleep_study.R)

#### `sleep-study-sleep-study/fig-sleepstudy-pp_check-fit5`

- 種別: `figure` / 公式ID: `fig-sleepstudy-pp_check-fit5` / ページ内順序: 24
- caption/列: Figure 24
- 周辺文脈（EN）: Posterior predictive checking
- 周辺文脈（JA, 自動訳）: 9 対数線形変化切片および傾きモデル / 事後予測検査
- Workflowフェーズ: **Posterior predictive checking / calibration**
- 実務での読み方: モデルが再現すべき特徴を外していないか確認する。PPC統計量と図をartifact化し、モデル改善の根拠にする。
- MLflow連携: `ppc_stat_*, loo_pit_ecdf_maxdev, calibration_error, replicated_seed`
- 参照: [公式ページ](https://avehtari.github.io/Bayesian-Workflow/sleep_study/sleep_study.html#fig-sleepstudy-pp_check-fit5) / [ソース候補](https://github.com/avehtari/Bayesian-Workflow/blob/eb00fa4397314ef7d90203382542bd44c590e289/sleep_study/sleep_study.R)

#### `sleep-study-sleep-study/fig-sleepstudy-pp_check-fit4-fit5`

- 種別: `figure` / 公式ID: `fig-sleepstudy-pp_check-fit4-fit5` / ページ内順序: 25
- caption/列: Figure 25
- 周辺文脈（EN）: Posterior predictive checking comparing fit4 and fit5
- 周辺文脈（JA, 自動訳）: 9 対数線形の変化する切片と傾きモデル / fit4 と fit5 を比較する事後予測チェック
- Workflowフェーズ: **Posterior predictive checking / calibration**
- 実務での読み方: モデルが再現すべき特徴を外していないか確認する。PPC統計量と図をartifact化し、モデル改善の根拠にする。
- MLflow連携: `ppc_stat_*, loo_pit_ecdf_maxdev, calibration_error, replicated_seed`
- 参照: [公式ページ](https://avehtari.github.io/Bayesian-Workflow/sleep_study/sleep_study.html#fig-sleepstudy-pp_check-fit4-fit5) / [ソース候補](https://github.com/avehtari/Bayesian-Workflow/blob/eb00fa4397314ef7d90203382542bd44c590e289/sleep_study/sleep_study.R)

#### `sleep-study-sleep-study/fig-sleepstudy-conditional_effects-plus-fit5`

- 種別: `figure` / 公式ID: `fig-sleepstudy-conditional_effects-plus-fit5` / ページ内順序: 26
- caption/列: Figure 26
- 周辺文脈（EN）: Posterior conditional effects
- 周辺文脈（JA, 自動訳）: 9 対数線形変化切片および傾きモデル / 事後条件効果
- Workflowフェーズ: **Posterior summary / effect interpretation**
- 実務での読み方: 推定効果・不確実性・派生量を意思決定に接続する。平均だけでなく区間・分布・実務閾値超過確率を残す。
- MLflow連携: `posterior_draws_uri, model_code_hash, ci_width, decision_threshold_prob`
- 参照: [公式ページ](https://avehtari.github.io/Bayesian-Workflow/sleep_study/sleep_study.html#fig-sleepstudy-conditional_effects-plus-fit5) / [ソース候補](https://github.com/avehtari/Bayesian-Workflow/blob/eb00fa4397314ef7d90203382542bd44c590e289/sleep_study/sleep_study.R)

#### `sleep-study-sleep-study/fig-sleepstudy-priorsense-fit5`

- 種別: `figure` / 公式ID: `fig-sleepstudy-priorsense-fit5` / ページ内順序: 27
- caption/列: Figure 27
- 周辺文脈（EN）: Prior sensitivity analysis
- 周辺文脈（JA, 自動訳）: 9 対数線形変化切片および傾きモデル / 事前感度分析
- Workflowフェーズ: **MCMC / computation diagnostics**
- 実務での読み方: 推論結果を解釈する前に、R-hat、ESS、divergence、treedepth、BFMI、trace/pairsを確認する。悪いrunは比較表から除外せず失敗として記録する。
- MLflow連携: `rhat_max, ess_bulk_min, ess_tail_min, divergences, treedepth_hits, bfmi_min`
- 参照: [公式ページ](https://avehtari.github.io/Bayesian-Workflow/sleep_study/sleep_study.html#fig-sleepstudy-priorsense-fit5) / [ソース候補](https://github.com/avehtari/Bayesian-Workflow/blob/eb00fa4397314ef7d90203382542bd44c590e289/sleep_study/sleep_study.R)

#### `sleep-study-sleep-study/fig-sleepstudy-conditional_effects-fit6`

- 種別: `figure` / 公式ID: `fig-sleepstudy-conditional_effects-fit6` / ページ内順序: 28
- caption/列: Figure 28
- 周辺文脈（EN）: Posterior conditional effects
- 周辺文脈（JA, 自動訳）: 10 対数線形分布マルチレベル モデル / 事後条件効果
- Workflowフェーズ: **Posterior summary / effect interpretation**
- 実務での読み方: 推定効果・不確実性・派生量を意思決定に接続する。平均だけでなく区間・分布・実務閾値超過確率を残す。
- MLflow連携: `posterior_draws_uri, model_code_hash, ci_width, decision_threshold_prob`
- 参照: [公式ページ](https://avehtari.github.io/Bayesian-Workflow/sleep_study/sleep_study.html#fig-sleepstudy-conditional_effects-fit6) / [ソース候補](https://github.com/avehtari/Bayesian-Workflow/blob/eb00fa4397314ef7d90203382542bd44c590e289/sleep_study/sleep_study.R)

#### `sleep-study-sleep-study/fig-sleepstudy-conditional_effects-fit7`

- 種別: `figure` / 公式ID: `fig-sleepstudy-conditional_effects-fit7` / ページ内順序: 29
- caption/列: Figure 29
- 周辺文脈（EN）: Posterior conditional effects
- 周辺文脈（JA, 自動訳）: 11 エクスガウス分布マルチレベルモデル / 事後条件効果
- Workflowフェーズ: **Posterior summary / effect interpretation**
- 実務での読み方: 推定効果・不確実性・派生量を意思決定に接続する。平均だけでなく区間・分布・実務閾値超過確率を残す。
- MLflow連携: `posterior_draws_uri, model_code_hash, ci_width, decision_threshold_prob`
- 参照: [公式ページ](https://avehtari.github.io/Bayesian-Workflow/sleep_study/sleep_study.html#fig-sleepstudy-conditional_effects-fit7) / [ソース候補](https://github.com/avehtari/Bayesian-Workflow/blob/eb00fa4397314ef7d90203382542bd44c590e289/sleep_study/sleep_study.R)

#### `sleep-study-sleep-study/fig-sleepstudy-conditional_effects-fit8`

- 種別: `figure` / 公式ID: `fig-sleepstudy-conditional_effects-fit8` / ページ内順序: 30
- caption/列: Figure 30
- 周辺文脈（EN）: Posterior conditional effects
- 周辺文脈（JA, 自動訳）: 12 エクスガウス分布マルチレベル モデル (デフォルトの事前分布) / 事後条件効果
- Workflowフェーズ: **Posterior summary / effect interpretation**
- 実務での読み方: 推定効果・不確実性・派生量を意思決定に接続する。平均だけでなく区間・分布・実務閾値超過確率を残す。
- MLflow連携: `posterior_draws_uri, model_code_hash, ci_width, decision_threshold_prob`
- 参照: [公式ページ](https://avehtari.github.io/Bayesian-Workflow/sleep_study/sleep_study.html#fig-sleepstudy-conditional_effects-fit8) / [ソース候補](https://github.com/avehtari/Bayesian-Workflow/blob/eb00fa4397314ef7d90203382542bd44c590e289/sleep_study/sleep_study.R)

#### `sleep-study-sleep-study/fig-sleepstudy-conditional_effects-fit9`

- 種別: `figure` / 公式ID: `fig-sleepstudy-conditional_effects-fit9` / ページ内順序: 31
- caption/列: Figure 31
- 周辺文脈（EN）: Posterior conditional effects
- 周辺文脈（JA, 自動訳）: 13 エクスガウス分布マルチレベルモデル (フラット事前分布) / 事後条件効果
- Workflowフェーズ: **Posterior summary / effect interpretation**
- 実務での読み方: 推定効果・不確実性・派生量を意思決定に接続する。平均だけでなく区間・分布・実務閾値超過確率を残す。
- MLflow連携: `posterior_draws_uri, model_code_hash, ci_width, decision_threshold_prob`
- 参照: [公式ページ](https://avehtari.github.io/Bayesian-Workflow/sleep_study/sleep_study.html#fig-sleepstudy-conditional_effects-fit9) / [ソース候補](https://github.com/avehtari/Bayesian-Workflow/blob/eb00fa4397314ef7d90203382542bd44c590e289/sleep_study/sleep_study.R)

#### `sleep-study-sleep-study/fig-sleepstudy-ppc-loo_intervals-fit4`

- 種別: `figure` / 公式ID: `fig-sleepstudy-ppc-loo_intervals-fit4` / ページ内順序: 32
- caption/列: Figure 32
- 周辺文脈（EN）: Posterior predictive checking of fit4 using LOO predictive intervals
- 周辺文脈（JA, 自動訳）: 14 モデルの比較と検査 / LOO 予測区間を使用した Fit4 の事後予測検査
- Workflowフェーズ: **Posterior predictive checking / calibration**
- 実務での読み方: モデルが再現すべき特徴を外していないか確認する。PPC統計量と図をartifact化し、モデル改善の根拠にする。
- MLflow連携: `ppc_stat_*, loo_pit_ecdf_maxdev, calibration_error, replicated_seed`
- 参照: [公式ページ](https://avehtari.github.io/Bayesian-Workflow/sleep_study/sleep_study.html#fig-sleepstudy-ppc-loo_intervals-fit4) / [ソース候補](https://github.com/avehtari/Bayesian-Workflow/blob/eb00fa4397314ef7d90203382542bd44c590e289/sleep_study/sleep_study.R)

#### `sleep-study-sleep-study/fig-sleepstudy-ppc-loo_intervals-fit4t`

- 種別: `figure` / 公式ID: `fig-sleepstudy-ppc-loo_intervals-fit4t` / ページ内順序: 33
- caption/列: Figure 33
- 周辺文脈（EN）: Posterior predictive checking of fit4t using LOO predictive intervals
- 周辺文脈（JA, 自動訳）: 14 モデルの比較と検査 / LOO 予測区間を使用した Fit4t の事後予測検査
- Workflowフェーズ: **Posterior predictive checking / calibration**
- 実務での読み方: モデルが再現すべき特徴を外していないか確認する。PPC統計量と図をartifact化し、モデル改善の根拠にする。
- MLflow連携: `ppc_stat_*, loo_pit_ecdf_maxdev, calibration_error, replicated_seed`
- 参照: [公式ページ](https://avehtari.github.io/Bayesian-Workflow/sleep_study/sleep_study.html#fig-sleepstudy-ppc-loo_intervals-fit4t) / [ソース候補](https://github.com/avehtari/Bayesian-Workflow/blob/eb00fa4397314ef7d90203382542bd44c590e289/sleep_study/sleep_study.R)

#### `sleep-study-sleep-study/fig-sleepstudy-ppc-loo_pit-fit4-fit4t`

- 種別: `figure` / 公式ID: `fig-sleepstudy-ppc-loo_pit-fit4-fit4t` / ページ内順序: 34
- caption/列: Figure 34
- 周辺文脈（EN）: The LOO predictive intervals look better now.
- 周辺文脈（JA, 自動訳）: 14 モデルの比較とチェック / LOO 予測間隔が改善されました。
- Workflowフェーズ: **Posterior predictive checking / calibration**
- 実務での読み方: モデルが再現すべき特徴を外していないか確認する。PPC統計量と図をartifact化し、モデル改善の根拠にする。
- MLflow連携: `ppc_stat_*, loo_pit_ecdf_maxdev, calibration_error, replicated_seed`
- 参照: [公式ページ](https://avehtari.github.io/Bayesian-Workflow/sleep_study/sleep_study.html#fig-sleepstudy-ppc-loo_pit-fit4-fit4t) / [ソース候補](https://github.com/avehtari/Bayesian-Workflow/blob/eb00fa4397314ef7d90203382542bd44c590e289/sleep_study/sleep_study.R)

### Predictive model checking and comparison: Clinical trial

- ページ: <https://avehtari.github.io/Bayesian-Workflow/nabiximols/nabiximols.html>
- ソース候補: <https://github.com/avehtari/Bayesian-Workflow/blob/eb00fa4397314ef7d90203382542bd44c590e289/nabiximols/nabiximols.R>

#### `nabiximols-nabiximols/fig-data`

- 種別: `figure` / 公式ID: `fig-data` / ページ内順序: 1
- caption/列: Figure 1
- 周辺文脈（EN）: It’s good to visualize the data distribution. There is a clear change in the distribution going from week 0 to later weeks.
- 周辺文脈（JA, 自動訳）: 2 データ / データの分布を可視化するとよい。第 0 週からその後の週にかけて、分布に明らかな変化が見られます。
- Workflowフェーズ: **EDA / observed data**
- 実務での読み方: モデル化前に、観測単位・外れ値・欠測・群構造・時系列性・上限/下限などを確認する。MLflowではデータ版と前処理版を固定する。
- MLflow連携: `dataset_uri, dataset_hash, preprocessing_version, n_obs, group_count`
- 参照: [公式ページ](https://avehtari.github.io/Bayesian-Workflow/nabiximols/nabiximols.html#fig-data) / [ソース候補](https://github.com/avehtari/Bayesian-Workflow/blob/eb00fa4397314ef7d90203382542bd44c590e289/nabiximols/nabiximols.R)

#### `nabiximols-nabiximols/figure-002`

- 種別: `figure` / 公式ID: `(none)` / ページ内順序: 2
- caption/列: figure 2
- 周辺文脈（EN）: I pick the id=2 and compute the posterior predictive probability of each possible outcome (0,1,2,\ldots,28) . At this point we don’t need to consider LOO-CV issues, and can focus o
- 周辺文脈（JA, 自動訳）: 4 離散モデルと連続モデルの比較 / id=2 を選択し、考えられる各結果の事後予測確率 (0,1,2,\ldots,28) を計算します。現時点では、LOO-CV の問題を考慮する必要はなく、次のことに集中できます。
- Workflowフェーズ: **Posterior predictive checking / calibration**
- 実務での読み方: モデルが再現すべき特徴を外していないか確認する。PPC統計量と図をartifact化し、モデル改善の根拠にする。
- MLflow連携: `ppc_stat_*, loo_pit_ecdf_maxdev, calibration_error, replicated_seed`
- 参照: [公式ページ](https://avehtari.github.io/Bayesian-Workflow/nabiximols/nabiximols.html) / [ソース候補](https://github.com/avehtari/Bayesian-Workflow/blob/eb00fa4397314ef7d90203382542bd44c590e289/nabiximols/nabiximols.R)

#### `nabiximols-nabiximols/figure-003`

- 種別: `figure` / 公式ID: `(none)` / ページ内順序: 3
- caption/列: figure 3
- 周辺文脈（EN）: In case of normal model, the observation model is continuous, and we can compute posterior predictive densities. I use log_lik() to compute log predictive densities. I compute the
- 周辺文脈（JA, 自動訳）: 4 離散モデルと連続モデルの比較 / 通常モデルの場合、観測モデルは連続であり、事後予測密度を計算できます。 log_lik() を使用してログの予測密度を計算します。私は計算します
- Workflowフェーズ: **Posterior predictive checking / calibration**
- 実務での読み方: モデルが再現すべき特徴を外していないか確認する。PPC統計量と図をartifact化し、モデル改善の根拠にする。
- MLflow連携: `ppc_stat_*, loo_pit_ecdf_maxdev, calibration_error, replicated_seed`
- 参照: [公式ページ](https://avehtari.github.io/Bayesian-Workflow/nabiximols/nabiximols.html) / [ソース候補](https://github.com/avehtari/Bayesian-Workflow/blob/eb00fa4397314ef7d90203382542bd44c590e289/nabiximols/nabiximols.R)

#### `nabiximols-nabiximols/figure-004`

- 種別: `figure` / 公式ID: `(none)` / ページ内順序: 4
- caption/列: figure 4
- 周辺文脈（EN）: We can’t compare probabilities and densities directly, but we can discretize the density to get probabilities. As the outcomes are integers (0,1,2,\ldots,28) , we can compute proba
- 周辺文脈（JA, 自動訳）: 4 離散モデルと連続モデルの比較 / 確率と密度を直接比較することはできませんが、密度を離散化して確率を取得することはできます。結果は整数 (0,1,2,\ldots,28) なので、プロバを計算できます。
- Workflowフェーズ: **Unclassified / inspect manually**
- 実務での読み方: captionが薄い図表。前後の本文・コードchunk・公式ソースを確認して役割を確定する。
- MLflow連携: `source_page_url, source_repo_url, manual_review_status`
- 参照: [公式ページ](https://avehtari.github.io/Bayesian-Workflow/nabiximols/nabiximols.html) / [ソース候補](https://github.com/avehtari/Bayesian-Workflow/blob/eb00fa4397314ef7d90203382542bd44c590e289/nabiximols/nabiximols.R)

#### `nabiximols-nabiximols/figure-005`

- 種別: `figure` / 公式ID: `(none)` / ページ内順序: 5
- caption/列: figure 5
- 周辺文脈（EN）: We can then integrate the density over the interval. For example, integrate predictive density from 11.5 to 12.5 to get a probability that 11.5 < cu < 12.5 (it doesn’t matter here
- 周辺文脈（JA, 自動訳）: 4 離散モデルと連続モデルの比較 / 次に、区間にわたる密度を積分できます。たとえば、11.5 から 12.5 までの予測密度を積分して、11.5 < cu < 12.5 である確率を取得します (ここでは関係ありません)
- Workflowフェーズ: **Posterior summary / effect interpretation**
- 実務での読み方: 推定効果・不確実性・派生量を意思決定に接続する。平均だけでなく区間・分布・実務閾値超過確率を残す。
- MLflow連携: `posterior_draws_uri, model_code_hash, ci_width, decision_threshold_prob`
- 参照: [公式ページ](https://avehtari.github.io/Bayesian-Workflow/nabiximols/nabiximols.html) / [ソース候補](https://github.com/avehtari/Bayesian-Workflow/blob/eb00fa4397314ef7d90203382542bd44c590e289/nabiximols/nabiximols.R)

#### `nabiximols-nabiximols/fig-discretized-normal`

- 種別: `figure` / 公式ID: `fig-discretized-normal` / ページ内順序: 6
- caption/列: Figure 2
- 周辺文脈（EN）: Now the probability of each interval is approximated by the height times the width of a bar. The height is the density in the middle of the interval and width of the bar is 1, and
- 周辺文脈（JA, 自動訳）: 4 離散モデルと連続モデルの比較 / 各区間の確率は、バーの高さと幅の積で近似されます。高さは間隔の中央の密度であり、バーの幅は 1 であり、
- Workflowフェーズ: **Posterior summary / effect interpretation**
- 実務での読み方: 推定効果・不確実性・派生量を意思決定に接続する。平均だけでなく区間・分布・実務閾値超過確率を残す。
- MLflow連携: `posterior_draws_uri, model_code_hash, ci_width, decision_threshold_prob`
- 参照: [公式ページ](https://avehtari.github.io/Bayesian-Workflow/nabiximols/nabiximols.html#fig-discretized-normal) / [ソース候補](https://github.com/avehtari/Bayesian-Workflow/blob/eb00fa4397314ef7d90203382542bd44c590e289/nabiximols/nabiximols.R)

#### `nabiximols-nabiximols/fig-ppc_hist-binomial`

- 種別: `figure` / 公式ID: `fig-ppc_hist-binomial` / ページ内順序: 7
- caption/列: Figure 3
- 周辺文脈（EN）: Histograms of posterior predictive replicates show that the binomial model predicts lower probability for both 0 and 28 than what is the observed proportion.
- 周辺文脈（JA, 自動訳）: 5 モデルのチェック / 事後予測反復のヒストグラムは、二項モデルが 0 と 28 の両方について観測された割合よりも低い確率を予測することを示しています。
- Workflowフェーズ: **EDA / observed data**
- 実務での読み方: モデル化前に、観測単位・外れ値・欠測・群構造・時系列性・上限/下限などを確認する。MLflowではデータ版と前処理版を固定する。
- MLflow連携: `dataset_uri, dataset_hash, preprocessing_version, n_obs, group_count`
- 参照: [公式ページ](https://avehtari.github.io/Bayesian-Workflow/nabiximols/nabiximols.html#fig-ppc_hist-binomial) / [ソース候補](https://github.com/avehtari/Bayesian-Workflow/blob/eb00fa4397314ef7d90203382542bd44c590e289/nabiximols/nabiximols.R)

#### `nabiximols-nabiximols/fig-ppc_bars-binomial`

- 種別: `figure` / 公式ID: `fig-ppc_bars-binomial` / ページ内順序: 8
- caption/列: Figure 4
- 周辺文脈（EN）: We can also look at the marginal distribution of the data and posterior replicates.
- 周辺文脈（JA, 自動訳）: 5 モデルのチェック / データの周辺分布と事後複製を確認することもできます。
- Workflowフェーズ: **EDA / observed data**
- 実務での読み方: モデル化前に、観測単位・外れ値・欠測・群構造・時系列性・上限/下限などを確認する。MLflowではデータ版と前処理版を固定する。
- MLflow連携: `dataset_uri, dataset_hash, preprocessing_version, n_obs, group_count`
- 参照: [公式ページ](https://avehtari.github.io/Bayesian-Workflow/nabiximols/nabiximols.html#fig-ppc_bars-binomial) / [ソース候補](https://github.com/avehtari/Bayesian-Workflow/blob/eb00fa4397314ef7d90203382542bd44c590e289/nabiximols/nabiximols.R)

#### `nabiximols-nabiximols/fig-ppc_loo_pit_ecdf-binomial`

- 種別: `figure` / 公式ID: `fig-ppc_loo_pit_ecdf-binomial` / ページ内順序: 9
- caption/列: Figure 5
- 周辺文脈（EN）: This effect can be seen also in LOO-PIT-ECDF calibration check plot ( Säilynoja, Bürkner, and Vehtari 2022 ) which shows that the pointwise predictive distributions are too narrow.
- 周辺文脈（JA, 自動訳）: 5 モデルのチェック / この効果は、LOO-PIT-ECDF キャリブレーション チェック プロット (Säilynoja、Bürkner、および Vehtari 2022) にも見られ、点ごとの予測分布が狭すぎることが示されています。
- Workflowフェーズ: **Posterior predictive checking / calibration**
- 実務での読み方: モデルが再現すべき特徴を外していないか確認する。PPC統計量と図をartifact化し、モデル改善の根拠にする。
- MLflow連携: `ppc_stat_*, loo_pit_ecdf_maxdev, calibration_error, replicated_seed`
- 参照: [公式ページ](https://avehtari.github.io/Bayesian-Workflow/nabiximols/nabiximols.html#fig-ppc_loo_pit_ecdf-binomial) / [ソース候補](https://github.com/avehtari/Bayesian-Workflow/blob/eb00fa4397314ef7d90203382542bd44c590e289/nabiximols/nabiximols.R)

#### `nabiximols-nabiximols/fig-ppc_hist-normal`

- 種別: `figure` / 公式ID: `fig-ppc_hist-normal` / ページ内順序: 10
- caption/列: Figure 6
- 周辺文脈（EN）: The normal model posterior predictive replicates look even more different than the observed data, including predicting outcomes less than 0 and larger than 28 , but the higher prob
- 周辺文脈（JA, 自動訳）: 5 モデルのチェック / 通常のモデルの事後予測反復は、0 未満および 28 より大きい結果の予測を含め、観察されたデータよりもさらに異なって見えますが、確率はより高くなります。
- Workflowフェーズ: **EDA / observed data**
- 実務での読み方: モデル化前に、観測単位・外れ値・欠測・群構造・時系列性・上限/下限などを確認する。MLflowではデータ版と前処理版を固定する。
- MLflow連携: `dataset_uri, dataset_hash, preprocessing_version, n_obs, group_count`
- 参照: [公式ページ](https://avehtari.github.io/Bayesian-Workflow/nabiximols/nabiximols.html#fig-ppc_hist-normal) / [ソース候補](https://github.com/avehtari/Bayesian-Workflow/blob/eb00fa4397314ef7d90203382542bd44c590e289/nabiximols/nabiximols.R)

#### `nabiximols-nabiximols/fig-ppc_loo_pit_ecdf-normal`

- 種別: `figure` / 公式ID: `fig-ppc_loo_pit_ecdf-normal` / ページ内順序: 11
- caption/列: Figure 7
- 周辺文脈（EN）: LOO-PIT-ECDF calibration check plot for normal model does indicate some problem with too few PIT values near 0.5, but surprisingly the miscalibration effects at left and right canc
- 周辺文脈（JA, 自動訳）: 5 通常モデルのモデル チェック/LOO-PIT-ECDF キャリブレーション チェック プロットは、PIT 値が 0.5 付近で少なすぎるという問題を示していますが、驚くべきことに、左右のキャリブレーションの影響が誤っていることがわかります。
- Workflowフェーズ: **Posterior predictive checking / calibration**
- 実務での読み方: モデルが再現すべき特徴を外していないか確認する。PPC統計量と図をartifact化し、モデル改善の根拠にする。
- MLflow連携: `ppc_stat_*, loo_pit_ecdf_maxdev, calibration_error, replicated_seed`
- 参照: [公式ページ](https://avehtari.github.io/Bayesian-Workflow/nabiximols/nabiximols.html#fig-ppc_loo_pit_ecdf-normal) / [ソース候補](https://github.com/avehtari/Bayesian-Workflow/blob/eb00fa4397314ef7d90203382542bd44c590e289/nabiximols/nabiximols.R)

#### `nabiximols-nabiximols/fig-ppc_marginal_pit_ecdf-normal`

- 種別: `figure` / 公式ID: `fig-ppc_marginal_pit_ecdf-normal` / ページ内順序: 12
- caption/列: Figure 8
- 周辺文脈（EN）: We can also examine PIT values computed by comparing all posterior predictive draws with observations marginally, which in this case show the miscalibration very clearly.
- 周辺文脈（JA, 自動訳）: 5 モデルのチェック / すべての事後予測描画を観測結果とわずかに比較することによって計算された PIT 値を調べることもできます。この場合、誤った校正が非常に明確に示されます。
- Workflowフェーズ: **Posterior predictive checking / calibration**
- 実務での読み方: モデルが再現すべき特徴を外していないか確認する。PPC統計量と図をartifact化し、モデル改善の根拠にする。
- MLflow連携: `ppc_stat_*, loo_pit_ecdf_maxdev, calibration_error, replicated_seed`
- 参照: [公式ページ](https://avehtari.github.io/Bayesian-Workflow/nabiximols/nabiximols.html#fig-ppc_marginal_pit_ecdf-normal) / [ソース候補](https://github.com/avehtari/Bayesian-Workflow/blob/eb00fa4397314ef7d90203382542bd44c590e289/nabiximols/nabiximols.R)

#### `nabiximols-nabiximols/fig-ppc_hist-betabinomial`

- 種別: `figure` / 公式ID: `fig-ppc_hist-betabinomial` / ページ内順序: 13
- caption/列: Figure 9
- 周辺文脈（EN）: The posterior predictive replicates from beta-binomial look very much like the original data.
- 周辺文脈（JA, 自動訳）: 8 モデルのチェック / ベータ二項からの事後予測複製は、元のデータと非常によく似ています。
- Workflowフェーズ: **EDA / observed data**
- 実務での読み方: モデル化前に、観測単位・外れ値・欠測・群構造・時系列性・上限/下限などを確認する。MLflowではデータ版と前処理版を固定する。
- MLflow連携: `dataset_uri, dataset_hash, preprocessing_version, n_obs, group_count`
- 参照: [公式ページ](https://avehtari.github.io/Bayesian-Workflow/nabiximols/nabiximols.html#fig-ppc_hist-betabinomial) / [ソース候補](https://github.com/avehtari/Bayesian-Workflow/blob/eb00fa4397314ef7d90203382542bd44c590e289/nabiximols/nabiximols.R)

#### `nabiximols-nabiximols/fig-ppc_bars-betabinomial`

- 種別: `figure` / 公式ID: `fig-ppc_bars-betabinomial` / ページ内順序: 14
- caption/列: Figure 10
- 周辺文脈（EN）: We can also look at the marginal distribution of the data and posterior replicates.
- 周辺文脈（JA, 自動訳）: 8 モデルの検査 / データの周辺分布と事後反復も調べることができます。
- Workflowフェーズ: **EDA / observed data**
- 実務での読み方: モデル化前に、観測単位・外れ値・欠測・群構造・時系列性・上限/下限などを確認する。MLflowではデータ版と前処理版を固定する。
- MLflow連携: `dataset_uri, dataset_hash, preprocessing_version, n_obs, group_count`
- 参照: [公式ページ](https://avehtari.github.io/Bayesian-Workflow/nabiximols/nabiximols.html#fig-ppc_bars-betabinomial) / [ソース候補](https://github.com/avehtari/Bayesian-Workflow/blob/eb00fa4397314ef7d90203382542bd44c590e289/nabiximols/nabiximols.R)

#### `nabiximols-nabiximols/fig-loo_pit_ecdf-betabinomial`

- 種別: `figure` / 公式ID: `fig-loo_pit_ecdf-betabinomial` / ページ内順序: 15
- caption/列: Figure 11
- 周辺文脈（EN）: LOO-PIT-ECDF calibration looks very nice and also better than for the normal model.
- 周辺文脈（JA, 自動訳）: 8 モデルチェック / LOO-PIT-ECDF キャリブレーションは非常に素晴らしく、通常のモデルよりも優れています。
- Workflowフェーズ: **Posterior predictive checking / calibration**
- 実務での読み方: モデルが再現すべき特徴を外していないか確認する。PPC統計量と図をartifact化し、モデル改善の根拠にする。
- MLflow連携: `ppc_stat_*, loo_pit_ecdf_maxdev, calibration_error, replicated_seed`
- 参照: [公式ページ](https://avehtari.github.io/Bayesian-Workflow/nabiximols/nabiximols.html#fig-loo_pit_ecdf-betabinomial) / [ソース候補](https://github.com/avehtari/Bayesian-Workflow/blob/eb00fa4397314ef7d90203382542bd44c590e289/nabiximols/nabiximols.R)

#### `nabiximols-nabiximols/fig-ppc_pit_ecdf-betabinomial`

- 種別: `figure` / 公式ID: `fig-ppc_pit_ecdf-betabinomial` / ページ内順序: 16
- caption/列: Figure 12
- 周辺文脈（EN）: The hierarchical beta-binomial model can also be used to illustrate the importance for using crossvalidation for computing PIT values. If we use the same observations to fit the mo
- 周辺文脈（JA, 自動訳）: 8 モデルの検査 / 階層型ベータ二項モデルは、PIT 値の計算に交差検証を使用する重要性を説明するためにも使用できます。同じ観察を使用して mo を当てはめると、
- Workflowフェーズ: **Posterior predictive checking / calibration**
- 実務での読み方: モデルが再現すべき特徴を外していないか確認する。PPC統計量と図をartifact化し、モデル改善の根拠にする。
- MLflow連携: `ppc_stat_*, loo_pit_ecdf_maxdev, calibration_error, replicated_seed`
- 参照: [公式ページ](https://avehtari.github.io/Bayesian-Workflow/nabiximols/nabiximols.html#fig-ppc_pit_ecdf-betabinomial) / [ソース候補](https://github.com/avehtari/Bayesian-Workflow/blob/eb00fa4397314ef7d90203382542bd44c590e289/nabiximols/nabiximols.R)

#### `nabiximols-nabiximols/fig-calibration-0-betabinomial`

- 種別: `figure` / 公式ID: `fig-calibration-0-betabinomial` / ページ内順序: 17
- caption/列: Figure 13
- 周辺文脈（EN）: Calibration check with reliability diagram for 0 vs others
- 周辺文脈（JA, 自動訳）: 8 モデルチェック/0 対その他の信頼性図によるキャリブレーションチェック
- Workflowフェーズ: **Posterior predictive checking / calibration**
- 実務での読み方: モデルが再現すべき特徴を外していないか確認する。PPC統計量と図をartifact化し、モデル改善の根拠にする。
- MLflow連携: `ppc_stat_*, loo_pit_ecdf_maxdev, calibration_error, replicated_seed`
- 参照: [公式ページ](https://avehtari.github.io/Bayesian-Workflow/nabiximols/nabiximols.html#fig-calibration-0-betabinomial) / [ソース候補](https://github.com/avehtari/Bayesian-Workflow/blob/eb00fa4397314ef7d90203382542bd44c590e289/nabiximols/nabiximols.R)

#### `nabiximols-nabiximols/fig-calibration-28-betabinomial`

- 種別: `figure` / 公式ID: `fig-calibration-28-betabinomial` / ページ内順序: 18
- caption/列: Figure 14
- 周辺文脈（EN）: Calibration check with reliability diagram for 28 vs others
- 周辺文脈（JA, 自動訳）: 8 モデルチェック/28対他の信頼性図によるキャリブレーションチェック
- Workflowフェーズ: **Posterior predictive checking / calibration**
- 実務での読み方: モデルが再現すべき特徴を外していないか確認する。PPC統計量と図をartifact化し、モデル改善の根拠にする。
- MLflow連携: `ppc_stat_*, loo_pit_ecdf_maxdev, calibration_error, replicated_seed`
- 参照: [公式ページ](https://avehtari.github.io/Bayesian-Workflow/nabiximols/nabiximols.html#fig-calibration-28-betabinomial) / [ソース候補](https://github.com/avehtari/Bayesian-Workflow/blob/eb00fa4397314ef7d90203382542bd44c590e289/nabiximols/nabiximols.R)

#### `nabiximols-nabiximols/fig-ppc_bars-betabinomial2b`

- 種別: `figure` / 公式ID: `fig-ppc_bars-betabinomial2b` / ページ内順序: 19
- caption/列: Figure 15
- 周辺文脈（EN）: The marginal distribution of the posterior replicates matches the data better than earlier models.
- 周辺文脈（JA, 自動訳）: 12 モデルのチェック / 事後反復の周辺分布は、以前のモデルよりもデータとよく一致しています。
- Workflowフェーズ: **EDA / observed data**
- 実務での読み方: モデル化前に、観測単位・外れ値・欠測・群構造・時系列性・上限/下限などを確認する。MLflowではデータ版と前処理版を固定する。
- MLflow連携: `dataset_uri, dataset_hash, preprocessing_version, n_obs, group_count`
- 参照: [公式ページ](https://avehtari.github.io/Bayesian-Workflow/nabiximols/nabiximols.html#fig-ppc_bars-betabinomial2b) / [ソース候補](https://github.com/avehtari/Bayesian-Workflow/blob/eb00fa4397314ef7d90203382542bd44c590e289/nabiximols/nabiximols.R)

#### `nabiximols-nabiximols/fig-ppc_pit_ecdf-betabinomial2b`

- 種別: `figure` / 公式ID: `fig-ppc_pit_ecdf-betabinomial2b` / ページ内順序: 20
- caption/列: Figure 16
- 周辺文脈（EN）: LOO-PIT-ECDF plot looks good:
- 周辺文脈（JA, 自動訳）: 12 モデルのチェック / LOO-PIT-ECDF プロットは良好です。
- Workflowフェーズ: **Posterior predictive checking / calibration**
- 実務での読み方: モデルが再現すべき特徴を外していないか確認する。PPC統計量と図をartifact化し、モデル改善の根拠にする。
- MLflow連携: `ppc_stat_*, loo_pit_ecdf_maxdev, calibration_error, replicated_seed`
- 参照: [公式ページ](https://avehtari.github.io/Bayesian-Workflow/nabiximols/nabiximols.html#fig-ppc_pit_ecdf-betabinomial2b) / [ソース候補](https://github.com/avehtari/Bayesian-Workflow/blob/eb00fa4397314ef7d90203382542bd44c590e289/nabiximols/nabiximols.R)

#### `nabiximols-nabiximols/fig-calibration-0-betabinomial2`

- 種別: `figure` / 公式ID: `fig-calibration-0-betabinomial2` / ページ内順序: 21
- caption/列: Figure 17
- 周辺文脈（EN）: Calibration check with reliability diagrams for 0 vs others and 28 vs others look better than for the previous model.
- 周辺文脈（JA, 自動訳）: 12 モデル チェック / 0 対その他および 28 対その他の信頼性図によるキャリブレーション チェックは、以前のモデルよりも優れているようです。
- Workflowフェーズ: **Posterior predictive checking / calibration**
- 実務での読み方: モデルが再現すべき特徴を外していないか確認する。PPC統計量と図をartifact化し、モデル改善の根拠にする。
- MLflow連携: `ppc_stat_*, loo_pit_ecdf_maxdev, calibration_error, replicated_seed`
- 参照: [公式ページ](https://avehtari.github.io/Bayesian-Workflow/nabiximols/nabiximols.html#fig-calibration-0-betabinomial2) / [ソース候補](https://github.com/avehtari/Bayesian-Workflow/blob/eb00fa4397314ef7d90203382542bd44c590e289/nabiximols/nabiximols.R)

#### `nabiximols-nabiximols/fig-calibration-28-betabinomial2`

- 種別: `figure` / 公式ID: `fig-calibration-28-betabinomial2` / ページ内順序: 22
- caption/列: Figure 18
- 周辺文脈（EN）: Calibration check with reliability diagrams for 0 vs others and 28 vs others look better than for the previous model.
- 周辺文脈（JA, 自動訳）: 12 モデル チェック / 0 対その他および 28 対その他の信頼性図によるキャリブレーション チェックは、以前のモデルよりも優れているようです。
- Workflowフェーズ: **Posterior predictive checking / calibration**
- 実務での読み方: モデルが再現すべき特徴を外していないか確認する。PPC統計量と図をartifact化し、モデル改善の根拠にする。
- MLflow連携: `ppc_stat_*, loo_pit_ecdf_maxdev, calibration_error, replicated_seed`
- 参照: [公式ページ](https://avehtari.github.io/Bayesian-Workflow/nabiximols/nabiximols.html#fig-calibration-28-betabinomial2) / [ソース候補](https://github.com/avehtari/Bayesian-Workflow/blob/eb00fa4397314ef7d90203382542bd44c590e289/nabiximols/nabiximols.R)

#### `nabiximols-nabiximols/fig-posterior_prediction-betabinomial2`

- 種別: `figure` / 公式ID: `fig-posterior_prediction-betabinomial2` / ページ内順序: 23
- caption/列: Figure 19
- 周辺文脈（EN）: We start by examining the posterior predictive distribution. We predict cu for a new id=129 given cu_baseline=28 (median value). The distribution is wide as it included the aleator
- 周辺文脈（JA, 自動訳）: 13 治療効果 / 事後予測分布を調べることから始めます。 cu_baseline=28 (中央値) を前提として、新しい id=129 の cu を予測します。アリエーターも含めて分布は広い
- Workflowフェーズ: **EDA / observed data**
- 実務での読み方: モデル化前に、観測単位・外れ値・欠測・群構造・時系列性・上限/下限などを確認する。MLflowではデータ版と前処理版を固定する。
- MLflow連携: `dataset_uri, dataset_hash, preprocessing_version, n_obs, group_count`
- 参照: [公式ページ](https://avehtari.github.io/Bayesian-Workflow/nabiximols/nabiximols.html#fig-posterior_prediction-betabinomial2) / [ソース候補](https://github.com/avehtari/Bayesian-Workflow/blob/eb00fa4397314ef7d90203382542bd44c590e289/nabiximols/nabiximols.R)

#### `nabiximols-nabiximols/fig-posterior_prediction-diff-betabinomial2`

- 種別: `figure` / 公式ID: `fig-posterior_prediction-diff-betabinomial2` / ページ内順序: 24
- caption/列: Figure 20
- 周辺文脈（EN）: The difference between groups is the biggest in week 12. The next plot shows the comparison of predicted cu between the groups in different weeks.
- 周辺文脈（JA, 自動訳）: 13 治療効果 / グループ間の差は 12 週目に最も大きくなります。次のプロットは、異なる週におけるグループ間の予測 cu の比較を示しています。
- Workflowフェーズ: **Posterior summary / effect interpretation**
- 実務での読み方: 推定効果・不確実性・派生量を意思決定に接続する。平均だけでなく区間・分布・実務閾値超過確率を残す。
- MLflow連携: `posterior_draws_uri, model_code_hash, ci_width, decision_threshold_prob`
- 参照: [公式ページ](https://avehtari.github.io/Bayesian-Workflow/nabiximols/nabiximols.html#fig-posterior_prediction-diff-betabinomial2) / [ソース候補](https://github.com/avehtari/Bayesian-Workflow/blob/eb00fa4397314ef7d90203382542bd44c590e289/nabiximols/nabiximols.R)

#### `nabiximols-nabiximols/fig-kde-kde-hist-comparison-betabinomial2`

- 種別: `figure` / 公式ID: `fig-kde-kde-hist-comparison-betabinomial2` / ページ内順序: 25
- caption/列: Figure 21
- 周辺文脈（EN）: For comparison I plot 1) the ggplot2 default KDE with stat_density, 2) ggdist KDE with stat_slabinterval, and 3) ggplot default histogram with stat_histogram for the week 12 differ
- 周辺文脈（JA, 自動訳）: 13 治療効果 / 比較のために、1) stat_density を使用した ggplot2 のデフォルト KDE、2) stat_slabinterval を使用した ggdist KDE、および 3) 週の stat_histogram を使用した ggplot のデフォルト ヒストグラムをプロットしました。
- Workflowフェーズ: **Posterior summary / effect interpretation**
- 実務での読み方: 推定効果・不確実性・派生量を意思決定に接続する。平均だけでなく区間・分布・実務閾値超過確率を残す。
- MLflow連携: `posterior_draws_uri, model_code_hash, ci_width, decision_threshold_prob`
- 参照: [公式ページ](https://avehtari.github.io/Bayesian-Workflow/nabiximols/nabiximols.html#fig-kde-kde-hist-comparison-betabinomial2) / [ソース候補](https://github.com/avehtari/Bayesian-Workflow/blob/eb00fa4397314ef7d90203382542bd44c590e289/nabiximols/nabiximols.R)

#### `nabiximols-nabiximols/fig-epred-betabinomial2`

- 種別: `figure` / 公式ID: `fig-epred-betabinomial2` / ページ内順序: 26
- caption/列: Figure 22
- 周辺文脈（EN）: To get more accuracy we can remove the aleatoric uncertainty and focus on expected effect. The following plots shows the expectation of the posterior predictive distribution for cu
- 周辺文脈（JA, 自動訳）: 13 治療効果 / より正確さを得るために、偶然の不確実性を取り除き、期待される効果に焦点を当てることができます。次のプロットは、cu の事後予測分布の期待値を示しています。
- Workflowフェーズ: **EDA / observed data**
- 実務での読み方: モデル化前に、観測単位・外れ値・欠測・群構造・時系列性・上限/下限などを確認する。MLflowではデータ版と前処理版を固定する。
- MLflow連携: `dataset_uri, dataset_hash, preprocessing_version, n_obs, group_count`
- 参照: [公式ページ](https://avehtari.github.io/Bayesian-Workflow/nabiximols/nabiximols.html#fig-epred-betabinomial2) / [ソース候補](https://github.com/avehtari/Bayesian-Workflow/blob/eb00fa4397314ef7d90203382542bd44c590e289/nabiximols/nabiximols.R)

#### `nabiximols-nabiximols/fig-epred-diff-betabinomial2`

- 種別: `figure` / 公式ID: `fig-epred-diff-betabinomial2` / ページ内順序: 27
- caption/列: Figure 23
- 周辺文脈（EN）: The next plot shows the comparison of expected cu between the groups in different weeks.
- 周辺文脈（JA, 自動訳）: 13 治療効果 / 次のプロットは、異なる週のグループ間の予想 cu の比較を示しています。
- Workflowフェーズ: **Posterior summary / effect interpretation**
- 実務での読み方: 推定効果・不確実性・派生量を意思決定に接続する。平均だけでなく区間・分布・実務閾値超過確率を残す。
- MLflow連携: `posterior_draws_uri, model_code_hash, ci_width, decision_threshold_prob`
- 参照: [公式ページ](https://avehtari.github.io/Bayesian-Workflow/nabiximols/nabiximols.html#fig-epred-diff-betabinomial2) / [ソース候補](https://github.com/avehtari/Bayesian-Workflow/blob/eb00fa4397314ef7d90203382542bd44c590e289/nabiximols/nabiximols.R)

#### `nabiximols-nabiximols/fig-priorsense-diff-betabinomial2b`

- 種別: `figure` / 公式ID: `fig-priorsense-diff-betabinomial2b` / ページ内順序: 28
- caption/列: Figure 24
- 周辺文脈（EN）: Prior-likelihood sensitivity analysis using powerscaling approach for the treatment effect posteriors at weeks 4, 8, and 12
- 周辺文脈（JA, 自動訳）: 14 事後治療効果の事前および尤度感度 / 4、8、および 12 週目での事後治療効果に対するパワースケーリング手法を使用した事前尤度感度分析
- Workflowフェーズ: **Posterior summary / effect interpretation**
- 実務での読み方: 推定効果・不確実性・派生量を意思決定に接続する。平均だけでなく区間・分布・実務閾値超過確率を残す。
- MLflow連携: `posterior_draws_uri, model_code_hash, ci_width, decision_threshold_prob`
- 参照: [公式ページ](https://avehtari.github.io/Bayesian-Workflow/nabiximols/nabiximols.html#fig-priorsense-diff-betabinomial2b) / [ソース候補](https://github.com/avehtari/Bayesian-Workflow/blob/eb00fa4397314ef7d90203382542bd44c590e289/nabiximols/nabiximols.R)

#### `nabiximols-nabiximols/fig-ppc_loo_pit_ecdf-normal2b`

- 種別: `figure` / 公式ID: `fig-ppc_loo_pit_ecdf-normal2b` / ページ内順序: 29
- caption/列: Figure 25
- 周辺文脈（EN）: LOO-PIT-ECDF shows miscalibration
- 周辺文脈（JA, 自動訳）: 15 モデル選択に対する感度 / LOO-PIT-ECDF が誤った校正を示す
- Workflowフェーズ: **Posterior predictive checking / calibration**
- 実務での読み方: モデルが再現すべき特徴を外していないか確認する。PPC統計量と図をartifact化し、モデル改善の根拠にする。
- MLflow連携: `ppc_stat_*, loo_pit_ecdf_maxdev, calibration_error, replicated_seed`
- 参照: [公式ページ](https://avehtari.github.io/Bayesian-Workflow/nabiximols/nabiximols.html#fig-ppc_loo_pit_ecdf-normal2b) / [ソース候補](https://github.com/avehtari/Bayesian-Workflow/blob/eb00fa4397314ef7d90203382542bd44c590e289/nabiximols/nabiximols.R)

#### `nabiximols-nabiximols/fig-ppc_pit_ecdf-normal2b`

- 種別: `figure` / 公式ID: `fig-ppc_pit_ecdf-normal2b` / ページ内順序: 30
- caption/列: Figure 26
- 周辺文脈（EN）: Marginal PIT-ECDF shows clear miscalibration
- 周辺文脈（JA, 自動訳）: 15 モデル選択に対する感度 / 限界 PIT-ECDF は明らかな校正ミスを示す
- Workflowフェーズ: **Posterior predictive checking / calibration**
- 実務での読み方: モデルが再現すべき特徴を外していないか確認する。PPC統計量と図をartifact化し、モデル改善の根拠にする。
- MLflow連携: `ppc_stat_*, loo_pit_ecdf_maxdev, calibration_error, replicated_seed`
- 参照: [公式ページ](https://avehtari.github.io/Bayesian-Workflow/nabiximols/nabiximols.html#fig-ppc_pit_ecdf-normal2b) / [ソース候補](https://github.com/avehtari/Bayesian-Workflow/blob/eb00fa4397314ef7d90203382542bd44c590e289/nabiximols/nabiximols.R)

#### `nabiximols-nabiximols/fig-epred-diff-4models`

- 種別: `figure` / 公式ID: `fig-epred-diff-4models` / ページ内順序: 31
- caption/列: Figure 27
- 周辺文脈（EN）: We plot here the difference either for the last 4 week period or for the all weeks depending on the model.
- 周辺文脈（JA, 自動訳）: 15 モデル選択に対する感度 / ここでは、モデルに応じて、過去 4 週間または全週の差異をプロットします。
- Workflowフェーズ: **Prior-likelihood sensitivity**
- 実務での読み方: 結論がpriorに依存していないか、またpriorとlikelihoodが衝突していないか確認する。
- MLflow連携: `priorsense_*, power_scaling_delta, prior_conflict_flag`
- 参照: [公式ページ](https://avehtari.github.io/Bayesian-Workflow/nabiximols/nabiximols.html#fig-epred-diff-4models) / [ソース候補](https://github.com/avehtari/Bayesian-Workflow/blob/eb00fa4397314ef7d90203382542bd44c590e289/nabiximols/nabiximols.R)

#### `nabiximols-nabiximols/tinytable_ppjihagml4i9fngi988z`

- 種別: `table` / 公式ID: `tinytable_ppjihagml4i9fngi988z` / ページ内順序: 1
- caption/列: variable; prior; likelihood; diagnosis; b_Intercept; 0.15; 0.54; potential prior-likelihood conflict
- 周辺文脈（EN）: The priors provided by Mills seems a bit narrow, so I do prior-likelihood sensitivity analysis using powerscaling approach ( Kallioinen et al. 2023 ) .
- 周辺文脈（JA, 自動訳）: 9 事前感度分析 / Mills が提供する事前感度は少し狭いように見えるので、パワースケーリング手法を使用して事前尤度感度分析を行います (Kallioinen et al. 2023)。
- Workflowフェーズ: **Prior-likelihood sensitivity**
- 実務での読み方: 結論がpriorに依存していないか、またpriorとlikelihoodが衝突していないか確認する。
- MLflow連携: `priorsense_*, power_scaling_delta, prior_conflict_flag`
- 参照: [公式ページ](https://avehtari.github.io/Bayesian-Workflow/nabiximols/nabiximols.html#tinytable_ppjihagml4i9fngi988z) / [ソース候補](https://github.com/avehtari/Bayesian-Workflow/blob/eb00fa4397314ef7d90203382542bd44c590e289/nabiximols/nabiximols.R)

#### `nabiximols-nabiximols/tinytable_9afmxe70cmvzt9wokn6t`

- 種別: `table` / 公式ID: `tinytable_9afmxe70cmvzt9wokn6t` / ページ内順序: 2
- caption/列: variable; prior; likelihood; diagnosis; b_Intercept; 0.03; 0.41; -
- 周辺文脈（EN）: There are no prior data conflicts.
- 周辺文脈（JA, 自動訳）: 10 の代替事前データ / 以前のデータの競合はありません。
- Workflowフェーズ: **EDA / observed data**
- 実務での読み方: モデル化前に、観測単位・外れ値・欠測・群構造・時系列性・上限/下限などを確認する。MLflowではデータ版と前処理版を固定する。
- MLflow連携: `dataset_uri, dataset_hash, preprocessing_version, n_obs, group_count`
- 参照: [公式ページ](https://avehtari.github.io/Bayesian-Workflow/nabiximols/nabiximols.html#tinytable_9afmxe70cmvzt9wokn6t) / [ソース候補](https://github.com/avehtari/Bayesian-Workflow/blob/eb00fa4397314ef7d90203382542bd44c590e289/nabiximols/nabiximols.R)

#### `nabiximols-nabiximols/tinytable_xkqq12gj92iyhe913grj`

- 種別: `table` / 公式ID: `tinytable_xkqq12gj92iyhe913grj` / ページ内順序: 3
- caption/列: variable; mean; median; sd; mad; q5; q95; rhat
- 周辺文脈（EN）: By comparing phi parameter posteriors, we see that the overdispersion of the beta-binomial in the new model is smaller (smaller phi means bigger overdispersion).
- 周辺文脈（JA, 自動訳）: 11 モデルの改良 / ファイ パラメータの事後比較により、新しいモデルのベータ二項分布の過分散が小さいことがわかります (ファイが小さいほど過分散が大きいことを意味します)。
- Workflowフェーズ: **Posterior summary / effect interpretation**
- 実務での読み方: 推定効果・不確実性・派生量を意思決定に接続する。平均だけでなく区間・分布・実務閾値超過確率を残す。
- MLflow連携: `posterior_draws_uri, model_code_hash, ci_width, decision_threshold_prob`
- 参照: [公式ページ](https://avehtari.github.io/Bayesian-Workflow/nabiximols/nabiximols.html#tinytable_xkqq12gj92iyhe913grj) / [ソース候補](https://github.com/avehtari/Bayesian-Workflow/blob/eb00fa4397314ef7d90203382542bd44c590e289/nabiximols/nabiximols.R)

#### `nabiximols-nabiximols/tinytable_o85637ww2b12ykpz3ezb`

- 種別: `table` / 公式ID: `tinytable_o85637ww2b12ykpz3ezb` / ページ内順序: 4
- caption/列: variable; mean; median; sd; mad; q5; q95; rhat
- 周辺文脈（EN）: By comparing phi parameter posteriors, we see that the overdispersion of the beta-binomial in the new model is smaller (smaller phi means bigger overdispersion).
- 周辺文脈（JA, 自動訳）: 11 モデルの改良 / ファイ パラメータの事後比較により、新しいモデルのベータ二項分布の過分散が小さいことがわかります (ファイが小さいほど過分散が大きいことを意味します)。
- Workflowフェーズ: **Posterior summary / effect interpretation**
- 実務での読み方: 推定効果・不確実性・派生量を意思決定に接続する。平均だけでなく区間・分布・実務閾値超過確率を残す。
- MLflow連携: `posterior_draws_uri, model_code_hash, ci_width, decision_threshold_prob`
- 参照: [公式ページ](https://avehtari.github.io/Bayesian-Workflow/nabiximols/nabiximols.html#tinytable_o85637ww2b12ykpz3ezb) / [ソース候補](https://github.com/avehtari/Bayesian-Workflow/blob/eb00fa4397314ef7d90203382542bd44c590e289/nabiximols/nabiximols.R)

### Building up to a hierarchical model: Coronavirus testing

- ページ: <https://avehtari.github.io/Bayesian-Workflow/coronavirus/coronavirus.html>
- ソース候補: <https://github.com/avehtari/Bayesian-Workflow/blob/eb00fa4397314ef7d90203382542bd44c590e289/coronavirus/coronavirus.R>

#### `coronavirus-coronavirus/fig-specificity_priorsense_1`

- 種別: `figure` / 公式ID: `fig-specificity_priorsense_1` / ページ内順序: 1
- caption/列: Figure 1
- 周辺文脈（EN）: Check prior-likelihood sensitivity using powerscaling
- 周辺文脈（JA, 自動訳）: 2 プールされた特異性と感度を使用した単純なモデルの適合 / パワースケーリングを使用した事前尤度の感度の確認
- Workflowフェーズ: **Prior-likelihood sensitivity**
- 実務での読み方: 結論がpriorに依存していないか、またpriorとlikelihoodが衝突していないか確認する。
- MLflow連携: `priorsense_*, power_scaling_delta, prior_conflict_flag`
- 参照: [公式ページ](https://avehtari.github.io/Bayesian-Workflow/coronavirus/coronavirus.html#fig-specificity_priorsense_1) / [ソース候補](https://github.com/avehtari/Bayesian-Workflow/blob/eb00fa4397314ef7d90203382542bd44c590e289/coronavirus/coronavirus.R)

#### `coronavirus-coronavirus/fig-scatter`

- 種別: `figure` / 公式ID: `fig-scatter` / ページ内順序: 2
- caption/列: Figure 2
- 周辺文脈（EN）: Inference for the population prevalence
- 周辺文脈（JA, 自動訳）: 2 プールされた特異性と感度を使用した単純なモデルの適合 / 集団有病率の推論
- Workflowフェーズ: **Prior-likelihood sensitivity**
- 実務での読み方: 結論がpriorに依存していないか、またpriorとlikelihoodが衝突していないか確認する。
- MLflow連携: `priorsense_*, power_scaling_delta, prior_conflict_flag`
- 参照: [公式ページ](https://avehtari.github.io/Bayesian-Workflow/coronavirus/coronavirus.html#fig-scatter) / [ソース候補](https://github.com/avehtari/Bayesian-Workflow/blob/eb00fa4397314ef7d90203382542bd44c590e289/coronavirus/coronavirus.R)

#### `coronavirus-coronavirus/fig-gg-scatter`

- 種別: `figure` / 公式ID: `fig-gg-scatter` / ページ内順序: 3
- caption/列: Figure 3
- 周辺文脈（EN）: ggplot version
- 周辺文脈（JA, 自動訳）: 2 プールされた特異性と感度を使用した単純なモデル フィット / ggplot バージョン
- Workflowフェーズ: **Prior-likelihood sensitivity**
- 実務での読み方: 結論がpriorに依存していないか、またpriorとlikelihoodが衝突していないか確認する。
- MLflow連携: `priorsense_*, power_scaling_delta, prior_conflict_flag`
- 参照: [公式ページ](https://avehtari.github.io/Bayesian-Workflow/coronavirus/coronavirus.html#fig-gg-scatter) / [ソース候補](https://github.com/avehtari/Bayesian-Workflow/blob/eb00fa4397314ef7d90203382542bd44c590e289/coronavirus/coronavirus.R)

#### `coronavirus-coronavirus/fig-hist`

- 種別: `figure` / 公式ID: `fig-hist` / ページ内順序: 4
- caption/列: Figure 4
- 周辺文脈（EN）: ggplot version
- 周辺文脈（JA, 自動訳）: 2 プールされた特異性と感度を使用した単純なモデル フィット / ggplot バージョン
- Workflowフェーズ: **Prior-likelihood sensitivity**
- 実務での読み方: 結論がpriorに依存していないか、またpriorとlikelihoodが衝突していないか確認する。
- MLflow連携: `priorsense_*, power_scaling_delta, prior_conflict_flag`
- 参照: [公式ページ](https://avehtari.github.io/Bayesian-Workflow/coronavirus/coronavirus.html#fig-hist) / [ソース候補](https://github.com/avehtari/Bayesian-Workflow/blob/eb00fa4397314ef7d90203382542bd44c590e289/coronavirus/coronavirus.R)

#### `coronavirus-coronavirus/fig-gg-hist`

- 種別: `figure` / 公式ID: `fig-gg-hist` / ページ内順序: 5
- caption/列: Figure 5
- 周辺文脈（EN）: ggplot version
- 周辺文脈（JA, 自動訳）: 2 プールされた特異性と感度を使用した単純なモデル フィット / ggplot バージョン
- Workflowフェーズ: **Prior-likelihood sensitivity**
- 実務での読み方: 結論がpriorに依存していないか、またpriorとlikelihoodが衝突していないか確認する。
- MLflow連携: `priorsense_*, power_scaling_delta, prior_conflict_flag`
- 参照: [公式ページ](https://avehtari.github.io/Bayesian-Workflow/coronavirus/coronavirus.html#fig-gg-hist) / [ソース候補](https://github.com/avehtari/Bayesian-Workflow/blob/eb00fa4397314ef7d90203382542bd44c590e289/coronavirus/coronavirus.R)

#### `coronavirus-coronavirus/fig-specificity_priorsense_x`

- 種別: `figure` / 公式ID: `fig-specificity_priorsense_x` / ページ内順序: 6
- caption/列: Figure 6
- 周辺文脈（EN）: Check prior-likelihood sensitivity using powerscaling
- 周辺文脈（JA, 自動訳）: 2 プールされた特異性と感度を使用した単純なモデルの適合 / パワースケーリングを使用した事前尤度の感度の確認
- Workflowフェーズ: **Prior-likelihood sensitivity**
- 実務での読み方: 結論がpriorに依存していないか、またpriorとlikelihoodが衝突していないか確認する。
- MLflow連携: `priorsense_*, power_scaling_delta, prior_conflict_flag`
- 参照: [公式ページ](https://avehtari.github.io/Bayesian-Workflow/coronavirus/coronavirus.html#fig-specificity_priorsense_x) / [ソース候補](https://github.com/avehtari/Bayesian-Workflow/blob/eb00fa4397314ef7d90203382542bd44c590e289/coronavirus/coronavirus.R)

#### `coronavirus-coronavirus/fig-specificity_priorsense_2`

- 種別: `figure` / 公式ID: `fig-specificity_priorsense_2` / ページ内順序: 7
- caption/列: Figure 7
- 周辺文脈（EN）: Check prior-likelihood sensitivity using powerscaling
- 周辺文脈（JA, 自動訳）: 3 感度と特異度の階層モデル / パワースケーリングを使用した事前尤度感度の確認
- Workflowフェーズ: **Prior-likelihood sensitivity**
- 実務での読み方: 結論がpriorに依存していないか、またpriorとlikelihoodが衝突していないか確認する。
- MLflow連携: `priorsense_*, power_scaling_delta, prior_conflict_flag`
- 参照: [公式ページ](https://avehtari.github.io/Bayesian-Workflow/coronavirus/coronavirus.html#fig-specificity_priorsense_2) / [ソース候補](https://github.com/avehtari/Bayesian-Workflow/blob/eb00fa4397314ef7d90203382542bd44c590e289/coronavirus/coronavirus.R)

#### `coronavirus-coronavirus/fig-prior-sensitivity-2`

- 種別: `figure` / 公式ID: `fig-prior-sensitivity-2` / ページ内順序: 8
- caption/列: Figure 8
- 周辺文脈（EN）: Loop over different prior parameter values
- 周辺文脈（JA, 自動訳）: 6 追加の事前感度分析 / 異なる事前パラメータ値のループ
- Workflowフェーズ: **LOO-CV / model comparison**
- 実務での読み方: elpd差だけでなくSEとPareto-kを読み、勝敗より『どのデータ点で負けるか』を確認する。
- MLflow連携: `loo_elpd, loo_elpd_diff, loo_se_diff, pareto_k_gt_0_7, reloo_count`
- 参照: [公式ページ](https://avehtari.github.io/Bayesian-Workflow/coronavirus/coronavirus.html#fig-prior-sensitivity-2) / [ソース候補](https://github.com/avehtari/Bayesian-Workflow/blob/eb00fa4397314ef7d90203382542bd44c590e289/coronavirus/coronavirus.R)

### Using a fitted model for decision analysis: Mixture model for time series competition

- ページ: <https://avehtari.github.io/Bayesian-Workflow/timeseries/timeseries.html>
- ソース候補: <https://github.com/avehtari/Bayesian-Workflow/blob/eb00fa4397314ef7d90203382542bd44c590e289/timeseries/timeseries.R>

#### `timeseries-timeseries/fig-series_1`

- 種別: `figure` / 公式ID: `fig-series_1` / ページ内順序: 1
- caption/列: Figure 1
- 周辺文脈（EN）: OK, now it’s time to get to work. We start by downloading and graphing the data.
- 周辺文脈（JA, 自動訳）: 2 データ / OK、さあ、仕事に取り掛かりましょう。まず、データをダウンロードしてグラフ化します。
- Workflowフェーズ: **EDA / observed data**
- 実務での読み方: モデル化前に、観測単位・外れ値・欠測・群構造・時系列性・上限/下限などを確認する。MLflowではデータ版と前処理版を固定する。
- MLflow連携: `dataset_uri, dataset_hash, preprocessing_version, n_obs, group_count`
- 参照: [公式ページ](https://avehtari.github.io/Bayesian-Workflow/timeseries/timeseries.html#fig-series_1) / [ソース候補](https://github.com/avehtari/Bayesian-Workflow/blob/eb00fa4397314ef7d90203382542bd44c590e289/timeseries/timeseries.R)

#### `timeseries-timeseries/fig-series_2`

- 種別: `figure` / 公式ID: `fig-series_2` / ページ内順序: 2
- caption/列: Figure 2
- 周辺文脈（EN）: Next we plot the estimated slopes and their standard errors:
- 周辺文脈（JA, 自動訳）: 3 個別の線形回帰 / 次に、推定された傾きとその標準誤差をプロットします。
- Workflowフェーズ: **MCMC / computation diagnostics**
- 実務での読み方: 推論結果を解釈する前に、R-hat、ESS、divergence、treedepth、BFMI、trace/pairsを確認する。悪いrunは比較表から除外せず失敗として記録する。
- MLflow連携: `rhat_max, ess_bulk_min, ess_tail_min, divergences, treedepth_hits, bfmi_min`
- 参照: [公式ページ](https://avehtari.github.io/Bayesian-Workflow/timeseries/timeseries.html#fig-series_2) / [ソース候補](https://github.com/avehtari/Bayesian-Workflow/blob/eb00fa4397314ef7d90203382542bd44c590e289/timeseries/timeseries.R)

#### `timeseries-timeseries/fig-series_3`

- 種別: `figure` / 公式ID: `fig-series_3` / ページ内順序: 3
- caption/列: Figure 3
- 周辺文脈（EN）: OK, not much information in the se’s. How about a histogram of the estimated slopes?
- 周辺文脈（JA, 自動訳）: 3 線形回帰を分離 / OK、SE にはあまり情報がありません。推定された傾きのヒストグラムはどうでしょうか?
- Workflowフェーズ: **MCMC / computation diagnostics**
- 実務での読み方: 推論結果を解釈する前に、R-hat、ESS、divergence、treedepth、BFMI、trace/pairsを確認する。悪いrunは比較表から除外せず失敗として記録する。
- MLflow連携: `rhat_max, ess_bulk_min, ess_tail_min, divergences, treedepth_hits, bfmi_min`
- 参照: [公式ページ](https://avehtari.github.io/Bayesian-Workflow/timeseries/timeseries.html#fig-series_3) / [ソース候補](https://github.com/avehtari/Bayesian-Workflow/blob/eb00fa4397314ef7d90203382542bd44c590e289/timeseries/timeseries.R)

### Posterior predictive checking: Stochastic learning in dogs

- ページ: <https://avehtari.github.io/Bayesian-Workflow/dogs/dogs.html>
- ソース候補: <https://github.com/avehtari/Bayesian-Workflow/blob/eb00fa4397314ef7d90203382542bd44c590e289/dogs/dogs.R>

#### `dogs-dogs/fig-pred9-0h`

- 種別: `figure` / 公式ID: `fig-pred9-0h` / ページ内順序: 1
- caption/列: Figure 1
- 周辺文脈（EN）: Visualize the model fit for 9 first dogs with some help from tidybayes ( Kay 2023 ) .
- 周辺文脈（JA, 自動訳）: 4.2 予測の視覚化 / tinybayes の助けを借りて、最初の 9 頭の犬に適合するモデルを視覚化します (Kay 2023)。
- Workflowフェーズ: **Posterior predictive checking / calibration**
- 実務での読み方: モデルが再現すべき特徴を外していないか確認する。PPC統計量と図をartifact化し、モデル改善の根拠にする。
- MLflow連携: `ppc_stat_*, loo_pit_ecdf_maxdev, calibration_error, replicated_seed`
- 参照: [公式ページ](https://avehtari.github.io/Bayesian-Workflow/dogs/dogs.html#fig-pred9-0h) / [ソース候補](https://github.com/avehtari/Bayesian-Workflow/blob/eb00fa4397314ef7d90203382542bd44c590e289/dogs/dogs.R)

#### `dogs-dogs/fig-calib-0h`

- 種別: `figure` / 公式ID: `fig-calib-0h` / ページ内順序: 2
- caption/列: Figure 2
- 周辺文脈（EN）: Examine how well the leave-one-out predictive probabilities (computed with loo_epred() ) are calibrated using PAV-adjusted calibration plot ( Dimitriadis, Gneiting, and Jordan 2021
- 周辺文脈（JA, 自動訳）: 4.3 予測キャリブレーションチェック / PAV 調整キャリブレーションプロットを使用して、リーブワンアウト予測確率 (loo_epred() で計算) がどの程度適切にキャリブレーションされているかを検査します (Dimitriadis、Gneiting、Jordan 2021)
- Workflowフェーズ: **Posterior predictive checking / calibration**
- 実務での読み方: モデルが再現すべき特徴を外していないか確認する。PPC統計量と図をartifact化し、モデル改善の根拠にする。
- MLflow連携: `ppc_stat_*, loo_pit_ecdf_maxdev, calibration_error, replicated_seed`
- 参照: [公式ページ](https://avehtari.github.io/Bayesian-Workflow/dogs/dogs.html#fig-calib-0h) / [ソース候補](https://github.com/avehtari/Bayesian-Workflow/blob/eb00fa4397314ef7d90203382542bd44c590e289/dogs/dogs.R)

#### `dogs-dogs/fig-ppc_pava_residual-0h`

- 種別: `figure` / 公式ID: `fig-ppc_pava_residual-0h` / ページ内順序: 3
- caption/列: Figure 3
- 周辺文脈（EN）: PAV-adjusted residual plot looks reasonable.
- 周辺文脈（JA, 自動訳）: 4.4 残差プロット / PAV 調整済み残差プロットは合理的であるように見えます。
- Workflowフェーズ: **Posterior predictive checking / calibration**
- 実務での読み方: モデルが再現すべき特徴を外していないか確認する。PPC統計量と図をartifact化し、モデル改善の根拠にする。
- MLflow連携: `ppc_stat_*, loo_pit_ecdf_maxdev, calibration_error, replicated_seed`
- 参照: [公式ページ](https://avehtari.github.io/Bayesian-Workflow/dogs/dogs.html#fig-ppc_pava_residual-0h) / [ソース候補](https://github.com/avehtari/Bayesian-Workflow/blob/eb00fa4397314ef7d90203382542bd44c590e289/dogs/dogs.R)

#### `dogs-dogs/fig-ppc_shocks-0h`

- 種別: `figure` / 公式ID: `fig-ppc_shocks-0h` / ページ内順序: 4
- caption/列: Figure 4
- 周辺文脈（EN）: Visual posterior predictive checking plotting predicted shocks and avoidances by ordering the dogs with last observed shock.
- 周辺文脈（JA, 自動訳）: 4.5 事後予測チェック / 視覚的な事後予測チェックは、最後にショックが観察された犬に順序を付けることによって、予測されたショックと回避をプロットします。
- Workflowフェーズ: **EDA / observed data**
- 実務での読み方: モデル化前に、観測単位・外れ値・欠測・群構造・時系列性・上限/下限などを確認する。MLflowではデータ版と前処理版を固定する。
- MLflow連携: `dataset_uri, dataset_hash, preprocessing_version, n_obs, group_count`
- 参照: [公式ページ](https://avehtari.github.io/Bayesian-Workflow/dogs/dogs.html#fig-ppc_shocks-0h) / [ソース候補](https://github.com/avehtari/Bayesian-Workflow/blob/eb00fa4397314ef7d90203382542bd44c590e289/dogs/dogs.R)

#### `dogs-dogs/fig-ppc-mean_switches-0h`

- 種別: `figure` / 公式ID: `fig-ppc-mean_switches-0h` / ページ内順序: 5
- caption/列: Figure 5
- 周辺文脈（EN）: Posterior predictive checking using mean number of switches between shocks and avoidances as the test statistic.
- 周辺文脈（JA, 自動訳）: 4.5 事後予測チェック / 衝撃と回避の間の切り替えの平均数を検定統計量として使用する事後予測チェック。
- Workflowフェーズ: **Posterior predictive checking / calibration**
- 実務での読み方: モデルが再現すべき特徴を外していないか確認する。PPC統計量と図をartifact化し、モデル改善の根拠にする。
- MLflow連携: `ppc_stat_*, loo_pit_ecdf_maxdev, calibration_error, replicated_seed`
- 参照: [公式ページ](https://avehtari.github.io/Bayesian-Workflow/dogs/dogs.html#fig-ppc-mean_switches-0h) / [ソース候補](https://github.com/avehtari/Bayesian-Workflow/blob/eb00fa4397314ef7d90203382542bd44c590e289/dogs/dogs.R)

#### `dogs-dogs/fig-pred9-4`

- 種別: `figure` / 公式ID: `fig-pred9-4` / ページ内順序: 6
- caption/列: Figure 6
- 周辺文脈（EN）: Visualize the model fit for 9 first dogs. These look different from the logistic regression. Specifically we tend to see a sharper drop after the first avoidance, which makes sense
- 周辺文脈（JA, 自動訳）: 8.2 予測の視覚化 / 最初の 9 頭の犬に適合するモデルを視覚化します。これらはロジスティック回帰とは異なるように見えます。具体的には、最初の回避後に急激な低下が見られる傾向がありますが、これは理にかなっています。
- Workflowフェーズ: **Posterior predictive checking / calibration**
- 実務での読み方: モデルが再現すべき特徴を外していないか確認する。PPC統計量と図をartifact化し、モデル改善の根拠にする。
- MLflow連携: `ppc_stat_*, loo_pit_ecdf_maxdev, calibration_error, replicated_seed`
- 参照: [公式ページ](https://avehtari.github.io/Bayesian-Workflow/dogs/dogs.html#fig-pred9-4) / [ソース候補](https://github.com/avehtari/Bayesian-Workflow/blob/eb00fa4397314ef7d90203382542bd44c590e289/dogs/dogs.R)

#### `dogs-dogs/fig-pred9-2`

- 種別: `figure` / 公式ID: `fig-pred9-2` / ページ内順序: 7
- caption/列: Figure 7
- 周辺文脈（EN）: We can compare these two the predictions from the non-hierarchial 2-parameter log model, and we can see that even if the model is non-hierarchical, dog-specific number of shocks an
- 周辺文脈（JA, 自動訳）: 8.2 予測の視覚化 / これら 2 つを非階層 2 パラメーター対数モデルからの予測と比較できます。モデルが非階層であっても、犬に特有のショックの数は、
- Workflowフェーズ: **Posterior predictive checking / calibration**
- 実務での読み方: モデルが再現すべき特徴を外していないか確認する。PPC統計量と図をartifact化し、モデル改善の根拠にする。
- MLflow連携: `ppc_stat_*, loo_pit_ecdf_maxdev, calibration_error, replicated_seed`
- 参照: [公式ページ](https://avehtari.github.io/Bayesian-Workflow/dogs/dogs.html#fig-pred9-2) / [ソース候補](https://github.com/avehtari/Bayesian-Workflow/blob/eb00fa4397314ef7d90203382542bd44c590e289/dogs/dogs.R)

#### `dogs-dogs/fig-calib-4`

- 種別: `figure` / 公式ID: `fig-calib-4` / ページ内順序: 8
- caption/列: Figure 8
- 周辺文脈（EN）: Examine how well the leave-one-out predictive probabilities from hierarchical 2-parameter log model are calibrated. Looks quite good.
- 周辺文脈（JA, 自動訳）: 8.3 予測校正チェック / 階層型 2 パラメーター対数モデルからの 1 つ抜き予測確率がどの程度適切に校正されているかを検査します。見た目はかなり良いです。
- Workflowフェーズ: **Posterior predictive checking / calibration**
- 実務での読み方: モデルが再現すべき特徴を外していないか確認する。PPC統計量と図をartifact化し、モデル改善の根拠にする。
- MLflow連携: `ppc_stat_*, loo_pit_ecdf_maxdev, calibration_error, replicated_seed`
- 参照: [公式ページ](https://avehtari.github.io/Bayesian-Workflow/dogs/dogs.html#fig-calib-4) / [ソース候補](https://github.com/avehtari/Bayesian-Workflow/blob/eb00fa4397314ef7d90203382542bd44c590e289/dogs/dogs.R)

#### `dogs-dogs/fig-ppc_pava_residual-4`

- 種別: `figure` / 公式ID: `fig-ppc_pava_residual-4` / ページ内順序: 9
- caption/列: Figure 9
- 周辺文脈（EN）: PAV-adjusted residual plot looks reasonable.
- 周辺文脈（JA, 自動訳）: 8.4 残差プロット / PAV 調整済み残差プロットは合理的であるように見えます。
- Workflowフェーズ: **Posterior predictive checking / calibration**
- 実務での読み方: モデルが再現すべき特徴を外していないか確認する。PPC統計量と図をartifact化し、モデル改善の根拠にする。
- MLflow連携: `ppc_stat_*, loo_pit_ecdf_maxdev, calibration_error, replicated_seed`
- 参照: [公式ページ](https://avehtari.github.io/Bayesian-Workflow/dogs/dogs.html#fig-ppc_pava_residual-4) / [ソース候補](https://github.com/avehtari/Bayesian-Workflow/blob/eb00fa4397314ef7d90203382542bd44c590e289/dogs/dogs.R)

#### `dogs-dogs/fig-ppc_shocks-4`

- 種別: `figure` / 公式ID: `fig-ppc_shocks-4` / ページ内順序: 10
- caption/列: Figure 10
- 周辺文脈（EN）: Visual posterior predictive checking
- 周辺文脈（JA, 自動訳）: 8.5 事後予測チェック / 視覚的な事後予測チェック
- Workflowフェーズ: **Posterior predictive checking / calibration**
- 実務での読み方: モデルが再現すべき特徴を外していないか確認する。PPC統計量と図をartifact化し、モデル改善の根拠にする。
- MLflow連携: `ppc_stat_*, loo_pit_ecdf_maxdev, calibration_error, replicated_seed`
- 参照: [公式ページ](https://avehtari.github.io/Bayesian-Workflow/dogs/dogs.html#fig-ppc_shocks-4) / [ソース候補](https://github.com/avehtari/Bayesian-Workflow/blob/eb00fa4397314ef7d90203382542bd44c590e289/dogs/dogs.R)

#### `dogs-dogs/fig-ppc_mean_switches-4`

- 種別: `figure` / 公式ID: `fig-ppc_mean_switches-4` / ページ内順序: 11
- caption/列: Figure 11
- 周辺文脈（EN）: Posterior predictive checking using mean number of switches between shocks and avoidances as the test statistic.
- 周辺文脈（JA, 自動訳）: 8.5 事後予測チェック / 衝撃と回避の間の切り替えの平均数を検定統計量として使用する事後予測チェック。
- Workflowフェーズ: **Posterior predictive checking / calibration**
- 実務での読み方: モデルが再現すべき特徴を外していないか確認する。PPC統計量と図をartifact化し、モデル改善の根拠にする。
- MLflow連携: `ppc_stat_*, loo_pit_ecdf_maxdev, calibration_error, replicated_seed`
- 参照: [公式ページ](https://avehtari.github.io/Bayesian-Workflow/dogs/dogs.html#fig-ppc_mean_switches-4) / [ソース候補](https://github.com/avehtari/Bayesian-Workflow/blob/eb00fa4397314ef7d90203382542bd44c590e289/dogs/dogs.R)

#### `dogs-dogs/fig-pred-0h-4`

- 種別: `figure` / 公式ID: `fig-pred-0h-4` / ページ内順序: 12
- caption/列: Figure 12
- 周辺文脈（EN）: We can compare the posterior predictions by overlaying them in the same plot. We see the biggest difference is visible in time t=2 , but the differences are that small that given t
- 周辺文脈（JA, 自動訳）: 9 事後予測の比較 / 同じプロット内に事後予測を重ねて比較できます。最大の違いは時間 t=2 に見られますが、その違いは t を考慮した場合にはそれほど小さいものではありません。
- Workflowフェーズ: **Posterior predictive checking / calibration**
- 実務での読み方: モデルが再現すべき特徴を外していないか確認する。PPC統計量と図をartifact化し、モデル改善の根拠にする。
- MLflow連携: `ppc_stat_*, loo_pit_ecdf_maxdev, calibration_error, replicated_seed`
- 参照: [公式ページ](https://avehtari.github.io/Bayesian-Workflow/dogs/dogs.html#fig-pred-0h-4) / [ソース候補](https://github.com/avehtari/Bayesian-Workflow/blob/eb00fa4397314ef7d90203382542bd44c590e289/dogs/dogs.R)

#### `dogs-dogs/fig-mcmc_areas-4`

- 種別: `figure` / 公式ID: `fig-mcmc_areas-4` / ページ内順序: 13
- caption/列: Figure 13
- 周辺文脈（EN）: One assumption about the 2-parameter log model is that if the posteriors of a and b are different, then the dogs learn a different amount from shocks and avoidances.
- 周辺文脈（JA, 自動訳）: 11 データは 2 パラメーター対数モデルの 2 つのパラメーターに関する情報を提供しますか? / 2 パラメーター対数モデルに関する 1 つの仮定は、a と b の事後値が異なる場合、犬はショックと回避から異なる量を学習するということです。
- Workflowフェーズ: **EDA / observed data**
- 実務での読み方: モデル化前に、観測単位・外れ値・欠測・群構造・時系列性・上限/下限などを確認する。MLflowではデータ版と前処理版を固定する。
- MLflow連携: `dataset_uri, dataset_hash, preprocessing_version, n_obs, group_count`
- 参照: [公式ページ](https://avehtari.github.io/Bayesian-Workflow/dogs/dogs.html#fig-mcmc_areas-4) / [ソース候補](https://github.com/avehtari/Bayesian-Workflow/blob/eb00fa4397314ef7d90203382542bd44c590e289/dogs/dogs.R)

#### `dogs-dogs/fig-mcmc_areas-4s`

- 種別: `figure` / 公式ID: `fig-mcmc_areas-4s` / ページ内順序: 14
- caption/列: Figure 14
- 周辺文脈（EN）: The posterior for a and b are different!
- 周辺文脈（JA, 自動訳）: 11 データは 2 パラメーター対数モデルの 2 つのパラメーターに関する情報を提供しますか? ／aとbでは後が違う！
- Workflowフェーズ: **EDA / observed data**
- 実務での読み方: モデル化前に、観測単位・外れ値・欠測・群構造・時系列性・上限/下限などを確認する。MLflowではデータ版と前処理版を固定する。
- MLflow連携: `dataset_uri, dataset_hash, preprocessing_version, n_obs, group_count`
- 参照: [公式ページ](https://avehtari.github.io/Bayesian-Workflow/dogs/dogs.html#fig-mcmc_areas-4s) / [ソース候補](https://github.com/avehtari/Bayesian-Workflow/blob/eb00fa4397314ef7d90203382542bd44c590e289/dogs/dogs.R)

#### `dogs-dogs/fig-mcmc_areas-4sh`

- 種別: `figure` / 公式ID: `fig-mcmc_areas-4sh` / ページ内順序: 15
- caption/列: Figure 15
- 周辺文脈（EN）: The posterior for a and b are different!
- 周辺文脈（JA, 自動訳）: 11 データは 2 パラメーター対数モデルの 2 つのパラメーターに関する情報を提供しますか? ／aとbでは後が違う！
- Workflowフェーズ: **EDA / observed data**
- 実務での読み方: モデル化前に、観測単位・外れ値・欠測・群構造・時系列性・上限/下限などを確認する。MLflowではデータ版と前処理版を固定する。
- MLflow連携: `dataset_uri, dataset_hash, preprocessing_version, n_obs, group_count`
- 参照: [公式ページ](https://avehtari.github.io/Bayesian-Workflow/dogs/dogs.html#fig-mcmc_areas-4sh) / [ソース候補](https://github.com/avehtari/Bayesian-Workflow/blob/eb00fa4397314ef7d90203382542bd44c590e289/dogs/dogs.R)

#### `dogs-dogs/tinytable_cfgv55zn76pj13zi3rid`

- 種別: `table` / 公式ID: `tinytable_cfgv55zn76pj13zi3rid` / ページ内順序: 1
- caption/列: model; elpd_diff; se_diff; bfit_0h; 0; 0; bfit_0; -13
- 周辺文脈（EN）: We compare the simple and hierarchical logistic regression using PSIS-LOO-CV ( Vehtari, Gelman, and Gabry 2017 ) , and as the latter is clearly better, we can skip model checking f
- 周辺文脈（JA, 自動訳）: 4.1 モデルの比較 / PSIS-LOO-CV (Vehtari, Gelman, and Gabry 2017) を使用して単純ロジスティック回帰と階層ロジスティック回帰を比較します。後者の方が明らかに優れているため、モデル チェックを省略できます。
- Workflowフェーズ: **Posterior predictive checking / calibration**
- 実務での読み方: モデルが再現すべき特徴を外していないか確認する。PPC統計量と図をartifact化し、モデル改善の根拠にする。
- MLflow連携: `ppc_stat_*, loo_pit_ecdf_maxdev, calibration_error, replicated_seed`
- 参照: [公式ページ](https://avehtari.github.io/Bayesian-Workflow/dogs/dogs.html#tinytable_cfgv55zn76pj13zi3rid) / [ソース候補](https://github.com/avehtari/Bayesian-Workflow/blob/eb00fa4397314ef7d90203382542bd44c590e289/dogs/dogs.R)

#### `dogs-dogs/tinytable_gbhg98pu8rkcb1u0hc8g`

- 種別: `table` / 公式ID: `tinytable_gbhg98pu8rkcb1u0hc8g` / ページ内順序: 2
- caption/列: variable; prior; likelihood; diagnosis; b_Intercept; 0.01; 0.18; -
- 周辺文脈（EN）: Using priorsense package for powerscaling prior-likelihood sensitivity analysis ( Kallioinen et al. 2023 ) shows that the data are informative and there is no need to think more ab
- 周辺文脈（JA, 自動訳）: 4.6 事前尤度感度分析 / パワースケーリング事前尤度感度分析に Priorsense パッケージを使用する (Kallioinen et al. 2023) と、データが有益であり、より厳密に考える必要がないことが示されています。
- Workflowフェーズ: **EDA / observed data**
- 実務での読み方: モデル化前に、観測単位・外れ値・欠測・群構造・時系列性・上限/下限などを確認する。MLflowではデータ版と前処理版を固定する。
- MLflow連携: `dataset_uri, dataset_hash, preprocessing_version, n_obs, group_count`
- 参照: [公式ページ](https://avehtari.github.io/Bayesian-Workflow/dogs/dogs.html#tinytable_gbhg98pu8rkcb1u0hc8g) / [ソース候補](https://github.com/avehtari/Bayesian-Workflow/blob/eb00fa4397314ef7d90203382542bd44c590e289/dogs/dogs.R)

#### `dogs-dogs/tinytable_6qtwr217ixldxk6t6q3m`

- 種別: `table` / 公式ID: `tinytable_6qtwr217ixldxk6t6q3m` / ページ内順序: 3
- caption/列: model; elpd_diff; se_diff; bfit_0h; 0; 0; bfit_0; -13
- 周辺文脈（EN）: PSIS-LOO-CV comparison shows that the 1-parameter log model is worse than either logistic regression model. Thus we don’t examine it further and move to more elaborate log models.
- 周辺文脈（JA, 自動訳）: 5.1 モデル比較 / PSIS-LOO-CV 比較は、1 パラメーター対数モデルがどちらのロジスティック回帰モデルよりも劣っていることを示しています。したがって、これ以上は調査せず、より複雑なログ モデルに移行します。
- Workflowフェーズ: **Posterior predictive checking / calibration**
- 実務での読み方: モデルが再現すべき特徴を外していないか確認する。PPC統計量と図をartifact化し、モデル改善の根拠にする。
- MLflow連携: `ppc_stat_*, loo_pit_ecdf_maxdev, calibration_error, replicated_seed`
- 参照: [公式ページ](https://avehtari.github.io/Bayesian-Workflow/dogs/dogs.html#tinytable_6qtwr217ixldxk6t6q3m) / [ソース候補](https://github.com/avehtari/Bayesian-Workflow/blob/eb00fa4397314ef7d90203382542bd44c590e289/dogs/dogs.R)

#### `dogs-dogs/tinytable_q4bghmc5jfoy64qb4uo6`

- 種別: `table` / 公式ID: `tinytable_q4bghmc5jfoy64qb4uo6` / ページ内順序: 4
- caption/列: model; elpd_diff; se_diff; bfit_0h; 0; 0; bfit_2; -4.7
- 周辺文脈（EN）: PSIS-LOO-CV comparison shows that the 2-parameter log model is worse than the hierarchical logistic regression model, but not significantly. We don’t examine this model further, as
- 周辺文脈（JA, 自動訳）: 6.1 モデルの比較 / PSIS-LOO-CV の比較は、2 パラメーター対数モデルが階層型ロジスティック回帰モデルよりも劣っていることを示していますが、有意ではありません。このモデルについてはこれ以上調査しません。
- Workflowフェーズ: **Posterior predictive checking / calibration**
- 実務での読み方: モデルが再現すべき特徴を外していないか確認する。PPC統計量と図をartifact化し、モデル改善の根拠にする。
- MLflow連携: `ppc_stat_*, loo_pit_ecdf_maxdev, calibration_error, replicated_seed`
- 参照: [公式ページ](https://avehtari.github.io/Bayesian-Workflow/dogs/dogs.html#tinytable_q4bghmc5jfoy64qb4uo6) / [ソース候補](https://github.com/avehtari/Bayesian-Workflow/blob/eb00fa4397314ef7d90203382542bd44c590e289/dogs/dogs.R)

#### `dogs-dogs/tinytable_hqg2z105mpas3bgir1se`

- 種別: `table` / 公式ID: `tinytable_hqg2z105mpas3bgir1se` / ページ内順序: 5
- caption/列: model; elpd_diff; se_diff; bfit_0h; 0; 0; bfit_2; -4.7
- 周辺文脈（EN）: PSIS-LOO-CV comparison shows that the hierarchical 1-parameter log model is worse than the hierarchcial logistic regression model and non-hierarchcial 2-parameter log model, and th
- 周辺文脈（JA, 自動訳）: 7.1 モデル比較 / PSIS-LOO-CV 比較は、階層 1 パラメーター対数モデルが階層ロジスティック回帰モデルおよび非階層 2 パラメーター対数モデルよりも劣っていることを示しています。
- Workflowフェーズ: **Posterior predictive checking / calibration**
- 実務での読み方: モデルが再現すべき特徴を外していないか確認する。PPC統計量と図をartifact化し、モデル改善の根拠にする。
- MLflow連携: `ppc_stat_*, loo_pit_ecdf_maxdev, calibration_error, replicated_seed`
- 参照: [公式ページ](https://avehtari.github.io/Bayesian-Workflow/dogs/dogs.html#tinytable_hqg2z105mpas3bgir1se) / [ソース候補](https://github.com/avehtari/Bayesian-Workflow/blob/eb00fa4397314ef7d90203382542bd44c590e289/dogs/dogs.R)

#### `dogs-dogs/tinytable_qvaumab6djwic3171943`

- 種別: `table` / 公式ID: `tinytable_qvaumab6djwic3171943` / ページ内順序: 6
- caption/列: model; elpd_diff; se_diff; bfit_0h; 0; 0; bfit_4; -3.8
- 周辺文脈（EN）: PSIS-LOO-CV comparison shows that hierarchical 2-parameter log model is worse than the hierarchical logistic regression, although not significantly. While adding hierarchy to logis
- 周辺文脈（JA, 自動訳）: 8.1 モデルの比較 / PSIS-LOO-CV の比較は、階層 2 パラメーター対数モデルが階層ロジスティック回帰よりも、有意ではないものの劣っていることを示しています。ロジに階層を追加するとき
- Workflowフェーズ: **Posterior predictive checking / calibration**
- 実務での読み方: モデルが再現すべき特徴を外していないか確認する。PPC統計量と図をartifact化し、モデル改善の根拠にする。
- MLflow連携: `ppc_stat_*, loo_pit_ecdf_maxdev, calibration_error, replicated_seed`
- 参照: [公式ページ](https://avehtari.github.io/Bayesian-Workflow/dogs/dogs.html#tinytable_qvaumab6djwic3171943) / [ソース候補](https://github.com/avehtari/Bayesian-Workflow/blob/eb00fa4397314ef7d90203382542bd44c590e289/dogs/dogs.R)

#### `dogs-dogs/tinytable_90cltwasbblxau872a37`

- 種別: `table` / 公式ID: `tinytable_90cltwasbblxau872a37` / ページ内順序: 7
- caption/列: variable; prior; likelihood; diagnosis; b_etaa_Intercept; 0.01; 0.14; -
- 周辺文脈（EN）: Using priorsense package for prior-likelihood sensitivity analysis shows that the data are informative and there is no need to think more about priors unless we do happen to have e
- 周辺文脈（JA, 自動訳）: 8.6 事前尤度感度分析 / 事前尤度感度分析に prioritysense パッケージを使用すると、データが有益であり、たまたま e が存在しない限り、事前確率についてさらに考える必要がないことがわかります。
- Workflowフェーズ: **EDA / observed data**
- 実務での読み方: モデル化前に、観測単位・外れ値・欠測・群構造・時系列性・上限/下限などを確認する。MLflowではデータ版と前処理版を固定する。
- MLflow連携: `dataset_uri, dataset_hash, preprocessing_version, n_obs, group_count`
- 参照: [公式ページ](https://avehtari.github.io/Bayesian-Workflow/dogs/dogs.html#tinytable_90cltwasbblxau872a37) / [ソース候補](https://github.com/avehtari/Bayesian-Workflow/blob/eb00fa4397314ef7d90203382542bd44c590e289/dogs/dogs.R)

#### `dogs-dogs/tinytable_pyyhatcj0gqfjexghkxn`

- 種別: `table` / 公式ID: `tinytable_pyyhatcj0gqfjexghkxn` / ページ内順序: 8
- caption/列: model; elpd_diff; se_diff; bfit_4; 0; 0; bfit_0h; -2.3
- 周辺文脈（EN）: There is no difference in predictive performance between the hierarchical logistic regression and hierarchical log model.
- 周辺文脈（JA, 自動訳）: 10 将来除外相互検証 / 階層型ロジスティック回帰と階層型対数モデルの間で予測パフォーマンスに違いはありません。
- Workflowフェーズ: **Posterior predictive checking / calibration**
- 実務での読み方: モデルが再現すべき特徴を外していないか確認する。PPC統計量と図をartifact化し、モデル改善の根拠にする。
- MLflow連携: `ppc_stat_*, loo_pit_ecdf_maxdev, calibration_error, replicated_seed`
- 参照: [公式ページ](https://avehtari.github.io/Bayesian-Workflow/dogs/dogs.html#tinytable_pyyhatcj0gqfjexghkxn) / [ソース候補](https://github.com/avehtari/Bayesian-Workflow/blob/eb00fa4397314ef7d90203382542bd44c590e289/dogs/dogs.R)

### Posterior predictive checking: Stochastic learning in dogs

- ページ: <https://avehtari.github.io/Bayesian-Workflow/dogs/dogs_stan.html>
- ソース候補: <https://github.com/avehtari/Bayesian-Workflow/blob/eb00fa4397314ef7d90203382542bd44c590e289/dogs/dogs_stan.R>

#### `dogs-dogs-stan/fig-dogs_ppc`

- 種別: `figure` / 公式ID: `fig-dogs_ppc` / ページ内順序: 1
- caption/列: Figure 1
- 周辺文脈（EN）: Load packages
- 周辺文脈（JA, 自動訳）: 4 プロット / パッケージのロード
- Workflowフェーズ: **Posterior predictive checking / calibration**
- 実務での読み方: モデルが再現すべき特徴を外していないか確認する。PPC統計量と図をartifact化し、モデル改善の根拠にする。
- MLflow連携: `ppc_stat_*, loo_pit_ecdf_maxdev, calibration_error, replicated_seed`
- 参照: [公式ページ](https://avehtari.github.io/Bayesian-Workflow/dogs/dogs_stan.html#fig-dogs_ppc) / [ソース候補](https://github.com/avehtari/Bayesian-Workflow/blob/eb00fa4397314ef7d90203382542bd44c590e289/dogs/dogs_stan.R)

#### `dogs-dogs-stan/fig-dogs_inference`

- 種別: `figure` / 公式ID: `fig-dogs_inference` / ページ内順序: 2
- caption/列: Figure 2
- 周辺文脈（EN）: Load packages
- 周辺文脈（JA, 自動訳）: 4 プロット / パッケージのロード
- Workflowフェーズ: **Posterior predictive checking / calibration**
- 実務での読み方: モデルが再現すべき特徴を外していないか確認する。PPC統計量と図をartifact化し、モデル改善の根拠にする。
- MLflow連携: `ppc_stat_*, loo_pit_ecdf_maxdev, calibration_error, replicated_seed`
- 参照: [公式ページ](https://avehtari.github.io/Bayesian-Workflow/dogs/dogs_stan.html#fig-dogs_inference) / [ソース候補](https://github.com/avehtari/Bayesian-Workflow/blob/eb00fa4397314ef7d90203382542bd44c590e289/dogs/dogs_stan.R)

#### `dogs-dogs-stan/fig-dogs_point_estimate`

- 種別: `figure` / 公式ID: `fig-dogs_point_estimate` / ページ内順序: 3
- caption/列: Figure 3
- 周辺文脈（EN）: Load packages
- 周辺文脈（JA, 自動訳）: 4 プロット / パッケージのロード
- Workflowフェーズ: **Posterior predictive checking / calibration**
- 実務での読み方: モデルが再現すべき特徴を外していないか確認する。PPC統計量と図をartifact化し、モデル改善の根拠にする。
- MLflow連携: `ppc_stat_*, loo_pit_ecdf_maxdev, calibration_error, replicated_seed`
- 参照: [公式ページ](https://avehtari.github.io/Bayesian-Workflow/dogs/dogs_stan.html#fig-dogs_point_estimate) / [ソース候補](https://github.com/avehtari/Bayesian-Workflow/blob/eb00fa4397314ef7d90203382542bd44c590e289/dogs/dogs_stan.R)

#### `dogs-dogs-stan/fig-dogs_parameters`

- 種別: `figure` / 公式ID: `fig-dogs_parameters` / ページ内順序: 4
- caption/列: Figure 4
- 周辺文脈（EN）: Load packages
- 周辺文脈（JA, 自動訳）: 4 プロット / パッケージのロード
- Workflowフェーズ: **Posterior predictive checking / calibration**
- 実務での読み方: モデルが再現すべき特徴を外していないか確認する。PPC統計量と図をartifact化し、モデル改善の根拠にする。
- MLflow連携: `ppc_stat_*, loo_pit_ecdf_maxdev, calibration_error, replicated_seed`
- 参照: [公式ページ](https://avehtari.github.io/Bayesian-Workflow/dogs/dogs_stan.html#fig-dogs_parameters) / [ソース候補](https://github.com/avehtari/Bayesian-Workflow/blob/eb00fa4397314ef7d90203382542bd44c590e289/dogs/dogs_stan.R)

#### `dogs-dogs-stan/fig-dogs_data`

- 種別: `figure` / 公式ID: `fig-dogs_data` / ページ内順序: 5
- caption/列: Figure 5
- 周辺文脈（EN）: Load packages
- 周辺文脈（JA, 自動訳）: 4 プロット / パッケージのロード
- Workflowフェーズ: **Posterior predictive checking / calibration**
- 実務での読み方: モデルが再現すべき特徴を外していないか確認する。PPC統計量と図をartifact化し、モデル改善の根拠にする。
- MLflow連携: `ppc_stat_*, loo_pit_ecdf_maxdev, calibration_error, replicated_seed`
- 参照: [公式ページ](https://avehtari.github.io/Bayesian-Workflow/dogs/dogs_stan.html#fig-dogs_data) / [ソース候補](https://github.com/avehtari/Bayesian-Workflow/blob/eb00fa4397314ef7d90203382542bd44c590e289/dogs/dogs_stan.R)

#### `dogs-dogs-stan/fig-dogs_calibration`

- 種別: `figure` / 公式ID: `fig-dogs_calibration` / ページ内順序: 6
- caption/列: Figure 6
- 周辺文脈（EN）: Load packages
- 周辺文脈（JA, 自動訳）: 4 プロット / パッケージのロード
- Workflowフェーズ: **Posterior predictive checking / calibration**
- 実務での読み方: モデルが再現すべき特徴を外していないか確認する。PPC統計量と図をartifact化し、モデル改善の根拠にする。
- MLflow連携: `ppc_stat_*, loo_pit_ecdf_maxdev, calibration_error, replicated_seed`
- 参照: [公式ページ](https://avehtari.github.io/Bayesian-Workflow/dogs/dogs_stan.html#fig-dogs_calibration) / [ソース候補](https://github.com/avehtari/Bayesian-Workflow/blob/eb00fa4397314ef7d90203382542bd44c590e289/dogs/dogs_stan.R)

#### `dogs-dogs-stan/fig-dogs_data_50`

- 種別: `figure` / 公式ID: `fig-dogs_data_50` / ページ内順序: 7
- caption/列: Figure 7
- 周辺文脈（EN）: Load packages
- 周辺文脈（JA, 自動訳）: 4 プロット / パッケージのロード
- Workflowフェーズ: **Posterior predictive checking / calibration**
- 実務での読み方: モデルが再現すべき特徴を外していないか確認する。PPC統計量と図をartifact化し、モデル改善の根拠にする。
- MLflow連携: `ppc_stat_*, loo_pit_ecdf_maxdev, calibration_error, replicated_seed`
- 参照: [公式ページ](https://avehtari.github.io/Bayesian-Workflow/dogs/dogs_stan.html#fig-dogs_data_50) / [ソース候補](https://github.com/avehtari/Bayesian-Workflow/blob/eb00fa4397314ef7d90203382542bd44c590e289/dogs/dogs_stan.R)

#### `dogs-dogs-stan/fig-dogs_calibration_50`

- 種別: `figure` / 公式ID: `fig-dogs_calibration_50` / ページ内順序: 8
- caption/列: Figure 8
- 周辺文脈（EN）: Load packages
- 周辺文脈（JA, 自動訳）: 4 プロット / パッケージのロード
- Workflowフェーズ: **Posterior predictive checking / calibration**
- 実務での読み方: モデルが再現すべき特徴を外していないか確認する。PPC統計量と図をartifact化し、モデル改善の根拠にする。
- MLflow連携: `ppc_stat_*, loo_pit_ecdf_maxdev, calibration_error, replicated_seed`
- 参照: [公式ページ](https://avehtari.github.io/Bayesian-Workflow/dogs/dogs_stan.html#fig-dogs_calibration_50) / [ソース候補](https://github.com/avehtari/Bayesian-Workflow/blob/eb00fa4397314ef7d90203382542bd44c590e289/dogs/dogs_stan.R)

### Incremental development and testing: Black cat adoptions

- ページ: <https://avehtari.github.io/Bayesian-Workflow/cat_adoptions/cat_adoptions.html>
- ソース候補: <https://github.com/avehtari/Bayesian-Workflow/blob/eb00fa4397314ef7d90203382542bd44c590e289/cat_adoptions/cat_adoptions.R>

#### `cat-adoptions-cat-adoptions/fig-cats-data`

- 種別: `figure` / 公式ID: `fig-cats-data` / ページ内順序: 1
- caption/列: Figure 1
- 周辺文脈（EN）: Plot individual cats as lines
- 周辺文脈（JA, 自動訳）: 2 データ / 個々の猫を線としてプロットする
- Workflowフェーズ: **EDA / observed data**
- 実務での読み方: モデル化前に、観測単位・外れ値・欠測・群構造・時系列性・上限/下限などを確認する。MLflowではデータ版と前処理版を固定する。
- MLflow連携: `dataset_uri, dataset_hash, preprocessing_version, n_obs, group_count`
- 参照: [公式ページ](https://avehtari.github.io/Bayesian-Workflow/cat_adoptions/cat_adoptions.html#fig-cats-data) / [ソース候補](https://github.com/avehtari/Bayesian-Workflow/blob/eb00fa4397314ef7d90203382542bd44c590e289/cat_adoptions/cat_adoptions.R)

#### `cat-adoptions-cat-adoptions/fig-gg-cats-data`

- 種別: `figure` / 公式ID: `fig-gg-cats-data` / ページ内順序: 2
- caption/列: Figure 2
- 周辺文脈（EN）: ggplot version
- 周辺文脈（JA, 自動訳）: 2 データ/ggplot バージョン
- Workflowフェーズ: **EDA / observed data**
- 実務での読み方: モデル化前に、観測単位・外れ値・欠測・群構造・時系列性・上限/下限などを確認する。MLflowではデータ版と前処理版を固定する。
- MLflow連携: `dataset_uri, dataset_hash, preprocessing_version, n_obs, group_count`
- 参照: [公式ページ](https://avehtari.github.io/Bayesian-Workflow/cat_adoptions/cat_adoptions.html#fig-gg-cats-data) / [ソース候補](https://github.com/avehtari/Bayesian-Workflow/blob/eb00fa4397314ef7d90203382542bd44c590e289/cat_adoptions/cat_adoptions.R)

#### `cat-adoptions-cat-adoptions/fig-cats-km-curves`

- 種別: `figure` / 公式ID: `fig-cats-km-curves` / ページ内順序: 3
- caption/列: Figure 3
- 周辺文脈（EN）: Plot empirical K-M curves
- 周辺文脈（JA, 自動訳）: 3 生成モデル / 経験的な K-M 曲線のプロット
- Workflowフェーズ: **Model development / debugging**
- 実務での読み方: 小さいモデルから始め、失敗runを観察しながらモデル族・prior・データ処理を段階的に拡張する。
- MLflow連携: `iteration_id, change_reason, failure_mode, hypothesis, next_action`
- 参照: [公式ページ](https://avehtari.github.io/Bayesian-Workflow/cat_adoptions/cat_adoptions.html#fig-cats-km-curves) / [ソース候補](https://github.com/avehtari/Bayesian-Workflow/blob/eb00fa4397314ef7d90203382542bd44c590e289/cat_adoptions/cat_adoptions.R)

#### `cat-adoptions-cat-adoptions/fig-gg-cats-km-curves`

- 種別: `figure` / 公式ID: `fig-gg-cats-km-curves` / ページ内順序: 4
- caption/列: Figure 4
- 周辺文脈（EN）: Plot empirical K-M curves using ggplot
- 周辺文脈（JA, 自動訳）: 3 生成モデル / ggplot を使用して経験的な K-M 曲線をプロットする
- Workflowフェーズ: **Model development / debugging**
- 実務での読み方: 小さいモデルから始め、失敗runを観察しながらモデル族・prior・データ処理を段階的に拡張する。
- MLflow連携: `iteration_id, change_reason, failure_mode, hypothesis, next_action`
- 参照: [公式ページ](https://avehtari.github.io/Bayesian-Workflow/cat_adoptions/cat_adoptions.html#fig-gg-cats-km-curves) / [ソース候補](https://github.com/avehtari/Bayesian-Workflow/blob/eb00fa4397314ef7d90203382542bd44c590e289/cat_adoptions/cat_adoptions.R)

#### `cat-adoptions-cat-adoptions/fig-prior-predictive-1`

- 種別: `figure` / 公式ID: `fig-prior-predictive-1` / ページ内順序: 5
- caption/列: Figure 5
- 周辺文脈（EN）: Prior predictive simulation
- 周辺文脈（JA, 自動訳）: 3.1 最初のスタンモデル/事前予測シミュレーション
- Workflowフェーズ: **Prior / prior predictive**
- 実務での読み方: 事前分布が現実的なデータ範囲を生成するかを見る。現場導入前に、あり得ない予測の比率をゲート化する。
- MLflow連携: `prior_spec_id, prior_predictive_seed, simulated_n, implausible_rate`
- 参照: [公式ページ](https://avehtari.github.io/Bayesian-Workflow/cat_adoptions/cat_adoptions.html#fig-prior-predictive-1) / [ソース候補](https://github.com/avehtari/Bayesian-Workflow/blob/eb00fa4397314ef7d90203382542bd44c590e289/cat_adoptions/cat_adoptions.R)

#### `cat-adoptions-cat-adoptions/fig-gg-prior-predictive-1`

- 種別: `figure` / 公式ID: `fig-gg-prior-predictive-1` / ページ内順序: 6
- caption/列: Figure 6
- 周辺文脈（EN）: Prior predictive simulation with ggplot
- 周辺文脈（JA, 自動訳）: 3.1 最初の Stan モデル / ggplot による事前予測シミュレーション
- Workflowフェーズ: **Prior / prior predictive**
- 実務での読み方: 事前分布が現実的なデータ範囲を生成するかを見る。現場導入前に、あり得ない予測の比率をゲート化する。
- MLflow連携: `prior_spec_id, prior_predictive_seed, simulated_n, implausible_rate`
- 参照: [公式ページ](https://avehtari.github.io/Bayesian-Workflow/cat_adoptions/cat_adoptions.html#fig-gg-prior-predictive-1) / [ソース候補](https://github.com/avehtari/Bayesian-Workflow/blob/eb00fa4397314ef7d90203382542bd44c590e289/cat_adoptions/cat_adoptions.R)

#### `cat-adoptions-cat-adoptions/fig-post1-sim`

- 種別: `figure` / 公式ID: `fig-post1-sim` / ページ内順序: 7
- caption/列: Figure 7
- 周辺文脈（EN）: Posterior with simulated data
- 周辺文脈（JA, 自動訳）: 3.1 最初の Stan モデル / シミュレートされたデータによる事後解析
- Workflowフェーズ: **EDA / observed data**
- 実務での読み方: モデル化前に、観測単位・外れ値・欠測・群構造・時系列性・上限/下限などを確認する。MLflowではデータ版と前処理版を固定する。
- MLflow連携: `dataset_uri, dataset_hash, preprocessing_version, n_obs, group_count`
- 参照: [公式ページ](https://avehtari.github.io/Bayesian-Workflow/cat_adoptions/cat_adoptions.html#fig-post1-sim) / [ソース候補](https://github.com/avehtari/Bayesian-Workflow/blob/eb00fa4397314ef7d90203382542bd44c590e289/cat_adoptions/cat_adoptions.R)

#### `cat-adoptions-cat-adoptions/fig-gg-post1-sim`

- 種別: `figure` / 公式ID: `fig-gg-post1-sim` / ページ内順序: 8
- caption/列: Figure 8
- 周辺文脈（EN）: Posterior with simulated data with ggplot
- 周辺文脈（JA, 自動訳）: 3.1 最初の Stan モデル / ggplot によるシミュレートされたデータによる事後分布
- Workflowフェーズ: **EDA / observed data**
- 実務での読み方: モデル化前に、観測単位・外れ値・欠測・群構造・時系列性・上限/下限などを確認する。MLflowではデータ版と前処理版を固定する。
- MLflow連携: `dataset_uri, dataset_hash, preprocessing_version, n_obs, group_count`
- 参照: [公式ページ](https://avehtari.github.io/Bayesian-Workflow/cat_adoptions/cat_adoptions.html#fig-gg-post1-sim) / [ソース候補](https://github.com/avehtari/Bayesian-Workflow/blob/eb00fa4397314ef7d90203382542bd44c590e289/cat_adoptions/cat_adoptions.R)

#### `cat-adoptions-cat-adoptions/fig-post1-km`

- 種別: `figure` / 公式ID: `fig-post1-km` / ページ内順序: 9
- caption/列: Figure 9
- 周辺文脈（EN）: Kaplan-Meier posterior simulations
- 周辺文脈（JA, 自動訳）: 3.1 最初の Stan モデル / Kaplan-Meier 事後シミュレーション
- Workflowフェーズ: **Posterior summary / effect interpretation**
- 実務での読み方: 推定効果・不確実性・派生量を意思決定に接続する。平均だけでなく区間・分布・実務閾値超過確率を残す。
- MLflow連携: `posterior_draws_uri, model_code_hash, ci_width, decision_threshold_prob`
- 参照: [公式ページ](https://avehtari.github.io/Bayesian-Workflow/cat_adoptions/cat_adoptions.html#fig-post1-km) / [ソース候補](https://github.com/avehtari/Bayesian-Workflow/blob/eb00fa4397314ef7d90203382542bd44c590e289/cat_adoptions/cat_adoptions.R)

#### `cat-adoptions-cat-adoptions/fig-gg-post1-km`

- 種別: `figure` / 公式ID: `fig-gg-post1-km` / ページ内順序: 10
- caption/列: Figure 10
- 周辺文脈（EN）: Posterior Kaplan-Meier with ggplot
- 周辺文脈（JA, 自動訳）: 3.1 最初の Stan モデル / ggplot による事後カプランマイヤー
- Workflowフェーズ: **Posterior summary / effect interpretation**
- 実務での読み方: 推定効果・不確実性・派生量を意思決定に接続する。平均だけでなく区間・分布・実務閾値超過確率を残す。
- MLflow連携: `posterior_draws_uri, model_code_hash, ci_width, decision_threshold_prob`
- 参照: [公式ページ](https://avehtari.github.io/Bayesian-Workflow/cat_adoptions/cat_adoptions.html#fig-gg-post1-km) / [ソース候補](https://github.com/avehtari/Bayesian-Workflow/blob/eb00fa4397314ef7d90203382542bd44c590e289/cat_adoptions/cat_adoptions.R)

#### `cat-adoptions-cat-adoptions/fig-post2-sim`

- 種別: `figure` / 公式ID: `fig-post2-sim` / ページ内順序: 11
- caption/列: Figure 11
- 周辺文脈（EN）: Posterior summary
- 周辺文脈（JA, 自動訳）: 3.2 観測（打ち切り）モデルの追加 / 事後集計
- Workflowフェーズ: **Posterior summary / effect interpretation**
- 実務での読み方: 推定効果・不確実性・派生量を意思決定に接続する。平均だけでなく区間・分布・実務閾値超過確率を残す。
- MLflow連携: `posterior_draws_uri, model_code_hash, ci_width, decision_threshold_prob`
- 参照: [公式ページ](https://avehtari.github.io/Bayesian-Workflow/cat_adoptions/cat_adoptions.html#fig-post2-sim) / [ソース候補](https://github.com/avehtari/Bayesian-Workflow/blob/eb00fa4397314ef7d90203382542bd44c590e289/cat_adoptions/cat_adoptions.R)

#### `cat-adoptions-cat-adoptions/fig-gg-post2-sim`

- 種別: `figure` / 公式ID: `fig-gg-post2-sim` / ページ内順序: 12
- caption/列: Figure 12
- 周辺文脈（EN）: Posterior with simulated data with ggplot
- 周辺文脈（JA, 自動訳）: 3.2 ggplot による観測 (打ち切り) モデル / シミュレートされたデータによる事後分布の追加
- Workflowフェーズ: **EDA / observed data**
- 実務での読み方: モデル化前に、観測単位・外れ値・欠測・群構造・時系列性・上限/下限などを確認する。MLflowではデータ版と前処理版を固定する。
- MLflow連携: `dataset_uri, dataset_hash, preprocessing_version, n_obs, group_count`
- 参照: [公式ページ](https://avehtari.github.io/Bayesian-Workflow/cat_adoptions/cat_adoptions.html#fig-gg-post2-sim) / [ソース候補](https://github.com/avehtari/Bayesian-Workflow/blob/eb00fa4397314ef7d90203382542bd44c590e289/cat_adoptions/cat_adoptions.R)

#### `cat-adoptions-cat-adoptions/fig-post1-sim2`

- 種別: `figure` / 公式ID: `fig-post1-sim2` / ページ内順序: 13
- caption/列: Figure 13
- 周辺文脈（EN）: Test previous model with new censored data
- 周辺文脈（JA, 自動訳）: 3.2 観測 (打ち切り) モデルの追加 / 新しい打ち切りデータを使用して以前のモデルをテストする
- Workflowフェーズ: **EDA / observed data**
- 実務での読み方: モデル化前に、観測単位・外れ値・欠測・群構造・時系列性・上限/下限などを確認する。MLflowではデータ版と前処理版を固定する。
- MLflow連携: `dataset_uri, dataset_hash, preprocessing_version, n_obs, group_count`
- 参照: [公式ページ](https://avehtari.github.io/Bayesian-Workflow/cat_adoptions/cat_adoptions.html#fig-post1-sim2) / [ソース候補](https://github.com/avehtari/Bayesian-Workflow/blob/eb00fa4397314ef7d90203382542bd44c590e289/cat_adoptions/cat_adoptions.R)

#### `cat-adoptions-cat-adoptions/fig-gg-post1-sim2`

- 種別: `figure` / 公式ID: `fig-gg-post1-sim2` / ページ内順序: 14
- caption/列: Figure 14
- 周辺文脈（EN）: Posterior with simulated data with ggplot
- 周辺文脈（JA, 自動訳）: 3.2 ggplot による観測 (打ち切り) モデル / シミュレートされたデータによる事後分布の追加
- Workflowフェーズ: **EDA / observed data**
- 実務での読み方: モデル化前に、観測単位・外れ値・欠測・群構造・時系列性・上限/下限などを確認する。MLflowではデータ版と前処理版を固定する。
- MLflow連携: `dataset_uri, dataset_hash, preprocessing_version, n_obs, group_count`
- 参照: [公式ページ](https://avehtari.github.io/Bayesian-Workflow/cat_adoptions/cat_adoptions.html#fig-gg-post1-sim2) / [ソース候補](https://github.com/avehtari/Bayesian-Workflow/blob/eb00fa4397314ef7d90203382542bd44c590e289/cat_adoptions/cat_adoptions.R)

#### `cat-adoptions-cat-adoptions/fig-post1-post2-km`

- 種別: `figure` / 公式ID: `fig-post1-post2-km` / ページ内順序: 15
- caption/列: Figure 15
- 周辺文脈（EN）: Kaplan-meier posterior simulations
- 周辺文脈（JA, 自動訳）: 3.2 観察（打ち切り）モデル/カプランマイヤー事後シミュレーションの追加
- Workflowフェーズ: **Posterior summary / effect interpretation**
- 実務での読み方: 推定効果・不確実性・派生量を意思決定に接続する。平均だけでなく区間・分布・実務閾値超過確率を残す。
- MLflow連携: `posterior_draws_uri, model_code_hash, ci_width, decision_threshold_prob`
- 参照: [公式ページ](https://avehtari.github.io/Bayesian-Workflow/cat_adoptions/cat_adoptions.html#fig-post1-post2-km) / [ソース候補](https://github.com/avehtari/Bayesian-Workflow/blob/eb00fa4397314ef7d90203382542bd44c590e289/cat_adoptions/cat_adoptions.R)

#### `cat-adoptions-cat-adoptions/fig-gg-post2-km`

- 種別: `figure` / 公式ID: `fig-gg-post2-km` / ページ内順序: 16
- caption/列: Figure 16
- 周辺文脈（EN）: Kaplan-meier posterior simulations
- 周辺文脈（JA, 自動訳）: 3.2 観察（打ち切り）モデル/カプランマイヤー事後シミュレーションの追加
- Workflowフェーズ: **Posterior summary / effect interpretation**
- 実務での読み方: 推定効果・不確実性・派生量を意思決定に接続する。平均だけでなく区間・分布・実務閾値超過確率を残す。
- MLflow連携: `posterior_draws_uri, model_code_hash, ci_width, decision_threshold_prob`
- 参照: [公式ページ](https://avehtari.github.io/Bayesian-Workflow/cat_adoptions/cat_adoptions.html#fig-gg-post2-km) / [ソース候補](https://github.com/avehtari/Bayesian-Workflow/blob/eb00fa4397314ef7d90203382542bd44c590e289/cat_adoptions/cat_adoptions.R)

#### `cat-adoptions-cat-adoptions/figure-017`

- 種別: `figure` / 公式ID: `(none)` / ページ内順序: 17
- caption/列: figure 17
- 周辺文脈（EN）: Repeatedly sample from prior, simulate observations Prior draws
- 周辺文脈（JA, 自動訳）: 4.1 事前予測分布 / 過去から繰り返しサンプリングし、観測をシミュレートする 事前描画
- Workflowフェーズ: **Prior / prior predictive**
- 実務での読み方: 事前分布が現実的なデータ範囲を生成するかを見る。現場導入前に、あり得ない予測の比率をゲート化する。
- MLflow連携: `prior_spec_id, prior_predictive_seed, simulated_n, implausible_rate`
- 参照: [公式ページ](https://avehtari.github.io/Bayesian-Workflow/cat_adoptions/cat_adoptions.html) / [ソース候補](https://github.com/avehtari/Bayesian-Workflow/blob/eb00fa4397314ef7d90203382542bd44c590e289/cat_adoptions/cat_adoptions.R)

#### `cat-adoptions-cat-adoptions/fig-km-2`

- 種別: `figure` / 公式ID: `fig-km-2` / ページ内順序: 18
- caption/列: Figure 17
- 周辺文脈（EN）: Sample from posterior, simulate observations. Problem with this example: need to impute censored values so we’ll simulate Kaplan-Meier curves to compare to empirical curve. Plot em
- 周辺文脈（JA, 自動訳）: 4.2 事後予測分布 / 事後からのサンプル、観察のシミュレーション。この例の問題: 打ち切り値を代入する必要があるため、カプラン マイヤー曲線をシミュレートして経験曲線と比較します。プロットしてください
- Workflowフェーズ: **EDA / observed data**
- 実務での読み方: モデル化前に、観測単位・外れ値・欠測・群構造・時系列性・上限/下限などを確認する。MLflowではデータ版と前処理版を固定する。
- MLflow連携: `dataset_uri, dataset_hash, preprocessing_version, n_obs, group_count`
- 参照: [公式ページ](https://avehtari.github.io/Bayesian-Workflow/cat_adoptions/cat_adoptions.html#fig-km-2) / [ソース候補](https://github.com/avehtari/Bayesian-Workflow/blob/eb00fa4397314ef7d90203382542bd44c590e289/cat_adoptions/cat_adoptions.R)

### Debugging a model: World Cup football

- ページ: <https://avehtari.github.io/Bayesian-Workflow/world_cup/world_cup.html>
- ソース候補: <https://github.com/avehtari/Bayesian-Workflow/blob/eb00fa4397314ef7d90203382542bd44c590e289/world_cup/world_cup.R>

#### `world-cup-world-cup/fig-worldcup-mcmc-intervals-fit_1`

- 種別: `figure` / 公式ID: `fig-worldcup-mcmc-intervals-fit_1` / ページ内順序: 1
- caption/列: Figure 1
- 周辺文脈（EN）: Fit the model and show the results
- 周辺文脈（JA, 自動訳）: 3 最初のモデル / モデルを当てはめて結果を表示する
- Workflowフェーズ: **Posterior summary / effect interpretation**
- 実務での読み方: 推定効果・不確実性・派生量を意思決定に接続する。平均だけでなく区間・分布・実務閾値超過確率を残す。
- MLflow連携: `posterior_draws_uri, model_code_hash, ci_width, decision_threshold_prob`
- 参照: [公式ページ](https://avehtari.github.io/Bayesian-Workflow/world_cup/world_cup.html#fig-worldcup-mcmc-intervals-fit_1) / [ソース候補](https://github.com/avehtari/Bayesian-Workflow/blob/eb00fa4397314ef7d90203382542bd44c590e289/world_cup/world_cup.R)

#### `world-cup-world-cup/fig-worldcup-ppc-intervals-fit_1`

- 種別: `figure` / 公式ID: `fig-worldcup-ppc-intervals-fit_1` / ページ内順序: 2
- caption/列: Figure 2
- 周辺文脈（EN）: Fit the model and show the results
- 周辺文脈（JA, 自動訳）: 3.1 最初のモデルの適合性を確認する / モデルを適合させて結果を表示する
- Workflowフェーズ: **Posterior predictive checking / calibration**
- 実務での読み方: モデルが再現すべき特徴を外していないか確認する。PPC統計量と図をartifact化し、モデル改善の根拠にする。
- MLflow連携: `ppc_stat_*, loo_pit_ecdf_maxdev, calibration_error, replicated_seed`
- 参照: [公式ページ](https://avehtari.github.io/Bayesian-Workflow/world_cup/world_cup.html#fig-worldcup-ppc-intervals-fit_1) / [ソース候補](https://github.com/avehtari/Bayesian-Workflow/blob/eb00fa4397314ef7d90203382542bd44c590e289/world_cup/world_cup.R)

#### `world-cup-world-cup/fig-worldcup-mcmc-intervals-fit_2`

- 種別: `figure` / 公式ID: `fig-worldcup-mcmc-intervals-fit_2` / ページ内順序: 3
- caption/列: Figure 3
- 周辺文脈（EN）: Fit the model and show the results
- 周辺文脈（JA, 自動訳）: 4 sqrt 変換を行わない 2 番目のモデル / モデルを当てはめて結果を表示する
- Workflowフェーズ: **Posterior summary / effect interpretation**
- 実務での読み方: 推定効果・不確実性・派生量を意思決定に接続する。平均だけでなく区間・分布・実務閾値超過確率を残す。
- MLflow連携: `posterior_draws_uri, model_code_hash, ci_width, decision_threshold_prob`
- 参照: [公式ページ](https://avehtari.github.io/Bayesian-Workflow/world_cup/world_cup.html#fig-worldcup-mcmc-intervals-fit_2) / [ソース候補](https://github.com/avehtari/Bayesian-Workflow/blob/eb00fa4397314ef7d90203382542bd44c590e289/world_cup/world_cup.R)

#### `world-cup-world-cup/fig-worldcup-ppc-intervals-fit_2`

- 種別: `figure` / 公式ID: `fig-worldcup-ppc-intervals-fit_2` / ページ内順序: 4
- caption/列: Figure 4
- 周辺文脈（EN）: Fit the model and show the results
- 周辺文脈（JA, 自動訳）: 4.1 2 番目のモデルのデータへの適合を確認する / モデルを適合させ、結果を表示する
- Workflowフェーズ: **EDA / observed data**
- 実務での読み方: モデル化前に、観測単位・外れ値・欠測・群構造・時系列性・上限/下限などを確認する。MLflowではデータ版と前処理版を固定する。
- MLflow連携: `dataset_uri, dataset_hash, preprocessing_version, n_obs, group_count`
- 参照: [公式ページ](https://avehtari.github.io/Bayesian-Workflow/world_cup/world_cup.html#fig-worldcup-ppc-intervals-fit_2) / [ソース候補](https://github.com/avehtari/Bayesian-Workflow/blob/eb00fa4397314ef7d90203382542bd44c590e289/world_cup/world_cup.R)

#### `world-cup-world-cup/fig-worldcup-mcmc-intervals-fit_3`

- 種別: `figure` / 公式ID: `fig-worldcup-mcmc-intervals-fit_3` / ページ内順序: 5
- caption/列: Figure 5
- 周辺文脈（EN）: Fit the model and show the results
- 周辺文脈（JA, 自動訳）: 5 最初のモデルを修正する / モデルを当てはめて結果を表示する
- Workflowフェーズ: **Posterior summary / effect interpretation**
- 実務での読み方: 推定効果・不確実性・派生量を意思決定に接続する。平均だけでなく区間・分布・実務閾値超過確率を残す。
- MLflow連携: `posterior_draws_uri, model_code_hash, ci_width, decision_threshold_prob`
- 参照: [公式ページ](https://avehtari.github.io/Bayesian-Workflow/world_cup/world_cup.html#fig-worldcup-mcmc-intervals-fit_3) / [ソース候補](https://github.com/avehtari/Bayesian-Workflow/blob/eb00fa4397314ef7d90203382542bd44c590e289/world_cup/world_cup.R)

#### `world-cup-world-cup/fig-worldcup-ppc-intervals-fit_3`

- 種別: `figure` / 公式ID: `fig-worldcup-ppc-intervals-fit_3` / ページ内順序: 6
- caption/列: Figure 6
- 周辺文脈（EN）: Fit the model and show the results
- 周辺文脈（JA, 自動訳）: 5.1 固定された最初のモデルの適合性を確認する / モデルを適合させて結果を表示する
- Workflowフェーズ: **Posterior predictive checking / calibration**
- 実務での読み方: モデルが再現すべき特徴を外していないか確認する。PPC統計量と図をartifact化し、モデル改善の根拠にする。
- MLflow連携: `ppc_stat_*, loo_pit_ecdf_maxdev, calibration_error, replicated_seed`
- 参照: [公式ページ](https://avehtari.github.io/Bayesian-Workflow/world_cup/world_cup.html#fig-worldcup-ppc-intervals-fit_3) / [ソース候補](https://github.com/avehtari/Bayesian-Workflow/blob/eb00fa4397314ef7d90203382542bd44c590e289/world_cup/world_cup.R)

#### `world-cup-world-cup/fig-worldcup-mcmc-intervals-fit_3_no_prior`

- 種別: `figure` / 公式ID: `fig-worldcup-mcmc-intervals-fit_3_no_prior` / ページ内順序: 7
- caption/列: Figure 7
- 周辺文脈（EN）: set b=0 in the data
- 周辺文脈（JA, 自動訳）: 5.2 事前に powerindex を使用せずに同じモデルを近似する / データに b=0 を設定する
- Workflowフェーズ: **EDA / observed data**
- 実務での読み方: モデル化前に、観測単位・外れ値・欠測・群構造・時系列性・上限/下限などを確認する。MLflowではデータ版と前処理版を固定する。
- MLflow連携: `dataset_uri, dataset_hash, preprocessing_version, n_obs, group_count`
- 参照: [公式ページ](https://avehtari.github.io/Bayesian-Workflow/world_cup/world_cup.html#fig-worldcup-mcmc-intervals-fit_3_no_prior) / [ソース候補](https://github.com/avehtari/Bayesian-Workflow/blob/eb00fa4397314ef7d90203382542bd44c590e289/world_cup/world_cup.R)

#### `world-cup-world-cup/figure-008`

- 種別: `figure` / 公式ID: `(none)` / ページ内順序: 8
- caption/列: figure 8
- 周辺文脈（EN）: LOO-CV predictive checking with LOO-PIT for the discrete model looks fine
- 周辺文脈（JA, 自動訳）: 7.6 LOO-CV 予測チェック / 離散モデルの LOO-PIT を使用した LOO-CV 予測チェックは正常に見える
- Workflowフェーズ: **Posterior predictive checking / calibration**
- 実務での読み方: モデルが再現すべき特徴を外していないか確認する。PPC統計量と図をartifact化し、モデル改善の根拠にする。
- MLflow連携: `ppc_stat_*, loo_pit_ecdf_maxdev, calibration_error, replicated_seed`
- 参照: [公式ページ](https://avehtari.github.io/Bayesian-Workflow/world_cup/world_cup.html) / [ソース候補](https://github.com/avehtari/Bayesian-Workflow/blob/eb00fa4397314ef7d90203382542bd44c590e289/world_cup/world_cup.R)

#### `world-cup-world-cup/figure-009`

- 種別: `figure` / 公式ID: `(none)` / ページ内順序: 9
- caption/列: figure 9
- 周辺文脈（EN）: LOO-CV predictive checking for the continuous model indicates slight miscalibration with too many low PIT values (left tail of the predictive distribution is shorter than expected)
- 周辺文脈（JA, 自動訳）: 7.6 LOO-CV 予測チェック / 連続モデルの LOO-CV 予測チェックは、低すぎる PIT 値によるわずかなミスキャリブレーションを示します (予測分布の左裾が予想より短い)
- Workflowフェーズ: **EDA / observed data**
- 実務での読み方: モデル化前に、観測単位・外れ値・欠測・群構造・時系列性・上限/下限などを確認する。MLflowではデータ版と前処理版を固定する。
- MLflow連携: `dataset_uri, dataset_hash, preprocessing_version, n_obs, group_count`
- 参照: [公式ページ](https://avehtari.github.io/Bayesian-Workflow/world_cup/world_cup.html) / [ソース候補](https://github.com/avehtari/Bayesian-Workflow/blob/eb00fa4397314ef7d90203382542bd44c590e289/world_cup/world_cup.R)

#### `world-cup-world-cup/figure-010`

- 種別: `figure` / 公式ID: `(none)` / ページ内順序: 10
- caption/列: figure 10
- 周辺文脈（EN）: LOO-CV predictive checking with LOO-PIT for the binary Poisson model looks fine.
- 周辺文脈（JA, 自動訳）: 8.1 LOO-CV 予測チェック / バイナリ ポアソン モデルの LOO-PIT を使用した LOO-CV 予測チェックは問題ないようです。
- Workflowフェーズ: **Posterior predictive checking / calibration**
- 実務での読み方: モデルが再現すべき特徴を外していないか確認する。PPC統計量と図をartifact化し、モデル改善の根拠にする。
- MLflow連携: `ppc_stat_*, loo_pit_ecdf_maxdev, calibration_error, replicated_seed`
- 参照: [公式ページ](https://avehtari.github.io/Bayesian-Workflow/world_cup/world_cup.html) / [ソース候補](https://github.com/avehtari/Bayesian-Workflow/blob/eb00fa4397314ef7d90203382542bd44c590e289/world_cup/world_cup.R)

#### `world-cup-world-cup/figure-011`

- 種別: `figure` / 公式ID: `(none)` / ページ内順序: 11
- caption/列: figure 11
- 周辺文脈（EN）: LOO-CV predictive checking with LOO-PIT for the Poisson difference model looks fine.
- 周辺文脈（JA, 自動訳）: 8.1 LOO-CV 予測チェック / ポアソン差分モデルの LOO-PIT を使用した LOO-CV 予測チェックは問題ないようです。
- Workflowフェーズ: **Posterior predictive checking / calibration**
- 実務での読み方: モデルが再現すべき特徴を外していないか確認する。PPC統計量と図をartifact化し、モデル改善の根拠にする。
- MLflow連携: `ppc_stat_*, loo_pit_ecdf_maxdev, calibration_error, replicated_seed`
- 参照: [公式ページ](https://avehtari.github.io/Bayesian-Workflow/world_cup/world_cup.html) / [ソース候補](https://github.com/avehtari/Bayesian-Workflow/blob/eb00fa4397314ef7d90203382542bd44c590e289/world_cup/world_cup.R)

### Leave-one-out cross validation model checking and comparison: Roaches

- ページ: <https://avehtari.github.io/Bayesian-Workflow/roaches/roaches.html>
- ソース候補: <https://github.com/avehtari/Bayesian-Workflow/blob/eb00fa4397314ef7d90203382542bd44c590e289/roaches/roaches.R>

#### `roaches-roaches/fig-posterior-poisson`

- 種別: `figure` / 公式ID: `fig-posterior-poisson` / ページ内順序: 1
- caption/列: Figure 1
- 周辺文脈（EN）: Plot posterior
- 周辺文脈（JA, 自動訳）: 3 ポアソンモデル / 事後プロット
- Workflowフェーズ: **Posterior summary / effect interpretation**
- 実務での読み方: 推定効果・不確実性・派生量を意思決定に接続する。平均だけでなく区間・分布・実務閾値超過確率を残す。
- MLflow連携: `posterior_draws_uri, model_code_hash, ci_width, decision_threshold_prob`
- 参照: [公式ページ](https://avehtari.github.io/Bayesian-Workflow/roaches/roaches.html#fig-posterior-poisson) / [ソース候補](https://github.com/avehtari/Bayesian-Workflow/blob/eb00fa4397314ef7d90203382542bd44c590e289/roaches/roaches.R)

#### `roaches-roaches/fig-ppc_dens-poisson`

- 種別: `figure` / 公式ID: `fig-ppc_dens-poisson` / ページ内順序: 2
- caption/列: Figure 2
- 周辺文脈（EN）: Posterior predictive checking can often detect problems and also provide more information about the reason. As the range of counts is large, we can use kernel density estimate plot
- 周辺文脈（JA, 自動訳）: 3.1 事後予測チェック / 事後予測チェックでは、問題を検出できることが多く、その理由についての詳細情報も提供されます。カウントの範囲が広いため、カーネル密度推定プロットを使用できます。
- Workflowフェーズ: **Posterior predictive checking / calibration**
- 実務での読み方: モデルが再現すべき特徴を外していないか確認する。PPC統計量と図をartifact化し、モデル改善の根拠にする。
- MLflow連携: `ppc_stat_*, loo_pit_ecdf_maxdev, calibration_error, replicated_seed`
- 参照: [公式ページ](https://avehtari.github.io/Bayesian-Workflow/roaches/roaches.html#fig-ppc_dens-poisson) / [ソース候補](https://github.com/avehtari/Bayesian-Workflow/blob/eb00fa4397314ef7d90203382542bd44c590e289/roaches/roaches.R)

#### `roaches-roaches/fig-ppc_rootogram-poisson`

- 種別: `figure` / 公式ID: `fig-ppc_rootogram-poisson` / ページ内順序: 3
- caption/列: Figure 3
- 周辺文脈（EN）: Although in this case the model misspecification is obvious with kernel density plot, too, for count the often a better choice is a rootogram variant proposed by Säilynoja et al. (
- 周辺文脈（JA, 自動訳）: 3.1 事後予測チェック / この場合、モデルの仕様ミスはカーネル密度プロットでも明らかですが、多くの場合、カウントに関しては、Säilynoja らによって提案されたルートグラムのバリアントがより良い選択となります。 (
- Workflowフェーズ: **Posterior predictive checking / calibration**
- 実務での読み方: モデルが再現すべき特徴を外していないか確認する。PPC統計量と図をartifact化し、モデル改善の根拠にする。
- MLflow連携: `ppc_stat_*, loo_pit_ecdf_maxdev, calibration_error, replicated_seed`
- 参照: [公式ページ](https://avehtari.github.io/Bayesian-Workflow/roaches/roaches.html#fig-ppc_rootogram-poisson) / [ソース候補](https://github.com/avehtari/Bayesian-Workflow/blob/eb00fa4397314ef7d90203382542bd44c590e289/roaches/roaches.R)

#### `roaches-roaches/fig-posterior-nb`

- 種別: `figure` / 公式ID: `fig-posterior-nb` / ページ内順序: 4
- caption/列: Figure 4
- 周辺文脈（EN）: Plot posterior
- 周辺文脈（JA, 自動訳）: 4 負の二項モデル / 事後プロット
- Workflowフェーズ: **Posterior summary / effect interpretation**
- 実務での読み方: 推定効果・不確実性・派生量を意思決定に接続する。平均だけでなく区間・分布・実務閾値超過確率を残す。
- MLflow連携: `posterior_draws_uri, model_code_hash, ci_width, decision_threshold_prob`
- 参照: [公式ページ](https://avehtari.github.io/Bayesian-Workflow/roaches/roaches.html#fig-posterior-nb) / [ソース候補](https://github.com/avehtari/Bayesian-Workflow/blob/eb00fa4397314ef7d90203382542bd44c590e289/roaches/roaches.R)

#### `roaches-roaches/fig-ppc_dens-nb`

- 種別: `figure` / 公式ID: `fig-ppc_dens-nb` / ページ内順序: 5
- caption/列: Figure 5
- 周辺文脈（EN）: We use posterior predictive checking to compare marginal data and predictive distributions.
- 周辺文脈（JA, 自動訳）: 4.1 事後予測チェックと LOO 予測チェック / 事後予測チェックを使用して周辺データと予測分布を比較します。
- Workflowフェーズ: **EDA / observed data**
- 実務での読み方: モデル化前に、観測単位・外れ値・欠測・群構造・時系列性・上限/下限などを確認する。MLflowではデータ版と前処理版を固定する。
- MLflow連携: `dataset_uri, dataset_hash, preprocessing_version, n_obs, group_count`
- 参照: [公式ページ](https://avehtari.github.io/Bayesian-Workflow/roaches/roaches.html#fig-ppc_dens-nb) / [ソース候補](https://github.com/avehtari/Bayesian-Workflow/blob/eb00fa4397314ef7d90203382542bd44c590e289/roaches/roaches.R)

#### `roaches-roaches/fig-ppc_rootogram-nb`

- 種別: `figure` / 公式ID: `fig-ppc_rootogram-nb` / ページ内順序: 6
- caption/列: Figure 6
- 周辺文脈（EN）: We see that the negative-binomial model is much better although it seems that the model predictive distribution has more mass for small counts than the real data. This discrepancy
- 周辺文脈（JA, 自動訳）: 4.1 事後予測および LOO 予測検査 / 負の二項モデルの方がはるかに優れていることがわかりますが、モデルの予測分布は小さいカウントに対して実際のデータよりも質量が大きいように見えます。この矛盾
- Workflowフェーズ: **EDA / observed data**
- 実務での読み方: モデル化前に、観測単位・外れ値・欠測・群構造・時系列性・上限/下限などを確認する。MLflowではデータ版と前処理版を固定する。
- MLflow連携: `dataset_uri, dataset_hash, preprocessing_version, n_obs, group_count`
- 参照: [公式ページ](https://avehtari.github.io/Bayesian-Workflow/roaches/roaches.html#fig-ppc_rootogram-nb) / [ソース候補](https://github.com/avehtari/Bayesian-Workflow/blob/eb00fa4397314ef7d90203382542bd44c590e289/roaches/roaches.R)

#### `roaches-roaches/fig-ppc_intervals-nb`

- 種別: `figure` / 公式ID: `fig-ppc_intervals-nb` / ページ内順序: 7
- caption/列: Figure 7
- 周辺文脈（EN）: Instead of looking at the marginal distribution, we can look at the pointwise predictive distribution and corresponding observations.
- 周辺文脈（JA, 自動訳）: 4.1 事後および LOO 予測チェック / 周辺分布を調べる代わりに、点ごとの予測分布と対応する観測値を調べることができます。
- Workflowフェーズ: **EDA / observed data**
- 実務での読み方: モデル化前に、観測単位・外れ値・欠測・群構造・時系列性・上限/下限などを確認する。MLflowではデータ版と前処理版を固定する。
- MLflow連携: `dataset_uri, dataset_hash, preprocessing_version, n_obs, group_count`
- 参照: [公式ページ](https://avehtari.github.io/Bayesian-Workflow/roaches/roaches.html#fig-ppc_intervals-nb) / [ソース候補](https://github.com/avehtari/Bayesian-Workflow/blob/eb00fa4397314ef7d90203382542bd44c590e289/roaches/roaches.R)

#### `roaches-roaches/fig-ppc_pit-nb`

- 種別: `figure` / 公式ID: `fig-ppc_pit-nb` / ページ内順序: 8
- caption/列: Figure 8
- 周辺文脈（EN）: If the model predictive distributions are well calibrated, then the observations should look like randomly drawn from the predictive distributions. We can use a pit_ecdf to make pr
- 周辺文脈（JA, 自動訳）: 4.1 事後および LOO 予測チェック / モデルの予測分布が適切に校正されている場合、観測値は予測分布からランダムに抽出されたように見えるはずです。 pr には、pit_ecdf を使用できます。
- Workflowフェーズ: **Posterior predictive checking / calibration**
- 実務での読み方: モデルが再現すべき特徴を外していないか確認する。PPC統計量と図をartifact化し、モデル改善の根拠にする。
- MLflow連携: `ppc_stat_*, loo_pit_ecdf_maxdev, calibration_error, replicated_seed`
- 参照: [公式ページ](https://avehtari.github.io/Bayesian-Workflow/roaches/roaches.html#fig-ppc_pit-nb) / [ソース候補](https://github.com/avehtari/Bayesian-Workflow/blob/eb00fa4397314ef7d90203382542bd44c590e289/roaches/roaches.R)

#### `roaches-roaches/fig-ppc_loo_intervals-nb`

- 種別: `figure` / 公式ID: `fig-ppc_loo_intervals-nb` / ページ内順序: 9
- caption/列: Figure 9
- 周辺文脈（EN）: All Pareto- \hat{k} are good indicating PSIS-LOO computation with moment matching works well. p_loo is closer to the actual number of parameters, but still slightly larger than the
- 周辺文脈（JA, 自動訳）: 4.1 事後および LOO 予測チェック / すべてのパレート-\hat{k} は良好で、モーメント マッチングによる PSIS-LOO 計算がうまく機能していることを示しています。 p_loo は実際のパラメータ数に近いですが、それでもわずかに大きくなります。
- Workflowフェーズ: **Posterior predictive checking / calibration**
- 実務での読み方: モデルが再現すべき特徴を外していないか確認する。PPC統計量と図をartifact化し、モデル改善の根拠にする。
- MLflow連携: `ppc_stat_*, loo_pit_ecdf_maxdev, calibration_error, replicated_seed`
- 参照: [公式ページ](https://avehtari.github.io/Bayesian-Workflow/roaches/roaches.html#fig-ppc_loo_intervals-nb) / [ソース候補](https://github.com/avehtari/Bayesian-Workflow/blob/eb00fa4397314ef7d90203382542bd44c590e289/roaches/roaches.R)

#### `roaches-roaches/fig-ppc_loo_pit-nb`

- 種別: `figure` / 公式ID: `fig-ppc_loo_pit-nb` / ページ内順序: 10
- caption/列: Figure 10
- 周辺文脈（EN）: All Pareto- \hat{k} are good indicating PSIS-LOO computation with moment matching works well. p_loo is closer to the actual number of parameters, but still slightly larger than the
- 周辺文脈（JA, 自動訳）: 4.1 事後および LOO 予測チェック / すべてのパレート-\hat{k} は良好で、モーメント マッチングによる PSIS-LOO 計算がうまく機能していることを示しています。 p_loo は実際のパラメータ数に近いですが、それでもわずかに大きくなります。
- Workflowフェーズ: **Posterior predictive checking / calibration**
- 実務での読み方: モデルが再現すべき特徴を外していないか確認する。PPC統計量と図をartifact化し、モデル改善の根拠にする。
- MLflow連携: `ppc_stat_*, loo_pit_ecdf_maxdev, calibration_error, replicated_seed`
- 参照: [公式ページ](https://avehtari.github.io/Bayesian-Workflow/roaches/roaches.html#fig-ppc_loo_pit-nb) / [ソース候補](https://github.com/avehtari/Bayesian-Workflow/blob/eb00fa4397314ef7d90203382542bd44c590e289/roaches/roaches.R)

#### `roaches-roaches/fig-posterior-nb_dispersion`

- 種別: `figure` / 公式ID: `fig-posterior-nb_dispersion` / ページ内順序: 11
- caption/列: Figure 11
- 周辺文脈（EN）: As Poisson is a special case of negative-Binomial, instead of using cross validation model comparison, we could have also seen that Poisson is not a good model by looking at the po
- 周辺文脈（JA, 自動訳）: 4.1 事後予測チェックと LOO 予測チェック / ポアソンは負の二項分布の特殊なケースであるため、相互検証モデルの比較を使用する代わりに、ポアソンが良いモデルではないことは、po を調べることで確認することもできました。
- Workflowフェーズ: **Posterior summary / effect interpretation**
- 実務での読み方: 推定効果・不確実性・派生量を意思決定に接続する。平均だけでなく区間・分布・実務閾値超過確率を残す。
- MLflow連携: `posterior_draws_uri, model_code_hash, ci_width, decision_threshold_prob`
- 参照: [公式ページ](https://avehtari.github.io/Bayesian-Workflow/roaches/roaches.html#fig-posterior-nb_dispersion) / [ソース候補](https://github.com/avehtari/Bayesian-Workflow/blob/eb00fa4397314ef7d90203382542bd44c590e289/roaches/roaches.R)

#### `roaches-roaches/fig-pava-nb`

- 種別: `figure` / 公式ID: `fig-pava-nb` / ページ内順序: 12
- caption/列: Figure 12
- 周辺文脈（EN）: Posterior predictive rootogram and LOO-PIT-ECDF looked good, but for discrete models where some discrete values have relatively high probability it may miss things and it is good t
- 周辺文脈（JA, 自動訳）: 4.1 事後予測チェックと LOO 予測チェック / 事後予測ルートグラムと LOO-PIT-ECDF は良好に見えましたが、いくつかの離散値が比較的高い確率を持つ離散モデルの場合は、何かを見逃す可能性があり、これは良いことです。
- Workflowフェーズ: **Posterior predictive checking / calibration**
- 実務での読み方: モデルが再現すべき特徴を外していないか確認する。PPC統計量と図をartifact化し、モデル改善の根拠にする。
- MLflow連携: `ppc_stat_*, loo_pit_ecdf_maxdev, calibration_error, replicated_seed`
- 参照: [公式ページ](https://avehtari.github.io/Bayesian-Workflow/roaches/roaches.html#fig-pava-nb) / [ソース候補](https://github.com/avehtari/Bayesian-Workflow/blob/eb00fa4397314ef7d90203382542bd44c590e289/roaches/roaches.R)

#### `roaches-roaches/fig-posterior-poisson_varying`

- 種別: `figure` / 公式ID: `fig-posterior-poisson_varying` / ページ内順序: 13
- caption/列: Figure 13
- 周辺文脈（EN）: Plot posterior
- 周辺文脈（JA, 自動訳）: 5.1 事後分析/事後プロット
- Workflowフェーズ: **Posterior summary / effect interpretation**
- 実務での読み方: 推定効果・不確実性・派生量を意思決定に接続する。平均だけでなく区間・分布・実務閾値超過確率を残す。
- MLflow連携: `posterior_draws_uri, model_code_hash, ci_width, decision_threshold_prob`
- 参照: [公式ページ](https://avehtari.github.io/Bayesian-Workflow/roaches/roaches.html#fig-posterior-poisson_varying) / [ソース候補](https://github.com/avehtari/Bayesian-Workflow/blob/eb00fa4397314ef7d90203382542bd44c590e289/roaches/roaches.R)

#### `roaches-roaches/fig-ppc_dens-poisson_varying`

- 種別: `figure` / 公式ID: `fig-ppc_dens-poisson_varying` / ページ内順序: 14
- caption/列: Figure 14
- 周辺文脈（EN）: We do posterior predictive checking for varying intercept Poisson model.
- 周辺文脈（JA, 自動訳）: 5.3 事後予測チェック / さまざまな切片ポアソン モデルに対して事後予測チェックを行います。
- Workflowフェーズ: **Posterior predictive checking / calibration**
- 実務での読み方: モデルが再現すべき特徴を外していないか確認する。PPC統計量と図をartifact化し、モデル改善の根拠にする。
- MLflow連携: `ppc_stat_*, loo_pit_ecdf_maxdev, calibration_error, replicated_seed`
- 参照: [公式ページ](https://avehtari.github.io/Bayesian-Workflow/roaches/roaches.html#fig-ppc_dens-poisson_varying) / [ソース候補](https://github.com/avehtari/Bayesian-Workflow/blob/eb00fa4397314ef7d90203382542bd44c590e289/roaches/roaches.R)

#### `roaches-roaches/fig-ppc_rootogram-pvi`

- 種別: `figure` / 公式ID: `fig-ppc_rootogram-pvi` / ページ内順序: 15
- caption/列: Figure 15
- 周辺文脈（EN）: Looking at the discrete rootogram looks also fine.
- 周辺文脈（JA, 自動訳）: 5.3 事後予測チェック / 離散ルートグラムを見ても問題ないようです。
- Workflowフェーズ: **Posterior predictive checking / calibration**
- 実務での読み方: モデルが再現すべき特徴を外していないか確認する。PPC統計量と図をartifact化し、モデル改善の根拠にする。
- MLflow連携: `ppc_stat_*, loo_pit_ecdf_maxdev, calibration_error, replicated_seed`
- 参照: [公式ページ](https://avehtari.github.io/Bayesian-Workflow/roaches/roaches.html#fig-ppc_rootogram-pvi) / [ソース候補](https://github.com/avehtari/Bayesian-Workflow/blob/eb00fa4397314ef7d90203382542bd44c590e289/roaches/roaches.R)

#### `roaches-roaches/fig-ppc_pit-poisson_varying`

- 種別: `figure` / 公式ID: `fig-ppc_pit-poisson_varying` / ページ内順序: 16
- caption/列: Figure 16
- 周辺文脈（EN）: PIT-ECDF plot seems to indicate problems
- 周辺文脈（JA, 自動訳）: 5.3 事後予測チェック/PIT-ECDF プロットは問題を示しているようです
- Workflowフェーズ: **Posterior predictive checking / calibration**
- 実務での読み方: モデルが再現すべき特徴を外していないか確認する。PPC統計量と図をartifact化し、モデル改善の根拠にする。
- MLflow連携: `ppc_stat_*, loo_pit_ecdf_maxdev, calibration_error, replicated_seed`
- 参照: [公式ページ](https://avehtari.github.io/Bayesian-Workflow/roaches/roaches.html#fig-ppc_pit-poisson_varying) / [ソース候補](https://github.com/avehtari/Bayesian-Workflow/blob/eb00fa4397314ef7d90203382542bd44c590e289/roaches/roaches.R)

#### `roaches-roaches/fig-ppc_intervals-poisson_varying`

- 種別: `figure` / 公式ID: `fig-ppc_intervals-poisson_varying` / ページ内順序: 17
- caption/列: Figure 17
- 周辺文脈（EN）: There are too many PIT values near 0.5. If we look at the predictive intervals and observations, we see that many the observations are in the middle of the posterior predictive int
- 周辺文脈（JA, 自動訳）: 5.3 事後予測チェック / 0.5 付近の PIT 値が多すぎます。予測区間と観測値を見ると、多くの観測値が事後予測 int の中央にあることがわかります。
- Workflowフェーズ: **Posterior predictive checking / calibration**
- 実務での読み方: モデルが再現すべき特徴を外していないか確認する。PPC統計量と図をartifact化し、モデル改善の根拠にする。
- MLflow連携: `ppc_stat_*, loo_pit_ecdf_maxdev, calibration_error, replicated_seed`
- 参照: [公式ページ](https://avehtari.github.io/Bayesian-Workflow/roaches/roaches.html#fig-ppc_intervals-poisson_varying) / [ソース候補](https://github.com/avehtari/Bayesian-Workflow/blob/eb00fa4397314ef7d90203382542bd44c590e289/roaches/roaches.R)

#### `roaches-roaches/fig-ppc_loo_pit-poisson_varying`

- 種別: `figure` / 公式ID: `fig-ppc_loo_pit-poisson_varying` / ページ内順序: 18
- caption/列: Figure 18
- 周辺文脈（EN）: LOO-PIT’s can take into account the model flexibility, if the computation works. In this case LOO-PIT’s look slightly better, but still showing problems, but this is because PSIS-L
- 周辺文脈（JA, 自動訳）: 5.3 事後予測チェック / LOO-PIT は、計算が機能する場合、モデルの柔軟性を考慮に入れることができます。この場合、LOO-PIT は若干改善されているように見えますが、まだ問題が発生しています。これは PSIS-L が原因です。
- Workflowフェーズ: **Posterior predictive checking / calibration**
- 実務での読み方: モデルが再現すべき特徴を外していないか確認する。PPC統計量と図をartifact化し、モデル改善の根拠にする。
- MLflow連携: `ppc_stat_*, loo_pit_ecdf_maxdev, calibration_error, replicated_seed`
- 参照: [公式ページ](https://avehtari.github.io/Bayesian-Workflow/roaches/roaches.html#fig-ppc_loo_pit-poisson_varying) / [ソース候補](https://github.com/avehtari/Bayesian-Workflow/blob/eb00fa4397314ef7d90203382542bd44c590e289/roaches/roaches.R)

#### `roaches-roaches/fig-posterior-poisson_var_int`

- 種別: `figure` / 公式ID: `fig-posterior-poisson_var_int` / ページ内順序: 19
- caption/列: Figure 19
- 周辺文脈（EN）: The posterior is similar as above for varying intercept Poisson model, as it should be, as the generated quantities is not affecting the posterior.
- 周辺文脈（JA, 自動訳）: 6 変化する切片と統合 LOO を備えたポアソン モデル / 事後分布は、生成された量が事後分布に影響を及ぼさないため、変化する切片ポアソン モデルの場合と同様です。
- Workflowフェーズ: **Posterior summary / effect interpretation**
- 実務での読み方: 推定効果・不確実性・派生量を意思決定に接続する。平均だけでなく区間・分布・実務閾値超過確率を残す。
- MLflow連携: `posterior_draws_uri, model_code_hash, ci_width, decision_threshold_prob`
- 参照: [公式ページ](https://avehtari.github.io/Bayesian-Workflow/roaches/roaches.html#fig-posterior-poisson_var_int) / [ソース候補](https://github.com/avehtari/Bayesian-Workflow/blob/eb00fa4397314ef7d90203382542bd44c590e289/roaches/roaches.R)

#### `roaches-roaches/fig-ppc_loo_pit-poisson_varying_int`

- 種別: `figure` / 公式ID: `fig-ppc_loo_pit-poisson_varying_int` / ページ内順序: 20
- caption/列: Figure 20
- 周辺文脈（EN）: LOO-PIT plot looks good, although a bit more variation, which is probably due to lower effective sample sizes due to more challenging posterior than for negative binomial model.
- 周辺文脈（JA, 自動訳）: 6 変化する切片と統合された LOO / LOO-PIT プロットを備えたポアソン モデルは、ばらつきが若干多くなりますが、良好に見えます。これはおそらく、負の二項モデルよりも事後分布がより困難であるため、有効サンプル サイズが低いことが原因と考えられます。
- Workflowフェーズ: **Posterior predictive checking / calibration**
- 実務での読み方: モデルが再現すべき特徴を外していないか確認する。PPC統計量と図をartifact化し、モデル改善の根拠にする。
- MLflow連携: `ppc_stat_*, loo_pit_ecdf_maxdev, calibration_error, replicated_seed`
- 参照: [公式ページ](https://avehtari.github.io/Bayesian-Workflow/roaches/roaches.html#fig-ppc_loo_pit-poisson_varying_int) / [ソース候補](https://github.com/avehtari/Bayesian-Workflow/blob/eb00fa4397314ef7d90203382542bd44c590e289/roaches/roaches.R)

#### `roaches-roaches/fig-pava-p_vi`

- 種別: `figure` / 公式ID: `fig-pava-p_vi` / ページ内順序: 21
- caption/列: Figure 21
- 周辺文脈（EN）: We check the calibration of predictive probabilities for zeros vs non-zeros. The calibration plot looks better than with negative binomial model. The predicted probabilities have w
- 周辺文脈（JA, 自動訳）: 6 可変切片と統合 LOO を備えたポアソン モデル / ゼロと非ゼロの予測確率の校正をチェックします。キャリブレーション プロットは、負の二項モデルを使用した場合よりも良く見えます。予測される確率は w になります。
- Workflowフェーズ: **Posterior predictive checking / calibration**
- 実務での読み方: モデルが再現すべき特徴を外していないか確認する。PPC統計量と図をartifact化し、モデル改善の根拠にする。
- MLflow連携: `ppc_stat_*, loo_pit_ecdf_maxdev, calibration_error, replicated_seed`
- 参照: [公式ページ](https://avehtari.github.io/Bayesian-Workflow/roaches/roaches.html#fig-pava-p_vi) / [ソース候補](https://github.com/avehtari/Bayesian-Workflow/blob/eb00fa4397314ef7d90203382542bd44c590e289/roaches/roaches.R)

#### `roaches-roaches/fig-ppc_dens-zinb`

- 種別: `figure` / 公式ID: `fig-ppc_dens-zinb` / ページ内順序: 22
- caption/列: Figure 22
- 周辺文脈（EN）: Posterior predictive checking looks good, but there is no clear difference when looking at marginal predictive distributions or LOO-PIT.
- 周辺文脈（JA, 自動訳）: 7 ゼロインフレの負の二項モデル / 事後予測チェックは良好に見えますが、周辺予測分布または LOO-PIT を見ると明確な違いはありません。
- Workflowフェーズ: **Posterior predictive checking / calibration**
- 実務での読み方: モデルが再現すべき特徴を外していないか確認する。PPC統計量と図をartifact化し、モデル改善の根拠にする。
- MLflow連携: `ppc_stat_*, loo_pit_ecdf_maxdev, calibration_error, replicated_seed`
- 参照: [公式ページ](https://avehtari.github.io/Bayesian-Workflow/roaches/roaches.html#fig-ppc_dens-zinb) / [ソース候補](https://github.com/avehtari/Bayesian-Workflow/blob/eb00fa4397314ef7d90203382542bd44c590e289/roaches/roaches.R)

#### `roaches-roaches/fig-ppc_rootogram-zinb`

- 種別: `figure` / 公式ID: `fig-ppc_rootogram-zinb` / ページ内順序: 23
- caption/列: Figure 23
- 周辺文脈（EN）: Posterior predictive checking looks good, but there is no clear difference when looking at marginal predictive distributions or LOO-PIT.
- 周辺文脈（JA, 自動訳）: 7 ゼロインフレの負の二項モデル / 事後予測チェックは良好に見えますが、周辺予測分布または LOO-PIT を見ると明確な違いはありません。
- Workflowフェーズ: **Posterior predictive checking / calibration**
- 実務での読み方: モデルが再現すべき特徴を外していないか確認する。PPC統計量と図をartifact化し、モデル改善の根拠にする。
- MLflow連携: `ppc_stat_*, loo_pit_ecdf_maxdev, calibration_error, replicated_seed`
- 参照: [公式ページ](https://avehtari.github.io/Bayesian-Workflow/roaches/roaches.html#fig-ppc_rootogram-zinb) / [ソース候補](https://github.com/avehtari/Bayesian-Workflow/blob/eb00fa4397314ef7d90203382542bd44c590e289/roaches/roaches.R)

#### `roaches-roaches/fig-ppc_loo_pit-zinb`

- 種別: `figure` / 公式ID: `fig-ppc_loo_pit-zinb` / ページ内順序: 24
- caption/列: Figure 24
- 周辺文脈（EN）: LOO-PIT-ECDF
- 周辺文脈（JA, 自動訳）: 7 ゼロインフレート負二項モデル / LOO-PIT-ECDF
- Workflowフェーズ: **Posterior predictive checking / calibration**
- 実務での読み方: モデルが再現すべき特徴を外していないか確認する。PPC統計量と図をartifact化し、モデル改善の根拠にする。
- MLflow連携: `ppc_stat_*, loo_pit_ecdf_maxdev, calibration_error, replicated_seed`
- 参照: [公式ページ](https://avehtari.github.io/Bayesian-Workflow/roaches/roaches.html#fig-ppc_loo_pit-zinb) / [ソース候補](https://github.com/avehtari/Bayesian-Workflow/blob/eb00fa4397314ef7d90203382542bd44c590e289/roaches/roaches.R)

#### `roaches-roaches/fig-pava-zinb`

- 種別: `figure` / 公式ID: `fig-pava-zinb` / ページ内順序: 25
- caption/列: Figure 25
- 周辺文脈（EN）: Reliability diagram assessing the calibration of predicted probabilities of zero vs non-zero looks clearly better than the one for negative binomial model.
- 周辺文脈（JA, 自動訳）: 7 ゼロインフレート負の二項モデル / ゼロ対非ゼロの予測確率の校正を評価する信頼性図は、負の二項モデルよりも明らかに優れているように見えます。
- Workflowフェーズ: **Posterior predictive checking / calibration**
- 実務での読み方: モデルが再現すべき特徴を外していないか確認する。PPC統計量と図をartifact化し、モデル改善の根拠にする。
- MLflow連携: `ppc_stat_*, loo_pit_ecdf_maxdev, calibration_error, replicated_seed`
- 参照: [公式ページ](https://avehtari.github.io/Bayesian-Workflow/roaches/roaches.html#fig-pava-zinb) / [ソース候補](https://github.com/avehtari/Bayesian-Workflow/blob/eb00fa4397314ef7d90203382542bd44c590e289/roaches/roaches.R)

#### `roaches-roaches/fig-posterior-zinb`

- 種別: `figure` / 公式ID: `fig-posterior-zinb` / ページ内順序: 26
- caption/列: Figure 26
- 周辺文脈（EN）: Plot posterior
- 周辺文脈（JA, 自動訳）: 7.1 事後分析/事後プロット
- Workflowフェーズ: **Posterior summary / effect interpretation**
- 実務での読み方: 推定効果・不確実性・派生量を意思決定に接続する。平均だけでなく区間・分布・実務閾値超過確率を残す。
- MLflow連携: `posterior_draws_uri, model_code_hash, ci_width, decision_threshold_prob`
- 参照: [公式ページ](https://avehtari.github.io/Bayesian-Workflow/roaches/roaches.html#fig-posterior-zinb) / [ソース候補](https://github.com/avehtari/Bayesian-Workflow/blob/eb00fa4397314ef7d90203382542bd44c590e289/roaches/roaches.R)

#### `roaches-roaches/fig-effect-zinb`

- 種別: `figure` / 公式ID: `fig-effect-zinb` / ページ内順序: 27
- caption/列: Figure 27
- 周辺文脈（EN）: Ratio of expected number of roaches with vs without treatment
- 周辺文脈（JA, 自動訳）: 7.1 事後分析 / 治療ありと治療なしのゴキブリの予想数の比
- Workflowフェーズ: **Posterior summary / effect interpretation**
- 実務での読み方: 推定効果・不確実性・派生量を意思決定に接続する。平均だけでなく区間・分布・実務閾値超過確率を残す。
- MLflow連携: `posterior_draws_uri, model_code_hash, ci_width, decision_threshold_prob`
- 参照: [公式ページ](https://avehtari.github.io/Bayesian-Workflow/roaches/roaches.html#fig-effect-zinb) / [ソース候補](https://github.com/avehtari/Bayesian-Workflow/blob/eb00fa4397314ef7d90203382542bd44c590e289/roaches/roaches.R)

#### `roaches-roaches/fig-effect-p-nb-zinb`

- 種別: `figure` / 公式ID: `fig-effect-p-nb-zinb` / ページ内順序: 28
- caption/列: Figure 28
- 周辺文脈（EN）: Assuming our model is causally sensible, we can trust the posterior more if the model has well calibrated predictive distributions (passes posterior and LOO predictive, and calibra
- 周辺文脈（JA, 自動訳）: 7.1 事後分析 / モデルが因果的に合理的であると仮定すると、モデルが適切に調整された予測分布を持っている (事後予測と LOO 予測に合格し、キャリブレーションに合格している) 場合、事後をより信頼できます。
- Workflowフェーズ: **Posterior summary / effect interpretation**
- 実務での読み方: 推定効果・不確実性・派生量を意思決定に接続する。平均だけでなく区間・分布・実務閾値超過確率を残す。
- MLflow連携: `posterior_draws_uri, model_code_hash, ci_width, decision_threshold_prob`
- 参照: [公式ページ](https://avehtari.github.io/Bayesian-Workflow/roaches/roaches.html#fig-effect-p-nb-zinb) / [ソース候補](https://github.com/avehtari/Bayesian-Workflow/blob/eb00fa4397314ef7d90203382542bd44c590e289/roaches/roaches.R)

### Model building and expansion: Golf putting

- ページ: <https://avehtari.github.io/Bayesian-Workflow/golf/golf.html>
- ソース候補: <https://github.com/avehtari/Bayesian-Workflow/blob/eb00fa4397314ef7d90203382542bd44c590e289/golf/golf.R>

#### `golf-golf/fig-golf-data`

- 種別: `figure` / 公式ID: `fig-golf-data` / ページ内順序: 1
- caption/列: Figure 1
- 周辺文脈（EN）: The following graph shows data from professional golfers on the proportion of successful putts as a function of distance from the hole (from Berry 1996 ) . Unsurprisingly, the prob
- 周辺文脈（JA, 自動訳）: 2 データ / 次のグラフは、ホールからの距離の関数としてパット成功の割合に関するプロゴルファーからのデータを示しています (Berry 1996 より)。当然のことながら、その可能性は
- Workflowフェーズ: **EDA / observed data**
- 実務での読み方: モデル化前に、観測単位・外れ値・欠測・群構造・時系列性・上限/下限などを確認する。MLflowではデータ版と前処理版を固定する。
- MLflow連携: `dataset_uri, dataset_hash, preprocessing_version, n_obs, group_count`
- 参照: [公式ページ](https://avehtari.github.io/Bayesian-Workflow/golf/golf.html#fig-golf-data) / [ソース候補](https://github.com/avehtari/Bayesian-Workflow/blob/eb00fa4397314ef7d90203382542bd44c590e289/golf/golf.R)

#### `golf-golf/fig-golf-fit1`

- 種別: `figure` / 公式ID: `fig-golf-fit1` / ページ内順序: 2
- caption/列: Figure 2
- 周辺文脈（EN）: The following graph shows the fit plotted along with the data:
- 周辺文脈（JA, 自動訳）: 3 ロジスティック回帰 / 次のグラフは、データとともにプロットされた近似を示しています。
- Workflowフェーズ: **EDA / observed data**
- 実務での読み方: モデル化前に、観測単位・外れ値・欠測・群構造・時系列性・上限/下限などを確認する。MLflowではデータ版と前処理版を固定する。
- MLflow連携: `dataset_uri, dataset_hash, preprocessing_version, n_obs, group_count`
- 参照: [公式ページ](https://avehtari.github.io/Bayesian-Workflow/golf/golf.html#fig-golf-fit1) / [ソース候補](https://github.com/avehtari/Bayesian-Workflow/blob/eb00fa4397314ef7d90203382542bd44c590e289/golf/golf.R)

#### `golf-golf/fig-golf-sketch-1`

- 種別: `figure` / 公式ID: `fig-golf-sketch-1` / ページ内順序: 3
- caption/列: Figure 3
- 周辺文脈（EN）: The graph below shows a simplified sketch of a golf shot. The dotted line represents the angle within which the ball of radius r must be hit so that it falls within the hole of rad
- 周辺文脈（JA, 自動訳）: 4 第一原理に基づくモデリング / 下のグラフは、ゴルフショットの簡略化されたスケッチを示しています。点線は、半径 r のボールが rad の穴に入るために打たなければならない角度を表します。
- Workflowフェーズ: **Model development / debugging**
- 実務での読み方: 小さいモデルから始め、失敗runを観察しながらモデル族・prior・データ処理を段階的に拡張する。
- MLflow連携: `iteration_id, change_reason, failure_mode, hypothesis, next_action`
- 参照: [公式ページ](https://avehtari.github.io/Bayesian-Workflow/golf/golf.html#fig-golf-sketch-1) / [ソース候補](https://github.com/avehtari/Bayesian-Workflow/blob/eb00fa4397314ef7d90203382542bd44c590e289/golf/golf.R)

#### `golf-golf/fig-golf-sketch-2`

- 種別: `figure` / 公式ID: `fig-golf-sketch-2` / ページ内順序: 4
- caption/列: Figure 4
- 周辺文脈（EN）: The next step is to model human error. We assume that the golfer is attempting to hit the ball completely straight but that many small factors interfere with this goal, so that the
- 周辺文脈（JA, 自動訳）: 4 第一原則に基づいたモデリング / 次のステップは、人的エラーをモデル化することです。ゴルファーはボールを完全に真っすぐに打とうとしているが、多くの小さな要因がこの目標を妨げていると仮定します。
- Workflowフェーズ: **Model development / debugging**
- 実務での読み方: 小さいモデルから始め、失敗runを観察しながらモデル族・prior・データ処理を段階的に拡張する。
- MLflow連携: `iteration_id, change_reason, failure_mode, hypothesis, next_action`
- 参照: [公式ページ](https://avehtari.github.io/Bayesian-Workflow/golf/golf.html#fig-golf-sketch-2) / [ソース候補](https://github.com/avehtari/Bayesian-Workflow/blob/eb00fa4397314ef7d90203382542bd44c590e289/golf/golf.R)

#### `golf-golf/fig-golf-angle-curves`

- 種別: `figure` / 公式ID: `fig-golf-angle-curves` / ページ内順序: 5
- caption/列: Figure 5
- 周辺文脈（EN）: Our model then has two parts: \begin{align} y_j &\sim \mathrm{binomial}(n_j, p_j)\\ p_j &= 2\Phi\left(\frac{\sin^{-1}((R-r)/x_j)}{\sigma}\right) - 1 , \text{ for } j=1,\dots, J. \e
- 周辺文脈（JA, 自動訳）: 4 第一原理に基づくモデリング / この場合、モデルには 2 つの部分があります: \begin{align} y_j &\sim \mathrm{binomial}(n_j, p_j)\\ p_j &= 2\Phi\left(\frac{\sin^{-1}((R-r)/x_j)}{\sigma}\right) - 1 , \text{ for } j=1,\dots, J. \e
- Workflowフェーズ: **Model development / debugging**
- 実務での読み方: 小さいモデルから始め、失敗runを観察しながらモデル族・prior・データ処理を段階的に拡張する。
- MLflow連携: `iteration_id, change_reason, failure_mode, hypothesis, next_action`
- 参照: [公式ページ](https://avehtari.github.io/Bayesian-Workflow/golf/golf.html#fig-golf-angle-curves) / [ソース候補](https://github.com/avehtari/Bayesian-Workflow/blob/eb00fa4397314ef7d90203382542bd44c590e289/golf/golf.R)

#### `golf-golf/fig-golf-fit-1-2`

- 種別: `figure` / 公式ID: `fig-golf-fit-1-2` / ページ内順序: 6
- caption/列: Figure 6
- 周辺文脈（EN）: We next plot the data and the fitted model (here using the posterior median of \sigma but in this case the uncertainty is so narrow that any reasonable posterior summary would give
- 周辺文脈（JA, 自動訳）: 4 第一原理に基づくモデリング / 次に、データと近似モデルをプロットします (ここでは \sigma の事後中央値を使用していますが、この場合、不確実性が非常に狭いため、合理的な事後サマリーが得られるでしょう)
- Workflowフェーズ: **EDA / observed data**
- 実務での読み方: モデル化前に、観測単位・外れ値・欠測・群構造・時系列性・上限/下限などを確認する。MLflowではデータ版と前処理版を固定する。
- MLflow連携: `dataset_uri, dataset_hash, preprocessing_version, n_obs, group_count`
- 参照: [公式ページ](https://avehtari.github.io/Bayesian-Workflow/golf/golf.html#fig-golf-fit-1-2) / [ソース候補](https://github.com/avehtari/Bayesian-Workflow/blob/eb00fa4397314ef7d90203382542bd44c590e289/golf/golf.R)

#### `golf-golf/fig-golf-fit-2-new`

- 種別: `figure` / 公式ID: `fig-golf-fit-2-new` / ページ内順序: 7
- caption/列: Figure 7
- 周辺文脈（EN）: Several years after fitting the above model, we were presented with a newer and more comprehensive dataset on professional golf putting ( Broadie 2018 ) . For simplicity we’ll just
- 周辺文脈（JA, 自動訳）: 5 新しいデータで当てはめたモデルをテスト / 上記のモデルを当てはめてから数年後、プロのゴルフのパッティングに関する、より新しく、より包括的なデータセットが提示されました (Broadie 2018)。簡単にするために、次のようにします
- Workflowフェーズ: **EDA / observed data**
- 実務での読み方: モデル化前に、観測単位・外れ値・欠測・群構造・時系列性・上限/下限などを確認する。MLflowではデータ版と前処理版を固定する。
- MLflow連携: `dataset_uri, dataset_hash, preprocessing_version, n_obs, group_count`
- 参照: [公式ページ](https://avehtari.github.io/Bayesian-Workflow/golf/golf.html#fig-golf-fit-2-new) / [ソース候補](https://github.com/avehtari/Bayesian-Workflow/blob/eb00fa4397314ef7d90203382542bd44c590e289/golf/golf.R)

#### `golf-golf/fig-golf-sketch-3`

- 種別: `figure` / 公式ID: `fig-golf-sketch-3` / ページ内順序: 8
- caption/列: Figure 8
- 周辺文脈（EN）: The following sketch, which is not to scale, illustrates the need for the distance as angle as well as the angle of the shot to be in some range, in this case the gray zone which r
- 周辺文脈（JA, 自動訳）: 6 ボールがどれだけ強く打たれるかを考慮した新しいモデル / 次のスケッチは縮尺通りではありませんが、ショットの角度だけでなく距離も一定の範囲内に収める必要があることを示しています。この場合はグレーゾーンです。
- Workflowフェーズ: **Model development / debugging**
- 実務での読み方: 小さいモデルから始め、失敗runを観察しながらモデル族・prior・データ処理を段階的に拡張する。
- MLflow連携: `iteration_id, change_reason, failure_mode, hypothesis, next_action`
- 参照: [公式ページ](https://avehtari.github.io/Bayesian-Workflow/golf/golf.html#fig-golf-sketch-3) / [ソース候補](https://github.com/avehtari/Bayesian-Workflow/blob/eb00fa4397314ef7d90203382542bd44c590e289/golf/golf.R)

#### `golf-golf/fig-golf-fit-3`

- 種別: `figure` / 公式ID: `fig-golf-fit-3` / ページ内順序: 9
- caption/列: Figure 9
- 周辺文脈（EN）: Now the convergence looks fine. We graph the new data and the fitted model:
- 周辺文脈（JA, 自動訳）: 6 ボールがどれだけ強く打たれるかを考慮した新しいモデル / 収束は問題なく見えるようになりました。新しいデータと適合モデルをグラフ化します。
- Workflowフェーズ: **EDA / observed data**
- 実務での読み方: モデル化前に、観測単位・外れ値・欠測・群構造・時系列性・上限/下限などを確認する。MLflowではデータ版と前処理版を固定する。
- MLflow連携: `dataset_uri, dataset_hash, preprocessing_version, n_obs, group_count`
- 参照: [公式ページ](https://avehtari.github.io/Bayesian-Workflow/golf/golf.html#fig-golf-fit-3) / [ソース候補](https://github.com/avehtari/Bayesian-Workflow/blob/eb00fa4397314ef7d90203382542bd44c590e289/golf/golf.R)

#### `golf-golf/fig-golf-fit-4`

- 種別: `figure` / 公式ID: `fig-golf-fit-4` / ページ内順序: 10
- caption/列: Figure 10
- 周辺文脈（EN）: And now we graph:
- 周辺文脈（JA, 自動訳）: 7 ファッジ係数を含めてモデルを拡張 / そして、次のグラフを作成します。
- Workflowフェーズ: **Model development / debugging**
- 実務での読み方: 小さいモデルから始め、失敗runを観察しながらモデル族・prior・データ処理を段階的に拡張する。
- MLflow連携: `iteration_id, change_reason, failure_mode, hypothesis, next_action`
- 参照: [公式ページ](https://avehtari.github.io/Bayesian-Workflow/golf/golf.html#fig-golf-fit-4) / [ソース候補](https://github.com/avehtari/Bayesian-Workflow/blob/eb00fa4397314ef7d90203382542bd44c590e289/golf/golf.R)

#### `golf-golf/fig-golf-res-4`

- 種別: `figure` / 公式ID: `fig-golf-res-4` / ページ内順序: 11
- caption/列: Figure 11
- 周辺文脈（EN）: Then we compute the posterior means of the residuals, y_j/n_j - p_j , then plot these vs. distance:
- 周辺文脈（JA, 自動訳）: 7 ファッジ係数を含めてモデルを拡張 / 次に、残差の事後平均 y_j/n_j - p_j を計算し、これらを距離に対してプロットします。
- Workflowフェーズ: **Posterior summary / effect interpretation**
- 実務での読み方: 推定効果・不確実性・派生量を意思決定に接続する。平均だけでなく区間・分布・実務閾値超過確率を残す。
- MLflow連携: `posterior_draws_uri, model_code_hash, ci_width, decision_threshold_prob`
- 参照: [公式ページ](https://avehtari.github.io/Bayesian-Workflow/golf/golf.html#fig-golf-res-4) / [ソース候補](https://github.com/avehtari/Bayesian-Workflow/blob/eb00fa4397314ef7d90203382542bd44c590e289/golf/golf.R)

#### `golf-golf/fig-golf-fit-5`

- 種別: `figure` / 公式ID: `fig-golf-fit-5` / ページ内順序: 12
- caption/列: Figure 12
- 周辺文脈（EN）: The sampling is slower than for earlier models, but the convergence diagnostic look just fine. We graph the new data and the fitted model:
- 周辺文脈（JA, 自動訳）: 8 ロジット スケールに誤差のある二項分布 / サンプリングは以前のモデルよりも遅くなりますが、収束診断は問題なく表示されます。新しいデータと適合モデルをグラフ化します。
- Workflowフェーズ: **EDA / observed data**
- 実務での読み方: モデル化前に、観測単位・外れ値・欠測・群構造・時系列性・上限/下限などを確認する。MLflowではデータ版と前処理版を固定する。
- MLflow連携: `dataset_uri, dataset_hash, preprocessing_version, n_obs, group_count`
- 参照: [公式ページ](https://avehtari.github.io/Bayesian-Workflow/golf/golf.html#fig-golf-fit-5) / [ソース候補](https://github.com/avehtari/Bayesian-Workflow/blob/eb00fa4397314ef7d90203382542bd44c590e289/golf/golf.R)

#### `golf-golf/fig-golf-fit-6`

- 種別: `figure` / 公式ID: `fig-golf-fit-6` / ページ内順序: 13
- caption/列: Figure 13
- 周辺文脈（EN）: We graph the new data and the fitted model:
- 周辺文脈（JA, 自動訳）: 9 比例誤差のある二項分布 / 新しいデータと適合モデルをグラフ化します。
- Workflowフェーズ: **EDA / observed data**
- 実務での読み方: モデル化前に、観測単位・外れ値・欠測・群構造・時系列性・上限/下限などを確認する。MLflowではデータ版と前処理版を固定する。
- MLflow連携: `dataset_uri, dataset_hash, preprocessing_version, n_obs, group_count`
- 参照: [公式ページ](https://avehtari.github.io/Bayesian-Workflow/golf/golf.html#fig-golf-fit-6) / [ソース候補](https://github.com/avehtari/Bayesian-Workflow/blob/eb00fa4397314ef7d90203382542bd44c590e289/golf/golf.R)

#### `golf-golf/fig-golf-res-6`

- 種別: `figure` / 公式ID: `fig-golf-res-6` / ページ内順序: 14
- caption/列: Figure 14
- 周辺文脈（EN）: We graph the new data and the fitted model:
- 周辺文脈（JA, 自動訳）: 9 比例誤差のある二項分布 / 新しいデータと適合モデルをグラフ化します。
- Workflowフェーズ: **EDA / observed data**
- 実務での読み方: モデル化前に、観測単位・外れ値・欠測・群構造・時系列性・上限/下限などを確認する。MLflowではデータ版と前処理版を固定する。
- MLflow連携: `dataset_uri, dataset_hash, preprocessing_version, n_obs, group_count`
- 参照: [公式ページ](https://avehtari.github.io/Bayesian-Workflow/golf/golf.html#fig-golf-res-6) / [ソース候補](https://github.com/avehtari/Bayesian-Workflow/blob/eb00fa4397314ef7d90203382542bd44c590e289/golf/golf.R)

#### `golf-golf/fig-golf-fit-7`

- 種別: `figure` / 公式ID: `fig-golf-fit-7` / ページ内順序: 15
- caption/列: Figure 15
- 周辺文脈（EN）: We graph the new data and the fitted model:
- 周辺文脈（JA, 自動訳）: 9 比例誤差のある二項分布 / 新しいデータと適合モデルをグラフ化します。
- Workflowフェーズ: **EDA / observed data**
- 実務での読み方: モデル化前に、観測単位・外れ値・欠測・群構造・時系列性・上限/下限などを確認する。MLflowではデータ版と前処理版を固定する。
- MLflow連携: `dataset_uri, dataset_hash, preprocessing_version, n_obs, group_count`
- 参照: [公式ページ](https://avehtari.github.io/Bayesian-Workflow/golf/golf.html#fig-golf-fit-7) / [ソース候補](https://github.com/avehtari/Bayesian-Workflow/blob/eb00fa4397314ef7d90203382542bd44c590e289/golf/golf.R)

#### `golf-golf/fig-golf-res-7`

- 種別: `figure` / 公式ID: `fig-golf-res-7` / ページ内順序: 16
- caption/列: Figure 16
- 周辺文脈（EN）: We graph the new data and the fitted model:
- 周辺文脈（JA, 自動訳）: 9 比例誤差のある二項分布 / 新しいデータと適合モデルをグラフ化します。
- Workflowフェーズ: **EDA / observed data**
- 実務での読み方: モデル化前に、観測単位・外れ値・欠測・群構造・時系列性・上限/下限などを確認する。MLflowではデータ版と前処理版を固定する。
- MLflow連携: `dataset_uri, dataset_hash, preprocessing_version, n_obs, group_count`
- 参照: [公式ページ](https://avehtari.github.io/Bayesian-Workflow/golf/golf.html#fig-golf-res-7) / [ソース候補](https://github.com/avehtari/Bayesian-Workflow/blob/eb00fa4397314ef7d90203382542bd44c590e289/golf/golf.R)

#### `golf-golf/fig-golf-fit-8`

- 種別: `figure` / 公式ID: `fig-golf-fit-8` / ページ内順序: 17
- caption/列: Figure 17
- 周辺文脈（EN）: We graph the new data and the fitted model:
- 周辺文脈（JA, 自動訳）: 9 比例誤差のある二項分布 / 新しいデータと適合モデルをグラフ化します。
- Workflowフェーズ: **EDA / observed data**
- 実務での読み方: モデル化前に、観測単位・外れ値・欠測・群構造・時系列性・上限/下限などを確認する。MLflowではデータ版と前処理版を固定する。
- MLflow連携: `dataset_uri, dataset_hash, preprocessing_version, n_obs, group_count`
- 参照: [公式ページ](https://avehtari.github.io/Bayesian-Workflow/golf/golf.html#fig-golf-fit-8) / [ソース候補](https://github.com/avehtari/Bayesian-Workflow/blob/eb00fa4397314ef7d90203382542bd44c590e289/golf/golf.R)

#### `golf-golf/fig-golf-res-8`

- 種別: `figure` / 公式ID: `fig-golf-res-8` / ページ内順序: 18
- caption/列: Figure 18
- 周辺文脈（EN）: We graph the new data and the fitted model:
- 周辺文脈（JA, 自動訳）: 9 比例誤差のある二項分布 / 新しいデータと適合モデルをグラフ化します。
- Workflowフェーズ: **EDA / observed data**
- 実務での読み方: モデル化前に、観測単位・外れ値・欠測・群構造・時系列性・上限/下限などを確認する。MLflowではデータ版と前処理版を固定する。
- MLflow連携: `dataset_uri, dataset_hash, preprocessing_version, n_obs, group_count`
- 参照: [公式ページ](https://avehtari.github.io/Bayesian-Workflow/golf/golf.html#fig-golf-res-8) / [ソース候補](https://github.com/avehtari/Bayesian-Workflow/blob/eb00fa4397314ef7d90203382542bd44c590e289/golf/golf.R)

#### `golf-golf/fig-mcmc-scatter-tolerance-overshot`

- 種別: `figure` / 公式ID: `fig-mcmc-scatter-tolerance-overshot` / ページ内順序: 19
- caption/列: Figure 19
- 周辺文脈（EN）: However, when we examine the bivariate posterior we see strong dependency and their ratio is well informed by the likelihood. The posterior standard deviation of the ratio is one f
- 周辺文脈（JA, 自動訳）: 9 比例誤差のある二項分布 / ただし、事後二変量を調べると、強い依存関係が見られ、それらの比は尤度によって十分に情報が得られます。比率の事後標準偏差は 1 f です。
- Workflowフェーズ: **Posterior summary / effect interpretation**
- 実務での読み方: 推定効果・不確実性・派生量を意思決定に接続する。平均だけでなく区間・分布・実務閾値超過確率を残す。
- MLflow連携: `posterior_draws_uri, model_code_hash, ci_width, decision_threshold_prob`
- 参照: [公式ページ](https://avehtari.github.io/Bayesian-Workflow/golf/golf.html#fig-mcmc-scatter-tolerance-overshot) / [ソース候補](https://github.com/avehtari/Bayesian-Workflow/blob/eb00fa4397314ef7d90203382542bd44c590e289/golf/golf.R)

#### `golf-golf/fig-golf-fit-11`

- 種別: `figure` / 公式ID: `fig-golf-fit-11` / ページ内順序: 20
- caption/列: Figure 20
- 周辺文脈（EN）: We graph the new data and the fitted model 11:
- 周辺文脈（JA, 自動訳）: 10 単純化された誤差項を含む二項分布 / 新しいデータと適合モデルをグラフ化します。 11:
- Workflowフェーズ: **EDA / observed data**
- 実務での読み方: モデル化前に、観測単位・外れ値・欠測・群構造・時系列性・上限/下限などを確認する。MLflowではデータ版と前処理版を固定する。
- MLflow連携: `dataset_uri, dataset_hash, preprocessing_version, n_obs, group_count`
- 参照: [公式ページ](https://avehtari.github.io/Bayesian-Workflow/golf/golf.html#fig-golf-fit-11) / [ソース候補](https://github.com/avehtari/Bayesian-Workflow/blob/eb00fa4397314ef7d90203382542bd44c590e289/golf/golf.R)

#### `golf-golf/fig-golf-res-11`

- 種別: `figure` / 公式ID: `fig-golf-res-11` / ページ内順序: 21
- caption/列: Figure 21
- 周辺文脈（EN）: We graph the new data and the fitted model 11:
- 周辺文脈（JA, 自動訳）: 10 単純化された誤差項を含む二項分布 / 新しいデータと適合モデルをグラフ化します。 11:
- Workflowフェーズ: **EDA / observed data**
- 実務での読み方: モデル化前に、観測単位・外れ値・欠測・群構造・時系列性・上限/下限などを確認する。MLflowではデータ版と前処理版を固定する。
- MLflow連携: `dataset_uri, dataset_hash, preprocessing_version, n_obs, group_count`
- 参照: [公式ページ](https://avehtari.github.io/Bayesian-Workflow/golf/golf.html#fig-golf-res-11) / [ソース候補](https://github.com/avehtari/Bayesian-Workflow/blob/eb00fa4397314ef7d90203382542bd44c590e289/golf/golf.R)

#### `golf-golf/figure-022`

- 種別: `figure` / 公式ID: `(none)` / ページ内順序: 22
- caption/列: figure 22
- 周辺文脈（EN）: If we examine the predictive performance difference at different distances, we see that the constant error model tends to be worse specifically at short distances.
- 周辺文脈（JA, 自動訳）: 10 簡略化された誤差項を使用した二項式 / さまざまな距離での予測パフォーマンスの違いを調べると、一定誤差モデルは、特に短距離で悪化する傾向があることがわかります。
- Workflowフェーズ: **Model development / debugging**
- 実務での読み方: 小さいモデルから始め、失敗runを観察しながらモデル族・prior・データ処理を段階的に拡張する。
- MLflow連携: `iteration_id, change_reason, failure_mode, hypothesis, next_action`
- 参照: [公式ページ](https://avehtari.github.io/Bayesian-Workflow/golf/golf.html) / [ソース候補](https://github.com/avehtari/Bayesian-Workflow/blob/eb00fa4397314ef7d90203382542bd44c590e289/golf/golf.R)

### Model building with latent variables: Markov models for animal movement

- ページ: <https://avehtari.github.io/Bayesian-Workflow/sharks/sharks.html>
- ソース候補: <https://github.com/avehtari/Bayesian-Workflow/blob/eb00fa4397314ef7d90203382542bd44c590e289/sharks/sharks.R>

#### `sharks-sharks/fig-sarika_tracks_1_10`

- 種別: `figure` / 公式ID: `fig-sarika_tracks_1_10` / ページ内順序: 1
- caption/列: Figure 1
- 周辺文脈（EN）: We plot two tracks of white shark female 1 that exhibit the distinct movement patterns we are hoping to capture with our HMM:
- 周辺文脈（JA, 自動訳）: 2 サメの動きのデータ / HMM でキャプチャしたいと考えている明確な動きのパターンを示すホホジロザメのメス 1 の 2 つの軌跡をプロットします。
- Workflowフェーズ: **EDA / observed data**
- 実務での読み方: モデル化前に、観測単位・外れ値・欠測・群構造・時系列性・上限/下限などを確認する。MLflowではデータ版と前処理版を固定する。
- MLflow連携: `dataset_uri, dataset_hash, preprocessing_version, n_obs, group_count`
- 参照: [公式ページ](https://avehtari.github.io/Bayesian-Workflow/sharks/sharks.html#fig-sarika_tracks_1_10) / [ソース候補](https://github.com/avehtari/Bayesian-Workflow/blob/eb00fa4397314ef7d90203382542bd44c590e289/sharks/sharks.R)

#### `sharks-sharks/fig-mcmc_hist_by_chain_2state`

- 種別: `figure` / 公式ID: `fig-mcmc_hist_by_chain_2state` / ページ内順序: 2
- caption/列: Figure 2
- 周辺文脈（EN）: Plot MCMC marginal distributions for certain parameters:
- 周辺文脈（JA, 自動訳）: 4 2 状態 HMM / 特定のパラメーターの MCMC 周辺分布をプロットします。
- Workflowフェーズ: **Model development / debugging**
- 実務での読み方: 小さいモデルから始め、失敗runを観察しながらモデル族・prior・データ処理を段階的に拡張する。
- MLflow連携: `iteration_id, change_reason, failure_mode, hypothesis, next_action`
- 参照: [公式ページ](https://avehtari.github.io/Bayesian-Workflow/sharks/sharks.html#fig-mcmc_hist_by_chain_2state) / [ソース候補](https://github.com/avehtari/Bayesian-Workflow/blob/eb00fa4397314ef7d90203382542bd44c590e289/sharks/sharks.R)

#### `sharks-sharks/fig-hmm_2state_distributions`

- 種別: `figure` / 公式ID: `fig-hmm_2state_distributions` / ページ内順序: 3
- caption/列: Figure 3
- 周辺文脈（EN）: Plot state-dependent distributions for step length and turning angle:
- 周辺文脈（JA, 自動訳）: 4 2 状態 HMM / ステップ長と回転角度の状態依存分布をプロットします。
- Workflowフェーズ: **Model development / debugging**
- 実務での読み方: 小さいモデルから始め、失敗runを観察しながらモデル族・prior・データ処理を段階的に拡張する。
- MLflow連携: `iteration_id, change_reason, failure_mode, hypothesis, next_action`
- 参照: [公式ページ](https://avehtari.github.io/Bayesian-Workflow/sharks/sharks.html#fig-hmm_2state_distributions) / [ソース候補](https://github.com/avehtari/Bayesian-Workflow/blob/eb00fa4397314ef7d90203382542bd44c590e289/sharks/sharks.R)

#### `sharks-sharks/fig-hmm_2state_decodings`

- 種別: `figure` / 公式ID: `fig-hmm_2state_decodings` / ページ内順序: 4
- caption/列: Figure 4
- 周辺文脈（EN）: Plot state-decodings onto track using the forward-backward algorithm for local state-decoding:
- 周辺文脈（JA, 自動訳）: 4 2 状態 HMM / ローカル状態デコード用の前方後方アルゴリズムを使用して、状態デコードをトラック上にプロットします。
- Workflowフェーズ: **Model development / debugging**
- 実務での読み方: 小さいモデルから始め、失敗runを観察しながらモデル族・prior・データ処理を段階的に拡張する。
- MLflow連携: `iteration_id, change_reason, failure_mode, hypothesis, next_action`
- 参照: [公式ページ](https://avehtari.github.io/Bayesian-Workflow/sharks/sharks.html#fig-hmm_2state_decodings) / [ソース候補](https://github.com/avehtari/Bayesian-Workflow/blob/eb00fa4397314ef7d90203382542bd44c590e289/sharks/sharks.R)

#### `sharks-sharks/fig-hmm_2state_decodings2`

- 種別: `figure` / 公式ID: `fig-hmm_2state_decodings2` / ページ内順序: 5
- caption/列: Figure 5
- 周辺文脈（EN）: Plot state-decodings onto track using the forward-backward algorithm for local state-decoding:
- 周辺文脈（JA, 自動訳）: 4 2 状態 HMM / ローカル状態デコード用の前方後方アルゴリズムを使用して、状態デコードをトラック上にプロットします。
- Workflowフェーズ: **Model development / debugging**
- 実務での読み方: 小さいモデルから始め、失敗runを観察しながらモデル族・prior・データ処理を段階的に拡張する。
- MLflow連携: `iteration_id, change_reason, failure_mode, hypothesis, next_action`
- 参照: [公式ページ](https://avehtari.github.io/Bayesian-Workflow/sharks/sharks.html#fig-hmm_2state_decodings2) / [ソース候補](https://github.com/avehtari/Bayesian-Workflow/blob/eb00fa4397314ef7d90203382542bd44c590e289/sharks/sharks.R)

#### `sharks-sharks/fig-hmm_2state_pseudo_residuals`

- 種別: `figure` / 公式ID: `fig-hmm_2state_pseudo_residuals` / ページ内順序: 6
- caption/列: Figure 6
- 周辺文脈（EN）: Plot pseudo-residuals
- 周辺文脈（JA, 自動訳）: 4 2 状態 HMM / 擬似残差のプロット
- Workflowフェーズ: **Model development / debugging**
- 実務での読み方: 小さいモデルから始め、失敗runを観察しながらモデル族・prior・データ処理を段階的に拡張する。
- MLflow連携: `iteration_id, change_reason, failure_mode, hypothesis, next_action`
- 参照: [公式ページ](https://avehtari.github.io/Bayesian-Workflow/sharks/sharks.html#fig-hmm_2state_pseudo_residuals) / [ソース候補](https://github.com/avehtari/Bayesian-Workflow/blob/eb00fa4397314ef7d90203382542bd44c590e289/sharks/sharks.R)

#### `sharks-sharks/fig-hmm_2state_decoding_histograms`

- 種別: `figure` / 公式ID: `fig-hmm_2state_decoding_histograms` / ページ内順序: 7
- caption/列: Figure 7
- 周辺文脈（EN）: Simulate data from posterior predictive distribution of fitted 2-state HMM
- 周辺文脈（JA, 自動訳）: 4 2 状態 HMM / 近似された 2 状態 HMM の事後予測分布からのデータをシミュレート
- Workflowフェーズ: **EDA / observed data**
- 実務での読み方: モデル化前に、観測単位・外れ値・欠測・群構造・時系列性・上限/下限などを確認する。MLflowではデータ版と前処理版を固定する。
- MLflow連携: `dataset_uri, dataset_hash, preprocessing_version, n_obs, group_count`
- 参照: [公式ページ](https://avehtari.github.io/Bayesian-Workflow/sharks/sharks.html#fig-hmm_2state_decoding_histograms) / [ソース候補](https://github.com/avehtari/Bayesian-Workflow/blob/eb00fa4397314ef7d90203382542bd44c590e289/sharks/sharks.R)

#### `sharks-sharks/fig-hmm_2state_tpmcov_crencp_transitions-1`

- 種別: `figure` / 公式ID: `fig-hmm_2state_tpmcov_crencp_transitions-1` / ページ内順序: 8
- caption/列: Figure 8
- 周辺文脈（EN）: Plot entries of transition probability matrix with covariates and individual varying effects:
- 周辺文脈（JA, 自動訳）: 遷移確率行列と個別変動効果における 6 つの 2 状態 HMM 共変量 / 共変量と個別変動効果を含む遷移確率行列のエントリをプロットする:
- Workflowフェーズ: **Posterior summary / effect interpretation**
- 実務での読み方: 推定効果・不確実性・派生量を意思決定に接続する。平均だけでなく区間・分布・実務閾値超過確率を残す。
- MLflow連携: `posterior_draws_uri, model_code_hash, ci_width, decision_threshold_prob`
- 参照: [公式ページ](https://avehtari.github.io/Bayesian-Workflow/sharks/sharks.html#fig-hmm_2state_tpmcov_crencp_transitions-1) / [ソース候補](https://github.com/avehtari/Bayesian-Workflow/blob/eb00fa4397314ef7d90203382542bd44c590e289/sharks/sharks.R)

#### `sharks-sharks/fig-hmm_2state_tpmcov_crencp_transitions-2`

- 種別: `figure` / 公式ID: `fig-hmm_2state_tpmcov_crencp_transitions-2` / ページ内順序: 9
- caption/列: Figure 9
- 周辺文脈（EN）: Plot entries of transition probability matrix with covariates and individual varying effects:
- 周辺文脈（JA, 自動訳）: 遷移確率行列と個別変動効果における 6 つの 2 状態 HMM 共変量 / 共変量と個別変動効果を含む遷移確率行列のエントリをプロットする:
- Workflowフェーズ: **Posterior summary / effect interpretation**
- 実務での読み方: 推定効果・不確実性・派生量を意思決定に接続する。平均だけでなく区間・分布・実務閾値超過確率を残す。
- MLflow連携: `posterior_draws_uri, model_code_hash, ci_width, decision_threshold_prob`
- 参照: [公式ページ](https://avehtari.github.io/Bayesian-Workflow/sharks/sharks.html#fig-hmm_2state_tpmcov_crencp_transitions-2) / [ソース候補](https://github.com/avehtari/Bayesian-Workflow/blob/eb00fa4397314ef7d90203382542bd44c590e289/sharks/sharks.R)

#### `sharks-sharks/fig-2state_tpmcov_crencp`

- 種別: `figure` / 公式ID: `fig-2state_tpmcov_crencp` / ページ内順序: 10
- caption/列: Figure 10
- 周辺文脈（EN）: Plot entries of transition probability matrix with covariates and individual varying effects:
- 周辺文脈（JA, 自動訳）: 遷移確率行列と個別変動効果における 6 つの 2 状態 HMM 共変量 / 共変量と個別変動効果を含む遷移確率行列のエントリをプロットする:
- Workflowフェーズ: **Posterior summary / effect interpretation**
- 実務での読み方: 推定効果・不確実性・派生量を意思決定に接続する。平均だけでなく区間・分布・実務閾値超過確率を残す。
- MLflow連携: `posterior_draws_uri, model_code_hash, ci_width, decision_threshold_prob`
- 参照: [公式ページ](https://avehtari.github.io/Bayesian-Workflow/sharks/sharks.html#fig-2state_tpmcov_crencp) / [ソース候補](https://github.com/avehtari/Bayesian-Workflow/blob/eb00fa4397314ef7d90203382542bd44c590e289/sharks/sharks.R)

### Model building: Time-series decomposition for birthdays

- ページ: <https://avehtari.github.io/Bayesian-Workflow/birthdays/birthdays.html>
- ソース候補: <https://github.com/avehtari/Bayesian-Workflow/blob/eb00fa4397314ef7d90203382542bd44c590e289/birthdays/birthdays.R>

#### `birthdays-birthdays/fig-births-data-all`

- 種別: `figure` / 公式ID: `fig-births-data-all` / ページ内順序: 1
- caption/列: Figure 1
- 周辺文脈（EN）: We can see slow variation in trend, yearly pattern, and especially in the later years spread to lower and higher values.
- 周辺文脈（JA, 自動訳）: 2.1 すべての出生をプロットする / 傾向や年次パターンにゆっくりとした変動が見られ、特に晩年にはより低い値とより高い値に広がっていることがわかります。
- Workflowフェーズ: **EDA / observed data**
- 実務での読み方: モデル化前に、観測単位・外れ値・欠測・群構造・時系列性・上限/下限などを確認する。MLflowではデータ版と前処理版を固定する。
- MLflow連携: `dataset_uri, dataset_hash, preprocessing_version, n_obs, group_count`
- 参照: [公式ページ](https://avehtari.github.io/Bayesian-Workflow/birthdays/birthdays.html#fig-births-data-all) / [ソース候補](https://github.com/avehtari/Bayesian-Workflow/blob/eb00fa4397314ef7d90203382542bd44c590e289/birthdays/birthdays.R)

#### `birthdays-birthdays/fig-births-data-all-relative`

- 種別: `figure` / 公式ID: `fig-births-data-all-relative` / ページ内順序: 2
- caption/列: Figure 2
- 周辺文脈（EN）: To make the interpretation we switch to examine the relative change, with the mean level denoted with 100.
- 周辺文脈（JA, 自動訳）: 2.2 すべての出生を平均に対する相対としてプロットする / 解釈を行うために、平均レベルを 100 で示した相対的な変化を調べるように切り替えます。
- Workflowフェーズ: **EDA / observed data**
- 実務での読み方: モデル化前に、観測単位・外れ値・欠測・群構造・時系列性・上限/下限などを確認する。MLflowではデータ版と前処理版を固定する。
- MLflow連携: `dataset_uri, dataset_hash, preprocessing_version, n_obs, group_count`
- 参照: [公式ページ](https://avehtari.github.io/Bayesian-Workflow/birthdays/birthdays.html#fig-births-data-all-relative) / [ソース候補](https://github.com/avehtari/Bayesian-Workflow/blob/eb00fa4397314ef7d90203382542bd44c590e289/birthdays/birthdays.R)

#### `birthdays-birthdays/fig-births-per-day-of-year`

- 種別: `figure` / 公式ID: `fig-births-per-day-of-year` / ページ内順序: 3
- caption/列: Figure 3
- 周辺文脈（EN）: We can see the generic pattern in yearly seasonal trend simply by averaging over each day of year (day_of_year has numbers from 1 to 366 every year with leap day being 60 and 1st M
- 周辺文脈（JA, 自動訳）: 2.3 年間の日ごとの平均をプロットする / 年間の各日を平均するだけで、年間の季節傾向の一般的なパターンがわかります (day_of_year には毎年 1 から 366 までの数値があり、うるう日は 60 日と最初の M 日です)
- Workflowフェーズ: **Model development / debugging**
- 実務での読み方: 小さいモデルから始め、失敗runを観察しながらモデル族・prior・データ処理を段階的に拡張する。
- MLflow連携: `iteration_id, change_reason, failure_mode, hypothesis, next_action`
- 参照: [公式ページ](https://avehtari.github.io/Bayesian-Workflow/birthdays/birthdays.html#fig-births-per-day-of-year) / [ソース候補](https://github.com/avehtari/Bayesian-Workflow/blob/eb00fa4397314ef7d90203382542bd44c590e289/birthdays/birthdays.R)

#### `birthdays-birthdays/fig-births-per-day-of-week`

- 種別: `figure` / 公式ID: `fig-births-per-day-of-week` / ページ内順序: 4
- caption/列: Figure 4
- 周辺文脈（EN）: We can see the generic pattern in weekly trend simply by averaging over each day of week.
- 周辺文脈（JA, 自動訳）: 2.4 曜日ごとの平均をプロットする / 曜日ごとに平均を取るだけで、週ごとの傾向の一般的なパターンがわかります。
- Workflowフェーズ: **Model development / debugging**
- 実務での読み方: 小さいモデルから始め、失敗runを観察しながらモデル族・prior・データ処理を段階的に拡張する。
- MLflow連携: `iteration_id, change_reason, failure_mode, hypothesis, next_action`
- 参照: [公式ページ](https://avehtari.github.io/Bayesian-Workflow/birthdays/birthdays.html#fig-births-per-day-of-week) / [ソース候補](https://github.com/avehtari/Bayesian-Workflow/blob/eb00fa4397314ef7d90203382542bd44c590e289/birthdays/birthdays.R)

#### `birthdays-birthdays/fig-births-opt1-vs-data`

- 種別: `figure` / 公式ID: `fig-births-opt1-vs-data` / ページ内順序: 5
- caption/列: Figure 5
- 周辺文脈（EN）: Compare the model to the data
- 周辺文脈（JA, 自動訳）: 5.1 Model 1: Slow trend / Compare the model to the data
- Workflowフェーズ: **EDA / observed data**
- 実務での読み方: モデル化前に、観測単位・外れ値・欠測・群構造・時系列性・上限/下限などを確認する。MLflowではデータ版と前処理版を固定する。
- MLflow連携: `dataset_uri, dataset_hash, preprocessing_version, n_obs, group_count`
- 参照: [公式ページ](https://avehtari.github.io/Bayesian-Workflow/birthdays/birthdays.html#fig-births-opt1-vs-data) / [ソース候補](https://github.com/avehtari/Bayesian-Workflow/blob/eb00fa4397314ef7d90203382542bd44c590e289/birthdays/birthdays.R)

#### `birthdays-birthdays/fig-births-fit1-trace`

- 種別: `figure` / 公式ID: `fig-births-fit1-trace` / ページ内順序: 6
- caption/列: Figure 6
- 周辺文脈（EN）: Trace plot shows slow mixing but no multimodality.
- 周辺文脈（JA, 自動訳）: 5.1 モデル 1: 遅い傾向 / トレース プロットは、混合が遅いことを示していますが、マルチモダリティはありません。
- Workflowフェーズ: **MCMC / computation diagnostics**
- 実務での読み方: 推論結果を解釈する前に、R-hat、ESS、divergence、treedepth、BFMI、trace/pairsを確認する。悪いrunは比較表から除外せず失敗として記録する。
- MLflow連携: `rhat_max, ess_bulk_min, ess_tail_min, divergences, treedepth_hits, bfmi_min`
- 参照: [公式ページ](https://avehtari.github.io/Bayesian-Workflow/birthdays/birthdays.html#fig-births-fit1-trace) / [ソース候補](https://github.com/avehtari/Bayesian-Workflow/blob/eb00fa4397314ef7d90203382542bd44c590e289/birthdays/birthdays.R)

#### `birthdays-birthdays/fig-births-fit1-vs-data`

- 種別: `figure` / 公式ID: `fig-births-fit1-vs-data` / ページ内順序: 7
- caption/列: Figure 7
- 周辺文脈（EN）: The model result from short MCMC chains looks very similar to the optimization result.
- 周辺文脈（JA, 自動訳）: 5.1 モデル 1: 緩やかな傾向 / 短い MCMC チェーンからのモデルの結果は、最適化の結果と非常によく似ています。
- Workflowフェーズ: **EDA / observed data**
- 実務での読み方: モデル化前に、観測単位・外れ値・欠測・群構造・時系列性・上限/下限などを確認する。MLflowではデータ版と前処理版を固定する。
- MLflow連携: `dataset_uri, dataset_hash, preprocessing_version, n_obs, group_count`
- 参照: [公式ページ](https://avehtari.github.io/Bayesian-Workflow/birthdays/birthdays.html#fig-births-fit1-vs-data) / [ソース候補](https://github.com/avehtari/Bayesian-Workflow/blob/eb00fa4397314ef7d90203382542bd44c590e289/birthdays/birthdays.R)

#### `birthdays-birthdays/fig-births-opt1-vs-fit1`

- 種別: `figure` / 公式ID: `fig-births-opt1-vs-fit1` / ページ内順序: 8
- caption/列: Figure 8
- 周辺文脈（EN）: If we compare the result from short sampling to optimizing, we don’t see practical difference in the predictions (although we see later more differences between optimization and MC
- 周辺文脈（JA, 自動訳）: 5.1 モデル 1: 緩やかな傾向 / ショート サンプリングの結果と最適化の結果を比較すると、予測に実質的な違いは見られません (ただし、後で最適化と MC の間のさらなる違いがわかります)
- Workflowフェーズ: **Model development / debugging**
- 実務での読み方: 小さいモデルから始め、失敗runを観察しながらモデル族・prior・データ処理を段階的に拡張する。
- MLflow連携: `iteration_id, change_reason, failure_mode, hypothesis, next_action`
- 参照: [公式ページ](https://avehtari.github.io/Bayesian-Workflow/birthdays/birthdays.html#fig-births-opt1-vs-fit1) / [ソース候補](https://github.com/avehtari/Bayesian-Workflow/blob/eb00fa4397314ef7d90203382542bd44c590e289/birthdays/birthdays.R)

#### `birthdays-birthdays/fig-births-fit1b-trace`

- 種別: `figure` / 公式ID: `fig-births-fit1b-trace` / ページ内順序: 9
- caption/列: Figure 9
- 周辺文脈（EN）: Examining the trace plots don’t show multimodality
- 周辺文脈（JA, 自動訳）: 5.1 モデル 1: 緩やかな傾向 / トレース プロットを調べてもマルチモダリティが示されない
- Workflowフェーズ: **MCMC / computation diagnostics**
- 実務での読み方: 推論結果を解釈する前に、R-hat、ESS、divergence、treedepth、BFMI、trace/pairsを確認する。悪いrunは比較表から除外せず失敗として記録する。
- MLflow連携: `rhat_max, ess_bulk_min, ess_tail_min, divergences, treedepth_hits, bfmi_min`
- 参照: [公式ページ](https://avehtari.github.io/Bayesian-Workflow/birthdays/birthdays.html#fig-births-fit1b-trace) / [ソース候補](https://github.com/avehtari/Bayesian-Workflow/blob/eb00fa4397314ef7d90203382542bd44c590e289/birthdays/birthdays.R)

#### `birthdays-birthdays/fig-births-pth1-vs-fit1`

- 種別: `figure` / 公式ID: `fig-births-pth1-vs-fit1` / ページ内順序: 10
- caption/列: Figure 10
- 周辺文脈（EN）: Compare the mean and sd of parameters from Pathfinder and MCMC. When the normal approximation is not good, Pathfinder tends to underestimate the posterior variance, which makes it
- 周辺文脈（JA, 自動訳）: 5.1 モデル 1: 緩やかな傾向 / パスファインダーと MCMC からのパラメーターの平均と標準偏差を比較します。正規近似が適切でない場合、パスファインダーは事後分散を過小評価する傾向があるため、
- Workflowフェーズ: **Posterior summary / effect interpretation**
- 実務での読み方: 推定効果・不確実性・派生量を意思決定に接続する。平均だけでなく区間・分布・実務閾値超過確率を残す。
- MLflow連携: `posterior_draws_uri, model_code_hash, ci_width, decision_threshold_prob`
- 参照: [公式ページ](https://avehtari.github.io/Bayesian-Workflow/birthdays/birthdays.html#fig-births-pth1-vs-fit1) / [ソース候補](https://github.com/avehtari/Bayesian-Workflow/blob/eb00fa4397314ef7d90203382542bd44c590e289/birthdays/birthdays.R)

#### `birthdays-birthdays/fig-births-pth2-vs-data`

- 種別: `figure` / 公式ID: `fig-births-pth2-vs-data` / ページ内順序: 11
- caption/列: Figure 11
- 周辺文脈（EN）: Compare the model to the data
- 周辺文脈（JA, 自動訳）: 5.1.1 モデル 2: 緩やかな傾向 + 年間の季節的傾向 / モデルとデータの比較
- Workflowフェーズ: **EDA / observed data**
- 実務での読み方: モデル化前に、観測単位・外れ値・欠測・群構造・時系列性・上限/下限などを確認する。MLflowではデータ版と前処理版を固定する。
- MLflow連携: `dataset_uri, dataset_hash, preprocessing_version, n_obs, group_count`
- 参照: [公式ページ](https://avehtari.github.io/Bayesian-Workflow/birthdays/birthdays.html#fig-births-pth2-vs-data) / [ソース候補](https://github.com/avehtari/Bayesian-Workflow/blob/eb00fa4397314ef7d90203382542bd44c590e289/birthdays/birthdays.R)

#### `birthdays-birthdays/fig-births-fit2-vs-data`

- 種別: `figure` / 公式ID: `fig-births-fit2-vs-data` / ページ内順序: 12
- caption/列: Figure 12
- 周辺文脈（EN）: Compare the model to the data
- 周辺文脈（JA, 自動訳）: 5.1.1 モデル 2: 緩やかな傾向 + 年間の季節的傾向 / モデルとデータの比較
- Workflowフェーズ: **EDA / observed data**
- 実務での読み方: モデル化前に、観測単位・外れ値・欠測・群構造・時系列性・上限/下限などを確認する。MLflowではデータ版と前処理版を固定する。
- MLflow連携: `dataset_uri, dataset_hash, preprocessing_version, n_obs, group_count`
- 参照: [公式ページ](https://avehtari.github.io/Bayesian-Workflow/birthdays/birthdays.html#fig-births-fit2-vs-data) / [ソース候補](https://github.com/avehtari/Bayesian-Workflow/blob/eb00fa4397314ef7d90203382542bd44c590e289/birthdays/birthdays.R)

#### `birthdays-birthdays/fig-births-pth2-vs-fit2`

- 種別: `figure` / 公式ID: `fig-births-pth2-vs-fit2` / ページ内順序: 13
- caption/列: Figure 13
- 周辺文脈（EN）: Compare the mean and sd of parameters from Pathfinder and MCMC.
- 周辺文脈（JA, 自動訳）: 5.1.1 モデル 2: 緩やかな傾向 + 年間の季節的傾向 / パスファインダーと MCMC からのパラメーターの平均と標準偏差を比較します。
- Workflowフェーズ: **Model development / debugging**
- 実務での読み方: 小さいモデルから始め、失敗runを観察しながらモデル族・prior・データ処理を段階的に拡張する。
- MLflow連携: `iteration_id, change_reason, failure_mode, hypothesis, next_action`
- 参照: [公式ページ](https://avehtari.github.io/Bayesian-Workflow/birthdays/birthdays.html#fig-births-pth2-vs-fit2) / [ソース候補](https://github.com/avehtari/Bayesian-Workflow/blob/eb00fa4397314ef7d90203382542bd44c590e289/birthdays/birthdays.R)

#### `birthdays-birthdays/fig-births-pth3-vs-data`

- 種別: `figure` / 公式ID: `fig-births-pth3-vs-data` / ページ内順序: 14
- caption/列: Figure 14
- 周辺文脈（EN）: Compare the model to the data
- 周辺文脈（JA, 自動訳）: 5.1.2 モデル 3: 緩やかな傾向 + 年間の季節傾向 + 曜日 / モデルとデータの比較
- Workflowフェーズ: **EDA / observed data**
- 実務での読み方: モデル化前に、観測単位・外れ値・欠測・群構造・時系列性・上限/下限などを確認する。MLflowではデータ版と前処理版を固定する。
- MLflow連携: `dataset_uri, dataset_hash, preprocessing_version, n_obs, group_count`
- 参照: [公式ページ](https://avehtari.github.io/Bayesian-Workflow/birthdays/birthdays.html#fig-births-pth3-vs-data) / [ソース候補](https://github.com/avehtari/Bayesian-Workflow/blob/eb00fa4397314ef7d90203382542bd44c590e289/birthdays/birthdays.R)

#### `birthdays-birthdays/fig-births-fit3-vs-data`

- 種別: `figure` / 公式ID: `fig-births-fit3-vs-data` / ページ内順序: 15
- caption/列: Figure 15
- 周辺文脈（EN）: Compare the model to the data
- 周辺文脈（JA, 自動訳）: 5.1.2 モデル 3: 緩やかな傾向 + 年間の季節傾向 + 曜日 / モデルとデータの比較
- Workflowフェーズ: **EDA / observed data**
- 実務での読み方: モデル化前に、観測単位・外れ値・欠測・群構造・時系列性・上限/下限などを確認する。MLflowではデータ版と前処理版を固定する。
- MLflow連携: `dataset_uri, dataset_hash, preprocessing_version, n_obs, group_count`
- 参照: [公式ページ](https://avehtari.github.io/Bayesian-Workflow/birthdays/birthdays.html#fig-births-fit3-vs-data) / [ソース候補](https://github.com/avehtari/Bayesian-Workflow/blob/eb00fa4397314ef7d90203382542bd44c590e289/birthdays/birthdays.R)

#### `birthdays-birthdays/fig-births-pth3-vs-fit3`

- 種別: `figure` / 公式ID: `fig-births-pth3-vs-fit3` / ページ内順序: 16
- caption/列: Figure 16
- 周辺文脈（EN）: Compare the mean and sd of parameters from Pathfinder and MCMC.
- 周辺文脈（JA, 自動訳）: 5.1.2 モデル 3: 緩やかな傾向 + 年間の季節傾向 + 曜日 / パスファインダーと MCMC からのパラメーターの平均と標準偏差を比較します。
- Workflowフェーズ: **Model development / debugging**
- 実務での読み方: 小さいモデルから始め、失敗runを観察しながらモデル族・prior・データ処理を段階的に拡張する。
- MLflow連携: `iteration_id, change_reason, failure_mode, hypothesis, next_action`
- 参照: [公式ページ](https://avehtari.github.io/Bayesian-Workflow/birthdays/birthdays.html#fig-births-pth3-vs-fit3) / [ソース候補](https://github.com/avehtari/Bayesian-Workflow/blob/eb00fa4397314ef7d90203382542bd44c590e289/birthdays/birthdays.R)

#### `birthdays-birthdays/fig-births-pth4-vs-data`

- 種別: `figure` / 公式ID: `fig-births-pth4-vs-data` / ページ内順序: 17
- caption/列: Figure 17
- 周辺文脈（EN）: Compare the model to the data
- 周辺文脈（JA, 自動訳）: 5.1.3 モデル 4: 長期平滑 + 季節 + 規模が増加する平日 / モデルとデータを比較
- Workflowフェーズ: **EDA / observed data**
- 実務での読み方: モデル化前に、観測単位・外れ値・欠測・群構造・時系列性・上限/下限などを確認する。MLflowではデータ版と前処理版を固定する。
- MLflow連携: `dataset_uri, dataset_hash, preprocessing_version, n_obs, group_count`
- 参照: [公式ページ](https://avehtari.github.io/Bayesian-Workflow/birthdays/birthdays.html#fig-births-pth4-vs-data) / [ソース候補](https://github.com/avehtari/Bayesian-Workflow/blob/eb00fa4397314ef7d90203382542bd44c590e289/birthdays/birthdays.R)

#### `birthdays-birthdays/fig-births-fit4-vs-data`

- 種別: `figure` / 公式ID: `fig-births-fit4-vs-data` / ページ内順序: 18
- caption/列: Figure 18
- 周辺文脈（EN）: Compare the model to the data
- 周辺文脈（JA, 自動訳）: 5.1.3 モデル 4: 長期平滑 + 季節 + 規模が増加する平日 / モデルとデータを比較
- Workflowフェーズ: **EDA / observed data**
- 実務での読み方: モデル化前に、観測単位・外れ値・欠測・群構造・時系列性・上限/下限などを確認する。MLflowではデータ版と前処理版を固定する。
- MLflow連携: `dataset_uri, dataset_hash, preprocessing_version, n_obs, group_count`
- 参照: [公式ページ](https://avehtari.github.io/Bayesian-Workflow/birthdays/birthdays.html#fig-births-fit4-vs-data) / [ソース候補](https://github.com/avehtari/Bayesian-Workflow/blob/eb00fa4397314ef7d90203382542bd44c590e289/birthdays/birthdays.R)

#### `birthdays-birthdays/fig-births-pth4-vs-fit4`

- 種別: `figure` / 公式ID: `fig-births-pth4-vs-fit4` / ページ内順序: 19
- caption/列: Figure 19
- 周辺文脈（EN）: Compare the mean and sd of parameters from Pathfinder and MCMC.
- 周辺文脈（JA, 自動訳）: 5.1.3 モデル 4: 長期平滑 + 季節 + 規模が増加する平日 / パスファインダーと MCMC からのパラメーターの平均と標準偏差を比較します。
- Workflowフェーズ: **Model development / debugging**
- 実務での読み方: 小さいモデルから始め、失敗runを観察しながらモデル族・prior・データ処理を段階的に拡張する。
- MLflow連携: `iteration_id, change_reason, failure_mode, hypothesis, next_action`
- 参照: [公式ページ](https://avehtari.github.io/Bayesian-Workflow/birthdays/birthdays.html#fig-births-pth4-vs-fit4) / [ソース候補](https://github.com/avehtari/Bayesian-Workflow/blob/eb00fa4397314ef7d90203382542bd44c590e289/birthdays/birthdays.R)

#### `birthdays-birthdays/fig-births-pth5-vs-data-1`

- 種別: `figure` / 公式ID: `fig-births-pth5-vs-data-1` / ページ内順序: 20
- caption/列: Figure 20
- 周辺文脈（EN）: We now get only one or couple distinct draws (depending on luck), so we don’t get much information about the posterior width, but the draws are still providing a useful approximati
- 周辺文脈（JA, 自動訳）: 5.1.4 モデル 5: 長期平滑 + 季節 + 時間に依存する大きさ + 曜日の RHS / 個別のドローが 1 つまたはいくつかしか得られないため (運に依存します)、後方幅に関する情報はあまり得られませんが、ドローは依然として有用な近似値を提供します。
- Workflowフェーズ: **EDA / observed data**
- 実務での読み方: モデル化前に、観測単位・外れ値・欠測・群構造・時系列性・上限/下限などを確認する。MLflowではデータ版と前処理版を固定する。
- MLflow連携: `dataset_uri, dataset_hash, preprocessing_version, n_obs, group_count`
- 参照: [公式ページ](https://avehtari.github.io/Bayesian-Workflow/birthdays/birthdays.html#fig-births-pth5-vs-data-1) / [ソース候補](https://github.com/avehtari/Bayesian-Workflow/blob/eb00fa4397314ef7d90203382542bd44c590e289/birthdays/birthdays.R)

#### `birthdays-birthdays/fig-births-pth5-vs-data-2`

- 種別: `figure` / 公式ID: `fig-births-pth5-vs-data-2` / ページ内順序: 21
- caption/列: Figure 21
- 周辺文脈（EN）: We now get only one or couple distinct draws (depending on luck), so we don’t get much information about the posterior width, but the draws are still providing a useful approximati
- 周辺文脈（JA, 自動訳）: 5.1.4 モデル 5: 長期平滑 + 季節 + 時間に依存する大きさ + 曜日の RHS / 個別のドローが 1 つまたはいくつかしか得られないため (運に依存します)、後方幅に関する情報はあまり得られませんが、ドローは依然として有用な近似値を提供します。
- Workflowフェーズ: **EDA / observed data**
- 実務での読み方: モデル化前に、観測単位・外れ値・欠測・群構造・時系列性・上限/下限などを確認する。MLflowではデータ版と前処理版を固定する。
- MLflow連携: `dataset_uri, dataset_hash, preprocessing_version, n_obs, group_count`
- 参照: [公式ページ](https://avehtari.github.io/Bayesian-Workflow/birthdays/birthdays.html#fig-births-pth5-vs-data-2) / [ソース候補](https://github.com/avehtari/Bayesian-Workflow/blob/eb00fa4397314ef7d90203382542bd44c590e289/birthdays/birthdays.R)

#### `birthdays-birthdays/fig-births-fit5-vs-data-1`

- 種別: `figure` / 公式ID: `fig-births-fit5-vs-data-1` / ページ内順序: 22
- caption/列: Figure 22
- 周辺文脈（EN）: Compare the model to the data
- 周辺文脈（JA, 自動訳）: 5.1.4 モデル 5: 長期平滑 + 季節 + 時間依存の大きさを持つ平日 + 年間の曜日の RHS / モデルとデータの比較
- Workflowフェーズ: **EDA / observed data**
- 実務での読み方: モデル化前に、観測単位・外れ値・欠測・群構造・時系列性・上限/下限などを確認する。MLflowではデータ版と前処理版を固定する。
- MLflow連携: `dataset_uri, dataset_hash, preprocessing_version, n_obs, group_count`
- 参照: [公式ページ](https://avehtari.github.io/Bayesian-Workflow/birthdays/birthdays.html#fig-births-fit5-vs-data-1) / [ソース候補](https://github.com/avehtari/Bayesian-Workflow/blob/eb00fa4397314ef7d90203382542bd44c590e289/birthdays/birthdays.R)

#### `birthdays-birthdays/fig-births-fit5-vs-data-2`

- 種別: `figure` / 公式ID: `fig-births-fit5-vs-data-2` / ページ内順序: 23
- caption/列: Figure 23
- 周辺文脈（EN）: Compare the model to the data
- 周辺文脈（JA, 自動訳）: 5.1.4 モデル 5: 長期平滑 + 季節 + 時間依存の大きさを持つ平日 + 年間の曜日の RHS / モデルとデータの比較
- Workflowフェーズ: **EDA / observed data**
- 実務での読み方: モデル化前に、観測単位・外れ値・欠測・群構造・時系列性・上限/下限などを確認する。MLflowではデータ版と前処理版を固定する。
- MLflow連携: `dataset_uri, dataset_hash, preprocessing_version, n_obs, group_count`
- 参照: [公式ページ](https://avehtari.github.io/Bayesian-Workflow/birthdays/birthdays.html#fig-births-fit5-vs-data-2) / [ソース候補](https://github.com/avehtari/Bayesian-Workflow/blob/eb00fa4397314ef7d90203382542bd44c590e289/birthdays/birthdays.R)

#### `birthdays-birthdays/fig-births-pth5-vs-fit5`

- 種別: `figure` / 公式ID: `fig-births-pth5-vs-fit5` / ページ内順序: 24
- caption/列: Figure 24
- 周辺文脈（EN）: The plot looks quite good. Compare the mean and sd of parameters from Pathfinder and MCMC. In this case, we are using the non-resampled Pathfinder draws (the resampled draws had on
- 周辺文脈（JA, 自動訳）: 5.1.4 モデル 5: 長期平滑 + 季節 + 時間依存の大きさを持つ平日 + 年間の曜日 RHS / プロットは非常に良好に見えます。パスファインダーと MCMC からのパラメーターの平均と標準偏差を比較します。この場合、リサンプリングされていないパスファインダー描画を使用しています（リサンプリングされた描画は
- Workflowフェーズ: **Posterior summary / effect interpretation**
- 実務での読み方: 推定効果・不確実性・派生量を意思決定に接続する。平均だけでなく区間・分布・実務閾値超過確率を残す。
- MLflow連携: `posterior_draws_uri, model_code_hash, ci_width, decision_threshold_prob`
- 参照: [公式ページ](https://avehtari.github.io/Bayesian-Workflow/birthdays/birthdays.html#fig-births-pth5-vs-fit5) / [ソース候補](https://github.com/avehtari/Bayesian-Workflow/blob/eb00fa4397314ef7d90203382542bd44c590e289/birthdays/birthdays.R)

#### `birthdays-birthdays/fig-births-pth6-vs-data-1`

- 種別: `figure` / 公式ID: `fig-births-pth6-vs-data-1` / ページ内順序: 25
- caption/列: Figure 25
- 周辺文脈（EN）: Compare the model to the data
- 周辺文脈（JA, 自動訳）: 5.1.5 モデル 6: 長期平滑 + 季節 + 平日 + 年間の曜日 / モデルとデータの比較
- Workflowフェーズ: **EDA / observed data**
- 実務での読み方: モデル化前に、観測単位・外れ値・欠測・群構造・時系列性・上限/下限などを確認する。MLflowではデータ版と前処理版を固定する。
- MLflow連携: `dataset_uri, dataset_hash, preprocessing_version, n_obs, group_count`
- 参照: [公式ページ](https://avehtari.github.io/Bayesian-Workflow/birthdays/birthdays.html#fig-births-pth6-vs-data-1) / [ソース候補](https://github.com/avehtari/Bayesian-Workflow/blob/eb00fa4397314ef7d90203382542bd44c590e289/birthdays/birthdays.R)

#### `birthdays-birthdays/fig-births-pth6-vs-data-2`

- 種別: `figure` / 公式ID: `fig-births-pth6-vs-data-2` / ページ内順序: 26
- caption/列: Figure 26
- 周辺文脈（EN）: Compare the model to the data
- 周辺文脈（JA, 自動訳）: 5.1.5 モデル 6: 長期平滑 + 季節 + 平日 + 年間の曜日 / モデルとデータの比較
- Workflowフェーズ: **EDA / observed data**
- 実務での読み方: モデル化前に、観測単位・外れ値・欠測・群構造・時系列性・上限/下限などを確認する。MLflowではデータ版と前処理版を固定する。
- MLflow連携: `dataset_uri, dataset_hash, preprocessing_version, n_obs, group_count`
- 参照: [公式ページ](https://avehtari.github.io/Bayesian-Workflow/birthdays/birthdays.html#fig-births-pth6-vs-data-2) / [ソース候補](https://github.com/avehtari/Bayesian-Workflow/blob/eb00fa4397314ef7d90203382542bd44c590e289/birthdays/birthdays.R)

#### `birthdays-birthdays/fig-births-fit6-vs-data-1`

- 種別: `figure` / 公式ID: `fig-births-fit6-vs-data-1` / ページ内順序: 27
- caption/列: Figure 27
- 周辺文脈（EN）: Compare the model to the data
- 周辺文脈（JA, 自動訳）: 5.1.5 モデル 6: 長期平滑 + 季節 + 平日 + 年間の曜日 / モデルとデータの比較
- Workflowフェーズ: **EDA / observed data**
- 実務での読み方: モデル化前に、観測単位・外れ値・欠測・群構造・時系列性・上限/下限などを確認する。MLflowではデータ版と前処理版を固定する。
- MLflow連携: `dataset_uri, dataset_hash, preprocessing_version, n_obs, group_count`
- 参照: [公式ページ](https://avehtari.github.io/Bayesian-Workflow/birthdays/birthdays.html#fig-births-fit6-vs-data-1) / [ソース候補](https://github.com/avehtari/Bayesian-Workflow/blob/eb00fa4397314ef7d90203382542bd44c590e289/birthdays/birthdays.R)

#### `birthdays-birthdays/fig-births-fit6-vs-data-2`

- 種別: `figure` / 公式ID: `fig-births-fit6-vs-data-2` / ページ内順序: 28
- caption/列: Figure 28
- 周辺文脈（EN）: Compare the model to the data
- 周辺文脈（JA, 自動訳）: 5.1.5 モデル 6: 長期平滑 + 季節 + 平日 + 年間の曜日 / モデルとデータの比較
- Workflowフェーズ: **EDA / observed data**
- 実務での読み方: モデル化前に、観測単位・外れ値・欠測・群構造・時系列性・上限/下限などを確認する。MLflowではデータ版と前処理版を固定する。
- MLflow連携: `dataset_uri, dataset_hash, preprocessing_version, n_obs, group_count`
- 参照: [公式ページ](https://avehtari.github.io/Bayesian-Workflow/birthdays/birthdays.html#fig-births-fit6-vs-data-2) / [ソース候補](https://github.com/avehtari/Bayesian-Workflow/blob/eb00fa4397314ef7d90203382542bd44c590e289/birthdays/birthdays.R)

#### `birthdays-birthdays/fig-births-pth6-vs-fit6`

- 種別: `figure` / 公式ID: `fig-births-pth6-vs-fit6` / ページ内順序: 29
- caption/列: Figure 29
- 周辺文脈（EN）: Compare the mean and sd of parameters from Pathfinder and MCMC. In this case, we are using the non-resampled Pathfinder draws.
- 周辺文脈（JA, 自動訳）: 5.1.5 モデル 6: 長期平滑 + 季節 + 平日 + 年間通算日 / パスファインダーと MCMC からのパラメーターの平均と標準偏差を比較します。この場合、リサンプリングされていないパスファインダー描画を使用しています。
- Workflowフェーズ: **Posterior summary / effect interpretation**
- 実務での読み方: 推定効果・不確実性・派生量を意思決定に接続する。平均だけでなく区間・分布・実務閾値超過確率を残す。
- MLflow連携: `posterior_draws_uri, model_code_hash, ci_width, decision_threshold_prob`
- 参照: [公式ページ](https://avehtari.github.io/Bayesian-Workflow/birthdays/birthdays.html#fig-births-pth6-vs-fit6) / [ソース候補](https://github.com/avehtari/Bayesian-Workflow/blob/eb00fa4397314ef7d90203382542bd44c590e289/birthdays/birthdays.R)

#### `birthdays-birthdays/fig-births-fit6-day-of-year`

- 種別: `figure` / 公式ID: `fig-births-fit6-day-of-year` / ページ内順序: 30
- caption/列: Figure 30
- 周辺文脈（EN）: The following plot shows the day of year effect with 90% posterior intervals.
- 周辺文脈（JA, 自動訳）: 5.1.5 モデル 6: 長期平滑 + 季節 + 平日 + 年間の日 / 次のプロットは、90% 事後間隔での年間の日の効果を示しています。
- Workflowフェーズ: **Posterior summary / effect interpretation**
- 実務での読み方: 推定効果・不確実性・派生量を意思決定に接続する。平均だけでなく区間・分布・実務閾値超過確率を残す。
- MLflow連携: `posterior_draws_uri, model_code_hash, ci_width, decision_threshold_prob`
- 参照: [公式ページ](https://avehtari.github.io/Bayesian-Workflow/birthdays/birthdays.html#fig-births-fit6-day-of-year) / [ソース候補](https://github.com/avehtari/Bayesian-Workflow/blob/eb00fa4397314ef7d90203382542bd44c590e289/birthdays/birthdays.R)

#### `birthdays-birthdays/fig-births-pth7-vs-data`

- 種別: `figure` / 公式ID: `fig-births-pth7-vs-data` / ページ内順序: 31
- caption/列: Figure 31
- 周辺文脈（EN）: Compare the model to the data
- 周辺文脈（JA, 自動訳）: 5.1.6 モデル 7: 長期平滑 + 季節 + 平日 + 年間通常日 + 変動特別日 / モデルとデータの比較
- Workflowフェーズ: **EDA / observed data**
- 実務での読み方: モデル化前に、観測単位・外れ値・欠測・群構造・時系列性・上限/下限などを確認する。MLflowではデータ版と前処理版を固定する。
- MLflow連携: `dataset_uri, dataset_hash, preprocessing_version, n_obs, group_count`
- 参照: [公式ページ](https://avehtari.github.io/Bayesian-Workflow/birthdays/birthdays.html#fig-births-pth7-vs-data) / [ソース候補](https://github.com/avehtari/Bayesian-Workflow/blob/eb00fa4397314ef7d90203382542bd44c590e289/birthdays/birthdays.R)

#### `birthdays-birthdays/fig-births-fit7-vs-data`

- 種別: `figure` / 公式ID: `fig-births-fit7-vs-data` / ページ内順序: 32
- caption/列: Figure 32
- 周辺文脈（EN）: Compare the model to the data
- 周辺文脈（JA, 自動訳）: 5.1.6 モデル 7: 長期平滑 + 季節 + 平日 + 年間通常日 + 変動特別日 / モデルとデータの比較
- Workflowフェーズ: **EDA / observed data**
- 実務での読み方: モデル化前に、観測単位・外れ値・欠測・群構造・時系列性・上限/下限などを確認する。MLflowではデータ版と前処理版を固定する。
- MLflow連携: `dataset_uri, dataset_hash, preprocessing_version, n_obs, group_count`
- 参照: [公式ページ](https://avehtari.github.io/Bayesian-Workflow/birthdays/birthdays.html#fig-births-fit7-vs-data) / [ソース候補](https://github.com/avehtari/Bayesian-Workflow/blob/eb00fa4397314ef7d90203382542bd44c590e289/birthdays/birthdays.R)

#### `birthdays-birthdays/fig-births-pth7-vs-fit7`

- 種別: `figure` / 公式ID: `fig-births-pth7-vs-fit7` / ページ内順序: 33
- caption/列: Figure 33
- 周辺文脈（EN）: Compare the mean and sd of parameters from Pathfinder and MCMC. In this case, we are using the non-resampled Pathfinder draws.
- 周辺文脈（JA, 自動訳）: 5.1.6 モデル 7: 長期平滑 + 季節 + 平日 + 通常日 + 変動特別日 / パスファインダーと MCMC からのパラメーターの平均と標準偏差を比較します。この場合、リサンプリングされていないパスファインダー描画を使用しています。
- Workflowフェーズ: **Posterior summary / effect interpretation**
- 実務での読み方: 推定効果・不確実性・派生量を意思決定に接続する。平均だけでなく区間・分布・実務閾値超過確率を残す。
- MLflow連携: `posterior_draws_uri, model_code_hash, ci_width, decision_threshold_prob`
- 参照: [公式ページ](https://avehtari.github.io/Bayesian-Workflow/birthdays/birthdays.html#fig-births-pth7-vs-fit7) / [ソース候補](https://github.com/avehtari/Bayesian-Workflow/blob/eb00fa4397314ef7d90203382542bd44c590e289/birthdays/birthdays.R)

#### `birthdays-birthdays/fig-births-fit7-day-of-year`

- 種別: `figure` / 公式ID: `fig-births-fit7-day-of-year` / ページ内順序: 34
- caption/列: Figure 34
- 周辺文脈（EN）: The following plot shows the day of year effect with 90% posterior intervals.
- 周辺文脈（JA, 自動訳）: 5.1.6 モデル 7: 長期平滑 + 季節 + 平日 + 年間通常日 + 変動特別日 / 次のプロットは、90% 事後間隔での年間日効果を示しています。
- Workflowフェーズ: **Posterior summary / effect interpretation**
- 実務での読み方: 推定効果・不確実性・派生量を意思決定に接続する。平均だけでなく区間・分布・実務閾値超過確率を残す。
- MLflow連携: `posterior_draws_uri, model_code_hash, ci_width, decision_threshold_prob`
- 参照: [公式ページ](https://avehtari.github.io/Bayesian-Workflow/birthdays/birthdays.html#fig-births-fit7-day-of-year) / [ソース候補](https://github.com/avehtari/Bayesian-Workflow/blob/eb00fa4397314ef7d90203382542bd44c590e289/birthdays/birthdays.R)

#### `birthdays-birthdays/fig-births-pth8-vs-data`

- 種別: `figure` / 公式ID: `fig-births-pth8-vs-data` / ページ内順序: 35
- caption/列: Figure 35
- 周辺文脈（EN）: Compare the model to the data
- 周辺文脈（JA, 自動訳）: 5.1.7 モデル 8: 長期平滑 + 季節 + 時間依存の大きさを持つ平日 + 年間の曜日 + 特別 / モデルとデータを比較する
- Workflowフェーズ: **EDA / observed data**
- 実務での読み方: モデル化前に、観測単位・外れ値・欠測・群構造・時系列性・上限/下限などを確認する。MLflowではデータ版と前処理版を固定する。
- MLflow連携: `dataset_uri, dataset_hash, preprocessing_version, n_obs, group_count`
- 参照: [公式ページ](https://avehtari.github.io/Bayesian-Workflow/birthdays/birthdays.html#fig-births-pth8-vs-data) / [ソース候補](https://github.com/avehtari/Bayesian-Workflow/blob/eb00fa4397314ef7d90203382542bd44c590e289/birthdays/birthdays.R)

#### `birthdays-birthdays/fig-births-fit8-vs-data`

- 種別: `figure` / 公式ID: `fig-births-fit8-vs-data` / ページ内順序: 36
- caption/列: Figure 36
- 周辺文脈（EN）: Compare the model to the data
- 周辺文脈（JA, 自動訳）: 5.1.7 モデル 8: 長期平滑 + 季節 + 時間依存の大きさを持つ平日 + 年間の曜日 + 特別 / モデルとデータを比較する
- Workflowフェーズ: **EDA / observed data**
- 実務での読み方: モデル化前に、観測単位・外れ値・欠測・群構造・時系列性・上限/下限などを確認する。MLflowではデータ版と前処理版を固定する。
- MLflow連携: `dataset_uri, dataset_hash, preprocessing_version, n_obs, group_count`
- 参照: [公式ページ](https://avehtari.github.io/Bayesian-Workflow/birthdays/birthdays.html#fig-births-fit8-vs-data) / [ソース候補](https://github.com/avehtari/Bayesian-Workflow/blob/eb00fa4397314ef7d90203382542bd44c590e289/birthdays/birthdays.R)

#### `birthdays-birthdays/fig-births-pth8-vs-fit8`

- 種別: `figure` / 公式ID: `fig-births-pth8-vs-fit8` / ページ内順序: 37
- caption/列: Figure 37
- 周辺文脈（EN）: Compare the mean and sd of parameters from Pathfinder and MCMC. In this case, we are using the non-resampled Pathfinder draws.
- 周辺文脈（JA, 自動訳）: 5.1.7 モデル 8: 長期平滑 + 季節 + 時間依存の大きさを持つ平日 + 年間の曜日 + 特別 / パスファインダーと MCMC からのパラメーターの平均と標準偏差を比較します。この場合、リサンプリングされていないパスファインダー描画を使用しています。
- Workflowフェーズ: **Posterior summary / effect interpretation**
- 実務での読み方: 推定効果・不確実性・派生量を意思決定に接続する。平均だけでなく区間・分布・実務閾値超過確率を残す。
- MLflow連携: `posterior_draws_uri, model_code_hash, ci_width, decision_threshold_prob`
- 参照: [公式ページ](https://avehtari.github.io/Bayesian-Workflow/birthdays/birthdays.html#fig-births-pth8-vs-fit8) / [ソース候補](https://github.com/avehtari/Bayesian-Workflow/blob/eb00fa4397314ef7d90203382542bd44c590e289/birthdays/birthdays.R)

#### `birthdays-birthdays/fig-births-fit8tnu-vs-data`

- 種別: `figure` / 公式ID: `fig-births-fit8tnu-vs-data` / ページ内順序: 38
- caption/列: Figure 38
- 周辺文脈（EN）: Posterior of degrees of freedom nu_f4 is very close to 0.5, and thus the distribution has thicker tails than Cauchy. This is strong evidence that the distribution of day of year ef
- 周辺文脈（JA, 自動訳）: 5.1.8 モデル 8+t_nu: スチューデントの t 事前 / 事後自由度 nu_f4 による年間通算日効果は 0.5 に非常に近いため、分布はコーシーよりも裾が太くなっています。これは、年間の曜日 ef の分布が次のことを示す強力な証拠です。
- Workflowフェーズ: **EDA / observed data**
- 実務での読み方: モデル化前に、観測単位・外れ値・欠測・群構造・時系列性・上限/下限などを確認する。MLflowではデータ版と前処理版を固定する。
- MLflow連携: `dataset_uri, dataset_hash, preprocessing_version, n_obs, group_count`
- 参照: [公式ページ](https://avehtari.github.io/Bayesian-Workflow/birthdays/birthdays.html#fig-births-fit8tnu-vs-data) / [ソース候補](https://github.com/avehtari/Bayesian-Workflow/blob/eb00fa4397314ef7d90203382542bd44c590e289/birthdays/birthdays.R)

#### `birthdays-birthdays/fig-births-pth8tnu-vs-fit8tnu`

- 種別: `figure` / 公式ID: `fig-births-pth8tnu-vs-fit8tnu` / ページ内順序: 39
- caption/列: Figure 39
- 周辺文脈（EN）: Compare the mean and sd of parameters from Pathfinder and MCMC. In this case, we are using the non-resampled Pathfinder draws.
- 周辺文脈（JA, 自動訳）: 5.1.8 モデル 8+t_nu: スチューデントの事前 t による年間日数効果 / パスファインダーと MCMC からのパラメーターの平均と標準偏差を比較します。この場合、リサンプリングされていないパスファインダー描画を使用しています。
- Workflowフェーズ: **Posterior summary / effect interpretation**
- 実務での読み方: 推定効果・不確実性・派生量を意思決定に接続する。平均だけでなく区間・分布・実務閾値超過確率を残す。
- MLflow連携: `posterior_draws_uri, model_code_hash, ci_width, decision_threshold_prob`
- 参照: [公式ページ](https://avehtari.github.io/Bayesian-Workflow/birthdays/birthdays.html#fig-births-pth8tnu-vs-fit8tnu) / [ソース候補](https://github.com/avehtari/Bayesian-Workflow/blob/eb00fa4397314ef7d90203382542bd44c590e289/birthdays/birthdays.R)

#### `birthdays-birthdays/fig-births-fit8rhs-vs-data`

- 種別: `figure` / 公式ID: `fig-births-fit8rhs-vs-data` / ページ内順序: 40
- caption/列: Figure 40
- 周辺文脈（EN）: Compare the model to the data
- 周辺文脈（JA, 自動訳）: 5.1.9 モデル 8+RHS: 以前の RHS との日付の影響 / モデルとデータの比較
- Workflowフェーズ: **EDA / observed data**
- 実務での読み方: モデル化前に、観測単位・外れ値・欠測・群構造・時系列性・上限/下限などを確認する。MLflowではデータ版と前処理版を固定する。
- MLflow連携: `dataset_uri, dataset_hash, preprocessing_version, n_obs, group_count`
- 参照: [公式ページ](https://avehtari.github.io/Bayesian-Workflow/birthdays/birthdays.html#fig-births-fit8rhs-vs-data) / [ソース候補](https://github.com/avehtari/Bayesian-Workflow/blob/eb00fa4397314ef7d90203382542bd44c590e289/birthdays/birthdays.R)

#### `birthdays-birthdays/fig-births-pth8rhs-vs-fit8rhs`

- 種別: `figure` / 公式ID: `fig-births-pth8rhs-vs-fit8rhs` / ページ内順序: 41
- caption/列: Figure 41
- 周辺文脈（EN）: Compare the mean and sd of parameters from Pathfinder and MCMC. In this case, we are using the non-resampled Pathfinder draws.
- 周辺文脈（JA, 自動訳）: 5.1.9 モデル 8+RHS: 事前の RHS との暦日の影響 / パスファインダーと MCMC からのパラメーターの平均と標準偏差を比較します。この場合、リサンプリングされていないパスファインダー描画を使用しています。
- Workflowフェーズ: **Posterior summary / effect interpretation**
- 実務での読み方: 推定効果・不確実性・派生量を意思決定に接続する。平均だけでなく区間・分布・実務閾値超過確率を残す。
- MLflow連携: `posterior_draws_uri, model_code_hash, ci_width, decision_threshold_prob`
- 参照: [公式ページ](https://avehtari.github.io/Bayesian-Workflow/birthdays/birthdays.html#fig-births-pth8rhs-vs-fit8rhs) / [ソース候補](https://github.com/avehtari/Bayesian-Workflow/blob/eb00fa4397314ef7d90203382542bd44c590e289/birthdays/birthdays.R)

#### `birthdays-birthdays/fig-births-fit8rhs-residuals`

- 種別: `figure` / 公式ID: `fig-births-fit8rhs-residuals` / ページ内順序: 42
- caption/列: Figure 42
- 周辺文脈（EN）: We can get further ideas for how to improve the model also by looking at the residuals.
- 周辺文脈（JA, 自動訳）: 5.1.12 残差分析 / 残差を調べることによって、モデルを改善する方法についてさらにアイデアを得ることができます。
- Workflowフェーズ: **LOO-CV / model comparison**
- 実務での読み方: elpd差だけでなくSEとPareto-kを読み、勝敗より『どのデータ点で負けるか』を確認する。
- MLflow連携: `loo_elpd, loo_elpd_diff, loo_se_diff, pareto_k_gt_0_7, reloo_count`
- 参照: [公式ページ](https://avehtari.github.io/Bayesian-Workflow/birthdays/birthdays.html#fig-births-fit8rhs-residuals) / [ソース候補](https://github.com/avehtari/Bayesian-Workflow/blob/eb00fa4397314ef7d90203382542bd44c590e289/birthdays/birthdays.R)

#### `birthdays-birthdays/fig-births-pth8rhs-vs-fit8rhs-2`

- 種別: `figure` / 公式ID: `fig-births-pth8rhs-vs-fit8rhs-2` / ページ内順序: 43
- caption/列: Figure 43
- 周辺文脈（EN）: Compare the mean and sd of some parameters from Pathfinder and MCMC. In this case, we are using the non-resampled Pathfinder draws.
- 周辺文脈（JA, 自動訳）: 5.1.12 残差分析 / パスファインダーと MCMC からのいくつかのパラメーターの平均と標準偏差を比較します。この場合、リサンプリングされていないパスファインダー描画を使用しています。
- Workflowフェーズ: **Posterior summary / effect interpretation**
- 実務での読み方: 推定効果・不確実性・派生量を意思決定に接続する。平均だけでなく区間・分布・実務閾値超過確率を残す。
- MLflow連携: `posterior_draws_uri, model_code_hash, ci_width, decision_threshold_prob`
- 参照: [公式ページ](https://avehtari.github.io/Bayesian-Workflow/birthdays/birthdays.html#fig-births-pth8rhs-vs-fit8rhs-2) / [ソース候補](https://github.com/avehtari/Bayesian-Workflow/blob/eb00fa4397314ef7d90203382542bd44c590e289/birthdays/birthdays.R)

#### `birthdays-birthdays/fig-births-pth8rhs-vs-fit8rhs-sd-ratio`

- 種別: `figure` / 公式ID: `fig-births-pth8rhs-vs-fit8rhs-sd-ratio` / ページ内順序: 44
- caption/列: Figure 44
- 周辺文脈（EN）: Plot the sd from Pathfinder divided by sd from MCMC. We see that for some parameters the order of magnitude is fine, but for some sd is underestimated by 2-3 orders of magnitude, w
- 周辺文脈（JA, 自動訳）: 5.1.12 残留分析 / パスファインダーからの標準偏差を MCMC からの標準偏差で割ったものをプロットします。一部のパラメータでは大きさのオーダーは問題ありませんが、一部のパラメーターでは sd が 2 ～ 3 桁過小評価されていることがわかります。
- Workflowフェーズ: **Model development / debugging**
- 実務での読み方: 小さいモデルから始め、失敗runを観察しながらモデル族・prior・データ処理を段階的に拡張する。
- MLflow連携: `iteration_id, change_reason, failure_mode, hypothesis, next_action`
- 参照: [公式ページ](https://avehtari.github.io/Bayesian-Workflow/birthdays/birthdays.html#fig-births-pth8rhs-vs-fit8rhs-sd-ratio) / [ソース候補](https://github.com/avehtari/Bayesian-Workflow/blob/eb00fa4397314ef7d90203382542bd44c590e289/birthdays/birthdays.R)

#### `birthdays-birthdays/fig-births-pth1b-vs-fit1b-sd-ratio`

- 種別: `figure` / 公式ID: `fig-births-pth1b-vs-fit1b-sd-ratio` / ページ内順序: 45
- caption/列: Figure 45
- 周辺文脈（EN）: In case of simpler models, Pathfinder estimates can be much better. For example, for the model 1b we get the following
- 周辺文脈（JA, 自動訳）: 5.1.12 残差分析 / より単純なモデルの場合、パスファインダーの推定値ははるかに優れている可能性があります。たとえば、モデル 1b の場合、次のようになります。
- Workflowフェーズ: **Model development / debugging**
- 実務での読み方: 小さいモデルから始め、失敗runを観察しながらモデル族・prior・データ処理を段階的に拡張する。
- MLflow連携: `iteration_id, change_reason, failure_mode, hypothesis, next_action`
- 参照: [公式ページ](https://avehtari.github.io/Bayesian-Workflow/birthdays/birthdays.html#fig-births-pth1b-vs-fit1b-sd-ratio) / [ソース候補](https://github.com/avehtari/Bayesian-Workflow/blob/eb00fa4397314ef7d90203382542bd44c590e289/birthdays/birthdays.R)

#### `birthdays-birthdays/fig-births-fit8tnu-day-of-year`

- 種別: `figure` / 公式ID: `fig-births-fit8tnu-day-of-year` / ページ内順序: 46
- caption/列: Figure 46
- 周辺文脈（EN）: Using this final model which is the best model based on LOO-CV comparison, we show the day of year effect with 90% posterior intervals.
- 周辺文脈（JA, 自動訳）: 5.1.13 より正確な推論 / LOO-CV 比較に基づく最良のモデルであるこの最終モデルを使用して、90% の事後間隔で曜日効果を示します。
- Workflowフェーズ: **Posterior summary / effect interpretation**
- 実務での読み方: 推定効果・不確実性・派生量を意思決定に接続する。平均だけでなく区間・分布・実務閾値超過確率を残す。
- MLflow連携: `posterior_draws_uri, model_code_hash, ci_width, decision_threshold_prob`
- 参照: [公式ページ](https://avehtari.github.io/Bayesian-Workflow/birthdays/birthdays.html#fig-births-fit8tnu-day-of-year) / [ソース候補](https://github.com/avehtari/Bayesian-Workflow/blob/eb00fa4397314ef7d90203382542bd44c590e289/birthdays/birthdays.R)

#### `birthdays-birthdays/tinytable_jahi1my9jhtktx6tj6tx`

- 種別: `table` / 公式ID: `tinytable_jahi1my9jhtktx6tj6tx` / ページ内順序: 1
- caption/列: intercept; sigma_f1; lengthscale_f1; sigma; -0.056; 1.1; 0.18; 0.81
- 周辺文脈（EN）: Check whether parameters have reasonable values
- 周辺文脈（JA, 自動訳）: 5.1 モデル 1: 緩やかな傾向 / パラメーターが適切な値であるかどうかを確認する
- Workflowフェーズ: **Model development / debugging**
- 実務での読み方: 小さいモデルから始め、失敗runを観察しながらモデル族・prior・データ処理を段階的に拡張する。
- MLflow連携: `iteration_id, change_reason, failure_mode, hypothesis, next_action`
- 参照: [公式ページ](https://avehtari.github.io/Bayesian-Workflow/birthdays/birthdays.html#tinytable_jahi1my9jhtktx6tj6tx) / [ソース候補](https://github.com/avehtari/Bayesian-Workflow/blob/eb00fa4397314ef7d90203382542bd44c590e289/birthdays/birthdays.R)

#### `birthdays-birthdays/tinytable_ghd9j0ad1brfztzddynh`

- 種別: `table` / 公式ID: `tinytable_ghd9j0ad1brfztzddynh` / ページ内順序: 2
- caption/列: variable; mean; median; sd; mad; q5; q95; intercept
- 周辺文脈（EN）: Check whether parameters have reasonable values. With Laplace method, we get also some information about the uncertainty in the posterior.
- 周辺文脈（JA, 自動訳）: 5.1 モデル 1: 緩やかな傾向 / パラメーターが適切な値であるかどうかを確認します。ラプラス法を使用すると、事後の不確かさに関する情報も得られます。
- Workflowフェーズ: **Posterior summary / effect interpretation**
- 実務での読み方: 推定効果・不確実性・派生量を意思決定に接続する。平均だけでなく区間・分布・実務閾値超過確率を残す。
- MLflow連携: `posterior_draws_uri, model_code_hash, ci_width, decision_threshold_prob`
- 参照: [公式ページ](https://avehtari.github.io/Bayesian-Workflow/birthdays/birthdays.html#tinytable_ghd9j0ad1brfztzddynh) / [ソース候補](https://github.com/avehtari/Bayesian-Workflow/blob/eb00fa4397314ef7d90203382542bd44c590e289/birthdays/birthdays.R)

#### `birthdays-birthdays/tinytable_b3pqaxxp0yjp6juz88s3`

- 種別: `table` / 公式ID: `tinytable_b3pqaxxp0yjp6juz88s3` / ページ内順序: 3
- caption/列: variable; khat; min_ss; khat_threshold; convergence_rate; w; 1.6; Inf
- 周辺文脈（EN）: At the moment, the Laplace method doesn’t automatically run diagnostic to assess the quality of the normal approximation, but we can do it manually by checking the Pareto- \hat{k}
- 周辺文脈（JA, 自動訳）: 5.1 モデル 1: 緩やかな傾向 / 現時点では、ラプラス法は正規近似の品質を評価するための診断を自動的に実行しませんが、パレート-\hat{k} をチェックすることで手動で実行できます。
- Workflowフェーズ: **MCMC / computation diagnostics**
- 実務での読み方: 推論結果を解釈する前に、R-hat、ESS、divergence、treedepth、BFMI、trace/pairsを確認する。悪いrunは比較表から除外せず失敗として記録する。
- MLflow連携: `rhat_max, ess_bulk_min, ess_tail_min, divergences, treedepth_hits, bfmi_min`
- 参照: [公式ページ](https://avehtari.github.io/Bayesian-Workflow/birthdays/birthdays.html#tinytable_b3pqaxxp0yjp6juz88s3) / [ソース候補](https://github.com/avehtari/Bayesian-Workflow/blob/eb00fa4397314ef7d90203382542bd44c590e289/birthdays/birthdays.R)

#### `birthdays-birthdays/tinytable_ygoztowr90rsapprzotq`

- 種別: `table` / 公式ID: `tinytable_ygoztowr90rsapprzotq` / ページ内順序: 4
- caption/列: variable; n_distinct; lp__; 24
- 周辺文脈（EN）: Pathfinder provides automatically Pareto- \hat{k} diagnostic which is high, indicating the normal approximation is not good. When Pareto- \hat{k} is very high the Pareto smoothed i
- 周辺文脈（JA, 自動訳）: 5.1 モデル 1: 遅い傾向 / パスファインダーは、パレート \hat{k} 診断を自動的に提供します。これは、正規近似が適切ではないことを示します。パレート- \hat{k} が非常に高い場合、パレート平滑化 i
- Workflowフェーズ: **LOO-CV / model comparison**
- 実務での読み方: elpd差だけでなくSEとPareto-kを読み、勝敗より『どのデータ点で負けるか』を確認する。
- MLflow連携: `loo_elpd, loo_elpd_diff, loo_se_diff, pareto_k_gt_0_7, reloo_count`
- 参照: [公式ページ](https://avehtari.github.io/Bayesian-Workflow/birthdays/birthdays.html#tinytable_ygoztowr90rsapprzotq) / [ソース候補](https://github.com/avehtari/Bayesian-Workflow/blob/eb00fa4397314ef7d90203382542bd44c590e289/birthdays/birthdays.R)

#### `birthdays-birthdays/tinytable_q76ul4zi967rn8msxqh8`

- 種別: `table` / 公式ID: `tinytable_q76ul4zi967rn8msxqh8` / ページ内順序: 5
- caption/列: variable; mean; median; sd; mad; q5; q95; intercept
- 周辺文脈（EN）: Check whether parameters have reasonable values
- 周辺文脈（JA, 自動訳）: 5.1 モデル 1: 緩やかな傾向 / パラメーターが適切な値であるかどうかを確認する
- Workflowフェーズ: **Model development / debugging**
- 実務での読み方: 小さいモデルから始め、失敗runを観察しながらモデル族・prior・データ処理を段階的に拡張する。
- MLflow連携: `iteration_id, change_reason, failure_mode, hypothesis, next_action`
- 参照: [公式ページ](https://avehtari.github.io/Bayesian-Workflow/birthdays/birthdays.html#tinytable_q76ul4zi967rn8msxqh8) / [ソース候補](https://github.com/avehtari/Bayesian-Workflow/blob/eb00fa4397314ef7d90203382542bd44c590e289/birthdays/birthdays.R)

#### `birthdays-birthdays/tinytable_8mz5a5qdyxvqnr4kufxa`

- 種別: `table` / 公式ID: `tinytable_8mz5a5qdyxvqnr4kufxa` / ページ内順序: 6
- caption/列: variable; mean; median; sd; mad; q5; q95; rhat
- 周辺文脈（EN）: In many of the following short MCMC samplings we get some or many divergences and usually very large number of treedepth exceedences. Divergences indicate possible bias and should
- 周辺文脈（JA, 自動訳）: 5.1 モデル 1: 緩やかな傾向 / 以下の短い MCMC サンプリングの多くで、いくつかまたは多数の発散が発生し、通常は非常に多くのツリー深さの超過が発生します。相違はバイアスの可能性を示しており、そうすべきです
- Workflowフェーズ: **MCMC / computation diagnostics**
- 実務での読み方: 推論結果を解釈する前に、R-hat、ESS、divergence、treedepth、BFMI、trace/pairsを確認する。悪いrunは比較表から除外せず失敗として記録する。
- MLflow連携: `rhat_max, ess_bulk_min, ess_tail_min, divergences, treedepth_hits, bfmi_min`
- 参照: [公式ページ](https://avehtari.github.io/Bayesian-Workflow/birthdays/birthdays.html#tinytable_8mz5a5qdyxvqnr4kufxa) / [ソース候補](https://github.com/avehtari/Bayesian-Workflow/blob/eb00fa4397314ef7d90203382542bd44c590e289/birthdays/birthdays.R)

#### `birthdays-birthdays/tinytable_t2b19szgji5x5u2wualp`

- 種別: `table` / 公式ID: `tinytable_t2b19szgji5x5u2wualp` / ページ内順序: 7
- caption/列: variable; mean; median; sd; mad; q5; q95; rhat
- 周辺文脈（EN）: The sampling is even faster, indicating that the strong posterior correlation in the first model was causing troubles for the adaptation in the short warmup.
- 周辺文脈（JA, 自動訳）: 5.1 モデル 1: 遅い傾向 / サンプリングはさらに速く、最初のモデルの強い事後相関が短いウォームアップでの適応に問題を引き起こしていたことを示しています。
- Workflowフェーズ: **Posterior summary / effect interpretation**
- 実務での読み方: 推定効果・不確実性・派生量を意思決定に接続する。平均だけでなく区間・分布・実務閾値超過確率を残す。
- MLflow連携: `posterior_draws_uri, model_code_hash, ci_width, decision_threshold_prob`
- 参照: [公式ページ](https://avehtari.github.io/Bayesian-Workflow/birthdays/birthdays.html#tinytable_t2b19szgji5x5u2wualp) / [ソース候補](https://github.com/avehtari/Bayesian-Workflow/blob/eb00fa4397314ef7d90203382542bd44c590e289/birthdays/birthdays.R)

#### `birthdays-birthdays/tinytable_j9xscf9lbmisy1lql4pw`

- 種別: `table` / 公式ID: `tinytable_j9xscf9lbmisy1lql4pw` / ページ内順序: 8
- caption/列: variable; n_distinct; lp__; 12
- 周辺文脈（EN）: Check whether parameters have reasonable values
- 周辺文脈（JA, 自動訳）: 5.1.1 モデル 2: 緩やかな傾向 + 年間の季節的傾向 / パラメータが妥当な値であるかどうかを確認する
- Workflowフェーズ: **Model development / debugging**
- 実務での読み方: 小さいモデルから始め、失敗runを観察しながらモデル族・prior・データ処理を段階的に拡張する。
- MLflow連携: `iteration_id, change_reason, failure_mode, hypothesis, next_action`
- 参照: [公式ページ](https://avehtari.github.io/Bayesian-Workflow/birthdays/birthdays.html#tinytable_j9xscf9lbmisy1lql4pw) / [ソース候補](https://github.com/avehtari/Bayesian-Workflow/blob/eb00fa4397314ef7d90203382542bd44c590e289/birthdays/birthdays.R)

#### `birthdays-birthdays/tinytable_fvq2rro22yz0to53ue9t`

- 種別: `table` / 公式ID: `tinytable_fvq2rro22yz0to53ue9t` / ページ内順序: 9
- caption/列: variable; mean; median; sd; mad; q5; q95; sigma_f1
- 周辺文脈（EN）: Check whether parameters have reasonable values
- 周辺文脈（JA, 自動訳）: 5.1.1 モデル 2: 緩やかな傾向 + 年間の季節的傾向 / パラメータが妥当な値であるかどうかを確認する
- Workflowフェーズ: **Model development / debugging**
- 実務での読み方: 小さいモデルから始め、失敗runを観察しながらモデル族・prior・データ処理を段階的に拡張する。
- MLflow連携: `iteration_id, change_reason, failure_mode, hypothesis, next_action`
- 参照: [公式ページ](https://avehtari.github.io/Bayesian-Workflow/birthdays/birthdays.html#tinytable_fvq2rro22yz0to53ue9t) / [ソース候補](https://github.com/avehtari/Bayesian-Workflow/blob/eb00fa4397314ef7d90203382542bd44c590e289/birthdays/birthdays.R)

#### `birthdays-birthdays/tinytable_pk0zs5kz55p8ermfs7kn`

- 種別: `table` / 公式ID: `tinytable_pk0zs5kz55p8ermfs7kn` / ページ内順序: 10
- caption/列: variable; mean; median; sd; mad; q5; q95; rhat
- 周辺文脈（EN）: Check whether parameters have reasonable values
- 周辺文脈（JA, 自動訳）: 5.1.1 モデル 2: 緩やかな傾向 + 年間の季節的傾向 / パラメータが妥当な値であるかどうかを確認する
- Workflowフェーズ: **Model development / debugging**
- 実務での読み方: 小さいモデルから始め、失敗runを観察しながらモデル族・prior・データ処理を段階的に拡張する。
- MLflow連携: `iteration_id, change_reason, failure_mode, hypothesis, next_action`
- 参照: [公式ページ](https://avehtari.github.io/Bayesian-Workflow/birthdays/birthdays.html#tinytable_pk0zs5kz55p8ermfs7kn) / [ソース候補](https://github.com/avehtari/Bayesian-Workflow/blob/eb00fa4397314ef7d90203382542bd44c590e289/birthdays/birthdays.R)

#### `birthdays-birthdays/tinytable_4ea6jrehxme661tu19y3`

- 種別: `table` / 公式ID: `tinytable_4ea6jrehxme661tu19y3` / ページ内順序: 11
- caption/列: variable; n_distinct; lp__; 8
- 周辺文脈（EN）: Check whether parameters have reasonable values
- 周辺文脈（JA, 自動訳）: 5.1.2 モデル 3: 緩やかな傾向 + 年間季節傾向 + 曜日 / パラメータが妥当な値であるかどうかを確認する
- Workflowフェーズ: **Model development / debugging**
- 実務での読み方: 小さいモデルから始め、失敗runを観察しながらモデル族・prior・データ処理を段階的に拡張する。
- MLflow連携: `iteration_id, change_reason, failure_mode, hypothesis, next_action`
- 参照: [公式ページ](https://avehtari.github.io/Bayesian-Workflow/birthdays/birthdays.html#tinytable_4ea6jrehxme661tu19y3) / [ソース候補](https://github.com/avehtari/Bayesian-Workflow/blob/eb00fa4397314ef7d90203382542bd44c590e289/birthdays/birthdays.R)

#### `birthdays-birthdays/tinytable_ef2hduaaqvo3vg5zzpco`

- 種別: `table` / 公式ID: `tinytable_ef2hduaaqvo3vg5zzpco` / ページ内順序: 12
- caption/列: variable; mean; median; sd; mad; q5; q95; sigma_f1
- 周辺文脈（EN）: Check whether parameters have reasonable values
- 周辺文脈（JA, 自動訳）: 5.1.2 モデル 3: 緩やかな傾向 + 年間季節傾向 + 曜日 / パラメータが妥当な値であるかどうかを確認する
- Workflowフェーズ: **Model development / debugging**
- 実務での読み方: 小さいモデルから始め、失敗runを観察しながらモデル族・prior・データ処理を段階的に拡張する。
- MLflow連携: `iteration_id, change_reason, failure_mode, hypothesis, next_action`
- 参照: [公式ページ](https://avehtari.github.io/Bayesian-Workflow/birthdays/birthdays.html#tinytable_ef2hduaaqvo3vg5zzpco) / [ソース候補](https://github.com/avehtari/Bayesian-Workflow/blob/eb00fa4397314ef7d90203382542bd44c590e289/birthdays/birthdays.R)

#### `birthdays-birthdays/tinytable_zmnxc3b23u0toxnxzy3q`

- 種別: `table` / 公式ID: `tinytable_zmnxc3b23u0toxnxzy3q` / ページ内順序: 13
- caption/列: variable; mean; median; sd; mad; q5; q95; rhat
- 周辺文脈（EN）: Check whether parameters have reasonable values
- 周辺文脈（JA, 自動訳）: 5.1.2 モデル 3: 緩やかな傾向 + 年間季節傾向 + 曜日 / パラメータが妥当な値であるかどうかを確認する
- Workflowフェーズ: **Model development / debugging**
- 実務での読み方: 小さいモデルから始め、失敗runを観察しながらモデル族・prior・データ処理を段階的に拡張する。
- MLflow連携: `iteration_id, change_reason, failure_mode, hypothesis, next_action`
- 参照: [公式ページ](https://avehtari.github.io/Bayesian-Workflow/birthdays/birthdays.html#tinytable_zmnxc3b23u0toxnxzy3q) / [ソース候補](https://github.com/avehtari/Bayesian-Workflow/blob/eb00fa4397314ef7d90203382542bd44c590e289/birthdays/birthdays.R)

#### `birthdays-birthdays/tinytable_700m8wnm1hdi70qso11z`

- 種別: `table` / 公式ID: `tinytable_700m8wnm1hdi70qso11z` / ページ内順序: 14
- caption/列: variable; mean; median; sd; mad; q5; q95; rhat
- 周辺文脈（EN）: Check whether parameters have reasonable values
- 周辺文脈（JA, 自動訳）: 5.1.2 モデル 3: 緩やかな傾向 + 年間季節傾向 + 曜日 / パラメータが妥当な値であるかどうかを確認する
- Workflowフェーズ: **Model development / debugging**
- 実務での読み方: 小さいモデルから始め、失敗runを観察しながらモデル族・prior・データ処理を段階的に拡張する。
- MLflow連携: `iteration_id, change_reason, failure_mode, hypothesis, next_action`
- 参照: [公式ページ](https://avehtari.github.io/Bayesian-Workflow/birthdays/birthdays.html#tinytable_700m8wnm1hdi70qso11z) / [ソース候補](https://github.com/avehtari/Bayesian-Workflow/blob/eb00fa4397314ef7d90203382542bd44c590e289/birthdays/birthdays.R)

#### `birthdays-birthdays/tinytable_r7xz9el21lcku51rjugc`

- 種別: `table` / 公式ID: `tinytable_r7xz9el21lcku51rjugc` / ページ内順序: 15
- caption/列: variable; n_distinct; lp__; 10
- 周辺文脈（EN）: Check whether parameters have reasonable values
- 周辺文脈（JA, 自動訳）: 5.1.3 モデル 4: 長期間の平滑 + 季節 + 規模が増加する平日 / パラメーターが妥当な値であるかどうかを確認する
- Workflowフェーズ: **Model development / debugging**
- 実務での読み方: 小さいモデルから始め、失敗runを観察しながらモデル族・prior・データ処理を段階的に拡張する。
- MLflow連携: `iteration_id, change_reason, failure_mode, hypothesis, next_action`
- 参照: [公式ページ](https://avehtari.github.io/Bayesian-Workflow/birthdays/birthdays.html#tinytable_r7xz9el21lcku51rjugc) / [ソース候補](https://github.com/avehtari/Bayesian-Workflow/blob/eb00fa4397314ef7d90203382542bd44c590e289/birthdays/birthdays.R)

#### `birthdays-birthdays/tinytable_3oiytf7rgyfjpl0n6vmg`

- 種別: `table` / 公式ID: `tinytable_3oiytf7rgyfjpl0n6vmg` / ページ内順序: 16
- caption/列: variable; mean; median; sd; mad; q5; q95; sigma_f1
- 周辺文脈（EN）: Check whether parameters have reasonable values
- 周辺文脈（JA, 自動訳）: 5.1.3 モデル 4: 長期間の平滑 + 季節 + 規模が増加する平日 / パラメーターが妥当な値であるかどうかを確認する
- Workflowフェーズ: **Model development / debugging**
- 実務での読み方: 小さいモデルから始め、失敗runを観察しながらモデル族・prior・データ処理を段階的に拡張する。
- MLflow連携: `iteration_id, change_reason, failure_mode, hypothesis, next_action`
- 参照: [公式ページ](https://avehtari.github.io/Bayesian-Workflow/birthdays/birthdays.html#tinytable_3oiytf7rgyfjpl0n6vmg) / [ソース候補](https://github.com/avehtari/Bayesian-Workflow/blob/eb00fa4397314ef7d90203382542bd44c590e289/birthdays/birthdays.R)

#### `birthdays-birthdays/tinytable_g7jnezi7qk1r0tsdwttv`

- 種別: `table` / 公式ID: `tinytable_g7jnezi7qk1r0tsdwttv` / ページ内順序: 17
- caption/列: variable; mean; median; sd; mad; q5; q95; rhat
- 周辺文脈（EN）: Check whether parameters have reasonable values
- 周辺文脈（JA, 自動訳）: 5.1.3 モデル 4: 長期間の平滑 + 季節 + 規模が増加する平日 / パラメーターが妥当な値であるかどうかを確認する
- Workflowフェーズ: **Model development / debugging**
- 実務での読み方: 小さいモデルから始め、失敗runを観察しながらモデル族・prior・データ処理を段階的に拡張する。
- MLflow連携: `iteration_id, change_reason, failure_mode, hypothesis, next_action`
- 参照: [公式ページ](https://avehtari.github.io/Bayesian-Workflow/birthdays/birthdays.html#tinytable_g7jnezi7qk1r0tsdwttv) / [ソース候補](https://github.com/avehtari/Bayesian-Workflow/blob/eb00fa4397314ef7d90203382542bd44c590e289/birthdays/birthdays.R)

#### `birthdays-birthdays/tinytable_0shee83hwf1ug41bvs5g`

- 種別: `table` / 公式ID: `tinytable_0shee83hwf1ug41bvs5g` / ページ内順序: 18
- caption/列: variable; mean; median; sd; mad; q5; q95; rhat
- 周辺文脈（EN）: Check whether parameters have reasonable values
- 周辺文脈（JA, 自動訳）: 5.1.3 モデル 4: 長期間の平滑 + 季節 + 規模が増加する平日 / パラメーターが妥当な値であるかどうかを確認する
- Workflowフェーズ: **Model development / debugging**
- 実務での読み方: 小さいモデルから始め、失敗runを観察しながらモデル族・prior・データ処理を段階的に拡張する。
- MLflow連携: `iteration_id, change_reason, failure_mode, hypothesis, next_action`
- 参照: [公式ページ](https://avehtari.github.io/Bayesian-Workflow/birthdays/birthdays.html#tinytable_0shee83hwf1ug41bvs5g) / [ソース候補](https://github.com/avehtari/Bayesian-Workflow/blob/eb00fa4397314ef7d90203382542bd44c590e289/birthdays/birthdays.R)

#### `birthdays-birthdays/tinytable_xwzqoyvzj02g0vq3z3s5`

- 種別: `table` / 公式ID: `tinytable_xwzqoyvzj02g0vq3z3s5` / ページ内順序: 19
- caption/列: variable; n_distinct; lp__; 1
- 周辺文脈（EN）: Check whether parameters have reasonable values
- 周辺文脈（JA, 自動訳）: 5.1.4 モデル 5: 長期平滑 + 季節 + 時間に依存する大きさを持つ平日 + 年間の曜日 RHS / パラメーターが妥当な値であるかどうかを確認する
- Workflowフェーズ: **Model development / debugging**
- 実務での読み方: 小さいモデルから始め、失敗runを観察しながらモデル族・prior・データ処理を段階的に拡張する。
- MLflow連携: `iteration_id, change_reason, failure_mode, hypothesis, next_action`
- 参照: [公式ページ](https://avehtari.github.io/Bayesian-Workflow/birthdays/birthdays.html#tinytable_xwzqoyvzj02g0vq3z3s5) / [ソース候補](https://github.com/avehtari/Bayesian-Workflow/blob/eb00fa4397314ef7d90203382542bd44c590e289/birthdays/birthdays.R)

#### `birthdays-birthdays/tinytable_5vyp3hrrvtvekd3xweap`

- 種別: `table` / 公式ID: `tinytable_5vyp3hrrvtvekd3xweap` / ページ内順序: 20
- caption/列: variable; mean; median; sd; mad; q5; q95; sigma_f1
- 周辺文脈（EN）: Check whether parameters have reasonable values
- 周辺文脈（JA, 自動訳）: 5.1.4 モデル 5: 長期平滑 + 季節 + 時間に依存する大きさを持つ平日 + 年間の曜日 RHS / パラメーターが妥当な値であるかどうかを確認する
- Workflowフェーズ: **Model development / debugging**
- 実務での読み方: 小さいモデルから始め、失敗runを観察しながらモデル族・prior・データ処理を段階的に拡張する。
- MLflow連携: `iteration_id, change_reason, failure_mode, hypothesis, next_action`
- 参照: [公式ページ](https://avehtari.github.io/Bayesian-Workflow/birthdays/birthdays.html#tinytable_5vyp3hrrvtvekd3xweap) / [ソース候補](https://github.com/avehtari/Bayesian-Workflow/blob/eb00fa4397314ef7d90203382542bd44c590e289/birthdays/birthdays.R)

#### `birthdays-birthdays/tinytable_14s0r97jx44ssaqvpj3j`

- 種別: `table` / 公式ID: `tinytable_14s0r97jx44ssaqvpj3j` / ページ内順序: 21
- caption/列: variable; mean; median; sd; mad; q5; q95; beta_f3[1]
- 周辺文脈（EN）: Check whether parameters have reasonable values
- 周辺文脈（JA, 自動訳）: 5.1.4 モデル 5: 長期平滑 + 季節 + 時間に依存する大きさを持つ平日 + 年間の曜日 RHS / パラメーターが妥当な値であるかどうかを確認する
- Workflowフェーズ: **Model development / debugging**
- 実務での読み方: 小さいモデルから始め、失敗runを観察しながらモデル族・prior・データ処理を段階的に拡張する。
- MLflow連携: `iteration_id, change_reason, failure_mode, hypothesis, next_action`
- 参照: [公式ページ](https://avehtari.github.io/Bayesian-Workflow/birthdays/birthdays.html#tinytable_14s0r97jx44ssaqvpj3j) / [ソース候補](https://github.com/avehtari/Bayesian-Workflow/blob/eb00fa4397314ef7d90203382542bd44c590e289/birthdays/birthdays.R)

#### `birthdays-birthdays/tinytable_dm91jh6v84eb9e9p07ms`

- 種別: `table` / 公式ID: `tinytable_dm91jh6v84eb9e9p07ms` / ページ内順序: 22
- caption/列: variable; n_distinct; lp__; 400
- 周辺文脈（EN）: We check the number of distinct draws, which is now higher (no resampling).
- 周辺文脈（JA, 自動訳）: 5.1.4 モデル 5: 長期平滑 + 季節 + 時間依存の大きさを持つ平日 + 年間の曜日 RHS / 個別の描画の数を確認しますが、これは現在より多くなっています (リサンプリングなし)。
- Workflowフェーズ: **Posterior summary / effect interpretation**
- 実務での読み方: 推定効果・不確実性・派生量を意思決定に接続する。平均だけでなく区間・分布・実務閾値超過確率を残す。
- MLflow連携: `posterior_draws_uri, model_code_hash, ci_width, decision_threshold_prob`
- 参照: [公式ページ](https://avehtari.github.io/Bayesian-Workflow/birthdays/birthdays.html#tinytable_dm91jh6v84eb9e9p07ms) / [ソース候補](https://github.com/avehtari/Bayesian-Workflow/blob/eb00fa4397314ef7d90203382542bd44c590e289/birthdays/birthdays.R)

#### `birthdays-birthdays/tinytable_gms1kf0x2y3jz99po2zg`

- 種別: `table` / 公式ID: `tinytable_gms1kf0x2y3jz99po2zg` / ページ内順序: 23
- caption/列: variable; n_distinct; lp__; 4
- 周辺文脈（EN）: We have now 4 distinct draws.
- 周辺文脈（JA, 自動訳）: 5.1.4 モデル 5: 長期平滑 + 季節 + 時間依存の大きさを持つ平日 + 年間の曜日 RHS / 現在、4 つの異なるドローがあります。
- Workflowフェーズ: **Posterior summary / effect interpretation**
- 実務での読み方: 推定効果・不確実性・派生量を意思決定に接続する。平均だけでなく区間・分布・実務閾値超過確率を残す。
- MLflow連携: `posterior_draws_uri, model_code_hash, ci_width, decision_threshold_prob`
- 参照: [公式ページ](https://avehtari.github.io/Bayesian-Workflow/birthdays/birthdays.html#tinytable_gms1kf0x2y3jz99po2zg) / [ソース候補](https://github.com/avehtari/Bayesian-Workflow/blob/eb00fa4397314ef7d90203382542bd44c590e289/birthdays/birthdays.R)

#### `birthdays-birthdays/tinytable_dlz65gsjagxdjmfeqrz9`

- 種別: `table` / 公式ID: `tinytable_dlz65gsjagxdjmfeqrz9` / ページ内順序: 24
- caption/列: variable; mean; median; sd; mad; q5; q95; rhat
- 周辺文脈（EN）: Check whether parameters have reasonable values
- 周辺文脈（JA, 自動訳）: 5.1.4 モデル 5: 長期平滑 + 季節 + 時間に依存する大きさを持つ平日 + 年間の曜日 RHS / パラメーターが妥当な値であるかどうかを確認する
- Workflowフェーズ: **Model development / debugging**
- 実務での読み方: 小さいモデルから始め、失敗runを観察しながらモデル族・prior・データ処理を段階的に拡張する。
- MLflow連携: `iteration_id, change_reason, failure_mode, hypothesis, next_action`
- 参照: [公式ページ](https://avehtari.github.io/Bayesian-Workflow/birthdays/birthdays.html#tinytable_dlz65gsjagxdjmfeqrz9) / [ソース候補](https://github.com/avehtari/Bayesian-Workflow/blob/eb00fa4397314ef7d90203382542bd44c590e289/birthdays/birthdays.R)

#### `birthdays-birthdays/tinytable_s6plvs9i0bdcvkp5fkxo`

- 種別: `table` / 公式ID: `tinytable_s6plvs9i0bdcvkp5fkxo` / ページ内順序: 25
- caption/列: variable; mean; median; sd; mad; q5; q95; rhat
- 周辺文脈（EN）: Check whether parameters have reasonable values
- 周辺文脈（JA, 自動訳）: 5.1.4 モデル 5: 長期平滑 + 季節 + 時間に依存する大きさを持つ平日 + 年間の曜日 RHS / パラメーターが妥当な値であるかどうかを確認する
- Workflowフェーズ: **Model development / debugging**
- 実務での読み方: 小さいモデルから始め、失敗runを観察しながらモデル族・prior・データ処理を段階的に拡張する。
- MLflow連携: `iteration_id, change_reason, failure_mode, hypothesis, next_action`
- 参照: [公式ページ](https://avehtari.github.io/Bayesian-Workflow/birthdays/birthdays.html#tinytable_s6plvs9i0bdcvkp5fkxo) / [ソース候補](https://github.com/avehtari/Bayesian-Workflow/blob/eb00fa4397314ef7d90203382542bd44c590e289/birthdays/birthdays.R)

#### `birthdays-birthdays/tinytable_kca2iaserm3wrvfl1xth`

- 種別: `table` / 公式ID: `tinytable_kca2iaserm3wrvfl1xth` / ページ内順序: 26
- caption/列: variable; n_distinct; lp__; 1
- 周辺文脈（EN）: Pathfinder provides automatically Pareto- \hat{k} diagnostic which is high, indicating the normal approximation is not good. When Pareto- \hat{k} is very high the Pareto smoothed i
- 周辺文脈（JA, 自動訳）: 5.1.5 モデル 6: 長期平滑 + 季節 + 平日 + 年間通算日 / パスファインダーは、パレート-\hat{k} 診断を自動的に提供します。これは、正規近似が適切ではないことを示します。パレート- \hat{k} が非常に高い場合、パレート平滑化 i
- Workflowフェーズ: **LOO-CV / model comparison**
- 実務での読み方: elpd差だけでなくSEとPareto-kを読み、勝敗より『どのデータ点で負けるか』を確認する。
- MLflow連携: `loo_elpd, loo_elpd_diff, loo_se_diff, pareto_k_gt_0_7, reloo_count`
- 参照: [公式ページ](https://avehtari.github.io/Bayesian-Workflow/birthdays/birthdays.html#tinytable_kca2iaserm3wrvfl1xth) / [ソース候補](https://github.com/avehtari/Bayesian-Workflow/blob/eb00fa4397314ef7d90203382542bd44c590e289/birthdays/birthdays.R)

#### `birthdays-birthdays/tinytable_jnfa4bwietxlyxl5ou2v`

- 種別: `table` / 公式ID: `tinytable_jnfa4bwietxlyxl5ou2v` / ページ内順序: 27
- caption/列: variable; mean; median; sd; mad; q5; q95; sigma_f1
- 周辺文脈（EN）: Pathfinder provides automatically Pareto- \hat{k} diagnostic which is high, indicating the normal approximation is not good. When Pareto- \hat{k} is very high the Pareto smoothed i
- 周辺文脈（JA, 自動訳）: 5.1.5 モデル 6: 長期平滑 + 季節 + 平日 + 年間通算日 / パスファインダーは、パレート-\hat{k} 診断を自動的に提供します。これは、正規近似が適切ではないことを示します。パレート- \hat{k} が非常に高い場合、パレート平滑化 i
- Workflowフェーズ: **LOO-CV / model comparison**
- 実務での読み方: elpd差だけでなくSEとPareto-kを読み、勝敗より『どのデータ点で負けるか』を確認する。
- MLflow連携: `loo_elpd, loo_elpd_diff, loo_se_diff, pareto_k_gt_0_7, reloo_count`
- 参照: [公式ページ](https://avehtari.github.io/Bayesian-Workflow/birthdays/birthdays.html#tinytable_jnfa4bwietxlyxl5ou2v) / [ソース候補](https://github.com/avehtari/Bayesian-Workflow/blob/eb00fa4397314ef7d90203382542bd44c590e289/birthdays/birthdays.R)

#### `birthdays-birthdays/tinytable_zv8hettxjf4epg3n2k04`

- 種別: `table` / 公式ID: `tinytable_zv8hettxjf4epg3n2k04` / ページ内順序: 28
- caption/列: variable; mean; median; sd; mad; q5; q95; beta_f3[1]
- 周辺文脈（EN）: Pathfinder provides automatically Pareto- \hat{k} diagnostic which is high, indicating the normal approximation is not good. When Pareto- \hat{k} is very high the Pareto smoothed i
- 周辺文脈（JA, 自動訳）: 5.1.5 モデル 6: 長期平滑 + 季節 + 平日 + 年間通算日 / パスファインダーは、パレート-\hat{k} 診断を自動的に提供します。これは、正規近似が適切ではないことを示します。パレート- \hat{k} が非常に高い場合、パレート平滑化 i
- Workflowフェーズ: **LOO-CV / model comparison**
- 実務での読み方: elpd差だけでなくSEとPareto-kを読み、勝敗より『どのデータ点で負けるか』を確認する。
- MLflow連携: `loo_elpd, loo_elpd_diff, loo_se_diff, pareto_k_gt_0_7, reloo_count`
- 参照: [公式ページ](https://avehtari.github.io/Bayesian-Workflow/birthdays/birthdays.html#tinytable_zv8hettxjf4epg3n2k04) / [ソース候補](https://github.com/avehtari/Bayesian-Workflow/blob/eb00fa4397314ef7d90203382542bd44c590e289/birthdays/birthdays.R)

#### `birthdays-birthdays/tinytable_mlsyjk91rart6vba1o1y`

- 種別: `table` / 公式ID: `tinytable_mlsyjk91rart6vba1o1y` / ページ内順序: 29
- caption/列: variable; mean; median; sd; mad; q5; q95; rhat
- 周辺文脈（EN）: Check whether parameters have reasonable values
- 周辺文脈（JA, 自動訳）: 5.1.5 モデル 6: 長期平滑 + 季節 + 平日 + 曜日 / パラメータが妥当な値であるかどうかを確認する
- Workflowフェーズ: **Model development / debugging**
- 実務での読み方: 小さいモデルから始め、失敗runを観察しながらモデル族・prior・データ処理を段階的に拡張する。
- MLflow連携: `iteration_id, change_reason, failure_mode, hypothesis, next_action`
- 参照: [公式ページ](https://avehtari.github.io/Bayesian-Workflow/birthdays/birthdays.html#tinytable_mlsyjk91rart6vba1o1y) / [ソース候補](https://github.com/avehtari/Bayesian-Workflow/blob/eb00fa4397314ef7d90203382542bd44c590e289/birthdays/birthdays.R)

#### `birthdays-birthdays/tinytable_rbza5g5avqbazsv6s1er`

- 種別: `table` / 公式ID: `tinytable_rbza5g5avqbazsv6s1er` / ページ内順序: 30
- caption/列: variable; mean; median; sd; mad; q5; q95; rhat
- 周辺文脈（EN）: Check whether parameters have reasonable values
- 周辺文脈（JA, 自動訳）: 5.1.5 モデル 6: 長期平滑 + 季節 + 平日 + 曜日 / パラメータが妥当な値であるかどうかを確認する
- Workflowフェーズ: **Model development / debugging**
- 実務での読み方: 小さいモデルから始め、失敗runを観察しながらモデル族・prior・データ処理を段階的に拡張する。
- MLflow連携: `iteration_id, change_reason, failure_mode, hypothesis, next_action`
- 参照: [公式ページ](https://avehtari.github.io/Bayesian-Workflow/birthdays/birthdays.html#tinytable_rbza5g5avqbazsv6s1er) / [ソース候補](https://github.com/avehtari/Bayesian-Workflow/blob/eb00fa4397314ef7d90203382542bd44c590e289/birthdays/birthdays.R)

#### `birthdays-birthdays/tinytable_1kotzxgyjfzfmu3o2mu9`

- 種別: `table` / 公式ID: `tinytable_1kotzxgyjfzfmu3o2mu9` / ページ内順序: 31
- caption/列: variable; n_distinct; lp__; 1
- 周辺文脈（EN）: Check whether parameters have reasonable values
- 周辺文脈（JA, 自動訳）: 5.1.6 モデル 7: 長期平滑 + 季節 + 平日 + 通常日 + 変動特別日 / パラメータが妥当な値であるかどうかを確認する
- Workflowフェーズ: **Model development / debugging**
- 実務での読み方: 小さいモデルから始め、失敗runを観察しながらモデル族・prior・データ処理を段階的に拡張する。
- MLflow連携: `iteration_id, change_reason, failure_mode, hypothesis, next_action`
- 参照: [公式ページ](https://avehtari.github.io/Bayesian-Workflow/birthdays/birthdays.html#tinytable_1kotzxgyjfzfmu3o2mu9) / [ソース候補](https://github.com/avehtari/Bayesian-Workflow/blob/eb00fa4397314ef7d90203382542bd44c590e289/birthdays/birthdays.R)

#### `birthdays-birthdays/tinytable_dbhh2m7y28bj9suw7ofj`

- 種別: `table` / 公式ID: `tinytable_dbhh2m7y28bj9suw7ofj` / ページ内順序: 32
- caption/列: variable; mean; median; sd; mad; q5; q95; sigma_f1
- 周辺文脈（EN）: Check whether parameters have reasonable values
- 周辺文脈（JA, 自動訳）: 5.1.6 モデル 7: 長期平滑 + 季節 + 平日 + 通常日 + 変動特別日 / パラメータが妥当な値であるかどうかを確認する
- Workflowフェーズ: **Model development / debugging**
- 実務での読み方: 小さいモデルから始め、失敗runを観察しながらモデル族・prior・データ処理を段階的に拡張する。
- MLflow連携: `iteration_id, change_reason, failure_mode, hypothesis, next_action`
- 参照: [公式ページ](https://avehtari.github.io/Bayesian-Workflow/birthdays/birthdays.html#tinytable_dbhh2m7y28bj9suw7ofj) / [ソース候補](https://github.com/avehtari/Bayesian-Workflow/blob/eb00fa4397314ef7d90203382542bd44c590e289/birthdays/birthdays.R)

#### `birthdays-birthdays/tinytable_7x212w6745netq88710e`

- 種別: `table` / 公式ID: `tinytable_7x212w6745netq88710e` / ページ内順序: 33
- caption/列: variable; mean; median; sd; mad; q5; q95; beta_f3[1]
- 周辺文脈（EN）: Check whether parameters have reasonable values
- 周辺文脈（JA, 自動訳）: 5.1.6 モデル 7: 長期平滑 + 季節 + 平日 + 通常日 + 変動特別日 / パラメータが妥当な値であるかどうかを確認する
- Workflowフェーズ: **Model development / debugging**
- 実務での読み方: 小さいモデルから始め、失敗runを観察しながらモデル族・prior・データ処理を段階的に拡張する。
- MLflow連携: `iteration_id, change_reason, failure_mode, hypothesis, next_action`
- 参照: [公式ページ](https://avehtari.github.io/Bayesian-Workflow/birthdays/birthdays.html#tinytable_7x212w6745netq88710e) / [ソース候補](https://github.com/avehtari/Bayesian-Workflow/blob/eb00fa4397314ef7d90203382542bd44c590e289/birthdays/birthdays.R)

#### `birthdays-birthdays/tinytable_wwua5yzng0fftqxlvz0d`

- 種別: `table` / 公式ID: `tinytable_wwua5yzng0fftqxlvz0d` / ページ内順序: 34
- caption/列: variable; mean; median; sd; mad; q5; q95; rhat
- 周辺文脈（EN）: Check whether parameters have reasonable values
- 周辺文脈（JA, 自動訳）: 5.1.6 モデル 7: 長期平滑 + 季節 + 平日 + 通常日 + 変動特別日 / パラメータが妥当な値であるかどうかを確認する
- Workflowフェーズ: **Model development / debugging**
- 実務での読み方: 小さいモデルから始め、失敗runを観察しながらモデル族・prior・データ処理を段階的に拡張する。
- MLflow連携: `iteration_id, change_reason, failure_mode, hypothesis, next_action`
- 参照: [公式ページ](https://avehtari.github.io/Bayesian-Workflow/birthdays/birthdays.html#tinytable_wwua5yzng0fftqxlvz0d) / [ソース候補](https://github.com/avehtari/Bayesian-Workflow/blob/eb00fa4397314ef7d90203382542bd44c590e289/birthdays/birthdays.R)

#### `birthdays-birthdays/tinytable_t1p3k9pzn6vpxhppoqkz`

- 種別: `table` / 公式ID: `tinytable_t1p3k9pzn6vpxhppoqkz` / ページ内順序: 35
- caption/列: variable; mean; median; sd; mad; q5; q95; rhat
- 周辺文脈（EN）: Check whether parameters have reasonable values
- 周辺文脈（JA, 自動訳）: 5.1.6 モデル 7: 長期平滑 + 季節 + 平日 + 通常日 + 変動特別日 / パラメータが妥当な値であるかどうかを確認する
- Workflowフェーズ: **Model development / debugging**
- 実務での読み方: 小さいモデルから始め、失敗runを観察しながらモデル族・prior・データ処理を段階的に拡張する。
- MLflow連携: `iteration_id, change_reason, failure_mode, hypothesis, next_action`
- 参照: [公式ページ](https://avehtari.github.io/Bayesian-Workflow/birthdays/birthdays.html#tinytable_t1p3k9pzn6vpxhppoqkz) / [ソース候補](https://github.com/avehtari/Bayesian-Workflow/blob/eb00fa4397314ef7d90203382542bd44c590e289/birthdays/birthdays.R)

#### `birthdays-birthdays/tinytable_61gn8c4ol6607xlzelg4`

- 種別: `table` / 公式ID: `tinytable_61gn8c4ol6607xlzelg4` / ページ内順序: 36
- caption/列: variable; n_distinct; lp__; 2
- 周辺文脈（EN）: Check whether parameters have reasonable values
- 周辺文脈（JA, 自動訳）: 5.1.7 モデル 8: 長期平滑 + 季節 + 時間依存の大きさを持つ平日 + 年間の曜日 + 特別 / パラメータが妥当な値であるかどうかを確認する
- Workflowフェーズ: **Model development / debugging**
- 実務での読み方: 小さいモデルから始め、失敗runを観察しながらモデル族・prior・データ処理を段階的に拡張する。
- MLflow連携: `iteration_id, change_reason, failure_mode, hypothesis, next_action`
- 参照: [公式ページ](https://avehtari.github.io/Bayesian-Workflow/birthdays/birthdays.html#tinytable_61gn8c4ol6607xlzelg4) / [ソース候補](https://github.com/avehtari/Bayesian-Workflow/blob/eb00fa4397314ef7d90203382542bd44c590e289/birthdays/birthdays.R)

#### `birthdays-birthdays/tinytable_ud8hbghzogvhngj3hqbv`

- 種別: `table` / 公式ID: `tinytable_ud8hbghzogvhngj3hqbv` / ページ内順序: 37
- caption/列: variable; mean; median; sd; mad; q5; q95; sigma_f1
- 周辺文脈（EN）: Check whether parameters have reasonable values
- 周辺文脈（JA, 自動訳）: 5.1.7 モデル 8: 長期平滑 + 季節 + 時間依存の大きさを持つ平日 + 年間の曜日 + 特別 / パラメータが妥当な値であるかどうかを確認する
- Workflowフェーズ: **Model development / debugging**
- 実務での読み方: 小さいモデルから始め、失敗runを観察しながらモデル族・prior・データ処理を段階的に拡張する。
- MLflow連携: `iteration_id, change_reason, failure_mode, hypothesis, next_action`
- 参照: [公式ページ](https://avehtari.github.io/Bayesian-Workflow/birthdays/birthdays.html#tinytable_ud8hbghzogvhngj3hqbv) / [ソース候補](https://github.com/avehtari/Bayesian-Workflow/blob/eb00fa4397314ef7d90203382542bd44c590e289/birthdays/birthdays.R)

#### `birthdays-birthdays/tinytable_ua41eeeknkqoqwcir36b`

- 種別: `table` / 公式ID: `tinytable_ua41eeeknkqoqwcir36b` / ページ内順序: 38
- caption/列: variable; mean; median; sd; mad; q5; q95; beta_f3[1]
- 周辺文脈（EN）: Check whether parameters have reasonable values
- 周辺文脈（JA, 自動訳）: 5.1.7 モデル 8: 長期平滑 + 季節 + 時間依存の大きさを持つ平日 + 年間の曜日 + 特別 / パラメータが妥当な値であるかどうかを確認する
- Workflowフェーズ: **Model development / debugging**
- 実務での読み方: 小さいモデルから始め、失敗runを観察しながらモデル族・prior・データ処理を段階的に拡張する。
- MLflow連携: `iteration_id, change_reason, failure_mode, hypothesis, next_action`
- 参照: [公式ページ](https://avehtari.github.io/Bayesian-Workflow/birthdays/birthdays.html#tinytable_ua41eeeknkqoqwcir36b) / [ソース候補](https://github.com/avehtari/Bayesian-Workflow/blob/eb00fa4397314ef7d90203382542bd44c590e289/birthdays/birthdays.R)

#### `birthdays-birthdays/tinytable_040sywpmuadrqufxjo9q`

- 種別: `table` / 公式ID: `tinytable_040sywpmuadrqufxjo9q` / ページ内順序: 39
- caption/列: variable; mean; median; sd; mad; q5; q95; rhat
- 周辺文脈（EN）: Check whether parameters have reasonable values
- 周辺文脈（JA, 自動訳）: 5.1.7 モデル 8: 長期平滑 + 季節 + 時間依存の大きさを持つ平日 + 年間の曜日 + 特別 / パラメータが妥当な値であるかどうかを確認する
- Workflowフェーズ: **Model development / debugging**
- 実務での読み方: 小さいモデルから始め、失敗runを観察しながらモデル族・prior・データ処理を段階的に拡張する。
- MLflow連携: `iteration_id, change_reason, failure_mode, hypothesis, next_action`
- 参照: [公式ページ](https://avehtari.github.io/Bayesian-Workflow/birthdays/birthdays.html#tinytable_040sywpmuadrqufxjo9q) / [ソース候補](https://github.com/avehtari/Bayesian-Workflow/blob/eb00fa4397314ef7d90203382542bd44c590e289/birthdays/birthdays.R)

#### `birthdays-birthdays/tinytable_xwbi6f7bw9crrdcgaudi`

- 種別: `table` / 公式ID: `tinytable_xwbi6f7bw9crrdcgaudi` / ページ内順序: 40
- caption/列: variable; mean; median; sd; mad; q5; q95; rhat
- 周辺文脈（EN）: Check whether parameters have reasonable values
- 周辺文脈（JA, 自動訳）: 5.1.7 モデル 8: 長期平滑 + 季節 + 時間依存の大きさを持つ平日 + 年間の曜日 + 特別 / パラメータが妥当な値であるかどうかを確認する
- Workflowフェーズ: **Model development / debugging**
- 実務での読み方: 小さいモデルから始め、失敗runを観察しながらモデル族・prior・データ処理を段階的に拡張する。
- MLflow連携: `iteration_id, change_reason, failure_mode, hypothesis, next_action`
- 参照: [公式ページ](https://avehtari.github.io/Bayesian-Workflow/birthdays/birthdays.html#tinytable_xwbi6f7bw9crrdcgaudi) / [ソース候補](https://github.com/avehtari/Bayesian-Workflow/blob/eb00fa4397314ef7d90203382542bd44c590e289/birthdays/birthdays.R)

#### `birthdays-birthdays/tinytable_uho11qx3xkf0fm0o4621`

- 種別: `table` / 公式ID: `tinytable_uho11qx3xkf0fm0o4621` / ページ内順序: 41
- caption/列: variable; mean; median; sd; mad; q5; q95; rhat
- 周辺文脈（EN）: Check whether parameters have reasonable values
- 周辺文脈（JA, 自動訳）: 5.1.8 モデル 8+t_nu: 学生の t 事前値による年間の曜日の効果 / パラメータが妥当な値であるかどうかを確認する
- Workflowフェーズ: **Posterior summary / effect interpretation**
- 実務での読み方: 推定効果・不確実性・派生量を意思決定に接続する。平均だけでなく区間・分布・実務閾値超過確率を残す。
- MLflow連携: `posterior_draws_uri, model_code_hash, ci_width, decision_threshold_prob`
- 参照: [公式ページ](https://avehtari.github.io/Bayesian-Workflow/birthdays/birthdays.html#tinytable_uho11qx3xkf0fm0o4621) / [ソース候補](https://github.com/avehtari/Bayesian-Workflow/blob/eb00fa4397314ef7d90203382542bd44c590e289/birthdays/birthdays.R)

#### `birthdays-birthdays/tinytable_uvwyjbx7ypxwfslrr5hk`

- 種別: `table` / 公式ID: `tinytable_uvwyjbx7ypxwfslrr5hk` / ページ内順序: 42
- caption/列: model; elpd_diff; se_diff; Model 8 Student's t; 0; 0; Model 8 normal; -116
- 周辺文脈（EN）: The other effects seem to be quite similar as with the previous model, but the day of year effects are clearly different with most days having non-detectable effect. There are also
- 周辺文脈（JA, 自動訳）: 5.1.8 モデル 8+t_nu: スチューデントの事前 t を使用した年間通算日の効果 / 他の効果は前のモデルと非常に似ているように見えますが、年間通算日の効果は明らかに異なり、ほとんどの日に検出できない影響があります。もあります
- Workflowフェーズ: **Posterior summary / effect interpretation**
- 実務での読み方: 推定効果・不確実性・派生量を意思決定に接続する。平均だけでなく区間・分布・実務閾値超過確率を残す。
- MLflow連携: `posterior_draws_uri, model_code_hash, ci_width, decision_threshold_prob`
- 参照: [公式ページ](https://avehtari.github.io/Bayesian-Workflow/birthdays/birthdays.html#tinytable_uvwyjbx7ypxwfslrr5hk) / [ソース候補](https://github.com/avehtari/Bayesian-Workflow/blob/eb00fa4397314ef7d90203382542bd44c590e289/birthdays/birthdays.R)

#### `birthdays-birthdays/tinytable_skwcgik6pubsv29kfhuu`

- 種別: `table` / 公式ID: `tinytable_skwcgik6pubsv29kfhuu` / ページ内順序: 43
- caption/列: variable; mean; median; sd; mad; q5; q95; rhat
- 周辺文脈（EN）: Check whether parameters have reasonable values
- 周辺文脈（JA, 自動訳）: 5.1.9 モデル 8+RHS: RHS 以前の日付の影響 / パラメータが妥当な値であるかどうかを確認する
- Workflowフェーズ: **Posterior summary / effect interpretation**
- 実務での読み方: 推定効果・不確実性・派生量を意思決定に接続する。平均だけでなく区間・分布・実務閾値超過確率を残す。
- MLflow連携: `posterior_draws_uri, model_code_hash, ci_width, decision_threshold_prob`
- 参照: [公式ページ](https://avehtari.github.io/Bayesian-Workflow/birthdays/birthdays.html#tinytable_skwcgik6pubsv29kfhuu) / [ソース候補](https://github.com/avehtari/Bayesian-Workflow/blob/eb00fa4397314ef7d90203382542bd44c590e289/birthdays/birthdays.R)

#### `birthdays-birthdays/tinytable_7g5fulh24r4j4vbn9osf`

- 種別: `table` / 公式ID: `tinytable_7g5fulh24r4j4vbn9osf` / ページ内順序: 44
- caption/列: model; elpd_diff; se_diff; Model 8 RHS; 0; 0; Model 8 Student's t; -0.21
- 周辺文脈（EN）: Visually we get quite similar result as with t_\nu prior. When we compare the models with LOO-CV ( Vehtari, Gelman, and Gabry 2017 ) , RHS prior is better.
- 周辺文脈（JA, 自動訳）: 5.1.9 モデル 8+RHS: RHS 以前の日付の影響 / 視覚的には、以前の t_\nu の場合と非常に似た結果が得られます。 LOO-CV (Vehtari, Gelman, and Gabry 2017) とモデルを比較すると、RHS 以前の方が優れています。
- Workflowフェーズ: **Posterior summary / effect interpretation**
- 実務での読み方: 推定効果・不確実性・派生量を意思決定に接続する。平均だけでなく区間・分布・実務閾値超過確率を残す。
- MLflow連携: `posterior_draws_uri, model_code_hash, ci_width, decision_threshold_prob`
- 参照: [公式ページ](https://avehtari.github.io/Bayesian-Workflow/birthdays/birthdays.html#tinytable_7g5fulh24r4j4vbn9osf) / [ソース候補](https://github.com/avehtari/Bayesian-Workflow/blob/eb00fa4397314ef7d90203382542bd44c590e289/birthdays/birthdays.R)

#### `birthdays-birthdays/tinytable_natfkao54hmo7wga3fzf`

- 種別: `table` / 公式ID: `tinytable_natfkao54hmo7wga3fzf` / ページ内順序: 45
- caption/列: model; elpd_diff; se_diff; Model 8 + RHS; 0; 0; Model 7; -960
- 周辺文脈（EN）: We didn’t use LOO-CV ( Vehtari, Gelman, and Gabry 2017 ) until in the end, as the qualitative differences between models were very convincing. We can use LOO-CV to check how big th
- 周辺文脈（JA, 自動訳）: 5.1.11 一連のモデルの定量的予測パフォーマンス / モデル間の定性的な違いが非常に説得力があったため、最終的に LOO-CV (Vehtari, Gelman, and Gabry 2017) を使用しませんでした。 LOO-CV を使用して、どのくらいの大きさかを確認できます。
- Workflowフェーズ: **LOO-CV / model comparison**
- 実務での読み方: elpd差だけでなくSEとPareto-kを読み、勝敗より『どのデータ点で負けるか』を確認する。
- MLflow連携: `loo_elpd, loo_elpd_diff, loo_se_diff, pareto_k_gt_0_7, reloo_count`
- 参照: [公式ページ](https://avehtari.github.io/Bayesian-Workflow/birthdays/birthdays.html#tinytable_natfkao54hmo7wga3fzf) / [ソース候補](https://github.com/avehtari/Bayesian-Workflow/blob/eb00fa4397314ef7d90203382542bd44c590e289/birthdays/birthdays.R)

#### `birthdays-birthdays/tinytable_6jw88k2u4n41xg8g20ko`

- 種別: `table` / 公式ID: `tinytable_6jw88k2u4n41xg8g20ko` / ページ内順序: 46
- caption/列: Model; LOO.R2; Model 8 Student's t; 0.94
- 周辺文脈（EN）: The best model so far explains already 95% of the variance (LOO-R2).
- 周辺文脈（JA, 自動訳）: 5.1.12 残差分析 / これまでの最良のモデルはすでに分散の 95% を説明しています (LOO-R2)。
- Workflowフェーズ: **LOO-CV / model comparison**
- 実務での読み方: elpd差だけでなくSEとPareto-kを読み、勝敗より『どのデータ点で負けるか』を確認する。
- MLflow連携: `loo_elpd, loo_elpd_diff, loo_se_diff, pareto_k_gt_0_7, reloo_count`
- 参照: [公式ページ](https://avehtari.github.io/Bayesian-Workflow/birthdays/birthdays.html#tinytable_6jw88k2u4n41xg8g20ko) / [ソース候補](https://github.com/avehtari/Bayesian-Workflow/blob/eb00fa4397314ef7d90203382542bd44c590e289/birthdays/birthdays.R)

### Models for regression coefficients and variable selection: Student grades

- ページ: <https://avehtari.github.io/Bayesian-Workflow/variable_selection/variable_selection.html>
- ソース候補: <https://github.com/avehtari/Bayesian-Workflow/blob/eb00fa4397314ef7d90203382542bd44c590e289/variable_selection/variable_selection.R>

#### `variable-selection-variable-selection/fig-data-histograms`

- 種別: `figure` / 公式ID: `fig-data-histograms` / ページ内順序: 1
- caption/列: Figure 1
- 周辺文脈（EN）: The following plot shows the distributions of median math and Portuguese exam scores for each student.
- 周辺文脈（JA, 自動訳）: 3 データ / 次のプロットは、各生徒の数学とポルトガル語の試験得点の中央値の分布を示しています。
- Workflowフェーズ: **EDA / observed data**
- 実務での読み方: モデル化前に、観測単位・外れ値・欠測・群構造・時系列性・上限/下限などを確認する。MLflowではデータ版と前処理版を固定する。
- MLflow連携: `dataset_uri, dataset_hash, preprocessing_version, n_obs, group_count`
- 参照: [公式ページ](https://avehtari.github.io/Bayesian-Workflow/variable_selection/variable_selection.html#fig-data-histograms) / [ソース候補](https://github.com/avehtari/Bayesian-Workflow/blob/eb00fa4397314ef7d90203382542bd44c590e289/variable_selection/variable_selection.R)

#### `variable-selection-variable-selection/fig-fitmu-mcmc_areas`

- 種別: `figure` / 公式ID: `fig-fitmu-mcmc_areas` / ページ内順序: 2
- caption/列: Figure 2
- 周辺文脈（EN）: We plot the marginal posteriors for coefficients. For many coefficients the posterior is quite wide.
- 周辺文脈（JA, 自動訳）: 4 係数に対するデフォルトの一様事前分布 / 係数の周辺事後分布をプロットします。多くの係数では事後係数が非常に広いです。
- Workflowフェーズ: **Posterior summary / effect interpretation**
- 実務での読み方: 推定効果・不確実性・派生量を意思決定に接続する。平均だけでなく区間・分布・実務閾値超過確率を残す。
- MLflow連携: `posterior_draws_uri, model_code_hash, ci_width, decision_threshold_prob`
- 参照: [公式ページ](https://avehtari.github.io/Bayesian-Workflow/variable_selection/variable_selection.html#fig-fitmu-mcmc_areas) / [ソース候補](https://github.com/avehtari/Bayesian-Workflow/blob/eb00fa4397314ef7d90203382542bd44c590e289/variable_selection/variable_selection.R)

#### `variable-selection-variable-selection/fig-implied-R2-prior-posterior-loo-html-1`

- 種別: `figure` / 公式ID: `fig-implied-R2-prior-posterior-loo-html-1` / ページ内順序: 3
- caption/列: Figure 3
- 周辺文脈（EN）: R2D2 prior, which has the benefit that it first defines the prior directly on R^2 , and then the prior is propagated to the coefficients. The R2D2 prior is predictively consistent,
- 周辺文脈（JA, 自動訳）: 6 R^2 および R2D2 事前 / R2D2 事前の暗黙の事前確率。これには、最初に R^2 で事前事前確率を直接定義し、次に事前確率が係数に伝播されるという利点があります。 R2D2 事前分布は予測的に一貫しています。
- Workflowフェーズ: **Posterior summary / effect interpretation**
- 実務での読み方: 推定効果・不確実性・派生量を意思決定に接続する。平均だけでなく区間・分布・実務閾値超過確率を残す。
- MLflow連携: `posterior_draws_uri, model_code_hash, ci_width, decision_threshold_prob`
- 参照: [公式ページ](https://avehtari.github.io/Bayesian-Workflow/variable_selection/variable_selection.html#fig-implied-R2-prior-posterior-loo-html-1) / [ソース候補](https://github.com/avehtari/Bayesian-Workflow/blob/eb00fa4397314ef7d90203382542bd44c590e289/variable_selection/variable_selection.R)

#### `variable-selection-variable-selection/fig-implied-R2-prior-posterior-loo-html-2`

- 種別: `figure` / 公式ID: `fig-implied-R2-prior-posterior-loo-html-2` / ページ内順序: 4
- caption/列: Figure 4
- 周辺文脈（EN）: R2D2 prior, which has the benefit that it first defines the prior directly on R^2 , and then the prior is propagated to the coefficients. The R2D2 prior is predictively consistent,
- 周辺文脈（JA, 自動訳）: 6 R^2 および R2D2 事前 / R2D2 事前の暗黙の事前確率。これには、最初に R^2 で事前事前確率を直接定義し、次に事前確率が係数に伝播されるという利点があります。 R2D2 事前分布は予測的に一貫しています。
- Workflowフェーズ: **Posterior summary / effect interpretation**
- 実務での読み方: 推定効果・不確実性・派生量を意思決定に接続する。平均だけでなく区間・分布・実務閾値超過確率を残す。
- MLflow連携: `posterior_draws_uri, model_code_hash, ci_width, decision_threshold_prob`
- 参照: [公式ページ](https://avehtari.github.io/Bayesian-Workflow/variable_selection/variable_selection.html#fig-implied-R2-prior-posterior-loo-html-2) / [ソース候補](https://github.com/avehtari/Bayesian-Workflow/blob/eb00fa4397314ef7d90203382542bd44c590e289/variable_selection/variable_selection.R)

#### `variable-selection-variable-selection/fig-implied-R2-prior-posterior-loo-html-3`

- 種別: `figure` / 公式ID: `fig-implied-R2-prior-posterior-loo-html-3` / ページ内順序: 5
- caption/列: Figure 5
- 周辺文脈（EN）: R2D2 prior, which has the benefit that it first defines the prior directly on R^2 , and then the prior is propagated to the coefficients. The R2D2 prior is predictively consistent,
- 周辺文脈（JA, 自動訳）: 6 R^2 および R2D2 事前 / R2D2 事前の暗黙の事前確率。これには、最初に R^2 で事前事前確率を直接定義し、次に事前確率が係数に伝播されるという利点があります。 R2D2 事前分布は予測的に一貫しています。
- Workflowフェーズ: **Posterior summary / effect interpretation**
- 実務での読み方: 推定効果・不確実性・派生量を意思決定に接続する。平均だけでなく区間・分布・実務閾値超過確率を残す。
- MLflow連携: `posterior_draws_uri, model_code_hash, ci_width, decision_threshold_prob`
- 参照: [公式ページ](https://avehtari.github.io/Bayesian-Workflow/variable_selection/variable_selection.html#fig-implied-R2-prior-posterior-loo-html-3) / [ソース候補](https://github.com/avehtari/Bayesian-Workflow/blob/eb00fa4397314ef7d90203382542bd44c590e289/variable_selection/variable_selection.R)

#### `variable-selection-variable-selection/fig-implied-R2-prior-posterior-loo-html-4`

- 種別: `figure` / 公式ID: `fig-implied-R2-prior-posterior-loo-html-4` / ページ内順序: 6
- caption/列: Figure 6
- 周辺文脈（EN）: R2D2 prior, which has the benefit that it first defines the prior directly on R^2 , and then the prior is propagated to the coefficients. The R2D2 prior is predictively consistent,
- 周辺文脈（JA, 自動訳）: 6 R^2 および R2D2 事前 / R2D2 事前の暗黙の事前確率。これには、最初に R^2 で事前事前確率を直接定義し、次に事前確率が係数に伝播されるという利点があります。 R2D2 事前分布は予測的に一貫しています。
- Workflowフェーズ: **Posterior summary / effect interpretation**
- 実務での読み方: 推定効果・不確実性・派生量を意思決定に接続する。平均だけでなく区間・分布・実務閾値超過確率を残す。
- MLflow連携: `posterior_draws_uri, model_code_hash, ci_width, decision_threshold_prob`
- 参照: [公式ページ](https://avehtari.github.io/Bayesian-Workflow/variable_selection/variable_selection.html#fig-implied-R2-prior-posterior-loo-html-4) / [ソース候補](https://github.com/avehtari/Bayesian-Workflow/blob/eb00fa4397314ef7d90203382542bd44c590e289/variable_selection/variable_selection.R)

#### `variable-selection-variable-selection/fig-fitm-mcmc_areas`

- 種別: `figure` / 公式ID: `fig-fitm-mcmc_areas` / ページ内順序: 7
- caption/列: Figure 7
- 周辺文脈（EN）: We plot the marginal posteriors for coefficients for the model with R2D2 prior. For many coefficients the posterior has been shrunk close to 0. Some marginal posteriors are wide.
- 周辺文脈（JA, 自動訳）: 7 係数の周辺事後分布 / R2D2 を事前に使用したモデルの係数の周辺事後分布をプロットします。多くの係数について、事後分布は 0 近くまで縮小されています。一部の周辺事後分布は幅が広くなります。
- Workflowフェーズ: **Posterior summary / effect interpretation**
- 実務での読み方: 推定効果・不確実性・派生量を意思決定に接続する。平均だけでなく区間・分布・実務閾値超過確率を残す。
- MLflow連携: `posterior_draws_uri, model_code_hash, ci_width, decision_threshold_prob`
- 参照: [公式ページ](https://avehtari.github.io/Bayesian-Workflow/variable_selection/variable_selection.html#fig-fitm-mcmc_areas) / [ソース候補](https://github.com/avehtari/Bayesian-Workflow/blob/eb00fa4397314ef7d90203382542bd44c590e289/variable_selection/variable_selection.R)

#### `variable-selection-variable-selection/fig-fitm-mcmc_scatter-Fedu-Medu`

- 種別: `figure` / 公式ID: `fig-fitm-mcmc_scatter-Fedu-Medu` / ページ内順序: 8
- caption/列: Figure 8
- 周辺文脈（EN）: We check the bivariate marginal for Fedu and Medu coefficients, and see that while the univariate marginals overlap with 0, jointly there is not much posterior mass near 0. This is
- 周辺文脈（JA, 自動訳）: 7 係数の周辺事後分布 / Fedu 係数と Medu 係数の 2 変量周辺分布をチェックすると、単変量周辺分布が 0 と重なっている一方で、0 付近の事後質量はそれほど多くないことがわかります。これは次のとおりです。
- Workflowフェーズ: **Posterior summary / effect interpretation**
- 実務での読み方: 推定効果・不確実性・派生量を意思決定に接続する。平均だけでなく区間・分布・実務閾値超過確率を残す。
- MLflow連携: `posterior_draws_uri, model_code_hash, ci_width, decision_threshold_prob`
- 参照: [公式ページ](https://avehtari.github.io/Bayesian-Workflow/variable_selection/variable_selection.html#fig-fitm-mcmc_scatter-Fedu-Medu) / [ソース候補](https://github.com/avehtari/Bayesian-Workflow/blob/eb00fa4397314ef7d90203382542bd44c590e289/variable_selection/variable_selection.R)

#### `variable-selection-variable-selection/fig-fitm-ppc-hist`

- 種別: `figure` / 公式ID: `fig-fitm-ppc-hist` / ページ内順序: 9
- caption/列: Figure 9
- 周辺文脈（EN）: We’re using a normal observation model, although we know that the exam scores are in a bounded range. The posterior predictive checking shows that we sometimes predict exam scores
- 周辺文脈（JA, 自動訳）: 8 モデルのチェック / 試験のスコアが制限された範囲内にあることはわかっていますが、通常の観察モデルを使用しています。事後予測チェックは、私たちが試験の得点を予測することがあることを示しています
- Workflowフェーズ: **Posterior predictive checking / calibration**
- 実務での読み方: モデルが再現すべき特徴を外していないか確認する。PPC統計量と図をartifact化し、モデル改善の根拠にする。
- MLflow連携: `ppc_stat_*, loo_pit_ecdf_maxdev, calibration_error, replicated_seed`
- 参照: [公式ページ](https://avehtari.github.io/Bayesian-Workflow/variable_selection/variable_selection.html#fig-fitm-ppc-hist) / [ソース候補](https://github.com/avehtari/Bayesian-Workflow/blob/eb00fa4397314ef7d90203382542bd44c590e289/variable_selection/variable_selection.R)

#### `variable-selection-variable-selection/fig-fitm-ppc_loo_pit`

- 種別: `figure` / 公式ID: `fig-fitm-ppc_loo_pit` / ページ内順序: 10
- caption/列: Figure 10
- 周辺文脈（EN）: LOO-PIT-ECDF plots shows that otherwise the normal model is quite well calibrated.
- 周辺文脈（JA, 自動訳）: 8 モデル チェック / LOO-PIT-ECDF プロットは、それ以外の点では通常のモデルが非常に適切に校正されていることを示しています。
- Workflowフェーズ: **Posterior predictive checking / calibration**
- 実務での読み方: モデルが再現すべき特徴を外していないか確認する。PPC統計量と図をartifact化し、モデル改善の根拠にする。
- MLflow連携: `ppc_stat_*, loo_pit_ecdf_maxdev, calibration_error, replicated_seed`
- 参照: [公式ページ](https://avehtari.github.io/Bayesian-Workflow/variable_selection/variable_selection.html#fig-fitm-ppc_loo_pit) / [ソース候補](https://github.com/avehtari/Bayesian-Workflow/blob/eb00fa4397314ef7d90203382542bd44c590e289/variable_selection/variable_selection.R)

#### `variable-selection-variable-selection/fig-vselm_fast`

- 種別: `figure` / 公式ID: `fig-vselm_fast` / ページ内順序: 11
- caption/列: Figure 11
- 周辺文脈（EN）: The following plot shows the relevance order of the predictors and estimated predictive performance given those variables. As the search can overfit and we didn’t cross-validate th
- 周辺文脈（JA, 自動訳）: 9.1 数学試験のスコア / 次のプロットは、予測子の関連性の順序と、それらの変数を考慮した推定予測パフォーマンスを示しています。検索は過剰適合する可能性があり、相互検証は行っていないため、
- Workflowフェーズ: **MCMC / computation diagnostics**
- 実務での読み方: 推論結果を解釈する前に、R-hat、ESS、divergence、treedepth、BFMI、trace/pairsを確認する。悪いrunは比較表から除外せず失敗として記録する。
- MLflow連携: `rhat_max, ess_bulk_min, ess_tail_min, divergences, treedepth_hits, bfmi_min`
- 参照: [公式ページ](https://avehtari.github.io/Bayesian-Workflow/variable_selection/variable_selection.html#fig-vselm_fast) / [ソース候補](https://github.com/avehtari/Bayesian-Workflow/blob/eb00fa4397314ef7d90203382542bd44c590e289/variable_selection/variable_selection.R)

#### `variable-selection-variable-selection/fig-vselm`

- 種別: `figure` / 公式ID: `fig-vselm` / ページ内順序: 12
- caption/列: Figure 12
- 周辺文脈（EN）: The following plot shows the relevance order of the predictors and estimated predictive performance given those variables. The order is the same as in the previous plot, but now th
- 周辺文脈（JA, 自動訳）: 9.1 数学試験のスコア / 次のプロットは、予測子の関連性の順序と、それらの変数を考慮した推定予測パフォーマンスを示しています。順序は前のプロットと同じですが、
- Workflowフェーズ: **MCMC / computation diagnostics**
- 実務での読み方: 推論結果を解釈する前に、R-hat、ESS、divergence、treedepth、BFMI、trace/pairsを確認する。悪いrunは比較表から除外せず失敗として記録する。
- MLflow連携: `rhat_max, ess_bulk_min, ess_tail_min, divergences, treedepth_hits, bfmi_min`
- 参照: [公式ページ](https://avehtari.github.io/Bayesian-Workflow/variable_selection/variable_selection.html#fig-vselm) / [ソース候補](https://github.com/avehtari/Bayesian-Workflow/blob/eb00fa4397314ef7d90203382542bd44c590e289/variable_selection/variable_selection.R)

#### `variable-selection-variable-selection/fig-fitm-proj-mcmc_areas`

- 種別: `figure` / 公式ID: `fig-fitm-proj-mcmc_areas` / ページ内順序: 13
- caption/列: Figure 13
- 周辺文脈（EN）: The marginals of the projected posterior are all clearly away from 0.
- 周辺文脈（JA, 自動訳）: 9.1 数学の試験の得点 / 投影された事後分布の境界はすべて明らかに 0 から離れています。
- Workflowフェーズ: **Posterior summary / effect interpretation**
- 実務での読み方: 推定効果・不確実性・派生量を意思決定に接続する。平均だけでなく区間・分布・実務閾値超過確率を残す。
- MLflow連携: `posterior_draws_uri, model_code_hash, ci_width, decision_threshold_prob`
- 参照: [公式ページ](https://avehtari.github.io/Bayesian-Workflow/variable_selection/variable_selection.html#fig-fitm-proj-mcmc_areas) / [ソース候補](https://github.com/avehtari/Bayesian-Workflow/blob/eb00fa4397314ef7d90203382542bd44c590e289/variable_selection/variable_selection.R)

#### `variable-selection-variable-selection/fig-vselm-cv_proportions`

- 種別: `figure` / 公式ID: `fig-vselm-cv_proportions` / ページ内順序: 14
- caption/列: Figure 14
- 周辺文脈（EN）: The following plot shows the stability of the search over the different LOO-CV folds. The numbers indicate the proportion of folds, the specific predictor was included at latest on
- 周辺文脈（JA, 自動訳）: 9.1 数学試験のスコア / 次のプロットは、さまざまな LOO-CV フォールドにわたる検索の安定性を示しています。数字はフォールドの割合を示しており、特定の予測因子は遅くとも含まれています。
- Workflowフェーズ: **MCMC / computation diagnostics**
- 実務での読み方: 推論結果を解釈する前に、R-hat、ESS、divergence、treedepth、BFMI、trace/pairsを確認する。悪いrunは比較表から除外せず失敗として記録する。
- MLflow連携: `rhat_max, ess_bulk_min, ess_tail_min, divergences, treedepth_hits, bfmi_min`
- 参照: [公式ページ](https://avehtari.github.io/Bayesian-Workflow/variable_selection/variable_selection.html#fig-vselm-cv_proportions) / [ソース候補](https://github.com/avehtari/Bayesian-Workflow/blob/eb00fa4397314ef7d90203382542bd44c590e289/variable_selection/variable_selection.R)

#### `variable-selection-variable-selection/fig-fitp-mcmc_areas`

- 種別: `figure` / 公式ID: `fig-fitp-mcmc_areas` / ページ内順序: 15
- caption/列: Figure 15
- 周辺文脈（EN）: Plot marginal posteriors of coefficients
- 周辺文脈（JA, 自動訳）: 9.2 ポルトガル語試験のスコア / 係数の周辺事後プロット
- Workflowフェーズ: **Posterior summary / effect interpretation**
- 実務での読み方: 推定効果・不確実性・派生量を意思決定に接続する。平均だけでなく区間・分布・実務閾値超過確率を残す。
- MLflow連携: `posterior_draws_uri, model_code_hash, ci_width, decision_threshold_prob`
- 参照: [公式ページ](https://avehtari.github.io/Bayesian-Workflow/variable_selection/variable_selection.html#fig-fitp-mcmc_areas) / [ソース候補](https://github.com/avehtari/Bayesian-Workflow/blob/eb00fa4397314ef7d90203382542bd44c590e289/variable_selection/variable_selection.R)

#### `variable-selection-variable-selection/fig-vselp_fast`

- 種別: `figure` / 公式ID: `fig-vselp_fast` / ページ内順序: 16
- caption/列: Figure 16
- 周辺文脈（EN）: The following plot shows the relevance order of the predictors and estimated predictive performance given those variables. As there is some overfitting in the search and we didn’t
- 周辺文脈（JA, 自動訳）: 9.2 ポルトガル語試験のスコア / 次のプロットは、予測子の関連性の順序と、これらの変数を考慮した推定予測パフォーマンスを示しています。検索には過剰適合があり、実際にはそうではなかったので、
- Workflowフェーズ: **MCMC / computation diagnostics**
- 実務での読み方: 推論結果を解釈する前に、R-hat、ESS、divergence、treedepth、BFMI、trace/pairsを確認する。悪いrunは比較表から除外せず失敗として記録する。
- MLflow連携: `rhat_max, ess_bulk_min, ess_tail_min, divergences, treedepth_hits, bfmi_min`
- 参照: [公式ページ](https://avehtari.github.io/Bayesian-Workflow/variable_selection/variable_selection.html#fig-vselp_fast) / [ソース候補](https://github.com/avehtari/Bayesian-Workflow/blob/eb00fa4397314ef7d90203382542bd44c590e289/variable_selection/variable_selection.R)

#### `variable-selection-variable-selection/fig-vselp`

- 種別: `figure` / 公式ID: `fig-vselp` / ページ内順序: 17
- caption/列: Figure 17
- 周辺文脈（EN）: The following plot shows the relevance order of the predictors and estimated predictive performance given those variables. The order is the same as in the previous plot, but now th
- 周辺文脈（JA, 自動訳）: 9.2 ポルトガル語試験のスコア / 次のプロットは、予測子の関連性の順序と、これらの変数を考慮した推定予測パフォーマンスを示しています。順序は前のプロットと同じですが、
- Workflowフェーズ: **MCMC / computation diagnostics**
- 実務での読み方: 推論結果を解釈する前に、R-hat、ESS、divergence、treedepth、BFMI、trace/pairsを確認する。悪いrunは比較表から除外せず失敗として記録する。
- MLflow連携: `rhat_max, ess_bulk_min, ess_tail_min, divergences, treedepth_hits, bfmi_min`
- 参照: [公式ページ](https://avehtari.github.io/Bayesian-Workflow/variable_selection/variable_selection.html#fig-vselp) / [ソース候補](https://github.com/avehtari/Bayesian-Workflow/blob/eb00fa4397314ef7d90203382542bd44c590e289/variable_selection/variable_selection.R)

#### `variable-selection-variable-selection/fig-fitp-proj-mcmc_areas`

- 種別: `figure` / 公式ID: `fig-fitp-proj-mcmc_areas` / ページ内順序: 18
- caption/列: Figure 18
- 周辺文脈（EN）: The marginals of the projected posterior are all clearly away from 0.
- 周辺文脈（JA, 自動訳）: 9.2 ポルトガル語試験のスコア / 投影された事後分布の境界はすべて明らかに 0 から離れています。
- Workflowフェーズ: **Posterior summary / effect interpretation**
- 実務での読み方: 推定効果・不確実性・派生量を意思決定に接続する。平均だけでなく区間・分布・実務閾値超過確率を残す。
- MLflow連携: `posterior_draws_uri, model_code_hash, ci_width, decision_threshold_prob`
- 参照: [公式ページ](https://avehtari.github.io/Bayesian-Workflow/variable_selection/variable_selection.html#fig-fitp-proj-mcmc_areas) / [ソース候補](https://github.com/avehtari/Bayesian-Workflow/blob/eb00fa4397314ef7d90203382542bd44c590e289/variable_selection/variable_selection.R)

#### `variable-selection-variable-selection/fig-vselp-cv_proportions`

- 種別: `figure` / 公式ID: `fig-vselp-cv_proportions` / ページ内順序: 19
- caption/列: Figure 19
- 周辺文脈（EN）: The following plot shows the stability of the search over the different LOO-CV folds. The numbers indicate the proportion of folds, the specific predictor was included at latest on
- 周辺文脈（JA, 自動訳）: 9.2 ポルトガル語試験のスコア / 次のプロットは、さまざまな LOO-CV フォールドにわたる検索の安定性を示しています。数字はフォールドの割合を示しており、特定の予測因子は遅くとも含まれています。
- Workflowフェーズ: **MCMC / computation diagnostics**
- 実務での読み方: 推論結果を解釈する前に、R-hat、ESS、divergence、treedepth、BFMI、trace/pairsを確認する。悪いrunは比較表から除外せず失敗として記録する。
- MLflow連携: `rhat_max, ess_bulk_min, ess_tail_min, divergences, treedepth_hits, bfmi_min`
- 参照: [公式ページ](https://avehtari.github.io/Bayesian-Workflow/variable_selection/variable_selection.html#fig-vselp-cv_proportions) / [ソース候補](https://github.com/avehtari/Bayesian-Workflow/blob/eb00fa4397314ef7d90203382542bd44c590e289/variable_selection/variable_selection.R)

#### `variable-selection-variable-selection/tinytable_q9c8k1fcoar9ie5bb4ui`

- 種別: `table` / 公式ID: `tinytable_q9c8k1fcoar9ie5bb4ui` / ページ内順序: 1
- caption/列: Gmat; school; sex; age; address; famsize; Pstatus; Medu
- 周辺文脈（EN）: The data includes 3 grades for both mathematics and Portuguese. To reduce the variability in the outcome we use median grades based on those three exams for each topic. We select o
- 周辺文脈（JA, 自動訳）: 3 データ / データには数学とポルトガル語の 3 つの成績が含まれています。結果のばらつきを減らすために、各トピックの 3 つの試験に基づいた成績の中央値を使用します。 oを選択します
- Workflowフェーズ: **EDA / observed data**
- 実務での読み方: モデル化前に、観測単位・外れ値・欠測・群構造・時系列性・上限/下限などを確認する。MLflowではデータ版と前処理版を固定する。
- MLflow連携: `dataset_uri, dataset_hash, preprocessing_version, n_obs, group_count`
- 参照: [公式ページ](https://avehtari.github.io/Bayesian-Workflow/variable_selection/variable_selection.html#tinytable_q9c8k1fcoar9ie5bb4ui) / [ソース候補](https://github.com/avehtari/Bayesian-Workflow/blob/eb00fa4397314ef7d90203382542bd44c590e289/variable_selection/variable_selection.R)

#### `variable-selection-variable-selection/tinytable_b8bd8jkpy4urkcxd07fw`

- 種別: `table` / 公式ID: `tinytable_b8bd8jkpy4urkcxd07fw` / ページ内順序: 2
- caption/列: Gpor; school; sex; age; address; famsize; Pstatus; Medu
- 周辺文脈（EN）: The data includes 3 grades for both mathematics and Portuguese. To reduce the variability in the outcome we use median grades based on those three exams for each topic. We select o
- 周辺文脈（JA, 自動訳）: 3 データ / データには数学とポルトガル語の 3 つの成績が含まれています。結果のばらつきを減らすために、各トピックの 3 つの試験に基づいた成績の中央値を使用します。 oを選択します
- Workflowフェーズ: **EDA / observed data**
- 実務での読み方: モデル化前に、観測単位・外れ値・欠測・群構造・時系列性・上限/下限などを確認する。MLflowではデータ版と前処理版を固定する。
- MLflow連携: `dataset_uri, dataset_hash, preprocessing_version, n_obs, group_count`
- 参照: [公式ページ](https://avehtari.github.io/Bayesian-Workflow/variable_selection/variable_selection.html#tinytable_b8bd8jkpy4urkcxd07fw) / [ソース候補](https://github.com/avehtari/Bayesian-Workflow/blob/eb00fa4397314ef7d90203382542bd44c590e289/variable_selection/variable_selection.R)

#### `variable-selection-variable-selection/tinytable_duyf57ucs2mv796opazf`

- 種別: `table` / 公式ID: `tinytable_duyf57ucs2mv796opazf` / ページ内順序: 3
- caption/列: Estimate; Est.Error; Q2.5; Q97.5; 0.3; 0.033; 0.24; 0.37
- 周辺文脈（EN）: We first re-define bayes_R2() to match the paper.
- 周辺文脈（JA, 自動訳）: 4 デフォルトの均一事前係数 / まず、論文に一致するように Bayes_R2() を再定義します。
- Workflowフェーズ: **MCMC / computation diagnostics**
- 実務での読み方: 推論結果を解釈する前に、R-hat、ESS、divergence、treedepth、BFMI、trace/pairsを確認する。悪いrunは比較表から除外せず失敗として記録する。
- MLflow連携: `rhat_max, ess_bulk_min, ess_tail_min, divergences, treedepth_hits, bfmi_min`
- 参照: [公式ページ](https://avehtari.github.io/Bayesian-Workflow/variable_selection/variable_selection.html#tinytable_duyf57ucs2mv796opazf) / [ソース候補](https://github.com/avehtari/Bayesian-Workflow/blob/eb00fa4397314ef7d90203382542bd44c590e289/variable_selection/variable_selection.R)

#### `variable-selection-variable-selection/tinytable_ltl885dk7az1xfsr2by4`

- 種別: `table` / 公式ID: `tinytable_ltl885dk7az1xfsr2by4` / ページ内順序: 4
- caption/列: Estimate; Est.Error; Q2.5; Q97.5; 0.18; 0.04; 0.1; 0.26
- 周辺文脈（EN）: We first re-define bayes_R2() to match the paper.
- 周辺文脈（JA, 自動訳）: 4 デフォルトの均一事前係数 / まず、論文に一致するように Bayes_R2() を再定義します。
- Workflowフェーズ: **MCMC / computation diagnostics**
- 実務での読み方: 推論結果を解釈する前に、R-hat、ESS、divergence、treedepth、BFMI、trace/pairsを確認する。悪いrunは比較表から除外せず失敗として記録する。
- MLflow連携: `rhat_max, ess_bulk_min, ess_tail_min, divergences, treedepth_hits, bfmi_min`
- 参照: [公式ページ](https://avehtari.github.io/Bayesian-Workflow/variable_selection/variable_selection.html#tinytable_ltl885dk7az1xfsr2by4) / [ソース候補](https://github.com/avehtari/Bayesian-Workflow/blob/eb00fa4397314ef7d90203382542bd44c590e289/variable_selection/variable_selection.R)

### Sampling problems with latent variables: No vehicles in the park

- ページ: <https://avehtari.github.io/Bayesian-Workflow/park_rule/park_rule.html>
- ソース候補: <https://github.com/avehtari/Bayesian-Workflow/blob/eb00fa4397314ef7d90203382542bd44c590e289/park_rule/park_rule.R>

#### `park-rule-park-rule/fig-park-lme4-1`

- 種別: `figure` / 公式ID: `fig-park-lme4-1` / ページ内順序: 1
- caption/列: Figure 1
- 周辺文脈（EN）: Check with simulated data that inference works.
- 周辺文脈（JA, 自動訳）: 3.3 プロット / 推論が機能することをシミュレートされたデータで確認します。
- Workflowフェーズ: **EDA / observed data**
- 実務での読み方: モデル化前に、観測単位・外れ値・欠測・群構造・時系列性・上限/下限などを確認する。MLflowではデータ版と前処理版を固定する。
- MLflow連携: `dataset_uri, dataset_hash, preprocessing_version, n_obs, group_count`
- 参照: [公式ページ](https://avehtari.github.io/Bayesian-Workflow/park_rule/park_rule.html#fig-park-lme4-1) / [ソース候補](https://github.com/avehtari/Bayesian-Workflow/blob/eb00fa4397314ef7d90203382542bd44c590e289/park_rule/park_rule.R)

#### `park-rule-park-rule/fig-park-lme4-2`

- 種別: `figure` / 公式ID: `fig-park-lme4-2` / ページ内順序: 2
- caption/列: Figure 2
- 周辺文脈（EN）: Check with simulated data that inference works.
- 周辺文脈（JA, 自動訳）: 3.3 プロット / 推論が機能することをシミュレートされたデータで確認します。
- Workflowフェーズ: **EDA / observed data**
- 実務での読み方: モデル化前に、観測単位・外れ値・欠測・群構造・時系列性・上限/下限などを確認する。MLflowではデータ版と前処理版を固定する。
- MLflow連携: `dataset_uri, dataset_hash, preprocessing_version, n_obs, group_count`
- 参照: [公式ページ](https://avehtari.github.io/Bayesian-Workflow/park_rule/park_rule.html#fig-park-lme4-2) / [ソース候補](https://github.com/avehtari/Bayesian-Workflow/blob/eb00fa4397314ef7d90203382542bd44c590e289/park_rule/park_rule.R)

#### `park-rule-park-rule/fig-park-lme4-3`

- 種別: `figure` / 公式ID: `fig-park-lme4-3` / ページ内順序: 3
- caption/列: Figure 3
- 周辺文脈（EN）: Check with simulated data that inference works.
- 周辺文脈（JA, 自動訳）: 3.3 プロット / 推論が機能することをシミュレートされたデータで確認します。
- Workflowフェーズ: **EDA / observed data**
- 実務での読み方: モデル化前に、観測単位・外れ値・欠測・群構造・時系列性・上限/下限などを確認する。MLflowではデータ版と前処理版を固定する。
- MLflow連携: `dataset_uri, dataset_hash, preprocessing_version, n_obs, group_count`
- 参照: [公式ページ](https://avehtari.github.io/Bayesian-Workflow/park_rule/park_rule.html#fig-park-lme4-3) / [ソース候補](https://github.com/avehtari/Bayesian-Workflow/blob/eb00fa4397314ef7d90203382542bd44c590e289/park_rule/park_rule.R)

#### `park-rule-park-rule/fig-fit_1-trace-a`

- 種別: `figure` / 公式ID: `fig-fit_1-trace-a` / ページ内順序: 4
- caption/列: Figure 4
- 周辺文脈（EN）: We are specifically interested in how efficient each Hamiltonian Monte Carlo iteration is. This can be measured by the number of leapfrog steps n_leapfrog__ , which is close to the
- 周辺文脈（JA, 自動訳）: 4.2 非中心パラメータ化による階層的ロジスティック回帰 / 私たちは、各ハミルトニアン モンテカルロ反復がどの程度効率的であるかに特に興味を持っています。これは、リープフロッグ ステップ数 n_leapfrog__ によって測定できます。これは、
- Workflowフェーズ: **MCMC / computation diagnostics**
- 実務での読み方: 推論結果を解釈する前に、R-hat、ESS、divergence、treedepth、BFMI、trace/pairsを確認する。悪いrunは比較表から除外せず失敗として記録する。
- MLflow連携: `rhat_max, ess_bulk_min, ess_tail_min, divergences, treedepth_hits, bfmi_min`
- 参照: [公式ページ](https://avehtari.github.io/Bayesian-Workflow/park_rule/park_rule.html#fig-fit_1-trace-a) / [ソース候補](https://github.com/avehtari/Bayesian-Workflow/blob/eb00fa4397314ef7d90203382542bd44c590e289/park_rule/park_rule.R)

#### `park-rule-park-rule/fig-fit_1-scatter-a-a_item`

- 種別: `figure` / 公式ID: `fig-fit_1-scatter-a-a_item` / ページ内順序: 5
- caption/列: Figure 5
- 周辺文脈（EN）: We can examine the scatter plot of a and sum of a_item to see the strong correlation.
- 周辺文脈（JA, 自動訳）: 4.2 非中心パラメータ化による階層的ロジスティック回帰 / a の散布図と a_item の合計を調べて、強い相関関係を確認できます。
- Workflowフェーズ: **MCMC / computation diagnostics**
- 実務での読み方: 推論結果を解釈する前に、R-hat、ESS、divergence、treedepth、BFMI、trace/pairsを確認する。悪いrunは比較表から除外せず失敗として記録する。
- MLflow連携: `rhat_max, ess_bulk_min, ess_tail_min, divergences, treedepth_hits, bfmi_min`
- 参照: [公式ページ](https://avehtari.github.io/Bayesian-Workflow/park_rule/park_rule.html#fig-fit_1-scatter-a-a_item) / [ソース候補](https://github.com/avehtari/Bayesian-Workflow/blob/eb00fa4397314ef7d90203382542bd44c590e289/park_rule/park_rule.R)

#### `park-rule-park-rule/fig-fit_2-scatter-a_item-sigma_item`

- 種別: `figure` / 公式ID: `fig-fit_2-scatter-a_item-sigma_item` / ページ内順序: 6
- caption/列: Figure 6
- 周辺文脈（EN）: The usual way to investigate funnels in hierarchical models, is to look at the scatter plot of one of the variables and corresponding prior scale. We examine a_item and sigma_item
- 周辺文脈（JA, 自動訳）: 4.3 ゼロ和のパラメータ化による階層ロジスティック回帰 / 階層モデルでファネルを調査する通常の方法は、変数の 1 つと対応する事前スケールの散布図を調べることです。 a_item と sigma_item を調べます
- Workflowフェーズ: **MCMC / computation diagnostics**
- 実務での読み方: 推論結果を解釈する前に、R-hat、ESS、divergence、treedepth、BFMI、trace/pairsを確認する。悪いrunは比較表から除外せず失敗として記録する。
- MLflow連携: `rhat_max, ess_bulk_min, ess_tail_min, divergences, treedepth_hits, bfmi_min`
- 参照: [公式ページ](https://avehtari.github.io/Bayesian-Workflow/park_rule/park_rule.html#fig-fit_2-scatter-a_item-sigma_item) / [ソース候補](https://github.com/avehtari/Bayesian-Workflow/blob/eb00fa4397314ef7d90203382542bd44c590e289/park_rule/park_rule.R)

#### `park-rule-park-rule/fig-fit_2-scatter-z_item-sigma_item`

- 種別: `figure` / 公式ID: `fig-fit_2-scatter-z_item-sigma_item` / ページ内順序: 7
- caption/列: Figure 7
- 周辺文脈（EN）: Now \widehat{R} and ESSs indicate problems with z_item . We examine the scatter plot for z_item[1] and sigma_item :
- 周辺文脈（JA, 自動訳）: 4.3 ゼロ和のパラメータ化を使用した階層型ロジスティック回帰 / \widehat{R} と ESS は z_item の問題を示しています。 z_item[1] と sigma_item の散布図を調べます。
- Workflowフェーズ: **MCMC / computation diagnostics**
- 実務での読み方: 推論結果を解釈する前に、R-hat、ESS、divergence、treedepth、BFMI、trace/pairsを確認する。悪いrunは比較表から除外せず失敗として記録する。
- MLflow連携: `rhat_max, ess_bulk_min, ess_tail_min, divergences, treedepth_hits, bfmi_min`
- 参照: [公式ページ](https://avehtari.github.io/Bayesian-Workflow/park_rule/park_rule.html#fig-fit_2-scatter-z_item-sigma_item) / [ソース候補](https://github.com/avehtari/Bayesian-Workflow/blob/eb00fa4397314ef7d90203382542bd44c590e289/park_rule/park_rule.R)

#### `park-rule-park-rule/fig-fit_2-scatter-z_item-log_sigma_item`

- 種別: `figure` / 公式ID: `fig-fit_2-scatter-z_item-log_sigma_item` / ページ内順序: 8
- caption/列: Figure 8
- 周辺文脈（EN）: There is a strong correlation. There is also slight banana shape, but as sigma_item is constrained to be positive, the sampling is done in log space, and we should use that also fo
- 周辺文脈（JA, 自動訳）: 4.3 ゼロ和のパラメータ化による階層型ロジスティック回帰 / 強い相関関係があります。わずかなバナナの形もありますが、sigma_item が正になるように制約されているため、サンプリングは対数空間で行われ、それを次の目的にも使用する必要があります。
- Workflowフェーズ: **MCMC / computation diagnostics**
- 実務での読み方: 推論結果を解釈する前に、R-hat、ESS、divergence、treedepth、BFMI、trace/pairsを確認する。悪いrunは比較表から除外せず失敗として記録する。
- MLflow連携: `rhat_max, ess_bulk_min, ess_tail_min, divergences, treedepth_hits, bfmi_min`
- 参照: [公式ページ](https://avehtari.github.io/Bayesian-Workflow/park_rule/park_rule.html#fig-fit_2-scatter-z_item-log_sigma_item) / [ソース候補](https://github.com/avehtari/Bayesian-Workflow/blob/eb00fa4397314ef7d90203382542bd44c590e289/park_rule/park_rule.R)

#### `park-rule-park-rule/fig-lme4-vs-stan-a_item`

- 種別: `figure` / 公式ID: `fig-lme4-vs-stan-a_item` / ページ内順序: 9
- caption/列: Figure 9
- 周辺文脈（EN）: We compare the point estimates (conditional mode for lme4, posterior mean for Bayes) and 90% intervals (normal approximation for lme4, central posterior interval for Bayes) for a_i
- 周辺文脈（JA, 自動訳）: 4.6 lme4 とベイズの事後推定値の比較 / a_i の点推定値 (lme4 の条件付きモード、ベイズの事後平均) と 90% 区間 (lme4 の正規近似、ベイズの中心事後区間) を比較します。
- Workflowフェーズ: **Posterior summary / effect interpretation**
- 実務での読み方: 推定効果・不確実性・派生量を意思決定に接続する。平均だけでなく区間・分布・実務閾値超過確率を残す。
- MLflow連携: `posterior_draws_uri, model_code_hash, ci_width, decision_threshold_prob`
- 参照: [公式ページ](https://avehtari.github.io/Bayesian-Workflow/park_rule/park_rule.html#fig-lme4-vs-stan-a_item) / [ソース候補](https://github.com/avehtari/Bayesian-Workflow/blob/eb00fa4397314ef7d90203382542bd44c590e289/park_rule/park_rule.R)

#### `park-rule-park-rule/fig-lme4-vs-stan-a_respondent`

- 種別: `figure` / 公式ID: `fig-lme4-vs-stan-a_respondent` / ページ内順序: 10
- caption/列: Figure 10
- 周辺文脈（EN）: We compare the point estimates (conditional mode for lme4, posterior mean for Bayes) and 90% intervals (normal approximation for lme4, central posterior interval for Bayes) for a_i
- 周辺文脈（JA, 自動訳）: 4.6 lme4 とベイズの事後推定値の比較 / a_i の点推定値 (lme4 の条件付きモード、ベイズの事後平均) と 90% 区間 (lme4 の正規近似、ベイズの中心事後区間) を比較します。
- Workflowフェーズ: **Posterior summary / effect interpretation**
- 実務での読み方: 推定効果・不確実性・派生量を意思決定に接続する。平均だけでなく区間・分布・実務閾値超過確率を残す。
- MLflow連携: `posterior_draws_uri, model_code_hash, ci_width, decision_threshold_prob`
- 参照: [公式ページ](https://avehtari.github.io/Bayesian-Workflow/park_rule/park_rule.html#fig-lme4-vs-stan-a_respondent) / [ソース候補](https://github.com/avehtari/Bayesian-Workflow/blob/eb00fa4397314ef7d90203382542bd44c590e289/park_rule/park_rule.R)

#### `park-rule-park-rule/fig-lme4-vs-stan-sigmas`

- 種別: `figure` / 公式ID: `fig-lme4-vs-stan-sigmas` / ページ内順序: 11
- caption/列: Figure 11
- 周辺文脈（EN）: The wider range of Stan estimates is likely due to effect of integrating over the uncertainty in sigma_item and sigma_respondent :
- 周辺文脈（JA, 自動訳）: 4.6 lme4 とベイジアン事後推定値の比較 / Stan 推定値の範囲が広いのは、おそらく sigma_item と sigma_respondent の不確実性を統合した効果によるものです。
- Workflowフェーズ: **Posterior summary / effect interpretation**
- 実務での読み方: 推定効果・不確実性・派生量を意思決定に接続する。平均だけでなく区間・分布・実務閾値超過確率を残す。
- MLflow連携: `posterior_draws_uri, model_code_hash, ci_width, decision_threshold_prob`
- 参照: [公式ページ](https://avehtari.github.io/Bayesian-Workflow/park_rule/park_rule.html#fig-lme4-vs-stan-sigmas) / [ソース候補](https://github.com/avehtari/Bayesian-Workflow/blob/eb00fa4397314ef7d90203382542bd44c590e289/park_rule/park_rule.R)

### Challenge of multimodality: Differential equation for planetary motion

- ページ: <https://avehtari.github.io/Bayesian-Workflow/planetary_motion/planetary_motion.html>
- ソース候補: <https://github.com/avehtari/Bayesian-Workflow/blob/eb00fa4397314ef7d90203382542bd44c590e289/planetary_motion/planetary_motion.R>

#### `planetary-motion-planetary-motion/fig-sim`

- 種別: `figure` / 公式ID: `fig-sim` / ページ内順序: 1
- caption/列: Figure 1
- 周辺文脈（EN）: The simulation can be done in Stan, using one of its numerical integrators. At t = 0 , q_0 = (1, 0) and p_0 = (0, 1) , and we set k = 1 .
- 周辺文脈（JA, 自動訳）: 2.2 シミュレーション / シミュレーションは、Stan の数値積分器の 1 つを使用して実行できます。 t = 0 、 q_0 = (1, 0) および p_0 = (0, 1) で、 k = 1 と設定します。
- Workflowフェーズ: **MCMC / computation diagnostics**
- 実務での読み方: 推論結果を解釈する前に、R-hat、ESS、divergence、treedepth、BFMI、trace/pairsを確認する。悪いrunは比較表から除外せず失敗として記録する。
- MLflow連携: `rhat_max, ess_bulk_min, ess_tail_min, divergences, treedepth_hits, bfmi_min`
- 参照: [公式ページ](https://avehtari.github.io/Bayesian-Workflow/planetary_motion/planetary_motion.html#fig-sim) / [ソース候補](https://github.com/avehtari/Bayesian-Workflow/blob/eb00fa4397314ef7d90203382542bd44c590e289/planetary_motion/planetary_motion.R)

#### `planetary-motion-planetary-motion/fig-trace`

- 種別: `figure` / 公式ID: `fig-trace` / ページ内順序: 2
- caption/列: Figure 2
- 周辺文脈（EN）: We see that \hat R \gg 1 . Wow, these numbers are dramatic! Clearly the chains are not mixing and we can visualize this using trace plots.
- 周辺文脈（JA, 自動訳）: 3 単純なモデルのフィッティングと推論の診断 / \hat R \gg 1 であることがわかります。うわー、この数字は劇的ですね！明らかにチェーンは混合していないので、トレース プロットを使用してこれを視覚化できます。
- Workflowフェーズ: **MCMC / computation diagnostics**
- 実務での読み方: 推論結果を解釈する前に、R-hat、ESS、divergence、treedepth、BFMI、trace/pairsを確認する。悪いrunは比較表から除外せず失敗として記録する。
- MLflow連携: `rhat_max, ess_bulk_min, ess_tail_min, divergences, treedepth_hits, bfmi_min`
- 参照: [公式ページ](https://avehtari.github.io/Bayesian-Workflow/planetary_motion/planetary_motion.html#fig-trace) / [ソース候補](https://github.com/avehtari/Bayesian-Workflow/blob/eb00fa4397314ef7d90203382542bd44c590e289/planetary_motion/planetary_motion.R)

#### `planetary-motion-planetary-motion/fig-ppc`

- 種別: `figure` / 公式ID: `fig-ppc` / ページ内順序: 3
- caption/列: Figure 3
- 周辺文脈（EN）: Bearing a slight abuse of language, we use “degenerate” to mean that wildly different values of k roughly produce the same data generating process. We can check for degeneracy by l
- 周辺文脈（JA, 自動訳）: 3.1 モデルは退化していますか? / 少し言葉を乱用してしまいますが、k の大きく異なる値がほぼ同じデータ生成プロセスを生成することを意味するために「退化」を使用します。 l によって縮退をチェックできます
- Workflowフェーズ: **EDA / observed data**
- 実務での読み方: モデル化前に、観測単位・外れ値・欠測・群構造・時系列性・上限/下限などを確認する。MLflowではデータ版と前処理版を固定する。
- MLflow連携: `dataset_uri, dataset_hash, preprocessing_version, n_obs, group_count`
- 参照: [公式ページ](https://avehtari.github.io/Bayesian-Workflow/planetary_motion/planetary_motion.html#fig-ppc) / [ソース候補](https://github.com/avehtari/Bayesian-Workflow/blob/eb00fa4397314ef7d90203382542bd44c590e289/planetary_motion/planetary_motion.R)

#### `planetary-motion-planetary-motion/fig-trace-with-warmup-fit1`

- 種別: `figure` / 公式ID: `fig-trace-with-warmup-fit1` / ページ内順序: 4
- caption/列: Figure 4
- 周辺文脈（EN）: Given our prior, k \sim \mathrm{normal}^+(0, 1) , and the very strong log posterior density around k = 1 , we may wonder: how did the chains drift to these distant modes? Based on
- 周辺文脈（JA, 自動訳）: 3.2 放浪者: チェーンはどのようにしてこれらの推定モードを見つけるのでしょうか? / 事前の k \sim \mathrm{normal}^+(0, 1) と、 k = 1 付近の非常に強い対数事後密度を考えると、チェーンはどのようにしてこれらの遠いモードにドリフトしたのか疑問に思うかもしれません。に基づいて
- Workflowフェーズ: **Posterior summary / effect interpretation**
- 実務での読み方: 推定効果・不確実性・派生量を意思決定に接続する。平均だけでなく区間・分布・実務閾値超過確率を残す。
- MLflow連携: `posterior_draws_uri, model_code_hash, ci_width, decision_threshold_prob`
- 参照: [公式ページ](https://avehtari.github.io/Bayesian-Workflow/planetary_motion/planetary_motion.html#fig-trace-with-warmup-fit1) / [ソース候補](https://github.com/avehtari/Bayesian-Workflow/blob/eb00fa4397314ef7d90203382542bd44c590e289/planetary_motion/planetary_motion.R)

#### `planetary-motion-planetary-motion/fig-log-joint`

- 種別: `figure` / 公式ID: `fig-log-joint` / ページ内順序: 5
- caption/列: Figure 5
- 周辺文脈（EN）: Because the parameter space is one-dimensional, we can “cheat” a bit – well, we’ve earned it by setting up a simplified problem – and compute the joint distribution (i.e. unnormali
- 周辺文脈（JA, 自動訳）: 3.3 ローカルモードの存在の確認 / パラメータ空間は 1 次元であるため、少し「ごまかし」をすることができます – まあ、単純化された問題を設定することでそれを獲得しました – し、結合分布 (つまり、非正規分布) を計算します。
- Workflowフェーズ: **EDA / observed data**
- 実務での読み方: モデル化前に、観測単位・外れ値・欠測・群構造・時系列性・上限/下限などを確認する。MLflowではデータ版と前処理版を固定する。
- MLflow連携: `dataset_uri, dataset_hash, preprocessing_version, n_obs, group_count`
- 参照: [公式ページ](https://avehtari.github.io/Bayesian-Workflow/planetary_motion/planetary_motion.html#fig-log-joint) / [ソース候補](https://github.com/avehtari/Bayesian-Workflow/blob/eb00fa4397314ef7d90203382542bd44c590e289/planetary_motion/planetary_motion.R)

#### `planetary-motion-planetary-motion/fig-sim-trajectories`

- 種別: `figure` / 公式ID: `fig-sim-trajectories` / ページ内順序: 6
- caption/列: Figure 6
- 周辺文脈（EN）: Let us now simulate trajectories for various values of k .
- 周辺文脈（JA, 自動訳）: 3.4 楕円運動は多峰性を誘発する / ここで、 k のさまざまな値に対する軌道をシミュレートしてみましょう。
- Workflowフェーズ: **MCMC / computation diagnostics**
- 実務での読み方: 推論結果を解釈する前に、R-hat、ESS、divergence、treedepth、BFMI、trace/pairsを確認する。悪いrunは比較表から除外せず失敗として記録する。
- MLflow連携: `rhat_max, ess_bulk_min, ess_tail_min, divergences, treedepth_hits, bfmi_min`
- 参照: [公式ページ](https://avehtari.github.io/Bayesian-Workflow/planetary_motion/planetary_motion.html#fig-sim-trajectories) / [ソース候補](https://github.com/avehtari/Bayesian-Workflow/blob/eb00fa4397314ef7d90203382542bd44c590e289/planetary_motion/planetary_motion.R)

#### `planetary-motion-planetary-motion/fig-ppc-fit1p`

- 種別: `figure` / 公式ID: `fig-ppc-fit1p` / ページ内順序: 7
- caption/列: Figure 7
- 周辺文脈（EN）: Convergence diagnostics look good
- 周辺文脈（JA, 自動訳）: 4 パスファインダーが助けに来ます！ / コンバージェンス診断は良好なようです
- Workflowフェーズ: **Posterior predictive checking / calibration**
- 実務での読み方: モデルが再現すべき特徴を外していないか確認する。PPC統計量と図をartifact化し、モデル改善の根拠にする。
- MLflow連携: `ppc_stat_*, loo_pit_ecdf_maxdev, calibration_error, replicated_seed`
- 参照: [公式ページ](https://avehtari.github.io/Bayesian-Workflow/planetary_motion/planetary_motion.html#fig-ppc-fit1p) / [ソース候補](https://github.com/avehtari/Bayesian-Workflow/blob/eb00fa4397314ef7d90203382542bd44c590e289/planetary_motion/planetary_motion.R)

#### `planetary-motion-planetary-motion/fig-conditional-likelihood`

- 種別: `figure` / 公式ID: `fig-conditional-likelihood` / ページ内順序: 8
- caption/列: Figure 8
- 周辺文脈（EN）: This is more difficult to visualize because the parameters are now 7-dimensional, rather than 1-dimensional as was the case in our first simplified model. Unfortunately we cannot c
- 周辺文脈（JA, 自動訳）: 5.1 モードを理解するための条件付き尤度の使用 / 最初の単純化モデルの場合のようにパラメータが 1 次元ではなく 7 次元になったため、これを視覚化するのはさらに困難です。残念ながら、
- Workflowフェーズ: **MCMC / computation diagnostics**
- 実務での読み方: 推論結果を解釈する前に、R-hat、ESS、divergence、treedepth、BFMI、trace/pairsを確認する。悪いrunは比較表から除外せず失敗として記録する。
- MLflow連携: `rhat_max, ess_bulk_min, ess_tail_min, divergences, treedepth_hits, bfmi_min`
- 参照: [公式ページ](https://avehtari.github.io/Bayesian-Workflow/planetary_motion/planetary_motion.html#fig-conditional-likelihood) / [ソース候補](https://github.com/avehtari/Bayesian-Workflow/blob/eb00fa4397314ef7d90203382542bd44c590e289/planetary_motion/planetary_motion.R)

#### `planetary-motion-planetary-motion/fig-conditional-likelihood-heatmap`

- 種別: `figure` / 公式ID: `fig-conditional-likelihood-heatmap` / ページ内順序: 9
- caption/列: Figure 9
- 周辺文脈（EN）: This is the type of profile we expect. We can extend this to a heat map, with both coordinates of q_* varying, and observe “ripples” that suggest the presence of local modes.
- 周辺文脈（JA, 自動訳）: 5.1 条件付き尤度を使用してモードを理解する / これは、私たちが期待するタイプのプロファイルです。 q_* の両方の座標が変化するヒート マップにこれを拡張し、ローカル モードの存在を示唆する「リップル」を観察できます。
- Workflowフェーズ: **MCMC / computation diagnostics**
- 実務での読み方: 推論結果を解釈する前に、R-hat、ESS、divergence、treedepth、BFMI、trace/pairsを確認する。悪いrunは比較表から除外せず失敗として記録する。
- MLflow連携: `rhat_max, ess_bulk_min, ess_tail_min, divergences, treedepth_hits, bfmi_min`
- 参照: [公式ページ](https://avehtari.github.io/Bayesian-Workflow/planetary_motion/planetary_motion.html#fig-conditional-likelihood-heatmap) / [ソース候補](https://github.com/avehtari/Bayesian-Workflow/blob/eb00fa4397314ef7d90203382542bd44c590e289/planetary_motion/planetary_motion.R)

#### `planetary-motion-planetary-motion/fig-ppc-fit2p`

- 種別: `figure` / 公式ID: `fig-ppc-fit2p` / ページ内順序: 10
- caption/列: Figure 10
- 周辺文脈（EN）: Posterior predictive checks look good for all chains!
- 周辺文脈（JA, 自動訳）: 5.2 モデルのフィッティング / 事後予測チェックはすべてのチェーンに適しているように見えます。
- Workflowフェーズ: **Posterior predictive checking / calibration**
- 実務での読み方: モデルが再現すべき特徴を外していないか確認する。PPC統計量と図をartifact化し、モデル改善の根拠にする。
- MLflow連携: `ppc_stat_*, loo_pit_ecdf_maxdev, calibration_error, replicated_seed`
- 参照: [公式ページ](https://avehtari.github.io/Bayesian-Workflow/planetary_motion/planetary_motion.html#fig-ppc-fit2p) / [ソース候補](https://github.com/avehtari/Bayesian-Workflow/blob/eb00fa4397314ef7d90203382542bd44c590e289/planetary_motion/planetary_motion.R)

### Simulation-based calibration checking in model development workflow

- ページ: <https://avehtari.github.io/Bayesian-Workflow/sbc/sbc.html>
- ソース候補: <https://github.com/avehtari/Bayesian-Workflow/blob/eb00fa4397314ef7d90203382542bd44c590e289/sbc/sbc.R>

#### `sbc-sbc/figure-001`

- 種別: `figure` / 公式ID: `(none)` / ページ内順序: 1
- caption/列: Figure 1: Pairs plot for our first attempt at the mixture component.
- 周辺文脈（EN）: There are divergences. Let’s examine the MCMC pairs plots:
- 周辺文脈（JA, 自動訳）: 2 混合サブモデル / 発散があります。 MCMC ペアのプロットを調べてみましょう。
- Workflowフェーズ: **Posterior predictive checking / calibration**
- 実務での読み方: モデルが再現すべき特徴を外していないか確認する。PPC統計量と図をartifact化し、モデル改善の根拠にする。
- MLflow連携: `ppc_stat_*, loo_pit_ecdf_maxdev, calibration_error, replicated_seed`
- 参照: [公式ページ](https://avehtari.github.io/Bayesian-Workflow/sbc/sbc.html) / [ソース候補](https://github.com/avehtari/Bayesian-Workflow/blob/eb00fa4397314ef7d90203382542bd44c590e289/sbc/sbc.R)

#### `sbc-sbc/figure-002`

- 種別: `figure` / 公式ID: `(none)` / ページ内順序: 2
- caption/列: Figure 2: Distribution of \widehat{R} statistic for the fits of the mixture component after fixing the first bug.
- 周辺文脈（EN）: So there are some problems - we have quite a bunch of high R-hat and low ESS values. This is the distribution of all rhats:
- 周辺文脈（JA, 自動訳）: 2.1 固定混合モデル / したがって、いくつかの問題があります - かなりの高い R ハット値と低い ESS 値が存在します。これはすべての rhat の分布です。
- Workflowフェーズ: **EDA / observed data**
- 実務での読み方: モデル化前に、観測単位・外れ値・欠測・群構造・時系列性・上限/下限などを確認する。MLflowではデータ版と前処理版を固定する。
- MLflow連携: `dataset_uri, dataset_hash, preprocessing_version, n_obs, group_count`
- 参照: [公式ページ](https://avehtari.github.io/Bayesian-Workflow/sbc/sbc.html) / [ソース候補](https://github.com/avehtari/Bayesian-Workflow/blob/eb00fa4397314ef7d90203382542bd44c590e289/sbc/sbc.R)

#### `sbc-sbc/figure-003`

- 種別: `figure` / 公式ID: `(none)` / ページ内順序: 3
- caption/列: Figure 3: A pairs plot for one of the problematic fits.
- 周辺文脈（EN）: Let’s examine a single pairs plot:
- 周辺文脈（JA, 自動訳）: 2.1 固定混合モデル / 単一ペアのプロットを調べてみましょう:
- Workflowフェーズ: **Posterior predictive checking / calibration**
- 実務での読み方: モデルが再現すべき特徴を外していないか確認する。PPC統計量と図をartifact化し、モデル改善の根拠にする。
- MLflow連携: `ppc_stat_*, loo_pit_ecdf_maxdev, calibration_error, replicated_seed`
- 参照: [公式ページ](https://avehtari.github.io/Bayesian-Workflow/sbc/sbc.html) / [ソース候補](https://github.com/avehtari/Bayesian-Workflow/blob/eb00fa4397314ef7d90203382542bd44c590e289/sbc/sbc.R)

#### `sbc-sbc/figure-004`

- 種別: `figure` / 公式ID: `(none)` / ページ内順序: 4
- caption/列: Figure 4: Pairs plot of a problematic fit in mixture model with ordered components.
- 周辺文脈（EN）: One of the fits has quite a lot of divergent transitions. Let’s look at the pairs plot for the model:
- 周辺文脈（JA, 自動訳）: 2.2 パラメータの順序を修正 / フィットの 1 つに非常に多くの分岐遷移があります。モデルのペア プロットを見てみましょう。
- Workflowフェーズ: **Posterior predictive checking / calibration**
- 実務での読み方: モデルが再現すべき特徴を外していないか確認する。PPC統計量と図をartifact化し、モデル改善の根拠にする。
- MLflow連携: `ppc_stat_*, loo_pit_ecdf_maxdev, calibration_error, replicated_seed`
- 参照: [公式ページ](https://avehtari.github.io/Bayesian-Workflow/sbc/sbc.html) / [ソース候補](https://github.com/avehtari/Bayesian-Workflow/blob/eb00fa4397314ef7d90203382542bd44c590e289/sbc/sbc.R)

#### `sbc-sbc/figure-005`

- 種別: `figure` / 公式ID: `(none)` / ページ内順序: 5
- caption/列: Figure 5: Rank histograms for the simulations where there were no divergecnces
- 周辺文脈（EN）: This gives us no obvious problems.
- 周辺文脈（JA, 自動訳）: 2.3 縮退したコンポーネントを修正しますか? / これにより、明らかな問題は発生しません。
- Workflowフェーズ: **Posterior predictive checking / calibration**
- 実務での読み方: モデルが再現すべき特徴を外していないか確認する。PPC統計量と図をartifact化し、モデル改善の根拠にする。
- MLflow連携: `ppc_stat_*, loo_pit_ecdf_maxdev, calibration_error, replicated_seed`
- 参照: [公式ページ](https://avehtari.github.io/Bayesian-Workflow/sbc/sbc.html) / [ソース候補](https://github.com/avehtari/Bayesian-Workflow/blob/eb00fa4397314ef7d90203382542bd44c590e289/sbc/sbc.R)

#### `sbc-sbc/figure-006`

- 種別: `figure` / 公式ID: `(none)` / ページ内順序: 6
- caption/列: Figure 6: ECDF plots for the simulations where there were no divergences
- 周辺文脈（EN）: This gives us no obvious problems.
- 周辺文脈（JA, 自動訳）: 2.3 縮退したコンポーネントを修正しますか? / これにより、明らかな問題は発生しません。
- Workflowフェーズ: **Posterior predictive checking / calibration**
- 実務での読み方: モデルが再現すべき特徴を外していないか確認する。PPC統計量と図をartifact化し、モデル改善の根拠にする。
- MLflow連携: `ppc_stat_*, loo_pit_ecdf_maxdev, calibration_error, replicated_seed`
- 参照: [公式ページ](https://avehtari.github.io/Bayesian-Workflow/sbc/sbc.html) / [ソース候補](https://github.com/avehtari/Bayesian-Workflow/blob/eb00fa4397314ef7d90203382542bd44c590e289/sbc/sbc.R)

#### `sbc-sbc/figure-007`

- 種別: `figure` / 公式ID: `(none)` / ページ内順序: 7
- caption/列: Figure 7: Nominal (light blue) and observed (black) coverage of central posterior intervals for the simulations where there were no divergecnces
- 周辺文脈（EN）: Since we now have only 8 simulations, it is not surprising that we are still left with a huge uncertainty about the actual coverage of our posterior intervals - we can see that in
- 周辺文脈（JA, 自動訳）: 2.3 縮退したコンポーネントを修正しますか? / 現在、シミュレーションが 8 つしかないため、後方間隔の実際の範囲について大きな不確実性が依然として残っていることは驚くべきことではありません。
- Workflowフェーズ: **EDA / observed data**
- 実務での読み方: モデル化前に、観測単位・外れ値・欠測・群構造・時系列性・上限/下限などを確認する。MLflowではデータ版と前処理版を固定する。
- MLflow連携: `dataset_uri, dataset_hash, preprocessing_version, n_obs, group_count`
- 参照: [公式ページ](https://avehtari.github.io/Bayesian-Workflow/sbc/sbc.html) / [ソース候補](https://github.com/avehtari/Bayesian-Workflow/blob/eb00fa4397314ef7d90203382542bd44c590e289/sbc/sbc.R)

#### `sbc-sbc/figure-008`

- 種別: `figure` / 公式ID: `(none)` / ページ内順序: 8
- caption/列: Figure 8: Rank histogram (top) and ECDF plot (bottom) for the first 100 simulations of the fixed mixture submodel after removing fits with divergent transitions.
- 周辺文脈（EN）: And we can use bind_results to combine the new results with the previous fits to not waste our computational effort.
- 周辺文脈（JA, 自動訳）: 2.3 縮退したコンポーネントを修正しますか? / そして、bind_results を使用して、新しい結果を以前の近似と組み合わせて、計算量を無駄にしないようにできます。
- Workflowフェーズ: **Posterior predictive checking / calibration**
- 実務での読み方: モデルが再現すべき特徴を外していないか確認する。PPC統計量と図をartifact化し、モデル改善の根拠にする。
- MLflow連携: `ppc_stat_*, loo_pit_ecdf_maxdev, calibration_error, replicated_seed`
- 参照: [公式ページ](https://avehtari.github.io/Bayesian-Workflow/sbc/sbc.html) / [ソース候補](https://github.com/avehtari/Bayesian-Workflow/blob/eb00fa4397314ef7d90203382542bd44c590e289/sbc/sbc.R)

#### `sbc-sbc/figure-009`

- 種別: `figure` / 公式ID: `(none)` / ページ内順序: 9
- caption/列: Figure 9: Nominal (light blue) and observed (black) coverage of central posterior intervals for the fixed mixture submodel.
- 周辺文脈（EN）: Seems fairly well within the expected bounds. We could definitely run more iterations if we wanted to have a more strict check, but for now, we are happy and the remaining uncertai
- 周辺文脈（JA, 自動訳）: 2.3 縮退したコンポーネントを修正しますか? / 予想の範囲内にかなり収まっているようです。より厳密なチェックが必要な場合は、さらに反復を実行することもできますが、現時点では満足していますが、残りの点は不確実です。
- Workflowフェーズ: **EDA / observed data**
- 実務での読み方: モデル化前に、観測単位・外れ値・欠測・群構造・時系列性・上限/下限などを確認する。MLflowではデータ版と前処理版を固定する。
- MLflow連携: `dataset_uri, dataset_hash, preprocessing_version, n_obs, group_count`
- 参照: [公式ページ](https://avehtari.github.io/Bayesian-Workflow/sbc/sbc.html) / [ソース候補](https://github.com/avehtari/Bayesian-Workflow/blob/eb00fa4397314ef7d90203382542bd44c590e289/sbc/sbc.R)

#### `sbc-sbc/figure-010`

- 種別: `figure` / 公式ID: `(none)` / ページ内順序: 10
- caption/列: Figure 10: Rank histogram (top) and ECDF plot (bottom) for the first 20 simulations of the logistic submodel.
- 周辺文脈（EN）: Already with 20 datasets we are likely to see suspicious rank/ECDF plots:
- 周辺文脈（JA, 自動訳）: 3 ロジスティック回帰サブモデル / すでに 20 個のデータセットがあるため、疑わしいランク/ECDF プロットが表示される可能性があります。
- Workflowフェーズ: **Posterior predictive checking / calibration**
- 実務での読み方: モデルが再現すべき特徴を外していないか確認する。PPC統計量と図をartifact化し、モデル改善の根拠にする。
- MLflow連携: `ppc_stat_*, loo_pit_ecdf_maxdev, calibration_error, replicated_seed`
- 参照: [公式ページ](https://avehtari.github.io/Bayesian-Workflow/sbc/sbc.html) / [ソース候補](https://github.com/avehtari/Bayesian-Workflow/blob/eb00fa4397314ef7d90203382542bd44c590e289/sbc/sbc.R)

#### `sbc-sbc/figure-011`

- 種別: `figure` / 公式ID: `(none)` / ページ内順序: 11
- caption/列: Figure 11: Simulated and estimated values of all parameters for the first 20 simulations of the logistic regression submodel.
- 周辺文脈（EN）: At this point, we could use more simulations to see if the discrepancy is real. But this is also a good opportunity to introduce additional ways to diagnose mismatches between the
- 周辺文脈（JA, 自動訳）: 3 ロジスティック回帰サブモデル / この時点で、さらに多くのシミュレーションを使用して、不一致が本物かどうかを確認できます。しかし、これは、データ間の不一致を診断するための追加の方法を導入する良い機会でもあります。
- Workflowフェーズ: **Posterior predictive checking / calibration**
- 実務での読み方: モデルが再現すべき特徴を外していないか確認する。PPC統計量と図をartifact化し、モデル改善の根拠にする。
- MLflow連携: `ppc_stat_*, loo_pit_ecdf_maxdev, calibration_error, replicated_seed`
- 参照: [公式ページ](https://avehtari.github.io/Bayesian-Workflow/sbc/sbc.html) / [ソース候補](https://github.com/avehtari/Bayesian-Workflow/blob/eb00fa4397314ef7d90203382542bd44c590e289/sbc/sbc.R)

#### `sbc-sbc/figure-012`

- 種別: `figure` / 公式ID: `(none)` / ページ内順序: 12
- caption/列: Figure 12: Rank histogram (top) and ECDF plot (bottom) for the first 20 simulations of the logistic submodel, now with the log-likelihood derived quantity.
- 周辺文脈（EN）: The rank and ECDF plots are shown below.
- 周辺文脈（JA, 自動訳）: 3 ロジスティック回帰サブモデル / ランクと ECDF プロットを以下に示します。
- Workflowフェーズ: **Posterior predictive checking / calibration**
- 実務での読み方: モデルが再現すべき特徴を外していないか確認する。PPC統計量と図をartifact化し、モデル改善の根拠にする。
- MLflow連携: `ppc_stat_*, loo_pit_ecdf_maxdev, calibration_error, replicated_seed`
- 参照: [公式ページ](https://avehtari.github.io/Bayesian-Workflow/sbc/sbc.html) / [ソース候補](https://github.com/avehtari/Bayesian-Workflow/blob/eb00fa4397314ef7d90203382542bd44c590e289/sbc/sbc.R)

#### `sbc-sbc/figure-013`

- 種別: `figure` / 公式ID: `(none)` / ページ内順序: 13
- caption/列: Rank histogram (top) and ECDF plot (bottom) for the first 10 simulations of the logistic submodel with merged intercept.
- 周辺文脈（EN）: The results for 10 simulations are:
- 周辺文脈（JA, 自動訳）: 3 ロジスティック回帰サブモデル / 10 回のシミュレーションの結果は次のとおりです。
- Workflowフェーズ: **Posterior predictive checking / calibration**
- 実務での読み方: モデルが再現すべき特徴を外していないか確認する。PPC統計量と図をartifact化し、モデル改善の根拠にする。
- MLflow連携: `ppc_stat_*, loo_pit_ecdf_maxdev, calibration_error, replicated_seed`
- 参照: [公式ページ](https://avehtari.github.io/Bayesian-Workflow/sbc/sbc.html) / [ソース候補](https://github.com/avehtari/Bayesian-Workflow/blob/eb00fa4397314ef7d90203382542bd44c590e289/sbc/sbc.R)

#### `sbc-sbc/figure-014`

- 種別: `figure` / 公式ID: `(none)` / ページ内順序: 14
- caption/列: Figure 13: Rank histogram (top) and ECDF plot (bottom) for the first 10 simulations of the logistic submodel with fixed prior.
- 周辺文脈（EN）: The results for ten simulations are:
- 周辺文脈（JA, 自動訳）: 3.1 事前定義の修正 / 10 回のシミュレーションの結果は次のとおりです。
- Workflowフェーズ: **Posterior predictive checking / calibration**
- 実務での読み方: モデルが再現すべき特徴を外していないか確認する。PPC統計量と図をartifact化し、モデル改善の根拠にする。
- MLflow連携: `ppc_stat_*, loo_pit_ecdf_maxdev, calibration_error, replicated_seed`
- 参照: [公式ページ](https://avehtari.github.io/Bayesian-Workflow/sbc/sbc.html) / [ソース候補](https://github.com/avehtari/Bayesian-Workflow/blob/eb00fa4397314ef7d90203382542bd44c590e289/sbc/sbc.R)

#### `sbc-sbc/figure-015`

- 種別: `figure` / 公式ID: `(none)` / ページ内順序: 15
- caption/列: Figure 14: Rank histogram (top) and ECDF plot (bottom) for the full 200 simulations of the logistic submodel with merged intercept.
- 周辺文脈（EN）: No obvious problem, so let’s add 200 additional simulations:
- 周辺文脈（JA, 自動訳）: 3.1 事前定義の修正 / 明らかな問題はないので、さらに 200 個のシミュレーションを追加しましょう。
- Workflowフェーズ: **Posterior predictive checking / calibration**
- 実務での読み方: モデルが再現すべき特徴を外していないか確認する。PPC統計量と図をartifact化し、モデル改善の根拠にする。
- MLflow連携: `ppc_stat_*, loo_pit_ecdf_maxdev, calibration_error, replicated_seed`
- 参照: [公式ページ](https://avehtari.github.io/Bayesian-Workflow/sbc/sbc.html) / [ソース候補](https://github.com/avehtari/Bayesian-Workflow/blob/eb00fa4397314ef7d90203382542bd44c590e289/sbc/sbc.R)

#### `sbc-sbc/figure-016`

- 種別: `figure` / 公式ID: `(none)` / ページ内順序: 16
- caption/列: Figure 15: Simulated and estimated values for the 200 simulations of the logistic submodel with merged intercept.
- 周辺文脈（EN）: Looking good! We can also check that we are indeed able to learn the model parameters with reasonable precision from the data.
- 周辺文脈（JA, 自動訳）: 3.1 以前の定義を修正/見栄えが良くなりました!また、実際にデータから妥当な精度でモデル パラメーターを学習できることを確認することもできます。
- Workflowフェーズ: **EDA / observed data**
- 実務での読み方: モデル化前に、観測単位・外れ値・欠測・群構造・時系列性・上限/下限などを確認する。MLflowではデータ版と前処理版を固定する。
- MLflow連携: `dataset_uri, dataset_hash, preprocessing_version, n_obs, group_count`
- 参照: [公式ページ](https://avehtari.github.io/Bayesian-Workflow/sbc/sbc.html) / [ソース候補](https://github.com/avehtari/Bayesian-Workflow/blob/eb00fa4397314ef7d90203382542bd44c590e289/sbc/sbc.R)

#### `sbc-sbc/figure-017`

- 種別: `figure` / 公式ID: `(none)` / ページ内順序: 17
- caption/列: Figure 16: Rank histogram (top) and ECDF difference plot (bottom) for the first 200 simulations of the logistic submodel with fixed prior.
- 周辺文脈（EN）: We get some amount of divergent transitions, but the ranks look pretty good:
- 周辺文脈（JA, 自動訳）: 4 完全なモデル / ある程度の発散遷移が得られますが、ランクはかなり良好に見えます。
- Workflowフェーズ: **Posterior predictive checking / calibration**
- 実務での読み方: モデルが再現すべき特徴を外していないか確認する。PPC統計量と図をartifact化し、モデル改善の根拠にする。
- MLflow連携: `ppc_stat_*, loo_pit_ecdf_maxdev, calibration_error, replicated_seed`
- 参照: [公式ページ](https://avehtari.github.io/Bayesian-Workflow/sbc/sbc.html) / [ソース候補](https://github.com/avehtari/Bayesian-Workflow/blob/eb00fa4397314ef7d90203382542bd44c590e289/sbc/sbc.R)

#### `sbc-sbc/figure-018`

- 種別: `figure` / 公式ID: `(none)` / ページ内順序: 18
- caption/列: Figure 17: Fano factors of fits with/without divergent transitions.
- 周辺文脈（EN）: All the divergences are for low Fano factors - this is the histogram of Fano factor for diverging fits:
- 周辺文脈（JA, 自動訳）: 4.1 棄却サンプリングの追加 / すべての発散は低い Fano 因子に対するものです - これは発散近似の Fano 因子のヒストグラムです。
- Workflowフェーズ: **Posterior predictive checking / calibration**
- 実務での読み方: モデルが再現すべき特徴を外していないか確認する。PPC統計量と図をartifact化し、モデル改善の根拠にする。
- MLflow連携: `ppc_stat_*, loo_pit_ecdf_maxdev, calibration_error, replicated_seed`
- 参照: [公式ページ](https://avehtari.github.io/Bayesian-Workflow/sbc/sbc.html) / [ソース候補](https://github.com/avehtari/Bayesian-Workflow/blob/eb00fa4397314ef7d90203382542bd44c590e289/sbc/sbc.R)

#### `sbc-sbc/figure-019`

- 種別: `figure` / 公式ID: `(none)` / ページ内順序: 19
- caption/列: Figure 18: Rank histogram (top) and ECDF difference plot (bottom) for the full model after rejecting datasets with low Fano factor.
- 周辺文脈（EN）: No more divergences! And the ranks look nice.
- 周辺文脈（JA, 自動訳）: 4.1 拒絶サンプリングの追加 / もう発散はありません!そしてランクもいい感じです。
- Workflowフェーズ: **Posterior predictive checking / calibration**
- 実務での読み方: モデルが再現すべき特徴を外していないか確認する。PPC統計量と図をartifact化し、モデル改善の根拠にする。
- MLflow連携: `ppc_stat_*, loo_pit_ecdf_maxdev, calibration_error, replicated_seed`
- 参照: [公式ページ](https://avehtari.github.io/Bayesian-Workflow/sbc/sbc.html) / [ソース候補](https://github.com/avehtari/Bayesian-Workflow/blob/eb00fa4397314ef7d90203382542bd44c590e289/sbc/sbc.R)

#### `sbc-sbc/figure-020`

- 種別: `figure` / 公式ID: `(none)` / ページ内順序: 20
- caption/列: Figure 19: Difference between actual and expected coverage of central posterior intervals for the full model.
- 周辺文脈（EN）: And our coverage is pretty tight:
- 周辺文脈（JA, 自動訳）: 4.1 拒絶サンプリングの追加 / そして、私たちのカバー範囲はかなり狭いです:
- Workflowフェーズ: **Posterior predictive checking / calibration**
- 実務での読み方: モデルが再現すべき特徴を外していないか確認する。PPC統計量と図をartifact化し、モデル改善の根拠にする。
- MLflow連携: `ppc_stat_*, loo_pit_ecdf_maxdev, calibration_error, replicated_seed`
- 参照: [公式ページ](https://avehtari.github.io/Bayesian-Workflow/sbc/sbc.html) / [ソース候補](https://github.com/avehtari/Bayesian-Workflow/blob/eb00fa4397314ef7d90203382542bd44c590e289/sbc/sbc.R)

#### `sbc-sbc/figure-021`

- 種別: `figure` / 公式ID: `(none)` / ページ内順序: 21
- caption/列: Figure 20: Rank histogram (top) and ECDF difference plot (bottom) after adding more simulations for the complete model.
- 周辺文脈（EN）: Our plots and coverage are now pretty decent:
- 周辺文脈（JA, 自動訳）: 4.1 拒絶サンプリングの追加 / プロットとカバレッジはかなりまともになりました。
- Workflowフェーズ: **Posterior predictive checking / calibration**
- 実務での読み方: モデルが再現すべき特徴を外していないか確認する。PPC統計量と図をartifact化し、モデル改善の根拠にする。
- MLflow連携: `ppc_stat_*, loo_pit_ecdf_maxdev, calibration_error, replicated_seed`
- 参照: [公式ページ](https://avehtari.github.io/Bayesian-Workflow/sbc/sbc.html) / [ソース候補](https://github.com/avehtari/Bayesian-Workflow/blob/eb00fa4397314ef7d90203382542bd44c590e289/sbc/sbc.R)

#### `sbc-sbc/figure-022`

- 種別: `figure` / 公式ID: `(none)` / ページ内順序: 22
- caption/列: Figure 21: Difference between actual and expected coverage of central posterior intervals for the full model, including more simulations.
- 周辺文脈（EN）: Our plots and coverage are now pretty decent:
- 周辺文脈（JA, 自動訳）: 4.1 拒絶サンプリングの追加 / プロットとカバレッジはかなりまともになりました。
- Workflowフェーズ: **Posterior predictive checking / calibration**
- 実務での読み方: モデルが再現すべき特徴を外していないか確認する。PPC統計量と図をartifact化し、モデル改善の根拠にする。
- MLflow連携: `ppc_stat_*, loo_pit_ecdf_maxdev, calibration_error, replicated_seed`
- 参照: [公式ページ](https://avehtari.github.io/Bayesian-Workflow/sbc/sbc.html) / [ソース候補](https://github.com/avehtari/Bayesian-Workflow/blob/eb00fa4397314ef7d90203382542bd44c590e289/sbc/sbc.R)

#### `sbc-sbc/figure-023`

- 種別: `figure` / 公式ID: `(none)` / ページ内順序: 23
- caption/列: Figure 22: Simulated and estimated values for the comibned model and more simulations.
- 周辺文脈（EN）: Finally, we can also use this simulation exercise to understand what would we be likely to learn from an experiment matching the simulations (50 observations, 3 predictors) and plo
- 周辺文脈（JA, 自動訳）: 4.1 拒絶サンプリングの追加 / 最後に、このシミュレーション演習を使用して、シミュレーション (50 の観測値、3 つの予測子) と plo に一致する実験から何が学べるかを理解することもできます。
- Workflowフェーズ: **Posterior predictive checking / calibration**
- 実務での読み方: モデルが再現すべき特徴を外していないか確認する。PPC統計量と図をartifact化し、モデル改善の根拠にする。
- MLflow連携: `ppc_stat_*, loo_pit_ecdf_maxdev, calibration_error, replicated_seed`
- 参照: [公式ページ](https://avehtari.github.io/Bayesian-Workflow/sbc/sbc.html) / [ソース候補](https://github.com/avehtari/Bayesian-Workflow/blob/eb00fa4397314ef7d90203382542bd44c590e289/sbc/sbc.R)
