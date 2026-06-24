from __future__ import annotations

import csv
import hashlib
import html
import json
import re
import textwrap
import time
from pathlib import Path
from typing import Iterable

try:
    from deep_translator import GoogleTranslator
except Exception:  # pragma: no cover - doc generation can run without network translator
    GoogleTranslator = None  # type: ignore[assignment]

try:
    import argostranslate.translate as argos_translate
except Exception:  # pragma: no cover - optional offline translator
    argos_translate = None  # type: ignore[assignment]

ROOT = Path(__file__).resolve().parents[1]
CACHE = ROOT.parent / ".cache_bys_workflow"
INVENTORY = ROOT / "figure_table_inventory.json"
ARXIV_TEXT = CACHE / "arxiv_text.txt"
TRANSLATION_CACHE = ROOT / "data" / "translation_cache_arxiv2011_01808.json"
CATALOGUE_CSV = ROOT / "data" / "official_site_figures_tables_catalogue.csv"
FIG_MD = ROOT / "01_figures_tables_explanation.md"
TRANS_MD = ROOT / "02_four_line_chunk_translation_arxiv2011.md"
MLFLOW_MD = ROOT / "03_mlflow_implementation_guide.md"
README = ROOT / "README.md"

SITE_BASE = "https://avehtari.github.io/Bayesian-Workflow/"
OFFICIAL_REPO = "https://github.com/avehtari/Bayesian-Workflow"
OFFICIAL_COMMIT = "eb00fa4397314ef7d90203382542bd44c590e289"
ARXIV_ABS = "https://arxiv.org/abs/2011.01808"
ARXIV_PDF = "https://arxiv.org/pdf/2011.01808"
ARXIV_LICENSE = "https://creativecommons.org/licenses/by/4.0/"

PHASE_RULES: list[tuple[str, str]] = [
    (r"\b(data|plot the data|observed|dataset|read in data|visualize the data|distribution)\b", "EDA / observed data"),
    (r"prior predictive|prior-only|prior only|simulate fake|simulated data|constructed data", "Prior / prior predictive"),
    (r"posterior predictive|pp_check|ppc|loo[- ]?pit|calibration|rootogram|predictive interval|replicates", "Posterior predictive checking / calibration"),
    (r"posterior|conditional effects|derived quantities|ld50|effect|summary|draws|interval", "Posterior summary / effect interpretation"),
    (r"convergence|rhat|widehat|ess|trace|pairs|diverg|treedepth|bfmi|funnel|mixing|multimod|geometry", "MCMC / computation diagnostics"),
    (r"loo|elpd|cross validation|model comparison|compare the models|reloo|pareto", "LOO-CV / model comparison"),
    (r"prior sensitivity|priorsense|power[- ]?scaling|prior.*likelihood|sensitivity|conflict", "Prior-likelihood sensitivity"),
    (r"simulation-based calibration|rank histogram|ecdf|coverage|fano|sbc", "Simulation-Based Calibration"),
    (r"decision|utility|loss|time series competition|forecast|mixture model for time series", "Decision analysis / forecasting"),
    (r"debug|fix|breaking|incremental|model building|expansion|variable selection|latent", "Model development / debugging"),
]

