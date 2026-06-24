# Bayesian WorkflowをMLflowで実装・運用するためのガイド

## 0. 目的

Bayesian Workflowの実務化では、**一つの最終モデルだけを保存する**のでは足りない。重要なのは、失敗モデル・priorの試行錯誤・MCMC診断・PPC・LOO比較・SBC・意思決定までを、あとから追跡できる形で残すこと。本ガイドでは、Stan/R/brms/Pythonの実験をMLflowで管理するための最小設計を示す。

参照元:

- 公式書籍サイト: <https://avehtari.github.io/Bayesian-Workflow/>
- 公式コードリポジトリ: <https://github.com/avehtari/Bayesian-Workflow>
- 本文精読用のCC-BY arXiv版: <https://arxiv.org/abs/2011.01808>

## 1. MLflow設計原則

1. **workflow iterationをrunにする**: 「fitしたモデル」だけでなく、EDA、prior predictive、posterior fit、diagnostics、PPC、LOO、SBC、decisionをrunとして残す。
2. **失敗runを消さない**: divergence、R-hat不良、Pareto-k不良、prior predictive破綻は、次の改善理由になる。
3. **図表をartifact化する**: bayesplot/ggplot/ArviZのpng/html、LOO表、diagnostic table、SBC rank plotをartifactとして保存する。
4. **モデルコードとデータ版を固定する**: Stan/R/Pythonコード、formula、prior spec、seed、データhash、前処理versionをparams/tags/artifactsへ記録する。
5. **比較はmetricだけで決めない**: elpd差、SE、Pareto-k、PPC失敗箇所、意思決定損失を一緒に見る。

## 2. Experiment / Run構造

推奨experiment名:

```text
bayesian-workflow/<project_or_case_study>
```

推奨nested run構造:

```text
parent run: analysis_iteration/<YYYYMMDD>-<question>-<iteration>
  child: 00_data_profile
  child: 01_prior_predictive/<model_id>
  child: 02_fit/<model_id>
  child: 03_diagnostics/<model_id>
  child: 04_posterior_predictive/<model_id>
  child: 05_loo_compare/<comparison_id>
  child: 06_sbc/<model_id>             # 実装検証が必要な場合
  child: 07_decision/<policy_id>       # 意思決定へ接続する場合
```

## 3. 共通タグ・パラメータ・メトリクス

### 3.1 Tags

| tag | 例 | 用途 |
|---|---|---|
| `bw.project` | `marketing_response_model` | プロジェクト名 |
| `bw.case_study` | `sleep_study` | Bayesian Workflow内の類似ケース |
| `bw.phase` | `prior_predictive`, `fit`, `ppc`, `loo` | Workflowフェーズ |
| `bw.model_id` | `m03_student_t_varying_slope` | モデル識別子 |
| `bw.model_family` | `hierarchical_gaussian`, `beta_binomial` | モデル族 |
| `bw.question` | `treatment_effect` | 実務上の問い |
| `bw.status` | `candidate`, `failed_diagnostics`, `reportable` | run状態 |
| `bw.source.figure_id` | `sleep_study/fig-sleepstudy-pp_check-fit4` | 図表カタログへの参照 |

### 3.2 Params

| param | 例 | 用途 |
|---|---|---|
| `data_uri` | `s3://.../train.parquet` | 入力データ |
| `data_hash` | `sha256:...` | データ固定 |
| `formula` | `y ~ x + (1+x|group)` | モデル式 |
| `prior_spec_id` | `prior_v04_student_t` | prior定義 |
| `stan_file` | `models/m03.stan` | モデルコード |
| `model_code_hash` | `sha256:...` | コード固定 |
| `seed` | `20260622` | 再現性 |
| `chains`, `iter_warmup`, `iter_sampling` | `4`, `1000`, `1000` | MCMC設定 |
| `adapt_delta`, `max_treedepth` | `0.95`, `12` | NUTS設定 |

### 3.3 Metrics

| フェーズ | metric例 | ゲート例 |
|---|---|---|
| MCMC診断 | `rhat_max`, `ess_bulk_min`, `ess_tail_min`, `divergences`, `bfmi_min` | `rhat_max <= 1.01`, `divergences == 0`を目標。例外時は理由を残す。 |
| prior predictive | `prior_implausible_rate`, `prior_y_min`, `prior_y_max` | あり得ない領域の生成率が閾値以下。 |
| PPC | `ppc_stat_mean_abs_z`, `loo_pit_ecdf_maxdev`, `calibration_error` | 重要な観測特徴を再現できない場合はモデル改善へ。 |
| LOO | `loo_elpd`, `loo_elpd_diff`, `loo_se_diff`, `pareto_k_gt_0_7`, `reloo_count` | elpd差だけでなくSEとPareto-kを確認。 |
| SBC | `sbc_rank_ks_stat`, `sbc_coverage_error`, `sbc_failed_fit_count` | rank/coverageが崩れたら実装か推論設定を疑う。 |
| decision | `expected_utility`, `expected_loss`, `prob_action_is_optimal` | 予測性能ではなく業務損失で最終判断。 |

## 4. Artifact設計

