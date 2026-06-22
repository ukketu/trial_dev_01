# bys_workflow

Bayesian Workflowを実務で使うための日本語ワークスペースです。

## 作成ファイル

- [`01_figures_tables_explanation.md`](01_figures_tables_explanation.md)  
  公式書籍サイト/公式リポジトリから抽出した全図表インベントリ（図384件、単独画像1件、表78件、合計463件）を、Workflowフェーズ・実務上の読み方・MLflow連携観点つきで整理。
- [`02_four_line_chunk_translation_arxiv2011.md`](02_four_line_chunk_translation_arxiv2011.md)  
  CC-BY 4.0のarXiv論文版 `Bayesian Workflow` を、4行ごとに英文・日本語訳・熟語/専門語・要約で整理（806 chunks）。CRC Press版の本文逐語訳ではありません。
- [`03_mlflow_implementation_guide.md`](03_mlflow_implementation_guide.md)  
  Bayesian WorkflowをMLflowで実装・監査・比較するためのrun設計、tags/params/metrics/artifacts、実装スケルトン、判定チェックリスト。
- [`data/official_site_figures_tables_catalogue.csv`](data/official_site_figures_tables_catalogue.csv)  
  公式サイト図表の機械可読カタログ。
- [`figure_table_inventory.json`](figure_table_inventory.json)  
  公式サイトHTMLから抽出した元インベントリ。
- [`assets/arxiv_images/`](assets/arxiv_images/)  
  CC-BY 4.0のarXiv PDFから抽出した画像素材。公式CRC書籍サイトの画像コピーではありません。

## 権利方針

- 公式書籍サイト: <https://avehtari.github.io/Bayesian-Workflow/> は `Published by CRC Press in 2026. Copyright by the authors.` と表示しています。公式サイト図表は画像バイナリを再配布せず、リンク・ID・周辺文脈・解説のみを保存しています。
- 本文の4行訳は、arXiv:2011.01808 のCC-BY 4.0版 <https://arxiv.org/abs/2011.01808> を対象にしています。
- `assets/arxiv_images/` の画像も同じarXiv版から抽出しています。利用時は原著者・arXiv ID・CC BY 4.0を明記してください。
- 自動翻訳初版なので、引用・公開・業務判断に使う前に原文PDFと照合してください。

## 再生成

```bash
python bys_workflow/scripts/build_bys_workflow_docs.py
```

`deep-translator` または `argostranslate` が利用可能な環境では、日本語訳キャッシュを更新します。ネットワークが使えない場合は、既存のMarkdownを参照してください。