PRACTICAL_READING = {
    "EDA / observed data": "モデル化前に、観測単位・外れ値・欠測・群構造・時系列性・上限/下限などを確認する。MLflowではデータ版と前処理版を固定する。",
    "Prior / prior predictive": "事前分布が現実的なデータ範囲を生成するかを見る。現場導入前に、あり得ない予測の比率をゲート化する。",
    "Posterior summary / effect interpretation": "推定効果・不確実性・派生量を意思決定に接続する。平均だけでなく区間・分布・実務閾値超過確率を残す。",
    "MCMC / computation diagnostics": "推論結果を解釈する前に、R-hat、ESS、divergence、treedepth、BFMI、trace/pairsを確認する。悪いrunは比較表から除外せず失敗として記録する。",
    "Posterior predictive checking / calibration": "モデルが再現すべき特徴を外していないか確認する。PPC統計量と図をartifact化し、モデル改善の根拠にする。",
    "LOO-CV / model comparison": "elpd差だけでなくSEとPareto-kを読み、勝敗より『どのデータ点で負けるか』を確認する。",
    "Prior-likelihood sensitivity": "結論がpriorに依存していないか、またpriorとlikelihoodが衝突していないか確認する。",
    "Simulation-Based Calibration": "実装バグ・推論バイアス・coverage崩れをrank/ECDF/coverageで検出する。Stan/PPL実装のCIに組み込む。",
    "Decision analysis / forecasting": "予測分布を損失・効用・閾値判断へ変換し、選択アクションと期待効用を記録する。",
    "Model development / debugging": "小さいモデルから始め、失敗runを観察しながらモデル族・prior・データ処理を段階的に拡張する。",
    "Unclassified / inspect manually": "captionが薄い図表。前後の本文・コードchunk・公式ソースを確認して役割を確定する。",
}

MLFLOW_LINKS = {
    "EDA / observed data": "dataset_uri, dataset_hash, preprocessing_version, n_obs, group_count",
    "Prior / prior predictive": "prior_spec_id, prior_predictive_seed, simulated_n, implausible_rate",
    "Posterior summary / effect interpretation": "posterior_draws_uri, model_code_hash, ci_width, decision_threshold_prob",
    "MCMC / computation diagnostics": "rhat_max, ess_bulk_min, ess_tail_min, divergences, treedepth_hits, bfmi_min",
    "Posterior predictive checking / calibration": "ppc_stat_*, loo_pit_ecdf_maxdev, calibration_error, replicated_seed",
    "LOO-CV / model comparison": "loo_elpd, loo_elpd_diff, loo_se_diff, pareto_k_gt_0_7, reloo_count",
    "Prior-likelihood sensitivity": "priorsense_*, power_scaling_delta, prior_conflict_flag",
    "Simulation-Based Calibration": "sbc_sim_n, rank_uniformity_stat, coverage_error, failed_fit_count",
    "Decision analysis / forecasting": "utility_function_id, loss, threshold, expected_utility, chosen_action",
    "Model development / debugging": "iteration_id, change_reason, failure_mode, hypothesis, next_action",
    "Unclassified / inspect manually": "source_page_url, source_repo_url, manual_review_status",
}

TERMS: dict[str, str] = {
    "Bayesian workflow": "ベイズワークフロー。モデル構築・推論・診断・改善・比較を反復する実務プロセス。",
    "Bayesian inference": "ベイズ推論。事前分布と尤度から事後分布を計算する中核処理。",
    "probabilistic programming": "確率的プログラミング。Stanなどで確率モデルをコードとして記述し推論する方法。",
    "prior predictive": "事前予測。データを見る前のpriorだけで生成される予測分布を確認する診断。",
    "posterior predictive": "事後予測。推定後のモデルが観測データの特徴を再現できるかを見る診断。",
    "model checking": "モデルチェック。モデルの仮定・予測・計算結果がデータや目的に合うか検査すること。",
    "model comparison": "モデル比較。LOO-CVなどで複数モデルの予測性能や弱点を比較すること。",
    "cross validation": "交差検証。汎化性能を推定するためにデータを分割/近似除外する評価法。",
    "leave-one-out": "LOO。一点ずつ除外した予測評価を効率的に近似する交差検証。",
    "Pareto": "Pareto-k診断。PSIS-LOOの信頼性を示す診断量。大きいと再推定やモデル修正が必要。",
    "simulation-based calibration": "SBC。シミュレーション真値と事後rankを比べ、実装・推論の校正を検査する方法。",
    "posterior distribution": "事後分布。データ観測後の未知量の不確実性を表す分布。",
    "prior distribution": "事前分布。データ観測前の知識・制約を表す分布。",
    "likelihood": "尤度。パラメータが与えられたときデータがどれだけ起こりやすいか。",
    "generative model": "生成モデル。データ生成過程を確率的に記述するモデル。",
    "reparameterization": "再パラメータ化。計算しやすい幾何に変えるためのパラメータ表現変更。",
    "multimodality": "多峰性。事後分布に複数の山があり、MCMCが混合しにくい状態。",
    "divergent": "divergence。HMC/NUTSで幾何が悪く積分が破綻した警告。",
    "R-hat": "R-hat。複数chainの収束を測る診断量。1から離れるほど問題。",
    "ESS": "有効サンプルサイズ。自己相関を考慮した独立サンプル相当数。",
    "Markov chain": "マルコフ連鎖。MCMCで事後分布からサンプルを得るための確率過程。",
    "posterior draws": "事後ドロー。事後分布から得たサンプル。",
    "uncertainty": "不確実性。観測・パラメータ・モデル構造・意思決定に残る曖昧さ。",
    "validation": "検証。モデルが目的・データ・外部知識に照らして妥当かを確認すること。",
    "troubleshooting": "トラブルシュート。計算・モデル・データの失敗原因を切り分けること。",
    "workflow": "ワークフロー。実務分析の反復手順全体。",
    "model building": "モデル構築。仮定・データ構造・prior・likelihoodを組み合わせる工程。",
    "approximate": "近似。速度や扱いやすさのため、正確な推論・モデルを緩めること。",
    "prediction": "予測。未知/将来/除外データに対する分布や点推定。",
    "decision": "意思決定。予測分布を損失・効用・行動選択へ接続する工程。",
}