```text
artifacts/
  data_profile/
    schema.json
    missingness.md
    eda_plots/*.png
  model/
    model.stan
    formula.txt
    priors.yaml
    generated_quantities_notes.md
  diagnostics/
    summary_draws.csv
    rhat_ess.csv
    trace_rank_plots/*.png
    divergences_pairs.png
  checks/
    prior_predictive/*.png
    posterior_predictive/*.png
    loo_pit/*.png
  comparison/
    loo_compare.csv
    model_card.md
  sbc/
    rank_histograms/*.png
    coverage.csv
  decision/
    utility_curve.png
    policy_table.csv
```

## 5. Python実装スケルトン

```python
from __future__ import annotations

import hashlib
import json
from pathlib import Path

import mlflow


def file_sha256(path: str | Path) -> str:
    p = Path(path)
    h = hashlib.sha256()
    with p.open('rb') as f:
        for block in iter(lambda: f.read(1024 * 1024), b''):
            h.update(block)
    return 'sha256:' + h.hexdigest()


def log_bayes_fit(
    *,
    experiment: str,
    model_id: str,
    phase: str,
    data_uri: str,
    model_file: str | Path,
    prior_spec: dict,
    sampler_config: dict,
    metrics: dict,
    artifact_paths: list[str | Path],
    tags: dict | None = None,
) -> str:
    mlflow.set_experiment(experiment)
    with mlflow.start_run(run_name=f"{phase}/{model_id}") as run:
        mlflow.set_tags({
            'bw.phase': phase,
            'bw.model_id': model_id,
            'bw.status': 'candidate',
            **(tags or {}),
        })
        mlflow.log_params({
            'data_uri': data_uri,
            'model_file': str(model_file),
            'model_code_hash': file_sha256(model_file),
            **sampler_config,
        })
        mlflow.log_text(json.dumps(prior_spec, ensure_ascii=False, indent=2), 'model/priors.json')
        mlflow.log_metrics({k: float(v) for k, v in metrics.items() if v is not None})
        for path in artifact_paths:
            path = Path(path)
            if path.exists():
                mlflow.log_artifact(str(path))
        return run.info.run_id
```

## 6. R / brms / cmdstanr運用メモ

- R側からはMLflow R API、または `reticulate` 経由でPythonの `mlflow` を呼ぶ。
- `brmsfit` / `cmdstanr` の巨大オブジェクトをそのままMLflowへ置くより、まず以下を分離する。
  - posterior draws: parquet/csv/arrow、または外部ストレージURI
  - summary: `posterior::summarise_draws()` のCSV
  - diagnostics: `cmdstanr$diagnostic_summary()`、divergence一覧、treedepth一覧
  - plots: png/html
- 生データや認証情報はcommit/MLflow artifactに直接入れない。hashと安全なURIだけを残す。

## 7. 図表カテゴリとMLflow runの対応

| 図表カテゴリ | MLflow phase | 主なartifact | 主なmetric/tag |
|---|---|---|---|
| EDA / 観測データ | `data_profile` | data schema, missingness, EDA plot | `n_obs`, `group_count`, `data_hash` |
| prior predictive | `prior_predictive` | prior predictive plot, implausible examples | `prior_implausible_rate`, `prior_spec_id` |
| posterior summary | `fit` | posterior intervals, effect plots | `ci_width`, `prob_gt_threshold` |
| MCMC診断 | `diagnostics` | trace/rank/pairs/divergence plots | `rhat_max`, `ess_min`, `divergences` |
| PPC / calibration | `posterior_predictive` | PPC hist/rootogram/LOO-PIT | `calibration_error`, `ppc_stat_*` |
| LOO / model comparison | `loo_compare` | `loo_compare.csv`, pointwise elpd plot | `loo_elpd_diff`, `pareto_k_gt_0_7` |
| prior-likelihood sensitivity | `sensitivity` | powerscaling plots | `prior_conflict_flag`, `sensitivity_delta` |
| SBC | `sbc` | rank hist, ECDF, coverage plots | `sbc_rank_ks_stat`, `coverage_error` |
| decision analysis | `decision` | utility/loss curves, policy table | `expected_utility`, `chosen_action` |

## 8. Reportable modelの判定チェックリスト

- [ ] データ版・前処理版・schemaが固定されている。
- [ ] prior predictiveで実務的に不可能な値が許容範囲内。
- [ ] MCMC診断に重大な警告がない、または警告の影響を説明できる。
- [ ] PPC/校正図で重要なデータ特徴を再現できている。
- [ ] LOO比較ではelpd差、SE、Pareto-kをセットで見ている。
- [ ] 主要結論がprior変更・likelihood変更・データ点影響に過度依存していない。
- [ ] 最終判断がビジネス/研究上の損失・効用に接続されている。
- [ ] 失敗runと改善理由がMLflow上で追跡できる。

## 9. 最小導入手順

```bash
# Python側（uv管理プロジェクトの場合）
uv add mlflow arviz pandas matplotlib
uv run mlflow ui --backend-store-uri ./mlruns
```

1. 既存分析コードの最後に、summary CSVと図を保存する処理を追加する。
2. その保存先を `mlflow.log_artifact()` で記録する。
3. `rhat_max`, `ess_min`, `divergences`, `loo_elpd_diff`, `pareto_k_gt_0_7` だけでも先にmetric化する。
4. model_id/prior_spec_id/data_hashをparamsに入れる。
5. 比較ダッシュボードはMLflow UIでrunをfilterし、必要なら `mlflow.search_runs()` で表を作る。