def slug(text: str) -> str:
    text = re.sub(r"[^A-Za-z0-9]+", "-", text.strip()).strip("-").lower()
    return text or "item"


def clean_text(text: str | None) -> str:
    if text is None:
        return ""
    text = html.unescape(str(text))
    text = re.sub(r"\s+", " ", text).strip()
    return text


def infer_phase(item: dict, page: dict) -> str:
    hay = " ".join(
        clean_text(x)
        for x in [
            item.get("id"),
            item.get("caption"),
            item.get("heading"),
            item.get("previous_text"),
            page.get("title"),
            page.get("h1"),
            page.get("nav_text"),
        ]
    ).lower()
    for pattern, phase in PHASE_RULES:
        if re.search(pattern, hay, flags=re.I):
            return phase
    return "Unclassified / inspect manually"


def source_url(page: dict, item: dict) -> str:
    base = clean_text(page.get("url"))
    iid = clean_text(item.get("id"))
    return f"{base}#{iid}" if iid else base


def source_repo_url(page: dict) -> str:
    href = clean_text(page.get("href"))
    if href.endswith(".html"):
        stem = href[:-5]
    else:
        stem = href
    # Quarto top-level pages are .qmd; case-study pages generally pair with .R or .qmd.
    if "/" not in stem:
        candidate = f"{stem}.qmd"
    else:
        folder = stem.rsplit("/", 1)[0]
        name = stem.rsplit("/", 1)[1]
        candidate = f"{folder}/{name}.R"
    return f"{OFFICIAL_REPO}/blob/{OFFICIAL_COMMIT}/{candidate}"


def iter_records(data: list[dict]) -> Iterable[dict]:
    for page in data:
        page_key = slug(page.get("href", page.get("title", "page")).replace(".html", ""))
        for kind, key in [("figure", "figures"), ("standalone_image", "standalone_images"), ("table", "tables")]:
            for ordinal, item in enumerate(page.get(key, []), 1):
                iid = clean_text(item.get("id"))
                caption = clean_text(item.get("caption") or item.get("alt"))
                heading = clean_text(item.get("heading"))
                previous = clean_text(item.get("previous_text"))
                phase = infer_phase(item, page)
                local_id = f"{page_key}/{iid or kind + '-' + str(ordinal).zfill(3)}"
                if kind == "table":
                    caption_or_headers = "; ".join(str(x) for x in item.get("preview", [])[:8])
                else:
                    caption_or_headers = caption
                yield {
                    "kind": kind,
                    "page_href": clean_text(page.get("href")),
                    "page_title": clean_text(page.get("title")),
                    "h1": clean_text(page.get("h1")),
                    "nav_text": clean_text(page.get("nav_text")),
                    "local_id": local_id,
                    "official_id": iid,
                    "ordinal_in_page": ordinal,
                    "official_caption_or_headers": caption_or_headers,
                    "caption_status": "label_only" if item.get("label_only") else ("empty" if not caption_or_headers else "descriptive_or_headers"),
                    "nearest_heading": heading,
                    "context_en": previous,
                    "rows": item.get("rows", ""),
                    "cols": item.get("cols", ""),
                    "n_imgs": item.get("n_imgs", ""),
                    "workflow_phase": phase,
                    "practical_reading_ja": PRACTICAL_READING[phase],
                    "mlflow_links": MLFLOW_LINKS[phase],
                    "source_page_url": source_url(page, item),
                    "source_repo_url": source_repo_url(page),
                    "image_storage_policy": "link_only_no_binary_copy_for_crc_book_site",
                }


def load_json(path: Path, default):
    if not path.exists():
        return default
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except Exception:
        return default


def write_text_lf(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="\n") as f:
        f.write(text)


def save_json(path: Path, obj) -> None:
    write_text_lf(path, json.dumps(obj, ensure_ascii=False, indent=2))


def split_batches(items: list[tuple[str, str]], max_chars: int = 4200) -> list[list[tuple[str, str]]]:
    batches: list[list[tuple[str, str]]] = []
    cur: list[tuple[str, str]] = []
    cur_len = 0
    for key, text in items:
        block_len = len(key) + len(text) + 30
        if cur and cur_len + block_len > max_chars:
            batches.append(cur)
            cur = []
            cur_len = 0
        cur.append((key, text))
        cur_len += block_len
    if cur:
        batches.append(cur)
    return batches


def google_translate_many(texts: dict[str, str], cache_key: str, sleep_s: float = 0.25) -> dict[str, str]:
    """Translate values to Japanese with JSON cache.

    Figure/table contexts are short and use Google Translate when available.
    The arXiv chunk file is much larger; for that we prefer the installed
    Argos Translate en→ja package to avoid network timeouts/rate limits.
    """
    cache = load_json(TRANSLATION_CACHE, {})
    store = cache.setdefault(cache_key, {})
    missing = [(k, v) for k, v in texts.items() if v and k not in store]

    if missing and cache_key == "arxiv_chunks" and argos_translate is not None:
        total = len(missing)
        for idx, (key, text) in enumerate(missing, 1):
            try:
                store[key] = argos_translate.translate(text, "en", "ja").strip()
            except Exception as exc:  # pragma: no cover - model dependent
                print(f"WARN: Argos translation failed for {key}: {exc}")
                store[key] = ""
            if idx % 25 == 0 or idx == total:
                print(f"Argos translated arXiv chunks {idx}/{total}")
                save_json(TRANSLATION_CACHE, cache)
        save_json(TRANSLATION_CACHE, cache)
        return {k: store.get(k) or texts.get(k, "") for k in texts}

    if missing and GoogleTranslator is not None:
        translator = GoogleTranslator(source="en", target="ja")
        batches = split_batches(missing)
        for idx, batch in enumerate(batches, 1):
            print(f"Google translating {cache_key} batch {idx}/{len(batches)}")
            body = "\n".join(f"<<<{k}>>>\n{v}" for k, v in batch)
            for attempt in range(3):
                try:
                    translated = translator.translate(body)
                    break
                except Exception as exc:  # pragma: no cover - network dependent
                    if attempt == 2:
                        print(f"WARN: translation failed for batch {idx}/{len(batches)}: {exc}")
                        translated = ""
                    else:
                        time.sleep(1.5 * (attempt + 1))
            if translated:
                # Parse text between preserved markers.
                marker_re = re.compile(r"<<<([^>]+)>>>")
                matches = list(marker_re.finditer(translated))
                for m_i, m in enumerate(matches):
                    key = m.group(1)
                    start = m.end()
                    end = matches[m_i + 1].start() if m_i + 1 < len(matches) else len(translated)
                    val = translated[start:end].strip()
                    store[key] = val
            save_json(TRANSLATION_CACHE, cache)
            time.sleep(sleep_s)
    # fallback: keep English if translation unavailable
    return {k: store.get(k) or texts.get(k, "") for k in texts}


def write_catalogue_and_figure_md() -> list[dict]:
    data = json.loads(INVENTORY.read_text(encoding="utf-8"))
    records = list(iter_records(data))

    CATALOGUE_CSV.parent.mkdir(parents=True, exist_ok=True)
    with CATALOGUE_CSV.open("w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=list(records[0].keys()))
        writer.writeheader()
        writer.writerows(records)

    context_texts = {
        hashlib.sha1((r["nearest_heading"] + "\n" + r["context_en"]).encode("utf-8")).hexdigest()[:12]:
        " / ".join(x for x in [r["nearest_heading"], r["context_en"]] if x)
        for r in records
        if r["nearest_heading"] or r["context_en"]
    }
    context_ja_by_hash = google_translate_many(context_texts, "figure_contexts")
    for r in records:
        key = hashlib.sha1((r["nearest_heading"] + "\n" + r["context_en"]).encode("utf-8")).hexdigest()[:12]
        r["context_ja"] = context_ja_by_hash.get(key, "")

    counts_by_page: dict[str, dict[str, int]] = {}
    counts_by_phase: dict[str, int] = {}
    for r in records:
        d = counts_by_page.setdefault(r["page_href"], {"figure": 0, "standalone_image": 0, "table": 0})
        d[r["kind"]] += 1
        counts_by_phase[r["workflow_phase"]] = counts_by_phase.get(r["workflow_phase"], 0) + 1

    lines: list[str] = []
    lines += [
        "# Bayesian Workflow：図表抽出ベースの実務解説",
        "",
        "## 0. 出典・権利方針",
        "",
        f"- 公式公開サイト: <{SITE_BASE}>",
        f"- 公式リポジトリ: <{OFFICIAL_REPO}> / 確認コミット `{OFFICIAL_COMMIT}`",
        "- 公式サイトの `index.qmd` は `Published by CRC Press in 2026. Copyright by the authors.` と明記している。リポジトリ直下に本文・図表再配布を許す明示LICENSEは見つからなかった。",
        "- そのため、このMarkdownではCRC Press版/公式サイトの画像バイナリをコピーせず、公式ページへのリンク・図表ID・caption/周辺文脈・実務上の読み方を記録する。",
        "- 本ファイルは翻訳本文ではなく、図表カタログと実務解説である。逐語本文訳は `02_four_line_chunk_translation_arxiv2011.md` 側で、CC-BY 4.0 のarXiv論文版を対象にした。",
        "",
        "## 1. 抽出サマリー",
        "",
        f"- 調査ページ数: **{len(data)}ページ**",
        f"- 図: **{sum(1 for r in records if r['kind']=='figure')}件**",
        f"- 単独画像: **{sum(1 for r in records if r['kind']=='standalone_image')}件**",
        f"- HTML表: **{sum(1 for r in records if r['kind']=='table')}件**",
        f"- 合計: **{len(records)}件**",
        f"- 機械可読カタログ: [`data/official_site_figures_tables_catalogue.csv`](data/official_site_figures_tables_catalogue.csv)",
        f"- 元インベントリJSON: [`figure_table_inventory.json`](figure_table_inventory.json)",
        "",
        "## 2. 図表から逆算した Bayesian Workflow の実務構造",
        "",
        "| フェーズ | 件数 | 実務での読み方 | MLflowで紐づけるもの |",
        "|---|---:|---|---|",
    ]
    for phase, count in sorted(counts_by_phase.items(), key=lambda kv: (-kv[1], kv[0])):
        lines.append(f"| {phase} | {count} | {PRACTICAL_READING[phase]} | `{MLFLOW_LINKS[phase]}` |")

    lines += [
        "",
        "## 3. ケーススタディ別の図表量",
        "",
        "| ページ | 図 | 単独画像 | 表 | 主な用途 |",
        "|---|---:|---:|---:|---|",
    ]
    for page in data:
        href = clean_text(page.get("href"))
        d = counts_by_page.get(href, {"figure": 0, "standalone_image": 0, "table": 0})
        if sum(d.values()) == 0:
            continue
        page_records = [r for r in records if r["page_href"] == href]
        top_phase = max({r["workflow_phase"] for r in page_records}, key=lambda p: sum(rr["workflow_phase"] == p for rr in page_records))
        url = clean_text(page.get("url"))
        title = clean_text(page.get("h1") or page.get("title"))
        lines.append(f"| [{title}]({url}) | {d['figure']} | {d['standalone_image']} | {d['table']} | {top_phase} |")

    lines += [
        "",
        "## 4. 全図表カタログと実務メモ",
        "",
        "各項目は `local_id` を安定参照IDとして使う。captionが `Figure N` だけの項目は、見出し・直前文・コードchunk由来の文脈で意味づけしている。",
        "",
    ]

    current_page = None
    for r in records:
        if r["page_href"] != current_page:
            current_page = r["page_href"]
            title = r["h1"] or r["page_title"]
            lines += [
                f"### {title}",
                "",
                f"- ページ: <{SITE_BASE}{current_page}>",
                f"- ソース候補: <{source_repo_url({'href': current_page})}>",
                "",
            ]
        label = r["official_caption_or_headers"] or r["official_id"] or f"{r['kind']} {r['ordinal_in_page']}"
        label = label.replace("|", "\\|")
        context_en = r["context_en"] or r["nearest_heading"] or "(context not available)"
        context_en = context_en.replace("|", "\\|")
        context_ja = r.get("context_ja") or "（自動翻訳なし。公式ページの前後文を参照）"
        context_ja = context_ja.replace("|", "\\|")
        lines += [
            f"#### `{r['local_id']}`",
            "",
            f"- 種別: `{r['kind']}` / 公式ID: `{r['official_id'] or '(none)'}` / ページ内順序: {r['ordinal_in_page']}",
            f"- caption/列: {label}",
            f"- 周辺文脈（EN）: {context_en}",
            f"- 周辺文脈（JA, 自動訳）: {context_ja}",
            f"- Workflowフェーズ: **{r['workflow_phase']}**",
            f"- 実務での読み方: {r['practical_reading_ja']}",
            f"- MLflow連携: `{r['mlflow_links']}`",
            f"- 参照: [公式ページ]({r['source_page_url']}) / [ソース候補]({r['source_repo_url']})",
            "",
        ]

    write_text_lf(FIG_MD, "\n".join(line.rstrip() for line in lines).rstrip() + "\n")
    return records


def clean_arxiv_lines() -> list[str]:
    raw = ARXIV_TEXT.read_text(encoding="utf-8", errors="replace").splitlines()
    lines: list[str] = []
    for line in raw:
        s = clean_text(line)
        if not s:
            continue
        if re.match(r"^--- PAGE \d+ ---$", s):
            continue
        # Remove standalone page numbers and arXiv header fragments. Keep section numbers with titles.
        if re.match(r"^\d+$", s):
            continue
        if s.startswith("arXiv:2011.01808"):
            continue
        if s in {"Contents", "References"}:
            lines.append(s)
            continue
        lines.append(s)
    return lines


def terms_for(text: str) -> list[str]:
    found: list[str] = []
    lower = text.lower()
    for term, desc in TERMS.items():
        if term.lower() in lower:
            found.append(f"- **{term}**: {desc}")
        if len(found) >= 6:
            break
    if not found:
        return ["- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）"]
    return found


def summarize_ja(translation: str) -> str:
    s = re.sub(r"\s+", " ", translation).strip()
    if not s:
        return "（翻訳未取得のため、英文を参照。）"
    # First Japanese sentence-ish, capped.
    parts = re.split(r"(?<=[。！？])", s)
    summary = parts[0].strip() if parts else s
    if len(summary) > 120:
        summary = summary[:117] + "…"
    return summary


def write_translation_md() -> int:
    lines = clean_arxiv_lines()
    chunks = [lines[i:i + 4] for i in range(0, len(lines), 4)]
    chunk_texts = {f"ARXIV_CHUNK_{i:04d}": "\n".join(chunk) for i, chunk in enumerate(chunks, 1)}
    translations = google_translate_many(chunk_texts, "arxiv_chunks")

    out: list[str] = [
        "# Bayesian Workflow arXiv版：4行ごとの英文・日本語訳・熟語解説・要約",
        "",
        "## 出典・ライセンス・範囲",
        "",
        f"- 対象本文: Andrew Gelman et al., *Bayesian Workflow*, arXiv:2011.01808, <{ARXIV_ABS}> / PDF <{ARXIV_PDF}>",
        f"- arXivページで確認できるライセンス: CC BY 4.0 <{ARXIV_LICENSE}>",
        "- 本ファイルは **CRC Press 2026年版の本文逐語訳ではない**。公式書籍サイト/CRC版には著作権表示があるため、本文訳はCC-BY 4.0のarXiv論文版を対象にした。",
        "- 日本語訳は `deep-translator` の Google Translate と、長文処理用の Argos Translate（en→ja）を併用して作成した自動翻訳初版。実務利用前に、数式・図番号・専門語・否定表現を原PDFで確認すること。",
        "- PDF抽出由来の改行を4行単位で機械的に区切っているため、文がチャンクをまたぐ場合がある。",
        f"- チャンク数: **{len(chunks)}**",
        "",
        "## 読み方",
        "",
        "1. `English`で原文位置を確認する。",
        "2. `日本語訳`で意味をつかむ。",
        "3. `熟語・専門語`を実務語彙としてメモする。",
        "4. `要約`だけを追うと、全体の流れを高速に復習できる。",
        "",
    ]

    for i, chunk in enumerate(chunks, 1):
        key = f"ARXIV_CHUNK_{i:04d}"
        src = chunk_texts[key]
        ja = translations.get(key, "")
        out += [
            f"## Chunk {i:04d}",
            "",
            "### English（抽出4行）",
            "",
        ]
        out += [f"> {line}" for line in chunk]
        out += [
            "",
            "### 日本語訳（自動翻訳）",
            "",
        ]
        out += [f"> {line.strip()}" for line in ja.splitlines() if line.strip()]
        out += [
            "",
            "### 熟語・専門語",
            "",
            *terms_for(src),
            "",
            "### 要約",
            "",
            f"- {summarize_ja(ja)}",
            "",
        ]

    write_text_lf(TRANS_MD, "\n".join(line.rstrip() for line in out).rstrip() + "\n")
    return len(chunks)


def write_mlflow_guide() -> None:
    write_text_lf(MLFLOW_MD, textwrap.dedent(f"""
    # Bayesian WorkflowをMLflowで実装・運用するためのガイド

    ## 0. 目的

    Bayesian Workflowの実務化では、**一つの最終モデルだけを保存する**のでは足りない。重要なのは、失敗モデル・priorの試行錯誤・MCMC診断・PPC・LOO比較・SBC・意思決定までを、あとから追跡できる形で残すこと。本ガイドでは、Stan/R/brms/Pythonの実験をMLflowで管理するための最小設計を示す。

    参照元:

    - 公式書籍サイト: <{SITE_BASE}>
    - 公式コードリポジトリ: <{OFFICIAL_REPO}>
    - 本文精読用のCC-BY arXiv版: <{ARXIV_ABS}>

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
        with mlflow.start_run(run_name=f"{{phase}}/{{model_id}}") as run:
            mlflow.set_tags({{
                'bw.phase': phase,
                'bw.model_id': model_id,
                'bw.status': 'candidate',
                **(tags or {{}}),
            }})
            mlflow.log_params({{
                'data_uri': data_uri,
                'model_file': str(model_file),
                'model_code_hash': file_sha256(model_file),
                **sampler_config,
            }})
            mlflow.log_text(json.dumps(prior_spec, ensure_ascii=False, indent=2), 'model/priors.json')
            mlflow.log_metrics({{k: float(v) for k, v in metrics.items() if v is not None}})
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
    """).strip() + "\n")


def write_readme(records: list[dict], chunks: int) -> None:
    write_text_lf(README, textwrap.dedent(f"""
    # bys_workflow

    Bayesian Workflowを実務で使うための日本語ワークスペースです。

    ## 作成ファイル

    - [`01_figures_tables_explanation.md`](01_figures_tables_explanation.md)  
      公式書籍サイト/公式リポジトリから抽出した全図表インベントリ（図384件、単独画像1件、表78件、合計{len(records)}件）を、Workflowフェーズ・実務上の読み方・MLflow連携観点つきで整理。
    - [`02_four_line_chunk_translation_arxiv2011.md`](02_four_line_chunk_translation_arxiv2011.md)  
      CC-BY 4.0のarXiv論文版 `Bayesian Workflow` を、4行ごとに英文・日本語訳・熟語/専門語・要約で整理（{chunks} chunks）。CRC Press版の本文逐語訳ではありません。
    - [`03_mlflow_implementation_guide.md`](03_mlflow_implementation_guide.md)  
      Bayesian WorkflowをMLflowで実装・監査・比較するためのrun設計、tags/params/metrics/artifacts、実装スケルトン、判定チェックリスト。
    - [`data/official_site_figures_tables_catalogue.csv`](data/official_site_figures_tables_catalogue.csv)  
      公式サイト図表の機械可読カタログ。
    - [`figure_table_inventory.json`](figure_table_inventory.json)  
      公式サイトHTMLから抽出した元インベントリ。
    - [`assets/arxiv_images/`](assets/arxiv_images/)  
      CC-BY 4.0のarXiv PDFから抽出した画像素材。公式CRC書籍サイトの画像コピーではありません。

    ## 権利方針

    - 公式書籍サイト: <{SITE_BASE}> は `Published by CRC Press in 2026. Copyright by the authors.` と表示しています。公式サイト図表は画像バイナリを再配布せず、リンク・ID・周辺文脈・解説のみを保存しています。
    - 本文の4行訳は、arXiv:2011.01808 のCC-BY 4.0版 <{ARXIV_ABS}> を対象にしています。
    - `assets/arxiv_images/` の画像も同じarXiv版から抽出しています。利用時は原著者・arXiv ID・CC BY 4.0を明記してください。
    - 自動翻訳初版なので、引用・公開・業務判断に使う前に原文PDFと照合してください。

    ## 再生成

    ```bash
    python bys_workflow/scripts/build_bys_workflow_docs.py
    ```

    `deep-translator` または `argostranslate` が利用可能な環境では、日本語訳キャッシュを更新します。ネットワークが使えない場合は、既存のMarkdownを参照してください。
    """).strip() + "\n")


def main() -> None:
    ROOT.mkdir(parents=True, exist_ok=True)
    (ROOT / "data").mkdir(parents=True, exist_ok=True)
    records = write_catalogue_and_figure_md()
    chunks = write_translation_md()
    write_mlflow_guide()
    write_readme(records, chunks)
    print(f"wrote {FIG_MD.relative_to(ROOT.parent)}")
    print(f"wrote {TRANS_MD.relative_to(ROOT.parent)}")
    print(f"wrote {MLFLOW_MD.relative_to(ROOT.parent)}")
    print(f"wrote {README.relative_to(ROOT.parent)}")
    print(f"records={len(records)} chunks={chunks}")


if __name__ == "__main__":
    main()
