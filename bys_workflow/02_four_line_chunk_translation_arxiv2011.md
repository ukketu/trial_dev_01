# Bayesian Workflow arXiv版：4行ごとの英文・日本語訳・熟語解説・要約

## 出典・ライセンス・範囲

- 対象本文: Andrew Gelman et al., *Bayesian Workflow*, arXiv:2011.01808, <https://arxiv.org/abs/2011.01808> / PDF <https://arxiv.org/pdf/2011.01808>
- arXivページで確認できるライセンス: CC BY 4.0 <https://creativecommons.org/licenses/by/4.0/>
- 本ファイルは **CRC Press 2026年版の本文逐語訳ではない**。公式書籍サイト/CRC版には著作権表示があるため、本文訳はCC-BY 4.0のarXiv論文版を対象にした。
- 日本語訳は `deep-translator` の Google Translate と、長文処理用の Argos Translate（en→ja）を併用して作成した自動翻訳初版。実務利用前に、数式・図番号・専門語・否定表現を原PDFで確認すること。
- PDF抽出由来の改行を4行単位で機械的に区切っているため、文がチャンクをまたぐ場合がある。
- チャンク数: **806**

## 読み方

1. `English`で原文位置を確認する。
2. `日本語訳`で意味をつかむ。
3. `熟語・専門語`を実務語彙としてメモする。
4. `要約`だけを追うと、全体の流れを高速に復習できる。

## Chunk 0001

### English（抽出4行）

> Bayesian workﬂow∗
> Andrew Gelman†
> Aki Vehtari‡
> Daniel Simpson§

### 日本語訳（自動翻訳）

> ベイジアンワークフロー∗
> アンドリュー・ゲルマン†
> アキ・ヴェフタリ‡
> ダニエル・シンプソン§

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- ベイジアンワークフロー∗ アンドリュー・ゲルマン† アキ・ヴェフタリ‡ ダニエル・シンプソン§

## Chunk 0002

### English（抽出4行）

> Charles C. Margossian†
> Bob Carpenter¶
> Yuling Yao†
> Lauren Kennedy‖

### 日本語訳（自動翻訳）

> チャールズ・C・マーゴシアン†
> ボブ・カーペンター¶
> ヤオ・ユーリン†
> ローレン・ケネディ」

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- チャールズ・C・マーゴシアン† ボブ・カーペンター¶ ヤオ・ユーリン† ローレン・ケネディ」

## Chunk 0003

### English（抽出4行）

> Jonah Gabry†
> Paul-Christian Bürkner∗∗
> Martin Modrák††
> 2 Nov 2020

### 日本語訳（自動翻訳）

> ジョナ・ゲイブリー†
> パウル・クリスチャン・ビュルクナー∗∗
> マルティン・モドラク††
> 2020 年 11 月 2 日

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- ジョナ・ゲイブリー† パウル・クリスチャン・ビュルクナー∗∗ マルティン・モドラク†† 2020 年 11 月 2 日

## Chunk 0004

### English（抽出4行）

> Abstract
> The Bayesian approach to data analysis provides a powerful way to handle uncertainty in all
> observations, model parameters, and model structure using probability theory. Probabilistic
> programming languages make it easier to specify and ﬁt Bayesian models, but this still leaves

### 日本語訳（自動翻訳）

> 要約
> データ分析に対するベイジアン アプローチは、すべての不確実性を処理する強力な方法を提供します。
> 確率論を使用した観測値、モデル パラメーター、モデル構造。確率的
> プログラミング言語を使用すると、ベイジアン モデルの指定と適合が容易になりますが、それでも問題は残ります。

### 熟語・専門語

- **uncertainty**: 不確実性。観測・パラメータ・モデル構造・意思決定に残る曖昧さ。

### 要約

- 要約 データ分析に対するベイジアン アプローチは、すべての不確実性を処理する強力な方法を提供します。

## Chunk 0005

### English（抽出4行）

> us with many options regarding constructing, evaluating, and using these models, along with
> many remaining challenges in computation.
> Using Bayesian inference to solve real-world
> problems requires not only statistical skills, subject matter knowledge, and programming, but

### 日本語訳（自動翻訳）

> これらのモデルの構築、評価、使用に関して多くのオプションが用意されています。
> 計算には多くの課題が残されています。
> ベイズ推論を使用して現実世界を解決する
> 問題を解決するには、統計スキル、主題の知識、プログラミングだけでなく、

### 熟語・専門語

- **Bayesian inference**: ベイズ推論。事前分布と尤度から事後分布を計算する中核処理。

### 要約

- これらのモデルの構築、評価、使用に関して多くのオプションが用意されています。

## Chunk 0006

### English（抽出4行）

> also awareness of the decisions made in the process of data analysis. All of these aspects
> can be understood as part of a tangled workﬂow of applied Bayesian statistics.
> Beyond
> inference, the workﬂow also includes iterative model building, model checking, validation and

### 日本語訳（自動翻訳）

> また、データ分析の過程で行われた意思決定についても認識します。これらすべての側面
> 応用ベイズ統計の複雑なワークフローの一部として理解できます。
> ビヨンド
> 推論のワークフローには、反復的なモデル構築、モデルのチェック、検証、および

### 熟語・専門語

- **model checking**: モデルチェック。モデルの仮定・予測・計算結果がデータや目的に合うか検査すること。
- **ESS**: 有効サンプルサイズ。自己相関を考慮した独立サンプル相当数。
- **validation**: 検証。モデルが目的・データ・外部知識に照らして妥当かを確認すること。
- **model building**: モデル構築。仮定・データ構造・prior・likelihoodを組み合わせる工程。
- **decision**: 意思決定。予測分布を損失・効用・行動選択へ接続する工程。

### 要約

- また、データ分析の過程で行われた意思決定についても認識します。

## Chunk 0007

### English（抽出4行）

> troubleshooting of computational problems, model understanding, and model comparison. We
> review all these aspects of workﬂow in the context of several examples, keeping in mind that
> in practice we will be ﬁtting many models for any given problem, even if only a subset of them
> will ultimately be relevant for our conclusions.

### 日本語訳（自動翻訳）

> 計算上の問題のトラブルシューティング、モデルの理解、モデルの比較。私たち
> 以下の点に留意しながら、ワークフローのこれらすべての側面をいくつかの例に基づいて確認してください。
> 実際には、たとえモデルのサブセットであっても、特定の問題に対して多くのモデルを適合させることになります。
> 最終的には私たちの結論に関係します。

### 熟語・専門語

- **model comparison**: モデル比較。LOO-CVなどで複数モデルの予測性能や弱点を比較すること。
- **troubleshooting**: トラブルシュート。計算・モデル・データの失敗原因を切り分けること。

### 要約

- 計算上の問題のトラブルシューティング、モデルの理解、モデルの比較。

## Chunk 0008

### English（抽出4行）

> Contents
> Introduction
> 1.1
> From Bayesian inference to Bayesian workﬂow

### 日本語訳（自動翻訳）

> 内容
> はじめに
> 1.1
> ベイズ推論からベイズ ワークフローへ

### 熟語・専門語

- **Bayesian inference**: ベイズ推論。事前分布と尤度から事後分布を計算する中核処理。

### 要約

- 内容 はじめに 1.1 ベイズ推論からベイズ ワークフローへ

## Chunk 0009

### English（抽出4行）

> . . . . . . . . . . . . . . . . . . .
> 1.2
> Why do we need a Bayesian workﬂow? . . . . . . . . . . . . . . . . . . . . . . . .
> 1.3

### 日本語訳（自動翻訳）

> 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。
> 1.2
> なぜベイズ ワークフローが必要なのでしょうか? 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。
> 1.3

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- 。

## Chunk 0010

### English（抽出4行）

> “Workﬂow” and its relation to statistical theory and practice
> . . . . . . . . . . . .
> 1.4
> Organizing the many aspects of Bayesian workﬂow . . . . . . . . . . . . . . . . .

### 日本語訳（自動翻訳）

> 「ワークフロー」と統計理論および実践との関係
> 。 。 。 。 。 。 。 。 。 。 。 。
> 1.4
> ベイジアン ワークフローのさまざまな側面を整理します。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- 「ワークフロー」と統計理論および実践との関係 。

## Chunk 0011

### English（抽出4行）

> 1.5
> Aim and structure of this article
> . . . . . . . . . . . . . . . . . . . . . . . . . . .
> ∗We thank Berna Devezer, Danielle Navarro, Matthew West, and Ben Bales for helpful suggestions and the National

### 日本語訳（自動翻訳）

> 1.5
> この記事の目的と構成
> 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。
> ∗有益な提案をしてくれた Berna Devezer、Danielle Navarro、Matthew West、Ben Bales に感謝します。

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- 1.5 この記事の目的と構成 。

## Chunk 0012

### English（抽出4行）

> Science Foundation, Institute of Education Sciences, Oﬃce of Naval Research, National Institutes of Health, Sloan
> Foundation, Schmidt Futures, the Canadian Research Chairs program, and the Natural Sciences and Engineering
> Research Council of Canada for ﬁnancial support. This work was supported by ELIXIR CZ research infrastructure
> project (MEYS Grant No. LM2015047) including access to computing and storage facilities. Much of Sections 10 and

### 日本語訳（自動翻訳）

> 科学財団、教育科学研究所、海軍研究局、国立衛生研究所、スローン
> 財団、シュミット フューチャーズ、カナダ研究椅子プログラム、自然科学工学
> カナダ研究評議会による資金援助。この研究はELIXIR CZ研究インフラストラクチャによってサポートされました
> プロジェクト (MEYS 助成金番号 LM2015047) には、コンピューティングおよびストレージ施設へのアクセスが含まれます。セクション 10 と

### 熟語・専門語

- **ESS**: 有効サンプルサイズ。自己相関を考慮した独立サンプル相当数。

### 要約

- 科学財団、教育科学研究所、海軍研究局、国立衛生研究所、スローン 財団、シュミット フューチャーズ、カナダ研究椅子プログラム、自然科学工学 カナダ研究評議会による資金援助。

## Chunk 0013

### English（抽出4行）

> 11 are taken from Gelman (2019) and Margossian and Gelman (2020), respectively.
> †Department of Statistics, Columbia University, New York.
> ‡Department of Computer Science, Aalto University, Espoo, Finland.
> §Department of Statistical Sciences, University of Toronto.

### 日本語訳（自動翻訳）

> 11 はそれぞれ、Gelman (2019) および Margossian and Gelman (2020) から引用されています。
> †コロンビア大学統計学部、ニューヨーク州。
> ‡フィンランド、エスポーのアアルト大学コンピューターサイエンス学部。
> §トロント大学統計科学部。

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- 11 はそれぞれ、Gelman (2019) および Margossian and Gelman (2020) から引用されています。

## Chunk 0014

### English（抽出4行）

> ¶Center for Computational Mathematics, Flatiron Institute, New York.
> ‖Monash University, Melbourne, Australia.
> ∗∗Cluster of Excellence SimTech, University of Stuttgart, Germany.
> ††Institute of Microbiology of the Czech Academy of Sciences.

### 日本語訳（自動翻訳）

> ¶計算数学センター、フラットアイアン研究所、ニューヨーク。
> モナシュ大学、メルボルン、オーストラリア。
> ∗∗Cluster of Excellence SimTech、シュトゥットガルト大学、ドイツ。
> ††チェコ科学アカデミー微生物研究所。

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- ¶計算数学センター、フラットアイアン研究所、ニューヨーク。

## Chunk 0015

### English（抽出4行）

> Before ﬁtting a model
> 2.1
> Choosing an initial model . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
> 2.2

### 日本語訳（自動翻訳）

> モデルをフィッティングする前に
> 2.1
> 初期モデルの選択。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。
> 2.2

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- モデルをフィッティングする前に 2.1 初期モデルの選択。

## Chunk 0016

### English（抽出4行）

> Modular construction . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
> 2.3
> Scaling and transforming the parameters . . . . . . . . . . . . . . . . . . . . . . .
> 2.4

### 日本語訳（自動翻訳）

> モジュール構造。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。
> 2.3
> パラメータのスケーリングと変換。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。
> 2.4

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- モジュール構造。

## Chunk 0017

### English（抽出4行）

> Prior predictive checking . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
> 2.5
> Generative and partially generative models . . . . . . . . . . . . . . . . . . . . . .
> Fitting a model

### 日本語訳（自動翻訳）

> 事前の予測チェック。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。
> 2.5
> 生成モデルおよび部分生成モデル。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。
> モデルのフィッティング

### 熟語・専門語

- **prior predictive**: 事前予測。データを見る前のpriorだけで生成される予測分布を確認する診断。
- **generative model**: 生成モデル。データ生成過程を確率的に記述するモデル。

### 要約

- 事前の予測チェック。

## Chunk 0018

### English（抽出4行）

> 3.1
> Initial values, adaptation, and warmup . . . . . . . . . . . . . . . . . . . . . . . .
> 3.2
> How long to run an iterative algorithm . . . . . . . . . . . . . . . . . . . . . . . .

### 日本語訳（自動翻訳）

> 3.1
> 初期値、適応、およびウォームアップ。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。
> 3.2
> 反復アルゴリズムを実行する時間。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- 3.1 初期値、適応、およびウォームアップ。

## Chunk 0019

### English（抽出4行）

> 3.3
> Approximate algorithms and approximate models . . . . . . . . . . . . . . . . . .
> 3.4
> Fit fast, fail fast . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

### 日本語訳（自動翻訳）

> 3.3
> 近似アルゴリズムと近似モデル。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。
> 3.4
> 素早くフィットし、素早く失敗します。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。

### 熟語・専門語

- **approximate**: 近似。速度や扱いやすさのため、正確な推論・モデルを緩めること。

### 要約

- 3.3 近似アルゴリズムと近似モデル。

## Chunk 0020

### English（抽出4行）

> Using constructed data to ﬁnd and understand problems
> 4.1
> Fake-data simulation
> . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

### 日本語訳（自動翻訳）

> 構築されたデータを使用して問題を発見し、理解する
> 4.1
> 偽データのシミュレーション
> 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- 構築されたデータを使用して問題を発見し、理解する 4.1 偽データのシミュレーション 。

## Chunk 0021

### English（抽出4行）

> 4.2
> Simulation-based calibration . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
> 4.3
> Experimentation using constructed data

### 日本語訳（自動翻訳）

> 4.2
> シミュレーションベースのキャリブレーション。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。
> 4.3
> 構築したデータを用いた実験

### 熟語・専門語

- **simulation-based calibration**: SBC。シミュレーション真値と事後rankを比べ、実装・推論の校正を検査する方法。

### 要約

- 4.2 シミュレーションベースのキャリブレーション。

## Chunk 0022

### English（抽出4行）

> . . . . . . . . . . . . . . . . . . . . . . .
> Addressing computational problems
> 5.1
> The folk theorem of statistical computing

### 日本語訳（自動翻訳）

> 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。
> 計算上の問題に対処する
> 5.1
> 統計計算の民間定理

### 熟語・専門語

- **ESS**: 有効サンプルサイズ。自己相関を考慮した独立サンプル相当数。

### 要約

- 。

## Chunk 0023

### English（抽出4行）

> . . . . . . . . . . . . . . . . . . . . . .
> 5.2
> Starting at simple and complex models and meeting in the middle
> . . . . . . . . .

### 日本語訳（自動翻訳）

> 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。
> 5.2
> 単純なモデルと複雑なモデルから始めて途中で出会う
> 。 。 。 。 。 。 。 。 。

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- 。

## Chunk 0024

### English（抽出4行）

> 5.3
> Getting a handle on models that take a long time to ﬁt . . . . . . . . . . . . . . . .
> 5.4
> Monitoring intermediate quantities . . . . . . . . . . . . . . . . . . . . . . . . . .

### 日本語訳（自動翻訳）

> 5.3
> 適合に時間がかかるモデルを把握する。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。
> 5.4
> 中間量の監視。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- 5.3 適合に時間がかかるモデルを把握する。

## Chunk 0025

### English（抽出4行）

> 5.5
> Stacking to reweight poorly mixing chains . . . . . . . . . . . . . . . . . . . . . .
> 5.6
> Posterior distributions with multimodality and other diﬃcult geometry . . . . . . .

### 日本語訳（自動翻訳）

> 5.5
> 混合が不十分なチェーンの重みを再調整するためのスタッキング。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。
> 5.6
> 多峰性およびその他の困難な幾何学を備えた事後分布。 。 。 。 。 。 。

### 熟語・専門語

- **posterior distribution**: 事後分布。データ観測後の未知量の不確実性を表す分布。
- **multimodality**: 多峰性。事後分布に複数の山があり、MCMCが混合しにくい状態。

### 要約

- 5.5 混合が不十分なチェーンの重みを再調整するためのスタッキング。

## Chunk 0026

### English（抽出4行）

> 5.7
> Reparameterization . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
> 5.8
> Marginalization . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

### 日本語訳（自動翻訳）

> 5.7
> 再パラメータ化。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。
> 5.8
> 疎外化。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。

### 熟語・専門語

- **reparameterization**: 再パラメータ化。計算しやすい幾何に変えるためのパラメータ表現変更。

### 要約

- 5.7 再パラメータ化。

## Chunk 0027

### English（抽出4行）

> 5.9
> Adding prior information . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
> 5.10 Adding data . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
> Evaluating and using a ﬁtted model

### 日本語訳（自動翻訳）

> 5.9
> 事前情報を追加します。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。
> 5.10 データの追加。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。
> 適合モデルの評価と使用

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- 5.9 事前情報を追加します。

## Chunk 0028

### English（抽出4行）

> 6.1
> Posterior predictive checking . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
> 6.2
> Cross validation and inﬂuence of individual data points and subsets of the data . . .

### 日本語訳（自動翻訳）

> 6.1
> 事後予測チェック。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。
> 6.2
> 相互検証と、個々のデータ ポイントおよびデータのサブセットの影響。 。 。

### 熟語・専門語

- **posterior predictive**: 事後予測。推定後のモデルが観測データの特徴を再現できるかを見る診断。
- **cross validation**: 交差検証。汎化性能を推定するためにデータを分割/近似除外する評価法。
- **validation**: 検証。モデルが目的・データ・外部知識に照らして妥当かを確認すること。

### 要約

- 6.1 事後予測チェック。

## Chunk 0029

### English（抽出4行）

> 6.3
> Inﬂuence of prior information
> . . . . . . . . . . . . . . . . . . . . . . . . . . . .
> 6.4

### 日本語訳（自動翻訳）

> 6.3
> 事前情報の影響
> 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。
> 6.4

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- 6.3 事前情報の影響 。

## Chunk 0030

### English（抽出4行）

> Summarizing inference and propagating uncertainty . . . . . . . . . . . . . . . . .
> Modifying a model
> 7.1
> Constructing a model for the data . . . . . . . . . . . . . . . . . . . . . . . . . . .

### 日本語訳（自動翻訳）

> 推論を要約し、不確実性を伝播します。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。
> モデルの変更
> 7.1
> データのモデルを構築します。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。

### 熟語・専門語

- **uncertainty**: 不確実性。観測・パラメータ・モデル構造・意思決定に残る曖昧さ。

### 要約

- 推論を要約し、不確実性を伝播します。

## Chunk 0031

### English（抽出4行）

> 7.2
> Incorporating additional data . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
> 7.3
> Working with prior distributions . . . . . . . . . . . . . . . . . . . . . . . . . . .

### 日本語訳（自動翻訳）

> 7.2
> 追加データの組み込み。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。
> 7.3
> 以前のディストリビューションを使用して作業する。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。

### 熟語・専門語

- **prior distribution**: 事前分布。データ観測前の知識・制約を表す分布。

### 要約

- 7.2 追加データの組み込み。

## Chunk 0032

### English（抽出4行）

> 7.4
> A topology of models . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
> Understanding and comparing multiple models
> 8.1

### 日本語訳（自動翻訳）

> 7.4
> モデルのトポロジ。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。
> 複数のモデルの理解と比較
> 8.1

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- 7.4 モデルのトポロジ。

## Chunk 0033

### English（抽出4行）

> Visualizing models in relation to each other . . . . . . . . . . . . . . . . . . . . .
> 8.2
> Cross validation and model averaging
> . . . . . . . . . . . . . . . . . . . . . . . .

### 日本語訳（自動翻訳）

> モデルを相互に関連付けて視覚化します。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。
> 8.2
> 相互検証とモデルの平均化
> 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。

### 熟語・専門語

- **cross validation**: 交差検証。汎化性能を推定するためにデータを分割/近似除外する評価法。
- **validation**: 検証。モデルが目的・データ・外部知識に照らして妥当かを確認すること。

### 要約

- モデルを相互に関連付けて視覚化します。

## Chunk 0034

### English（抽出4行）

> 8.3
> Comparing a large number of models
> . . . . . . . . . . . . . . . . . . . . . . . .
> Modeling as software development

### 日本語訳（自動翻訳）

> 8.3
> 多数のモデルを比較する
> 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。
> ソフトウェア開発としてのモデリング

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- 8.3 多数のモデルを比較する 。

## Chunk 0035

### English（抽出4行）

> 9.1
> Version control smooths collaborations with others and with your past self . . . . .
> 9.2
> Testing as you go . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

### 日本語訳（自動翻訳）

> 9.1
> バージョン管理により、他の人や過去の自分とのコラボレーションがスムーズになります。 。 。 。 。
> 9.2
> 進みながらテストします。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- 9.1 バージョン管理により、他の人や過去の自分とのコラボレーションがスムーズになります。

## Chunk 0036

### English（抽出4行）

> 9.3
> Making it essentially reproducible . . . . . . . . . . . . . . . . . . . . . . . . . .
> 9.4
> Making it readable and maintainable . . . . . . . . . . . . . . . . . . . . . . . . .

### 日本語訳（自動翻訳）

> 9.3
> 本質的に再現可能にする。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。
> 9.4
> 読みやすく、保守しやすいようにします。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。

### 熟語・専門語

- **ESS**: 有効サンプルサイズ。自己相関を考慮した独立サンプル相当数。

### 要約

- 9.3 本質的に再現可能にする。

## Chunk 0037

### English（抽出4行）

> 10 Example of workﬂow involving model building and expansion: Golf putting
> 10.1 First model: logistic regression . . . . . . . . . . . . . . . . . . . . . . . . . . . .
> 10.2 Modeling from ﬁrst principles
> . . . . . . . . . . . . . . . . . . . . . . . . . . . .

### 日本語訳（自動翻訳）

> 10 モデル構築と拡張のワークフロー例: ゴルフパッティング
> 10.1 最初のモデル: 記号論理的回帰 . . . . . . . . . . . . . . . . . . . . . . . . . . .
> 10.2 原則からモデリング
> . . . . . . . . . . . . . . . . . . . .

### 熟語・専門語

- **ESS**: 有効サンプルサイズ。自己相関を考慮した独立サンプル相当数。
- **model building**: モデル構築。仮定・データ構造・prior・likelihoodを組み合わせる工程。

### 要約

- 10 モデル構築と拡張のワークフロー例: ゴルフパッティング 10.1 最初のモデル: 記号論理的回帰 . . . . . . . . . . . . . . . . . . . . . . . . . . . 10.2 原則からモデ…

## Chunk 0038

### English（抽出4行）

> 10.3 Testing the ﬁtted model on new data . . . . . . . . . . . . . . . . . . . . . . . . .
> 10.4 A new model accounting for how hard the ball is hit . . . . . . . . . . . . . . . . .
> 10.5 Expanding the model by including a fudge factor
> . . . . . . . . . . . . . . . . . .

### 日本語訳（自動翻訳）

> 10.3 適合したモデルを新しいデータでテストする . . . . . . . . . . . . . . . . . . . . . .
> 10.4 ボールがどれだけ硬いかを占める新しいモデル . . . . . . . . . . . . . . .
> 10.5 汚泥係数を含むモデルを拡大
> . . . . . . . .

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- 10.3 適合したモデルを新しいデータでテストする . . . . . . . . . . . . . . . . . . . . . . 10.4 ボールがどれだけ硬いかを占める新しいモデル . . . . . . . . . . …

## Chunk 0039

### English（抽出4行）

> 10.6 General lessons from the golf example . . . . . . . . . . . . . . . . . . . . . . . .
> 11 Example of workﬂow for a model with unexpected multimodality: Planetary motion
> 11.1 Mechanistic model of motion . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
> 11.2 Fitting a simpliﬁed model . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

### 日本語訳（自動翻訳）

> . . . . . . . . . . . . . . . . . . . . . . . .
> 11 予期しない多項性を持つモデルのワークフローの例: 惑星の動き
> 11.1 動きの機械的モデル . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
> 11.2 簡略化されたモデル . . . . . . . . . . . . . . . . . . . . . . .

### 熟語・専門語

- **multimodality**: 多峰性。事後分布に複数の山があり、MCMCが混合しにくい状態。
- **ESS**: 有効サンプルサイズ。自己相関を考慮した独立サンプル相当数。

### 要約

- . . . . . . . . . . . . . . . . . . . . . . . . 11 予期しない多項性を持つモデルのワークフローの例: 惑星の動き 11.1 動きの機械的モデル . . . . . . . . . . …

## Chunk 0040

### English（抽出4行）

> 11.3 Bad Markov chain, slow Markov chain? . . . . . . . . . . . . . . . . . . . . . . .
> 11.4 Building up the model
> . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
> 11.5 General lessons from the planetary motion example . . . . . . . . . . . . . . . . .

### 日本語訳（自動翻訳）

> . . . . . . . . . . . . . . . . . . . . . . . . .
> 11.4 モデルを組み立てる
> . . . . . . . . . . . . . . . . . . . . . . . .
> . . . . . . . . . . . . . . . . . . .

### 熟語・専門語

- **ESS**: 有効サンプルサイズ。自己相関を考慮した独立サンプル相当数。
- **Markov chain**: マルコフ連鎖。MCMCで事後分布からサンプルを得るための確率過程。

### 要約

- . . . . . . . . . . . . . . . . . . . . . . . . . 11.4 モデルを組み立てる . . . . . . . . . . . . . . . . . . . . . . . . . . …

## Chunk 0041

### English（抽出4行）

> 12 Discussion
> 12.1 Diﬀerent perspectives on statistical modeling and prediction
> . . . . . . . . . . . .
> 12.2 Justiﬁcation of iterative model building

### 日本語訳（自動翻訳）

> 12 ディスカッション
> 12.1 統計モデリングと予測に関する異なる視点
> . . . . .
> 12.2 反復モデル構築の正当化

### 熟語・専門語

- **model building**: モデル構築。仮定・データ構造・prior・likelihoodを組み合わせる工程。
- **prediction**: 予測。未知/将来/除外データに対する分布や点推定。

### 要約

- 12 ディスカッション 12.1 統計モデリングと予測に関する異なる視点 . . . . . 12.2 反復モデル構築の正当化

## Chunk 0042

### English（抽出4行）

> . . . . . . . . . . . . . . . . . . . . . . .
> 12.3 Model selection and overﬁtting . . . . . . . . . . . . . . . . . . . . . . . . . . . .
> 12.4 Bigger datasets demand bigger models . . . . . . . . . . . . . . . . . . . . . . . .
> 12.5 Prediction, generalization, and poststratiﬁcation . . . . . . . . . . . . . . . . . . .

### 日本語訳（自動翻訳）

> . . . . . . . . . . . . . .
> 12.3 モデル選択とオーバーフィッティング . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
> 12.4 より大きいデータセットはより大きいモデルを要求します。 . . . . . . . . . . . . . . . . .
> . . . . . . .

### 熟語・専門語

- **prediction**: 予測。未知/将来/除外データに対する分布や点推定。

### 要約

- . . . . . . . . . . . . . . 12.3 モデル選択とオーバーフィッティング . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . …

## Chunk 0043

### English（抽出4行）

> 12.6 Going forward . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
> 1.
> Introduction
> 1.1.

### 日本語訳（自動翻訳）

> . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
> 1。
> 導入事例
> 1.1. .

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1。

## Chunk 0044

### English（抽出4行）

> From Bayesian inference to Bayesian workflow
> If mathematical statistics is to be the theory of applied statistics, then any serious discussion of
> Bayesian methods needs to be clear about how they are used in practice. In particular, we need to
> clearly separate concepts of Bayesian inference from Bayesian data analysis and, critically, from

### 日本語訳（自動翻訳）

> ベイジアンの推論からベイジアンワークフローまで
> 数学統計が適用される統計の理論である場合, その後、任意の重大な議論の
> ベイジアンメソッドは、練習で使われる方法を明確にする必要があります。 特に、私達は必要とします
> ベイジアンのデータ分析からベイジアンの推論の概念を明らかに分離し、批判的に、

### 熟語・専門語

- **Bayesian workflow**: ベイズワークフロー。モデル構築・推論・診断・改善・比較を反復する実務プロセス。
- **Bayesian inference**: ベイズ推論。事前分布と尤度から事後分布を計算する中核処理。
- **workflow**: ワークフロー。実務分析の反復手順全体。

### 要約

- ベイジアンの推論からベイジアンワークフローまで 数学統計が適用される統計の理論である場合, その後、任意の重大な議論の ベイジアンメソッドは、練習で使われる方法を明確にする必要があります。

## Chunk 0045

### English（抽出4行）

> full Bayesian workﬂow (the object of our attention).
> Bayesian inference is just the formulation and computation of conditional probability or proba-
> bility densities, p(θ|y) ∝p(θ)p(y|θ). Bayesian workﬂow includes the three steps of model building,
> inference, and model checking/improvement, along with the comparison of diﬀerent models, not

### 日本語訳（自動翻訳）

> ベイジアンワークフロー(私たちの注意の対象)。
> ベイジアン・インフェレンスは、条件付き確率やプロバの処方と計算だけです。
> 特性密度、p(θ|y) Ω(θ)p(y|θ)。 ベイジアンワークフローには、モデルビルの3つのステップが含まれています。
> 異なるモデルの比較と同様に、推論とモデルのチェック/改善、

### 熟語・専門語

- **Bayesian inference**: ベイズ推論。事前分布と尤度から事後分布を計算する中核処理。
- **model checking**: モデルチェック。モデルの仮定・予測・計算結果がデータや目的に合うか検査すること。
- **model building**: モデル構築。仮定・データ構造・prior・likelihoodを組み合わせる工程。

### 要約

- ベイジアンワークフロー(私たちの注意の対象)。

## Chunk 0046

### English（抽出4行）

> just for the purpose of model choice or model averaging but more importantly to better understand
> these models. That is, for example, why some models have trouble predicting certain aspects of the
> data, or why uncertainty estimates of important parameters can vary across models. Even when
> we have a model we like, it will be useful to compare its inferences to those from simpler and

### 日本語訳（自動翻訳）

> モデルの選択やモデル平均化の目的のためだけでなく、より重要な理解を深めるために
> これらのモデル。 つまり、例えば、一部のモデルは、特定の側面を予測するトラブルを持っている理由
> データ、または重要なパラメータの不確実性推定がモデル間で変化する可能性がある理由。 でも、
> 私達は私達が好むモデルがあります、それはより単純にそれらにその推論を比較するのに有用であり、

### 熟語・専門語

- **uncertainty**: 不確実性。観測・パラメータ・モデル構造・意思決定に残る曖昧さ。

### 要約

- モデルの選択やモデル平均化の目的のためだけでなく、より重要な理解を深めるために これらのモデル。

## Chunk 0047

### English（抽出4行）

> more complicated models as a way to understand what the model is doing. Figure 1 provides an
> outline. An extended Bayesian workﬂow would also include pre-data design of data collection and
> measurement and after-inference decision making, but we focus here on modeling the data.
> In a typical Bayesian workﬂow we end up ﬁtting a series of models, some of which are

### 日本語訳（自動翻訳）

> モデルが何をしているかを理解する方法としてより複雑なモデル。 図1は、
> 概要。 エクステンションベイジアンワークフローには、データ収集の事前データ設計も含まれます。
> 測定とアフターインフェレンス決定は、データモデリングに注力しています。
> 典型的なベイジアンワークフローでは、一連のモデルをフィッティングし、その一部が

### 熟語・専門語

- **decision**: 意思決定。予測分布を損失・効用・行動選択へ接続する工程。

### 要約

- モデルが何をしているかを理解する方法としてより複雑なモデル。

## Chunk 0048

### English（抽出4行）

> in retrospect poor choices (for reasons including poor ﬁt to data; lack of connection to relevant
> substantive theory or practical goals; priors that are too weak, too strong, or otherwise inappropriate;
> or simply from programming errors), some of which are useful but ﬂawed (for example, a regression
> that adjusts for some confounders but excludes others, or a parametric form that captures some

### 日本語訳（自動翻訳）

> 逆境の悪い選択(データに悪いフィットを含む理由のために;関連性への接続の欠如
> 実質的な理論または実用的な目標; 弱すぎる、強すぎる、または不適切な優先順位。
> または単にプログラミングエラーから)、そのうちのいくつかは有用であるが、欠陥(例えば、回帰
> いくつかの共同創設者のために調整するが、他の人を除外する、またはいくつかをキャプチャするパラメトリックフォーム

### 熟語・専門語

- **ESS**: 有効サンプルサイズ。自己相関を考慮した独立サンプル相当数。

### 要約

- 逆境の悪い選択(データに悪いフィットを含む理由のために;関連性への接続の欠如 実質的な理論または実用的な目標; 弱すぎる、強すぎる、または不適切な優先順位。

## Chunk 0049

### English（抽出4行）

> but not all of a functional relationship), and some of which are ultimately worth reporting. The
> hopelessly wrong models and the seriously ﬂawed models are, in practice, unavoidable steps along
> the way toward ﬁtting the useful models. Recognizing this can change how we set up and apply
> statistical methods.

### 日本語訳（自動翻訳）

> しかし、機能的な関係のすべてではありません)、そしてそのうちのいくつかは、最終的に報告する価値があります。 ザ・オブ・ザ・
> 絶え間なく間違ったモデルと真剣なモデルが、実際には、回避できない手順に沿って
> 便利なモデルをフィッティングする方法。 これを認識することで、設定方法を変更し、適用することができます
> 統計的な方法。

### 熟語・専門語

- **ESS**: 有効サンプルサイズ。自己相関を考慮した独立サンプル相当数。

### 要約

- しかし、機能的な関係のすべてではありません)、そしてそのうちのいくつかは、最終的に報告する価値があります。

## Chunk 0050

### English（抽出4行）

> 1.2.
> Why do we need a Bayesian workflow?
> We need a Bayesian workﬂow, rather than mere Bayesian inference, for several reasons.
> • Computation can be a challenge, and we often need to work through various steps including

### 日本語訳（自動翻訳）

> 1.2. .
> なぜベイジアンワークフローが必要なのですか?
> ベイジアン・インフェレンスではなくベイジアン・ワークフローが必要です。
> • 計算は課題であり得ます。また、さまざまな手順で作業する必要があります。

### 熟語・専門語

- **Bayesian workflow**: ベイズワークフロー。モデル構築・推論・診断・改善・比較を反復する実務プロセス。
- **Bayesian inference**: ベイズ推論。事前分布と尤度から事後分布を計算する中核処理。
- **workflow**: ワークフロー。実務分析の反復手順全体。

### 要約

- 1.2. . なぜベイジアンワークフローが必要なのですか? ベイジアン・インフェレンスではなくベイジアン・ワークフローが必要です。

## Chunk 0051

### English（抽出4行）

> ﬁtting simpler or alternative models, approximate computation that is less accurate but faster,
> and exploration of the ﬁtting process, in order to get to inferences that we trust.
> • In diﬃcult problems we typically do not know ahead of time what model we want to ﬁt, and
> even in those rare cases that an acceptable model has been chosen ahead of time, we will

### 日本語訳（自動翻訳）

> より簡単または代替モデルをフィッティングし、正確で高速な近似計算、
> そして私達が信頼するinferencesを得るためにフィッティング プロセスの調査。
> • 困難な問題では、通常、私たちがどのようなモデルに合うかを事前に知らず、
> 今までに受け入れられるモデルが選ばれているという稀なケースでも、

### 熟語・専門語

- **ESS**: 有効サンプルサイズ。自己相関を考慮した独立サンプル相当数。
- **approximate**: 近似。速度や扱いやすさのため、正確な推論・モデルを緩めること。

### 要約

- より簡単または代替モデルをフィッティングし、正確で高速な近似計算、 そして私達が信頼するinferencesを得るためにフィッティング プロセスの調査。

## Chunk 0052

### English（抽出4行）

> generally want to expand it as we gather more data or want to ask more detailed questions of
> the data we have.
> • Even if our data were static, and we knew what model to ﬁt, and we had no problems ﬁtting
> it, we still would want to understand the ﬁtted model and its relation to the data, and that

### 日本語訳（自動翻訳）

> 一般的に、より多くのデータを収集したり、より詳細な質問をしたいときにそれを拡張したい
> 私たちが持っているデータ。
> • 当社のデータが静的であったとしても、どのようなモデルに収まるかを知り、問題の解決がなかった
> それでも、適合したモデルとその関連性をデータに理解したいと考えています。

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- 一般的に、より多くのデータを収集したり、より詳細な質問をしたいときにそれを拡張したい 私たちが持っているデータ。

## Chunk 0053

### English（抽出4行）

> understanding can often best be achieved by comparing inferences from a series of related
> models.
> • Sometimes diﬀerent models yield diﬀerent conclusions, without one of them being clearly
> favourable. In such cases, presenting multiple models is helpful to illustrate the uncertainty

### 日本語訳（自動翻訳）

> 関連するシリーズからの推論を比較することで、理解が最もよく達成することができます
> モデル。
> •時々異なるモデルは、異なる結論を産み、そのうちの1つなしで明らかに
> 好ましい。 そのような場合、複数のモデルを提示することは、不確実性を示すのに役立ちます

### 熟語・専門語

- **uncertainty**: 不確実性。観測・パラメータ・モデル構造・意思決定に残る曖昧さ。

### 要約

- 関連するシリーズからの推論を比較することで、理解が最もよく達成することができます モデル。

## Chunk 0054

### English（抽出4行）

> in model choice.
> 1.3.
> “Workflow” and its relation to statistical theory and practice
> “Workﬂow” has diﬀerent meanings in diﬀerent contexts. For the purposes of this paper it should

### 日本語訳（自動翻訳）

> モデル選択で。
> 1.3. .
> 「ワークフロー」と統計理論と実践の関係
> 「ワークフロー」は、異なるコンテキストで異なる意味を持ちます。 この紙の目的のため、

### 熟語・専門語

- **workflow**: ワークフロー。実務分析の反復手順全体。

### 要約

- モデル選択で。

## Chunk 0055

### English（抽出4行）

> suﬃce that workﬂow is more general than an example but less precisely speciﬁed than a method.
> We have been inﬂuenced by the ideas about workﬂow in computing that are in the air, including
> statistical developments such as the tidyverse which are not particularly Bayesian but have a similar
> feel of experiential learning (Wickham and Groelmund, 2017). Many of the recent developments in

### 日本語訳（自動翻訳）

> ワークフローは例よりも一般的ですが、メソッドよりも正確に指定されないという問題です。
> 私たちは、空気中のコンピューティングのワークフローに関するアイデアの影響を受けています。
> 特にベイジアンではなく、類似のチダルなどの統計的開発
> 体験学習の感触(Wickham and Groelmund, 2017). 最近の開発の多く

### 熟語・専門語

- **ESS**: 有効サンプルサイズ。自己相関を考慮した独立サンプル相当数。

### 要約

- ワークフローは例よりも一般的ですが、メソッドよりも正確に指定されないという問題です。

## Chunk 0056

### English（抽出4行）

> machine learning have a similar plug-and-play feel: they are easy to use, easy to experiment with,
> and users have the healthy sense that ﬁtting a model is a way of learning something from the data
> without representing a commitment to some probability model or set of statistical assumptions.
> Figure 2 shows our perspective on the development of statistical methodology as a process

### 日本語訳（自動翻訳）

> 機械学習は同じようなプラグ アンド プレイ感じを持っています: それらは使いやすく、実験に容易です、
> モデルを当てる健康な感覚は、データから何かを学ぶ方法です
> いくつかの確率モデルまたは統計的な仮定のセットに対するコミットメントを表すことなく。
> 図2は、統計的方法論の開発に関する我々の視点をプロセスとして示します

### 熟語・専門語

- **ESS**: 有効サンプルサイズ。自己相関を考慮した独立サンプル相当数。

### 要約

- 機械学習は同じようなプラグ アンド プレイ感じを持っています: それらは使いやすく、実験に容易です、 モデルを当てる健康な感覚は、データから何かを学ぶ方法です いくつかの確率モデルまたは統計的な仮定のセットに対するコミットメントを表す…

## Chunk 0057

### English（抽出4行）

> of increasing codiﬁcation, from example to case study to workﬂow to method to theory. Not
> all methods will reach these ﬁnal levels of mathematical abstraction, but looking at the history
> Figure 1: Overview of the steps we currently consider in Bayesian workﬂow. Numbers in brackets
> refer to sections of this paper where the steps are discussed. The chart aims to show possible

### 日本語訳（自動翻訳）

> 例えば、ケーススタディからワークフローまで、理論にコダイファイを増加させる。 お知らせ
> すべての方法は、数学的抽象化のこれらの最終レベルに達するが、歴史を見る
> 図1:ベイジアンワークフローで現在検討している手順の概要。 ブラケットの数
> 手順が議論されているこの論文のセクションを参照してください。 グラフは、可能を示すことを目指しています

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- 例えば、ケーススタディからワークフローまで、理論にコダイファイを増加させる。

## Chunk 0058

### English（抽出4行）

> steps and paths an individual analysis may go through, with the understanding that any particular
> analysis will most likely not involve all of these steps. One of our goals in studying workﬂow is to
> understand how these ideas ﬁt together so they can be applied more systematically.
> Example · · · Case study · · · Workﬂow · · · Method · · · Theory

### 日本語訳（自動翻訳）

> 個々の分析のステップとパスは、特定の特定のことを理解して、通過することができます
> 分析は、これらのすべてのステップを含まない可能性が最も高い。 ワークフローを勉強する私たちの目標は、
> これらのアイデアが一緒に収まる方法を理解し、より体系的に適用することができます。
> 事例・・ケーススタディ・・・・ワークフロー・・方法・・理論

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- 個々の分析のステップとパスは、特定の特定のことを理解して、通過することができます 分析は、これらのすべてのステップを含まない可能性が最も高い。

## Chunk 0059

### English（抽出4行）

> Figure 2: Meta-workﬂow of statistical methodology, representing the way in which new ideas ﬁrst
> appear in examples, then get formalized into case studies, codiﬁed as workﬂows, are given general
> implementation as algorithms, and become the subject of theories.
> of statistics we have seen new methods being developed in the context of particular examples,

### 日本語訳（自動翻訳）

> 図2: 統計的方法論のメタワークフロー、新しいアイデアを最初に表現する
> 事例に現れ、ケーススタディに正式化し、ワークフローとしてコダイファイドされ、一般的なもの
> アルゴリズムとして実装し、理論の対象となります。
> 統計では、特定の例の文脈で開発される新しい方法を見てきました。

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- 図2: 統計的方法論のメタワークフロー、新しいアイデアを最初に表現する 事例に現れ、ケーススタディに正式化し、ワークフローとしてコダイファイドされ、一般的なもの アルゴリズムとして実装し、理論の対象となります。

## Chunk 0060

### English（抽出4行）

> stylized into case studies, set up as templates or workﬂows for new problems, and, when possible,
> formalized, coded, and studied theoretically.
> One way to understand Figure 2 is through important ideas in the history of statistics that have
> moved from left to right along that path. There have been many ideas that started out as hacks or

### 日本語訳（自動翻訳）

> ケーススタディにstylized、新しい問題のテンプレートやワークフローとして設定し、可能であれば、
> 正式に、コード化され、理論的に研究。
> 図2を理解するための1つの方法は、持っている統計の歴史の重要なアイデアを通して
> 左から右へ進みます。 ハックとして始まり、または

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- ケーススタディにstylized、新しい問題のテンプレートやワークフローとして設定し、可能であれば、 正式に、コード化され、理論的に研究。

## Chunk 0061

### English（抽出4行）

> statistics-adjacent tools and eventually were formalized as methods and brought into the core of
> statistics. Multilevel modeling is a formalization of what has been called empirical Bayes estimation
> of prior distributions, expanding the model so as to fold inference about priors into a fully Bayesian
> framework. Exploratory data analysis can be understood as a form of predictive model checking

### 日本語訳（自動翻訳）

> 統計分析ツールと、最終的には方法として正式化され、コアに持ってきました
> 統計情報 マルチレベルモデリングは、帝国湾の推定と呼ばれるものの正式化です
> 事前の配布、モデルを拡張して、先物が完全にベイジアンに及ぼす影響を折ります
> フレームワーク。 探査データ解析は、予測モデルチェックの形態として理解できます

### 熟語・専門語

- **model checking**: モデルチェック。モデルの仮定・予測・計算結果がデータや目的に合うか検査すること。
- **prior distribution**: 事前分布。データ観測前の知識・制約を表す分布。

### 要約

- 統計分析ツールと、最終的には方法として正式化され、コアに持ってきました 統計情報 マルチレベルモデリングは、帝国湾の推定と呼ばれるものの正式化です 事前の配布、モデルを拡張して、先物が完全にベイジアンに及ぼす影響を折ります フレームワーク。

## Chunk 0062

### English（抽出4行）

> (Gelman, 2003). Regularization methods such as lasso (Tibshirani, 1996) and horseshoe (Piironen
> et al., 2020) have replaced ad hoc variable selection tools in regression. Nonparametric models
> such as Gaussian processes (O’Hagan, 1978, Rasumussen and Williams, 2006) can be thought of as
> Bayesian replacements for procedures such as kernel smoothing. In each of these cases and many

### 日本語訳（自動翻訳）

> (ゲルマン、2003年) lasso(Tibshirani、1996)、馬蹄(Piironen)などの正規化方法
> et al., 2020) は、退会時にアドホック変数選択ツールを交換しました。 非パラメトリックモデル
> Gaussianプロセス(O’Hagan, 1978, Rasumussen, Williams, 2006)など、
> カーネルスムースなどの手順のベイジアン交換。 これらの各症例と多く

### 熟語・専門語

- **ESS**: 有効サンプルサイズ。自己相関を考慮した独立サンプル相当数。

### 要約

- (ゲルマン、2003年) lasso(Tibshirani、1996)、馬蹄(Piironen)などの正規化方法 et al., 2020) は、退会時にアドホック変数選択ツールを交換しました。

## Chunk 0063

### English（抽出4行）

> others, a framework of statistical methodology has been expanded to include existing methods,
> along the way making the methods more modular and potentially useful.
> The term “workﬂow” has been gradually coming into use in statistics and data science; see for
> example Liu et al. (2005), Lins et al. (2008), Long (2009), and Turner and Lambert (2015). Related

### 日本語訳（自動翻訳）

> ほか、既存の方法を含む統計手法の枠組みを拡大し、
> 方法に沿って、よりモジュラーと潜在的に有用.
> 「ワークフロー」という用語は、統計やデータサイエンスで徐々に使われています。
> Liu ら. (2005), Lins ら. (2008), Long (2009), Turner and Lambert (2015). 関連記事

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- ほか、既存の方法を含む統計手法の枠組みを拡大し、 方法に沿って、よりモジュラーと潜在的に有用. 「ワークフロー」という用語は、統計やデータサイエンスで徐々に使われています。

## Chunk 0064

### English（抽出4行）

> ideas of workﬂow are in the air in software development and other ﬁelds of informatics; recent
> discussions for practitioners include Wilson et al. (2014, 2017). Applied statistics (not just Bayesian
> statistics) has become increasingly computational and algorithmic, and this has placed workﬂow at
> the center of statistical practice (see, for example, Grolemund and Wickham, 2017, Bryan, 2017,

### 日本語訳（自動翻訳）

> ワークフローのアイデアは、ソフトウェア開発やその他の情報分野における空気です。 最近の
> 実務家のための議論は、ウィルソンら. (2014, 2017). 応用統計(ベイジアンだけでなく)
> 統計) 計算とアルゴリズムがますますます増加し、これはワークフローをで置いた
> 統計的慣行の中心(2017年、ブライアン、GrolemundおよびWickham、2017年、

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- ワークフローのアイデアは、ソフトウェア開発やその他の情報分野における空気です。

## Chunk 0065

### English（抽出4行）

> and Yu and Kumbier, 2020), as well as in application areas (for example, Lee et al., 2019, discuss
> modeling workﬂow in psychology research). “Bayesian workﬂow” has been expressed as a general
> concept by Savage (2016), Gabry et al. (2019), and Betancourt (2020a). Several of the individual
> components of Bayesian workﬂow were discussed by Gelman (2011) but not in a coherent way. In

### 日本語訳（自動翻訳）

> そして、YuとKumbier、2020)、ならびにアプリケーション領域(例えば、Le et al.、2019、議論
> 心理学研究におけるワークフローのモデル化 「ベイジアンワークフロー」は、一般として表現されています。
> Savage (2016)、Gabry et al. (2019)、Betancourt(2020a)のコンセプト。 個体数
> ベイジアンのワークフローのコンポーネントは、ゲルマン(2011)で議論されたが、一貫した方法では議論されていない。 インスタグラム

### 熟語・専門語

- **ESS**: 有効サンプルサイズ。自己相関を考慮した独立サンプル相当数。

### 要約

- そして、YuとKumbier、2020)、ならびにアプリケーション領域(例えば、Le et al.、2019、議論 心理学研究におけるワークフローのモデル化 「ベイジアンワークフロー」は、一般として表現されています。

## Chunk 0066

### English（抽出4行）

> addition there has been development of Bayesian workﬂow for particular problems, as by Shi and
> Stevens (2008) and Chiu et al. (2017).
> In this paper we go through several aspects of Bayesian workﬂow with the hope that these can
> ultimately make their way into routine practice and automatic software. We set up much of our

### 日本語訳（自動翻訳）

> また、特定の問題に対するベイジアンワークフローの開発も進めています。
> スティーブンス (2008) と Chiu ら. (2017).
> この論文では、ベイジアンのワークフローのいくつかの側面を、これらができることを期待して行きます
> ルーチンの練習と自動ソフトウェアに、究極の方法を作る. たくさんの設定を

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- また、特定の問題に対するベイジアンワークフローの開発も進めています。

## Chunk 0067

### English（抽出4行）

> workﬂow in the probabilistic programming language Stan (Carpenter et al., 2017, Stan Development
> Team, 2020), but similar ideas apply in other computing environments.1
> 1.4.
> Organizing the many aspects of Bayesian workflow

### 日本語訳（自動翻訳）

> 確率的プログラミング言語のワークフロー Stan (Carpenter et al., 2017, Stan Development
> チーム、2020)が、他のコンピューティング環境で同様のアイデアを適用します。 1
> 1.4. .
> ベイジアンワークフローの多くの側面を整理する

### 熟語・専門語

- **Bayesian workflow**: ベイズワークフロー。モデル構築・推論・診断・改善・比較を反復する実務プロセス。
- **probabilistic programming**: 確率的プログラミング。Stanなどで確率モデルをコードとして記述し推論する方法。
- **workflow**: ワークフロー。実務分析の反復手順全体。

### 要約

- 確率的プログラミング言語のワークフロー Stan (Carpenter et al., 2017, Stan Development チーム、2020)が、他のコンピューティング環境で同様のアイデアを適用します。

## Chunk 0068

### English（抽出4行）

> Textbook presentations of statistical workﬂow are often linear, with diﬀerent paths corresponding
> to diﬀerent problem situations. For example, a clinical trial in medicine conventionally begins with
> 1Wikipedia currently lists more than 50 probabilistic programming frameworks:
> en.wikipedia.org/wiki/

### 日本語訳（自動翻訳）

> 統計的なワークフローの教科書のプレゼンテーションは、異なるパスが対応する線形です。
> さまざまな問題の状況に。 例えば、従来から薬の臨床試験が始まります。
> 1Wikipediaは現在、50以上の確率的プログラミングフレームワークをリストしています。
> ウィキペディア.org/wiki/

### 熟語・専門語

- **probabilistic programming**: 確率的プログラミング。Stanなどで確率モデルをコードとして記述し推論する方法。

### 要約

- 統計的なワークフローの教科書のプレゼンテーションは、異なるパスが対応する線形です。

## Chunk 0069

### English（抽出4行）

> Probabilistic_programming.
> a sample size calculation and analysis plan, followed by data collection, cleaning, and statistical
> analysis, and concluding with the reporting of p-values and conﬁdence intervals. An observational
> study in economics might begin with exploratory data analysis, which then informs choices of

### 日本語訳（自動翻訳）

> Probabilistic programming。
> サンプルサイズの計算と分析計画、データ収集、清掃、統計
> p-valuesと自信の間隔のレポートで分析、および決定。 展望台
> 経済学での勉強は、探索的なデータ分析で始まり、その後の選択肢を知らせる可能性があります。

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- Probabilistic programming。

## Chunk 0070

### English（抽出4行）

> transformations of variables, followed by a set of regression analyses and then an array of alternative
> speciﬁcations and robustness studies.
> The statistical workﬂow discussed in this article is more tangled than the usual data analysis
> workﬂows presented in textbooks and research articles. The additional complexity comes in several

### 日本語訳（自動翻訳）

> 変数の変換、および一連の回帰解析の後、代替の配列
> 仕様および堅牢性の研究。
> この記事で議論した統計ワークフローは、通常のデータ分析よりも、より一層引き合います
> テキストブックや研究記事で提示されたワークフロー。 追加の複雑性はいくつかあります

### 熟語・専門語

- **ESS**: 有効サンプルサイズ。自己相関を考慮した独立サンプル相当数。

### 要約

- 変数の変換、および一連の回帰解析の後、代替の配列 仕様および堅牢性の研究。

## Chunk 0071

### English（抽出4行）

> places and there are many sub-workﬂows inside the higher level workﬂow:
> 1. Computation to ﬁt a complex model can itself be diﬃcult, requiring a certain amount of
> experimentation to solve the problem of computing, approximating, or simulating from the
> desired posterior distribution, along with checking that the computational algorithm did what

### 日本語訳（自動翻訳）

> 上位のワークフロー内で、複数のサブワークフローがあります。
> 1。 複雑なモデルに合う計算は、特定の量を必要とする、それ自体が困難である可能性があります
> コンピューティング、近似、またはシミュレートの問題を解決するための実験
> 所望のポスター分布、計算アルゴリズムが何をしたかをチェックして、

### 熟語・専門語

- **posterior distribution**: 事後分布。データ観測後の未知量の不確実性を表す分布。

### 要約

- 上位のワークフロー内で、複数のサブワークフローがあります。

## Chunk 0072

### English（抽出4行）

> it was intended to do.
> 2. With complex problems we typically have an idea of a general model that is more complex
> than we can easily computationally ﬁt (for example including features such as correlations,
> hierarchical structure, and parameters varying over time), and so we start with a model that

### 日本語訳（自動翻訳）

> そのためには
> 2. 複雑な問題では、通常、より複雑である一般的なモデルのアイデアを持っています
> 簡単に計算できるよりも(例えば、相関などの機能など)
> 階層構造とパラメータは時間とともに変化します)。

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- そのためには 2. 複雑な問題では、通常、より複雑である一般的なモデルのアイデアを持っています 簡単に計算できるよりも(例えば、相関などの機能など) 階層構造とパラメータは時間とともに変化します)。

## Chunk 0073

### English（抽出4行）

> we know is missing some important features, in the hope it will be computationally easier,
> with the understanding that we will gradually add in features.
> 3. Relatedly, we often consider problems where the data are not ﬁxed, either because data
> collection is ongoing or because we have the ability to draw in related datasets, for example

### 日本語訳（自動翻訳）

> 重要な機能が欠落していることがわかっています。
> 徐々に機能を追加することを理解して。
> 3。 関連することに、データが修正されていない問題はしばしば考慮します。
> 収集は進行中または関連するデータセットに描画する機能があるので、例えば

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- 重要な機能が欠落していることがわかっています。

## Chunk 0074

### English（抽出4行）

> new surveys in a public opinion analysis or data from other experiments in a drug trial.
> Adding new data often requires model extensions to allow parameters to vary or to extend
> functional forms, as for example a linear model might ﬁt well at ﬁrst but then break down
> with data are added under new conditions.

### 日本語訳（自動翻訳）

> 薬物実験における他の実験からの公開意見分析やデータに関する新しい調査。
> 新しいデータを追加するには、パラメータが異なるか、拡張できるようにするモデル拡張が必要です。
> たとえば、線形モデルが最初はよく合うかもしれないが、それから破壊します
> 新しい条件下でデータを追加。

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- 薬物実験における他の実験からの公開意見分析やデータに関する新しい調査。

## Chunk 0075

### English（抽出4行）

> 4. Beyond all the challenges of ﬁtting and expansion, models can often be best understood by
> comparing to inferences under alternative models. Hence our workﬂow includes tools for
> understanding and comparing multiple models ﬁt to the same data.
> Statistics is all about uncertainty. In addition to the usual uncertainties in the data and model

### 日本語訳（自動翻訳）

> 4。 フィッティングと拡張のすべての課題を超えて、モデルはよく理解することができます
> 代替モデルの下での推論を比較します。. ワークフローにはツールが含まれています
> 複数のモデルの理解と比較は、同じデータに適合します。
> 統計は、不確実性についてのすべてです。 データとモデルの通常の不確実性に加えて

### 熟語・専門語

- **uncertainty**: 不確実性。観測・パラメータ・モデル構造・意思決定に残る曖昧さ。

### 要約

- 4。

## Chunk 0076

### English（抽出4行）

> parameters, we are often uncertain whether we are ﬁtting our models correctly, uncertain about
> how best to set up and expand our models, and uncertain in their interpretation. Once we go
> beyond simple preassigned designs and analysis, our workﬂow can be disorderly, with our focus
> moving back and forth between data exploration, substantive theory, computing, and interpretation

### 日本語訳（自動翻訳）

> 変数、私達は私達が私達のモデルを正しく合っているかどうか、私達について不確実ではないです
> モデルのセットアップと拡大、解釈の不確実性を最大限に高める方法。 行くと
> シンプルな設計と分析を超えて、私たちのワークフローは、私たちの焦点で無秩序にすることができます
> データの探索、実質的な理論、計算、解釈の前後の移動

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- 変数、私達は私達が私達のモデルを正しく合っているかどうか、私達について不確実ではないです モデルのセットアップと拡大、解釈の不確実性を最大限に高める方法。

## Chunk 0077

### English（抽出4行）

> of results.
> Thus, any attempt to organize the steps of workﬂow will oversimplify and many
> sub-workﬂows are complex enough to justify their own articles or book chapters.
> We discuss many aspects of workﬂow, but practical considerations—especially available time,

### 日本語訳（自動翻訳）

> 結果について
> そのため、ワークフローの手順を整理しようとすると、単純化と多くがなくなります。
> サブワークフローは、自分の記事や本の章を正当化するのに十分な複雑です。
> 私たちは、ワークフローの多くの側面を議論します, しかし、実用的な考察 - 特に利用可能な時間,

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- 結果について そのため、ワークフローの手順を整理しようとすると、単純化と多くがなくなります。

## Chunk 0078

### English（抽出4行）

> computational resources and the severity of penalty for being wrong—can compel a practitioner
> to take shortcuts. Such shortcuts can make interpretation of results more diﬃcult, but we must
> be aware that they will be taken, and not ﬁtting a model at all could be worse than ﬁtting it using
> an approximate computation (where approximate can be deﬁned as not giving exact summaries

### 日本語訳（自動翻訳）

> 計算リソースと誤ってペナルティの重症度 - プラクティショナーをコンパイルできます
> ショートカットを取るために。 このようなショートカットは、結果の解釈をより困難にすることができますが、我々は必要
> それらが取られることに注意して下さい、そしてすべてのモデルを付属品より悪くないです
> 近似計算(近似は正確な要約を付与しないと定義できます)

### 熟語・専門語

- **approximate**: 近似。速度や扱いやすさのため、正確な推論・モデルを緩めること。

### 要約

- 計算リソースと誤ってペナルティの重症度 - プラクティショナーをコンパイルできます ショートカットを取るために。

## Chunk 0079

### English（抽出4行）

> of the posterior distribution even in the limit of inﬁnite compute time). Our aim in describing
> statistical workﬂow is thus also to explicitly understand various shortcuts as approximations to
> the full workﬂow, letting practitioners to make more informed choices about where to invest their
> limited time and energy.

### 日本語訳（自動翻訳）

> 無限の計算時間の制限であっても、ポスター分布の)。 私たちのこだわり
> 統計的なワークフローは、様々なショートカットを近似として明示的に理解するためにも
> 完全なワークフロー, 開業医がどこに投資するかについてより多くの情報に基づいた選択肢を作ることを可能にします
> 限られた時間およびエネルギー。

### 熟語・専門語

- **posterior distribution**: 事後分布。データ観測後の未知量の不確実性を表す分布。

### 要約

- 無限の計算時間の制限であっても、ポスター分布の)。

## Chunk 0080

### English（抽出4行）

> 1.5.
> Aim and structure of this article
> There is all sorts of tacit knowledge in applied statistics that does not always make it into published
> papers and textbooks. The present article is intended to put some of these ideas out in the open, both

### 日本語訳（自動翻訳）

> 1.5インチ
> この記事の目的と構造
> 常に公開されていない適用された統計では、すべての種類の引用の知識があります
> 論文と教科書。 この記事は、両方のオープンでこれらのアイデアの一部を置くことを意図しています

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- 1.5インチ この記事の目的と構造 常に公開されていない適用された統計では、すべての種類の引用の知識があります 論文と教科書。

## Chunk 0081

### English（抽出4行）

> to improve applied Bayesian analyses and to suggest directions for future development of theory,
> methods, and software.
> Our target audience is (a) practitioners of applied Bayesian statistics, especially users of proba-
> bilistic programming languages such as Stan, and (b) developers of methods and software intended

### 日本語訳（自動翻訳）

> 応用ベイジアン分析を改善し、将来の理論の開発の方向を提案するために、
> 方法およびソフトウェア。
> 私たちのターゲットオーディエンスは(a)適用ベイジアン統計の実践者、特にプロバのユーザーです。
> Stan や (b) のメソッドやソフトウェアの開発者など、プログラミング言語の複雑化

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- 応用ベイジアン分析を改善し、将来の理論の開発の方向を提案するために、 方法およびソフトウェア。

## Chunk 0082

### English（抽出4行）

> for these users. We are also targeting researchers of Bayesian theory and methods, as we believe
> that many of these aspects of workﬂow have been under-studied.
> In the rest of the paper we go more slowly through individual aspects of Bayesian workﬂow
> as outlined in Figure 1, starting with steps to be done before a model is ﬁt (Section 2), through

### 日本語訳（自動翻訳）

> これらのユーザーのために。 また、ベイジアン理論と方法の研究者を対象としています。
> ワークフローのこれらの側面の多くが未踏化されていること。
> 紙の残りの部分では、ベイジアンのワークフローの個々の側面を通してもっとゆっくり行きます
> 図1に示すように、モデルが合っている前に行われる手順から始まります(セクション2)、

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- これらのユーザーのために。

## Chunk 0083

### English（抽出4行）

> ﬁtting, debugging and evaluating models (Sections 3–6), and then modifying models (Section 7)
> and understanding and comparing a series of models (Section 8).
> Sections 10 and 11 then go through these steps in two examples, one in which we add features
> step by step to a model of golf putting, and one in which we go through a series of investigations

### 日本語訳（自動翻訳）

> モデルのフィッティング、デバッグ、評価(セクション3～6)、モデル変更(セクション7)
> 一連のモデル(セクション8)を理解し、比較します。
> セクション10と11は、2つの例でこれらの手順を通過します。
> ゴルフパッティングのモデルに一歩足を踏み入れ、一連の調査を通過する1つ

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- モデルのフィッティング、デバッグ、評価(セクション3～6)、モデル変更(セクション7) 一連のモデル(セクション8)を理解し、比較します。

## Chunk 0084

### English（抽出4行）

> to resolve diﬃculties in ﬁtting a simple model of planetary motion. The ﬁrst of these examples
> shows how new data can motivate model improvements, and also illustrates some of the unexpected
> challenges that arise when expanding a model. The second example demonstrates the way in which
> challenges in computation can point to modeling diﬃculties. These two small examples do not

### 日本語訳（自動翻訳）

> 惑星の動きの単純なモデルをフィッティングすることで困難を解決します。 これらの例の最初の例
> 新しいデータがどのようにモデルの改善を動機づけることができるかを示し、また予期しないもののいくつかを示します
> モデルを拡大する際に発生する課題。 2番目の例は、その方法を示しています
> 計算の課題は困難をモデル化することができます。 これらの2つの小さな例は、

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- 惑星の動きの単純なモデルをフィッティングすることで困難を解決します。

## Chunk 0085

### English（抽出4行）

> illustrate all the aspects of Bayesian workﬂow, but they should at least suggest that there could be a
> beneﬁt to systematizing the many aspects of Bayesian model development. We conclude in Section
> 12 with some general discussion and our responses to potential criticism of the workﬂow.
> 2.

### 日本語訳（自動翻訳）

> ベイジアンのワークフローのすべての側面を記述するが、少なくとも、ベイジアンのワークフローが存在することを示唆すべきである。
> ベイジアンモデル開発の多くの側面を体系化するのに役立ちます。 セクションでは、
> 12 一般的な議論とワークフローの潜在的な批判に対する当社の応答。
> 2。

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- ベイジアンのワークフローのすべての側面を記述するが、少なくとも、ベイジアンのワークフローが存在することを示唆すべきである。

## Chunk 0086

### English（抽出4行）

> Before fitting a model
> 2.1.
> Choosing an initial model
> The starting point of almost all analyses is to adapt what has been done before, using a model from

### 日本語訳（自動翻訳）

> モデルを取り付ける前に
> 2.1. .
> 初期モデルの選択
> ほぼすべての分析の開始点は、モデルをモデルから使用して、これまで行われてきたものを適応させることです。

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- モデルを取り付ける前に 2.1. . 初期モデルの選択 ほぼすべての分析の開始点は、モデルをモデルから使用して、これまで行われてきたものを適応させることです。

## Chunk 0087

### English（抽出4行）

> a textbook or case study or published paper that has been applied to a similar problem (a strongly
> related concept in software engineering is software design pattern). Using a model taken from
> some previous analysis and altering it can be seen as a shortcut to eﬀective data analysis, and by
> looking at the results from the model template we know in which direction of the model space there

### 日本語訳（自動翻訳）

> 同じような問題に加えられたテキストブックか場合の調査か公表されたペーパー(強い
> ソフトウェアエンジニアリングの関連コンセプトはソフトウェア設計パターンです。 から取られたモデルを使う
> 以前の分析と変更は、効果的なデータ分析にショートカットとして表示することができ、
> モデルのテンプレートから結果を見ると、そこでモデルの空間の方向を知る

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- 同じような問題に加えられたテキストブックか場合の調査か公表されたペーパー(強い ソフトウェアエンジニアリングの関連コンセプトはソフトウェア設計パターンです。

## Chunk 0088

### English（抽出4行）

> are likely to be useful elaborations or simpliﬁcations. Templates can save time in model building
> and computing, and we should also take into account the cognitive load for the person who needs
> to understand the results. Shortcuts are important for humans as well as computers, and shortcuts
> help explain why the typical workﬂow is iterative (see more in Section 12.2). Similarly, if we were

### 日本語訳（自動翻訳）

> 有用な詳述や単純化である可能性があります。 テンプレートはモデルビルの時間を節約できます
> そして、コンピューティング、そして私達はまた必要としている人のための認知負荷を考慮に入れるべきです
> 結果を理解する。 人間だけでなく、コンピュータやショートカットのショートカットが重要
> 典型的なワークフローが反復的である理由を説明するのに役立ちます(セクション12.2で詳細を参照)。 同様に、私たちがいたら

### 熟語・専門語

- **model building**: モデル構築。仮定・データ構造・prior・likelihoodを組み合わせる工程。

### 要約

- 有用な詳述や単純化である可能性があります。

## Chunk 0089

### English（抽出4行）

> to try to program a computer to perform data analysis automatically, it would have to work through
> some algorithm to construct models, and the building blocks of such an algorithm would represent
> templates of a sort. Despite the negative connotations of “cookbook analysis,” we think templates
> can be useful as starting points and comparison points to more elaborate analyses. Conversely, we

### 日本語訳（自動翻訳）

> データ分析を自動的に実行するためにコンピュータをプログラムしようとすると、
> モデルをビルドするアルゴリズムと、そのようなアルゴリズムのビルドブロックは表現する
> ソートのテンプレート。 「cookbook分析」のネガティブな表記にもかかわらず、テンプレートを考えます
> スタートポイントや比較ポイントとしてより精巧な分析に役立ちます。 逆に、私達は

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- データ分析を自動的に実行するためにコンピュータをプログラムしようとすると、 モデルをビルドするアルゴリズムと、そのようなアルゴリズムのビルドブロックは表現する ソートのテンプレート。

## Chunk 0090

### English（抽出4行）

> should recognize that theories are not static, and the process of development of scientiﬁc theories
> is not the same as that of statistical models (Navarro, 2020).
> Sometimes our workﬂow starts with a simple model with the aim to add features later (modeling
> varying parameters, including measurement errors, correlations, and so forth). Other times we start

### 日本語訳（自動翻訳）

> 理論が静的ではないことを認識し、科学理論の開発プロセス
> 統計モデル(Navarro, 2020)と同じではありません。
> ワークフローは、後で機能を追加する目的でシンプルなモデルから始まります(モデリング)
> 測定エラー、相関など、さまざまなパラメータ。 開始する他の時間

### 熟語・専門語

- **ESS**: 有効サンプルサイズ。自己相関を考慮した独立サンプル相当数。

### 要約

- 理論が静的ではないことを認識し、科学理論の開発プロセス 統計モデル(Navarro, 2020)と同じではありません。

## Chunk 0091

### English（抽出4行）

> with a big model and aim to strip it down in next steps, trying to ﬁnd something that is simple and
> understandable that still captures key features of the data. Sometimes we even consider multiple
> completely diﬀerent approaches to modeling the same data and thus have multiple starting points
> to choose from.

### 日本語訳（自動翻訳）

> 大きなモデルで、次のステップでそれを除去することを目指し、シンプルで簡単な何かを見つけようとします。
> データの重要な機能をまだキャプチャできる。 時々私達はまた複数の考慮します
> 同じデータをモデル化し、複数の開始点を持つために完全に異なるアプローチ
> から選ぶ

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- 大きなモデルで、次のステップでそれを除去することを目指し、シンプルで簡単な何かを見つけようとします。

## Chunk 0092

### English（抽出4行）

> 2.2.
> Modular construction
> A Bayesian model is built from modules which can often be viewed as placeholders to be replaced
> as necessary. For example, we model data with a normal distribution and then replace this with a

### 日本語訳（自動翻訳）

> 2.2. .
> モジュラー構造
> ベイジアンモデルは、交換するプレースホルダとしてしばしば見ることができるモジュールから構築されています
> 必要に応じて。 たとえば、通常の分布でデータをモデル化し、これを置換します。

### 熟語・専門語

- **ESS**: 有効サンプルサイズ。自己相関を考慮した独立サンプル相当数。

### 要約

- 2.2. . モジュラー構造 ベイジアンモデルは、交換するプレースホルダとしてしばしば見ることができるモジュールから構築されています 必要に応じて。

## Chunk 0093

### English（抽出4行）

> longer-tailed or mixture distribution; we model a latent regression function as linear and replace it
> with nonlinear splines or Gaussian processes; we can treat a set of observations as exact and then
> add a measurement-error model; we can start with a weak prior and then make it stronger when
> we ﬁnd the posterior inference includes unrealistic parameter values. Thinking of components as

### 日本語訳（自動翻訳）

> 長尾か混合物の配分;私達は線形として潜伏回帰機能を模倣し、それを取り替えます
> 非線形スプラインまたはGaussianプロセスを使って;私達は厳密な観察のセットを扱い、そしてそれから
> 測定エラーモデルを追加してください。 以前は弱いから始めて、それをより強くすることができます。
> ポスターインフェレンスには非現実的なパラメータ値が含まれています。 コンポーネントの考え方

### 熟語・専門語

- **ESS**: 有効サンプルサイズ。自己相関を考慮した独立サンプル相当数。

### 要約

- 長尾か混合物の配分;私達は線形として潜伏回帰機能を模倣し、それを取り替えます 非線形スプラインまたはGaussianプロセスを使って;私達は厳密な観察のセットを扱い、そしてそれから 測定エラーモデルを追加してください。

## Chunk 0094

### English（抽出4行）

> placeholders takes some of the pressure oﬀthe model-building process, because you can always go
> back and generalize or add information as necessary.
> The idea of modular construction goes against a long-term tradition in the statistical literature
> where whole models were given names and a new name was given every time a slight change to an

### 日本語訳（自動翻訳）

> プレースホルダーは、常に行くことができるので、モデル構築プロセスの圧力オフの一部です
> 必要に応じて情報をバックアップおよび一般化または追加します。
> モジュラー構造の考え方は、統計文献における長期の伝統に反する
> モデル全体が名前を与えられ、新しい名前がわずかな変化を毎回与えられました

### 熟語・専門語

- **ESS**: 有効サンプルサイズ。自己相関を考慮した独立サンプル相当数。

### 要約

- プレースホルダーは、常に行くことができるので、モデル構築プロセスの圧力オフの一部です 必要に応じて情報をバックアップおよび一般化または追加します。

## Chunk 0095

### English（抽出4行）

> existing model was proposed. Naming model modules rather than whole models makes it easier to
> see connections between seemingly diﬀerent models and adapt them to the speciﬁc requirements
> of the given analysis project.
> 2.3.

### 日本語訳（自動翻訳）

> 既存のモデルを提案しました。 モデル全体ではなくモデルモジュールを浪費することで、より簡単に
> 一見異なるモデル間の接続を見て、特定の要件にそれらを適応させます
> 与えられた解析プロジェクト。
> 2.3. .

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- 既存のモデルを提案しました。

## Chunk 0096

### English（抽出4行）

> Scaling and transforming the parameters
> We like our parameters to be interpretable for both practical and ethical reasons.
> This leads
> to wanting them on natural scales and modeling them as independent, if possible, or with an

### 日本語訳（自動翻訳）

> パラメータのスケーリングと変換
> 実用的かつ倫理的な理由で解釈できるパラメーターが好きです。
> このリード
> 自然なスケールでそれらを望むし、可能な限り独立してそれらをモデル化し、または

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- パラメータのスケーリングと変換 実用的かつ倫理的な理由で解釈できるパラメーターが好きです。

## Chunk 0097

### English（抽出4行）

> interpretable dependence structure, as this facilitates the use of informative priors (Gelman, 2004).
> It can also help to separate out the scale so that the unknown parameters are scale-free. For example,
> in a problem in pharmacology (Weber et al., 2018) we had a parameter that we expected would
> take on values of approximately 50 on the scale of measurement; following the principle of scaling

### 日本語訳（自動翻訳）

> 通訳可能な依存構造で、これは有益な優先順位(Gelman, 2004)の使用を容易にします。
> また、未知のパラメータがスケールフリーであるようにスケールを分離するのに役立ちます。 例えば、
> 薬理学(Weber et al., 2018)の問題で、我々は期待するパラメータを持っていた
> 測定のスケールで約50値を取る;スケーリングの原則に従って

### 熟語・専門語

- **approximate**: 近似。速度や扱いやすさのため、正確な推論・モデルを緩めること。

### 要約

- 通訳可能な依存構造で、これは有益な優先順位(Gelman, 2004)の使用を容易にします。

## Chunk 0098

### English（抽出4行）

> we might set up a model on log(θ/50), so that 0 corresponds to an interpretable value (50 on the
> original scale) and a diﬀerence of 0.1, for example, on the log scale corresponds to increasing or
> decreasing by approximately 10%. This sort of transformation is not just for ease of interpretation;
> it also sets up the parameters in a way that readies them for eﬀective hierarchical modeling. As

### 日本語訳（自動翻訳）

> log(θ/50) にモデルを設定できるため、0 は解釈可能な値(50)に相当する
> オリジナルのスケール)と0.1の違い(例えば、ログのスケールは増加するか、
> 約10%削減 この種の変換は単なる解釈の容易さではありません。
> また、効果的な階層モデリングのためにそれらを読み込む方法でパラメータを設定します。 お問い合わせ

### 熟語・専門語

- **approximate**: 近似。速度や扱いやすさのため、正確な推論・モデルを緩めること。

### 要約

- log(θ/50) にモデルを設定できるため、0 は解釈可能な値(50)に相当する オリジナルのスケール)と0.1の違い(例えば、ログのスケールは増加するか、 約10%削減 この種の変換は単なる解釈の容易さではありません。

## Chunk 0099

### English（抽出4行）

> we build larger models, for example by incorporating data from additional groups of patients or
> additional drugs, it will make sense to allow parameters to vary by group (as we discuss in Section
> 12.5), and partial pooling can be more eﬀective on scale-free parameters. For example, a model
> in toxicology required the volume of the liver for each person in the study. Rather than ﬁtting a

### 日本語訳（自動翻訳）

> 患者の追加グループからデータを組み込むことで、より大きなモデルを構築します。
> 追加の薬は、グループによってパラメータが変化することを可能にするという意味になります(セクションで議論する
> 12.5)、および部分的なプールはスケールフリーの変数でより有効である場合もあります。 例えば、モデル
> 毒性学では、研究の各人のための肝臓の体積を必要とします。 フィッティングよりもむしろ

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- 患者の追加グループからデータを組み込むことで、より大きなモデルを構築します。

## Chunk 0100

### English（抽出4行）

> hierarchical model to these volumes, we expressed each as the volume of the person multiplied
> by the proportion of volume that the liver; we would expect these scale-free factors to vary less
> across people and so the ﬁtted model can do more partial pooling compared to the result from
> modeling absolute volumes. The scaling transformation is a decomposition that facilitates eﬀective

### 日本語訳（自動翻訳）

> これらのボリュームに階層的なモデルを表現し、その人それぞれが多岐に渡る
> 肝臓の容積の割合で; 私たちは、これらのスケールフリー要因が少ないことを期待します
> 人を超えて、フィットしたモデルは、結果と比較してより部分的なプールを行うことができます
> 絶対的な容積を模倣する。 スケール変換は効果的な分解です

### 熟語・専門語

- **ESS**: 有効サンプルサイズ。自己相関を考慮した独立サンプル相当数。

### 要約

- これらのボリュームに階層的なモデルを表現し、その人それぞれが多岐に渡る 肝臓の容積の割合で; 私たちは、これらのスケールフリー要因が少ないことを期待します 人を超えて、フィットしたモデルは、結果と比較してより部分的なプールを行うことが…

## Chunk 0101

### English（抽出4行）

> hierarchical modeling.
> In many cases we can put parameters roughly on unit scale by using logarithmic or logit
> transformations or by standardizing, subtracting a center and dividing by a scale. If the center and
> scale are themselves computed from the data, as we do for default priors in regression coeﬃcients

### 日本語訳（自動翻訳）

> 階層モデリング。
> 多くの場合、logarithmic や logit を使用して、ユニットスケールでパラメーターを大体に置くことができます。
> トランスフォーメーションまたは標準化することにより、センターを分割し、スケールで分割します。 中心および場合
> スケールは、レグレッション係数のデフォルト優先順位で行うため、データから計算されます。

### 熟語・専門語

- **ESS**: 有効サンプルサイズ。自己相関を考慮した独立サンプル相当数。

### 要約

- 階層モデリング。

## Chunk 0102

### English（抽出4行）

> 2 predictors
> 4 predictors
> 15 predictors
> 0.00

### 日本語訳（自動翻訳）

> 2 予測
> 4つの予測
> 15 予測
> 日 時

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- 2 予測 4つの予測 15 予測 日 時

## Chunk 0103

### English（抽出4行）

> 0.25
> 0.50
> 0.75
> 1.00 0.00

### 日本語訳（自動翻訳）

> 0.25の
> 0.50円
> 0.75の
> 1.00 0.00 0.00 1.00 0.00 1.00 0.00 1.00 0.00 0.00 1.00 0.00 1.00 0.00 1.00 0.00 1.00 0.00 1.00 0.00 1.00 0.00 1.00 0.00 1.00 0.00 0.00 0.00 1.00 0.00 0.00 1.00 0.00 1.00 0.00 0.00 1.00 0.00 1.00 0.00 0.00 1.00 0.00 0.00 1.00 0.00 0.00 0.00 1.00 0.00 0.00 1.00 0.00 0.00 0.00 0.00 1.00 1.00 0.00 0.00 0.00 1.00 0.00 0.00 1.00 0.00 1.00 0.00 1.00 1.00 0.00 1.00 1.00 1.00 0.00 1.00 1.00 1.00 1.00 1.00 0.00 1.00 1.00 1.00 1.00 1.00 1.00 1.00 1.00 1.00 1.00 1.00 1.00 1.00 1.00 1.00 0.00 1.00 1.00 0.00 1.00 1.00 1.00 1.00 1.00 1.00 1.00 1.00 1.00 1.00 1.00 1.00 1.00 1.00 1.00 1.00 1.00 1.00 1.00 1.00 1.00 1.00 1.00 1.00 1.00 1.00 1.00 0.00

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- 0.25の 0.50円 0.75の 1.00 0.00 0.00 1.00 0.00 1.00 0.00 1.00 0.00 0.00 1.00 0.00 1.00 0.00 1.00 0.00 1.00 0.00 1.00 0.00…

## Chunk 0104

### English（抽出4行）

> 0.25
> 0.50
> 0.75
> 1.00 0.00

### 日本語訳（自動翻訳）

> 0.25の
> 0.50円
> 0.75の
> 1.00 0.00 0.00 1.00 0.00 1.00 0.00 1.00 0.00 0.00 1.00 0.00 1.00 0.00 1.00 0.00 1.00 0.00 1.00 0.00 1.00 0.00 1.00 0.00 1.00 0.00 0.00 0.00 1.00 0.00 0.00 1.00 0.00 1.00 0.00 0.00 1.00 0.00 1.00 0.00 0.00 1.00 0.00 0.00 1.00 0.00 0.00 0.00 1.00 0.00 0.00 1.00 0.00 0.00 0.00 0.00 1.00 1.00 0.00 0.00 0.00 1.00 0.00 0.00 1.00 0.00 1.00 0.00 1.00 1.00 0.00 1.00 1.00 1.00 0.00 1.00 1.00 1.00 1.00 1.00 0.00 1.00 1.00 1.00 1.00 1.00 1.00 1.00 1.00 1.00 1.00 1.00 1.00 1.00 1.00 1.00 0.00 1.00 1.00 0.00 1.00 1.00 1.00 1.00 1.00 1.00 1.00 1.00 1.00 1.00 1.00 1.00 1.00 1.00 1.00 1.00 1.00 1.00 1.00 1.00 1.00 1.00 1.00 1.00 1.00 1.00 1.00 0.00

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- 0.25の 0.50円 0.75の 1.00 0.00 0.00 1.00 0.00 1.00 0.00 1.00 0.00 0.00 1.00 0.00 1.00 0.00 1.00 0.00 1.00 0.00 1.00 0.00…

## Chunk 0105

### English（抽出4行）

> 0.25
> 0.50
> 0.75
> 1.00

### 日本語訳（自動翻訳）

> 0.25の
> 0.50円
> 0.75の
> 1.00円

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- 0.25の 0.50円 0.75の 1.00円

## Chunk 0106

### English（抽出4行）

> Response mean (per data row)
> count
> Figure 3: Demonstration of the use of prior predictive checking to gain understanding of non-
> obvious features of a model. The above graphs correspond to logistic regression models with 100

### 日本語訳（自動翻訳）

> 応答平均(データ列ごと)
> パスワード
> 図3:非理解を得るための事前予測チェックの使用の実証
> モデルの明らかな特徴。 上記のグラフは、100のロジスティック回帰モデルに対応

### 熟語・専門語

- **prior predictive**: 事前予測。データを見る前のpriorだけで生成される予測分布を確認する診断。
- **ESS**: 有効サンプルサイズ。自己相関を考慮した独立サンプル相当数。

### 要約

- 応答平均(データ列ごと) パスワード 図3:非理解を得るための事前予測チェックの使用の実証 モデルの明らかな特徴。

## Chunk 0107

### English（抽出4行）

> data points and 2, 4, or 15 binary covariates. In each case, the regression coeﬃcients were given
> independent normal(0, 1) prior distributions. For each model, we performed a prior predictive
> check, 1000 times simulating the vector of coeﬃcients θ from the prior, then simulating a dataset y
> from the logistic model, and then summarizing this by the mean of the simulated data, ¯y. Each plot

### 日本語訳（自動翻訳）

> データポイントと2、4、または15のバイナリコワリエート。 各ケースでは、回帰係数が与えられた
> 独立した普通(0、1)の事前の配分。 各モデルでは、事前予測を実施
> チェック, 1000 時間の係数のベクトルをシミュレート θ 先から, データセット y をシミュレートする
> ロジスティックモデルから、シミュレートされたデータの平均でこれを要約し、 ̄y。 各プロット

### 熟語・専門語

- **prior predictive**: 事前予測。データを見る前のpriorだけで生成される予測分布を確認する診断。
- **prior distribution**: 事前分布。データ観測前の知識・制約を表す分布。
- **ESS**: 有効サンプルサイズ。自己相関を考慮した独立サンプル相当数。

### 要約

- データポイントと2、4、または15のバイナリコワリエート。

## Chunk 0108

### English（抽出4行）

> shows the prior predictive distribution of this summary statistic, that is, the 1000 simulations of ¯y.
> When the number of covariates in the model is small, this prior predictive distribution is spread out,
> indicating that the model is compatible with a wide range of regimes of data. But as the number
> of covariates increases, the posterior predictive distribution becomes concentrated near ¯y = 0 or

### 日本語訳（自動翻訳）

> このサマリー統計の事前予測分布を示します。つまり、 ̄y の 1000 シミュレーション。
> モデルのコワリエートの数が小さくなると、この先行予測分布が広がり、
> モデルが広範囲のデータレジムと互換性があることを示す。 しかし、数字として
> コワリエートの増加により、ポスター予測分布は ̄y = 0 付近に集中します。

### 熟語・専門語

- **prior predictive**: 事前予測。データを見る前のpriorだけで生成される予測分布を確認する診断。
- **posterior predictive**: 事後予測。推定後のモデルが観測データの特徴を再現できるかを見る診断。

### 要約

- このサマリー統計の事前予測分布を示します。

## Chunk 0109

### English（抽出4行）

> 1, indicating that weak priors on the individual coeﬃcients of the model imply a strong prior on
> this particular predictive quantity. If we wanted a more moderate prior predictive distribution on
> ¯y, the prior on the coeﬃcients would need to be strongly concentrated near zero.
> in rstanarm (Gabry et al., 2020a), we can consider this as an approximation to a hierarchical model

### 日本語訳（自動翻訳）

> 1、モデルの個々の係数の弱い優先順位は、前の強いことを示す
> この特定の予測量。 より適度な予測分布を望むなら
> や、係数の前のところは、ゼロ付近に強く集中する必要があります。
> rstanarm (Gabry et al., 2020a) では、階層モデルへの近似として検討することができます。

### 熟語・専門語

- **prior predictive**: 事前予測。データを見る前のpriorだけで生成される予測分布を確認する診断。

### 要約

- 1、モデルの個々の係数の弱い優先順位は、前の強いことを示す この特定の予測量。

## Chunk 0110

### English（抽出4行）

> in which the center and scale are hyperparameters that are estimated from the data.
> More complicated transformations can also serve the purpose of making parameters more
> interpretable and thus facilitating the use of prior information; Riebler et al. (2016) give an example
> for a class of spatial correlation models, and Simpson et al. (2017) consider this idea more generally.

### 日本語訳（自動翻訳）

> 中心とスケールは、データから推定されるハイパーパラメータである。
> より複雑な変換は、パラメータを作るための目的にも役立つ
> 通訳可能で、したがって、事前情報の使用を促進します。 Riebler et al。 (2016) 例
> 空間相関モデルのクラス、Simpson et al. (2017) は、より一般的にこの考えを検討します。

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- 中心とスケールは、データから推定されるハイパーパラメータである。

## Chunk 0111

### English（抽出4行）

> 2.4.
> Prior predictive checking
> Prior predictive checks are a useful tool to understand the implications of a prior distribution in
> the context of a generative model (Box, 1980, Gabry et al., 2019; see also Section 7.3 for details

### 日本語訳（自動翻訳）

> 2.4. .
> 事前予測チェック
> 事前の予測チェックは、事前の配布の含意を理解するための有用なツールです
> ジェネレーションモデル(Box、1980、Gabry et al.、2019)のコンテキスト。詳細はセクション7.3を参照してください。

### 熟語・専門語

- **prior predictive**: 事前予測。データを見る前のpriorだけで生成される予測分布を確認する診断。
- **prior distribution**: 事前分布。データ観測前の知識・制約を表す分布。
- **generative model**: 生成モデル。データ生成過程を確率的に記述するモデル。

### 要約

- 2.4. . 事前予測チェック 事前の予測チェックは、事前の配布の含意を理解するための有用なツールです ジェネレーションモデル(Box、1980、Gabry et al.、2019)のコンテキスト。

## Chunk 0112

### English（抽出4行）

> on how to work with prior distributions). In particular, because prior predictive checks make use
> of simulations from the model rather than observed data, they provide a way to reﬁne the model
> without using the data multiple times. Figure 3 shows a simple prior predictive check for a logistic
> regression model. The simulation shows that even independent priors on the individual coeﬃcients

### 日本語訳（自動翻訳）

> 事前配布の操作方法 特に、事前の予測チェックが使用できるように
> 観察されたデータではなくモデルのシミュレーションでモデルを精製する方法を提供します。
> 複数回データを使わずに。 図3は、記号論理学のための簡単な事前予測チェックを示しています
> 回帰モデル。 シミュレーションは、個々の係数の独立した優先順位を示す

### 熟語・専門語

- **prior predictive**: 事前予測。データを見る前のpriorだけで生成される予測分布を確認する診断。
- **prior distribution**: 事前分布。データ観測前の知識・制約を表す分布。
- **ESS**: 有効サンプルサイズ。自己相関を考慮した独立サンプル相当数。

### 要約

- 事前配布の操作方法 特に、事前の予測チェックが使用できるように 観察されたデータではなくモデルのシミュレーションでモデルを精製する方法を提供します。

## Chunk 0113

### English（抽出4行）

> have diﬀerent implications as the number of covariates in the model increases. This is a general
> phenomenon in regression models where as the number of predictors increases, we need stronger
> priors on model coeﬃcients (or enough data) if we want to push the model away from extreme
> predictions.

### 日本語訳（自動翻訳）

> モデルのコワリエートの数が増加するにつれて、異なる影響があります。 これは一般的なことです
> 回帰モデルの現象は、予測者数が増加するにつれて、より強くなる
> モデルの係数(または十分なデータ)を極端に押したい場合
> 予測。

### 熟語・専門語

- **ESS**: 有効サンプルサイズ。自己相関を考慮した独立サンプル相当数。
- **prediction**: 予測。未知/将来/除外データに対する分布や点推定。

### 要約

- モデルのコワリエートの数が増加するにつれて、異なる影響があります。

## Chunk 0114

### English（抽出4行）

> A useful approach is to consider priors on outcomes and then derive a corresponding joint prior
> on parameters (see, e.g., Piironen and Vehtari, 2017, and Zhang et al., 2020). More generally, joint
> priors allow us to control the overall complexity of larger parameter sets, which helps generate more
> sensible prior predictions that would be hard or impossible to achieve with independent priors.

### 日本語訳（自動翻訳）

> 有用なアプローチは、結果の事前を検討し、事前に対応するジョイントを導き出すことです
> パラメータ(例、Piironen、Vehtari、2017、およびZhang et al.、2020)。 より一般的に、ジョイント
> 前者は、より大きなパラメータセットの全体的な複雑性を制御することを可能にします。これにより、より多くのパラメータを生成することができます。
> 独立した優先順位で達成しにくい、または不可能であろう賢明な事前予測。

### 熟語・専門語

- **prediction**: 予測。未知/将来/除外データに対する分布や点推定。

### 要約

- 有用なアプローチは、結果の事前を検討し、事前に対応するジョイントを導き出すことです パラメータ(例、Piironen、Vehtari、2017、およびZhang et al.、2020)。

## Chunk 0115

### English（抽出4行）

> Figure 4: Prior predictive draws from the Gaussian process model with squared exponential co-
> variance function and diﬀerent values of the amplitude parameter τ and the length scale parameter
> l. From Gelman et al. (2013).
> Figure 4 shows an example of prior predictive checking for three choices of prior distribution for

### 日本語訳（自動翻訳）

> 図4:ガウスのプロセスモデルから先行予測の描画を正方形の指数関数の共同で
> variance 関数と振幅パラメータ τ と長さスケールパラメーターの異なる値
> l. ゲルマン ら. (2013).
> 図4は、事前の配布の3つの選択肢の事前予測チェックの例を示しています

### 熟語・専門語

- **prior predictive**: 事前予測。データを見る前のpriorだけで生成される予測分布を確認する診断。
- **prior distribution**: 事前分布。データ観測前の知識・制約を表す分布。
- **ESS**: 有効サンプルサイズ。自己相関を考慮した独立サンプル相当数。

### 要約

- 図4:ガウスのプロセスモデルから先行予測の描画を正方形の指数関数の共同で variance 関数と振幅パラメータ τ と長さスケールパラメーターの異なる値 l. ゲルマン ら. (2013). 図4は、事前の配布の3つの選択肢の事前予…

## Chunk 0116

### English（抽出4行）

> a Gaussian process model (Rasmussen and Willams, 2006). This sort of simulation and graphical
> comparison is useful when working with any model and essential when setting up unfamiliar or
> complicated models.
> Another beneﬁt of prior predictive simulations is that they can be used to elicit expert prior

### 日本語訳（自動翻訳）

> Gaussian プロセスモデル (Rasmussen と Willams, 2006). この種のシミュレーションとグラフィカル
> 比較は、不慣れなモデルや必須を設定するときに便利です。
> 複雑なモデル。
> 事前予測シミュレーションのもう1つの利点は、以前に専門家をelicitに使用できることです

### 熟語・専門語

- **prior predictive**: 事前予測。データを見る前のpriorだけで生成される予測分布を確認する診断。
- **ESS**: 有効サンプルサイズ。自己相関を考慮した独立サンプル相当数。

### 要約

- Gaussian プロセスモデル (Rasmussen と Willams, 2006). この種のシミュレーションとグラフィカル 比較は、不慣れなモデルや必須を設定するときに便利です。

## Chunk 0117

### English（抽出4行）

> knowledge on the measurable quantities of interest, which is often easier than soliciting expert
> opinion on model parameters that are not observable (O’Hagan et al., 2006).
> Finally, even when we skip computational prior predictive checking, it might be useful to think
> about how the priors we have chosen would aﬀect a hypothetical simulated dataset.

### 日本語訳（自動翻訳）

> 目に見える関心の量に関する知識は、しばしば勧誘専門家よりも簡単です
> 観察できないモデルパラメータに関する意見(O’Hagan et al., 2006).
> 最後に、計算前の予測チェックをスキップしても、考えるのに便利です
> 選択した先物が仮説シミュレーションされたデータセットにどのように影響するかについて。

### 熟語・専門語

- **prior predictive**: 事前予測。データを見る前のpriorだけで生成される予測分布を確認する診断。

### 要約

- 目に見える関心の量に関する知識は、しばしば勧誘専門家よりも簡単です 観察できないモデルパラメータに関する意見(O’Hagan et al., 2006). 最後に、計算前の予測チェックをスキップしても、考えるのに便利です 選択した先物…

## Chunk 0118

### English（抽出4行）

> 2.5.
> Generative and partially generative models
> Fully Bayesian data analysis requires a generative model—that is, a joint probability distribution
> for all the data and parameters. The point is subtle: Bayesian inference does not actually require

### 日本語訳（自動翻訳）

> 2.5インチ
> ジェネレーションと部分的に生成されるモデル
> ベイジアンのデータ解析では、共同確率分布である遺伝子モデルが必要です。
> すべてのデータとパラメーター。 点は微妙です:ベイジアン推論は実際には要求しません

### 熟語・専門語

- **Bayesian inference**: ベイズ推論。事前分布と尤度から事後分布を計算する中核処理。
- **generative model**: 生成モデル。データ生成過程を確率的に記述するモデル。

### 要約

- 2.5インチ ジェネレーションと部分的に生成されるモデル ベイジアンのデータ解析では、共同確率分布である遺伝子モデルが必要です。

## Chunk 0119

### English（抽出4行）

> the generative model; all it needs from the data is the likelihood, and diﬀerent generative models
> can have the same likelihood. But Bayesian data analysis requires the generative model to be able
> to perform predictive simulation and model checking (Sections 2.4, 4.1, 4.2, 6.1, and 6.2), and
> Bayesian workﬂow will consider a series of generative models.

### 日本語訳（自動翻訳）

> ジェネレーションモデル。データから必要なのは、可能性と異なる遺伝子モデルです。
> 同じ可能性を持つことができます。 しかし、ベイジアンのデータ分析では、遺伝子モデルが必要
> 予測シミュレーションとモデルチェック(セクション2.4, 4.1, 4.2, 6.1, 6.2)を行い、
> ベイジアンワークフローは、一連の遺伝子モデルを検討します。

### 熟語・専門語

- **model checking**: モデルチェック。モデルの仮定・予測・計算結果がデータや目的に合うか検査すること。
- **likelihood**: 尤度。パラメータが与えられたときデータがどれだけ起こりやすいか。
- **generative model**: 生成モデル。データ生成過程を確率的に記述するモデル。

### 要約

- ジェネレーションモデル。

## Chunk 0120

### English（抽出4行）

> For a simple example, suppose we have data y ∼binomial(n, θ), where n and y are observed
> and we wish to make inference about θ. For the purpose of Bayesian inference it is irrelevant
> if the data were sampled with ﬁxed n (binomial sampling) or sampled until a speciﬁed number
> of successes occurred (negative binomial sampling): the two likelihoods are equivalent for the

### 日本語訳（自動翻訳）

> 単純な例では、n と y が観察されるデータ y〜binomial(n, θ) があるとします。
> そして、θについて推論したい。 ベイジアン推論の目的のために、それは無関係です
> 固定 n (binomial sampling) でデータがサンプル化されたり、指定された番号までサンプル化された場合
> 成功の発生(負のbinomialサンプリング):2つの可能性は、

### 熟語・専門語

- **Bayesian inference**: ベイズ推論。事前分布と尤度から事後分布を計算する中核処理。
- **likelihood**: 尤度。パラメータが与えられたときデータがどれだけ起こりやすいか。
- **ESS**: 有効サンプルサイズ。自己相関を考慮した独立サンプル相当数。

### 要約

- 単純な例では、n と y が観察されるデータ y〜binomial(n, θ) があるとします。

## Chunk 0121

### English（抽出4行）

> purpose of estimating θ because they diﬀer only by a multiplicative factor that depends on y and
> n but not θ. However, if we want to simulate new data from the predictive model, the two models
> are diﬀerent, as the binomial model yields replications with a ﬁxed value of n and the negative
> binomial model yields replications with a ﬁxed value of y. Prior and posterior predictive checks

### 日本語訳（自動翻訳）

> y に依存する多重的要因によってのみ異なるため θ を推定する目的
> nがθではない。 しかし、予測モデルから新しいデータをシミュレートしたい場合、2つのモデル
> binomialモデルがnの固定値とネガティブのreplicationsを収穫するので異なる
> binomial モデルは、y の固定値でレプリケーションを生成します。 事前およびポスター予測チェック

### 熟語・専門語

- **posterior predictive**: 事後予測。推定後のモデルが観測データの特徴を再現できるかを見る診断。

### 要約

- y に依存する多重的要因によってのみ異なるため θ を推定する目的 nがθではない。

## Chunk 0122

### English（抽出4行）

> (Sections 2.4 and 6.1) will look diﬀerent under these two diﬀerent generative models.
> This is not to say that the Bayesian approach is necessarily better; the assumptions of a generative
> model can increase inferential eﬃciency but can also go wrong, and this motivates much of our
> workﬂow.

### 日本語訳（自動翻訳）

> (セクション 2.4 と 6.1) は、これらの2つの異なる遺伝子モデルの下で異なる外観になります。
> ベイジアンのアプローチは必ずしも優れているとは言えません。
> モデルは、不当な効率性を高めることができますが、誤って行くこともできますし、この動機は私たちの多くを
> ワークフロー。

### 熟語・専門語

- **generative model**: 生成モデル。データ生成過程を確率的に記述するモデル。
- **ESS**: 有効サンプルサイズ。自己相関を考慮した独立サンプル相当数。

### 要約

- (セクション 2.4 と 6.1) は、これらの2つの異なる遺伝子モデルの下で異なる外観になります。

## Chunk 0123

### English（抽出4行）

> It is common in Bayesian analysis to use models that are not fully generative. For example, in
> regression we will typically model an outcome y given predictors x without a generative model
> for x. Another example is survival data with censoring, where the censoring process is not usually
> modeled. When performing predictive checks for such models, we either need to condition on the

### 日本語訳（自動翻訳）

> 完全に遺伝子組み合わされていないモデルを使用するベイジアン解析では共通です。 例えば、
> 私たちが通常、遺伝子モデルなしで予測Xを与えられた結果Yをモデル化します
> x の場合 もう一つの例は、検閲プロセスが通常ではない検閲で生存データです
> モデリング。 そのようなモデルの予測チェックを実行するとき、我々はどちらかの上で条件する必要があります

### 熟語・専門語

- **generative model**: 生成モデル。データ生成過程を確率的に記述するモデル。
- **ESS**: 有効サンプルサイズ。自己相関を考慮した独立サンプル相当数。

### 要約

- 完全に遺伝子組み合わされていないモデルを使用するベイジアン解析では共通です。

## Chunk 0124

### English（抽出4行）

> observed predictors or else extend the model to allow new values of the predictors to be sampled.
> It is also possible that there is no stochastic generative process for some parts of the model, for
> example if x has been chosen by a deterministic design of experiment.
> Thinking in terms of generative models can help illuminate the limitations of what can be

### 日本語訳（自動翻訳）

> 観察された予測者または他のモデルは、予測者の新しい値がサンプル化できるようにするモデルを拡張します。
> モデルは、モデルのいくつかの部分の確率的遺伝子組み換えプロセスがないことも可能である
> 実験の決定的な設計によってxが選ばれる場合例。
> 遺伝子モデルの面で考えると、何ができるかの制限を照らすのを助けることができます

### 熟語・専門語

- **generative model**: 生成モデル。データ生成過程を確率的に記述するモデル。
- **ESS**: 有効サンプルサイズ。自己相関を考慮した独立サンプル相当数。

### 要約

- 観察された予測者または他のモデルは、予測者の新しい値がサンプル化できるようにするモデルを拡張します。

## Chunk 0125

### English（抽出4行）

> learned from the observations. For example, we might want to model a temporal process with a
> complicated autocorrelation structure, but if our actual data are spaced far apart in time, we might
> not be able to distinguish this model from a simpler process with nearly independent errors.
> In addition, Bayesian models that use improper priors are not fully generative, in the sense that

### 日本語訳（自動翻訳）

> 観察から学んだこと。 たとえば、一時的なプロセスをモデル化したいかもしれません。
> 複雑な自動相関構造ですが、実際のデータが時間外に間隔をあけば、
> ほぼ独立したエラーでこのモデルを単純プロセスから区別できません。
> また、不適切な優先順位を使用するベイジアンモデルは完全に遺伝子的ではなく、その意味で

### 熟語・専門語

- **ESS**: 有効サンプルサイズ。自己相関を考慮した独立サンプル相当数。

### 要約

- 観察から学んだこと。

## Chunk 0126

### English（抽出4行）

> they do not have a joint distribution for data and parameters and it would not be possible to sample
> from the prior predictive distribution. When we do use improper priors, we think of them as being
> placeholders or steps along the road to a full Bayesian model with a proper joint distribution over
> parameters and data.

### 日本語訳（自動翻訳）

> それらはデータおよび変数のための共同配分を持っていませんし、それはサンプルすることができません
> 事前予測分布から。 不適切な優先順位を使用するときは、そのように考えます。
> プレースホルダやフルベイジアンモデルへの道に沿って、適切なジョイントディストリビューション
> パラメータとデータ。

### 熟語・専門語

- **prior predictive**: 事前予測。データを見る前のpriorだけで生成される予測分布を確認する診断。

### 要約

- それらはデータおよび変数のための共同配分を持っていませんし、それはサンプルすることができません 事前予測分布から。

## Chunk 0127

### English（抽出4行）

> In applied work, complexity often arises from incorporating diﬀerent sources of data. For
> example, we ﬁt a Bayesian model for the 2020 presidential election using state and national
> polls, partially pooling toward a forecast based on political and economic “fundamentals” (Morris,
> Gelman, and Heidemanns, 2020). The model includes a stochastic process for latent time trends

### 日本語訳（自動翻訳）

> 応用作業では、複雑性はしばしば異なるデータソースを組み込むことから生じる。 のために
> 例えば、2020年大統領選挙で国家と国民の選挙でベイジアンモデルに収まる
> 政治と経済の「金融」に基づく予測に向けて部分的にプール(モーリス)
> ゲルマン、ハイドマン、2020年) モデルは、潜在時間の傾向のための素晴らしいプロセスが含まれています

### 熟語・専門語

- **ESS**: 有効サンプルサイズ。自己相関を考慮した独立サンプル相当数。

### 要約

- 応用作業では、複雑性はしばしば異なるデータソースを組み込むことから生じる。

## Chunk 0128

### English（抽出4行）

> in state and national opinion. Fitting the model using Stan yields posterior simulations which
> are used to compute probabilities for election outcomes. The Bayesian model-based approach is
> superﬁcially similar to poll aggregations such as described by Katz (2016), which also summarize
> uncertainty by random simulations. The diﬀerence is that our model could be run forward to

### 日本語訳（自動翻訳）

> 国家と国民の意見。 Stan の収穫のポスター シミュレーションを使用してモデルに合います
> 選挙結果の確率を計算するために使用されます。 ベイジアンモデルベースのアプローチは
> Katz (2016) で説明したような投票集計に類似した。
> ランダムシミュレーションによる不確実性。 違いは、モデルが先に進むことができることです。

### 熟語・専門語

- **uncertainty**: 不確実性。観測・パラメータ・モデル構造・意思決定に残る曖昧さ。

### 要約

- 国家と国民の意見。

## Chunk 0129

### English（抽出4行）

> generate polling data; it is not just a data analysis procedure but also provides a probabilistic model
> for public opinion at the national and state levels.
> Thinking more generally, we can consider a progression from least to most generative models.
> At one extreme are completely non-generative methods which are deﬁned simply as data summaries,

### 日本語訳（自動翻訳）

> ポーリングデータを生成します。データ分析の手順だけでなく、確率的モデルも提供します。
> 国家レベルと国家レベルでの公共の意見のために。
> より一般的に考えると、少なくとも最も遺伝子的なモデルの進歩を考慮することができます。
> 1つの極端では、単にデータ集約として定義される完全に非遺伝子的な方法であり、

### 熟語・専門語

- **generative model**: 生成モデル。データ生成過程を確率的に記述するモデル。
- **ESS**: 有効サンプルサイズ。自己相関を考慮した独立サンプル相当数。

### 要約

- ポーリングデータを生成します。

## Chunk 0130

### English（抽出4行）

> with no model for the data at all. Next come classical statistical models, characterized by probability
> distributions p(y; θ) for data y given parameters θ, but with no probability distribution for θ. At
> the next step are the Bayesian models we usually ﬁt, which are generative on y and θ but include
> additional unmodeled data x such as sample sizes, design settings, and hyperparameters; we write

### 日本語訳（自動翻訳）

> データのモデルが全くありません。 次は、確率で特徴的な古典的な統計モデル来ます
> 引数 θ を指定したデータ y に対して p(y;θ) を配布しますが、 θ の確率分布はありません。 お問い合わせ
> 次のステップは、私たちが通常フィットするベイジアンモデルです。これはyとθで生成されますが、
> サンプルサイズ、設計設定、ハイパーパラメータなど、追加の非モデル化されたデータx; 書き込み

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- データのモデルが全くありません。

## Chunk 0131

### English（抽出4行）

> such models as p(y, θ|x). The ﬁnal step would be a completely generative model p(y, θ, x) with no
> “left out” data, x.
> In statistical workﬂow we can move up and down this ladder, for example starting with an
> unmodeled data-reduction algorithm and then formulating it as a probability model, or starting

### 日本語訳（自動翻訳）

> p(y、θ|x) のようなモデル。 最後のステップは、全く遺伝子型モデルp(y,θ,x)でなく、
> 「左アウト」のデータ、x。
> 統計的なワークフローでは、この梯子を上下に動かすことができます。例えば、
> unmodeled data-reduction のアルゴリズムおよびそれから確率モデルとしてそれを、または始まります

### 熟語・専門語

- **generative model**: 生成モデル。データ生成過程を確率的に記述するモデル。

### 要約

- p(y、θ|x) のようなモデル。

## Chunk 0132

### English（抽出4行）

> with the inference from a probability model, considering it as a data-based estimate, and tweaking
> it in some way to improve performance. In Bayesian workﬂow we can move data in and out of the
> model, for example taking an unmodeled predictor x and allowing it to have measurement error,
> so that the model then includes a new level of latent data (Clayton, 1992, Richardson and Gilks,

### 日本語訳（自動翻訳）

> 確率モデルからの推論で、データに基づく推定値として検討し、微調整
> パフォーマンスを向上させる方法もあります。 ベイジアンワークフローでは、データの内外や外を移動することができます。
> モデルは、例えば、非モデル化された予測器xをとり、測定誤差を持たせるため、
> モデルは、新しいレベルのレイトデータ(クレイトン、1992、リチャードソン、ギルクス、

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- 確率モデルからの推論で、データに基づく推定値として検討し、微調整 パフォーマンスを向上させる方法もあります。

## Chunk 0133

### English（抽出4行）

> 1993).
> 3.
> Fitting a model
> Traditionally, Bayesian computation has been performed using a combination of analytic calculation

### 日本語訳（自動翻訳）

> 1993年(平成5年)
> 3。
> モデルに合う
> 伝統的に、ベイジアン計算を組み合わせて行う

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- 1993年(平成5年) 3。

## Chunk 0134

### English（抽出4行）

> and normal approximation. Then in the 1990s, it became possible to perform Bayesian inference
> for a wide range of models using Gibbs and Metropolis algorithms (Robert and Casella, 2011).
> The current state of the art algorithms for ﬁtting open-ended Bayesian models include variational
> inference (Blei and Kucukelbir, 2017), sequential Monte Carlo (Smith, 2013), and Hamiltonian

### 日本語訳（自動翻訳）

> 通常の近似。 その後、1990年代にベイジアン・インフェレンスを実行することが可能になりました
> GibbsとMetropolisアルゴリズム(Robert and Casella, 2011)を使用して、幅広いモデルのモデル。
> オープンエンドのベイジアンモデルをフィッティングするためのアートアルゴリズムの現在の状態には、バリエーションが含まれています
> 推論 (Blei and Kucukelbir, 2017), シーケンシャルモンテカルロ (Smith, 2013), ハミルトニアン

### 熟語・専門語

- **Bayesian inference**: ベイズ推論。事前分布と尤度から事後分布を計算する中核処理。

### 要約

- 通常の近似。

## Chunk 0135

### English（抽出4行）

> Monte Carlo (HMC; Neal, 2011, Betancourt, 2017a). Variational inference is a generalization of
> the expectation-maximization (EM) algorithm and can, in the Bayesian context, be considered as
> providing a fast but possibly inaccurate approximation to the posterior distribution. Variational
> inference is the current standard for computationally intensive models such as deep neural networks.

### 日本語訳（自動翻訳）

> モンテカルロ(HMC;Neal、2011年、Betancourt、2017a)。 変種推論は一般化のことです
> 期待最大化 (EM) アルゴリズムとベイジアンコンテキストで、ベイジアンコンテキストで、
> ポスターの配布に高速で不正確な近似を提供できます。 バリエーション
> インフェレンスは、ディープニューラルネットワークなどの計算式集中型モデルの現状です。

### 熟語・専門語

- **posterior distribution**: 事後分布。データ観測後の未知量の不確実性を表す分布。

### 要約

- モンテカルロ(HMC;Neal、2011年、Betancourt、2017a)。

## Chunk 0136

### English（抽出4行）

> Sequential Monte Carlo is a generalization of the Metropolis algorithm that can be applied to any
> Bayesian computation, and HMC is a diﬀerent generalization of Metropolis that uses gradient
> computation to move eﬃciently through continuous probability spaces.
> In the present article we focus on ﬁtting Bayesian models using HMC and its variants, as

### 日本語訳（自動翻訳）

> シーケンシャル・モンテ・カルロは、メトロポリス・アルゴリズムの一般化で、あらゆる用途に適応できます。
> ベイジアン計算とHMCは、グラデーションを使用するメトロポリスの異なる汎用性です
> 連続確率空間で効率よく動くための計算
> この記事では、HMCとその変種を使用してベイジアンモデルをフィッティングに焦点を当てています。

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- シーケンシャル・モンテ・カルロは、メトロポリス・アルゴリズムの一般化で、あらゆる用途に適応できます。

## Chunk 0137

### English（抽出4行）

> implemented in Stan and other probabilistic programming languages. While similar principles
> should apply also to other software and other algorithms, there will be diﬀerences in the details.
> To safely use an inference algorithm in Bayesian workﬂow, it is vital that the algorithm provides
> strong diagnostics to determine when the computation is unreliable. In the present paper we discuss

### 日本語訳（自動翻訳）

> Stanとその他の確率的プログラミング言語で実装。 同様の原則ながら
> 他のソフトウェアや他のアルゴリズムにも適用する必要があります。詳細は違いがあります。
> ベイジアンワークフローで推論アルゴリズムを安全に使用するためには、アルゴリズムが提供することが重要です。
> 計算が信頼できないときを決定する強い診断。 現在の紙では、我々は議論します

### 熟語・専門語

- **probabilistic programming**: 確率的プログラミング。Stanなどで確率モデルをコードとして記述し推論する方法。

### 要約

- Stanとその他の確率的プログラミング言語で実装。

## Chunk 0138

### English（抽出4行）

> such diagnostics for HMC.
> 3.1.
> Initial values, adaptation, and warmup
> Except in the simplest case, Markov chain simulation algorithms operate in multiple stages. First

### 日本語訳（自動翻訳）

> HMCのためのそのような診断。
> 3.1.
> 初期値、適応、ウォームアップ
> 最も単純なケースを除き、Markovチェーンシミュレーションアルゴリズムは複数のステージで動作します。 ファースト

### 熟語・専門語

- **Markov chain**: マルコフ連鎖。MCMCで事後分布からサンプルを得るための確率過程。

### 要約

- HMCのためのそのような診断。

## Chunk 0139

### English（抽出4行）

> there is a warmup phase which is intended to move the simulations from their possibly unrepresen-
> tative initial values to something closer to the region of parameter space where the log posterior
> density is close to its expected value, which is related to the concept of “typical set” in information
> theory (Carpenter, 2017). Initial values are not supposed to matter in the asymptotic limit, but they

### 日本語訳（自動翻訳）

> おそらく未解釈からシミュレーションを動かすことを意図しているウォームアップ段階があります-
> tative 初期値が、ログ ポスター の領域に近いもの
> 密度は期待値に近いため、情報における「典型的なセット」の概念に関連しています。
> 理論(カルペンター、2017年)。 初期値は、非対称的な限界では重要ではないが、

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- おそらく未解釈からシミュレーションを動かすことを意図しているウォームアップ段階があります- tative 初期値が、ログ ポスター の領域に近いもの 密度は期待値に近いため、情報における「典型的なセット」の概念に関連しています。

## Chunk 0140

### English（抽出4行）

> can matter in practice, and a wrong choice can threaten the validity of the results.
> Also during warmup there needs to be some procedure to set the algorithm’s tuning parameters;
> this can be done using information gathered from the warmup runs. Third is the sampling phase,
> which ideally is run until multiple chains have mixed (Vehtari et al., 2020).

### 日本語訳（自動翻訳）

> 実際には問題があり、間違った選択は結果の妥当性を脅かすことができます。
> またウォームアップ中にアルゴリズムの調整パラメータを設定する手順がいくつかある必要があります。
> これは、ウォームアップランから収集した情報を使用して行うことができます。 第3は見本抽出段階です、
> 複数のチェーンが混合されるまで理想的に実行される(Vehtari et al., 2020).

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- 実際には問題があり、間違った選択は結果の妥当性を脅かすことができます。

## Chunk 0141

### English（抽出4行）

> When ﬁtting a model that has been correctly speciﬁed, warmup thus has two purposes: (a) to
> run through a transient phase to reduce the bias due to dependence on the initial values, and (b)
> to provide information about the target distribution to use in setting tuning parameters. In model
> exploration, warmup has a third role, which is to quickly ﬂag computationally problematic models.

### 日本語訳（自動翻訳）

> 正しく指定されているモデルをフィッティングするとき、ウォームアップは2つの目的を持っています。(a)
> 初期値に依存し、(b) による偏差を減らすために一時的なフェーズを経る
> チューニングパラメータの設定で使用するターゲット分布に関する情報を提供する。 モデル
> 探査、ウォームアップには3番目のロールがあり、それはすぐに計算的に問題のあるモデルをフラグすることです。

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- 正しく指定されているモデルをフィッティングするとき、ウォームアップは2つの目的を持っています。

## Chunk 0142

### English（抽出4行）

> 3.2.
> How long to run an iterative algorithm
> We similarly would like to consider decisions in the operation of iterative algorithms in the context
> of the larger workﬂow. Recommended standard practice is to run at least until bR, the measure

### 日本語訳（自動翻訳）

> 3.2。
> 反復アルゴリズムを実行する長さ
> 同様に、コンテキスト内の反復アルゴリズムの動作に関する決定を検討したいと思います
> より大きなワークフロー。 推奨標準の練習は、少なくともbR、測定まで実行することです

### 熟語・専門語

- **decision**: 意思決定。予測分布を損失・効用・行動選択へ接続する工程。

### 要約

- 3.2。

## Chunk 0143

### English（抽出4行）

> of mixing of chains, is less than 1.01 for all parameters and quantities of interest (Vehtari et al.,
> 2020), and to also monitor the multivariate mixing statistic R∗(Lambert and Vehtari, 2020). There
> are times when earlier stopping can make sense in the early stages of modeling. For example, it
> might seem like a safe and conservative choice to run MCMC until the eﬀective sample size is

### 日本語訳（自動翻訳）

> チェーンの混合は、すべてのパラメータと関心の量(Vehtari et al.、
> 2020年)、多品種混合統計R※(Lambert and Vehtari, 2020)を監視する。 お問い合わせ
> モデリングの初期段階では、止まる時間が経ちます。 例えば、
> 効果的なサンプルサイズまでMCMCを実行するための安全で保守的な選択肢のように見えるかもしれません

### 熟語・専門語

- **ESS**: 有効サンプルサイズ。自己相関を考慮した独立サンプル相当数。

### 要約

- チェーンの混合は、すべてのパラメータと関心の量(Vehtari et al.、 2020年)、多品種混合統計R※(Lambert and Vehtari, 2020)を監視する。

## Chunk 0144

### English（抽出4行）

> in the thousands or Monte Carlo standard error is tiny in comparison to the required precision for
> parameter interpretation—but if this takes a long time, it limits the number of models that can be
> ﬁt in the exploration stage. More often than not, our model also has some big issues (especially
> coding errors) that become apparent after running only a few iterations, so that the remaining

### 日本語訳（自動翻訳）

> 数千またはモンテカルロの標準的な間違いはのための必須の精密と比較して小さいです
> パラメータの解釈—しかし、これが長時間かかる場合、それはできるモデルの数を制限します
> 調査の段階で合います。 多くの場合、私たちのモデルには大きな問題があります(特に
> エラーのコーディング)は、いくつかの反復だけを実行した後に明らかになったので、残りの部分

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- 数千またはモンテカルロの標準的な間違いはのための必須の精密と比較して小さいです パラメータの解釈—しかし、これが長時間かかる場合、それはできるモデルの数を制限します 調査の段階で合います。

## Chunk 0145

### English（抽出4行）

> Computation time
> Distance from
> target distribution
> MCMC

### 日本語訳（自動翻訳）

> 計算の時間
> 距離から
> ターゲット分布
> MCMCMCの特長

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- 計算の時間 距離から ターゲット分布 MCMCMCの特長

## Chunk 0146

### English（抽出4行）

> algorithm
> Approximate algorithm
> Figure 5: Idealized sketch of the tradeoﬀbetween approximate algorithms and MCMC in Bayesian
> computation. If the goal is to get the best ﬁt to the target distribution, MCMC should ultimately

### 日本語訳（自動翻訳）

> アルゴリズム
> 近似アルゴリズム
> 図5: ベイジアンにおけるトレードオフベエン近似アルゴリズムとMCMCの理想的なスケッチ
> 計算。 目標が目標配分に最も合うことであるならば、MCMCは最終的にべきです

### 熟語・専門語

- **approximate**: 近似。速度や扱いやすさのため、正確な推論・モデルを緩めること。

### 要約

- アルゴリズム 近似アルゴリズム 図5: ベイジアンにおけるトレードオフベエン近似アルゴリズムとMCMCの理想的なスケッチ 計算。

## Chunk 0147

### English（抽出4行）

> win out. But if we are currently ﬁtting just one in a series of models, it can make sense to use
> approximate algorithms so as to be able to move through model space more rapidly. Which of
> these algorithms performs better depends on the time budget of the user and where the two curves
> intersect.

### 日本語訳（自動翻訳）

> 勝つ。 しかし、現在、モデルのシリーズで1つだけフィッティングしている場合、使いやすさを作ることができます。
> より迅速にモデル空間を移動できるように、近似アルゴリズム。 のどの
> これらのアルゴリズムは、ユーザの時間の予算と、2つの曲線のタイミングに依存します
> インターセクト。

### 熟語・専門語

- **approximate**: 近似。速度や扱いやすさのため、正確な推論・モデルを緩めること。

### 要約

- 勝つ。

## Chunk 0148

### English（抽出4行）

> computation is wasted. In this respect, running many iterations for a newly-written model is similar
> to premature optimization in software engineering. For the ﬁnal model, the required number of
> iterations depends on the desired Monte Carlo accuracy for the quantities of interest.
> Another choice in computation is how to best make use of available parallelism, beyond the

### 日本語訳（自動翻訳）

> 計算を無駄にしました。 この点では、新品種のイテレーションを多数実施しています。
> ソフトウェアエンジニアリングの早期最適化 最終モデルの場合、必要な数
> 反復は目的のモンテ・カルロの正確さに関心の量によって決まります。
> 計算のもう1つの選択肢は、利用可能な並列の使用を最大限に活用する方法です。

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- 計算を無駄にしました。

## Chunk 0149

### English（抽出4行）

> default of running 4 or 8 separate chains on multiple cores. Instead of increasing the number of
> iterations, eﬀective variance reduction can also be obtained by increasing the number of parallel
> chains (see, e.g., Hoﬀman and Ma, 2020).
> 3.3.

### 日本語訳（自動翻訳）

> 複数のコアで4つまたは8つの別々のチェーンを実行するデフォルト。 数を増やす代わりに
> 反復、有効な分散の減少は平行の数を高めることによってまた得ることができます
> チェーン(Hoffman, Ma, 2020など)
> 3.3.

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- 複数のコアで4つまたは8つの別々のチェーンを実行するデフォルト。

## Chunk 0150

### English（抽出4行）

> Approximate algorithms and approximate models
> Bayesian inference typically involves intractable integrals, hence the need for approximations.
> Markov chain simulation is a form of approximation where the theoretical error approaches zero
> as the number of simulations increases. If our chains have mixed, we can make a good estimate

### 日本語訳（自動翻訳）

> 近似アルゴリズムと近似モデル
> ベイジアン・インフェレンス(Bayesian Inference)は、通常、引き込み式のインテグレータを伴います。したがって、近似の必要性が伴います。
> Markovチェーンシミュレーションは、理論的なエラーがゼロに近づく近似の形態です
> シミュレーションの回数が増える。 連鎖が混在している場合は、良いお見積りができます。

### 熟語・専門語

- **Bayesian inference**: ベイズ推論。事前分布と尤度から事後分布を計算する中核処理。
- **Markov chain**: マルコフ連鎖。MCMCで事後分布からサンプルを得るための確率過程。
- **approximate**: 近似。速度や扱いやすさのため、正確な推論・モデルを緩めること。

### 要約

- 近似アルゴリズムと近似モデル ベイジアン・インフェレンス(Bayesian Inference)は、通常、引き込み式のインテグレータを伴います。

## Chunk 0151

### English（抽出4行）

> of the Monte Carlo standard error (Vehtari et al., 2020), and for practical purposes we often treat
> these computations as exact.
> Unfortunately, running MCMC to convergence is not always a scalable solution as data and
> models get large, hence the desire for faster approximations. Figure 5 shows the resulting tradeoﬀ

### 日本語訳（自動翻訳）

> モンテカルロの標準的な間違い(Vehtari et al.、2020)のそして実用的な目的のために私達は頻繁に扱う
> これらを正確に計算します。
> 残念ながら、MCMCをコンバージェンスに実行することは、常にデータとしてスケーラブルなソリューションではありません。
> モデルが大きくなるので、見積りが早くなりたい。 図5は、結果のトレードオフを示しています

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- モンテカルロの標準的な間違い(Vehtari et al.、2020)のそして実用的な目的のために私達は頻繁に扱う これらを正確に計算します。

## Chunk 0152

### English（抽出4行）

> between speed and accuracy. This graph is only conceptual; in a real problem, the positions of
> these lines would be unknown, and indeed in some problems an approximate algorithm can perform
> worse than MCMC even at short time scales.
> Depending on where we are in the workﬂow, we have diﬀerent requirements of our computed

### 日本語訳（自動翻訳）

> 速度と精度の間。 このグラフは概念的です。実際の問題では、位置は
> これらの行は不明で、確かに近似アルゴリズムが実行できる問題があります
> ショートタイムスケールでもMCMCよりも悪い。
> ワークフローのどこにいるかに応じて、私たちは計算の異なる要件を持っています

### 熟語・専門語

- **approximate**: 近似。速度や扱いやすさのため、正確な推論・モデルを緩めること。

### 要約

- 速度と精度の間。

## Chunk 0153

### English（抽出4行）

> posteriors. Near the end of the workﬂow, where we are examining ﬁne-scale and delicate features,
> we require accurate exploration of the posterior distribution. This usually requires MCMC. On the
> other hand, at the beginning of the workﬂow, we can frequently make our modeling decisions based
> on large-scale features of the posterior that can be accurately estimated using relatively simple

### 日本語訳（自動翻訳）

> ポスター。 ワークフローの最後には、細かな機能と繊細な機能を検討しています。
> ポスター分布の正確な探査が必要です。 これは通常MCMCが必要です。 とりあえず
> 一方、ワークフローの先頭では、モデリングの決定をベースにすることで、
> 比較的簡単な使い方を正確に推定できるポスターの大規模な機能

### 熟語・専門語

- **posterior distribution**: 事後分布。データ観測後の未知量の不確実性を表す分布。
- **decision**: 意思決定。予測分布を損失・効用・行動選択へ接続する工程。

### 要約

- ポスター。

## Chunk 0154

### English（抽出4行）

> methods such as empirical Bayes, linearization or Laplace approximation, nested approximations
> like INLA (Rue et al., 2009), or even sometimes data-splitting methods like expectation propagation
> (Vehtari, Gelman, Siivola, et al., 2020), mode-ﬁnding approximations like variational inference
> (Kucukelbir et al., 2017), or penalized maximum likelihood. The point is to use a suitable tool for

### 日本語訳（自動翻訳）

> 帝国湾、線形化、または場所近似などの方法、ネスト近似
> INLA (Rue et al., 2009) や、期待の伝搬のようなデータ分割方法など
> (Vehtari, Gelman, Siivola, et al., 2020), 変動推論などのモードファインディング
> (Kucukelbir et al., 2017), または最大の可能性を罰. ポイントは、適切なツールを使用する

### 熟語・専門語

- **likelihood**: 尤度。パラメータが与えられたときデータがどれだけ起こりやすいか。

### 要約

- 帝国湾、線形化、または場所近似などの方法、ネスト近似 INLA (Rue et al., 2009) や、期待の伝搬のようなデータ分割方法など (Vehtari, Gelman, Siivola, et al., 2020), 変動推…

## Chunk 0155

### English（抽出4行）

> the job and to not try to knock down a retaining wall using a sculptor’s chisel.
> All of these approximate methods have at least a decade of practical experience, theory, and
> diagnostics behind them. There is no one-size-ﬁts-all approximate inference algorithm, but when
> a workﬂow includes relatively well-understood components such as generalized linear models,

### 日本語訳（自動翻訳）

> 彫刻家のキゼルを使って、保留壁をノックダウンしようとしない。
> これらすべての近似メソッドは、少なくとも10年以上の実用的な経験、理論、および
> それらの背後にある診断。 1つのサイズのfits-all近似推論アルゴリズムはありませんが、いつ
> ワークフローには、一般的なリニアモデルなどの比較的よく使われるコンポーネントが含まれます。

### 熟語・専門語

- **approximate**: 近似。速度や扱いやすさのため、正確な推論・モデルを緩めること。

### 要約

- 彫刻家のキゼルを使って、保留壁をノックダウンしようとしない。

## Chunk 0156

### English（抽出4行）

> multilevel regression, autoregressive time series models, or Gaussian processes, it is often possi-
> ble to construct an appropriate approximate algorithm. Furthermore, depending on the speciﬁc
> approximation being used, generic diagnostic tools described by Yao et al. (2018a) and Talts et al.
> (2020) can be used to verify that a particular approximate algorithm reproduces the features of the

### 日本語訳（自動翻訳）

> マルチレベルの回帰、自動回帰時間シリーズモデル、またはガウスのプロセスは、多くの場合、possi-
> 適切な近似アルゴリズムを構築できます。 さらに、具体的な内容に応じて
> ヤオ・エ・アル((2018a)、タルト・エ・アル(Talts et al)が説明する一般的な診断ツールとして用いられている近似。
> (2020) 特定の近似アルゴリズムが機能の再現を検証するために使用できる

### 熟語・専門語

- **ESS**: 有効サンプルサイズ。自己相関を考慮した独立サンプル相当数。
- **approximate**: 近似。速度や扱いやすさのため、正確な推論・モデルを緩めること。

### 要約

- マルチレベルの回帰、自動回帰時間シリーズモデル、またはガウスのプロセスは、多くの場合、possi- 適切な近似アルゴリズムを構築できます。

## Chunk 0157

### English（抽出4行）

> posterior that you care about for a speciﬁc model.
> An alternative view is to understand an approximate algorithm as an exact algorithm for an
> approximate model. In this sense, a workﬂow is a sequence of steps in an abstract computational
> scheme aiming to infer some ultimate, unstated model. More usefully, we can think of things

### 日本語訳（自動翻訳）

> 特定のモデルに気付いたポスター。
> 代替ビューは、近似アルゴリズムを正確なアルゴリズムとして理解することです。
> 近似モデル。 この意味では、ワークフローは抽象的な計算のステップのシーケンスです
> 究極の未定モデルを推論するスキーム。 もっと便利で、物事を考えることができます

### 熟語・専門語

- **approximate**: 近似。速度や扱いやすさのため、正確な推論・モデルを緩めること。

### 要約

- 特定のモデルに気付いたポスター。

## Chunk 0158

### English（抽出4行）

> like empirical Bayes approximations as replacing a model’s prior distributions with a particular
> data-dependent point-mass prior. Similarly a Laplace approximation can be viewed as a data-
> dependent linearization of the desired model, while a nested Laplace approximation (Rue et al.,
> 2009, Margossian et al., 2020a) uses a linearized conditional posterior in place of the posited

### 日本語訳（自動翻訳）

> 特定のモデルの事前分布を置き換えるような帝国湾の近似
> 前のデータに依存するポイント・マス。 同様に、Laplaceの近似はデータとして見ることができます-
> 目的のモデルの依存線形化、ネストされたランス近似(Rue et al.)
> 2009年、Margosian et al.、2020a) は posited の場所で線形化された条件のポスターを使用します

### 熟語・専門語

- **prior distribution**: 事前分布。データ観測前の知識・制約を表す分布。

### 要約

- 特定のモデルの事前分布を置き換えるような帝国湾の近似 前のデータに依存するポイント・マス。

## Chunk 0159

### English（抽出4行）

> conditional posterior.
> 3.4.
> Fit fast, fail fast
> An important intermediate goal is to be able to fail fast when ﬁtting bad models. This can be

### 日本語訳（自動翻訳）

> 条件付きポスター。
> 3.4.
> 速い適合は、速く失敗します
> 重要な中間目標は、悪いモデルをフィッティングするときに迅速に失敗することができることです。 これは、

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- 条件付きポスター。

## Chunk 0160

### English（抽出4行）

> considered as a shortcut that avoids spending a lot of time for (near) perfect inference for a bad
> model. There is a large literature on approximate algorithms to ﬁt the desired model fast, but little
> on algorithms designed to waste as little time as possible on the models that we will ultimately
> abandon. We believe it is important to evaluate methods on this criterion, especially because

### 日本語訳（自動翻訳）

> 悪いために多くの時間を費やすことを回避するショートカットとして考えられます(笑) 完璧な推論
> モデル。 目的のモデルに速く合うために近似アルゴリズムに大きい文献がありますが、少し
> 究極のモデルでできるだけ少し時間を無駄にするように設計されたアルゴリズム
> アバンドン。 私たちは、特にこの基準で方法を評価することが重要です。

### 熟語・専門語

- **approximate**: 近似。速度や扱いやすさのため、正確な推論・モデルを緩めること。

### 要約

- 悪いために多くの時間を費やすことを回避するショートカットとして考えられます(笑) 完璧な推論 モデル。

## Chunk 0161

### English（抽出4行）

> inappropriate and poorly ﬁtting models can often be more diﬃcult to ﬁt.
> For a simple idealized example, suppose you are an astronomer several centuries ago ﬁtting
> ellipses to a planetary orbit based on 10 data points measured with error. Figure 6a shows the sort
> of data that might arise, and just about any algorithm will ﬁt reasonably well. For example, you

### 日本語訳（自動翻訳）

> 不適切なフィッティングモデルは、装着が困難になる場合があります。
> 単純な理想化例では、数世紀前にフィッティングされたアストロンマーです。
> エラーで測定された10のデータポイントに基づいて惑星軌道に楕円します。 図6aはソートを示しています
> 任意のアルゴリズムが合理的に収まる可能性があるデータ。 例えば、

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- 不適切なフィッティングモデルは、装着が困難になる場合があります。

## Chunk 0162

### English（抽出4行）

> could take various sets of ﬁve points and ﬁt the exact ellipse to each, and then take the average of
> these ﬁts. Or you could ﬁt an ellipse to the ﬁrst ﬁve points, then perturb it slightly to ﬁt the sixth
> point, then perturb that slightly to ﬁt the seventh, and so forth. Or you could implement some sort
> of least squares algorithm.

### 日本語訳（自動翻訳）

> 5つのポイントのさまざまなセットを取り、それぞれに正確な楕円に合い、そして平均を取ることができます
> これらの適合。 または、最初の5つのポイントに楕円を合わせることができ、6番目の点に収まるのに少しひっくり返します
> ポイント, その後、7th に収まるために少し perturb, 等. または、いくつかのソートを実行できます
> 少なくとも正方形のアルゴリズム。

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- 5つのポイントのさまざまなセットを取り、それぞれに正確な楕円に合い、そして平均を取ることができます これらの適合。

## Chunk 0163

### English（抽出4行）

> Now suppose some Death Star comes along and alters the orbit—in this case, we are purposely
> choosing an unrealistic example to create a gross discrepancy between model and data—so that
> your 10 data points look like Figure 6b. In this case, convergence will be much harder to attain.
> If you start with the ellipse ﬁt to the ﬁrst ﬁve points, it will be diﬃcult to take any set of small

### 日本語訳（自動翻訳）

> 今、いくつかのデススターが一緒に来て、軌道を変更します - この場合、我々は意図的に
> モデルとデータの間のグロスの矛盾を作成するために、非現実的な例を選ぶ
> 図6bのように、10つのデータポイントが見えます。 この場合、コンバージェンスは達成するのがはるかに困難になります。
> 楕円で最初の5点に収まると、小さめのセットを取らない

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- 今、いくつかのデススターが一緒に来て、軌道を変更します - この場合、我々は意図的に モデルとデータの間のグロスの矛盾を作成するために、非現実的な例を選ぶ 図6bのように、10つのデータポイントが見えます。

## Chunk 0164

### English（抽出4行）

> perturbations that will allow the curve to ﬁt the later points in the series. But, more than that, even
> if you could obtain a least squares solution, any ellipse would be a terrible ﬁt to the data. It’s just
> an inappropriate model. If you ﬁt an ellipse to these data, you should want the ﬁt to fail fast so you
> Figure 6: Illustration of the need for “ﬁt fast, fail fast”: (a) Idealized data representing measure-

### 日本語訳（自動翻訳）

> 曲線がシリーズの後にポイントに収まることを可能にするパーチュレーション。 でも、それよりも、
> 少なくとも四角形溶液を得られることができれば、楕円はデータにひどくフィットします。 それだけです
> 不適切なモデル。 これらのデータに楕円を合えば、あなたはあなたが速く失敗するフィットを望むはずです
> 図6:「速くフィットし、高速失敗」の必要性の実例:(a)測定を表す理想化されたデータ-

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- 曲線がシリーズの後にポイントに収まることを可能にするパーチュレーション。

## Chunk 0165

### English（抽出4行）

> ments of planetary orbit which could be ﬁt as an ellipse with measurement error, (b) Measurements
> of a hypothetical orbit that was perturbed by a Death Star. In the second example, it would be
> challenging to ﬁt a single ellipse to the data—but we have no particular interest in an omnibus
> elliptical ﬁt in any case. We would like any attempt to ﬁt an ellipse to the second dataset to fail fast.

### 日本語訳（自動翻訳）

> 測定の間違い(b)の測定と楕円として合うことができる惑星軌道のments
> 死星に耐えられた仮説軌道。 2番目の例では、
> 単一の楕円をデータに収まるのに挑戦するが、私たちはオムニバスに特に関心がありません
> あらゆる場合の楕円適合。 2 番目のデータセットに ellipse を合わせると、高速に失敗します。

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- 測定の間違い(b)の測定と楕円として合うことができる惑星軌道のments 死星に耐えられた仮説軌道。

## Chunk 0166

### English（抽出4行）

> can quickly move on to something more reasonable.
> This example has, in extreme form, a common pattern of diﬃcult statistical computations, that
> ﬁtting to diﬀerent subsets of the data yields much diﬀerent parameter estimates.
> 4.

### 日本語訳（自動翻訳）

> より合理的に何かに移すことができます。
> この例は、極端な形で、困難な統計計算の一般的なパターンであり、
> データの異なるサブセットへのフィッティングは、はるかに異なるパラメータの推定値になります。
> 4。

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- より合理的に何かに移すことができます。

## Chunk 0167

### English（抽出4行）

> Using constructed data to find and understand problems
> The ﬁrst step in validating computation is to check that the model actually ﬁnishes the ﬁtting
> process in an acceptable time frame and the convergence diagnostics are reasonable. In the context
> of HMC, this is primarily the absence of divergent transitions, bR diagnostic near 1, and suﬃcient

### 日本語訳（自動翻訳）

> 構築されたデータを使用して、問題の発見と理解
> 計算を検証する最初のステップは、モデルが実際にフィッティングを終了していることを確認することです
> 受諾可能な時間のフレームおよびconvergenceの診断のプロセスは適度です。 コンテキストで
> HMCの、これは主に1近くdivergent転移、bRの診断の不在であり、十分です

### 熟語・専門語

- **divergent**: divergence。HMC/NUTSで幾何が悪く積分が破綻した警告。
- **ESS**: 有効サンプルサイズ。自己相関を考慮した独立サンプル相当数。

### 要約

- 構築されたデータを使用して、問題の発見と理解 計算を検証する最初のステップは、モデルが実際にフィッティングを終了していることを確認することです 受諾可能な時間のフレームおよびconvergenceの診断のプロセスは適度です。

## Chunk 0168

### English（抽出4行）

> eﬀective sample sizes for the central tendency, the tail quantiles, and the energy (Vehtari et al.,
> 2020). However, those diagnostics cannot protect against a probabilistic program that is computed
> correctly but encodes a diﬀerent model than the user intended.
> The main tool we have for ensuring that the statistical computation is done reasonably well is

### 日本語訳（自動翻訳）

> 中央傾向、尾のquantilesおよびエネルギー(Vehtari et al)のための有効なサンプル サイズ。
> 2020年1月1日 しかし、これらの診断は、計算されている確率的プログラムから保護することはできません
> 正しくではなく、意図したユーザーよりも異なるモデルをエンコードします。
> 統計計算が合理的にうまく行われることを確実にするための主要なツールは、

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- 中央傾向、尾のquantilesおよびエネルギー(Vehtari et al)のための有効なサンプル サイズ。

## Chunk 0169

### English（抽出4行）

> to actually ﬁt the model to some data and check that the ﬁt is good. Real data can be awkward for
> this purpose because modeling issues can collide with computational issues and make it impossible
> to tell if the problem is the computation or the model itself. To get around this challenge, we ﬁrst
> explore models by ﬁtting them to simulated data.

### 日本語訳（自動翻訳）

> 実際にモデルをいくつかのデータに収まり、適合が良好であることを確認してください。 実際のデータは、
> 課題をモデル化し、計算上の問題に対処することができるため、この目的
> 問題が計算かモデル自体であるかを言うため。 この課題を解決するため、まずは
> 模擬したデータをフィッティングすることでモデルを探ります。

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- 実際にモデルをいくつかのデータに収まり、適合が良好であることを確認してください。

## Chunk 0170

### English（抽出4行）

> 4.1.
> Fake-data simulation
> Working in a controlled setting where the true parameters are known can help us understand our
> data model and priors, what can be learned from an experiment, and the validity of the applied

### 日本語訳（自動翻訳）

> 4.1.
> 偽データシミュレーション
> 真のパラメータが知られているコントロールされた設定で作業することは、私たちを理解するのに役立ちます
> データモデルと優先順位、実験から学んだこと、および適用の妥当性

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- 4.1. 偽データシミュレーション 真のパラメータが知られているコントロールされた設定で作業することは、私たちを理解するのに役立ちます データモデルと優先順位、実験から学んだこと、および適用の妥当性

## Chunk 0171

### English（抽出4行）

> inference methods. The basic idea is to check whether our procedure recovers the correct parameter
> values when ﬁtting fake data. Typically we choose parameter values that seem reasonable a priori
> and then simulate a fake dataset of the same size, shape, and structure as the original data. We next
> ﬁt the model to the fake data to check several things.

### 日本語訳（自動翻訳）

> 推論方法。 基本的な考え方は、当社の手順が正しいパラメータを回復するかどうかを確認することです
> 偽物データをフィッティングするときの値。 一般的には、合理的に優先するようなパラメータ値を選択します。
> そして、元のデータと同じサイズの偽のデータセット、形および構造を模倣して下さい。 次へ
> 偽物データにモデルを合わせ、いくつかのものを確認します。

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- 推論方法。

## Chunk 0172

### English（抽出4行）

> The ﬁrst thing we check isn’t strictly computational, but rather an aspect of the design of the data.
> For all parameters, we check to see if the observed data are able to provide additional information
> beyond the prior. The procedure is to simulate some fake data from the model with ﬁxed, known
> parameters and then see whether our method comes close to reproducing the known truth. We can

### 日本語訳（自動翻訳）

> 最初にチェックするのは、厳密に計算ではなく、データの設計の側面ではありません。
> すべてのパラメータについては、観察されたデータが追加情報を提供できるかどうかを確認します。
> 前のことを超えて。 手順は、既定の既知のモデルからいくつかの偽のデータをシミュレートすることです
> パラメータは、私たちの方法は、既知の真実を再現するために近づいているかどうかを確認します。 お問い合わせ

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- 最初にチェックするのは、厳密に計算ではなく、データの設計の側面ではありません。

## Chunk 0173

### English（抽出4行）

> look at point estimates and also the coverage of posterior intervals.
> If our fake-data check fails, in the sense that the inferences are not close to the assumed parameter
> values or if there seem to be model components that are not gaining any information from the data
> (Lindley, 1956, Goel and DeGroot, 1981), we recommend breaking down the model. Go simpler

### 日本語訳（自動翻訳）

> ポイント見積りや、ポスターの間隔のカバレッジを見てください。
> 偽データチェックが失敗すると、推論が想定されたパラメータに近接しないという意味で
> 値またはデータから情報を得ることができないモデルコンポーネントがあるかどうか
> (リンドリー、1956年、ゴエルとデグルート、1981年)、モデルを分解することをお勧めします。 シンプルに

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- ポイント見積りや、ポスターの間隔のカバレッジを見てください。

## Chunk 0174

### English（抽出4行）

> and simpler until we get the model to work. Then, from there, we can try to identify the problem,
> as illustrated in Section 5.2.
> The second thing that we check is if the true parameters can be recovered to roughly within
> the uncertainty implied by the ﬁtted posterior distribution. This will not be possible if the data

### 日本語訳（自動翻訳）

> 作業するモデルを得られるまでシンプルに。 それから、そこから、問題を特定しようとします。
> セクション5.2で示されるように。
> 私たちがチェックする2つ目は、真のパラメータが大体に回復できるかどうかです。
> 適合したポスター分配による不確実性。 データがない場合は可能です

### 熟語・専門語

- **posterior distribution**: 事後分布。データ観測後の未知量の不確実性を表す分布。
- **uncertainty**: 不確実性。観測・パラメータ・モデル構造・意思決定に残る曖昧さ。

### 要約

- 作業するモデルを得られるまでシンプルに。

## Chunk 0175

### English（抽出4行）

> are not informative for a parameter, but it should typically happen otherwise. It is not possible
> to run a single fake data simulation, compute the associated posterior distribution, and declare
> that everything works well. We will see in the next section that a more elaborate setup is needed.
> However, a single simulation run will often reveal blatant errors. For instance, if the code has an

### 日本語訳（自動翻訳）

> パラメータは非公式ではありませんが、通常はそうでなければいけません。 可能です。
> 単一の偽物データシミュレーションを実行し、関連するポスター分布を計算し、宣言する
> すべてがうまくいく。 次のセクションでは、より精巧なセットアップが必要なセクションが表示されます。
> しかしながら、ひとつのシミュレーション実行では、空っぽのエラーを明らかにすることが多い。 例えば、コードにコードが存在している場合

### 熟語・専門語

- **posterior distribution**: 事後分布。データ観測後の未知量の不確実性を表す分布。

### 要約

- パラメータは非公式ではありませんが、通常はそうでなければいけません。

## Chunk 0176

### English（抽出4行）

> error in it and ﬁts the wrong model this will often be clear from a catastrophic failure of parameter
> recovery.
> The third thing that we can do is use fake data simulations to understand how the behavior
> of a model can change across diﬀerent parts of the parameter space. In this sense, a statistical

### 日本語訳（自動翻訳）

> それに誤ったモデルに収まると、これはしばしばパラメータの壊滅的な失敗から明らかになります
> 回復。
> 私たちができることの3分の1は、偽のデータのシミュレーションを使用して行動を理解しています
> パラメータ空間の異なる部分にモデルを変更できます。 この意味では、統計的

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- それに誤ったモデルに収まると、これはしばしばパラメータの壊滅的な失敗から明らかになります 回復。

## Chunk 0177

### English（抽出4行）

> model can contain many stories of how the data get generated. As illustrated in Section 5.9, the
> data are informative about the parameters for a sum of declining exponentials when the exponents
> are well separated, but not so informative when the two components are close to each other. This
> sort of instability contingent on parameter values is also a common phenomenon in diﬀerential

### 日本語訳（自動翻訳）

> 生成されたデータがいくつあるかをモデルに含めることができます。 セクション5.9で示されているように、
> データは、指数関数が指数関数のときの降順指数の合計のパラメータについて非公式です
> 2つのコンポーネントが互いに閉じているとき、よく分かれますが、それほど有益ではありません。 お問い合わせ
> パラメータ値の整合性は、差動の一般的な現象です

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- 生成されたデータがいくつあるかをモデルに含めることができます。

## Chunk 0178

### English（抽出4行）

> equation models, as can been seen in Section 11. For another example, the posterior distribution
> of a hierarchical model looks much diﬀerent at the neck than at the mouth of the funnel geometry
> implied by the hierarchical prior. Similar issues arise in Gaussian process models, depending on
> the length scale of the process and the resolution of the data.

### 日本語訳（自動翻訳）

> 式モデルは、セクション11で見ることができるように。 別の例では、ポスター配布
> 階層モデルは、漏斗幾何学の口よりも首ではるかに異なります
> 階層的な優先順位で暗示される。 Gaussianプロセスモデルで発生する同様の問題
> プロセスの長さとデータの解像度。

### 熟語・専門語

- **posterior distribution**: 事後分布。データ観測後の未知量の不確実性を表す分布。
- **ESS**: 有効サンプルサイズ。自己相関を考慮した独立サンプル相当数。

### 要約

- 式モデルは、セクション11で見ることができるように。

## Chunk 0179

### English（抽出4行）

> All this implies that fake data simulation can be particularly relevant in the zone of the parameter
> space that is predictive of the data. This in turn suggests a two-step procedure in which we ﬁrst
> ﬁt the model to real data, then draw parameters from the resulting posterior distribution to use in
> fake-data checking. The statistical properties of such a procedure are unclear but in practice we

### 日本語訳（自動翻訳）

> これは、偽のデータシミュレーションは、パラメータのゾーンに特に関連性があることを意味しています
> データを予測する空間。 これは、順番に私たちが最初に2ステップの手順を提案します
> モデルを実際のデータに合わせ、その結果のあるポスター分布からパラメータを描画して使用
> 偽データチェック そのような手順の統計的特性は不明ですが、慣行では、我々は

### 熟語・専門語

- **posterior distribution**: 事後分布。データ観測後の未知量の不確実性を表す分布。

### 要約

- これは、偽のデータシミュレーションは、パラメータのゾーンに特に関連性があることを意味しています データを予測する空間。

## Chunk 0180

### English（抽出4行）

> have found such checks to be helpful, both for revealing problems with the computation or model,
> and for providing some reassurance when the fake-data-based inferences do reproduce the assumed
> parameter value.
> To carry this idea further, we may break our method by coming up with fake data that cause

### 日本語訳（自動翻訳）

> 計算やモデルの問題を明らかにするために、そのようなチェックが有用であることが判明しました。
> 偽データベースのインフェレンスが仮定を再現したときに、いくつかの安心を提供するため
> パラメータ値。
> このアイデアをさらに持ち運ぶには、偽物データが起きて来ることによって、当社の方法が壊れる場合があります。

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- 計算やモデルの問題を明らかにするために、そのようなチェックが有用であることが判明しました。

## Chunk 0181

### English（抽出4行）

> our procedure to give bad answers. This sort of simulation-and-exploration can be the ﬁrst step in
> a deeper understanding of an inference method, which can be valuable even for a practitioner who
> plans to use this method for just one applied problem. It can also be useful for building up a set of
> more complex models to possibly explore later.

### 日本語訳（自動翻訳）

> 悪い回答を与えるための手順。 この種のシミュレーションと探査は、最初のステップで行うことができます
> 開業医にとっても価値ある「推論法」の深い理解
> 1つの適用問題だけのためにこの方法を使用することを計画して下さい。 1組の組み立てにも便利です
> 後で探すことができるより複雑なモデル。

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- 悪い回答を与えるための手順。

## Chunk 0182

### English（抽出4行）

> Fake-data simulation is a crucial component of our workﬂow because it is, arguably, the only
> point where we can directly check that our inference on latent variables is reliable. When ﬁtting the
> model to real data, we do not by deﬁnition observe the latent variables. Hence we can only evaluate
> how our model ﬁts the observed data. If our goal is not merely prediction but estimating the latent

### 日本語訳（自動翻訳）

> Fake-data シミュレーションは、ワークフローの重要なコンポーネントです。つまり、
> 潜在変数の推論が信頼できることを直接点検できるところ。 フィッティング時
> 実際のデータをモデル化し、定義では、潜在変数を観察しない。 したがって、我々は唯一の評価することができます
> 当社のモデルが観察されたデータに適合する方法。 私たちの目標が単なる予測ではなく、潜伏を推定していない場合

### 熟語・専門語

- **prediction**: 予測。未知/将来/除外データに対する分布や点推定。

### 要約

- Fake-data シミュレーションは、ワークフローの重要なコンポーネントです。

## Chunk 0183

### English（抽出4行）

> variables, examining predictions only helps us so much. This is especially true of overparameterized
> models, where wildly diﬀerent parameter values can yield comparable predictions (e.g. Section 5.9
> and Gelman et al, 1996).
> In general, even when the model ﬁt is good, we should only draw

### 日本語訳（自動翻訳）

> 変数、予測を調べるだけで、私たちを助けます。 これは、特に過分化の本当です
> 野生の異なるパラメータ値が比較可能な予測をもたらすモデル(セクション5.9など)
> そしてゲルマンら、1996)。
> 一般的には、モデルのフィットが良好であっても、描画のみ

### 熟語・専門語

- **prediction**: 予測。未知/将来/除外データに対する分布や点推定。

### 要約

- 変数、予測を調べるだけで、私たちを助けます。

## Chunk 0184

### English（抽出4行）

> conclusions about the estimated latent variables with caution. Fitting the model to simulated data
> helps us better understand what the model can and cannot learn about the latent process in a
> controlled setting where we know the ground truth. If a model is able to make good inference
> on fake-data generated from that very model, this provides no guarantee that its inference on real

### 日本語訳（自動翻訳）

> 計算による推定遅延変数に関する結論。 模倣されたデータにモデルに合う
> モデルができることを理解し、ランタンプロセスについて学ぶことができないのに役立つ
> 地上の真理を知っている制御設定。 モデルがよい推論をすることができれば
> その非常にモデルから生成された偽物データでは、これは実際のところその推論を保証するものではありません

### 熟語・専門語

- **ESS**: 有効サンプルサイズ。自己相関を考慮した独立サンプル相当数。

### 要約

- 計算による推定遅延変数に関する結論。

## Chunk 0185

### English（抽出4行）

> data will be sensible. But if a model is unable to make good inference on such fake data, then it’s
> hopeless to expect the model to provide reasonable inference on real data. Fake-data simulations
> provide an upper bound of what can be learned about a latent process.
> 4.2.

### 日本語訳（自動翻訳）

> データをセンシブルにします。 しかし、そのような偽物データにモデルが劣らない場合、それは
> 実際のデータに対する妥当な推論を提供するモデルを期待しない限り。 偽データシミュレーション
> 潜伏プロセスについて学ぶことができるものの上限の境界を提供します。
> 4.2 .

### 熟語・専門語

- **ESS**: 有効サンプルサイズ。自己相関を考慮した独立サンプル相当数。

### 要約

- データをセンシブルにします。

## Chunk 0186

### English（抽出4行）

> Simulation-based calibration
> There is a formal, and at times practical, issue when comparing the result of Bayesian inference, a
> posterior distribution, to a single (true) point, as illustrated in Figure 7.
> Using a single fake data simulation to test a model will not necessarily “work,” even if the

### 日本語訳（自動翻訳）

> シミュレーションベースの校正
> 正式で、時には実用的な問題があります。ベイジアンの推論の結果を比較するとき、
> ポスター分布、図7に示すように、単一の(true)ポイントに、
> モデルをテストするために単一の偽物データシミュレーションを使用して、必ずしも「仕事」ではなく、

### 熟語・専門語

- **Bayesian inference**: ベイズ推論。事前分布と尤度から事後分布を計算する中核処理。
- **simulation-based calibration**: SBC。シミュレーション真値と事後rankを比べ、実装・推論の校正を検査する方法。
- **posterior distribution**: 事後分布。データ観測後の未知量の不確実性を表す分布。
- **ESS**: 有効サンプルサイズ。自己相関を考慮した独立サンプル相当数。

### 要約

- シミュレーションベースの校正 正式で、時には実用的な問題があります。

## Chunk 0187

### English（抽出4行）

> computational algorithm is working correctly. The problem here arises not just because with one
> simulation anything can happen (there is a 5% chance that a random draw will be outside a 95%
> uncertainty interval) but also because Bayesian inference will in general only be calibrated when
> averaging over the prior, not for any single parameter value. Furthermore, parameter recovery may

### 日本語訳（自動翻訳）

> 計算アルゴリズムは正しく機能します。 ここの問題は、一つだけでは消えません
> シミュレーションは何でも起こります(ランダムな描画は95%外になる5%チャンスです)
> 不確実性の間隔)しかしまたベイジアンの本質が一般的なときだけ校正されるので
> 任意のパラメータ値ではなく、前の値を上回る。 さらに、パラメータの回復はかもしれない

### 熟語・専門語

- **Bayesian inference**: ベイズ推論。事前分布と尤度から事後分布を計算する中核処理。
- **uncertainty**: 不確実性。観測・パラメータ・モデル構造・意思決定に残る曖昧さ。

### 要約

- 計算アルゴリズムは正しく機能します。

## Chunk 0188

### English（抽出4行）

> fail not because the algorithm fails, but because the observed data are not providing information
> that could update the uncertainty quantiﬁed by the prior for a particular parameter. If the prior
> and posterior are approximately unimodal and the chosen parameter value is from the center of the
> prior, we can expect overcoverage of posterior intervals.

### 日本語訳（自動翻訳）

> アルゴリズムが失敗するので失敗しますが、観察されたデータは情報を提供していないため
> 特定のパラメータの事前によって定量化される不確実性を更新できます。 前の場合
> および Posterior は unimodal およそであり、選ばれた変数は中心からあります
> 前回は、ポスターの間隔を覆うことを期待できます。

### 熟語・専門語

- **uncertainty**: 不確実性。観測・パラメータ・モデル構造・意思決定に残る曖昧さ。
- **approximate**: 近似。速度や扱いやすさのため、正確な推論・モデルを緩めること。

### 要約

- アルゴリズムが失敗するので失敗しますが、観察されたデータは情報を提供していないため 特定のパラメータの事前によって定量化される不確実性を更新できます。

## Chunk 0189

### English（抽出4行）

> A more comprehensive approach than what we present in Section 4.1 is simulation-based
> calibration (SBC; Cook et al., 2006, Talts et al., 2020). In this scheme, the model parameters are
> drawn from the prior; then data are simulated conditional on these parameter values; then the model
> is ﬁt to data; and ﬁnally the obtained posterior is compared to the simulated parameter values that

### 日本語訳（自動翻訳）

> セクション4.1に存在するものよりも、より包括的なアプローチはシミュレーションベースです。
> キャリブレーション(SBC;クックet al.、2006、Talts et al.、2020)。 このスキームでは、モデルパラメータは
> これらのパラメータ値でデータをシミュレートします。その後、モデル
> データに合致し、最終的に得られたポスターはシミュレートされたパラメータ値と比較している

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- セクション4.1に存在するものよりも、より包括的なアプローチはシミュレーションベースです。

## Chunk 0190

### English（抽出4行）

> were used to generate the data. By repeating this procedure several times, it is possible to check
> the coherence of the inference algorithm. The idea is that by performing Bayesian inference across
> a range of datasets simulated using parameters drawn from the prior, we should recover the prior.
> Simulation-based calibration is useful to evaluate how closely approximate algorithms match the

### 日本語訳（自動翻訳）

> データを生成するために使用されます。 この手順を複数回繰り返すことで、
> 推論アルゴリズムの一貫性。 アイデアは、ベイジアンの本質を貫くことで、
> 前のパラメータから描画されたパラメータを使用してシミュレートされたデータセットの範囲は、事前に回復する必要があります。
> シミュレーションベースのキャリブレーションは、近似アルゴリズムがどのように一致するかを評価するのに便利です。

### 熟語・専門語

- **Bayesian inference**: ベイズ推論。事前分布と尤度から事後分布を計算する中核処理。
- **simulation-based calibration**: SBC。シミュレーション真値と事後rankを比べ、実装・推論の校正を検査する方法。
- **approximate**: 近似。速度や扱いやすさのため、正確な推論・モデルを緩めること。

### 要約

- データを生成するために使用されます。

## Chunk 0191

### English（抽出4行）

> theoretical posterior even in cases when the posterior is not tractable.
> While in many ways superior to benchmarking against a truth point, simulation-based calibration
> requires ﬁtting the model multiple times, which incurs a substantial computational cost, especially
> if we do not use extensive parallelization. In our view, simulation-based calibration and truth-point

### 日本語訳（自動翻訳）

> ポスターが魅力的でない場合でも理論的なポスター。
> 真実の点に対するベンチマークよりも優れている多くの点では、シミュレーションベースの校正
> 実質的な計算費を、特に治るモデルに複数の回を、満たして下さい
> 広範囲の並列化を使用しない場合。 当社のビューでは、シミュレーションベースの校正と真実のポイント

### 熟語・専門語

- **simulation-based calibration**: SBC。シミュレーション真値と事後rankを比べ、実装・推論の校正を検査する方法。

### 要約

- ポスターが魅力的でない場合でも理論的なポスター。

## Chunk 0192

### English（抽出4行）

> benchmarking are two ends of a spectrum. Roughly, a single truth-point benchmark will possibly
> ﬂag gross problems, but it does not guarantee anything. As we do more experiments, it is possible
> to see ﬁner and ﬁner problems in the computation. It is an open research question to understand
> SBC with a small number of draws. We expect that abandoning random draws for a more designed

### 日本語訳（自動翻訳）

> ベンチマーキングはスペクトルの2つの端です。 明らかに、単一の真理ポイントベンチマークはおそらく
> フラググロスの問題, しかし、それは何も保証しません. 実験をもっと進めるので、
> 計算の細かい問題や細かい問題を見る。 理解するためのオープンリサーチの質問です
> 小さな数のドローを持つSBC。 より設計されているためにランダムな描画を放棄することを期待します

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- ベンチマーキングはスペクトルの2つの端です。

## Chunk 0193

### English（抽出4行）

> exploration of the prior would make the method more eﬃcient, especially in models with a relatively
> small number of parameters.
> A serious problem with SBC is that it clashes somewhat with most modelers’ tendency to
> specify their priors wider than they believe necessary. The slightly conservative nature of weakly

### 日本語訳（自動翻訳）

> 前の探査は、特に比較的モデルでは、より効率的な方法を作る
> パラメータの小数。
> SBCの深刻な問題は、ほとんどのモデラーの傾向に多少衝突するということです
> 必要に応じて、より広い優先事項を指定します。 弱く保守的な性質

### 熟語・専門語

- **ESS**: 有効サンプルサイズ。自己相関を考慮した独立サンプル相当数。

### 要約

- 前の探査は、特に比較的モデルでは、より効率的な方法を作る パラメータの小数。

## Chunk 0194

### English（抽出4行）

> informative priors can cause the data sets simulated during SBC to occasionally be extreme. Gabry
> et al. (2019) give an example in which fake air pollution datasets were simulated where the pollution
> is denser than a black hole. These extreme data sets can cause an algorithm that works well on
> realistic data to fail dramatically. But this isn’t really a problem with the computation so much as a

### 日本語訳（自動翻訳）

> 情報主体の事前は、SBC中にシミュレートされたデータセットを時折極端に引き起こすことができます。 ガブリ
> et al. (2019) 偽の大気汚染データセットが汚染場所をシミュレートした例を与える
> 黒穴よりもデンザーです。 これらの極端なデータセットは、うまく動作するアルゴリズムを引き起こす可能性があります
> 実質的なデータは劇的に失敗する。 しかし、これはそれほど計算の問題ではありません

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- 情報主体の事前は、SBC中にシミュレートされたデータセットを時折極端に引き起こすことができます。

## Chunk 0195

### English（抽出4行）

> scenario 1
> scenario 2
> scenario 3
> −3

### 日本語訳（自動翻訳）

> シナリオ 1
> シナリオ2
> シナリオ 3
> −3

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- シナリオ 1 シナリオ2 シナリオ 3 −3

## Chunk 0196

### English（抽出4行）

> 9−3
> 9−3
> 0.00
> 0.25

### 日本語訳（自動翻訳）

> 9−3
> 9−3
> 日 時
> 0.25の

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- 9−3 9−3 日 時 0.25の

## Chunk 0197

### English（抽出4行）

> 0.50
> 0.75
> 1.00
> µ

### 日本語訳（自動翻訳）

> 0.50円
> 0.75の
> 1.00円
> μの

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- 0.50円 0.75の 1.00円 μの

## Chunk 0198

### English（抽出4行）

> Figure 7: Comparison of a posterior distribution to the assumed true parameter value. When
> ﬁtting the model to simulated data, we can examine whether the posterior sample (blue histogram)
> comports with the true parameter value (red line). In scenario 1, the posterior is centered at the
> true value, which suggests the ﬁt is reasonable. In scenario 2, the true parameter is now in the

### 日本語訳（自動翻訳）

> 図7:想定された真のパラメータ値に対するポスター分布の比較。 いつか
> 模倣されたデータにモデルを合わせて下さい、私達はポスター サンプル(青いヒストグラム)かどうかを調べることができます
> 真のパラメータ値(赤線)でコンポートします。 シナリオ1では、ポスターが中心になっています
> フィットを示唆する真の値が合理的です。 シナリオ2では、真のパラメータは今では

### 熟語・専門語

- **posterior distribution**: 事後分布。データ観測後の未知量の不確実性を表す分布。

### 要約

- 図7:想定された真のパラメータ値に対するポスター分布の比較。

## Chunk 0199

### English（抽出4行）

> tail of the posterior distribution. It is unclear whether this indicates a fault in our inference. In
> scenario 3, the posterior is multimodal and it becomes evident that comparing the posterior to a
> single point cannot validate the inference algorithm. A more comprehensive approach, such as
> simulation-based calibration, can teach us more.

### 日本語訳（自動翻訳）

> ポスター分布の尾。 これは私たちの推論の欠陥を示すかどうかは不明です。 インスタグラム
> シナリオ3、ポスターはマルチモーダルであり、ポスターを比較する明らかになります
> 単一ポイントは、推論アルゴリズムを検証できません。 など、より包括的なアプローチ
> シミュレーションベースの口径測定は、私達をもっと教えることができます。

### 熟語・専門語

- **simulation-based calibration**: SBC。シミュレーション真値と事後rankを比べ、実装・推論の校正を検査する方法。
- **posterior distribution**: 事後分布。データ観測後の未知量の不確実性を表す分布。

### 要約

- ポスター分布の尾。

## Chunk 0200

### English（抽出4行）

> If nobody gets the treatment
> Midterm exam score
> Final exam score
> Balanced treatment assignment

### 日本語訳（自動翻訳）

> 誰も治療を受けない場合
> 中間試験スコア
> 最終試験成績
> バランスの取れた処置の割り当て

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- 誰も治療を受けない場合 中間試験スコア 最終試験成績 バランスの取れた処置の割り当て

## Chunk 0201

### English（抽出4行）

> Midterm exam score
> Final exam score
> Figure 8: Simulated data on 500 students from a hypothetical study of the eﬀect of an educational
> intervention.

### 日本語訳（自動翻訳）

> 中間試験スコア
> 最終試験成績
> 図8: 教育の効果の仮説的研究から500人の学生にデータを模倣
> 介入。

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- 中間試験スコア 最終試験成績 図8: 教育の効果の仮説的研究から500人の学生にデータを模倣 介入。

## Chunk 0202

### English（抽出4行）

> problem with the prior.
> One possible way around this is to ensure that the priors are very tight. However, a pragmatic
> idea is to keep the priors and compute reasonable parameter values using the real data. This can
> be done either through rough estimates or by computing the actual posterior. We then suggest

### 日本語訳（自動翻訳）

> 前の問題。
> ここの周りの1つの可能な方法は、優先順位が非常にタイトであることを保証することです。 しかし、実用的
> 実際のデータを使用して、優先値を保持し、合理的なパラメータ値を計算することです。 これは、
> 実際のポスターを計算するか、大幅な見積りで行います。 お問い合わせ

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- 前の問題。

## Chunk 0203

### English（抽出4行）

> widening out the estimates slightly and using these as a prior for the SBC. This will ensure that all
> of the simulated data will be as realistic as the model allows.
> 4.3.
> Experimentation using constructed data

### 日本語訳（自動翻訳）

> 見積りを少し増幅し、これらをSBCの前で使用する。 これは、すべてを確実にする
> シミュレーションされたデータはモデルが許すように現実的になります。
> 4.3. .
> データ構築による実験

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- 見積りを少し増幅し、これらをSBCの前で使用する。

## Chunk 0204

### English（抽出4行）

> A good way to understand a model is to ﬁt it to data simulated from diﬀerent scenarios.
> For a simple case, suppose we are interested in the statistical properties of linear regression ﬁt
> to data from alternative distributional forms. To start, we could specify data xi, i = 1, . . . , n, draw
> coeﬃcients a and b and a residual standard deviation σ from our prior distribution, simulate data

### 日本語訳（自動翻訳）

> モデルを理解するための良い方法は、異なるシナリオからシミュレートされたデータに収まることです。
> 簡単な場合、リニア回帰フィットの統計特性に興味があるとします
> 代替流通形態のデータへ。 起動するには、データxi、i = 1, . . , n を指定できます。
> 前の分布からbと残留標準偏差のσを係数し、データのシミュレート

### 熟語・専門語

- **prior distribution**: 事前分布。データ観測前の知識・制約を表す分布。
- **ESS**: 有効サンプルサイズ。自己相関を考慮した独立サンプル相当数。

### 要約

- モデルを理解するための良い方法は、異なるシナリオからシミュレートされたデータに収まることです。

## Chunk 0205

### English（抽出4行）

> from yi ∼normal(a + bxi, σ), and ﬁt the model to the simulated data. Repeat this 1000 times and
> we can check the coverage of interval estimates: that’s a version of simulation-based calibration.
> We could then ﬁt the same model but simulating data using diﬀerent assumptions, for example
> drawing independent data points yi from the t4 distribution rather than the normal. This will then

### 日本語訳（自動翻訳）

> y〜normal(a + bxi, σ) から、モデルをシミュレートしたデータに合わせます。 この1000回を繰り返し、
> インターバル推定のカバレッジを確認できます。それはシミュレーションベースのキャリブレーションのバージョンです。
> 同じモデルに収まりますが、異なる仮定を使用してデータをシミュレートすることができます。
> 独立したデータポイントを通常のものではなくt4分布から描画します。 それから

### 熟語・専門語

- **simulation-based calibration**: SBC。シミュレーション真値と事後rankを比べ、実装・推論の校正を検査する方法。

### 要約

- y〜normal(a + bxi, σ) から、モデルをシミュレートしたデータに合わせます。

## Chunk 0206

### English（抽出4行）

> fail simulation-based calibration—the wrong model is being ﬁt—but the interesting question here
> is, how bad will these inferences be? One could, for example, use SBC simulations to examine
> coverage of posterior 50% and 95% intervals for the coeﬃcients.
> For a more elaborate example, we perform a series of simulations to understand assumptions

### 日本語訳（自動翻訳）

> シミュレーションベースのキャリブレーションに失敗する - 間違ったモデルは適合していますが、ここでは興味深い質問
> 悪いのは、これらの推論は? たとえば、SBCシミュレーションを使って調べることもできます。
> ポスターの適用範囲 係数のための50%および95%間隔。
> より精巧な例では、一連のシミュレーションを実行し、仮定を理解する

### 熟語・専門語

- **simulation-based calibration**: SBC。シミュレーション真値と事後rankを比べ、実装・推論の校正を検査する方法。

### 要約

- シミュレーションベースのキャリブレーションに失敗する - 間違ったモデルは適合していますが、ここでは興味深い質問 悪いのは、これらの推論は? たとえば、SBCシミュレーションを使って調べることもできます。

## Chunk 0207

### English（抽出4行）

> and bias correction in observational studies. We start with a scenario in which 500 students in a
> class take a midterm and ﬁnal exam. We simulate the data by ﬁrst drawing students’ true abilities
> ηi from a normal(50, 20) distribution, then drawing the two exam scores xi, yi as independent
> normal(ηi, 10) distributions. This induces the two scores to have a correlation of

### 日本語訳（自動翻訳）

> 観察研究におけるバイアス補正。 生徒500名が参加するシナリオからスタート
> 授業は中期および最終試験を受けます。 生徒の真の能力を描き出すことでデータをシミュレートします
> 通常の(50、20)分布からηi、その後、独立した2つの試験スコアxiを描画
> 通常(ηi、10)分布。 これは、相関関係を持つ2つのスコアを誘導します

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- 観察研究におけるバイアス補正。

## Chunk 0208

### English（抽出4行）

> 202+52 = 0.94;
> we designed the simulation with this high value to make patterns apparent in the graphs. Figure
> 8a displays the result, along with the underlying regression line, E(y|x). We then construct a
> hypothetical randomized experiment of a treatment performed after the midterm that would add 10

### 日本語訳（自動翻訳）

> 202+52 = 0.94;
> グラフのパターンを明らかにするために、この高い値でシミュレーションを設計しました。 プロフィール
> 8aは、根本的な回帰線、E(y|x)と共に結果を表示します。 それから構築します
> 治療の仮説的ランダム化実験は、中期後に行われる10

### 熟語・専門語

- **ESS**: 有効サンプルサイズ。自己相関を考慮した独立サンプル相当数。

### 要約

- 202+52 = 0.94; グラフのパターンを明らかにするために、この高い値でシミュレーションを設計しました。

## Chunk 0209

### English（抽出4行）

> Pre−test score
> Pr (z=1)
> 0.0
> 0.5

### 日本語訳（自動翻訳）

> 事前テストスコア
> Pr (z=1)
> ツイート
> 0.5パーセント

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- 事前テストスコア Pr (z=1) ツイート 0.5パーセント

## Chunk 0210

### English（抽出4行）

> 1.0
> (assigned to treatment group, z=1)
> (assigned to control group, z=0)
> Unalanced treatment assignment

### 日本語訳（自動翻訳）

> 1.0 の
> (処理グループ、z=1) に割り当てられる
> (グループ、z=0 の制御に割り当てられる)
> 未処理処置の割り当て

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- 1.0 の (処理グループ、z=1) に割り当てられる (グループ、z=0 の制御に割り当てられる) 未処理処置の割り当て

## Chunk 0211

### English（抽出4行）

> Midterm exam score
> Final exam score
> Figure 9: Alternative simulation in which the treatment assignment is unbalanced, with less well-
> performing students being more likely to receive the treatment.

### 日本語訳（自動翻訳）

> 中間試験スコア
> 最終試験成績
> 図9:治療の割り当てが不均衡である代替シミュレーション
> 治療を受ける可能性が高くなる学生のパフォーマンス。

### 熟語・専門語

- **ESS**: 有効サンプルサイズ。自己相関を考慮した独立サンプル相当数。

### 要約

- 中間試験スコア 最終試験成績 図9:治療の割り当てが不均衡である代替シミュレーション 治療を受ける可能性が高くなる学生のパフォーマンス。

## Chunk 0212

### English（抽出4行）

> points to any student’s ﬁnal exam score. We give each student an equal chance of receiving the
> treatment or control. Figure 8b shows the simulated data and underlying regression lines.
> In this example we can estimate the treatment eﬀect by simply taking the diﬀerence between
> the two groups, which for these simulated data yields an estimate of 10.7 with standard error 1.8.

### 日本語訳（自動翻訳）

> 任意の学生の最終試験のスコアにポイント. 生徒一人ひとりが受け取る機会を均等に与えます
> 処置か制御。 図8bは、シミュレートされたデータと根本的な回帰線を示しています。
> この例では、治療効果を単純に違いをとって推定することができます。
> これらのシミュレートされたデータが標準エラー1.8で10.7の推定値をもたらす2グループ。

### 熟語・専門語

- **ESS**: 有効サンプルサイズ。自己相関を考慮した独立サンプル相当数。

### 要約

- 任意の学生の最終試験のスコアにポイント. 生徒一人ひとりが受け取る機会を均等に与えます 処置か制御。

## Chunk 0213

### English（抽出4行）

> Or we can ﬁt a regression adjusting for midterm score, yielding an estimate of 9.7 ± 0.6.
> We next consider an unbalanced assignment mechanism in which the probability of receiving
> the treatment depends on the midterm score: Pr(z = 1) = logit−1((x −50)/10). Figure 9a shows
> simulated treatment assignments for the 200 students and Figure 9a displays the simulated exam

### 日本語訳（自動翻訳）

> または、中期スコアの回帰調整、9.7 ± 0.6の推定値に収まることもできます。
> 次は、受信の確率が不均衡な代入メカニズムを検討します
> 治療は、中期スコアによって異なります: Pr(z = 1) = logit−1(x −50)/10)。 図9aのショー
> 200人の学生および図9aのためのシミュレートされた処置の割り当ては模倣された試験を表示します

### 熟語・専門語

- **ESS**: 有効サンプルサイズ。自己相関を考慮した独立サンプル相当数。

### 要約

- または、中期スコアの回帰調整、9.7 ± 0.6の推定値に収まることもできます。

## Chunk 0214

### English（抽出4行）

> scores. The underlying regression lines are the same as before, as this simulation changes the
> distribution of z but not the model for y|x, z. Under this design, the treatment is preferentially
> given to the less well-performing students, hence a simple comparison of ﬁnal exam scores will
> give a poor estimate. For this particular simulation, the diﬀerence in average grades comparing the

### 日本語訳（自動翻訳）

> スコア。 根本的な回帰線は、このシミュレーションが変更されるため、前と同じです。
> zの分布が、yのモデルではない|x、z。 この設計の下で、処置は優先的にです
> 十分なパフォーマンスの少ない学生に与えられた, したがって、最終的な試験スコアの簡単な比較は、
> 予報が悪くなる。 この特定のシミュレーションのために、平均的な等級の相違は比較します

### 熟語・専門語

- **ESS**: 有効サンプルサイズ。自己相関を考慮した独立サンプル相当数。

### 要約

- スコア。

## Chunk 0215

### English（抽出4行）

> two groups is −13.8 ± 1.5, a terrible inference given that the true eﬀect is, by construction, 10.
> In this case, though, the linear regression adjusting for x recovers the treatment eﬀect, yielding an
> estimate of 9.7 ± 0.8.
> But this new estimate is sensitive to the functional form of the adjustment for x. We can see this

### 日本語訳（自動翻訳）

> 2つのグループは、真の効果が、構造によって10であると与えられるひどい推論である- 13.8 ± 1.5です。
> この場合、x の線形回帰調整は処置の効果を回復し、収穫します
> 9.7 ± 0.8の推定。
> しかし、この新しい見積もりは、xの調整の機能的な形態に敏感です。 お問い合わせはこちら

### 熟語・専門語

- **ESS**: 有効サンプルサイズ。自己相関を考慮した独立サンプル相当数。

### 要約

- 2つのグループは、真の効果が、構造によって10であると与えられるひどい推論である- 13.8 ± 1.5です。

## Chunk 0216

### English（抽出4行）

> by simulating data from an alternative model in which the true treatment eﬀect is 10 but the function
> E(y|x, z) is no longer linear. In this case we construct such a model by drawing the midterm exam
> score given true ability from normal(ηi, 10) as before, but transforming the ﬁnal ﬁnal exam score,
> as displayed in Figure 10. We again consider two hypothetical experiments: Figure 10a shows

### 日本語訳（自動翻訳）

> 真の治療効果が10である代替モデルからデータをシミュレートすることにより、機能
> E(y|x, z) は、線形になりません。 この場合、このようなモデルを中期試験を図って構築します
> 通常の(ηi、10)から真の能力を与えられたスコアが、最終的な試験のスコアを変換する、
> 図10に示すように 2つの仮説実験:図10aショー

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- 真の治療効果が10である代替モデルからデータをシミュレートすることにより、機能 E(y|x, z) は、線形になりません。

## Chunk 0217

### English（抽出4行）

> data from the completely randomized assignment, and Figure 10b displays the result using the
> unbalanced treatment assignment rule from Figure 9a. Both graphs show the underlying regression
> curves as well.
> What happens when we now ﬁt a linear regression to estimate the treatment eﬀect? The estimate

### 日本語訳（自動翻訳）

> 完全にランダム化された代入からのデータ、および図10bは結果を表示します
> 図9aからの不均衡な処理代入ルール。 両方のグラフは、根本的な回帰を示す
> カーブも。
> 治療効果を推定するために線形回帰に合えばどうなりますか? 見積り

### 熟語・専門語

- **ESS**: 有効サンプルサイズ。自己相関を考慮した独立サンプル相当数。

### 要約

- 完全にランダム化された代入からのデータ、および図10bは結果を表示します 図9aからの不均衡な処理代入ルール。

## Chunk 0218

### English（抽出4行）

> from the design in Figure 10a is reasonable: even though the linear model is wrong and thus the
> resulting estimate is not fully statistically eﬃcient, the balance in the design ensures that on average
> the speciﬁcation errors will cancel, and the estimate is 10.5 ± 0.8. But the unbalanced design has
> problems: even after adjusting for x in the linear regression, the estimate is 7.3 ± 0.9.

### 日本語訳（自動翻訳）

> 図10aの設計から合理的な:リニアモデルが間違っているにもかかわらず、したがって、
> 結果の見積もりは、完全に統計的に効率的ではありません。設計の残高は平均的にそれを保証する
> 仕様のエラーはキャンセルされ、見積りは10.5±0.8となります。 しかし、不均衡なデザインは、
> 問題: 線形回帰のxのために調節した後でさえ、見積もりは7.3 ± 0.9です。

### 熟語・専門語

- **ESS**: 有効サンプルサイズ。自己相関を考慮した独立サンプル相当数。

### 要約

- 図10aの設計から合理的な:リニアモデルが間違っているにもかかわらず、したがって、 結果の見積もりは、完全に統計的に効率的ではありません。

## Chunk 0219

### English（抽出4行）

> Nonlinear model, balanced assignment
> Midterm exam score
> Final exam score
> Nonlinear model, unbalanced assignment

### 日本語訳（自動翻訳）

> 非線形モデル、バランスの取れた代入
> 中間試験スコア
> 最終試験成績
> 非線形モデル、不均衡な割り当て

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- 非線形モデル、バランスの取れた代入 中間試験スコア 最終試験成績 非線形モデル、不均衡な割り当て

## Chunk 0220

### English（抽出4行）

> Midterm exam score
> Final exam score
> Figure 10: Again comparing two diﬀerent treatment assignments, this time in a setting where the
> relation between ﬁnal and midterm exam scores is nonlinear.

### 日本語訳（自動翻訳）

> 中間試験スコア
> 最終試験成績
> 図10:再び2つの異なる治療の代入を比較する、この時間の設定で
> 最終試験と中間試験のスコアの関係は非線形です。

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- 中間試験スコア 最終試験成績 図10:再び2つの異なる治療の代入を比較する、この時間の設定で 最終試験と中間試験のスコアの関係は非線形です。

## Chunk 0221

### English（抽出4行）

> In the context of the present article, the point of this example is to demonstrate how simulation of
> a statistical system under diﬀerent conditions can give us insight, not just about computational issues
> but also about data and inference more generally. One could go further in this particular example
> by considering varying treatment eﬀects, selection on unobservables, and other complications, and

### 日本語訳（自動翻訳）

> この記事の文脈では、この例のポイントは、シミュレーションのシミュレーションを実証することです。
> 異なる条件下での統計システムは、計算上の問題だけでなく、私たちに洞察を与えることができます
> しかし、より一般的にデータと推論について. この特定の例でさらに行くことができるもの
> さまざまな治療効果、観察不可能な選択、その他の合併症を考慮し、

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- この記事の文脈では、この例のポイントは、シミュレーションのシミュレーションを実証することです。

## Chunk 0222

### English（抽出4行）

> this is generally true that such theoretical explorations can be considered indeﬁnitely to address
> whatever concerns might arise.
> 5.
> Addressing computational problems

### 日本語訳（自動翻訳）

> これは、このような理論的探査は、アドレスに無期限に考慮することができることが一般的に当てはまります
> どんな問題でも発生する可能性があります。
> 5。
> 計算上の問題に対処する

### 熟語・専門語

- **ESS**: 有効サンプルサイズ。自己相関を考慮した独立サンプル相当数。

### 要約

- これは、このような理論的探査は、アドレスに無期限に考慮することができることが一般的に当てはまります どんな問題でも発生する可能性があります。

## Chunk 0223

### English（抽出4行）

> 5.1.
> The folk theorem of statistical computing
> When you have computational problems, often there’s a problem with your model (Yao, Vehtari,
> and Gelman, 2020). Not always—sometimes you will have a model that is legitimately diﬃcult to

### 日本語訳（自動翻訳）

> 5.1. .
> 統計計算の民間理論
> 計算上の問題がある場合, 多くの場合、あなたのモデルに問題があります (ヤオ, Vehtari,
> そしてゲルマン、2020年)。 いつもではなく、あなたが正当な困難であるモデルを持っているとき

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- 5.1. . 統計計算の民間理論 計算上の問題がある場合, 多くの場合、あなたのモデルに問題があります (ヤオ, Vehtari, そしてゲルマン、2020年)。

## Chunk 0224

### English（抽出4行）

> ﬁt—but many cases of poor convergence correspond to regions of parameter space that are not of
> substantive interest or even to a nonsensical model. An example of pathologies in irrelevant regions
> of parameter space is given in Figure 6. Examples of fundamentally problematic models would be
> bugs in code or using a Gaussian-distributed varying intercept for each individual observation in a

### 日本語訳（自動翻訳）

> フィット — しかし、貧しいコンバージェンスの多くのケースは、パラメータ空間の領域に相当します。
> 実質的な興味か、またはnonsensicalモデルに。 関連する地域の病状の例
> 図6にパラメータ空間が与えられる 根本的に問題のあるモデルの例は
> コード内のバグや、Gausian-distributed を使用して、個々の観察のインターセプト

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- フィット — しかし、貧しいコンバージェンスの多くのケースは、パラメータ空間の領域に相当します。

## Chunk 0225

### English（抽出4行）

> Gaussian or logistic regression context, where they cannot be informed by data. Our ﬁrst instinct
> when faced with a problematic model should not be to throw more computational resources on
> the model (e.g., by running the sampler for more iterations or reducing the step size of the HMC
> algorithm), but to check whether our model contains some substantive pathology.

### 日本語訳（自動翻訳）

> ガウスや記号論理的な回帰コンテキストは、データによって通知できない。 私たちの最初の本能
> 問題のあるモデルに直面した場合は、より多くの計算リソースを投げるべきではありません
> より多くの反復のためのサンプラーを動くか、またはHFCのステップ サイズを減らすことによってモデル(例えば、
> アルゴリズム)が、当社のモデルにいくつかの実質的な病理学が含まれているかどうかを確認する。

### 熟語・専門語

- **ESS**: 有効サンプルサイズ。自己相関を考慮した独立サンプル相当数。

### 要約

- ガウスや記号論理的な回帰コンテキストは、データによって通知できない。

## Chunk 0226

### English（抽出4行）

> 5.2.
> Starting at simple and complex models and meeting in the middle
> Figure 11 illustrates a commonly useful approach to debugging. The starting point is that a model
> is not performing well, possibly not converging or being able to reproduce the true parameter

### 日本語訳（自動翻訳）

> 5.2. .
> シンプルで複雑なモデルから始まり、ミドルでミーティング
> 図11はデバッグによく役立つアプローチを示しています。 スタートポイントはモデル
> 真のパラメータを反発したり、再現したりできない、うまく機能しない

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- 5.2. . シンプルで複雑なモデルから始まり、ミドルでミーティング 図11はデバッグによく役立つアプローチを示しています。

## Chunk 0227

### English（抽出4行）

> values in fake-data simulation, or not ﬁtting the data well, or yielding unreasonable inferences.
> The path toward diagnosing the problem is to move from two directions: to gradually simplify the
> Figure 11: Diagram of advice for debugging. The asterisk on the lower right represents the scenario
> in which problems arise when trying to ﬁt the desired complex model. The dots on the upper left

### 日本語訳（自動翻訳）

> 偽データシミュレーションの値は、データをうまくフィッティングしたり、不当なインフェレンスを収穫したりしません。
> 問題を診断するためのパスは、2つの方向から移動することです。
> 図11:デバッグのためのアドバイスの図。 右下にあるアスタリスクは、シナリオを表します
> 必要な複雑なモデルに合うようにしようとすると、問題が発生する。 左上の点

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- 偽データシミュレーションの値は、データをうまくフィッティングしたり、不当なインフェレンスを収穫したりしません。

## Chunk 0228

### English（抽出4行）

> represent successes at ﬁtting various simple versions, and the dots on the lower right represent
> failures at ﬁtting various simpliﬁcations of the full model. The dotted line represents the idea
> that the problems can be identiﬁed somewhere between the simple models that ﬁt and the complex
> models that don’t. From Gelman and Hill (2007).

### 日本語訳（自動翻訳）

> さまざまなシンプルなバージョンをフィッティングし、右下の点は、
> フルモデルの様々な単純化を施すことで失敗。 点線は考えを表します
> 問題は、フィットするシンプルなモデルと複雑のどこかで識別することができます
> ないモデル。 ゲルマン・ヒル(2007年)

### 熟語・専門語

- **ESS**: 有効サンプルサイズ。自己相関を考慮した独立サンプル相当数。

### 要約

- さまざまなシンプルなバージョンをフィッティングし、右下の点は、 フルモデルの様々な単純化を施すことで失敗。

## Chunk 0229

### English（抽出4行）

> poorly-performing model, stripping it down until you get something that works; and from the other
> direction starting with a simple and well-understood model and gradually adding features until the
> problem appears. Similarly, if the model has multiple components (e.g., a diﬀerential equation and
> a linear predictor for parameters of the equation), it is usually sensible to perform a sort of unit test

### 日本語訳（自動翻訳）

> パフォーマンスの悪いモデル, あなたが作品何かを得るまで、それを除去; そして、他の
> シンプルでしっかりしたモデルから始まり、徐々に機能を追加する方向
> 問題は現れます。 同様に、モデルに複数のコンポーネントがある場合(例、差動式など)
> 式のパラメータの線形予測装置)、それは通常一種の単位テストを実行する目に見えるです

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- パフォーマンスの悪いモデル, あなたが作品何かを得るまで、それを除去; そして、他の シンプルでしっかりしたモデルから始まり、徐々に機能を追加する方向 問題は現れます。

## Chunk 0230

### English（抽出4行）

> by ﬁrst making sure each component can be ﬁt separately, using simulated data.
> We may never end up ﬁtting the complex model we had intended to ﬁt at ﬁrst, either because
> it was too diﬃcult to ﬁt using currently available computational algorithms, or because existing
> data and prior information are not informative enough to allow useful inferences from the model,

### 日本語訳（自動翻訳）

> 各コンポーネントは、シミュレートされたデータを使用して、それぞれが別々に収まるようにする。
> 私たちは、私たちが最初に合うことを意図していた複雑なモデルをフィッティングし終わることはできません。
> 現在利用可能な計算アルゴリズムを使用して収まるのは難しかったです。
> モデルからの有用な推論を可能にするために、データと事前の情報は十分に有益ではありません。

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- 各コンポーネントは、シミュレートされたデータを使用して、それぞれが別々に収まるようにする。

## Chunk 0231

### English（抽出4行）

> or simply because the process of model exploration lead us in a diﬀerent direction than we had
> originally planned.
> 5.3.
> Getting a handle on models that take a long time to fit

### 日本語訳（自動翻訳）

> または単にモデル探査のプロセスは、私たちが持っていたよりも異なる方向に私たちをリードしているため
> 当初の予定。
> 5.3.
> フィットする時間を取るモデルのハンドルを取得する

### 熟語・専門語

- **ESS**: 有効サンプルサイズ。自己相関を考慮した独立サンプル相当数。

### 要約

- または単にモデル探査のプロセスは、私たちが持っていたよりも異なる方向に私たちをリードしているため 当初の予定。

## Chunk 0232

### English（抽出4行）

> We generally ﬁt our models using HMC, which can run slowly for various reasons, including expen-
> sive gradient evaluations as in diﬀerential equation models, high dimensionality of the parameter
> space, or a posterior geometry in which HMC steps that are eﬃcient in one part of the space are
> too large or too small in other regions of the posterior distribution. Slow computation is often a

### 日本語訳（自動翻訳）

> 一般的には、エクスペンを含む様々な理由でゆっくりと実行できるHMCを使用してモデルに適合しています。
> 差動的な方程式のモデル、変数の高い次元としてsiveの勾配の評価
> スペース、またはスペースの1つの部分で有効なHMCのステップがであるポスタージオメトリ
> ポスター分布の他の領域で大きすぎるか小さすぎます。 遅い計算は頻繁にあります

### 熟語・専門語

- **posterior distribution**: 事後分布。データ観測後の未知量の不確実性を表す分布。

### 要約

- 一般的には、エクスペンを含む様々な理由でゆっくりと実行できるHMCを使用してモデルに適合しています。

## Chunk 0233

### English（抽出4行）

> sign of other problems, as it indicates a poorly-performing HMC. However the very fact that the ﬁt
> takes long means the model is harder to debug.
> For example, we recently received a query in the Stan users group regarding a multilevel logistic
> regression with 35,000 data points, 14 predictors, and 9 batches of varying intercepts, which failed

### 日本語訳（自動翻訳）

> 他の問題の兆候は、HMCの変形が悪いことを示すためです。 しかし、フィットする非常に事実
> 長い意味では、モデルはデバッグするのが難しくなります。
> 例えば、Stanユーザーグループでマルチレベル・ロジスティックに関する問い合わせを最近受けました。
> 35,000のデータポイント、14の予測者、および9つの異なるインターセプトのバッチとの回帰、失敗

### 熟語・専門語

- **ESS**: 有効サンプルサイズ。自己相関を考慮した独立サンプル相当数。

### 要約

- 他の問題の兆候は、HMCの変形が悪いことを示すためです。

## Chunk 0234

### English（抽出4行）

> to ﬁnish running after several hours in Stan using default settings from rstanarm.
> We gave the following suggestions, in no particular order:
> • Simulate fake data from the model and try ﬁtting the model to the fake data (Section 4.1).
> Frequently a badly speciﬁed model is slow, and working with simulated data allows us not to

### 日本語訳（自動翻訳）

> rstanarm のデフォルト設定を使用して Stan の複数の時間後に実行を終了します。
> 私たちは、特定の順序で、次の提案を与えました。
> •モデルから偽データを模倣し、モデルを偽物データ(セクション4.1)にフィッティングしてみてください。
> 悪意のあるモデルが遅く、シミュレートされたデータで動作するので、そうしない

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- rstanarm のデフォルト設定を使用して Stan の複数の時間後に実行を終了します。

## Chunk 0235

### English（抽出4行）

> worry about lack of ﬁt.
> • Since the big model is too slow, you should start with a smaller model and build up from there.
> First ﬁt the model with no varying intercepts. Then add one batch of varying intercepts, then
> the next, and so forth.

### 日本語訳（自動翻訳）

> フィット感の欠如を心配します。
> ・大きめのモデルが遅いので、小さめのモデルから始めて、そこからビルドしてください。
> 最初は、異なるインターセプトなしでモデルに合います。 その後、異なるインターセプトの1つのバッチを追加します。
> 以下、等。

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- フィット感の欠如を心配します。

## Chunk 0236

### English（抽出4行）

> • Run for 200 iterations, rather than the default (at the time of this writing). Eventually you can
> run for 2000 iterations, but there is no point in doing that while you’re still trying to ﬁgure
> out what’s going on. If, after 200 iterations, bR is large, you can run longer, but there is no
> need to start with 2000.

### 日本語訳（自動翻訳）

> • デフォルトではなく200の反復のために実行します(この文章の時間)。 時事にできる
> 2000年の反復のために実行しますが、まだ図をしようとしている間、それを行う点はありません
> 何が起こっているか。 もし200の反復の後で、bRは大きいです、より長く動くことができますが、そこにありません
> 2000 から始める必要があります。

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- • デフォルトではなく200の反復のために実行します(この文章の時間)。

## Chunk 0237

### English（抽出4行）

> • Put at least moderately informative priors on the regression coeﬃcients and group-level
> variance parameters (Section 7.3).
> • Consider some interactions of the group-level predictors. It seems strange to have an additive
> model with 14 terms and no interactions. This suggestion may seem irrelevant to the user’s

### 日本語訳（自動翻訳）

> • 回帰係数およびグループレベルの少なくとも適度に有益な優先順位を置いて下さい
> 分散パラメータ(セクション7.3)。
> • グループレベルの予測者の相互作用を検討してください。 添加剤を持っているのは不思議なようです
> 14の用語と相互作用なしのモデル。 この提案は、ユーザーの関連性に反する可能性があります

### 熟語・専門語

- **ESS**: 有効サンプルサイズ。自己相関を考慮した独立サンプル相当数。

### 要約

- • 回帰係数およびグループレベルの少なくとも適度に有益な優先順位を置いて下さい 分散パラメータ(セクション7.3)。

## Chunk 0238

### English（抽出4行）

> concern about speed—indeed, adding interactions should only increase run time—but it
> is a reminder that ultimately the goal is to make predictions or learn something about the
> underlying process, not merely to get some arbitrary pre-chosen model to converge.
> • Fit the model on a subset of your data. Again, this is part of the general advice to understand

### 日本語訳（自動翻訳）

> 速度に関する懸念 - 隠されて、インタラクションを追加すると、実行時間だけ増加する必要がありますが、それは
> 究極の目標は、予測や何かについて学ぶことです。
> 従順なプロセスは、単にコンバージにいくつかの任意のプレコーストモデルを取得することではありません。
> • データのサブセットでモデルにフィットします。 繰り返しますが、これは理解するための一般的なアドバイスの一部です

### 熟語・専門語

- **ESS**: 有効サンプルサイズ。自己相関を考慮した独立サンプル相当数。
- **prediction**: 予測。未知/将来/除外データに対する分布や点推定。

### 要約

- 速度に関する懸念 - 隠されて、インタラクションを追加すると、実行時間だけ増加する必要がありますが、それは 究極の目標は、予測や何かについて学ぶことです。

## Chunk 0239

### English（抽出4行）

> the ﬁtting process and get it to work well, before throwing the model at all the data.
> The common theme in all these tips is to think of any particular model choice as provisional, and to
> recognize that data analysis requires many models to be ﬁt in order to gain control over the process
> of computation and inference for a particular applied problem.

### 日本語訳（自動翻訳）

> フィッティング プロセスは、すべてのデータをモデルを投げる前に、うまく機能します。
> これらのすべてのヒントの共通テーマは、暫定的として任意の特定のモデルの選択を考えることです。
> プロセスをコントロールするために、データ分析が多くのモデルに適合するように要求していることを認識
> 特定の適用問題の計算そして不当。

### 熟語・専門語

- **ESS**: 有効サンプルサイズ。自己相関を考慮した独立サンプル相当数。

### 要約

- フィッティング プロセスは、すべてのデータをモデルを投げる前に、うまく機能します。

## Chunk 0240

### English（抽出4行）

> 5.4.
> Monitoring intermediate quantities
> Another useful approach to diagnosing model issues is to save intermediate quantities in our
> computations and plot them along with other MCMC output, for example using bayesplot (Gabry

### 日本語訳（自動翻訳）

> 5.4。
> 中間量を監視して下さい
> モデルの問題を診断するためのもう一つの有用なアプローチは、私たちの中の量を節約することです
> bayesplot (Gabry) を使うなど、他の MC の出力とともに計算し、それらをプロットして下さい

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- 5.4。

## Chunk 0241

### English（抽出4行）

> et al., 2020a) or ArviZ (Kumar et al., 2019). These displays are an alternative to inserting print
> statements inside the code. In our experience, we typically learn more from a visualization than
> from a stream of numbers in the console.
> One problem that sometimes arises is chains getting stuck in out-of-the-way places in parameter

### 日本語訳（自動翻訳）

> et al., 2020a) または ArviZ (Kumar et al., 2019). これらのディスプレイは、印刷をインサートする代替品です
> コード内のステートメント。 私たちの経験では、通常、視覚化よりも多くを学びます
> コンソールの数字のストリームから。
> 時々アリスは、パラメータのアウト・オブ・ザ・ウェイの場所で立ち往生するチェーンである1つの問題

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- et al., 2020a) または ArviZ (Kumar et al., 2019). これらのディスプレイは、印刷をインサートする代替品です コード内のステートメント。

## Chunk 0242

### English（抽出4行）

> space where the posterior density is very low and where it can be baﬄing why the MCMC algorithm
> does not drift back toward the region where the log posterior density is near its expectation and
> where most of the posterior mass is. Here it can be helpful to look at predictions from the model
> given these parameter values to understand what is going wrong, as we illustrate in Section 11. But

### 日本語訳（自動翻訳）

> ポスター密度が非常に低く、MCMCアルゴリズムがバッフルできる空間
> ログのポスター密度が期待の近傍にある領域に戻って漂流しません
> ポスターの質量のほとんどがどこにあるか。 ここではモデルから予測を見るのに役立ちます
> セクション11で説明するので、何が間違っているかを理解するために、これらのパラメータ値を指定しました。 しかし、

### 熟語・専門語

- **prediction**: 予測。未知/将来/除外データに対する分布や点推定。

### 要約

- ポスター密度が非常に低く、MCMCアルゴリズムがバッフルできる空間 ログのポスター密度が期待の近傍にある領域に戻って漂流しません ポスターの質量のほとんどがどこにあるか。

## Chunk 0243

### English（抽出4行）

> the most direct approach is to plot the expected data conditional on the parameter values in these
> stuck chains, and then to transform the gradient of the parameters to the gradient of the expected
> data. This should give some insight as to how the parameters map to expected data in the relevant
> regions of the posterior distribution.

### 日本語訳（自動翻訳）

> 最も直接的なアプローチは、これらのパラメータ値に期待されるデータ条件をプロットすることです。
> チェーンをスタックし、パラメータの勾配を期待の勾配に変換する
> データ。 これは、関連するデータに期待されるデータにパラメータマップする方法についていくつかの洞察を与える必要があります
> ポスター分布の領域。

### 熟語・専門語

- **posterior distribution**: 事後分布。データ観測後の未知量の不確実性を表す分布。

### 要約

- 最も直接的なアプローチは、これらのパラメータ値に期待されるデータ条件をプロットすることです。

## Chunk 0244

### English（抽出4行）

> 5.5.
> Stacking to reweight poorly mixing chains
> In practice, often our MCMC algorithms mix just ﬁne. Other times, the simulations quickly move
> to unreasonable areas of parameter space, indicating the possibility of model misspeciﬁcation,

### 日本語訳（自動翻訳）

> 5。
> 重みが悪い混合鎖を重くする積み重ね
> 実際には、MCMCのアルゴリズムはよく似ています。 他の時間、シミュレーションはすぐに動きます
> パラメータ空間の不当な領域に、モデルの誤差の可能性を示す、

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- 5。

## Chunk 0245

### English（抽出4行）

> non-informative or weakly informative observations, or just diﬃcult geometry.
> But it is also common to be in an intermediate situation where multiple chains are slow to
> mix but they are in a generally reasonable range. In this case we can use stacking to combine
> the simulations, using cross validation to assign weights to the diﬀerent chains (Yao, Vehtari,

### 日本語訳（自動翻訳）

> 非情報的または弱く有益な観察、または単に難しいジオメトリ。
> しかし、複数のチェーンが遅くなる中間の状況にも共通している
> 混合するが、それらは一般的に合理的な範囲にある。 この場合、スタックを組み合わせて使うことができます。
> シミュレーション、クロスバリデーションを使用して、異なるチェーン(ヤオ、ヴェタリ、

### 熟語・専門語

- **cross validation**: 交差検証。汎化性能を推定するためにデータを分割/近似除外する評価法。
- **validation**: 検証。モデルが目的・データ・外部知識に照らして妥当かを確認すること。

### 要約

- 非情報的または弱く有益な観察、または単に難しいジオメトリ。

## Chunk 0246

### English（抽出4行）

> and Gelman, 2020). This will have the approximate eﬀect of discarding chains that are stuck in
> out-of-the-way low-probability modes of the target distribution. The result from stacking is not
> necessarily equivalent, even asymptotically, to fully Bayesian inference, but it serves many of the
> same goals, and is especially suitable during the model exploration phase, allowing us to move

### 日本語訳（自動翻訳）

> そしてゲルマン、2020年)。 これは、に詰まっている破棄チェーンの近似効果を持っています
> ターゲット分布の外側の低確率モード。 スタックからの結果は、
> ベイジアン・インフェレンスを完全にするために、必然的に等しいが、それは多くの役立ちます
> 同じ目標は、モデルの探査段階の間に特に適して、私達を移動できるようにします

### 熟語・専門語

- **Bayesian inference**: ベイズ推論。事前分布と尤度から事後分布を計算する中核処理。
- **ESS**: 有効サンプルサイズ。自己相関を考慮した独立サンプル相当数。
- **approximate**: 近似。速度や扱いやすさのため、正確な推論・モデルを緩めること。

### 要約

- そしてゲルマン、2020年)。

## Chunk 0247

### English（抽出4行）

> forward and spend more time and energy in other part of Bayesian workﬂow without getting hung
> up on exactly ﬁtting one particular model. In addition, non-uniform stacking weights, when used
> in concert with traceplots and other diagnostic tools, can help us understand where to focus that
> eﬀort in an iterative way.

### 日本語訳（自動翻訳）

> 空にすることなくベイジアンワークフローの他の部分で時間とエネルギーを費やす
> 正確に1つの特定のモデルを合わせます。 加えて、使用されるとき非均一な積み重ね重量、
> トレースプロットおよび他の診断用具とのコンサートでは、私達が焦点を合わせる場所を理解するのを助けることができます
> 反復的な方法での努力。

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- 空にすることなくベイジアンワークフローの他の部分で時間とエネルギーを費やす 正確に1つの特定のモデルを合わせます。

## Chunk 0248

### English（抽出4行）

> 5.6.
> Posterior distributions with multimodality and other difficult geometry
> We can roughly distinguish four sorts of problems with MCMC related to multimodality and other
> diﬃcult posterior geometries:

### 日本語訳（自動翻訳）

> 5.6.
> 多変性や他の困難な幾何学とポスター分布
> MCMCと多様性、その他に関連した4つの課題を大まかに把握できます。
> 困難なポスターの幾何学:

### 熟語・専門語

- **posterior distribution**: 事後分布。データ観測後の未知量の不確実性を表す分布。
- **multimodality**: 多峰性。事後分布に複数の山があり、MCMCが混合しにくい状態。

### 要約

- 5.6. 多変性や他の困難な幾何学とポスター分布 MCMCと多様性、その他に関連した4つの課題を大まかに把握できます。

## Chunk 0249

### English（抽出4行）

> • Eﬀectively disjoint posterior volumes, where all but one of the modes have near-zero mass.
> An example appears in Section 11. In such problems, the minor modes can be avoided
> using judicious choices of initial values for the simulation, adding prior information or hard
> constraints for parameters or they can be pruned by approximately estimating the mass in

### 日本語訳（自動翻訳）

> •すべてのモードの1つがほぼゼロの固まりを持っているが、実際には、ポスターのボリュームを分離します。
> セクション11に例が表示されます。 そのような問題では、マイナーモードは避けることができます
> シミュレーションの初期値の決定的な選択を使用して、事前情報またはハードを追加
> パラメータの制約や、質量を推定することで実行できます。

### 熟語・専門語

- **approximate**: 近似。速度や扱いやすさのため、正確な推論・モデルを緩めること。

### 要約

- •すべてのモードの1つがほぼゼロの固まりを持っているが、実際には、ポスターのボリュームを分離します。

## Chunk 0250

### English（抽出4行）

> each mode.
> • Eﬀectively disjoint posterior volumes of high probability mass that are trivially symmetric,
> such as label switching in a mixture model. It is standard practice here to restrict the model
> in some way to identify the mode of interest; see for example Bafumi et al. (2005) and

### 日本語訳（自動翻訳）

> 各モード。
> • 実質的に対称的である高い確率の固まりのポスターの容積をdisjoint、
> 混合モデルでのラベル切り替えなど。 モデルを制限するためにここに標準練習です
> 興味のモードを識別する方法は、例えばBafumi et al. (2005) を参照してください。

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- 各モード。

## Chunk 0251

### English（抽出4行）

> Betancourt (2017b).
> • Eﬀectively disjoint posterior volumes of high probability mass that are diﬀerent. For example
> in a model ofgene regulation(Modrák, 2018), some dataadmit twodistinct regulatoryregimes
> with opposite signs of the eﬀect, while an eﬀect close to zero has much lower posterior density.

### 日本語訳（自動翻訳）

> ベタヌクール(2017b)。
> •効果的に異なる高確率質量のポスターのボリュームを分離します。 例えば
> 遺伝子規制(Modrák, 2018)のモデルでは、いくつかのデータアドミット2distinct規制
> 効果の反対の徴候と、ゼロに近い効果がはるかに低いポスター密度を持っています。

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- ベタヌクール(2017b)。

## Chunk 0252

### English（抽出4行）

> This problem is more challenging. In some settings, we can use stacking (predictive model
> averaging) as an approximate solution, recognizing that this is not completely general as
> it requires deﬁning a predictive quantity of interest. A more fully Bayesian alternative is
> to divide the model into pieces by introducing a strong mixture prior and then ﬁtting the

### 日本語訳（自動翻訳）

> この問題はより困難です。 いくつかの設定では、スタッキング(予測モデル)を使うことができます。
> 平均化) 近似ソリューションとして、これは完全に一般的なものではないことを認識
> 利息の予測数量を定義する必要があります。 より多くのベイジアンの代替手段は
> 前に強い混合物を導入し、それから付属品によってモデルを部分に分けるために

### 熟語・専門語

- **approximate**: 近似。速度や扱いやすさのため、正確な推論・モデルを緩めること。

### 要約

- この問題はより困難です。

## Chunk 0253

### English（抽出4行）

> model separately given each of the components of the prior. Other times the problem can be
> addressed using strong priors that have the eﬀect of ruling out some of the possible modes.
> • A single posterior volume of high probability mass with an arithmetically unstable tail.
> If you initialize near the mass of the distribution, there should not be problems for most

### 日本語訳（自動翻訳）

> 事前に各コンポーネントを別々にモデル化します。 その他、問題が問題になる場合があります
> 可能なモードのいくつかを台無しにする効果がある強い優先順位を使用して対処される。
> • 単一ポスターの容量の高い確率の固まりの算術的な不安定な尾。
> 分布の質量の近くで初期化する場合、ほとんどの問題はない

### 熟語・専門語

- **ESS**: 有効サンプルサイズ。自己相関を考慮した独立サンプル相当数。

### 要約

- 事前に各コンポーネントを別々にモデル化します。

## Chunk 0254

### English（抽出4行）

> inferences. If there is particular interest in extremely rare events, then the problem should
> be reparameterized anyway, as there is a limit to what can be learned from the usual default
> eﬀective sample size of a few hundred to a few thousand.
> 5.7.

### 日本語訳（自動翻訳）

> インフェレンス 非常にまれなイベントに特定の関心がある場合、問題は、問題は、
> いつものデフォルトから学習できるものの制限があるので、とにかく再パラメータ化されます。
> 数千〜数千の有効なサンプルサイズ。
> 5.7 .

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- インフェレンス 非常にまれなイベントに特定の関心がある場合、問題は、問題は、 いつものデフォルトから学習できるものの制限があるので、とにかく再パラメータ化されます。

## Chunk 0255

### English（抽出4行）

> Reparameterization
> Generally, an HMC-based sampler will work best if its mass matrix is appropriately tuned and the
> geometry of the joint posterior distribution is relatively uninteresting, in that it has no sharp corners,
> cusps, or other irregularities. This is easily satisﬁed for many classical models, where results like

### 日本語訳（自動翻訳）

> パラメータ化
> 一般的に、その質量行列が適切に調整されれば、HMCベースのサンプラーが最善を尽くします。
> 関節のポスター分布の幾何学は、それが鋭い角を持っていないことの比較的興味がないです、
> カスプ、またはその他の不規則性。 これは、多くの古典的なモデルに簡単に満足しています。

### 熟語・専門語

- **posterior distribution**: 事後分布。データ観測後の未知量の不確実性を表す分布。
- **reparameterization**: 再パラメータ化。計算しやすい幾何に変えるためのパラメータ表現変更。

### 要約

- パラメータ化 一般的に、その質量行列が適切に調整されれば、HMCベースのサンプラーが最善を尽くします。

## Chunk 0256

### English（抽出4行）

> the Bernstein-von Mises theorem suggest that the posterior will become fairly simple when there
> is enough data. Unfortunately, the moment a model becomes even slightly complex, we can no
> longer guarantee that we will have enough data to reach this asymptotic utopia (or, for that matter,
> that a Bernstein-von Mises theorem holds). For these models, the behavior of HMC can be greatly

### 日本語訳（自動翻訳）

> Bernstein-von Mises theoremは、そこにあるとき、ポスターがかなり単純になることを示唆しています
> 十分なデータです。 残念なことに、モデルが少し複雑になる瞬間、私たちは決してできない
> この非対称性ユートピア(または、その問題のために)に到達するのに十分なデータがあることを保証し、
> Bernstein-von Mises theorem が保持されていること これらのモデルでは、HMCの挙動が大きくなる

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- Bernstein-von Mises theoremは、そこにあるとき、ポスターがかなり単純になることを示唆しています 十分なデータです。

## Chunk 0257

### English（抽出4行）

> improved by judiciously choosing a parameterization that makes the posterior geometry simpler.
> For example, hierarchical models can have diﬃcult funnel pathologies in the limit when group-
> level variance parameters approach zero (Neal, 2011), but in many such problems these computa-
> tional diﬃculties can be resolved using reparameterization, following the principles discussed by

### 日本語訳（自動翻訳）

> ポスタージオメトリをシンプルにするパラメータ化を選択することで、
> たとえば、階層モデルは、グループ時に限界に困難な漏斗病理を持つことができます。
> レベルの分散パラメータはゼロ(Neal, 2011)に近づくが、このような問題では、これらのコンプタ-
> 説明する原則に従って、再パラメータ化を使用して、条件の困難を解決することができます

### 熟語・専門語

- **reparameterization**: 再パラメータ化。計算しやすい幾何に変えるためのパラメータ表現変更。

### 要約

- ポスタージオメトリをシンプルにするパラメータ化を選択することで、 たとえば、階層モデルは、グループ時に限界に困難な漏斗病理を持つことができます。

## Chunk 0258

### English（抽出4行）

> Meng and van Dyk (2001); see also Betancourt and Girolami (2015).
> 5.8.
> Marginalization
> Challenging geometries in the posterior distribution are often due to interactions between param-

### 日本語訳（自動翻訳）

> メングとヴァン・ダイク(2001年)、ベタクールとジロラミ(2015年)も参照してください。
> 5.8。
> マージナル化
> ポスター分布の幾何学を鍛えることは、多くの場合、パラメータ間の相互作用によるものです-

### 熟語・専門語

- **posterior distribution**: 事後分布。データ観測後の未知量の不確実性を表す分布。

### 要約

- メングとヴァン・ダイク(2001年)、ベタクールとジロラミ(2015年)も参照してください。

## Chunk 0259

### English（抽出4行）

> eters. An example is the above-mentioned funnel shape, which we may observe when plotting the
> joint density of the group-level scale parameter, φ, and the individual-level mean, θ. By contrast,
> the marginal density of φ is well behaved. Hence we can eﬃciently draw MCMC samples from the
> marginal posterior,

### 日本語訳（自動翻訳）

> ツイート 上記のファネル形状は、プロット時に観察できる例です。
> グループレベルのスケールパラメータ、φ、個々のレベル平均の接合密度、θ。 対照的に、
> φの限界密度はよく機能します。 したがって、MCMCサンプルを効率的に描画することができます
> 余白のポスター、

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- ツイート 上記のファネル形状は、プロット時に観察できる例です。

## Chunk 0260

### English（抽出4行）

> p(φ|y) =
> Z
> Θ
> p(φ, θ|y)dθ.

### 日本語訳（自動翻訳）

> p(φ|y) =
> ツイート
> . . .
> p(φ、θ|y)dθ。

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- p(φ|y) = ツイート . . . p(φ、θ|y)dθ。

## Chunk 0261

### English（抽出4行）

> To draw posterior draws with MCMC, Bayes’ rule teaches us we only need the marginal likelihood,
> p(y|φ). It is then possible to recover posterior draws for θ by doing exact sampling from the
> conditional distribution p(θ|φ, y), at a small computational cost. This marginalization strategy is
> notably used for Gaussian processes with a normal likelihood (e.g. Rasmussen and Williams, 2006,

### 日本語訳（自動翻訳）

> ポスターを描くためにMCMCで描く, ベイズのルールは、我々は唯一の証拠金を必要とする,
> p(y|φ). ポスターのドローをθに回復してから、正確なサンプリングを行うことで可能です
> 条件分布 p(θ|φ、y)、小計算コストで。 このマージン化戦略は
> Gaussian のプロセスに普通の尤度(例えば Rasmussen およびウィリアムズ、2006 年、

### 熟語・専門語

- **likelihood**: 尤度。パラメータが与えられたときデータがどれだけ起こりやすいか。
- **ESS**: 有効サンプルサイズ。自己相関を考慮した独立サンプル相当数。
- **posterior draws**: 事後ドロー。事後分布から得たサンプル。

### 要約

- ポスターを描くためにMCMCで描く, ベイズのルールは、我々は唯一の証拠金を必要とする, p(y|φ). ポスターのドローをθに回復してから、正確なサンプリングを行うことで可能です 条件分布 p(θ|φ、y)、小計算コストで。

## Chunk 0262

### English（抽出4行）

> Betancourt, 2020b).
> In general, the densities p(y|φ) and p(θ|φ, y) are not available to us. Exploiting the structure
> of the problem, we can approximate these distributions using a Laplace approximation, notably for
> latent Gaussian models (e.g., Tierney and Kadane, 1986, Rasmussen and Williams, 2006, Rue et

### 日本語訳（自動翻訳）

> Betancourt、2020b)。
> 一般的には、弊社では入れ歯p(y|φ)とp(θ|φ、y)は使用できません。 構造を探索する
> 問題は、この分布をLaplace 近似で近似できます。
> 1986年、ラズムセンとウィリアムズ、2006年、ルー・エト

### 熟語・専門語

- **approximate**: 近似。速度や扱いやすさのため、正確な推論・モデルを緩めること。

### 要約

- Betancourt、2020b)。

## Chunk 0263

### English（抽出4行）

> al., 2009, Margossian et al., 2020b). When coupled with HMC, this marginalization scheme can,
> depending on the cases, be more eﬀective than reparameterization, if sometimes at the cost of a
> bias; for a discussion on the topic, see Margossian et al. (2020a).
> 5.9.

### 日本語訳（自動翻訳）

> ., 2009, マルゴシアン ら., 2020b). HMCと組み合わせると、このマージン化スキームは、
> ケースによっては、再パラメータ化よりも効果的です。場合によっては、
> 偏見; 話題の議論のために, マルゴシアン ら. (2020a).
> 5.9. .

### 熟語・専門語

- **reparameterization**: 再パラメータ化。計算しやすい幾何に変えるためのパラメータ表現変更。

### 要約

- ., 2009, マルゴシアン ら., 2020b). HMCと組み合わせると、このマージン化スキームは、 ケースによっては、再パラメータ化よりも効果的です。

## Chunk 0264

### English（抽出4行）

> Adding prior information
> Often the problems in computation can be ﬁxed by including prior information that is already
> available but which had not yet been included in the model, for example, because prior elicitation
> from domain experts has substantial cost (O’Hagan et al., 2006, Sarma and Kay, 2020) and we

### 日本語訳（自動翻訳）

> 事前情報の追加
> 多くの場合、計算の問題は、既にある事前情報を含むことによって固定することができます
> 利用可能なが、モデルにはまだ含まれていない、例えば、事前の勧誘
> ドメインの専門家から大幅なコスト(O’Hagan et al., 2006, サルマとケイ, 2020)を保有し、私たちは、

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- 事前情報の追加 多くの場合、計算の問題は、既にある事前情報を含むことによって固定することができます 利用可能なが、モデルにはまだ含まれていない、例えば、事前の勧誘 ドメインの専門家から大幅なコスト(O’Hagan et al., 20…

## Chunk 0265

### English（抽出4行）

> started with some template model and prior (Section 2.1). In some cases, running for more iterations
> can also help. But many ﬁtting problems go away when reasonable prior information is added,
> which is not to say that the primary use of priors is to resolve ﬁtting problems.
> We may have assumed (or hoped) that the data would suﬃciently informative for all parts of the

### 日本語訳（自動翻訳）

> いくつかのテンプレートモデルと前のテンプレート(セクション2.1)から始まります。 場合によっては、より多くの反復のために動く
> 助けることができる。 しかし、合理的な事前情報を追加すると、多くの適切な問題が消えます。
> これは、優先順位の主な使用は、適切な問題の解決とは言えません。
> データがすべての部品に対して十分な情報を提供すると仮定した(または希望)

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- いくつかのテンプレートモデルと前のテンプレート(セクション2.1)から始まります。

## Chunk 0266

### English（抽出4行）

> model, but with careful inspection or as the byproduct of computational diagnostics, we may ﬁnd out
> 0.0
> 0.5
> 1.0

### 日本語訳（自動翻訳）

> モデル、しかし慎重な点検か計算の診断の副産物として、私達は見つけるかもしれません
> ツイート
> 0.5パーセント
> 1.0 の

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- モデル、しかし慎重な点検か計算の診断の副産物として、私達は見つけるかもしれません ツイート 0.5パーセント 1.0 の

## Chunk 0267

### English（抽出4行）

> 1.5
> 2.0
> y = (a1e−0.1x + a2e−2x) × error
> x

### 日本語訳（自動翻訳）

> 1.5マイル
> 2.0 の
> y = (a1e-0.1x + a2e-2x) × エラー
> ツイート

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- 1.5マイル 2.0 の y = (a1e-0.1x + a2e-2x) × エラー ツイート

## Chunk 0268

### English（抽出4行）

> y
> 0.0
> 1.0
> 2.0

### 日本語訳（自動翻訳）

> ログイン
> ツイート
> 1.0 の
> 2.0 の

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- ログイン ツイート 1.0 の 2.0 の

## Chunk 0269

### English（抽出4行）

> 3.0
> y = (a1e−0.1x + a2e−0.2x) × error
> x
> y

### 日本語訳（自動翻訳）

> ディスクロージャー
> y = (a1e-0.1x + a2e-0.2x) × エラー
> ツイート
> ログイン

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- ディスクロージャー y = (a1e-0.1x + a2e-0.2x) × エラー ツイート ログイン

## Chunk 0270

### English（抽出4行）

> Figure 12: Simulated data from the model, y = (a1e−b1x + a2e−b2x) ∗error: (a) setting (b1, b2) =
> (0.1, 2.0), and (b) setting (b1, b2) = (0.1, 0.2). In addition, the dotted line in the second plot shows
> the curve, y = 1.8e−0.135x, which almost exactly coincides with the true curve over the range of
> these data. It was easy to ﬁt the model to the data in the left graph and recover the true parameter

### 日本語訳（自動翻訳）

> 図12:モデル、y = (a1e-b1x + a2e-b2x) からデータをシミュレートする ※エラー: (a) 設定 (b1、b2) =
> (0.1, 2.0), (b) の設定 (b1, b2) = (0.1, 0.2). また、2つ目のプロットショーの点線は、
> 曲線、y = 1.8e-0.135x、ほぼ正確に真の曲線と真の曲線の範囲を一致させます
> これらのデータ。 左グラフのデータにモデルを合わせ、真のパラメータを回復するのは簡単です

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- 図12:モデル、y = (a1e-b1x + a2e-b2x) からデータをシミュレートする ※エラー: (a) 設定 (b1、b2) = (0.1, 2.0), (b) の設定 (b1, b2) = (0.1, 0.2). また、2…

## Chunk 0271

### English（抽出4行）

> values. For the data in the right graph, however, the observations did not provide information
> to reduce the uncertainty suﬃciently, and and the model could only be stably ﬁt using a prior
> distribution that provided that needed missing information.
> that this is not the case. In classical statistics, models are sometimes classiﬁed as identiﬁable or non-

### 日本語訳（自動翻訳）

> 値。 右側のグラフのデータについては、しかし、観察は情報を提供しなかった
> 不確実性を十分に減らすために、モデルは前にだけ固定して合うことができます
> 不要な情報を提供した配布。
> この場合はそうではありません。 古典的統計では、モデルは識別可能か非として分類されます

### 熟語・専門語

- **uncertainty**: 不確実性。観測・パラメータ・モデル構造・意思決定に残る曖昧さ。

### 要約

- 値。

## Chunk 0272

### English（抽出4行）

> identiﬁable, but this can be misleading (even after adding intermediate categories such as partial or
> weak identiﬁability), as the amount of information that can be learned from observations depends
> also on the speciﬁc realization of the data that was actually obtained. In addition, “identiﬁcation”
> is formally deﬁned in statistics as an asymptotic property, but in Bayesian inference we care about

### 日本語訳（自動翻訳）

> 識別可能であるが、これは誤解を招くことができます(部分的または部分的などの中間カテゴリを追加した後であっても)
> 観察から学習できる情報量は、弱な識別性)
> 実際に取得したデータの特定の実現にも。 加えて「特定」
> asymptotic プロパティとして統計的に定義されますが、Bayesian の推論では、

### 熟語・専門語

- **Bayesian inference**: ベイズ推論。事前分布と尤度から事後分布を計算する中核処理。

### 要約

- 識別可能であるが、これは誤解を招くことができます(部分的または部分的などの中間カテゴリを追加した後であっても) 観察から学習できる情報量は、弱な識別性) 実際に取得したデータの特定の実現にも。

## Chunk 0273

### English（抽出4行）

> inference with ﬁnite data, especially given that our models often increase in size and complexity
> as more data are included into the analysis. Asymptotic results can supply some insight into ﬁnite-
> sample performance, but we generally prefer to consider the posterior distribution that is in front of
> us. Lindley (1956) and Goel and DeGroot (1981) discuss how to measure the information provided

### 日本語訳（自動翻訳）

> 特に当社のモデルがサイズと複雑性を増加させると、finite のデータに対する推論
> より多くのデータが分析に含まれています。 アスンプトチックの結果は、finiteにいくつかの洞察を提供できます。
> サンプル性能はありますが、私達は一般に前部にあるポスター配分を考慮することを好みます
> リンドリー(1956)とGoelとDeGroot(1981)は、提供された情報を測定する方法について議論します

### 熟語・専門語

- **posterior distribution**: 事後分布。データ観測後の未知量の不確実性を表す分布。

### 要約

- 特に当社のモデルがサイズと複雑性を増加させると、finite のデータに対する推論 より多くのデータが分析に含まれています。

## Chunk 0274

### English（抽出4行）

> by an experiment as how diﬀerent the posterior is from the prior. If the data are not informative on
> some aspects of the model, we may improve the situation by providing more information via priors.
> Furthermore, we often prefer to use a model with parameters that can be updated by the information
> in the data instead of a model that may be closer to the truth but where data are not able to provide

### 日本語訳（自動翻訳）

> 以前のポスターとは異なるように実験することで データの非公式化がない場合
> モデルの側面によっては、事前に情報を提供することで状況を改善することがあります。
> さらに、情報によって更新できるパラメータでモデルを使用することが多い
> 真実に近いモデルではなく、データが提供できないモデルのデータ

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- 以前のポスターとは異なるように実験することで データの非公式化がない場合 モデルの側面によっては、事前に情報を提供することで状況を改善することがあります。

## Chunk 0275

### English（抽出4行）

> suﬃcient information. In Sections 6.2–6.3 we discuss tools for assessing the informativeness of
> individual data points or hyperparameters.
> We illustrate with the problem of estimating the sum of declining exponentials with unknown
> decay rates. This task is a well-known ill-conditioned problem in numerical analysis and also arises

### 日本語訳（自動翻訳）

> 十分な情報。 セクション 6.2–6.3 では、有益な情報を評価するためのツールについて説明します
> 個々のデータポイントまたはハイパーパラメータ。
> 未知の絶え間ない指数の合計を推定する問題について説明
> 減衰率。 このタスクは、数値解析でよく知られている病気で調節された問題であり、またアリス

### 熟語・専門語

- **ESS**: 有効サンプルサイズ。自己相関を考慮した独立サンプル相当数。

### 要約

- 十分な情報。

## Chunk 0276

### English（抽出4行）

> in applications such as pharmacology (Jacquez, 1972). We assume data
> yi = (a1e−b1xi + a2e−b2xi) × eϵi, for i = 1, . . . , n,
> with independent errors ϵi ∼normal(0, σ). The coeﬃcients a1, a2, and the residual standard
> deviation σ are constrained to be positive. The parameters b1 and b2 are also positive—these are

### 日本語訳（自動翻訳）

> 薬理学(Jacquez, 1972)などの用途で。 データを想定
> i = (a1e-b1xi + a2e-b2xi) × eεi, i = 1, . , n,
> 独立したエラーで εi〜normal(0、σ)。 係数 a1、a2、残留標準
> 偏差 σ は正に禁忌です。 パラメータb1とb2も肯定的です。

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- 薬理学(Jacquez, 1972)などの用途で。

## Chunk 0277

### English（抽出4行）

> supposed to be declining, not increasing, exponentials—and are also constrained to be ordered,
> b1 < b2, so as to uniquely deﬁne the two model components.
> We start by simulating fake data from a model where the two curves should be cleanly distin-
> guished, setting b1 = 0.1 and b2 = 2.0, a factor of 20 apart in scale. We simulate 1000 data points

### 日本語訳（自動翻訳）

> 順調に、増加しない、指数関数であるべきであり、また発注されるために禁忌である、
> b1 < b2 は、2 つのモデルコンポーネントを一意に定義するためです。
> 偽物データを2つの曲線を清潔にしないようにするモデルからシミュレートし始めます。
> guished, b1 = 0.1 と b2 = 2.0 の設定, スケールで 20 の要因. 1000点のデータポイントをシミュレート

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- 順調に、増加しない、指数関数であるべきであり、また発注されるために禁忌である、 b1 < b2 は、2 つのモデルコンポーネントを一意に定義するためです。

## Chunk 0278

### English（抽出4行）

> N = 1
> N = 2
> N = 8
> −3 −2 −1 0 1 2 3 −3 −2 −1 0 1 2 3 −3 −2 −1 0 1 2 3

### 日本語訳（自動翻訳）

> N = 1
> N = 2
> N = 8
> 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 日

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- N = 1 N = 2 N = 8 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 日

## Chunk 0279

### English（抽出4行）

> −2
> −1
> mu
> log(sigma)

### 日本語訳（自動翻訳）

> −2
> −1
> ログイン
> ログ(シグマ)

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- −2 −1 ログイン ログ(シグマ)

## Chunk 0280

### English（抽出4行）

> A
> N = 6
> N = 9
> N = 21

### 日本語訳（自動翻訳）

> ツイート
> N = 6
> N = 9
> N = 21

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- ツイート N = 6 N = 9 N = 21

## Chunk 0281

### English（抽出4行）

> 0.3
> 0.6
> 0.9
> 0.3

### 日本語訳（自動翻訳）

> 0.35パーセント
> ツイート
> ツイート
> 0.35パーセント

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- 0.35パーセント ツイート ツイート 0.35パーセント

## Chunk 0282

### English（抽出4行）

> 0.6
> 0.9
> 0.3
> 0.6

### 日本語訳（自動翻訳）

> ツイート
> ツイート
> 0.35パーセント
> ツイート

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- ツイート ツイート 0.35パーセント ツイート

## Chunk 0283

### English（抽出4行）

> 0.9
> −3
> −2
> −1

### 日本語訳（自動翻訳）

> ツイート
> −3
> −2
> −1

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- ツイート −3 −2 −1

## Chunk 0284

### English（抽出4行）

> log(theta[1])
> log(sigma[1])
> B
> Figure 13: Example of how adding data changes the geometry of the posterior distribution. (A)

### 日本語訳（自動翻訳）

> ログ(theta[1])
> ログ(sigma[1])
> ツイート
> 図13: ポスター分布の幾何学的なデータを追加する例。 (A)

### 熟語・専門語

- **posterior distribution**: 事後分布。データ観測後の未知量の不確実性を表す分布。

### 要約

- ログ(theta[1]) ログ(sigma[1]) ツイート 図13: ポスター分布の幾何学的なデータを追加する例。

## Chunk 0285

### English（抽出4行）

> Normal likelihood as a function of mean µ and standard deviation σ with increasing number
> of available observations N drawn from the standard normal distribution.
> For N = 1 the
> likelihood increases without bounds and for N = 2 the geometry is still funnel-like which can

### 日本語訳（自動翻訳）

> 平均μおよび標準偏差のσの機能として正常な可能性は増加数の
> 標準正規分布から描画可能な観察N。
> N = 1の場合
> 境界なしとN = 2のジオメトリは依然として漏斗のように増加する可能性

### 熟語・専門語

- **likelihood**: 尤度。パラメータが与えられたときデータがどれだけ起こりやすいか。

### 要約

- 平均μおよび標準偏差のσの機能として正常な可能性は増加数の 標準正規分布から描画可能な観察N。

## Chunk 0286

### English（抽出4行）

> cause computational problems.
> For N = 8 the funnel-like shape is mostly suppressed.
> (B)
> Practical example using an Lotka-Volterra model of population dynamics (8 parameters total) as

### 日本語訳（自動翻訳）

> 計算上の問題を引き起こす。
> N = 8 の場合、ファンネルのような形状がほとんど抑制されます。
> (B)
> 人口動態(合計8パラメータ)のロカ・ボルテラモデルを用いた実用例

### 熟語・専門語

- **ESS**: 有効サンプルサイズ。自己相関を考慮した独立サンプル相当数。

### 要約

- 計算上の問題を引き起こす。

## Chunk 0287

### English（抽出4行）

> described in Carpenter (2018), showing scatter plots of posterior samples of two parameters drawn
> from ﬁtting the model in Stan. The ﬁt with 6 data points shows a funnel-like shape. The red points
> indicate divergent transitions which signal that the sampler encountered diﬃcult geometry and the
> results are not trustworthy. Stan becomes able to ﬁt the model when 9 data points are used, despite

### 日本語訳（自動翻訳）

> Carpenter (2018) で説明し、描画された 2 つのパラメーターのポスター標本の散布図を示す
> スタンでモデルをフィッティングします。 6つのデータポイントとのフィット感は、ファネルのような形状を示しています。 赤いポイント
> 標本が困難な幾何学に遭遇した信号および標本が渡るdivergent転移を示します
> 結果は信頼できません。 Stanは9つのデータポイントが使用されるときモデルに合うようにすることができますが、

### 熟語・専門語

- **divergent**: divergence。HMC/NUTSで幾何が悪く積分が破綻した警告。

### 要約

- Carpenter (2018) で説明し、描画された 2 つのパラメーターのポスター標本の散布図を示す スタンでモデルをフィッティングします。

## Chunk 0288

### English（抽出4行）

> the slightly uneven geometry. The model is well behaved when ﬁt to 21 data points.
> where the predictor values x are uniformly spaced from 0 to 10, and, somewhat arbitrarily, set
> a1 = 1.0, a2 = 0.8, σ = 0.2. Figure 12a shows true curve and the simulated data. We then use Stan
> to ﬁt the model from the data. The simulations run smoothly and the posterior inference recovers

### 日本語訳（自動翻訳）

> わずかに不均等な幾何学。 モデルは21のデータポイントに収まるときよく振られます。
> 予測値 x が 0 から 10 に均一に間隔をあけているところ、 やや arbitrarily は、
> a1 = 1.0, a2 = 0.8, σ = 0.2. 図12aは真の曲線とシミュレートされたデータを示しています。 その後、スタントを使用する
> データからモデルに合うように。 シミュレーションは円滑に実行され、ポスター推論は回復します

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- わずかに不均等な幾何学。

## Chunk 0289

### English（抽出4行）

> the ﬁve parameters of the model, which is no surprise given that the data have been simulated from
> the model we are ﬁtting.
> But now we make the problem slightly more diﬃcult. The model is still, by construction, true,
> but instead of setting (b1, b2) to (0.1, 2.0), we make them (0.1, 0.2), so now only a factor of 2

### 日本語訳（自動翻訳）

> データをシミュレートしたという驚きの無いモデルの5つのパラメータ
> 私達が付属品であるモデル。
> しかし、今では問題は少し難しくなります。 このモデルは、構造、真、
> しかし、(b1、b2)を(0.1、2.0)に設定する代わりに、それら(0.1、0.2)を作るので、2つの要因だけ

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- データをシミュレートしたという驚きの無いモデルの5つのパラメータ 私達が付属品であるモデル。

## Chunk 0290

### English（抽出4行）

> separates the scales of the two declining exponentials. The simulated data are shown in Figure
> 12b. But now when we try to ﬁt the model in Stan, we get terrible convergence. The two declining
> exponentials have become very hard to tell apart, as we have indicated in the graph by also including
> the curve, y = 1.8e−0.135x, which is essentially impossible to distinguish from the true model given

### 日本語訳（自動翻訳）

> 2つのディクライニング指数のスケールを分離します。 シミュレーションされたデータは図に示します
> 12b. しかし、今、スタンでモデルに合うようにしようとすると、私たちはひどい説得力を手に入れます。 2つのデクライニング
> 指数関数は、グラフに示されているように、また、
> カーブ、y = 1.8e-0.135x、与えられた真のモデルと区別することは本質的に不可能です

### 熟語・専門語

- **ESS**: 有効サンプルサイズ。自己相関を考慮した独立サンプル相当数。

### 要約

- 2つのディクライニング指数のスケールを分離します。

## Chunk 0291

### English（抽出4行）

> these data.
> We can make this computation more stable by adding prior information. For example, default
> normal(0, 1) priors on all the parameters does suﬃcient regularization, while still being weak if the
> model has been set up so the parameters are roughly on unit scale, as discussed in Section 2.3. In

### 日本語訳（自動翻訳）

> これらのデータ。
> 事前情報を追加することで、より安定した計算ができます。 例えば、デフォルト
> 通常の(0, 1) すべてのパラメータの優先順位は十分な正規化を行います, それでも弱い場合
> セクション2.3で議論されているように、モデルがユニットスケールで大体であるため、セットアップされています。 インスタグラム

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- これらのデータ。

## Chunk 0292

### English（抽出4行）

> this case we are assuming this has been done. One could also check the sensitivity of the posterior
> inferences to the choice of prior, either by comparing to alternatives such as normal(0, 0.5) and
> normal(0, 2) or by diﬀerentiating the inferences with respect to the prior scale, as discussed in
> Section 6.3.

### 日本語訳（自動翻訳）

> こういったことが想定されているケースです。 ポスターの感度も確認できる
> 通常の(0, 0.5)などの代替品と比べて、前の選択肢への不当性
> 通常(0, 2) または前方スケールに関しての推論を区別することにより、
> セクション6.3。

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- こういったことが想定されているケースです。

## Chunk 0293

### English（抽出4行）

> Using an informative normal distribution for the prior adds to the tail-log-concavity of the
> posterior density, which leads to a quicker MCMC mixing time. But the informative prior does
> not represent a tradeoﬀof model bias vs. computational eﬃciency; rather, in this case the model
> ﬁtting is improved as the computation burden is eased, an instance of the folk theorem discussed in

### 日本語訳（自動翻訳）

> 事前の非公式な正規分布を使用して、tail-log-concavity に追加します
> より速いMCMCの混合の時間に導くポスター密度。 しかし、情報提供前のことは
> ではなく、トレードオフモデルバイアス対計算効率を表す; むしろ、この場合モデル
> 計算の負担が緩和されるとフィッティングが改善され、議論された民間の理論インスタンス

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- 事前の非公式な正規分布を使用して、tail-log-concavity に追加します より速いMCMCの混合の時間に導くポスター密度。

## Chunk 0294

### English（抽出4行）

> Section 5.1. More generally, there can be strong priors with thick tails, and thus the tail behavior
> is not guaranteed to be more log concave. On the other hand, the prior can be weak in the context
> of the likelihood while still guaranteeing a log-concave tail. This is related to the point that the
> informativeness of a model depends on what questions are being asked.

### 日本語訳（自動翻訳）

> セクション 5.1. より一般的には、太い尾の強い優先順位があり、したがって、尾の行動
> より多くのログ凹面であることを保証するものではありません。 一方、前者はコンテキストで弱くなる
> ログ・コンケーブ・テールをまだ保証している間、可能性の。 これは、その点に関連しています
> モデルの情報は、質問が何であるかによって異なります。

### 熟語・専門語

- **likelihood**: 尤度。パラメータが与えられたときデータがどれだけ起こりやすいか。
- **ESS**: 有効サンプルサイズ。自己相関を考慮した独立サンプル相当数。

### 要約

- セクション 5.1. より一般的には、太い尾の強い優先順位があり、したがって、尾の行動 より多くのログ凹面であることを保証するものではありません。

## Chunk 0295

### English（抽出4行）

> Consider four steps on a ladder of abstraction:
> 1. Poor mixing of MCMC;
> 2. Diﬃcult geometry as a mathematical explanation for the above;
> 3. Weakly informative data for some parts of the model as a statistical explanation for the above;

### 日本語訳（自動翻訳）

> 抽象の梯子の4つのステップを考慮する:
> 1. MCMCの貧しい混合;
> 2. 上記の数学的説明として困難ジオメトリ;
> 3. 上記の統計的説明として、モデルの一部の部分に弱い有益なデータ;

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- 抽象の梯子の4つのステップを考慮する: 1. MCMCの貧しい混合; 2. 上記の数学的説明として困難ジオメトリ; 3. 上記の統計的説明として、モデルの一部の部分に弱い有益なデータ;

## Chunk 0296

### English（抽出4行）

> 4. Substantive prior information as a solution to the above.
> Starting from the beginning of this ladder, we have computational troubleshooting; starting from
> the end, computational workﬂow.
> As another example, when trying to avoid the funnel pathologies of hierarchical models in the

### 日本語訳（自動翻訳）

> 4. 上記への解決策として実質的な事前情報。
> この梯子の始まりから始まり、私達は計算的なトラブルシューティングがあります;から始めて下さい
> エンド、計算ワークフロー。
> 別の例として、階層モデルの漏斗病理を回避しようとすると

### 熟語・専門語

- **troubleshooting**: トラブルシュート。計算・モデル・データの失敗原因を切り分けること。

### 要約

- 4. 上記への解決策として実質的な事前情報。

## Chunk 0297

### English（抽出4行）

> limit when group-level variance parameters approach zero, one could use zero-avoiding priors (for
> example, lognormal or inverse gamma distributions) to avoid the regions of high curvature of the
> likelihood; a related idea is discussed for penalized marginal likelihood estimation by Chung et al.
> (2013, 2014). Zero-avoiding priors can make sense when such prior information is available—such

### 日本語訳（自動翻訳）

> グループレベルの分散パラメータがゼロに近づくと制限, 一つは、ゼロ回避の優先順位を使うことができます (for
> たとえば、lognormal または inverse gamma 分布) は、高い湾曲の領域を回避します。
> 可能性; 関連するアイデアは、Chung et al による罰的証拠金推定のために議論されています。.
> (2013, 2014). そのような事前情報は、このような事前情報が利用可能であるとき、ゼロ回避の事前は意味をすることができます

### 熟語・専門語

- **likelihood**: 尤度。パラメータが与えられたときデータがどれだけ起こりやすいか。

### 要約

- グループレベルの分散パラメータがゼロに近づくと制限, 一つは、ゼロ回避の優先順位を使うことができます (for たとえば、lognormal または inverse gamma 分布) は、高い湾曲の領域を回避します。

## Chunk 0298

### English（抽出4行）

> as for the length-scale parameter of a Gaussian process (Fuglstad et al., 2019)—but we want to be
> careful when using such a restriction merely to make the algorithm run faster. At the very least,
> if we use a restrictive prior to speed computation, we should make it clear that this is information
> being added to the model.

### 日本語訳（自動翻訳）

> Gaussian プロセス (Fuglstad et al., 2019) のlength-scale パラメータとして、
> アルゴリズムがより速く実行するように、このような制限を使用するときに注意してください。 少なくとも、
> スピード計算の前に制限を使用する場合は、この情報が情報であることを明確にする必要があります
> モデルに追加されます。

### 熟語・専門語

- **ESS**: 有効サンプルサイズ。自己相関を考慮した独立サンプル相当数。

### 要約

- Gaussian プロセス (Fuglstad et al., 2019) のlength-scale パラメータとして、 アルゴリズムがより速く実行するように、このような制限を使用するときに注意してください。

## Chunk 0299

### English（抽出4行）

> More generally, we have found that poor mixing of statistical ﬁtting algorithms can often be
> ﬁxed by stronger regularization. This does not come free, though: in order to eﬀectively regularize
> without blurring the very aspects of the model we want to estimate, we need some subject-
> matter knowledge—actual prior information. Haphazardly tweaking the model until computational

### 日本語訳（自動翻訳）

> 一般的には、統計的なフィッティングアルゴリズムの混入が少ないことがよくあります。
> より強い正規化によって固定される。 これは無料ではありませんが、:効果的に正規化するために
> 見積りしたいモデルの非常に面をぼかすことなく、我々はいくつかの主題を必要とします-
> 問題知識 - 実際の事前情報。 誤ってモデルを微調整するまで

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- 一般的には、統計的なフィッティングアルゴリズムの混入が少ないことがよくあります。

## Chunk 0300

### English（抽出4行）

> problems disappear is dangerous and can threaten the validity of inferences without there being a
> good way to diagnose the problem.
> 5.10.
> Adding data

### 日本語訳（自動翻訳）

> 問題は危険であり、そこにあることなしで不当の妥当性を脅かすことができます
> 問題を診断する良い方法。
> 5.10。
> データの追加

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- 問題は危険であり、そこにあることなしで不当の妥当性を脅かすことができます 問題を診断する良い方法。

## Chunk 0301

### English（抽出4行）

> Similarly to adding prior information, one can constrain the model by adding new data sources
> that are handled within the model. For example, a calibration experiment can inform the standard
> deviation of a response.
> In other cases, models that are well behaved for larger datasets can have computational issues

### 日本語訳（自動翻訳）

> 以前の情報を追加するのと同様に、新しいデータソースを追加することによってモデルを制約することができます
> モデル内で処理されます。 例えば、校正実験は標準を知らせることができます
> 応答の偏差。
> 他のケースでは、より大きなデータセットでよく動作するモデルは、計算上の問題を持つことができます

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- 以前の情報を追加するのと同様に、新しいデータソースを追加することによってモデルを制約することができます モデル内で処理されます。

## Chunk 0302

### English（抽出4行）

> in small data regimes; Figure 13 shows an example. While the funnel-like shape of the posterior
> in such cases looks similar to the funnel in hierarchical models, this pathology is much harder to
> avoid, and we can often only acknowledge that the full model is not informed by the data and a
> simpler model needs to be used. Betancourt (2018) further discusses this issue.

### 日本語訳（自動翻訳）

> 小さなデータレジムでは、図13は例を示します。 ポスターのファネル様な形状ながら
> そのようなケースでは、階層モデルの漏斗に似ています、この病理ははるかに困難です
> 回避し、多くの場合、フルモデルがデータとaによって通知されていないことを認識することができます
> よりシンプルなモデルを使う必要があります。 Betancourt (2018)は、この問題をさらに議論しました。

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- 小さなデータレジムでは、図13は例を示します。

## Chunk 0303

### English（抽出4行）

> 6.
> Evaluating and using a fitted model
> Once a model has been ﬁt, the workﬂow of evaluating that ﬁt is more convoluted, because there are
> many diﬀerent things that can be checked, and each of these checks can lead in many directions.

### 日本語訳（自動翻訳）

> 6。
> 適合モデルの評価・利用
> モデルがフィットしたら、そのフィット感を評価するワークフローは、そこにありますので、
> チェックできるさまざまなこと、そしてこれらのチェックのそれぞれが多くの方向でリードすることができます。

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- 6。

## Chunk 0304

### English（抽出4行）

> Statistical models can be ﬁt with multiple goals in mind, and statistical methods are developed for
> diﬀerent groups of users. The aspects of a model that needs to be checked will depend on the
> application.
> 6.1.

### 日本語訳（自動翻訳）

> 統計モデルは、複数の目標を念頭に置くことができ、統計的な方法は、
> ユーザーの異なるグループ。 チェックが必要なモデルの側面は、
> アプリケーション。
> 6.1..

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- 統計モデルは、複数の目標を念頭に置くことができ、統計的な方法は、 ユーザーの異なるグループ。

## Chunk 0305

### English（抽出4行）

> Posterior predictive checking
> Posterior predictive checking is analogous to prior predictive checking (Section 2.4), but the
> parameter draws used in the simulations come from the posterior distribution rather than the prior.
> While prior predictive checking is a way to understand a model and the implications of the speciﬁed

### 日本語訳（自動翻訳）

> ポスター予測チェック
> ポスター予測チェックは、事前の予測チェック(セクション2.4)に類似していますが、
> シミュレーションで使用されるパラメータは、以前のものではなく、ポスター分布から来ています。
> 事前の予測チェックは、モデルと指定された影響を理解する方法です

### 熟語・専門語

- **prior predictive**: 事前予測。データを見る前のpriorだけで生成される予測分布を確認する診断。
- **posterior predictive**: 事後予測。推定後のモデルが観測データの特徴を再現できるかを見る診断。
- **posterior distribution**: 事後分布。データ観測後の未知量の不確実性を表す分布。

### 要約

- ポスター予測チェック ポスター予測チェックは、事前の予測チェック(セクション2.4)に類似していますが、 シミュレーションで使用されるパラメータは、以前のものではなく、ポスター分布から来ています。

## Chunk 0306

### English（抽出4行）

> priors, posterior predictive checking also allows one to examine the ﬁt of a model to real data (Box,
> 1980, Rubin, 1984, Gelman, Meng, and Stern, 1996).
> When comparing simulated datasets from the posterior predictive distribution to the actual
> dataset, if the dataset we are analyzing is unrepresentative of the posterior predictive distribution,

### 日本語訳（自動翻訳）

> 先ほど, ポスター予測チェックも、モデルの適合を実際のデータに調べることができます (ボックス,
> 1980、ルビン、1984、ゲルマン、メング、スタン、1996)。
> ポスター予測分布から実際のシミュレートデータセットを比較する場合
> データセットは、我々が分析しているデータセットがポスター予測分布の非表現的である場合、

### 熟語・専門語

- **posterior predictive**: 事後予測。推定後のモデルが観測データの特徴を再現できるかを見る診断。

### 要約

- 先ほど, ポスター予測チェックも、モデルの適合を実際のデータに調べることができます (ボックス, 1980、ルビン、1984、ゲルマン、メング、スタン、1996)。

## Chunk 0307

### English（抽出4行）

> this indicates a failure of the model to describe an aspect of the data. The most direct checks compare
> the simulations from the predictive distribution to the full distribution of the data or a summary
> statistic computed from the data or subgroups of the data, especially for groupings not included in
> the model (see Figure 14). There is no general way to choose which checks one should perform on

### 日本語訳（自動翻訳）

> これにより、データの側面を記述するモデルの失敗を示します。 最も直接チェックは比較します
> 予測分布から、データの完全分布または要約までのシミュレーション
> 特に、データのデータやサブグループから計算された統計は、グループ化には含まれていません。
> モデル(図14参照) 誰が実行すべきかを選択する一般的な方法はありません

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- これにより、データの側面を記述するモデルの失敗を示します。

## Chunk 0308

### English（抽出4行）

> a model, but running a few such direct checks is a good safeguard against gross misspeciﬁcation.
> There is also no general way to decide when a check that fails requires adjustments to the model.
> Depending on the goals of the analysis and the costs and beneﬁts speciﬁc to the circumstances,
> we may tolerate that the model fails to capture certain aspects of the data or it may be essential to

### 日本語訳（自動翻訳）

> モデルですが、このような直接チェックを実行することは、グロス誤差に対する良い保護です。
> チェックが失敗したときに決定する一般的な方法はモデルへの調整が必要です。
> 分析の目的や、状況に応じたコストと利点に応じて、
> モデルは、データの特定の側面をキャプチャできないか、またはそれが不可欠である可能性があることを許容することができます

### 熟語・専門語

- **ESS**: 有効サンプルサイズ。自己相関を考慮した独立サンプル相当数。

### 要約

- モデルですが、このような直接チェックを実行することは、グロス誤差に対する良い保護です。

## Chunk 0309

### English（抽出4行）

> invest in improving the model. In general, we try to ﬁnd “severe tests” (Mayo, 2018): checks that
> are likely to fail if the model would give misleading answers to the questions we care most about.
> Figure 15 shows a more involved posterior predictive check from an applied project. This
> example demonstrates the way that predictive simulation can be combined with graphical display,

### 日本語訳（自動翻訳）

> モデルの改善に投資します。 一般的には「厳しいテスト」(Mayo、2018): チェック
> モデルは、私たちが最も気にしている質問に誤解を招く答えを与えるかどうかに失敗する可能性があります。
> 図15は、適用されたプロジェクトから、より関与するポスター予測チェックを示しています。 お問い合わせ
> たとえば、予測シミュレーションがグラフィカル表示と組み合わせることができる方法を示します。

### 熟語・専門語

- **posterior predictive**: 事後予測。推定後のモデルが観測データの特徴を再現できるかを見る診断。

### 要約

- モデルの改善に投資します。

## Chunk 0310

### English（抽出4行）

> and it also gives a sense of the practical challenges of predictive checking, in that it is often necessary
> to come up with a unique visualization tailored to the speciﬁc problem at hand.
> 6.2.
> Cross validation and influence of individual data points and subsets of the data

### 日本語訳（自動翻訳）

> そして、それはまた、予測チェックの実用的な課題の感覚を与えます, それはしばしば必要です
> 特定の問題に合わせたユニークな視覚化を手元で実現します。
> 6.2. .
> データの個々のデータポイントとサブセットの相互検証と影響

### 熟語・専門語

- **cross validation**: 交差検証。汎化性能を推定するためにデータを分割/近似除外する評価法。
- **ESS**: 有効サンプルサイズ。自己相関を考慮した独立サンプル相当数。
- **validation**: 検証。モデルが目的・データ・外部知識に照らして妥当かを確認すること。

### 要約

- そして、それはまた、予測チェックの実用的な課題の感覚を与えます, それはしばしば必要です 特定の問題に合わせたユニークな視覚化を手元で実現します。

## Chunk 0311

### English（抽出4行）

> Posterior predictive checking is often suﬃcient for revealing model misﬁt, but as it uses data both
> for model ﬁtting and misﬁt evaluation, it can be overly optimistic. In cross validation, part of the
> data is left out, the model is ﬁt to the remaining data, and predictive performance is checked on
> the left-out data. This improves predictive checking diagnostics, especially for ﬂexible models (for

### 日本語訳（自動翻訳）

> ポスター予測チェックは、モデルの不備を明らかにするのに十分ですが、両方のデータを使用する
> モデルフィッティングと不適切な評価のために、それは過度に最適化することができます。 相互検証では、一部
> データを残し、残りのデータにモデルは収まり、予測的なパフォーマンスがチェックされます。
> 左側のデータ。 これは、特に柔軟なモデルのための予測検査診断を改善します(for

### 熟語・専門語

- **posterior predictive**: 事後予測。推定後のモデルが観測データの特徴を再現できるかを見る診断。
- **cross validation**: 交差検証。汎化性能を推定するためにデータを分割/近似除外する評価法。
- **validation**: 検証。モデルが目的・データ・外部知識に照らして妥当かを確認すること。

### 要約

- ポスター予測チェックは、モデルの不備を明らかにするのに十分ですが、両方のデータを使用する モデルフィッティングと不適切な評価のために、それは過度に最適化することができます。

## Chunk 0312

### English（抽出4行）

> example, overparameterized models with more parameters than observations).
> Three diagnostic approaches using cross validation that we have found useful for further evalu-
> ating models are
> 1. calibration checks using the cross validation predictive distribution,

### 日本語訳（自動翻訳）

> たとえば、観測値よりも複数のパラメータを持つオーバーパラメータモデル)。
> さらなる評価のために有用であることを発見したクロス検証を使用して3つの診断アプローチ-
> チャットモデルは
> 1. 口径測定は十字の検証の予測的な配分を使用して点検します、

### 熟語・専門語

- **cross validation**: 交差検証。汎化性能を推定するためにデータを分割/近似除外する評価法。
- **validation**: 検証。モデルが目的・データ・外部知識に照らして妥当かを確認すること。

### 要約

- たとえば、観測値よりも複数のパラメータを持つオーバーパラメータモデル)。

## Chunk 0313

### English（抽出4行）

> 2. identifying which observations or groups of observations are most diﬃcult to predict,
> 3. identifying how inﬂuential particular observations are, that is, how much information they
> provide on top of other observations.
> In all three cases, eﬃcient approximations to leave-one-out cross-validation using importance

### 日本語訳（自動翻訳）

> 2. 観察や観察グループが予測が最も困難であるかを識別する
> 3. 影響力ある特定の観察がいかにあるか、すなわち、それらがいかに多くの情報であるかを識別します
> ほかの観察を上回る。
> すべての3つのケースでは、重要度を使用して、一時停止の断続権を離れる効率的な近似

### 熟語・専門語

- **leave-one-out**: LOO。一点ずつ除外した予測評価を効率的に近似する交差検証。
- **validation**: 検証。モデルが目的・データ・外部知識に照らして妥当かを確認すること。

### 要約

- 2. 観察や観察グループが予測が最も困難であるかを識別する 3. 影響力ある特定の観察がいかにあるか、すなわち、それらがいかに多くの情報であるかを識別します ほかの観察を上回る。

## Chunk 0314

### English（抽出4行）

> sampling can facilitate practical use by removing the need to re-ﬁt the model when each data point
> is left out (Vehtari et al., 2017, Paananen et al., 2020).
> −40
> y

### 日本語訳（自動翻訳）

> samplingは各データポイントが時モデルを再適合させる必要性を取除くことによって実用的な使用を促進できます
> 左(Vehtari et al., 2017, Paananen et al., 2020).
> −40
> ログイン

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- samplingは各データポイントが時モデルを再適合させる必要性を取除くことによって実用的な使用を促進できます 左(Vehtari et al., 2017, Paananen et al., 2020). −40 ログイン

## Chunk 0315

### English（抽出4行）

> yrep
> A
> 0.5
> 1.0

### 日本語訳（自動翻訳）

> シロップ
> ツイート
> 0.5パーセント
> 1.0 の

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- シロップ ツイート 0.5パーセント 1.0 の

## Chunk 0316

### English（抽出4行）

> 1.5
> 2.0
> T = sd
> T(yrep)

### 日本語訳（自動翻訳）

> 1.5マイル
> 2.0 の
> T = sd
> T(麻)

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- 1.5マイル 2.0 の T = sd T(麻)

## Chunk 0317

### English（抽出4行）

> T(y)
> B
> Count
> yrep

### 日本語訳（自動翻訳）

> ツイート
> ツイート
> カウント数
> シロップ

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- ツイート ツイート カウント数 シロップ

## Chunk 0318

### English（抽出4行）

> y
> C
> High
> Low

### 日本語訳（自動翻訳）

> ログイン
> ツイート
> 高い
> 低い

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- ログイン ツイート 高い 低い

## Chunk 0319

### English（抽出4行）

> Count
> yrep
> y
> D

### 日本語訳（自動翻訳）

> カウント数
> シロップ
> ログイン
> ダイバーシティ

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- カウント数 シロップ ログイン ダイバーシティ

## Chunk 0320

### English（抽出4行）

> Figure 14: Examples of diagnosing model misﬁt with simple posterior predictive checks as imple-
> mented in the bayesplot R package. In all plots y is plotted based on the input data and yrep based
> on the distribution of posterior simulations. (A) A “density” check for a normal distribution being
> ﬁt to data simulated from a lognormal distribution: the tails of the yrep behave very diﬀerently

### 日本語訳（自動翻訳）

> 図14:単純なポスター予測チェックでモデルの不適切な診断例-
> bayesplot Rのパッケージで隠される。 すべてのプロットでは、y は入力データおよび yrep に基づいてプロットされます
> ポスターシミュレーションの配布 (A) 通常分布の「密度」チェック
> lognormal 分布からシミュレートされたデータに収まる: yrep の尾は非常に異なる振る舞い

### 熟語・専門語

- **posterior predictive**: 事後予測。推定後のモデルが観測データの特徴を再現できるかを見る診断。

### 要約

- 図14:単純なポスター予測チェックでモデルの不適切な診断例- bayesplot Rのパッケージで隠される。

## Chunk 0321

### English（抽出4行）

> than for y. (B) A “statistic” check for a binomial distribution being ﬁt to data simulated from a
> beta-binomial distribution. Histogram of standard deviation (sd) of the yrep datasets is compared to
> sd of y. The check shows that the data have larger sd than what the model can handle. (C) A “bars”
> check for discrete data (note the switch of colors between y and yrep). This check looks good: the

### 日本語訳（自動翻訳）

> y. (B) からシミュレートされたデータに収まる「統計的」チェック
> β-binomial分布。 yrep データセットの標準的な偏差(sd)のヒストグラムは、
> yのsd。 チェックは、モデルが処理できるものよりも大きいsdを持っていることを示しています。 (C) 「バー」
> ディスクリートデータ(y と yrep の間の色の切り替えに注意)をチェックします。 このチェックは良いです:

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- y. (B) からシミュレートされたデータに収まる「統計的」チェック β-binomial分布。

## Chunk 0322

### English（抽出4行）

> distribution of frequencies of individual counts in y falls well within those in yrep. (D) The same
> model and data but with the check grouped by a covariate that was not included in the model but
> in fact inﬂuenced the response. The High subgroup systematically deviates from the range of yrep,
> indicating that there is an additional source of variability that the model fails to capture.

### 日本語訳（自動翻訳）

> y の個々のカウントの頻度の分布は、yrep のそれらの中でよく落ちます。 (D) 同じ
> モデルとデータが、モデルに含まれていないコワリエートによってグループ化されたチェックで
> 実際には応答に影響を及ぼしました。 高いサブグループは、シロップの範囲から体系的に逸脱します。
> モデルがキャプチャに失敗する分散性の追加ソースがあることを示す。

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- y の個々のカウントの頻度の分布は、yrep のそれらの中でよく落ちます。

## Chunk 0323

### English（抽出4行）

> Although perfect calibration of predictive distributions is not the ultimate goal of Bayesian
> inference, looking at how well calibrated leave-one-out cross validation (LOO-CV) predictive dis-
> tributions are, can reveal opportunities to improve the model. While posterior predictive checking
> often compares the marginal distribution of the predictions to the data distribution, leave-one-out

### 日本語訳（自動翻訳）

> 予測分布の完璧な校正は、ベイジアンの究極の目標ではありませんが
> 推論, よく目立たせる残忍なクロス検証 (LOO-CV) 予測dis-
> トリビューションはモデルを改善するための機会を明らかにすることができます。 ポスター予測チェック中
> 多くの場合、予測の余剰分布をデータ分布に比較し、一時停止

### 熟語・専門語

- **posterior predictive**: 事後予測。推定後のモデルが観測データの特徴を再現できるかを見る診断。
- **cross validation**: 交差検証。汎化性能を推定するためにデータを分割/近似除外する評価法。
- **leave-one-out**: LOO。一点ずつ除外した予測評価を効率的に近似する交差検証。
- **validation**: 検証。モデルが目的・データ・外部知識に照らして妥当かを確認すること。
- **prediction**: 予測。未知/将来/除外データに対する分布や点推定。

### 要約

- 予測分布の完璧な校正は、ベイジアンの究極の目標ではありませんが 推論, よく目立たせる残忍なクロス検証 (LOO-CV) 予測dis- トリビューションはモデルを改善するための機会を明らかにすることができます。

## Chunk 0324

### English（抽出4行）

> cross validation predictive checking looks at the calibration of conditional predictive distributions.
> Under a good calibration, the conditional cumulative probability distribution of the predictive dis-
> tributions (also known as probability integral transformations, PIT) given the left-out observations
> are uniform. Deviations from uniformity can reveal, for example, under or overdispersion of the

### 日本語訳（自動翻訳）

> 相互検証予測チェックは、条件付き予測分布の較正を見てみましょう。
> 良い口径測定の下で、予測のdisの条件的な累積確率分布-
> 左アウトの観察によるトリビューション(確率積分変換、PITとも呼ばれる)
> 制服です。 均一性からの逸脱は、例えば、下または過分散の

### 熟語・専門語

- **cross validation**: 交差検証。汎化性能を推定するためにデータを分割/近似除外する評価法。
- **validation**: 検証。モデルが目的・データ・外部知識に照らして妥当かを確認すること。

### 要約

- 相互検証予測チェックは、条件付き予測分布の較正を見てみましょう。

## Chunk 0325

### English（抽出4行）

> predictive distributions. Figure 16 shows an example from Gabry et al. (2019) where leave-one-out
> cross validation probability integral transformation (LOO-PIT) values are too concentrated near
> Figure 15: Example of a posterior predictive check. The left column shows observed data from a
> psychology experiment, displayed as a 15×23 array of binary responses from each of 6 participants,

### 日本語訳（自動翻訳）

> 予測分布。 図16 は、Gabry et al. (2019) から退出した例を示します。
> 相互検証の確率の積分変換(LOO-PIT)値が近すぎる
> 図15: ポスター予測チェック例 左側の列は、観察されたデータをから示します
> 心理学実験は、6人の参加者のそれぞれから15×23配列のバイナリ応答として表示され、

### 熟語・専門語

- **posterior predictive**: 事後予測。推定後のモデルが観測データの特徴を再現できるかを見る診断。
- **cross validation**: 交差検証。汎化性能を推定するためにデータを分割/近似除外する評価法。
- **leave-one-out**: LOO。一点ずつ除外した予測評価を効率的に近似する交差検証。
- **validation**: 検証。モデルが目的・データ・外部知識に照らして妥当かを確認すること。

### 要約

- 予測分布。

## Chunk 0326

### English（抽出4行）

> ordered by row, column, and person.
> The right columns show 7 replicated datasets from the
> posterior predictive distribution of the ﬁtted model. Each replicated dataset has been ordered, as
> this is part of the display. The check reveals some patterns in the observed that do not appear in

### 日本語訳（自動翻訳）

> 行、列、人によって注文。
> 右側の列は、7つの重複したデータセットを表示します。
> フィットモデルの耐圧予測分布。 複製されたデータセットは、
> これは表示の一部です。 チェックでは、観察されていないパターンが現れている

### 熟語・専門語

- **posterior predictive**: 事後予測。推定後のモデルが観測データの特徴を再現できるかを見る診断。

### 要約

- 行、列、人によって注文。

## Chunk 0327

### English（抽出4行）

> the replications, indicating a aspect of lack of ﬁt of model to data. From Gelman et al. (2013).
> the middle, revealing that the predictive distributions are overdispersed compared to the actual
> conditional observations.
> In addition to looking at the calibration of the conditional predictive distributions, we can also

### 日本語訳（自動翻訳）

> レプリケーション、モデルのフィットの欠如をデータに示します。 ゲルマン ら. (2013).
> ミドルは、予測分布が実際のものと比較して分散されていることを明らかに
> 条件付き観察。
> 条件予測分布の校正を調べるだけでなく、

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- レプリケーション、モデルのフィットの欠如をデータに示します。

## Chunk 0328

### English（抽出4行）

> look at which observations are hard to predict and see if there is a pattern or explanation for why
> some are harder to predict than others. This approach can reveal potential problems in the data or
> data processing, or point to directions for model improvement (Vehtari et al., 2017, Gabry et al.,
> 2019). We illustrate with an analysis of a survey of residents from a small area in Bangladesh that

### 日本語訳（自動翻訳）

> どの観察が予測が困難であるかを見て、なぜパターンや説明があるのか
> 他の人よりも予測するのが困難です。 このアプローチは、データの潜在的な問題や
> データ処理、モデル改善(Vehtari et al.、2017、Gabry et al.、
> 2019年12月1日 バングラデシュの小さな地域から住民の調査を分析し、

### 熟語・専門語

- **ESS**: 有効サンプルサイズ。自己相関を考慮した独立サンプル相当数。

### 要約

- どの観察が予測が困難であるかを見て、なぜパターンや説明があるのか 他の人よりも予測するのが困難です。

## Chunk 0329

### English（抽出4行）

> was aﬀected by arsenic in drinking water. Respondents with elevated arsenic levels in their wells
> were asked if they were interested in switching to water from a neighbor’s well, and a series of
> models were ﬁt to predict this binary response given household information (Vehtari et al., 2017).
> Figure 17 compares the pointwise log scores for two of the models. The scattered blue dots on

### 日本語訳（自動翻訳）

> 飲水時にアルセニックの影響を受けました。 彼らの井戸の高められたarsenicレベルとの応答性
> 隣の井戸から水に切替えるのに興味があったら、シリーズ
> モデルは、世帯情報(Vehtari et al., 2017)を与えられたこのバイナリ応答を予測するために適合しました。
> 図17は、モデルの2つに対して、ポインシャルログスコアを比較します。 散らばる青の点

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- 飲水時にアルセニックの影響を受けました。

## Chunk 0330

### English（抽出4行）

> the left side of Figure 17a and on the lower right of Figure 17b correspond to data points for which
> one of the models ﬁts particularly poorly—that is, large negative contributions to the expected log
> predictive density. We can sum all of the pointwise diﬀerences to yield an estimated diﬀerence in
> expected log predictive densities elpdloo of 16.4 with a standard error of just 4.4, but beyond that

### 日本語訳（自動翻訳）

> 図17aの左側と図17bの下部の右側は、データポイントに対応する
> モデルの1つは、特に悪いことに収まる - つまり、予想されるログへの大きな負の貢献
> 予測密度。 私たちは、すべての点心的な違いをまとめて推定差を生じることができます
> 予想されるログ予測密度 elpdloo の 16.4 の標準的なエラーだけで 4.4, しかし、それを超えて

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- 図17aの左側と図17bの下部の右側は、データポイントに対応する モデルの1つは、特に悪いことに収まる - つまり、予想されるログへの大きな負の貢献 予測密度。

## Chunk 0331

### English（抽出4行）

> we can use this plot to ﬁnd which data points create problems for the model, in this case 10–15
> non-switchers with very high existing arsenic levels.
> In this particular example, we did not follow up on this modeling issue, because even more
> elaborate models that ﬁt the data better do not change the conclusions and thus would not change

### 日本語訳（自動翻訳）

> このプロットを使用して、モデルのデータポイントが問題になるかを調べることができます。この場合、10〜15
> 非常に高い既存のarsenicレベルが付いている非スイッチャ。
> この例では、このモデリングの問題に追随しませんでした。
> データをよりよく収まる精巧なモデルは、結論を変えず、変化しない

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- このプロットを使用して、モデルのデータポイントが問題になるかを調べることができます。

## Chunk 0332

### English（抽出4行）

> any recommended actions in Bangladesh. Gabry et al. (2019) provide an example where LOO-CV
> indicated problems that motivated eﬀorts to improve the statistical model.
> The above two approaches focus on the predictions, but we can also look at how parameter
> Figure 16: Leave-one-out cross validation probability integral transformation (LOO-PIT) plot

### 日本語訳（自動翻訳）

> バングラデシュでの推奨行為。 Gabry et al. (2019) は LOO-CV のインスタンスを提供
> 統計モデルを改善するための意欲的な努力を示す問題。
> 上記の2つのアプローチは予測に焦点を合わせていますが、どのようにパラメータを調べることもできます
> 図16: 離脱クロス検証確率積分変換(LOO-PIT)プロット

### 熟語・専門語

- **cross validation**: 交差検証。汎化性能を推定するためにデータを分割/近似除外する評価法。
- **leave-one-out**: LOO。一点ずつ除外した予測評価を効率的に近似する交差検証。
- **validation**: 検証。モデルが目的・データ・外部知識に照らして妥当かを確認すること。
- **prediction**: 予測。未知/将来/除外データに対する分布や点推定。

### 要約

- バングラデシュでの推奨行為。

## Chunk 0333

### English（抽出4行）

> evaluating the calibration of predictions from a ﬁtted model. Under perfect calibration, LOO-PIT
> values would be uniform. In this case the values are concentrated near the middle, indicating
> predictive distributions that are too wide. From Gabry et al. (2019).
> −3.5

### 日本語訳（自動翻訳）

> 適合したモデルから予測の校正を評価する。 完全な口径測定の下、LOO-PIT
> 値が均一になります。 この場合、値が中央付近に集中し、
> あまりにも広い予測分布。 Gabry et al. (2019) から。
> ツイート

### 熟語・専門語

- **prediction**: 予測。未知/将来/除外データに対する分布や点推定。

### 要約

- 適合したモデルから予測の校正を評価する。

## Chunk 0334

### English（抽出4行）

> −3
> −2.5
> −2
> −1.5

### 日本語訳（自動翻訳）

> −3
> −2.5
> −2
> −1.5

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- −3 −2.5 −2 −1.5

## Chunk 0335

### English（抽出4行）

> −1
> −0.5
> −3
> −2

### 日本語訳（自動翻訳）

> −1
> −0.5 まで
> −3
> −2

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- −1 −0.5 まで −3 −2

## Chunk 0336

### English（抽出4行）

> −1
> LOO1
> LOO2
> Didn’t switch

### 日本語訳（自動翻訳）

> −1
> ロオ1
> ロオ2
> スイッチがない

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- −1 ロオ1 ロオ2 スイッチがない

## Chunk 0337

### English（抽出4行）

> Switched
> −1
> −0.5
> 0.5

### 日本語訳（自動翻訳）

> スイッチ
> −1
> −0.5 まで
> 0.5パーセント

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- スイッチ −1 −0.5 まで 0.5パーセント

## Chunk 0338

### English（抽出4行）

> 1.5
> 2.5
> −1
> −0.5

### 日本語訳（自動翻訳）

> 1.5マイル
> 2.5マイル
> −1
> −0.5 まで

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- 1.5マイル 2.5マイル −1 −0.5 まで

## Chunk 0339

### English（抽出4行）

> log(arsenic)
> LOO1 −LOO2
> Didn’t switch
> Switched

### 日本語訳（自動翻訳）

> ログ(感度)
> LOO1 -LOO2(ロオ1)
> スイッチがない
> スイッチ

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- ログ(感度) LOO1 -LOO2(ロオ1) スイッチがない スイッチ

## Chunk 0340

### English（抽出4行）

> Figure 17: Logistic regression example, comparing two models in terms of their pointwise contribu-
> tions to leave one out (LOO) cross validation error: (a) comparing contributions of LOO directly;
> (b) plotting the diﬀerence in LOO as a function of a key predictor (the existing arsenic level). To
> aid insight, we have colored the data according to the (binary) output, with red corresponding to

### 日本語訳（自動翻訳）

> 図17: 論理的な回帰例、その意味論争の面で2つのモデルを比較する-
> 1つの(LOO)クロスバリデーションエラー(a)を直接LoOのコントリビューションを比較する。
> (b) LOO の差を主要な予測機能としてプロットする (既存の arsenic レベル)。 お問い合わせ
> 援助の洞察、私達は(バイナリ)の出力に従ってデータに、赤い対応しました着色しました

### 熟語・専門語

- **cross validation**: 交差検証。汎化性能を推定するためにデータを分割/近似除外する評価法。
- **ESS**: 有効サンプルサイズ。自己相関を考慮した独立サンプル相当数。
- **validation**: 検証。モデルが目的・データ・外部知識に照らして妥当かを確認すること。

### 要約

- 図17: 論理的な回帰例、その意味論争の面で2つのモデルを比較する- 1つの(LOO)クロスバリデーションエラー(a)を直接LoOのコントリビューションを比較する。

## Chunk 0341

### English（抽出4行）

> y = 1 and blue representing y = 0. For any given data point, one model will ﬁt better than another,
> but for this example the graphs reveal that the diﬀerence in LOO between the models arises from
> the linear model’s poor predictions for 10–15 particular data points. From Vehtari et al. (2017).
> inferences change when each data point is left out, which provides a sense of the inﬂuence of each

### 日本語訳（自動翻訳）

> y = 1 と y = 0 を表す青。 与えられたデータポイントのために、1つのモデルは別のものよりよく合います、
> しかし、この例では、グラフは、モデル間のLOOの違いは、
> リニアモデルの10〜15特定のデータポイントの予報が悪い。 Vehtari et al. (2017) から。
> 各データポイントが残っているときの推論が変化し、それぞれの影響の感覚を提供します

### 熟語・専門語

- **prediction**: 予測。未知/将来/除外データに対する分布や点推定。

### 要約

- y = 1 と y = 0 を表す青。

## Chunk 0342

### English（抽出4行）

> observation. As with cross validation more generally, this approach has limitations if the data are
> clustered or otherwise structured so that multiple points would need to be removed to have an eﬀect,
> but it can still be part of general Bayesian workﬂow, given that it is computationally inexpensive
> and can be valuable in many applied settings. Following this cross validation idea, the inﬂuence

### 日本語訳（自動翻訳）

> 観察。 より一般的にクロス検証と同様に、このアプローチは、データがなければ制限があります
> 複数のポイントが効果をもたらすために取除かれるか、またはそうように構造化されて、
> しかし、それは完全に安価であるというと、一般的にベイジアンのワークフローの一部であり得る。
> 多くの適用された設定で価値があり。 このクロス検証のアイデアに続いて、影響

### 熟語・専門語

- **cross validation**: 交差検証。汎化性能を推定するためにデータを分割/近似除外する評価法。
- **validation**: 検証。モデルが目的・データ・外部知識に照らして妥当かを確認すること。

### 要約

- 観察。

## Chunk 0343

### English（抽出4行）

> of an individual data point yi can be summarized according to properties of the distribution of the
> importance weights computed when approximating LOO-CV (see Vehtari et al., 2017 for details
> on the approximation and the corresponding implementation in the loo R package (Vehtari et al.
> 2020)).

### 日本語訳（自動翻訳）

> 個々のデータポイントの yi は分布の特性に従って要約することができます
> LOO-CV(Vehtari et al., 2017 参照)を近似するときに計算される重要度
> 近似とloo Rパッケージ(Vehtari et al)で対応する実装。
> 2020年)

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- 個々のデータポイントの yi は分布の特性に従って要約することができます LOO-CV(Vehtari et al., 2017 参照)を近似するときに計算される重要度 近似とloo Rパッケージ(Vehtari et al)で対応す…

## Chunk 0344

### English（抽出4行）

> An alternative approach to importance weighting is to frame the removal of data points as a
> gradient in a larger model space. Suppose we have a simple independent likelihood, Qn
> i=1 p(yi|θ),
> and we work with the more general form, Qn

### 日本語訳（自動翻訳）

> 重要な重みへの代替アプローチは、データポイントの除去をフレーム化することです
> より大きいモデル空間で勾配。 簡単な独立した可能性、Qnがあるとします
> i=1 p(yi|θ),
> そして私達はより多くの一般的な形態、Qnと働かせます

### 熟語・専門語

- **likelihood**: 尤度。パラメータが与えられたときデータがどれだけ起こりやすいか。

### 要約

- 重要な重みへの代替アプローチは、データポイントの除去をフレーム化することです より大きいモデル空間で勾配。

## Chunk 0345

### English（抽出4行）

> i=1 p(yi|θ)αi, which reduces to the likelihood of the
> original model when αi = 1 for all i.
> Leave-one-out cross validation corresponds to setting
> αi = 0 for one observation at a time. But another option, discussed by Giordano et al. (2018) and

### 日本語訳（自動翻訳）

> i=1 p(yi|θ)αiは、その可能性を低下させる
> αi = 1 が全ての i の場合のオリジナルモデル。
> 退去クロスバリデーションは設定に対応
> αi = 一度に1つの観察のための0。 しかし、別のオプション, によって議論 Giordano ら. (2018) と

### 熟語・専門語

- **cross validation**: 交差検証。汎化性能を推定するためにデータを分割/近似除外する評価法。
- **leave-one-out**: LOO。一点ずつ除外した予測評価を効率的に近似する交差検証。
- **likelihood**: 尤度。パラメータが与えられたときデータがどれだけ起こりやすいか。
- **validation**: 検証。モデルが目的・データ・外部知識に照らして妥当かを確認すること。

### 要約

- i=1 p(yi|θ)αiは、その可能性を低下させる αi = 1 が全ての i の場合のオリジナルモデル。

## Chunk 0346

### English（抽出4行）

> implemented by Giordano (2018), is to compute the gradient of the augmented log likelihood as a
> function of α: this can be interpreted as a sort of diﬀerential cross validation or inﬂuence function.
> Cross validation for multilevel (hierarchical) models requires more thought. Leave-one-out is
> still possible, but it does not always match our inferential goals. For example, when performing

### 日本語訳（自動翻訳）

> Giordano (2018) が実装したのは、拡張されたログのグラデーションを以下のように計算することです。
> αの機能:これは、異なるクロスバリデーションやインフルエンザ機能として解釈することができます。
> マルチレベル(階層)モデルのクロスバリデーションは、より多くの考えが必要です。 退去は
> それでも可能ですが、常に本能的な目標と一致しません。 例えば、実行時に

### 熟語・専門語

- **cross validation**: 交差検証。汎化性能を推定するためにデータを分割/近似除外する評価法。
- **leave-one-out**: LOO。一点ずつ除外した予測評価を効率的に近似する交差検証。
- **likelihood**: 尤度。パラメータが与えられたときデータがどれだけ起こりやすいか。
- **validation**: 検証。モデルが目的・データ・外部知識に照らして妥当かを確認すること。

### 要約

- Giordano (2018) が実装したのは、拡張されたログのグラデーションを以下のように計算することです。

## Chunk 0347

### English（抽出4行）

> multilevel regression for adjusting political surveys, we are often interested in estimating opinion at
> the state level. A model can show real improvements at the state level with this being undetectable
> at the level of cross validation of individual observations (Wang and Gelman, 2016). Millar (2018),
> Merkle, Furr, and Rabe-Hesketh (2019), and Vehtari (2019) demonstrate diﬀerent cross validation

### 日本語訳（自動翻訳）

> 政治的調査を調整するための多重レベルの回帰, 我々はしばしば推定意見に興味があります
> 状態レベル。 モデルは、この検出できない状態レベルで実際の改善を示すことができます
> 個々の観察の交差検証(ワンとゲルマン、2016) ミラー(2018),
> Merkle, Furr, Rabe-Hesketh (2019), Vehtari (2019) は、異なるクロス検証を実証します

### 熟語・専門語

- **cross validation**: 交差検証。汎化性能を推定するためにデータを分割/近似除外する評価法。
- **ESS**: 有効サンプルサイズ。自己相関を考慮した独立サンプル相当数。
- **validation**: 検証。モデルが目的・データ・外部知識に照らして妥当かを確認すること。

### 要約

- 政治的調査を調整するための多重レベルの回帰, 我々はしばしば推定意見に興味があります 状態レベル。

## Chunk 0348

### English（抽出4行）

> variants and their approximations in hierarchical models, including leave-one-unit-out and leave-
> one-group-out.
> In applied problems we have performed a mix, holding out some individual
> observations and some groups and then evaluating predictions at both levels (Price et al., 1996).

### 日本語訳（自動翻訳）

> バリアントと階層モデルの近似, 休暇1ユニットアウトと休暇を含む-
> 1グループアウト。
> 加えられた問題で私達は混合し、ある個人を握りました
> 観察といくつかのグループと、両方のレベルの予測の評価 (価格 et al., 1996).

### 熟語・専門語

- **prediction**: 予測。未知/将来/除外データに対する分布や点推定。

### 要約

- バリアントと階層モデルの近似, 休暇1ユニットアウトと休暇を含む- 1グループアウト。

## Chunk 0349

### English（抽出4行）

> Unfortunately, approximating such cross validation procedures using importance sampling tends
> to be much harder than in the leave-one-out case. This is because more observations are left out at
> a time which implies stronger changes in the posterior distributions from the full to the subsetted
> model. As a result, we may have to rely on more costly model reﬁts to obtain leave-one-unit-out

### 日本語訳（自動翻訳）

> 残念ながら、重要なサンプリング傾向を使用して、このようなクロス検証手順を近似
> 残留ケースよりもはるかに難しくなります。 これは、より多くの観察が残っているためです
> 全体からサブセットまでのポスター分布のより強い変化を意味する時間
> モデル。 その結果、残留ユニットアウトを取得するため、より高価なモデル refits に依存する必要があるかもしれません

### 熟語・専門語

- **cross validation**: 交差検証。汎化性能を推定するためにデータを分割/近似除外する評価法。
- **leave-one-out**: LOO。一点ずつ除外した予測評価を効率的に近似する交差検証。
- **posterior distribution**: 事後分布。データ観測後の未知量の不確実性を表す分布。
- **validation**: 検証。モデルが目的・データ・外部知識に照らして妥当かを確認すること。

### 要約

- 残念ながら、重要なサンプリング傾向を使用して、このようなクロス検証手順を近似 残留ケースよりもはるかに難しくなります。

## Chunk 0350

### English（抽出4行）

> and leave-one-group-out cross validation results.
> 6.3.
> Influence of prior information
> Complex models can be diﬃcult to understand, hence the need for exploratory model analysis

### 日本語訳（自動翻訳）

> そして、グループアウトのクロス検証結果を残します。
> 6.3。
> 事前情報の影響
> 複雑なモデルは理解し難いことができます。, したがって、実験モデル解析の必要性

### 熟語・専門語

- **cross validation**: 交差検証。汎化性能を推定するためにデータを分割/近似除外する評価法。
- **validation**: 検証。モデルが目的・データ・外部知識に照らして妥当かを確認すること。

### 要約

- そして、グループアウトのクロス検証結果を残します。

## Chunk 0351

### English（抽出4行）

> (Unwin et al., 2003, Wickham, 2006) and explainable AI (Chen et al., 2018, Gunning, 2017, Rudin,
> 2018), which complements methods for evaluating, comparing, and averaging models using a range
> of interrelated approaches, including cross validation, stacking, boosting, and Bayesian evaluation.
> In this section we discuss methods to understand how posterior inferences under a ﬁtted model

### 日本語訳（自動翻訳）

> (Unwin et al., 2003, Wickham, 2006) および説明可能な AI (Chen et al., 2018, Gunning, 2017, Rudin,
> 2018)、範囲を使用してモデルの評価、比較、および平均化のためのメソッドを補完する
> 相互検証、スタッキング、ブースト、ベイジアン評価などの関連アプローチ。
> このセクションでは、フィットモデルのポスターの推論を理解する方法について説明します

### 熟語・専門語

- **cross validation**: 交差検証。汎化性能を推定するためにデータを分割/近似除外する評価法。
- **validation**: 検証。モデルが目的・データ・外部知識に照らして妥当かを確認すること。

### 要約

- (Unwin et al., 2003, Wickham, 2006) および説明可能な AI (Chen et al., 2018, Gunning, 2017, Rudin, 2018)、範囲を使用してモデルの評価、比較、および平…

## Chunk 0352

### English（抽出4行）

> depend on the data and priors.
> A statistical model can be understood in two ways: generatively and inferentially. From the
> generative perspective, we want to understand how the parameters map to the data. We can perform
> prior predictive simulation to visualize possible data from the model (as in Figure 4). From the

### 日本語訳（自動翻訳）

> データおよび優先事項に依存します。
> 統計的モデルは、遺伝子的かつ本質的に2つの方法で理解することができます。 から
> 遺伝子の観点から、パラメータがデータにどのようにマップするかを把握したい。 演奏会
> モデル(図4)から可能なデータを視覚化するための事前予測シミュレーション。 から

### 熟語・専門語

- **prior predictive**: 事前予測。データを見る前のpriorだけで生成される予測分布を確認する診断。

### 要約

- データおよび優先事項に依存します。

## Chunk 0353

### English（抽出4行）

> inferential perspective, we want to understand the path from inputs (data and prior distributions) to
> outputs (estimates and uncertainties).
> The most direct way to understand the inﬂuence of priors is to run sensitivity analysis by reﬁtting
> Figure 18: Example of static sensitivity analysis from a statistical model ﬁt to a problem in

### 日本語訳（自動翻訳）

> 必須の観点から、インプット(データと事前の配布)からパスを理解したいと考えています。
> 出力(推定値と不確実性)。
> 事前の影響を理解するための最も直接的な方法は、感度分析を実行することです。
> 図18:統計モデルからの静的感度解析例は、問題に合致

### 熟語・専門語

- **prior distribution**: 事前分布。データ観測前の知識・制約を表す分布。

### 要約

- 必須の観点から、インプット(データと事前の配布)からパスを理解したいと考えています。

## Chunk 0354

### English（抽出4行）

> toxicology. Each graph shows posterior simulation draws of the percent metabolized under two
> conditions (hence the clusters of points at the top and bottom of each graph), plotted vs. two of
> the parameters in the model. The plots reveal little sensitivity to either parameter on inference for
> percent metabolized under one condition, but strong sensitivity for the other. This sort of graph

### 日本語訳（自動翻訳）

> 毒性学。 各グラフは2つの下で新陳代謝されるパーセントのポスターのシミュレーションの引くことを示します
> 条件(各グラフの上部と下部の点のクラスター)、プロットされた対2
> モデルのパラメータ。 プロットは、推論上の任意のパラメータに少し感度を明らかにします
> 1%は1つの条件の下で代謝しましたが、他のための強い感受性。 この種類のグラフ

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- 毒性学。

## Chunk 0355

### English（抽出4行）

> can be used to assess sensitivity to alternative prior distributions, without requiring the model to
> be re-ﬁt. From Gelman, Bois, and Jiang (1996).
> the model with multiple priors, this can however be prohibitively expensive if the models take a
> long time to ﬁt. However, there are some shortcuts.

### 日本語訳（自動翻訳）

> モデルを要求しないで、代替前分布に対する感度を評価するために使用することができます
> お問い合わせ ゲルマン、ボワ、ジャン(1996年)から。
> 複数の事前のモデルでは、モデルはモデルを取る場合、これはしかし、禁止的に高価になることができます
> 合うべき長い時間。 しかし、いくつかのショートカットがあります。

### 熟語・専門語

- **prior distribution**: 事前分布。データ観測前の知識・制約を表す分布。
- **ESS**: 有効サンプルサイズ。自己相関を考慮した独立サンプル相当数。

### 要約

- モデルを要求しないで、代替前分布に対する感度を評価するために使用することができます お問い合わせ ゲルマン、ボワ、ジャン(1996年)から。

## Chunk 0356

### English（抽出4行）

> One approach is to compute the shrinkage between prior and posterior, for example, by compar-
> ing prior to posterior standard deviations for each parameter or by comparing prior and posterior
> quantiles. If the data relative to the prior are informative for a particular parameter, shrinkage
> for that parameter should be stronger. This type of check has been extensively developed in the

### 日本語訳（自動翻訳）

> 1つのアプローチは、比較して、例えば、前後の収縮を計算することです。
> 各パラメータのポスター標準偏差、または前後の比較による
> 四角形。 前のデータが特定のパラメータに対して有益である場合、収縮
> そのパラメータがより強くなるはずです。 このタイプのチェックは広く開発されています

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- 1つのアプローチは、比較して、例えば、前後の収縮を計算することです。

## Chunk 0357

### English（抽出4行）

> literature; see, for example, Nott et al. (2020).
> Another approach is to use importance sampling to approximate the posterior of the new model
> using the posterior of old model, provided the two posteriors are similar enough for importance
> sampling to bridge (Vehtari et al., 2019, Paananen et al., 2020). And if they are not, this is also

### 日本語訳（自動翻訳）

> 文献; 参照してください。, 例えば, Nott ら. (2020).
> もう一つのアプローチは、新しいモデルのポスターを近似するために重要なサンプリングを使用することです
> 古いモデルのポスターを使用して、2つのポスターは重要のために十分類似しています
> 橋にサンプリング (Vehtari et al., 2019, Paananen et al., 2020). 彼らがそうでなければ、これはまた

### 熟語・専門語

- **approximate**: 近似。速度や扱いやすさのため、正確な推論・モデルを緩めること。

### 要約

- 文献; 参照してください。

## Chunk 0358

### English（抽出4行）

> valuable information in itself (see Section 6.2).
> Yet another approach is to perform static sensitivity analysis, which is a way to study sensitivity
> of posterior inferences to perturbations in the prior without requiring that the model be re-ﬁt using
> alternative prior distributions (Gelman, Bois, and Jiang, 1996; see Figure 18 for an example). Each

### 日本語訳（自動翻訳）

> 貴重な情報自体(セクション6を参照してください。)。
> しかし、別のアプローチは静的感度分析を実行することです。これは感度を研究する方法です
> モデルは、モデルが再フィットすることを要求することなく、以前のモデルの劣化に劣らない
> 代替プレディストリビューション(Gelman, Bois, and Jiang, 1996; 図 18 の例). 詳しくはこちら

### 熟語・専門語

- **prior distribution**: 事前分布。データ観測前の知識・制約を表す分布。

### 要約

- 貴重な情報自体(セクション6を参照してください。

## Chunk 0359

### English（抽出4行）

> graph in Figure 18 shows posterior simulations revealing the posterior dependence of a quantity of
> interest (in this example, the percentage of a toxin that is metabolized by the body) as a function of
> a parameter in the model.
> Consider Figure 18 as four scatterplots, as each of the two graphs is really two plots super-

### 日本語訳（自動翻訳）

> 図18のグラフは、数のポスター依存を明らかにするポスターシミュレーションを示しています
> 関心(この例では、体によって代謝される毒素の割合)の関数として
> モデルのパラメータ。
> 2つのグラフのそれぞれが本当に2つのプロットであるので、図18を4つのスキャッタプロットとして考慮して下さい

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- 図18のグラフは、数のポスター依存を明らかにするポスターシミュレーションを示しています 関心(この例では、体によって代謝される毒素の割合)の関数として モデルのパラメータ。

## Chunk 0360

### English（抽出4行）

> imposed, one for a condition of low exposure to the toxin and one for high exposure. Each of
> these four plots can be interpreted in two ways. First, the direct interpretation shows the posterior
> correlation between the predictive quantity of interest (the percentage metabolized in the body)
> and a particular parameter (for example, the scaling coeﬃcient of the toxin’s metabolism). Second,

### 日本語訳（自動翻訳）

> 課せられた、毒素および高い露出のための1つの低い露出の状態のための1。 それぞれ
> これらの4つのプロットは2つの方法で解釈することができます。 まず、直接通訳はポスターを示しています
> 利益の予測量の相関(体内で代謝される割合)
> そして特定の変数(例えば、毒素の新陳代謝のスケーリング係数)。 第2、

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- 課せられた、毒素および高い露出のための1つの低い露出の状態のための1。

## Chunk 0361

### English（抽出4行）

> each scatterplot can be read indirectly to reveal sensitivity of the quantity plotted on the y-axis to
> the prior of the parameter plotted on the x-axis. The interpretation goes as follows: a change in the
> prior distribution for the parameter plotted on the x-axis can be performed by reweighting of the
> points on the graph according to the ratio of the new prior to that used in the analysis. With these

### 日本語訳（自動翻訳）

> 各スキャッタープロットは、y軸上にプロットされた数量の感度を間接的に表示することができます
> x 軸上にプロットされたパラメータの優先値。 次のように解釈が進みます。
> x 軸上にプロットされたパラメータの事前の分布は、リ重量で実行できます
> グラフ上の点は、分析で使用される新しい比率に応じて示します。 これらの

### 熟語・専門語

- **prior distribution**: 事前分布。データ観測前の知識・制約を表す分布。

### 要約

- 各スキャッタープロットは、y軸上にプロットされた数量の感度を間接的に表示することができます x 軸上にプロットされたパラメータの優先値。

## Chunk 0362

### English（抽出4行）

> graphs, the importance weighing can be visualized implicitly: the impact of changes in the prior
> distribution can be seen based on the dependence in the scatterplot.
> The mapping of prior and data to posterior can also be studied more formally, as discussed in
> Section 6.2.

### 日本語訳（自動翻訳）

> グラフ、計量の重要性は暗黙的に視覚化することができます:前の変化の影響
> スキャッタープロットの依存に基づいて分布を見ることができます。
> ポスターへの事前とデータのマッピングは、議論のように、より形式的に学習することができます
> セクション6.2。

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- グラフ、計量の重要性は暗黙的に視覚化することができます:前の変化の影響 スキャッタープロットの依存に基づいて分布を見ることができます。

## Chunk 0363

### English（抽出4行）

> 6.4.
> Summarizing inference and propagating uncertainty
> Bayesian inference is well suited for problems with latent variables and other settings with unresolv-
> able uncertainty. In addition, we often use hierarchical models that include batches of parameters

### 日本語訳（自動翻訳）

> 6.4. 6.4.
> 浸透と不確実性を損なう
> ベイジアン・インフェレンスは、レイトント変数やその他の設定の未解決の問題に適しています。
> 不確実性を実現 また、パラメータのバッチを含む階層モデルを使用することが多い

### 熟語・専門語

- **Bayesian inference**: ベイズ推論。事前分布と尤度から事後分布を計算する中核処理。
- **uncertainty**: 不確実性。観測・パラメータ・モデル構造・意思決定に残る曖昧さ。

### 要約

- 6.4. 6.4. 浸透と不確実性を損なう ベイジアン・インフェレンスは、レイトント変数やその他の設定の未解決の問題に適しています。

## Chunk 0364

### English（抽出4行）

> representing variation.
> For example, when reporting the results from our election forecasting
> model, we are interested in uncertainty in the forecast votes and also variation among states.
> Unfortunately, the usual ways of displaying Bayesian inference do not fully capture the multiple

### 日本語訳（自動翻訳）

> バリエーションを表す。
> たとえば、選挙予測から結果を報告するとき
> モデル、予測票の不確実性、また州間の変動に興味があります。
> 残念ながら、ベイジアン・インフェレンスを表示する通常の方法は、複数のものを完全にキャプチャしません

### 熟語・専門語

- **Bayesian inference**: ベイズ推論。事前分布と尤度から事後分布を計算する中核処理。
- **uncertainty**: 不確実性。観測・パラメータ・モデル構造・意思決定に残る曖昧さ。

### 要約

- バリエーションを表す。

## Chunk 0365

### English（抽出4行）

> levels of variation and uncertainty in our inferences.
> A table or even a graph of parameter
> estimates, uncertainties, and standard errors is only showing one-dimensional margins, while
> graphs of marginal posterior distributions are unwieldy for models with many parameters and also

### 日本語訳（自動翻訳）

> 私たちの推論の変動と不確実性のレベル。
> パラメータの表またはグラフ
> 推定値、不確実性、標準誤差は1次元マージンのみ表示しますが、
> 余白のポスター分布のグラフは、多くのパラメータを持つモデルとまた、

### 熟語・専門語

- **posterior distribution**: 事後分布。データ観測後の未知量の不確実性を表す分布。
- **uncertainty**: 不確実性。観測・パラメータ・モデル構造・意思決定に残る曖昧さ。

### 要約

- 私たちの推論の変動と不確実性のレベル。

## Chunk 0366

### English（抽出4行）

> fail to capture the interplay between uncertainty and variation in a hierarchical model.
> To start with, we should follow general principles of good statistical practice and graph data and
> ﬁtted models, both for the “exploratory data analysis” purpose of uncovering unexpected patterns
> in the data and also more directly to understand how the model relates to the data used to ﬁt it.

### 日本語訳（自動翻訳）

> 階層モデルの不確実性とバリエーションのインタープレイをキャプチャできません。
> まずは、良い統計的な練習とグラフデータやグラフデータの一般的な原則に従う必要があります。
> 予期しないパターンを明らかにする「探索的データ解析」の目的で、適合モデル
> データを直接理解して、モデルがそのデータにどのように関連したかを理解します。

### 熟語・専門語

- **uncertainty**: 不確実性。観測・パラメータ・モデル構造・意思決定に残る曖昧さ。

### 要約

- 階層モデルの不確実性とバリエーションのインタープレイをキャプチャできません。

## Chunk 0367

### English（抽出4行）

> We illustrate some uses of graphical model exploration and summary from an analysis by Ghitza
> and Gelman (2020) of vote preferences in the 2016 U.S. presidential election. Figure 19 shows
> the estimated gender gap in support for the two candidates, ﬁrst displayed as a map and then as
> a scatterplot. The map, which is the natural ﬁrst step to visualizing these estimates, reveals some

### 日本語訳（自動翻訳）

> Ghitzaによる分析からグラフィカルなモデル探索と要約のいくつかの用途を説明します
> そしてゲルマン(2020年)は、2016年米国大統領選挙で投票の好みを好みます。 図19 ショー
> 2つの候補のサポートで推定された性別ギャップは、まずマップとして表示され、
> スキャッタープロット。 これらの見積もりを視覚化するための自然な第一歩である地図は、いくつかを明らかにします

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- Ghitzaによる分析からグラフィカルなモデル探索と要約のいくつかの用途を説明します そしてゲルマン(2020年)は、2016年米国大統領選挙で投票の好みを好みます。

## Chunk 0368

### English（抽出4行）

> intriguing geographic patterns which are then explored in a more focused way in the scatterplot.
> Figure 20 evaluates the model by comparing to simpler county-level estimates. This example
> demonstrates a general workﬂow in exploratory graphics, in which the results from inferential
> summary motivates future exploration.

### 日本語訳（自動翻訳）

> その後、スキャッタープロットのより焦点を絞った方法で探索される地理的なパターンを調べます。
> 図20は、単純郡レベルの推定と比較することでモデルを評価します。 この例
> 実験的なグラフィックスで一般的なワークフローを実証します。
> 要約は将来の探査を動機づけます。

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- その後、スキャッタープロットのより焦点を絞った方法で探索される地理的なパターンを調べます。

## Chunk 0369

### English（抽出4行）

> Gabry et al. (2019) present some of our ideas on graphics for Bayesian workﬂow, and some of
> this has been implemented in the R package bayesplot (Gabry et al., 2020b, see also Kay, 2020ab,
> Kumar, 2019). Probabilistic programming ultimately has the potential to allow random variables
> to manipulated like any other data objects, with uncertainty implicit in all the plots and calculations

### 日本語訳（自動翻訳）

> Gabry et al. (2019) ベイジアンワークフローのグラフィックにいくつかのアイデアを提示します。
> Rパッケージベイスプロット(Gabry et al., 2020b, Kay, 2020ab,
> 2019年4月1日 プロバシリスティックプログラミングは、最終的にランダム変数を許可する可能性がある
> すべてのプロットおよび計算の不確実性衝動と他のデータ オブジェクトのように操作するため

### 熟語・専門語

- **probabilistic programming**: 確率的プログラミング。Stanなどで確率モデルをコードとして記述し推論する方法。
- **uncertainty**: 不確実性。観測・パラメータ・モデル構造・意思決定に残る曖昧さ。

### 要約

- Gabry et al. (2019) ベイジアンワークフローのグラフィックにいくつかのアイデアを提示します。

## Chunk 0370

### English（抽出4行）

> (Kerman and Gelman, 2004, 2007), but much more work needs to be done to turn this possibility
> into reality, going beyond point and interval estimation so that we can make full use of the models
> we ﬁt.
> 7.

### 日本語訳（自動翻訳）

> (ケルマンとゲルマン、2004年、2007年)、しかし、この可能性をオンにするために多くの作業を行う必要があります
> 実際のところ、ポイントとインターバルの推定を超えて行くと、モデルのフル活用ができます
> お問い合わせ
> 7。

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- (ケルマンとゲルマン、2004年、2007年)、しかし、この可能性をオンにするために多くの作業を行う必要があります 実際のところ、ポイントとインターバルの推定を超えて行くと、モデルのフル活用ができます お問い合わせ 7。

## Chunk 0371

### English（抽出4行）

> Modifying a model
> Model building is a language-like task in which the modeler puts together existing components
> (linear, logistic, and exponential functions; additive and multiplicative models; binomial, Poisson,
> and normal distributions; varying coeﬃcients; and so forth) in order to encompass new data

### 日本語訳（自動翻訳）

> モデルの変更
> モデルビルは、モデラーが既存のコンポーネントを組み合わせる言語のようなタスクです
> (線形、記号論理学および指数関数; 添加物および多重性モデル; binomial、Poisson、
> そして正常な配分;異なった係数;等)新しいデータを包含するために

### 熟語・専門語

- **model building**: モデル構築。仮定・データ構造・prior・likelihoodを組み合わせる工程。

### 要約

- モデルの変更 モデルビルは、モデラーが既存のコンポーネントを組み合わせる言語のようなタスクです (線形、記号論理学および指数関数; 添加物および多重性モデル; binomial、Poisson、 そして正常な配分;異なった係数;等)新…

## Chunk 0372

### English（抽出4行）

> and additional features of existing data, along with links to underlying processes of interest.
> As mentioned in Section 2.2, most parts of the models can be seen as placeholders that allow
> Figure 19: From a model ﬁt to survey data during the 2016 U.S. presidential election campaign:
> (a) estimate of the gender gap among white voters, (b) estimated gender gap plotted vs. Obama’s

### 日本語訳（自動翻訳）

> 既存のデータの追加機能と、興味の根本的なプロセスへのリンク。
> セクション2.2で述べたように、モデルの大部分は、許可するプレースホルダとして見ることができる
> 図19:2016年米国大統領選挙キャンペーンでモデルフィットから調査データまで:
> (a)白い投票者の間で性別ギャップの推定、(b)推定性別ギャップのプロット対。 オバマの

### 熟語・専門語

- **ESS**: 有効サンプルサイズ。自己相関を考慮した独立サンプル相当数。

### 要約

- 既存のデータの追加機能と、興味の根本的なプロセスへのリンク。

## Chunk 0373

### English（抽出4行）

> estimated county-level vote share in 2012 among white votes. The area of each circle is proportional
> to the number of voters in the county, and the colors on the map represent a range going from
> dark purple (no diﬀerence in voting patterns comparing white men and white women) through
> light gray (white women supporting Clinton 7.5 percentage points more than white men) to dark

### 日本語訳（自動翻訳）

> 2012年に白書の中で推定された郡レベルの投票の共有。 各円の面積は比例しています
> 郡内の投票者の数に、地図上の色はから行く範囲を表します
> ダークパープル(白人男性と白人女性を比較する投票パターンの違いはありません)
> 光グレー(クリントン7.5パーセンテージをサポートする白い女性は、白人男性よりもポイント)ダーク

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- 2012年に白書の中で推定された郡レベルの投票の共有。

## Chunk 0374

### English（抽出4行）

> green (a white gender gap of 15 percentage points). The striking geographic patterns—a white
> gender gap that is low in much of the south and high in the west and much of the northeast and
> midwest—motivates the scatterplot, which reveals that the white gender gap tends to be highest in
> counties where the white vote is close to evenly split. From Ghitza and Gelman (2020).

### 日本語訳（自動翻訳）

> 緑色(15パーセントポイントの白い男女差)。 印象的な地理的パターン - 白
> 北東の西と南西の南と高の多くが低く、男女差が少なく、
> 中西部—スキャッタープロットをモチベートし、白い男女のギャップが最も高い傾向があることを明らかに
> 白い投票が均等に分割されるとカウントされます。 GhitzaとGelman(2020年)から。

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- 緑色(15パーセントポイントの白い男女差)。

## Chunk 0375

### English（抽出4行）

> Figure 20: Evaluation of one aspect of the model shown in Figure 19, comparing county-level
> support for Clinton as estimated from two diﬀerent models. We include this here to illustrate the
> way that graphical methods can be used to summarize, understand, evaluate, and compare ﬁtted
> models. From Ghitza and Gelman (2020).

### 日本語訳（自動翻訳）

> 図20: 図19に示すモデルの1つの側面の評価、比較郡レベル
> 2つの異なるモデルから推定されるClintonのサポート。 ここには、ここに示します
> グラフィカルな方法を使用して、適合した比較をまとめ、理解、評価、比較することができます
> モデル。 GhitzaとGelman(2020年)から。

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- 図20: 図19に示すモデルの1つの側面の評価、比較郡レベル 2つの異なるモデルから推定されるClintonのサポート。

## Chunk 0376

### English（抽出4行）

> replacement or expansion. Alternatively we may ﬁnd the need to use an approximate model or an
> approximate algorithm, as discussed in Section 3.3.
> Model expansion can come in response to new data, failures of models ﬁt to existing data,
> or computational struggles with existing ﬁtting procedures. For the election forecast described in

### 日本語訳（自動翻訳）

> 取り替えか拡張。 また、近似モデルや、
> セクション3.3で議論されるように、近似アルゴリズム。
> モデルの拡張は、新しいデータ、モデルの失敗が既存のデータに収まるように応答できます、
> または既存のフィッティング手順と計算の闘争. 選挙の予想について

### 熟語・専門語

- **approximate**: 近似。速度や扱いやすさのため、正確な推論・モデルを緩めること。

### 要約

- 取り替えか拡張。

## Chunk 0377

### English（抽出4行）

> Gelman, Hullman, et al. (2020), we started with the poll-aggregation model of Linzer (2013) which
> we had adapted in 2016 but with a notable failure of predictions in certain swing states, which we
> attributed to poor modeling of correlations of vote swings between states, along with nonsampling
> errors in the polls (Gelman and Azari, 2017). In our revision we expanded the model to include

### 日本語訳（自動翻訳）

> ゲルマン、ハルマン、et al。 (2020)、私達はLinzer (2013)のpoll-aggregationモデルから始まりました
> 私たちは2016年に適応しましたが、特定のスイング状態における予測の著しい失敗で、
> 州間の投票スイングの相関の悪いモデリングに起因し、ノンサンプリング
> 投票のエラー(2017年)。 リビジョンではモデルを拡大し、

### 熟語・専門語

- **prediction**: 予測。未知/将来/除外データに対する分布や点推定。

### 要約

- ゲルマン、ハルマン、et al。

## Chunk 0378

### English（抽出4行）

> both these features. Sections 10 and 11 give extended examples of iterative model building and
> evaluation.
> 7.1.
> Constructing a model for the data

### 日本語訳（自動翻訳）

> これらの機能の両方。 セクション10および11は反復的なモデル建物の延長例を与えます
> 評価。
> 7.1. .
> データのモデルの構築

### 熟語・専門語

- **model building**: モデル構築。仮定・データ構造・prior・likelihoodを組み合わせる工程。

### 要約

- これらの機能の両方。

## Chunk 0379

### English（抽出4行）

> In textbook treatments of statistics, the distribution of data given parameters is typically just given.
> In applications, though, we want to set up a data model based on some combination of ﬁt to the
> data (as found in posterior predictive checks) and domain expertise. If the model is being chosen
> from a small menu, we would like to at least be open about that. Often the most important aspect of

### 日本語訳（自動翻訳）

> 統計の教科書処理では、指定されたパラメータのデータの分布が典型的に与えられています。
> アプリケーションでは、しかしながら、フィットのいくつかの組み合わせに基づいてデータモデルを設定したい
> データ(ポスター予測チェックで見つかった)とドメインの専門知識。 モデルが選択されている場合
> 小さなメニューから、その内容について少なくとも開いてほしい。 最も重要な側面をしばしば

### 熟語・専門語

- **posterior predictive**: 事後予測。推定後のモデルが観測データの特徴を再現できるかを見る診断。

### 要約

- 統計の教科書処理では、指定されたパラメータのデータの分布が典型的に与えられています。

## Chunk 0380

### English（抽出4行）

> the data model is not its distributional form but how the data are linked to underlying parameters of
> interest. For example, in election forecasting, our model for polls includes terms for nonsampling
> error for individual polls and for polling averages, following Shirani-Mehr et al. (2018).
> A related challenge arises because data are typically preprocessed before they come to us, so that

### 日本語訳（自動翻訳）

> データモデルは、その分布形態ではなく、データが下位パラメータにリンクする方法ではありません
> お問い合わせ たとえば、選挙予測では、投票のモデルにはノンサンプリングの用語が含まれています
> 個々の小胞の誤差と平均値のポーリングについては、白ニ・メール ら(2018).
> データは通常、当社に来る前に処理されるため、関連する課題が生じる

### 熟語・専門語

- **ESS**: 有効サンプルサイズ。自己相関を考慮した独立サンプル相当数。

### 要約

- データモデルは、その分布形態ではなく、データが下位パラメータにリンクする方法ではありません お問い合わせ たとえば、選挙予測では、投票のモデルにはノンサンプリングの用語が含まれています 個々の小胞の誤差と平均値のポーリングについては、…

## Chunk 0381

### English（抽出4行）

> any generative model is necessarily an approximation. This can arise in meta-analysis or in settings
> where some large set of predictors have been combined into one or two numerical summaries using
> a machine learning algorithm or another dimensionality reduction technique. As always, we need
> to be concerned about data quality, and the most important aspect of the data model can be bias

### 日本語訳（自動翻訳）

> ジェネレーションモデルは必ずしも近似です。 これはメタ分析や設定で発生する可能性があります
> 予測者の大きなセットが1つまたは2つの数値の合計に組み込まれているところ
> 機械学習のアルゴリズムか別の次元の減少の技術。 いつものように、私達は必要とします
> データ品質を懸念し、データモデルの最も重要な側面はバイアスできます

### 熟語・専門語

- **generative model**: 生成モデル。データ生成過程を確率的に記述するモデル。
- **ESS**: 有効サンプルサイズ。自己相関を考慮した独立サンプル相当数。

### 要約

- ジェネレーションモデルは必ずしも近似です。

## Chunk 0382

### English（抽出4行）

> rather than what would traditionally be considered measurement error. Understanding this aﬀects
> Bayesian workﬂow in that it can make sense to expand a model to allow for systematic error; we
> give an example in Section 10.5.
> 7.2.

### 日本語訳（自動翻訳）

> 従来の測定エラーと見なされるよりもむしろ。 この影響を理解する
> ベイジアンワークフローは、体系的なエラーを可能にするモデルを拡大する意味を生むことができます。
> セクション10.5で例を示します。
> 7.2. .

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- 従来の測定エラーと見なされるよりもむしろ。

## Chunk 0383

### English（抽出4行）

> Incorporating additional data
> It is sometimes said that the most important aspect of a statistical method is not what it does with
> the data, but what data are used. A key part of Bayesian workﬂow is expanding a model to make use
> of more data. This can be as simple as adding regression predictors—but when more parameters

### 日本語訳（自動翻訳）

> 追加データを組み込む
> 統計的方法の最も重要な側面は、それが何をしているのかではないと時々言われています
> データ、しかし、どのようなデータが使用されるか。 ベイジアンワークフローの重要な部分は、使用するモデルを拡大しています
> より多くのデータ。 これは、回帰予測者を追加するのと同じくらい簡単ですが、より多くのパラメータがある場合

### 熟語・専門語

- **ESS**: 有効サンプルサイズ。自己相関を考慮した独立サンプル相当数。

### 要約

- 追加データを組み込む 統計的方法の最も重要な側面は、それが何をしているのかではないと時々言われています データ、しかし、どのようなデータが使用されるか。

## Chunk 0384

### English（抽出4行）

> are added, it can be necessary to assume that not all of them can have a big eﬀect in the model at
> the same time. One way to see this is to consider the addition of a parameter as a relaxation of a
> prior distribution that was previously concentrated at zero. For example, we expanded our election
> model to account for political polarization by adding interaction terms to the regression, allowing

### 日本語訳（自動翻訳）

> 加えて、それらのすべてがモデルに大きな効果をもたらすことができないと仮定する必要があります
> 同じ時間。 これを見るための1つの方法は、パラメーターのリラクゼーションとして考慮することです
> 以前にゼロに集中していた事前の配布。 例えば、選挙を拡大しました。
> 回帰に相互作用条件を追加することにより、政治的偏光のために考慮するモデル, 可能

### 熟語・専門語

- **prior distribution**: 事前分布。データ観測前の知識・制約を表す分布。
- **ESS**: 有効サンプルサイズ。自己相関を考慮した独立サンプル相当数。

### 要約

- 加えて、それらのすべてがモデルに大きな効果をもたらすことができないと仮定する必要があります 同じ時間。

## Chunk 0385

### English（抽出4行）

> the coeﬃcients for the national economic predictor to be lower in recent years.
> It sometimes happens that we have two forms of measurement of similar data, thus requiring a
> generative model for both data sources. Sometimes this creates technical challenges, as when we
> are combining direct measurements on a sample with population summary statistics, or integrating

### 日本語訳（自動翻訳）

> 近年、国の経済予測係数が低下する。
> 同様のデータの測定の2つの形態があることが時々起こります。
> 両方のデータソースのジェネレーションモデル。 時折、これは技術的な課題を生み出します。
> 集団概要の統計と標本の直接測定を結合するか、または統合します

### 熟語・専門語

- **generative model**: 生成モデル。データ生成過程を確率的に記述するモデル。

### 要約

- 近年、国の経済予測係数が低下する。

## Chunk 0386

### English（抽出4行）

> measurements of diﬀerent quality (for example, Lin et al., 1999), or when information is available
> on partial margins of a table (Deming and Stephan, 1940).
> In Weber et al. (2018), we ﬁt a
> pharmacological model with direct data for a set of patients taking one drug but only average data

### 日本語訳（自動翻訳）

> 異なる品質の測定(例えば、Lin et al.、1999)、または情報が利用可能な場合
> テーブルの部分的なマージン(デミングとステファン、1940)。
> Weber et al. (2018) では、
> 1つの薬を服用する患者のセットのための直接データが付いている薬理学モデルしかし平均データだけ

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- 異なる品質の測定(例えば、Lin et al.、1999)、または情報が利用可能な場合 テーブルの部分的なマージン(デミングとステファン、1940)。

## Chunk 0387

### English（抽出4行）

> for a set of patients that had received a competitor’s product. In order to avoid the computational
> cost of modeling as latent data the outcomes of all the averaged patients, we devised an analytic
> method to approximate the relevant integral so that we could include the averaged data in the
> likelihood function.

### 日本語訳（自動翻訳）

> 競合他社製品を受け取った患者の1組用。 計算を避けるため
> すべての平均的な患者の結果が潜在的データとしてモデル化するコスト、私たちは分析を考案しました
> 関連するインテグレーションを近づけるためのメソッドで、平均的なデータを含めることができます。
> 可能性機能。

### 熟語・専門語

- **likelihood**: 尤度。パラメータが与えられたときデータがどれだけ起こりやすいか。
- **approximate**: 近似。速度や扱いやすさのため、正確な推論・モデルを緩めること。

### 要約

- 競合他社製品を受け取った患者の1組用。

## Chunk 0388

### English（抽出4行）

> 7.3.
> Working with prior distributions
> Traditionally in Bayesian statistics we speak of noninformative or fully informative priors, but
> neither of these generally exist: a uniform prior contains some information, as it depends on the

### 日本語訳（自動翻訳）

> 7.3. .
> 事前の配布作業
> 伝統的にベイジアンの統計では、非公式または完全非公式の事前を話すが、
> これらのどれも一般的に存在します: 制服は、いくつかの情報が含まれています, それは依存するので、

### 熟語・専門語

- **prior distribution**: 事前分布。データ観測前の知識・制約を表す分布。

### 要約

- 7.3. . 事前の配布作業 伝統的にベイジアンの統計では、非公式または完全非公式の事前を話すが、 これらのどれも一般的に存在します: 制服は、いくつかの情報が含まれています, それは依存するので、

## Chunk 0389

### English（抽出4行）

> parameterization of the model; a reference prior depends on an assumed asymptotic regime for
> collecting new, ﬁctional data (Berger et al., 2009); and even an informative prior rarely includes all
> available knowledge. Rather, we prefer to think of a ladder of possibilities: (improper) ﬂat prior;
> super-vague but proper prior; very weakly informative prior; generic weakly informative prior;

### 日本語訳（自動翻訳）

> モデルのパラメータ化; 参照先は、想定される非対称法に依存します
> 新規、フィクション・データ(Berger et al., 2009)を収集し、非公式な事前のすべてを含む
> よくある質問 むしろ、我々は可能性の梯子を考えることを好みます: (improper) 前にフラット;
> 超漠然としたが、適切な前; 非常に弱い有益な前; 一般的な弱く有益な前;

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- モデルのパラメータ化; 参照先は、想定される非対称法に依存します 新規、フィクション・データ(Berger et al., 2009)を収集し、非公式な事前のすべてを含む よくある質問 むしろ、我々は可能性の梯子を考えることを好みます…

## Chunk 0390

### English（抽出4行）

> speciﬁc informative prior. For example, our election model includes random walk terms to allow
> variation in opinion at the state and national level. Each of these random walks has a standard
> deviation parameter corresponding to the unexplained variation (on the logit scale) in one day.
> This innovation standard deviation could be given a uniform prior, a super-vague but proper prior

### 日本語訳（自動翻訳）

> 事前に特定の情報提供を行います。 例えば、当社の選挙モデルにはランダムなウォーク条件が含まれている
> 国家と国家レベルでの意見の変化。 これらのランダムウォークのそれぞれに標準
> 未説明のバリエーションに対応した偏差パラメータ(logitスケールの場合)を1日で指定します。
> このイノベーション標準の偏差は、超漠然とした、しかし、適切な前に均一に与えることができます

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- 事前に特定の情報提供を行います。

## Chunk 0391

### English（抽出4行）

> (for example, normal+(0, 1000), where we are using the notation normal+ to represent the normal
> distribution truncated to be positive), a weak prior (for example, normal+(0, 1) on the percentage
> scale, which would allow unrealistically large day-to-day changes on the order of 0.25 percentage
> points in the probability of support for a candidate, but would still keep the distribution away from

### 日本語訳（自動翻訳）

> (例:normal+(0,1000)、正規表現を正規表現に使っている
> 配分は肯定的であるためにtuncated)、率の低い(例えば、normal+(0、1)
> スケール、それは0.25パーセントの順序の非現実的な大昼間変化を可能にする
> 候補者のためのサポートの確率でポイント, しかし、まだから配布を維持します

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- (例:normal+(0,1000)、正規表現を正規表現に使っている 配分は肯定的であるためにtuncated)、率の低い(例えば、normal+(0、1) スケール、それは0.25パーセントの順序の非現実的な大昼間変化を可能にする …

## Chunk 0392

### English（抽出4行）

> extreme parameter values), or a more informative prior such as normal+(0, 0.1) which does not
> encapsulate all our prior knowledge but does softly constrain this parameter to within a reasonable
> range. Our point here is that in choosing a prior, one is also choosing the amount of subject-matter
> information to include in the analysis.

### 日本語訳（自動翻訳）

> 極端なパラメータ値)、または、normal+(0, 0.1) などのより有益な前例では、
> 以前のすべての知識をカプセル化しますが、このパラメータを適度に制約します。
> 範囲。 ここのポイントは、前のものを選ぶ際に、被写者数の量も選択されていることです。
> 分析に含める情報。

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- 極端なパラメータ値)、または、normal+(0, 0.1) などのより有益な前例では、 以前のすべての知識をカプセル化しますが、このパラメータを適度に制約します。

## Chunk 0393

### English（抽出4行）

> Another way to view a prior distribution, or a statistical model more generally, is as a constraint.
> For example, if we ﬁt a linear model plus a spline or Gaussian process, y = b0 +b1x+g(x)+error,
> where the nonlinear function g has bounded variation, then with a strong enough prior on the g, we
> are ﬁtting a curve that is close to linear. The prior distribution in this example could represent prior

### 日本語訳（自動翻訳）

> 事前の配布、またはより一般的に統計的なモデルを表示する別の方法は、制約としてあります。
> 例えば、線形モデルとスプラインまたはガウスのプロセスに合えば、y = b0 +b1x+g(x)+error、
> 非線形関数 g が変化に縛られたところ、そして g の前の十分に強いと、私達は
> リニアに近い曲線をフィッティングします。 この例の事前の配布は、前述を表します

### 熟語・専門語

- **prior distribution**: 事前分布。データ観測前の知識・制約を表す分布。
- **ESS**: 有効サンプルサイズ。自己相関を考慮した独立サンプル相当数。

### 要約

- 事前の配布、またはより一般的に統計的なモデルを表示する別の方法は、制約としてあります。

## Chunk 0394

### English（抽出4行）

> information, or it could just be considered as part of the model speciﬁcation, if there is a desire
> to ﬁt an approximately linear curve. Simpson et al. (2017) provide further discussion on using
> prior distributions to shrink towards simpler models. This also leads to the more general point that
> priors are just like any other part of a statistical model in which they can serve diﬀerent purposes.

### 日本語訳（自動翻訳）

> 情報、またはモデルの仕様の一部として考慮することができ、欲望がある場合
> リニアカーブに近づく。 Simpson et al. (2017)は、使用に関するさらなる議論を提供
> 単純モデルに縮小する前の分布。 これはまたより多くの一般的なポイントにつながる
> 前者は、異なる目的のために役立つことができる統計モデルの他の部分と同様に、します。

### 熟語・専門語

- **prior distribution**: 事前分布。データ観測前の知識・制約を表す分布。
- **approximate**: 近似。速度や扱いやすさのため、正確な推論・モデルを緩めること。

### 要約

- 情報、またはモデルの仕様の一部として考慮することができ、欲望がある場合 リニアカーブに近づく。

## Chunk 0395

### English（抽出4行）

> Any clear distinction between model and prior is largely arbitrary and often depends mostly on the
> conceptual background of the one making the distinction.
> The amount of prior information needed to get reasonable inference depends strongly on the
> role of the parameter in the model as well as the depth of the parameter in the hierarchy (Goel and

### 日本語訳（自動翻訳）

> モデルと前の明確な区別は大抵任意であり、多くの場合ほとんどに依存します
> ひとつの概念的な背景は、差別化を図っています。
> 合理的な推論を得るために必要な事前情報量は、強くなります
> モデルのパラメータの役割と階層のパラメータの深さ(Goelと

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- モデルと前の明確な区別は大抵任意であり、多くの場合ほとんどに依存します ひとつの概念的な背景は、差別化を図っています。

## Chunk 0396

### English（抽出4行）

> DeGroot, 1981). For instance, parameters that mainly control central quantities (such as the mean
> or the median) typically tolerate vague priors more than scale parameters, which again are more
> forgiving of vague priors than parameters that control tail quantities, such as the shape parameter
> of a generalized extreme value distribution. When a model has a hierarchical structure, parameters

### 日本語訳（自動翻訳）

> DeGroot、1981年)。 例えば、中心量を主に制御する変数(平均のような)
> またはメディアン) 一般的には、スケールパラメータよりも前のvagueを許容します。
> 形状パラメータなど、尾の量を制御するパラメータよりも前のvagueの許す
> 一般化の極端な値分布。 モデルに階層構造がある場合、パラメータ

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- DeGroot、1981年)。

## Chunk 0397

### English（抽出4行）

> that are closer to the data are typically more willing to indulge vague priors than parameters further
> down the hierarchy.
> In Bayesian workﬂow, priors are needed for a sequence of models. Often as the model becomes
> more complex, all of the priors need to become tighter. The following simple example of multilevel

### 日本語訳（自動翻訳）

> データに近いのは、通常、パラメータよりも前の漠然とした漠然とした漠然とした意思です。
> 階層の下。
> ベイジアンワークフローでは、モデルのシーケンスには、事前に必要です。 モデルは、多くの場合、
> より複雑で、すべての優先順位がきつく必要があります。 マルチレベルの次の簡単な例

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- データに近いのは、通常、パラメータよりも前の漠然とした漠然とした漠然とした意思です。

## Chunk 0398

### English（抽出4行）

> data (see, for example, Raudenbush and Bryk, 2002) shows why this can be necessary.
> Consider a workﬂow where the data are yij, i = 1, . . . , nj, j = 1, . . . , J. Here i indexes the
> observation and j indexes the group. Imagine that for the ﬁrst model in the workﬂow we elect to
> ignore the group structure and use a simple normal distribution for the deviation from the mean.

### 日本語訳（自動翻訳）

> データ(Raudenbush、Bryk、2002など)は、これが必要な理由を示しています。
> データが yij, i = 1, . . . , nj, j = 1, . . . . . , J. ここで私はインデックス
> 観測とjはグループをインデックス化します。 私たちが選んだワークフローの最初のモデルについて
> グループ構造を無視し、平均からの偏差のための単純な通常の分布を使用します。

### 熟語・専門語

- **ESS**: 有効サンプルサイズ。自己相関を考慮した独立サンプル相当数。

### 要約

- データ(Raudenbush、Bryk、2002など)は、これが必要な理由を示しています。

## Chunk 0399

### English（抽出4行）

> In this case some of the information budget will be spent on estimating the overall mean and some
> of it is spent on the observation standard deviation. If we have a moderate amount of data, the
> mean will be approximately ¯y = Pn
> i=1 yi/n regardless of how weak the prior is. Furthermore,

### 日本語訳（自動翻訳）

> この場合、情報予算の一部は、全体的な平均といくつかの推定に費やされます
> 観察基準の偏差に費やされます。 適度な量のデータがある場合、
> つまり、およそ ̄y = Pn
> i=1 前の弱点に関係なく yi/n です。 さらに、

### 熟語・専門語

- **ESS**: 有効サンプルサイズ。自己相関を考慮した独立サンプル相当数。
- **approximate**: 近似。速度や扱いやすさのため、正確な推論・モデルを緩めること。

### 要約

- この場合、情報予算の一部は、全体的な平均といくつかの推定に費やされます 観察基準の偏差に費やされます。

## Chunk 0400

### English（抽出4行）

> the predictive distribution for a new observation will be approximately normal(¯y, s), where s is
> the sample standard deviation. Again, this will be true for most sensible priors on the observation
> standard deviation, regardless of how vague they are.
> If the next step in the workﬂow is to allow the mean to vary by group using a multilevel model,

### 日本語訳（自動翻訳）

> 新しい観察のための予測分布は、s がどこにあるか、ほぼ正規( ̄y, s)になります
> サンプル標準的な偏差。 繰り返しますが、これは観察の最も賢明な優先順位のために本当です
> 標準的な偏差、彼らがどのように漠然としているかに関係なく。
> ワークフローの次のステップは、マルチレベルモデルを使用してグループによって変化する手段を可能にすることです。

### 熟語・専門語

- **ESS**: 有効サンプルサイズ。自己相関を考慮した独立サンプル相当数。
- **approximate**: 近似。速度や扱いやすさのため、正確な推論・モデルを緩めること。

### 要約

- 新しい観察のための予測分布は、s がどこにあるか、ほぼ正規( ̄y, s)になります サンプル標準的な偏差。

## Chunk 0401

### English（抽出4行）

> then the information budget still needs to be divided between the standard deviation and the mean.
> However, the model now has J + 1 extra parameters (one for each group plus one for the standard
> deviation across groups) so the budget for the mean needs to be further divided to model the group
> means, whereas the budget for the standard deviation needs to be split between the within group

### 日本語訳（自動翻訳）

> その後、情報予算はまだ標準的な偏差と意味の間で分割する必要があります。
> しかし、このモデルはJ + 1の追加のパラメータ(各グループと標準のための1つ)を持っています
> グループ間での偏差) つまり、グループをモデル化するためにさらに分割する必要があります
> つまり、標準偏差の予算はグループ内間で分割する必要があります

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- その後、情報予算はまだ標準的な偏差と意味の間で分割する必要があります。

## Chunk 0402

### English（抽出4行）

> variation and the between group variation. But we still have the same amount of data, so we need
> to be careful to ensure that this model expansion does not destabilize our estimates. This means
> that as well as putting appropriate priors on our new parameters, we probably need to tighten up
> the priors on the overall mean and observation standard deviation, lest a lack of information lead to

### 日本語訳（自動翻訳）

> グループバリエーションとグループバリエーションの違い しかし、我々はまだ同じ量のデータを持っているので、我々は必要
> このモデルの拡張が当社の見積もりを損なわないことを確実にするために注意してください。 つまり、
> 新しいパラメータに適切な優先順位を付けるだけでなく、新しいパラメータを締める必要があります。
> 全体的な平均および観察標準的な偏差の優先順位は、情報の欠如を導きます

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- グループバリエーションとグループバリエーションの違い しかし、我々はまだ同じ量のデータを持っているので、我々は必要 このモデルの拡張が当社の見積もりを損なわないことを確実にするために注意してください。

## Chunk 0403

### English（抽出4行）

> nonsense estimates.
> A related issue is the concentration of measure in higher-dimensional space. For example in
> regression with an increasing number of predictors, the prior on the vector of coeﬃcients needs to
> have higher density near the mode if we want to keep most of the prior mass near the mode (as

### 日本語訳（自動翻訳）

> ナンセンス見積り
> 関連する問題は、高次元空間の測定の集中です。 例えば
> 増加する予測者数との回帰、係数のベクトルの前の要因は、
> モードの近くの前の固まりのほとんどを保ちたいと思うならモードの近くのより高い密度があります(として

### 熟語・専門語

- **ESS**: 有効サンプルサイズ。自己相関を考慮した独立サンプル相当数。

### 要約

- ナンセンス見積り 関連する問題は、高次元空間の測定の集中です。

## Chunk 0404

### English（抽出4行）

> the volume further away from the mode increases faster as dimension increases; see, for example,
> Piironen and Vehtari, 2017). Consider linear or logistic regression and what happens to the prior
> on R2 if the marginal prior on weights is ﬁxed. If we want the prior on R2 to stay ﬁxed, the
> prior on weights needs to get tighter. Figure 21 uses prior predictive checking (see Section 2.4) to

### 日本語訳（自動翻訳）

> モードから離れたボリュームは、次元が増加するにつれて増加します。 たとえば、
> ピロレンとヴェタリ、2017年 線形または記号論理的な回帰および前に起こることを考慮して下さい
> 重みが固定される前の余白がR2の場合。 R2 の事前の固定が必要な場合は、
> 体重の前にはよりきつく必要があります。 図21は、事前の予測チェック(セクション2.4参照)を使用して、

### 熟語・専門語

- **prior predictive**: 事前予測。データを見る前のpriorだけで生成される予測分布を確認する診断。
- **ESS**: 有効サンプルサイズ。自己相関を考慮した独立サンプル相当数。

### 要約

- モードから離れたボリュームは、次元が増加するにつれて増加します。

## Chunk 0405

### English（抽出4行）

> show how the usual weak prior on 26 weights in linear regression corresponds to a prior strongly
> favoring higher R2 values, aﬀecting also the posterior. From that perspective, weakly informative
> but independent priors may jointly be strongly informative if they appear in large numbers.
> Priors must be speciﬁed for each model within a workﬂow. An expanded model can require

### 日本語訳（自動翻訳）

> 線形回帰の26の重量の前の普通の弱さは前に強く対応する方法を示します
> より高いR2値を好む、ポスターにも影響を与えます。 その観点から弱く有益な情報
> しかし、独立した優先順位は、大量に表示されている場合、共同で強く有益な場合があります。
> ワークフロー内で各モデルに優先的に指定する必要があります。 拡大されたモデルは要求できます

### 熟語・専門語

- **ESS**: 有効サンプルサイズ。自己相関を考慮した独立サンプル相当数。

### 要約

- 線形回帰の26の重量の前の普通の弱さは前に強く対応する方法を示します より高いR2値を好む、ポスターにも影響を与えます。

## Chunk 0406

### English（抽出4行）

> additional thought regarding parameterization. For example, when going from normal(µ, σ) to
> a t-distribution tν(µ, σ) with ν degrees of freedom, we have to be careful with the prior on σ.
> The scale parameter σ looks the same for the two models, but the variance of the t distribution
> is actually

### 日本語訳（自動翻訳）

> パラメータ化に関する追加の考え。 例えば、normal(μ、σ)から
> t-distribution tν(μ, σ) と ν の自由度で、 σ の前に注意が必要です。
> スケールパラメータは2つのモデルと同じですが、t分布の分散
> 実際に

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- パラメータ化に関する追加の考え。

## Chunk 0407

### English（抽出4行）

> ν
> ν−2σ2 rather than σ2. Accordingly, if ν is small, σ is no longer close to the residual
> standard deviation.
> In general, we need to think in terms of the joint prior over all the parameters in a model,

### 日本語訳（自動翻訳）

> ツイート
> ν−2σ2ではなく2σ2。 したがって、 ν が小さい場合は、 σ は残留物に近接しません
> 標準偏差。
> 一般的には、モデル内のすべてのパラメータよりも前のジョイントの面で考える必要があります。

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- ツイート ν−2σ2ではなく2σ2。

## Chunk 0408

### English（抽出4行）

> to be assessed in the context of the generative model for the data, lest unfortunate cancellations
> or resonances lead to less stabilizing or more informative priors than the modeler actually wants
> (Gelman et al., 2017, Kennedy et al., 2019). As discussed in Section 2.4, prior predictive checking
> is a good general approach to exploring and understanding a prior distribution in the context of a

### 日本語訳（自動翻訳）

> データの生成モデルのコンテキストで評価されるためには、不幸なキャンセルを欠かせません。
> または共鳴は、モデラーが実際に望んでいるよりも安定化またはより有益な優先順位が少ないにつながる
> (Gelman et al., 2017, ケネディ et al., 2019). セクション2.4で議論したように、事前予測チェック
> コンテキスト内の事前分布を探索し理解するための良い一般的なアプローチです

### 熟語・専門語

- **prior predictive**: 事前予測。データを見る前のpriorだけで生成される予測分布を確認する診断。
- **prior distribution**: 事前分布。データ観測前の知識・制約を表す分布。
- **generative model**: 生成モデル。データ生成過程を確率的に記述するモデル。
- **ESS**: 有効サンプルサイズ。自己相関を考慮した独立サンプル相当数。

### 要約

- データの生成モデルのコンテキストで評価されるためには、不幸なキャンセルを欠かせません。

## Chunk 0409

### English（抽出4行）

> particular data model.
> The above examples carry particular messages about priors but also a meta-message about how
> we think about workﬂow when constructing statistical models. Phrases such as “the information
> budget still needs to be divided” represent important but somewhat informal decisions we make

### 日本語訳（自動翻訳）

> 特定のデータモデル。
> 上記の例では、優先事項について特定のメッセージを運ぶだけでなく、方法に関するメタメッセージ
> 統計モデル構築時のワークフローを考える。 「情報」などのフレーズ
> 予算は依然として分かれる必要があります" 重要ではなく、やや有益な決定を表す

### 熟語・専門語

- **ESS**: 有効サンプルサイズ。自己相関を考慮した独立サンプル相当数。
- **decision**: 意思決定。予測分布を損失・効用・行動選択へ接続する工程。

### 要約

- 特定のデータモデル。

## Chunk 0410

### English（抽出4行）

> Posterior
> Prior
> 0.25
> 0.5

### 日本語訳（自動翻訳）

> ポスター
> プライマー
> 0.25の
> 0.5パーセント

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- ポスター プライマー 0.25の 0.5パーセント

## Chunk 0411

### English（抽出4行）

> 0.75
> 0.25
> 0.5
> 0.75

### 日本語訳（自動翻訳）

> 0.75の
> 0.25の
> 0.5パーセント
> 0.75の

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- 0.75の 0.25の 0.5パーセント 0.75の

## Chunk 0412

### English（抽出4行）

> Bayesian R^2
> Posterior
> Prior
> 0.25

### 日本語訳（自動翻訳）

> ベイジアン R^2
> ポスター
> プライマー
> 0.25の

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- ベイジアン R^2 ポスター プライマー 0.25の

## Chunk 0413

### English（抽出4行）

> 0.5
> 0.75
> 0.25
> 0.5

### 日本語訳（自動翻訳）

> 0.5パーセント
> 0.75の
> 0.25の
> 0.5パーセント

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- 0.5パーセント 0.75の 0.25の 0.5パーセント

## Chunk 0414

### English（抽出4行）

> 0.75
> Bayesian R^2
> Posterior
> Prior

### 日本語訳（自動翻訳）

> 0.75の
> ベイジアン R^2
> ポスター
> プライマー

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- 0.75の ベイジアン R^2 ポスター プライマー

## Chunk 0415

### English（抽出4行）

> 0.25
> 0.5
> 0.75
> 0.25

### 日本語訳（自動翻訳）

> 0.25の
> 0.5パーセント
> 0.75の
> 0.25の

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- 0.25の 0.5パーセント 0.75の 0.25の

## Chunk 0416

### English（抽出4行）

> 0.5
> 0.75
> Bayesian R^2
> Figure 21: Prior and posterior distribution of Bayesian R2 for the regression predicting student

### 日本語訳（自動翻訳）

> 0.5パーセント
> 0.75の
> ベイジアン R^2
> 図21: 退会予測学生のためのベイジアンR2の事前およびポスター分布

### 熟語・専門語

- **posterior distribution**: 事後分布。データ観測後の未知量の不確実性を表す分布。
- **ESS**: 有効サンプルサイズ。自己相関を考慮した独立サンプル相当数。

### 要約

- 0.5パーセント 0.75の ベイジアン R^2 図21: 退会予測学生のためのベイジアンR2の事前およびポスター分布

## Chunk 0417

### English（抽出4行）

> grades from 26 predictors, using three diﬀerent priors for the coeﬃcients: (a) default weak prior,
> (b) normal prior scaled with the number of predictors, and (c) regularized horseshoe prior. From
> Section 12.7 of Gelman, Hill, and Vehtari (2020).
> about how much eﬀort we put in to include prior information. Such concerns are not always clear

### 日本語訳（自動翻訳）

> 26の予測者からの等級、係数の3つの異なる優先順位を使用して:(a)デフォルトは弱い前に、
> (b) 予測者数と、(c) 正規の前のスケールアップ。 詳しくはこちら
> セクション12.7 ゲルマン、ヒル、ヴェタリ(2020)。
> 事前情報を含めて、どのくらいの努力を払っております。 そのような懸念は常に明確ではありません

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- 26の予測者からの等級、係数の3つの異なる優先順位を使用して:(a)デフォルトは弱い前に、 (b) 予測者数と、(c) 正規の前のスケールアップ。

## Chunk 0418

### English（抽出4行）

> in articles or textbooks that present the ﬁnal model as is, without acknowledging the tradeoﬀs and
> choices that have been made.
> 7.4.
> A topology of models

### 日本語訳（自動翻訳）

> トレードオフを認めず、最終的なモデルをそのまま提示する記事や教科書
> 選ばれる
> 7.4. .
> モデルのトポロジー

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- トレードオフを認めず、最終的なモデルをそのまま提示する記事や教科書 選ばれる 7.4. . モデルのトポロジー

## Chunk 0419

### English（抽出4行）

> Consider a class of models, for simplicity in some particular restricted domain such as autoregressive
> moving average (ARMA) models, binary classiﬁcation trees, or linear regressions with some ﬁxed
> set of input variables. The models in any of these frameworks can be structured as a partial ordering:
> for example, AR(1) is simpler than AR(2) which is simpler than ARMA(2,1), and MA(1) is also

### 日本語訳（自動翻訳）

> オートレグレッシブなどの特定の制限されたドメインでモデルのクラスを考慮する
> 移動平均(ARMA)モデル、バイナリ分類ツリー、またはいくつかの固定で線形回帰
> 入力変数のセット。 これらのフレームワークのいずれかのモデルは、部分的な注文として構成することができます。
> 例えば、AR(1)はARMA(2,1)よりシンプルで、MA(1)も簡単です。

### 熟語・専門語

- **ESS**: 有効サンプルサイズ。自己相関を考慮した独立サンプル相当数。

### 要約

- オートレグレッシブなどの特定の制限されたドメインでモデルのクラスを考慮する 移動平均(ARMA)モデル、バイナリ分類ツリー、またはいくつかの固定で線形回帰 入力変数のセット。

## Chunk 0420

### English（抽出4行）

> simpler than ARMA(2,1), but AR(1) and MA(1) are not themselves ordered. Similarly, tree splits
> form a partial ordering, and the 2k possibilities of inclusion or exclusion in linear regression can be
> structured as the corners of a cube. As these examples illustrate, each of these model frameworks
> has its own topology or network structure as determined by the models in the class and their partial

### 日本語訳（自動翻訳）

> ARMA(2,1) よりもシンプルですが、AR(1) と MA(1) は注文されません。 同様に、ツリー分割
> 部分的な順序を形作り、線形回帰の包含か排除の2kの可能性はある場合もあります
> キューブの角として構造化。 これらの例は、これらのモデルのフレームワークのそれぞれを説明します。
> クラスと部分のモデルによって決定される独自のトポロジーまたはネットワーク構造を持っています

### 熟語・専門語

- **ESS**: 有効サンプルサイズ。自己相関を考慮した独立サンプル相当数。

### 要約

- ARMA(2,1) よりもシンプルですが、AR(1) と MA(1) は注文されません。

## Chunk 0421

### English（抽出4行）

> ordering.
> We speak of this as a topology of models rather than a probability space because we are not
> necessarily interested in assigning probabilities to the individual models. Our interest here is not
> in averaging over models but in navigating among them, and the topology refers to the connections

### 日本語訳（自動翻訳）

> 注文。
> 確率ではなくモデルのトポロジーとして話します。
> 必ずしも個々のモデルに確率を割り当てることに興味があります。 私たちの興味はここにありません
> モデルを上回るが、それらの中でナビゲートして、トポロジーは接続を参照する

### 熟語・専門語

- **ESS**: 有効サンプルサイズ。自己相関を考慮した独立サンプル相当数。

### 要約

- 注文。

## Chunk 0422

### English（抽出4行）

> between models and between parameters in neighboring models in the network.
> An example implementation of this idea is the Automatic Statistician (Hwang et al., 2016,
> Gharamani et al., 2019), which searches through models in speciﬁed but open-ended classes (for
> example, time series models and linear regression models), using inference and model criticism

### 日本語訳（自動翻訳）

> モデルとネットワークの隣接するモデルのパラメーター間。
> このアイデアの実装は、自動統計(Hwang et al.、2016、
> Gharamani et al., 2019), 指定されたが、オープンエンドクラス (for
> たとえば、インフェレンスとモデルの批判を使用して、時間シリーズモデルとリニア回帰モデル)

### 熟語・専門語

- **ESS**: 有効サンプルサイズ。自己相関を考慮した独立サンプル相当数。

### 要約

- モデルとネットワークの隣接するモデルのパラメーター間。

## Chunk 0423

### English（抽出4行）

> to explore the model and data space. We believe such algorithms can be better understood and,
> ultimately, improved, through a more formal understanding of the topology of models induced by
> a statistical modeling language. From another direction are menu-based packages such as Prophet
> (Taylor and Lethem, 2018) that allow users to put together models (in this case, for time series

### 日本語訳（自動翻訳）

> モデルとデータ空間を探索する。 そのようなアルゴリズムがよりよく理解でき、
> 最終的に改善され、モデルのトポロジーのより正式な理解を通じて、
> 統計的なモデリング言語。 別の方向から、Prophetなどのメニューベースのパッケージです。
> (Taylor and Lethem, 2018) ユーザーがモデルをまとめることを可能にする (この場合、時間シリーズの場合)

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- モデルとデータ空間を探索する。

## Chunk 0424

### English（抽出4行）

> forecasting) from some set of building blocks. It is important in such packages not just to be
> able to build and ﬁt these models but to understand each model in comparison to simpler or more
> complicated variants ﬁt to the same data.
> However, unlike combining variables, where in many cases a simple and often automated

### 日本語訳（自動翻訳）

> 建物ブロックの一部セットから予測)。 そのようなパッケージでは、それだけではありません
> これらのモデルを構築し、適合することができますが、よりシンプルに比較して各モデルを理解します
> 複雑なバリアントは同じデータに収まります。
> しかし、変数を組み合わせることとは異なり、多くの場合、シンプルで頻繁に自動化される

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- 建物ブロックの一部セットから予測)。

## Chunk 0425

### English（抽出4行）

> additive model is enough, here each model itself is a high dimensional object. The outputs from
> diﬀerent models, as probabilistic random variables, can be added, multiplied, linearly mixed, log-
> linearly-mixed, pointwisely-mixed, etc, which is within the choice of model topology we need to
> specify.

### 日本語訳（自動翻訳）

> 添加剤モデルは十分で、ここでは各モデル自体は高次元オブジェクトです。 出力から
> 確率的ランダム変数として、異なるモデルを追加することができます, 乗算, 線形混合, ログ-
> モデルトポロジの選択内にある線形混合、点心的に混合される、等、
> 指定する。

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- 添加剤モデルは十分で、ここでは各モデル自体は高次元オブジェクトです。

## Chunk 0426

### English（抽出4行）

> In addition, each model within a framework has its own internal structure involving parameters
> that can be estimated from data. And, importantly, the parameters within diﬀerent models in the
> network can “talk with each other” in the sense of having a shared, observable meaning outside
> the conﬁnes of the model itself. In machine learning and applied statistics, two familiar examples

### 日本語訳（自動翻訳）

> また、フレームワーク内の各モデルは、独自の内部構造の関与パラメータを持っています
> データから推定できます。 そして、重要なのは、さまざまなモデル内のパラメータ
> ネットワークは、外部に共有、観察可能な意味を持つという感覚で「互いに話せる」ことができます
> モデルそのものの混同。 機械学習と応用統計では、2つのよくある例

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- また、フレームワーク内の各モデルは、独自の内部構造の関与パラメータを持っています データから推定できます。

## Chunk 0427

### English（抽出4行）

> with inferential quantities that are shared across models are forecasting and causal inference. In
> forecasting, an increasingly complicated set of procedures can be used for a particular predictive
> goal. And in causal inference, a treatment eﬀect can be estimated using a series of regressions,
> starting from a simple diﬀerence and moving to elaborate interaction models adjusting for diﬀer-

### 日本語訳（自動翻訳）

> モデル全体で共有される必須の量は予測および原因の推論です。 インスタグラム
> 予測, ますます複雑な手順のセットは、特定の予測に使用することができます
> ゴール。 そして、原因の侵入では、処置の効果は一連の回帰を使用して推定することができます、
> 簡単な違いから始まり、異なるために調整する精巧な相互作用モデルに移動

### 熟語・専門語

- **ESS**: 有効サンプルサイズ。自己相関を考慮した独立サンプル相当数。

### 要約

- モデル全体で共有される必須の量は予測および原因の推論です。

## Chunk 0428

### English（抽出4行）

> ences between observed treated and control groups. Recall that causal inferences are a special case
> of predictions involving counterfactuals; see, for example, Morgan and Winship (2014).
> Thus, the topology of statistical or machine-learning models includes a partial ordering of
> models, and connections between parameters or functions of parameters and data across diﬀerent

### 日本語訳（自動翻訳）

> 観察された処理および管理グループ間のences。 原因の侵入が特別なケースであることを思い出させる
> 対向因子の予測; 参照, 例えば, モルガンと勝利 (2014).
> したがって、統計的または機械学習モデルのトポロジーには、部分的な順序が含まれています
> 異なるパラメータとデータの関数間のモデルと接続

### 熟語・専門語

- **prediction**: 予測。未知/将来/除外データに対する分布や点推定。

### 要約

- 観察された処理および管理グループ間のences。

## Chunk 0429

### English（抽出4行）

> models within the larger framework. Another twist is that prior distributions add a continuous
> dimension to the structure, bridging between models.
> 8.
> Understanding and comparing multiple models

### 日本語訳（自動翻訳）

> より大きいフレームワーク内のモデル。 もう1つのねじれは、事前の分配が連続して追加するということです
> モデル間の橋渡し、構造への次元。
> 8。
> 複数のモデルの理解と比較

### 熟語・専門語

- **prior distribution**: 事前分布。データ観測前の知識・制約を表す分布。

### 要約

- より大きいフレームワーク内のモデル。

## Chunk 0430

### English（抽出4行）

> 8.1.
> Visualizing models in relation to each other
> The key aspect of Bayesian workﬂow, which takes it beyond Bayesian data analysis, is that we
> are ﬁtting many models while working on a single problem. We are not talking here about model

### 日本語訳（自動翻訳）

> 8.1. 8.1.
> 互いに関係するモデルの見える化
> Bayesian のワークフローの重要な側面は、Bayesian のデータ分析を超えたことです。
> 単一の問題で働いている間多くのモデルを満たしています。 モデルについてはこちら

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- 8.1. 8.1. 互いに関係するモデルの見える化 Bayesian のワークフローの重要な側面は、Bayesian のデータ分析を超えたことです。

## Chunk 0431

### English（抽出4行）

> selection or model averaging but rather of the use of a series of ﬁtted models to better understand
> each one. In the words of Wickham, Cook, and Hofmann (2015), we seek to “explore the process
> of model ﬁtting, not just the end result.” We ﬁt multiple models for several reasons, including:
> • It can be hard to ﬁt and understand a big model, so we will build up to it from simple models.

### 日本語訳（自動翻訳）

> 選択またはモデル平均化ではなく、よりよく理解するために、一連のフィットモデルの使用
> それぞれ。 ウィッカム、クック、ホフマン(2015)の言葉で、「プロセスを探索する」
> 最終結果ではなくモデルフィッティング。 いくつかの理由で複数のモデルに合う:
> ・大きなモデルを装着し理解しにくいので、シンプルなモデルから構築します。

### 熟語・専門語

- **ESS**: 有効サンプルサイズ。自己相関を考慮した独立サンプル相当数。

### 要約

- 選択またはモデル平均化ではなく、よりよく理解するために、一連のフィットモデルの使用 それぞれ。

## Chunk 0432

### English（抽出4行）

> • When building our models, we make a lot of mistakes: typos, coding errors, conceptual
> errors (for example not realizing that the observations don’t contain useful information for
> some parts of the model), etc.
> • As we get more data, we typically expand our models accordingly. For example, if we’re doing

### 日本語訳（自動翻訳）

> • モデルを組み立てるとき、私達は間違いの多くを作ります:typos、コーディングの間違い、概念
> エラー(たとえば、観察には有用な情報が含まれていないことを認識しない
> モデルの部分など
> • より多くのデータを得るために、我々は通常、それに応じて私たちのモデルを拡大します。 例えば、

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- • モデルを組み立てるとき、私達は間違いの多くを作ります:typos、コーディングの間違い、概念 エラー(たとえば、観察には有用な情報が含まれていないことを認識しない モデルの部分など • より多くのデータを得るために、我々は通常、そ…

## Chunk 0433

### English（抽出4行）

> pharmacology and we get data on a new group of patients, we might let certain parameters
> vary by group.
> • Often we ﬁt a model that is mathematically well speciﬁed, but once we ﬁt it to data we realize
> that there’s more we can do, so we expand it.

### 日本語訳（自動翻訳）

> 薬理学および私達は患者の新しいグループにデータを得ます、私達はある特定の変数を許可するかもしれません
> グループごとに異なります。
> •多くの場合、我々は数学的に十分に指定されているモデルに収まりますが、私たちが実現するデータに収まると
> もっとできるので、拡大します。

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- 薬理学および私達は患者の新しいグループにデータを得ます、私達はある特定の変数を許可するかもしれません グループごとに異なります。

## Chunk 0434

### English（抽出4行）

> • Relatedly, when we ﬁrst ﬁt a model, we often put it together with various placeholders. We’re
> often starting with weak priors and making them stronger, or starting with strong priors and
> relaxing them.
> −2

### 日本語訳（自動翻訳）

> ・それに関連して、まずモデルに合うと、様々なプレースホルダーと組み合わせることがよくあります。 お問い合わせ
> 多くの場合、弱い優先順位で始まり、それらが強くなるか、または強い優先順位で始まり、
> リラックスして。
> −2

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- ・それに関連して、まずモデルに合うと、様々なプレースホルダーと組み合わせることがよくあります。

## Chunk 0435

### English（抽出4行）

> −1
> Complexity of model
> Inference for quantity of interest
> simpler

### 日本語訳（自動翻訳）

> −1
> モデルの複雑さ
> 利益の量のための推論
> シンプル

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- −1 モデルの複雑さ 利益の量のための推論 シンプル

## Chunk 0436

### English（抽出4行）

> more complex
> Figure 22: Hypothetical graph comparing inferences for a quantity of interest across multiple
> models. The goal here is not to perform model selection or model averaging but to understand
> how inference for a quantity of interest changes as we move from a simple comparison (on the left

### 日本語訳（自動翻訳）

> より複雑な
> 図22:複数の利益の量に対する推論を比較する仮説グラフ
> モデル。 ここでの目標は、モデルの選択やモデルの平均化を実行していませんが、理解
> 単純な比較から移動するので、関心の変化の量を推論する方法(左に)

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- より複雑な 図22:複数の利益の量に対する推論を比較する仮説グラフ モデル。

## Chunk 0437

### English（抽出4行）

> side of the graph) through the ﬁnal model (on the right side of the graph), going through various
> intermediate alternatives.
> • We’ll check a model, ﬁnd problems, and then expand or replace it. This is part of “Bayesian
> data analysis”; the extra “workﬂow” part is that we still keep the old model, not for the

### 日本語訳（自動翻訳）

> グラフの側面) 最終モデル(グラフの右側)を経由して、さまざまな
> 中間の選択肢。
> • モデルを確認し、問題を見つけ、それを拡張または交換します。 「ベイジアン」の一部です。
> データ分析」; 追加の “ワークフロー” 部分は、我々 はまだ古いモデルを維持しているということです。, ではなく、

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- グラフの側面) 最終モデル(グラフの右側)を経由して、さまざまな 中間の選択肢。

## Chunk 0438

### English（抽出4行）

> purpose of averaging but for the purpose of understanding what we are doing.
> • Sometimes we ﬁt simple models as comparisons. For example, if you’re doing a big regression
> for causal inference, you’ll also want to do a simple unadjusted comparison and then see what
> the adjustments have done.

### 日本語訳（自動翻訳）

> 平均化の目的が、私たちが何をしているかを理解する目的で。
> •時々私達は比較として簡単なモデルに合います。 例えば、大きな回帰をしているなら
> 原因推論のために、あなたはまた、単純な不調整の比較を行い、次に何を参照してください
> 調整が完了しました。

### 熟語・専門語

- **ESS**: 有効サンプルサイズ。自己相関を考慮した独立サンプル相当数。

### 要約

- 平均化の目的が、私たちが何をしているかを理解する目的で。

## Chunk 0439

### English（抽出4行）

> • The above ideas are listed as being motivated by statistical considerations, but sometimes
> we’re jolted into action because of computational problems.
> Given that we are ﬁtting multiple models, we also have to be concerned with researcher degrees of
> freedom (Simmons et al., 2011), most directly from overﬁtting if a single best model is picked, or

### 日本語訳（自動翻訳）

> •上記のアイデアは統計的考察によって動機づけられるようにリストされていますが、時々
> 計算上の問題からアクションに対処します。
> 複数のモデルをフィッティングするということで、研究者の学位にも関わらず
> 自由(シモンズら。、2011)、単一の最高のモデルを選ぶか、または

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- •上記のアイデアは統計的考察によって動機づけられるようにリストされていますが、時々 計算上の問題からアクションに対処します。

## Chunk 0440

### English（抽出4行）

> more subtly that if we are not careful, we can consider our inferences from a set of ﬁtted models to
> bracket some total uncertainty, without recognizing that there are other models we could have ﬁt.
> This concern arises in our election forecasting model, where ultimately we only have a handful of
> past presidential elections with which to calibrate our predictions.

### 日本語訳（自動翻訳）

> 注意していなければ、装着したモデルのセットから、当社の推論を検討することができます。
> 私達が合うことができる他のモデルがあることを認識しないでブラケットのいくつかの総不確実性。
> 私たちの選挙予測モデルのこの懸念は、最終的に我々は唯一の便利なを持っている
> 過去の大統領選挙は、私たちの予測をキャリブレーションする。

### 熟語・専門語

- **uncertainty**: 不確実性。観測・パラメータ・モデル構造・意思決定に残る曖昧さ。
- **prediction**: 予測。未知/将来/除外データに対する分布や点推定。

### 要約

- 注意していなければ、装着したモデルのセットから、当社の推論を検討することができます。

## Chunk 0441

### English（抽出4行）

> Figure 22 illustrates the basic idea: the diagram could represent, for example, a causal eﬀect
> estimated with a sequence of increasingly complicated models, starting with a simple treatment-
> control comparison and proceeding through a series of adjustments. Even if the ultimate interest
> is only in the ﬁnal model, it can be useful to understand how the inference changes as adjustments

### 日本語訳（自動翻訳）

> 図22は基本的な考え方を説明します:図は、例えば、原因の効果を表すことができます
> より複雑なモデルのシーケンスで推定され、簡単な治療から始まります。
> 制御比較と一連の調整を経た進行。 究極の利益が得られるとしても
> 最終モデルでは、調整として推論が変化する方法を理解するのに便利です。

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- 図22は基本的な考え方を説明します:図は、例えば、原因の効果を表すことができます より複雑なモデルのシーケンスで推定され、簡単な治療から始まります。

## Chunk 0442

### English（抽出4行）

> are added.
> Following the proposed workﬂow and exploring the topology of models can often lead us to
> multiple models that pass all the checks. Instead of selecting just one model, we can perform a
> multiverse analysis and use all of the models and see how the conclusions change across the models

### 日本語訳（自動翻訳）

> 追加します。
> 提案されたワークフローに続いて、モデルのトポロジーを調べることは、多くの場合、私たちにつながることができます
> すべてのチェックを通過する複数のモデル。 1つのモデルだけを選ぶ代わりに、我々は実行することができます
> 複数の解析とモデルの全てのモデルを使用して、結論がモデル間でどのように変化するかを確認します

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- 追加します。

## Chunk 0443

### English（抽出4行）

> Freq.
> frequentist all
> frequentist cLOF
> REN: BBS10 more frequent than BBS1

### 日本語訳（自動翻訳）

> フリーク
> 常勤者全員
> クレンディストcLOF
> REN: BBS10 より頻繁に BBS1

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- フリーク 常勤者全員 クレンディストcLOF REN: BBS10 より頻繁に BBS1

## Chunk 0444

### English（抽出4行）

> REN: BBS2 more frequent than BBS1
> REN: BBS2,7,9 more frequent than BBS1,4,8
> REN: BBSome genes differ
> CI: BBS7 more frequent than others

### 日本語訳（自動翻訳）

> REN: BBS2 より頻繁に BBS1
> REN: BBS2,7,9 より頻繁に BBS1,4,8
> REN:BBSome遺伝子は異なる
> CI: BBS7 他より頻繁に

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- REN: BBS2 より頻繁に BBS1 REN: BBS2,7,9 より頻繁に BBS1,4,8 REN:BBSome遺伝子は異なる CI: BBS7 他より頻繁に

## Chunk 0445

### English（抽出4行）

> CI: BBSome more frequent than BBS3
> PD: BBS10 more frequent than BBS1
> PD: BBS2 more frequent than BBS1
> BBSome genes differ

### 日本語訳（自動翻訳）

> CI:BBSomeはBBS3よりも頻繁に
> PD: BBS10 より頻繁に BBS1
> PD: BBS2 より頻繁に BBS1
> BBSome遺伝子は異なる

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- CI:BBSomeはBBS3よりも頻繁に PD: BBS10 より頻繁に BBS1 PD: BBS2 より頻繁に BBS1 BBSome遺伝子は異なる

## Chunk 0446

### English（抽出4行）

> BBS4 most #phenotypes
> BBS4 top odds
> BBS3 less severe than Chaperonins
> BBS3 less severe than BBSome

### 日本語訳（自動翻訳）

> BBS4 最も #フェノタイプ
> BBS4トップオッズ
> BBS3チャペロンインよりも厳しい
> BBS3はBBSomeより厳しいです

### 熟語・専門語

- **ESS**: 有効サンプルサイズ。自己相関を考慮した独立サンプル相当数。

### 要約

- BBS4 最も #フェノタイプ BBS4トップオッズ BBS3チャペロンインよりも厳しい BBS3はBBSomeより厳しいです

## Chunk 0447

### English（抽出4行）

> cLOF mutations more severe
> Freq. type
> Conclusion
> Main

### 日本語訳（自動翻訳）

> cLOF の変異はより厳しい
> フリークタイプ
> コンクルージョン
> メインページ

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- cLOF の変異はより厳しい フリークタイプ コンクルージョン メインページ

## Chunk 0448

### English（抽出4行）

> Secondary
> Problematic fits
> source
> source + cLOF

### 日本語訳（自動翻訳）

> セカンダリー
> 問題のあるフィット
> ソース
> ソース + cLOF

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- セカンダリー 問題のあるフィット ソース ソース + cLOF

## Chunk 0449

### English（抽出4行）

> source + filtered cLOF
> source + gene corr.
> source + no corr.
> source + narrow

### 日本語訳（自動翻訳）

> ソース+フィルタリングされたcLOF
> ソース+遺伝子コルド。
> ソース + ない破損.
> ソース + 狭い

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- ソース+フィルタリングされたcLOF ソース+遺伝子コルド。

## Chunk 0450

### English（抽出4行）

> source + wide
> source + cLOF + ethnic group
> source + cLOF + wide
> source + cLOF (by gene)

### 日本語訳（自動翻訳）

> ソース + ワイド
> ソース + cLOF + エスニックグループ
> ソース + cLOF + ワイド
> ソース + cLOF (遺伝子による)

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- ソース + ワイド ソース + cLOF + エスニックグループ ソース + cLOF + ワイド ソース + cLOF (遺伝子による)

## Chunk 0451

### English（抽出4行）

> source + family
> source + cLOF + family
> source + filtered sex
> source + filtered age

### 日本語訳（自動翻訳）

> ソース+家族
> ソース + cLOF + 家族
> ソース + 濾過性
> ソース + 濾過年齢

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- ソース+家族 ソース + cLOF + 家族 ソース + 濾過性 ソース + 濾過年齢

## Chunk 0452

### English（抽出4行）

> source + filtered cLOF + wide
> source + imputed sex
> source + imputed age
> source + imputed age + sex

### 日本語訳（自動翻訳）

> ソース + フィルタリング cLOF + ワイド
> ソース + インピート 性別
> ソース + 不足年齢
> ソース + インピート年齢 + 性別

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- ソース + フィルタリング cLOF + ワイド ソース + インピート 性別 ソース + 不足年齢 ソース + インピート年齢 + 性別

## Chunk 0453

### English（抽出4行）

> source + very narrow
> none
> ethnic group
> ethnicity

### 日本語訳（自動翻訳）

> ソース + 非常に狭い
> なし
> 民族グループ
> 民族学

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- ソース + 非常に狭い なし 民族グループ 民族学

## Chunk 0454

### English（抽出4行）

> cLOF
> cLOF (by gene)
> ethnic group + cLOF
> ethnicity + cLOF

### 日本語訳（自動翻訳）

> ログイン
> cLOF(遺伝子による)
> 民族グループ+ CLOF
> 民族性 + cLOF

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- ログイン cLOF(遺伝子による) 民族グループ+ CLOF 民族性 + cLOF

## Chunk 0455

### English（抽出4行）

> ethnic group + cLOF (by gene)
> ethnicity + cLOF (by gene)
> family
> filtered age + sex

### 日本語訳（自動翻訳）

> 民族グループ+ cLOF(遺伝子による)
> 民族性 + cLOF (遺伝子による)
> ファミリー
> 濾過年齢 + 性別

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- 民族グループ+ cLOF(遺伝子による) 民族性 + cLOF (遺伝子による) ファミリー 濾過年齢 + 性別

## Chunk 0456

### English（抽出4行）

> none + filtered cLOF
> cLOF + filtered age + sex
> cLOF (by gene) + filtered age + sex
> family + filtered age + sex + cLOF

### 日本語訳（自動翻訳）

> なし + フィルタリング cLOF
> cLOF + 濾過年齢 + 性別
> cLOF (遺伝子による) + 濾過年齢 + 性別
> 家族 + 濾過年齢 + 性別 + cLOF

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- なし + フィルタリング cLOF cLOF + 濾過年齢 + 性別 cLOF (遺伝子による) + 濾過年齢 + 性別 家族 + 濾過年齢 + 性別 + cLOF

## Chunk 0457

### English（抽出4行）

> imputed age + sex
> Model components/modifications besides gene
> 0.05
> 1e−4

### 日本語訳（自動翻訳）

> インピート年齢 + 性別
> 遺伝子以外のモデルコンポーネント/修正
> 0.05の
> 1e−4

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- インピート年齢 + 性別 遺伝子以外のモデルコンポーネント/修正 0.05の 1e−4

## Chunk 0458

### English（抽出4行）

> 1e−8
> p−value
> 0.01
> 0.10

### 日本語訳（自動翻訳）

> 1e−8
> p−値
> 0.01の
> 0.10円

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- 1e−8 p−値 0.01の 0.10円

## Chunk 0459

### English（抽出4行）

> 0.50
> 0.90
> 0.99
> Posterior prob.

### 日本語訳（自動翻訳）

> 0.50円
> 0.90の
> 0.99
> ポスタープロブ。

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- 0.50円 0.90の 0.99 ポスタープロブ。

## Chunk 0460

### English（抽出4行）

> ND
> Figure 23: The results of a multiverse analysis from the supplementary material of Niederlová et al.
> (2019). The heat map shows statistical evaluation of selected conclusions about the relation between
> phenotypes (PD, CI, REN, HEART, LIV) and mutations in various genes of the BBSome (BBS01 -

### 日本語訳（自動翻訳）

> ログイン
> 図23: Niederlová et alの補足材料からの多重解析の結果。
> (2019年) ヒートマップは、選択された結論の統計的評価を示しています。
> BBSome(BBS01)の様々な遺伝子におけるPD、CI、REN、HEART、LIV)および変異

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- ログイン 図23: Niederlová et alの補足材料からの多重解析の結果。

## Chunk 0461

### English（抽出4行）

> BBS8, cLOF - complete loss of function) using a set of Bayesian hierarchical logistic regression
> models and pairwise frequentist tests. Based on posterior predictive checks the Bayesian models
> were categorized as “Main” (passing all checks), “Secondary” (minor problems in some checks),
> and “Problematic ﬁts,” though we see that most conclusions hold across all possible models. The

### 日本語訳（自動翻訳）

> BBS8、cLOF - ベイジアン階層階階階階階階階階階階階階階階階階階階階階階階階階階階階階階階階階階階階階階階階階階階階階階階階階階階階階階階階階階階階階階階階階階階階階階階階階階階階階階階階階階階階階階階階階階階階階階階階階階階階階階階階階階階階階階階階階階階階階階階階階階階階階階階階階階階階階階階階階階階階階階階階階階階階階階階階階階階階階階階階階階階階階階階階階階階階階階階階階階階階階階階階階階階階階階階階階階階階階階階階階階階階階階階階階階階階階階階階階階階階階階階階階階階階階階階階階階階階階階階階階階階
> モデルと対等頻繁なテスト。 バイジアンモデルの予測モデルに基づく
> 「メイン」として分類された(すべてのチェックを通過)、「二次」(一部チェックのマイナーな問題)、
> そして、最も多くの結論は、すべての可能なモデルにわたって保持されていることがわかります。 ザ・オブ・ザ・

### 熟語・専門語

- **posterior predictive**: 事後予測。推定後のモデルが観測データの特徴を再現できるかを見る診断。
- **ESS**: 有効サンプルサイズ。自己相関を考慮した独立サンプル相当数。

### 要約

- BBS8、cLOF - ベイジアン階層階階階階階階階階階階階階階階階階階階階階階階階階階階階階階階階階階階階階階階階階階階階階階階階階階階階階階階階階階階階階階階階階階階階階階階階階階階階階階階階階階階階階階階階階階階階階階階階階階階…

## Chunk 0462

### English（抽出4行）

> models diﬀer in both predictors that are included and priors (default/wide/narrow/very narrow).
> (Steegen et al., 2016, Dragicevic et al., 2019, Kale, Kay, and Hullman, 2019). Using multiverse
> analysis can also relieve some of the eﬀort in validating models and priors: if the conclusions do
> not change it is less important to decide which model is “best.” Figure 23 shows an example of

### 日本語訳（自動翻訳）

> モデルは、含まれている予測者と優先順位(デフォルト/ワイド/矢印/ベリーの狭い)の両方で異なります。
> (Steegen et al., 2016, Dragicevic et al., 2019, Kale, Kay, Hullman, 2019). マルチバースの使用
> 分析は、検証モデルと事前の努力の一部を緩和することもできます。結論が行われる場合
> どのモデルが「ベスト」であるか決めるのはあまり重要ではありません。 図23は例を示します

### 熟語・専門語

- **ESS**: 有効サンプルサイズ。自己相関を考慮した独立サンプル相当数。

### 要約

- モデルは、含まれている予測者と優先順位(デフォルト/ワイド/矢印/ベリーの狭い)の両方で異なります。

## Chunk 0463

### English（抽出4行）

> a possible output. Other analytical choices (data preprocessing, response distribution, metric to
> evaluate, and so forth) can also be subject to multiverse analysis.
> 8.2.
> Cross validation and model averaging

### 日本語訳（自動翻訳）

> 可能な出力。 その他の分析選択(データ処理、応答分布、メトリック)
> また、多重解析の対象となります。
> 8.2. .
> クロス検証とモデル平均化

### 熟語・専門語

- **cross validation**: 交差検証。汎化性能を推定するためにデータを分割/近似除外する評価法。
- **ESS**: 有効サンプルサイズ。自己相関を考慮した独立サンプル相当数。
- **validation**: 検証。モデルが目的・データ・外部知識に照らして妥当かを確認すること。

### 要約

- 可能な出力。

## Chunk 0464

### English（抽出4行）

> We can use cross validation to compare models ﬁt to the same data (Vehtari et al., 2017). When
> performing model comparison, if there is non-negligible uncertainty in the comparison (Sivula et
> al., 2020), we should not simply choose the single model with the best cross validation results,
> as this would discard all the uncertainty from the cross validation process.

### 日本語訳（自動翻訳）

> 同じデータ(Vehtari et al., 2017)に適合するモデルを比較するために、クロス検証を使用できます。 いつか
> パフォーマンスモデルの比較, 比較で非必須の不確実性がある場合 (Sivula et
> al., 2020), 我々は、単に最高のクロス検証結果で単一のモデルを選択すべきではありません,
> これは、クロス検証プロセスからすべての不確実性を破棄するので.

### 熟語・専門語

- **model comparison**: モデル比較。LOO-CVなどで複数モデルの予測性能や弱点を比較すること。
- **cross validation**: 交差検証。汎化性能を推定するためにデータを分割/近似除外する評価法。
- **ESS**: 有効サンプルサイズ。自己相関を考慮した独立サンプル相当数。
- **uncertainty**: 不確実性。観測・パラメータ・モデル構造・意思決定に残る曖昧さ。
- **validation**: 検証。モデルが目的・データ・外部知識に照らして妥当かを確認すること。

### 要約

- 同じデータ(Vehtari et al., 2017)に適合するモデルを比較するために、クロス検証を使用できます。

## Chunk 0465

### English（抽出4行）

> Instead, we can
> maintain this information and use stacking to combine inferences using a weighting that is set up to
> minimize cross validation error (Yao et al., 2018b). We think that stacking makes more sense than
> traditional Bayesian model averaging, as the latter can depend strongly on aspects of the model

### 日本語訳（自動翻訳）

> 代わりに、私達はできます
> この情報を維持し、セットアップされる重みを使用して推論を結合するために積み重ねを使用して下さい
> クロス検証エラー(Yao et al., 2018b)を最小限に抑えます。 積み重ねがよりセンスを増すと思う
> 後者はモデルの面で強く依存することができるので、伝統的なベイジアンモデルの平均化

### 熟語・専門語

- **cross validation**: 交差検証。汎化性能を推定するためにデータを分割/近似除外する評価法。
- **validation**: 検証。モデルが目的・データ・外部知識に照らして妥当かを確認すること。

### 要約

- 代わりに、私達はできます この情報を維持し、セットアップされる重みを使用して推論を結合するために積み重ねを使用して下さい クロス検証エラー(Yao et al., 2018b)を最小限に抑えます。

## Chunk 0466

### English（抽出4行）

> that have minimal eﬀect on predictions. For example, for a model that is well informed by the data
> and whose parameters are on unit scale, changing the prior on parameters from normal(0, 10) to
> normal(0, 100) will divide the marginal likelihood by roughly 10k (for a model with k parameters)
> while keeping all predictions essentially the same. In addition, stacking takes into account the

### 日本語訳（自動翻訳）

> 予測への影響が最小限に抑えられます。 たとえば、データからよく情報されるモデルの場合
> およびその変数は単位のスケール、正常な(0、10)からの変数の前の変更にあります
> 通常(0,100)は、大体10k(kパラメータを持つモデル用)で限界を分割します。
> すべての予測を本質的に同じに保ちながら。 さらに、スタックは考慮に入れます

### 熟語・専門語

- **likelihood**: 尤度。パラメータが与えられたときデータがどれだけ起こりやすいか。
- **ESS**: 有効サンプルサイズ。自己相関を考慮した独立サンプル相当数。
- **prediction**: 予測。未知/将来/除外データに対する分布や点推定。

### 要約

- 予測への影響が最小限に抑えられます。

## Chunk 0467

### English（抽出4行）

> joint predictions and works well when there are a large number of similar but weak models in the
> candidate model list.
> In concept, stacking can sometimes be viewed as pointwise model selection.
> When there

### 日本語訳（自動翻訳）

> 関節の予測は、類似したが弱いモデルが多いときにうまく機能します
> 候補モデルリスト。
> 概念では、スキャニングは、時折ポイントウェイトモデル選択として表示することができます。
> そこまで

### 熟語・専門語

- **prediction**: 予測。未知/将来/除外データに対する分布や点推定。

### 要約

- 関節の予測は、類似したが弱いモデルが多いときにうまく機能します 候補モデルリスト。

## Chunk 0468

### English（抽出4行）

> are two models and the ﬁrst model outperforms the second model 20% of the time, the stacking
> weights will be close to (0.2, 0.8). In light of this, stacking ﬁlls a gap between independent-error
> oriented machine learning validation and the grouped structure of modern big data. Model stacking
> is therefore also an indicator of heterogeneity of model ﬁtting, and this suggests we can further

### 日本語訳（自動翻訳）

> 2つのモデルで、最初のモデルは、時間の2番目のモデル20%を出力します。
> 体重は0.2、0.8に近いです。 これの光では、スタックは独立したエラー間のギャップを埋めます
> 指向機械学習検証と近代的なビッグデータのグループ化された構造。 モデルスタッキング
> したがって、モデルフィッティングの異質性の指標であり、これは私たちがさらにできることを提案します

### 熟語・専門語

- **validation**: 検証。モデルが目的・データ・外部知識に照らして妥当かを確認すること。

### 要約

- 2つのモデルで、最初のモデルは、時間の2番目のモデル20%を出力します。

## Chunk 0469

### English（抽出4行）

> improve the aggregated model with a hierarchical model, so that the stacking is a step toward model
> improvement rather than an end to itself. In the extreme, model averaging can also be done so that
> diﬀerent models can apply to diﬀerent data points (Kamary et al., 2019, Pirš and Štrumbelj, 2019).
> In Bayesian workﬂow, we will ﬁt many models that we will not be interested in including in

### 日本語訳（自動翻訳）

> 階層モデルで集計されたモデルを改善し、スタックはモデルに向かってステップ
> 終わりではなく、それ自体の改善。 極端に、モデルの平均化も行えるので、
> 異なるモデルは、さまざまなデータポイント(Kamary et al., 2019, Pirš と Strumbelj, 2019)に適用することができます。
> ベイジアン・ワークフローでは、私たちは興味をそそそそそそそそそそそそそそそそそそそそそそそそそそそそそそそそそそそそそそそも興味をそそそそそそそそそそそそそそそそそそそそそそそそそそそそそそそそそもそそそそそそそそそそそそそそそそそそそそそそそそそそもそそそそそそそそそそそそそそそそそそそそそそそそそそそそそそそそそそそそそそそそそそそそそそそそそそそそそそそそそそそそそそそそそそそそそそそそそそそそそそそもそそそそそそそそそそそそそそそそそそそそそそそそそそそそそそそそそそそそそそそそそそそそそそそそそそそそそそそそそそそそそそ

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- 階層モデルで集計されたモデルを改善し、スタックはモデルに向かってステップ 終わりではなく、それ自体の改善。

## Chunk 0470

### English（抽出4行）

> any average; such “scaﬀolds” include models that are deliberately overly simple (included just for
> comparison to the models of interest) and models constructed for purely experimental purposes,
> as well as models that have major ﬂaws or even coding errors. But even after these mistakes
> or deliberate oversimpliﬁcations have been removed, there might be several models over which

### 日本語訳（自動翻訳）

> 任意の平均; そのような “足場” 意図的に過度に単純であるモデルを含みます (ちょうどのために含む)
> 興味のモデルと比較して)、純粋に実験的な目的のために構築されたモデル、
> また、大きな欠陥やコーディングエラーを持つモデル。 しかし、これらの間違いの後にも
> または重複の単純化が削除されたり、複数のモデルがある

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- 任意の平均; そのような “足場” 意図的に過度に単純であるモデルを含みます (ちょうどのために含む) 興味のモデルと比較して)、純粋に実験的な目的のために構築されたモデル、 また、大きな欠陥やコーディングエラーを持つモデル。

## Chunk 0471

### English（抽出4行）

> to average when making predictions. In our own applied work we have not generally had many
> occasions to perform this sort of model averaging, as we prefer continuous model expansion,
> but there will be settings where users will reasonably want to make predictions averaging over
> competing Bayesian models, as in Montgomery and Nyhan (2010).

### 日本語訳（自動翻訳）

> 予測をするときの平均値へ。 独自の応用作品では、一般的にはあまり多くなかった
> 連続モデルの拡張を好むので、この種のモデルのベールングを実行する機会,
> しかし、ユーザーが合理的に予測を検証したいという設定があります
> モンゴメリーとニャン(2010)でベイジアンのモデルを競います。

### 熟語・専門語

- **prediction**: 予測。未知/将来/除外データに対する分布や点推定。

### 要約

- 予測をするときの平均値へ。

## Chunk 0472

### English（抽出4行）

> 8.3.
> Comparing a large number of models
> There are many problems, for example in linear regression with several potentially relevant predic-
> tors, where many candidate models are available, all of which can be described as special cases of a

### 日本語訳（自動翻訳）

> 8.3..
> 多数のモデルを比較する
> いくつかの潜在的に関連した述語と線形回帰の例えば、多くの問題があります-
> 多くの候補モデルが利用可能であるtors、そのすべてが特別なケースとして記述することができます

### 熟語・専門語

- **ESS**: 有効サンプルサイズ。自己相関を考慮した独立サンプル相当数。

### 要約

- 8.3.. 多数のモデルを比較する いくつかの潜在的に関連した述語と線形回帰の例えば、多くの問題があります- 多くの候補モデルが利用可能であるtors、そのすべてが特別なケースとして記述することができます

## Chunk 0473

### English（抽出4行）

> single expanded model. If the number of candidate models is large, we are often interested in ﬁnd-
> ing a comparably smaller model that has the same predictive performance as our expanded model.
> This leads to the problem of predictor (variable) selection. If we have many models making similar
> predictions, selecting one of these models based on minimizing cross validation error would lead

### 日本語訳（自動翻訳）

> 単一の拡大されたモデル。 候補者のモデルの数が大きい場合は、よく見つかります-
> 拡大したモデルと同じ予測性能を持つ、非常に小型なモデルです。
> 予測者(変数)選択の問題につながります。 似ているモデルが多い
> 予測, これらのモデルの1つを選択して、クロスバリデーションエラーを最小限に抑える

### 熟語・専門語

- **cross validation**: 交差検証。汎化性能を推定するためにデータを分割/近似除外する評価法。
- **validation**: 検証。モデルが目的・データ・外部知識に照らして妥当かを確認すること。
- **prediction**: 予測。未知/将来/除外データに対する分布や点推定。

### 要約

- 単一の拡大されたモデル。

## Chunk 0474

### English（抽出4行）

> to overﬁtting and suboptimal model choices (Piironen and Vehtari, 2017). In contrast, projection
> predictive variable selection has been shown to be stable and reliable in ﬁnding smaller models
> with good predictive performance (Piironen and Vehtari, 2017, Piironen et al., 2020, Pavone et
> al., 2020). While searching through a big model space is usually associated with the danger of

### 日本語訳（自動翻訳）

> オーバーフィッティングとサブオプタルモデルの選択肢(PiironenとVehtari、2017年) 対照的に、投影
> 予測変数選択はより小さいモデルを見つけることで安定した、信頼できるために示されていました
> 優れた予測性能(PiironenとVehtari、2017、Piironen et al。、2020、Pavone et
> 2020年1月1日 大きいモデル空間を調べながら、通常は危険に関連しています

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- オーバーフィッティングとサブオプタルモデルの選択肢(PiironenとVehtari、2017年) 対照的に、投影 予測変数選択はより小さいモデルを見つけることで安定した、信頼できるために示されていました 優れた予測性能(Piiron…

## Chunk 0475

### English（抽出4行）

> overﬁtting, the projection predictive approach avoids it by examining only the projected submodels
> based on the expanded model’s predictions and not ﬁtting each model independently to the data.
> In addition to variable selection, projection predictive model selection can be used for structure
> selection in generalized additive multilevel models (Catalina et al., 2020) and for creating simpler

### 日本語訳（自動翻訳）

> オーバーフィット、予測予測アプローチは、予測されたサブモデルだけを調べることによってそれを避けます
> 拡張モデルの予測に基づいて、各モデルをデータを独立してフィッティングしません。
> 変数選択に加えて、予測予測モデルの選択は構造に使用することができます
> 総合添加剤マルチレベルモデル(Catalina et al., 2020)で選択し、シンプルに作成

### 熟語・専門語

- **prediction**: 予測。未知/将来/除外データに対する分布や点推定。

### 要約

- オーバーフィット、予測予測アプローチは、予測されたサブモデルだけを調べることによってそれを避けます 拡張モデルの予測に基づいて、各モデルをデータを独立してフィッティングしません。

## Chunk 0476

### English（抽出4行）

> explanations for complex nonparametric models (Afrabandpey et al., 2020).
> 9.
> Modeling as software development
> Developing a statistical model in a probabilistic programming language means writing code and is

### 日本語訳（自動翻訳）

> 複雑な非パラメトリックモデル(Afrabandpey et al., 2020)の説明。
> 9月9日
> ソフトウェア開発としてのモデリング
> 確率的プログラミング言語の統計モデルの開発は、コードを書くことを意味し、

### 熟語・専門語

- **probabilistic programming**: 確率的プログラミング。Stanなどで確率モデルをコードとして記述し推論する方法。

### 要約

- 複雑な非パラメトリックモデル(Afrabandpey et al., 2020)の説明。

## Chunk 0477

### English（抽出4行）

> thus a form of software development, with several stages: writing and debugging the model itself;
> the preprocessing necessary to get the data into suitable form to be modeled; and the later steps of
> understanding, communicating, and using the resulting inferences. Developing software is hard.
> So many things can go wrong because there are so many moving parts that need to be carefully

### 日本語訳（自動翻訳）

> したがって、モデル自体を記述してデバッグするソフトウェア開発の形態。
> 適切なフォームにデータをモデル化するために必要なプリプロセッシング。 後工程
> その結果の推論を理解し、伝達し、そして使用すること。 ソフトウェアの開発は困難です。
> とても多くの動きやすい部分があるので、多くのことが間違って行くことができます。

### 熟語・専門語

- **ESS**: 有効サンプルサイズ。自己相関を考慮した独立サンプル相当数。

### 要約

- したがって、モデル自体を記述してデバッグするソフトウェア開発の形態。

## Chunk 0478

### English（抽出4行）

> synchronized.
> Software development practices are designed to mitigate the problems caused by the inherent
> complexity of writing computer programs. Unfortunately, many methodologies veer oﬀinto dogma,
> bean counting, or both. A couple references we can recommend that provide solid, practical advice

### 日本語訳（自動翻訳）

> 同期。
> ソフトウェア開発慣行は、固有の問題の緩和を目的としています
> コンピュータプログラムの書き込みの複雑さ。 残念なことに、多くの方法論veer offintoのドマ、
> 豆のカウント、または両方。 しっかりした実践的なアドバイスを提供できるカップルの参考文献

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- 同期。

## Chunk 0479

### English（抽出4行）

> for developers are Hunt and Thomas (1999) and McConnell (2004).
> 9.1.
> Version control smooths collaborations with others and with your past self
> Version control software, such as Git, should be should be the ﬁrst piece of infrastructure put in

### 日本語訳（自動翻訳）

> 開発者はHunt and Thomas (1999) と McConnell (2004) です。
> 9.1.(日)
> バージョンコントロールは、他の人と、過去のセルフとのコラボレーションを滑らかに
> Gitなどのバージョン管理ソフトウェアは、置くインフラの最初の部分であるべきであるべきです

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- 開発者はHunt and Thomas (1999) と McConnell (2004) です。

## Chunk 0480

### English（抽出4行）

> place for a project. It may seem like a big investment to learn version control, but it’s well worth it
> to be able to type a single command to revert to a previously working version or to get the diﬀerence
> between the current version and an old version. It’s even better when you need to share work with
> others, even on a paper—work can be done independently and then automatically merged. While

### 日本語訳（自動翻訳）

> プロジェクトの場所。 バージョン管理を学ぶために大きな投資のように思えるかもしれませんが、それだけの価値があります
> 以前に動作するバージョンに戻すか、差分を取得するために、単一のコマンドを入力することができる
> 現在のバージョンと古いバージョンの間。 仕事を共有する必要がある場合は、より良いです
> その他、紙上でも、作業は独立して完了し、自動的にマージすることができます。 しばらくの間

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- プロジェクトの場所。

## Chunk 0481

### English（抽出4行）

> version control keeps track of smaller changes in one model, it is useful to keep the clearly diﬀerent
> models in diﬀerent ﬁles to allow easy comparison of the models. Version control also helps to keep
> notes on the ﬁndings and decisions in the iterative model building, increasing transparency of the
> process.

### 日本語訳（自動翻訳）

> バージョンコントロールは、モデルの小さな変更の追跡を維持します。
> モデルの簡単な比較を可能にするために異なるファイルでモデル。 版制御はまた保つのを助けます
> 反復的なモデルの建物の発見と決定に関するメモ, 透明性を高める
> プロセス。

### 熟語・専門語

- **ESS**: 有効サンプルサイズ。自己相関を考慮した独立サンプル相当数。
- **model building**: モデル構築。仮定・データ構造・prior・likelihoodを組み合わせる工程。
- **decision**: 意思決定。予測分布を損失・効用・行動選択へ接続する工程。

### 要約

- バージョンコントロールは、モデルの小さな変更の追跡を維持します。

## Chunk 0482

### English（抽出4行）

> Version control is not just for code. It is also for reports, graphs, and data. Version control is a
> critical part of ensuring that all of these components are synchronized and, more importantly, that
> it is possible to rewind the project to a previous state. Version control is particularly useful for its
> ability to package up and label “release candidate” versions of models and data that correspond to

### 日本語訳（自動翻訳）

> バージョン制御はコードだけではありません。 レポート、グラフ、データも対応しています。 バージョン制御はあります
> これらのすべてのコンポーネントが同期され、より重要なことを確実にする重要な部分
> プロジェクトを以前の状態に戻すことができます。 バージョン制御は、そのために特に有用である
> 対応するモデルとデータの「リリース候補」バージョンをパッケージ化およびラベル付けする機能

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- バージョン制御はコードだけではありません。

## Chunk 0483

### English（抽出4行）

> milestone reports and publications and to store them in the same directory without resorting to the
> dreaded _final_final_161020.pdf-style naming conventions.
> When working on models that are used to guide policy decision making, a public version control
> repository increases transparency about what model, data, inference parameters, and scripts were

### 日本語訳（自動翻訳）

> マイルストーンのレポートと出版物、および同じディレクトリに保存する
> dreaded  final final 161020.pdf-style 命名規則。
> 政策決定を導くために使用されるモデルで作業する場合, 公開バージョン管理
> リポジトリは、モデル、データ、推論パラメータ、およびスクリプトの透明性を高める

### 熟語・専門語

- **decision**: 意思決定。予測分布を損失・効用・行動選択へ接続する工程。

### 要約

- マイルストーンのレポートと出版物、および同じディレクトリに保存する dreaded final final 161020.pdf-style 命名規則。

## Chunk 0484

### English（抽出4行）

> used for speciﬁc reports. An excellent example of this is the Imperial College repository for models
> and scripts to estimate deaths and cases for COVID-19 (Flaxman et al., 2020).
> 9.2.
> Testing as you go

### 日本語訳（自動翻訳）

> 特定のレポートに使用する。 この優れた例は、モデルの帝国大学リポジトリです
> COVID-19(Flaxman et al., 2020)の死亡および症例を推定するスクリプト。
> 9.2. .
> あなたが行くようにテスト

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- 特定のレポートに使用する。

## Chunk 0485

### English（抽出4行）

> Software design ideally proceeds top down from the goals of the end user back to the technical
> machinery required to implement it. For a Bayesian statistical model, top-down design involves at
> least the data input format, the probabilistic model for the data, and the prior, but may also involve
> simulators and model testing like simulation-based calibration or posterior predictive checks.

### 日本語訳（自動翻訳）

> ソフトウェア設計は、エンドユーザーの目標から技術に理想的に追いつく
> 実装に必要な機械。 ベイジアン統計モデルの場合、トップダウン設計は
> 少なくともデータ入力フォーマット、データの確率的モデル、および前述のものを含むかもしれません
> シミュレーションベースの校正やポスター予測チェックなどのシミュレータおよびモデルテスト。

### 熟語・専門語

- **posterior predictive**: 事後予測。推定後のモデルが観測データの特徴を再現できるかを見る診断。
- **simulation-based calibration**: SBC。シミュレーション真値と事後rankを比べ、実装・推論の校正を検査する方法。

### 要約

- ソフトウェア設計は、エンドユーザーの目標から技術に理想的に追いつく 実装に必要な機械。

## Chunk 0486

### English（抽出4行）

> Software development ideally works bottom up from well-tested foundational functions to larger
> functional modules. That way, development proceeds through a series of well-tested steps, at each
> stage building only on tested pieces. The advantage to working this way as opposed to building a
> large program and then debugging it is the same as for incremental model development—it’s easier

### 日本語訳（自動翻訳）

> ソフトウェア開発は、十分にテストされた基礎機能からより大きいまで理想的に最下で働きます
> 機能モジュール。 このようにして、開発は一連のよくテストされたステップを各々で進めます
> テストされた部分だけに段階の建物。 建物ではなく、このように動作する利点
> 大規模なプログラムとデバッグは、増分モデル開発と同じです。

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- ソフトウェア開発は、十分にテストされた基礎機能からより大きいまで理想的に最下で働きます 機能モジュール。

## Chunk 0487

### English（抽出4行）

> to track where the development went wrong and you have more conﬁdence at each step working
> with well-tested foundations.
> The key to computational development, either in initial development or modifying code, is
> modularity. Big tangled functions are hard to document, harder to read, extraordinarily diﬃcult

### 日本語訳（自動翻訳）

> 開発が間違っていた場所を追跡し、各ステップでより多くの自信を持っている
> よくテストされた基礎を使って。
> 計算開発の鍵は、初期開発やコード変更の鍵となります。
> モジュール性。 大きい形づけられた機能は文書、読みにくい、余分に困難です

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- 開発が間違っていた場所を追跡し、各ステップでより多くの自信を持っている よくテストされた基礎を使って。

## Chunk 0488

### English（抽出4行）

> to debug, and nearly impossible to maintain or modify. Modularity means building larger pieces
> out of smaller trusted pieces, such as low-level functions. Whenever code fragments are repeated,
> they should be encapsulated as functions. This results in code that is easier to read and easier to
> maintain.

### 日本語訳（自動翻訳）

> デバッグ、メンテナンスや変更がほとんど不可能です。 モジュラー性はより大きい部分を造ることを意味します
> 低レベルの機能など、より小さい信頼される部分から。 フラグメントが繰り返されるたびに、
> 関数としてカプセル化する必要があります。 この結果は、読みやすく、読みやすくなります。
> メンテナンス

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- デバッグ、メンテナンスや変更がほとんど不可能です。

## Chunk 0489

### English（抽出4行）

> As an example of a low-level function, predictors might be rescaled for a generalized linear
> model by implementing the standardization, z(v) = (v −mean(v))/sd(v). Although this function
> seems simple, subtleties arise, starting with the sd function, which is sometimes deﬁned as sd(v) =
> pPn

### 日本語訳（自動翻訳）

> 低レベルの関数の例として、予測者は一般化された線形に対して再スケールされるかもしれません
> 標準化、z(v) = (v)/sd(v) の実装によるモデル。 この関数は
> sd 関数から始まる、単純で微妙な arise だ。 sd(v) =
> ppnの

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- 低レベルの関数の例として、予測者は一般化された線形に対して再スケールされるかもしれません 標準化、z(v) = (v)/sd(v) の実装によるモデル。

## Chunk 0490

### English（抽出4行）

> i=1(vi −mean(v))2/n and sometimes as sd(v) =
> pPn
> i=1(vi −mean(v))2/(n −1). If this
> isn’t sorted out at the level of the standardization function, it can produce mysterious biases during

### 日本語訳（自動翻訳）

> i=1(vi-mean(v)))2/n と sd(v) =
> ppnの
> i=1(vi-mean(v))2/(n −1)。 お問い合わせ
> 標準化機能のレベルでソートされていない、それはの間に神秘的なバイアスを作り出すことができます

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- i=1(vi-mean(v)))2/n と sd(v) = ppnの i=1(vi-mean(v))2/(n −1)。

## Chunk 0491

### English（抽出4行）

> inference.
> Simple tests that don’t rely on the sd() function will sort this out during function
> development. If the choice is the estimate that divides by n −1, there needs to be decision of what
> to do when v is a vector of length 1. In cases where there are illegal inputs, it helps to put checks in

### 日本語訳（自動翻訳）

> インフェレンス
> sd() 関数に依存しないシンプルなテストは、関数中にこれをソートします
> 開発。 n −1で割るお見積もりの場合は、何の決定が必要
> v が長さ1のベクトルであるときを行う 違法な入力がある場合には、チェックを入れるのに役立ちます

### 熟語・専門語

- **decision**: 意思決定。予測分布を損失・効用・行動選択へ接続する工程。

### 要約

- インフェレンス sd() 関数に依存しないシンプルなテストは、関数中にこれをソートします 開発。

## Chunk 0492

### English（抽出4行）

> the input-output routines that let users know when the problem arises rather than allowing errors
> to percolate through to mysterious divide-by-zero errors later.
> An implementation of cubic splines or an Euler solver for a diﬀerential equation is an example
> of a higher-level function that should be tested before it is used. As functions get more complicated,

### 日本語訳（自動翻訳）

> 問題がエラーを可能にするのではなく、問題が発生したときにユーザーに知らせる入力出力ルーチン
> 後で神秘的な分岐によるゼロエラーに打ち勝つ。
> 立方スプラインまたは差分式のためのユーラーソルバーの実装は、例
> 使用される前にテストされるべきより高いレベルの機能の。 機能がより複雑になるように、

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- 問題がエラーを可能にするのではなく、問題が発生したときにユーザーに知らせる入力出力ルーチン 後で神秘的な分岐によるゼロエラーに打ち勝つ。

## Chunk 0493

### English（抽出4行）

> they become harder to test because of issues with boundary-condition combinatorics, more general
> inputs such as functions to integrate, numerical instability or imprecision over regions of their
> domain which may or may not be acceptable depending on the application, the need for stable
> derivatives, etc.

### 日本語訳（自動翻訳）

> それらは境界条件の結合剤との問題のためにテストするより困難になります、より一般
> 統合する機能、数値的な不安定性、またはその地域の不正確などの入力
> 適用、安定したのための必要性によってまたは受け入れられないかもしれないドメイン
> 誘導体等

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- それらは境界条件の結合剤との問題のためにテストするより困難になります、より一般 統合する機能、数値的な不安定性、またはその地域の不正確などの入力 適用、安定したのための必要性によってまたは受け入れられないかもしれないドメイン 誘導体等

## Chunk 0494

### English（抽出4行）

> 9.3.
> Making it essentially reproducible
> A lofty goal for any project is to make it fully reproducible in the sense that another person on
> another machine could recreate the ﬁnal report. This is not the type of reproducibility that is

### 日本語訳（自動翻訳）

> 9.3. .
> それは本質的に再現可能にする
> どんなプロジェクトでもロフトの目標は、他の人がいる意味で完全に再現性を作ることです
> 別の機械は最終的なレポートを再作成できます。 これは再現性の一種ではありません

### 熟語・専門語

- **ESS**: 有効サンプルサイズ。自己相関を考慮した独立サンプル相当数。

### 要約

- 9.3. . それは本質的に再現可能にする どんなプロジェクトでもロフトの目標は、他の人がいる意味で完全に再現性を作ることです 別の機械は最終的なレポートを再作成できます。

## Chunk 0495

### English（抽出4行）

> considered in scientiﬁc ﬁelds, where the desire is to ensure that an eﬀect is conﬁrmed by new future
> data (nowadays often called “replicability” for a better distinction between the diﬀerent notions).
> Instead this is the more limited (but still vital) goal of ensuring that one particular analysis is
> consistently done. In particular, we would want to be able to produce analyses and ﬁgures that

### 日本語訳（自動翻訳）

> 新しい未来によって効果が確認されることを望む科学分野で考慮される、
> 異なる概念間のより良い区別のためのデータ(最近はしばしば「信頼性」と呼ばれます)。
> 代わりに、これは、その1つの特定の分析がであることを確実にするためのより限られた(しかし、まだ重要な)目標です
> 一貫して行います。 特に、分析や数値を生成したいと考えています。

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- 新しい未来によって効果が確認されることを望む科学分野で考慮される、 異なる概念間のより良い区別のためのデータ(最近はしばしば「信頼性」と呼ばれます)。

## Chunk 0496

### English（抽出4行）

> are essentially equivalent to the original document. Bit-level reproducibility may not be possible,
> but we would still liken equivalence at a practical level. In the event that this type of reproduction
> changes the outcome of a paper, we would argue that the original results were not particularly
> robust.

### 日本語訳（自動翻訳）

> 元の文書と基本的に等価です。 ビットレベルの再現性は不可能です。
> しかしながら、実用的なレベルでの平等性が気に入っています。 このタイプの再現が行われる場合
> 紙の成果を変化させ、原本的な結果が特になかったことを論じます
> 堅牢。

### 熟語・専門語

- **ESS**: 有効サンプルサイズ。自己相関を考慮した独立サンプル相当数。

### 要約

- 元の文書と基本的に等価です。

## Chunk 0497

### English（抽出4行）

> Rather than entering commands on the command line when running models (or entering
> commands directly into an interactive programming language like R or Python), write scripts to
> run the data through the models and produce whatever posterior analysis you need. Scripts can
> be written for the shell, R, Python, or any other programming language. The script should be

### 日本語訳（自動翻訳）

> 実行中のモデル(または入力)時にコマンドラインでコマンドを入力するよりもむしろ
> R や Python などのインタラクティブなプログラミング言語に直接コマンドを記述します。
> モデルを通してデータを実行し、必要なあらゆるポスター分析を生成します。 スクリプトは
> シェル、R、Python、その他のプログラミング言語で記述します。 スクリプトは

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- 実行中のモデル(または入力)時にコマンドラインでコマンドを入力するよりもむしろ R や Python などのインタラクティブなプログラミング言語に直接コマンドを記述します。

## Chunk 0498

### English（抽出4行）

> self-contained in the sense that it should run in a completely clean environment or, ideally, on a
> diﬀerent computer. This means that the script(s) must not depend on global variables having been
> set, other data being read in, or anything else that is not in the script.
> Scripts are good documentation. It may seem like overkill if running the project is only a single

### 日本語訳（自動翻訳）

> それは完全にきれいな環境で動くべきか、理想的に、意味で自己完結しました
> 別のコンピュータ。 つまり、スクリプトはグローバル変数に依存しない
> 設定、他のデータが読み込まれているか、スクリプトに存在しないもの。
> スクリプトは良いドキュメントです。 プロジェクトを実行すると、オーバーキルのように思えるかもしれません。

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- それは完全にきれいな環境で動くべきか、理想的に、意味で自己完結しました 別のコンピュータ。

## Chunk 0499

### English（抽出4行）

> line of code, but the script provides not only a way to run the code, but also a form of concrete
> documentation for what is being run. For complex projects, we often ﬁnd that a well-constructed
> series of scripts can be more practical than one large R Markdown document or Jupyter notebook.
> Depending on long-term reproducibility needs, it’s important to choose the right tooling for the

### 日本語訳（自動翻訳）

> コードの行, しかし、スクリプトは、コードを実行する方法だけでなく、コンクリートの形態を提供します
> 実行されているもののドキュメント。 複雑なプロジェクトでは、よく構築されたことがよくあります。
> スクリプトのシリーズは、1つの大きなRマークダウン文書またはジュピターノートよりも実用的であることができます。
> 長期的な再現性のニーズに応じて、適切なツーリングを選択することが重要です。

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- コードの行, しかし、スクリプトは、コードを実行する方法だけでなく、コンクリートの形態を提供します 実行されているもののドキュメント。

## Chunk 0500

### English（抽出4行）

> job at hand. To guarantee bit-level reproducibility, and sometimes even just to get a program to
> run, everything from hardware, to the operating system, to every piece of software and setting must
> be speciﬁed with their version number. As time passes between the initial writing of the script and
> the attempt of reproduction, bit-level reproducibility can be almost impossible to achieve even if

### 日本語訳（自動翻訳）

> 求人情報 ビットレベルの再現性を保証するため、プログラムを入手するだけでも
> 実行, ハードウェアから, オペレーティングシステムまで, ソフトウェアと設定のあらゆる部分に
> バージョン番号で指定します。 スクリプトとスクリプトの初期の書き込みとの間の時刻が渡る
> 再生の試み、ビットレベルの再現性は、たとえもしも達成することができません

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- 求人情報 ビットレベルの再現性を保証するため、プログラムを入手するだけでも 実行, ハードウェアから, オペレーティングシステムまで, ソフトウェアと設定のあらゆる部分に バージョン番号で指定します。

## Chunk 0501

### English（抽出4行）

> the environment is shipped with the script, as in a Docker container.
> 9.4.
> Making it readable and maintainable
> Treating programs and scripts like other forms of writing for an audience provides an important

### 日本語訳（自動翻訳）

> 環境は、Docker コンテナのようにスクリプトで出荷されます。
> 9.4。
> 読みやすく、維持可能にする
> 聴衆のための他の形態の書き込みのようなプログラムやスクリプトを扱うことは重要なことを提供します

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- 環境は、Docker コンテナのようにスクリプトで出荷されます。

## Chunk 0502

### English（抽出4行）

> perspective on how the code will be used. Not only might others want to read and understand a
> program or model, the developers themselves will want to read and understand it later. One of the
> motivations of Stan’s design was to make models self-documenting in terms of variable usage (e.g.,
> data or parameters), types (e.g., covariance matrix or unconstrained matrix) and sizes. This allows

### 日本語訳（自動翻訳）

> コードの使い方について 他の人が読んで理解したいかもしれないだけでなく、
> プログラムまたはモデル、開発者自身は後で読み、理解したいと思う。 の 1 つ
> Stanのデザインのモチベーションは、変数使用条件(例えば、
> データまたはパラメータ)、タイプ(例、コバリンス行列または未禁行列)およびサイズ。 これは、

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- コードの使い方について 他の人が読んで理解したいかもしれないだけでなく、 プログラムまたはモデル、開発者自身は後で読み、理解したいと思う。

## Chunk 0503

### English（抽出4行）

> us to understand Stan code (or code of other statically typed probabilistic programming languages)
> to be understandable without the context of the data it is applied on.
> A large part of readability is consistency, particularly in naming and layout, and not only of
> programs themselves, but the directories and ﬁles in which they are stored. Another key principle

### 日本語訳（自動翻訳）

> Stanコード(または、他の静的タイプの確率的プログラミング言語のコード)を理解するために私たち
> 適用されるデータのコンテキストなしで理解できるようにします。
> 読みやすさの大きな部分は、特にネーミングとレイアウトだけでなく、一貫性です
> プログラム自体が保存されているディレクトリとファイル。 別の主原則

### 熟語・専門語

- **probabilistic programming**: 確率的プログラミング。Stanなどで確率モデルをコードとして記述し推論する方法。

### 要約

- Stanコード(または、他の静的タイプの確率的プログラミング言語のコード)を理解するために私たち 適用されるデータのコンテキストなしで理解できるようにします。

## Chunk 0504

### English（抽出4行）

> in coding is to avoid repetition, instead pulling shared code out into functions that can be reused.
> Readability of code is not just about comments—it is also about naming and organization for
> readability. Indeed, comments can made code less readable. The best approach is to write readable
> code, not opaque code with comments. For example, we don’t want to write this:

### 日本語訳（自動翻訳）

> コーディングでは、繰り返しを避けるためです。代わりに、共有されたコードを再利用できる関数に引き出すことです。
> コードの読みやすさは、コメントだけでなく、ネーミングや組織について
> 可読性。 確かに、コメントはコードを読みやすくすることができます。 最良の方法は、読みやすく書くことです
> コメントの不透明コードではなく、コード。 例えば、次のように書きたくない。

### 熟語・専門語

- **ESS**: 有効サンプルサイズ。自己相関を考慮した独立サンプル相当数。

### 要約

- コーディングでは、繰り返しを避けるためです。

## Chunk 0505

### English（抽出4行）

> real x17;
> // oxygen level, should be positive
> when we can write this:
> real<lower = 0> oxygen_level;

### 日本語訳（自動翻訳）

> 実際のx17;
> // 酸素レベルは肯定的であるべきです
> これを記述できるとき:
> real<lower = 0> 酸素レベル;

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- 実際のx17; // 酸素レベルは肯定的であるべきです これを記述できるとき: real<lower = 0> 酸素レベル;

## Chunk 0506

### English（抽出4行）

> Similarly, we don’t want to do this:
> target += -0.5 * (y - mu)^2 / sigma^2;
> // y distributed normal(mu, sigma)
> when we can write,

### 日本語訳（自動翻訳）

> 同様に、これを行う必要はありません。
> ターゲット += -0.5 * (y - mu)^2 / sigma^2;
> // y は正規(mu, sigma) を配布しました。
> 書くことができるとき、

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- 同様に、これを行う必要はありません。

## Chunk 0507

### English（抽出4行）

> target += normal_lpdf(y | mu, sigma);
> Good practice is to minimize inline code comments and instead write readable code. As the above
> examples illustrate, clean code is facilitated by programming languages that gives users the tools
> they need to use.

### 日本語訳（自動翻訳）

> ターゲット+=normal lpdf(y | mu, sigma);
> グッドプラクティスは、インラインコードコメントを最小化し、読みやすいコードを書くことです。 上記と同様に
> サンプルは、ユーザーがツールを与えるプログラミング言語によって、きれいなコードを容易にします
> 使う必要があります。

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- ターゲット+=normal lpdf(y | mu, sigma); グッドプラクティスは、インラインコードコメントを最小化し、読みやすいコードを書くことです。

## Chunk 0508

### English（抽出4行）

> User-facing functions should be documented at the function level in terms of their argument
> types, return types, error conditions, and behavior—that’s the application programming interface
> (API) that users see instead of code internals. The problem with inline code comments aimed at
> developers is that they quickly go stale during development and wind up doing more harm than good.

### 日本語訳（自動翻訳）

> ユーザーフェーシング関数は、引数の面で関数レベルで文書化されるべきです
> 型, 戻り型, エラー条件, 動作 — アプリケーションプログラミングインターフェイス
> (API) ユーザーが内部のコードではなく参照する。 目指すインラインコードコメントの問題
> 開発者は、開発中すぐに階段を上り、良いよりも害を及ぼす風を上げることです。

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- ユーザーフェーシング関数は、引数の面で関数レベルで文書化されるべきです 型, 戻り型, エラー条件, 動作 — アプリケーションプログラミングインターフェイス (API) ユーザーが内部のコードではなく参照する。

## Chunk 0509

### English（抽出4行）

> Instead, rather than documenting the actual code inline, functions should be reduced to manageable
> size and names should be chosen so that the code is readable. Longer variable names are not always
> better, as they can make the structure of the code harder to scan. Code documentation should be
> written assuming the reader understands the programming language well; as such, documentation

### 日本語訳（自動翻訳）

> 代わりに、実際のコードのインラインを文書化するのではなく、管理可能な関数を削減する必要があります
> コードが読みやすくするために、サイズと名前を選択する必要があります。 より長い変数名は常にない
> より良く、コードの構造をスキャンするのが難しくなります。 コードのドキュメントは
> 読者がプログラミング言語をよく理解していると仮定して書かれています。 など、ドキュメント

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- 代わりに、実際のコードのインラインを文書化するのではなく、管理可能な関数を削減する必要があります コードが読みやすくするために、サイズと名前を選択する必要があります。

## Chunk 0510

### English（抽出4行）

> is only called for when the code strays from idiomatic usage of the language or involves complex
> Figure 24: Success rate of putts of professional golfers, from a small dataset appearing in Berry
> (1995). The error bars associated with each point j in the graph are simple classical standard
> deviations,

### 日本語訳（自動翻訳）

> 言語の慣用的な使用からコードのstraysが呼び出されるか、複雑なものを含む場合にのみ呼び出されます。
> 図24:ベリーに出現する小さなデータセットから、プロのゴルファーのパットの成功率
> (1995年) グラフ内の各ポイントjに関連付けられているエラーバーは、単純な古典的な標準です
> 偏差,

### 熟語・専門語

- **ESS**: 有効サンプルサイズ。自己相関を考慮した独立サンプル相当数。

### 要約

- 言語の慣用的な使用からコードのstraysが呼び出されるか、複雑なものを含む場合にのみ呼び出されます。

## Chunk 0511

### English（抽出4行）

> p
> ˆpj(1 −ˆpj)/nj, where ˆpj = yj/nj is the success rate for putts taken at distance xj.
> algorithms that need external documentation. When tempted to comment a long expression or
> block of code, instead consider replacing it with a well-named function.

### 日本語訳（自動翻訳）

> お問い合わせ
> 'pj = yj/nj は、距離 xj で撮影したパットの成功率です。
> 外部文書が必要なアルゴリズム。 長い表現や
> コードのブロックは、代わりによく名前を付けた関数で置き換えることを検討します。

### 熟語・専門語

- **ESS**: 有効サンプルサイズ。自己相関を考慮した独立サンプル相当数。

### 要約

- お問い合わせ 'pj = yj/nj は、距離 xj で撮影したパットの成功率です。

## Chunk 0512

### English（抽出4行）

> Related to readability is the maintainability of the workﬂow code. When ﬁtting a series of
> similar models, a lot of modules will be shared between them (see Section 2.2) and so will be the
> corresponding code. If we had just copied all of the model code each time we wrote a new model,
> and then discovered an error in one of the shared modules, we would have to ﬁx it in all models

### 日本語訳（自動翻訳）

> 読みやすさに関連したワークフローコードの保守性です。 シリーズの取り付け時
> 同様のモデルでは、それらの間で多くのモジュールが共有されます(セクション2.2を参照してください)。
> 対応するコード。 一度にモデルコードを全てコピーしただけだったら、新しいモデルを書きました。
> そして、共有モジュールの1つでエラーを発見し、すべてのモデルでそれを修正する必要があります

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- 読みやすさに関連したワークフローコードの保守性です。

## Chunk 0513

### English（抽出4行）

> manually. This is again an error-prone process. Instead, it can be sensible not only to build models
> in a modular manner but also keep the corresponding code modular and load it into the models as
> needed. That way, ﬁxing an error in a module requires changing code in just one rather than many
> places. Errors and other requirements for later changes will inevitably occur as we move through

### 日本語訳（自動翻訳）

> 手動で。 これは再びエラーが発生します。 代わりに、モデルをビルドするだけでなく、センシブルなことができます
> モジュラー方式で、また対応するコードをモジュラーに保ち、モデルにとして荷を積んで下さい
> 必要な。 このようにして、モジュール内のエラーを修正するには、複数の代わりにコードを変更する必要があります
> 場所。 後で変更するためのエラーやその他の要件は、私たちが移動するにつれて必然的に起こります

### 熟語・専門語

- **ESS**: 有効サンプルサイズ。自己相関を考慮した独立サンプル相当数。

### 要約

- 手動で。

## Chunk 0514

### English（抽出4行）

> the workﬂow and it will save us a lot of time if we prepare our modeling code accordingly.
> 10.
> Example of workflow involving model building and expansion: Golf putting
> We demonstrate the basic workﬂow of Bayesian modeling using an example of a set of models ﬁt

### 日本語訳（自動翻訳）

> ワークフローと、モデリングコードを適切に準備すれば、多くの時間を節約できます。
> 10月10日
> モデル構築と拡張のワークフロー例: ゴルフパッティング
> ベイジアンモデリングの基本的なワークフローをモデルのセット例で示します。

### 熟語・専門語

- **workflow**: ワークフロー。実務分析の反復手順全体。
- **model building**: モデル構築。仮定・データ構造・prior・likelihoodを組み合わせる工程。

### 要約

- ワークフローと、モデリングコードを適切に準備すれば、多くの時間を節約できます。

## Chunk 0515

### English（抽出4行）

> to data on golf putting (Gelman, 2019).
> Figure 24 shows data from professional golfers on the proportion of successful putts as a
> function of (rounded) distance from the hole. Unsurprisingly, the probability of making the shot
> declines as a function of distance.

### 日本語訳（自動翻訳）

> ゴルフパッティングに関するデータ(Gelman, 2019)
> 図24は、成功したパットの割合でプロのゴルファーからのデータを示しています
> 穴からの(円形にされた)間隔の機能。 絶対に、ショットを作る確率
> 距離の機能として低下します。

### 熟語・専門語

- **ESS**: 有効サンプルサイズ。自己相関を考慮した独立サンプル相当数。

### 要約

- ゴルフパッティングに関するデータ(Gelman, 2019) 図24は、成功したパットの割合でプロのゴルファーからのデータを示しています 穴からの(円形にされた)間隔の機能。

## Chunk 0516

### English（抽出4行）

> Figure 25: Golf data from Figure 24 along with ﬁtted logistic regression and draws of the ﬁtted
> curve, y = logit−1(a + bxj), given posterior draws of (a, b).
> Figure 26: Simple geometric model of golf putting, showing the range of angles with which the ball
> can be hit and still have a trajectory that goes entirely into the hole. Not to scale.

### 日本語訳（自動翻訳）

> 図25: 図24のゴルフデータと、適合したロジスティック回帰と描画
> 曲線、y = logit−1(a + bxj)、ポスターの描画(a、b)。
> 図26:ボールの角度の範囲を示す、ゴルフパッティングのシンプルな幾何学モデル
> 穴に完全に入るtrajectoryを打つことができます。 スケールしない

### 熟語・専門語

- **ESS**: 有効サンプルサイズ。自己相関を考慮した独立サンプル相当数。
- **posterior draws**: 事後ドロー。事後分布から得たサンプル。

### 要約

- 図25: 図24のゴルフデータと、適合したロジスティック回帰と描画 曲線、y = logit−1(a + bxj)、ポスターの描画(a、b)。

## Chunk 0517

### English（抽出4行）

> 10.1.
> First model: logistic regression
> Can we model the probability of success in golf putting as a function of distance from the hole?
> Given usual statistical practice, the natural starting point would be logistic regression:

### 日本語訳（自動翻訳）

> 10月1日
> ファーストモデル: ロジスティック回帰
> 穴からの距離の機能として、ゴルフでの成功の確率をモデル化できますか?
> 通常の統計的な練習を与えられた、自然な出発点は記号論理的な回帰です:

### 熟語・専門語

- **ESS**: 有効サンプルサイズ。自己相関を考慮した独立サンプル相当数。

### 要約

- 10月1日 ファーストモデル: ロジスティック回帰 穴からの距離の機能として、ゴルフでの成功の確率をモデル化できますか? 通常の統計的な練習を与えられた、自然な出発点は記号論理的な回帰です:

## Chunk 0518

### English（抽出4行）

> yj ∼binomial
>  nj, logit−1(a + bxj)
> 
> , for j = 1, . . . , J.

### 日本語訳（自動翻訳）

> yj 〜binomial さん
>  nj、logit−1(a + bxj)
> , j = 1, . . , J .

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- yj 〜binomial さん  nj、logit−1(a + bxj) , j = 1, . . , J .

## Chunk 0519

### English（抽出4行）

> Figure 25 shows the logistic ﬁtted regression along with draws form the posterior distribution.
> Here we ﬁt using a uniform prior on (a, b) which causes no problems given the large sample size.
> 10.2.
> Modeling from first principles

### 日本語訳（自動翻訳）

> 図25は、ドローとともに配置された回帰性を示し、ポスター分布を形成します。
> ここでは、大きなサンプルサイズを与えられた問題を引き起こしない(a、b)上の均一を使用して収まります。
> 10.2.
> 最初の原則からモデリング

### 熟語・専門語

- **posterior distribution**: 事後分布。データ観測後の未知量の不確実性を表す分布。
- **ESS**: 有効サンプルサイズ。自己相関を考慮した独立サンプル相当数。

### 要約

- 図25は、ドローとともに配置された回帰性を示し、ポスター分布を形成します。

## Chunk 0520

### English（抽出4行）

> We next ﬁt the data using a simple mathematical model of the golf putting process. Figure 26
> shows a simpliﬁed sketch of a golf shot. The dotted line represents the angle within which the
> ball of radius r must be hit so that it falls within the hole of radius R. This threshold angle is
> sin−1((R −r)/x). The graph is intended to illustrate the geometry of the ball needing to go into

### 日本語訳（自動翻訳）

> 次回は、ゴルフパッティングプロセスのシンプルな数学モデルを使ってデータに収まります。 図26
> ゴルフショットの簡単なスケッチが表示されます。 点線は内部の角度を表します
> 半径 R の球は半径 R の穴の内で落ちるように打つ必要があります。 この境界角は
> シン−1((R−r)/x) グラフは、ボールのジオメトリを調べることを目的としています。

### 熟語・専門語

- **ESS**: 有効サンプルサイズ。自己相関を考慮した独立サンプル相当数。

### 要約

- 次回は、ゴルフパッティングプロセスのシンプルな数学モデルを使ってデータに収まります。

## Chunk 0521

### English（抽出4行）

> the hole.
> Figure 27: Two models ﬁt to the golf data. The geometry-based model ﬁts much better than the
> logistic regression even while using one fewer parameter.
> The next step is to model human error. We assume that the golfer is attempting to hit the ball

### 日本語訳（自動翻訳）

> 穴。
> 図27: ゴルフデータに収まる2つのモデル。 幾何学ベースのモデルはより大いによく合います
> 1つのパラメータを使用しても、ロジスティック回帰。
> 次のステップは、ヒューマンエラーをモデル化することです。 ゴルファーがボールを打つことを試みていると仮定します

### 熟語・専門語

- **ESS**: 有効サンプルサイズ。自己相関を考慮した独立サンプル相当数。

### 要約

- 穴。

## Chunk 0522

### English（抽出4行）

> completely straight but that many small factors interfere with this goal, so that the actual angle
> follows a normal distribution centered at 0 with some standard deviation σ.
> The probability the ball goes in the hole is then the probability that the angle is less than the
> threshold; that is,

### 日本語訳（自動翻訳）

> 完全にまっすぐだが、多くの小さな要因は、この目標を妨げるので、実際の角度
> 標準的な偏差のσで0で中心にされた正常な配分に続いて下さい。
> ボールが穴に入る確率は、角度がより低い確率です
> しきい値; つまり、

### 熟語・専門語

- **ESS**: 有効サンプルサイズ。自己相関を考慮した独立サンプル相当数。

### 要約

- 完全にまっすぐだが、多くの小さな要因は、この目標を妨げるので、実際の角度 標準的な偏差のσで0で中心にされた正常な配分に続いて下さい。

## Chunk 0523

### English（抽出4行）

> Pr(|angle| < sin−1((R −r)/x)) = 2Φ
> sin−1((R −r)/x)
> σ
> 

### 日本語訳（自動翻訳）

> Pr(|角|< 罪−1(R−r)/x)=2Φ
> 罪−1(R−r)/x
> ログイン

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- Pr(|角|< 罪−1(R−r)/x)=2Φ 罪−1(R−r)/x ログイン

## Chunk 0524

### English（抽出4行）

> −1,
> where Φ is the cumulative normal distribution function. The only unknown parameter in this model
> is σ, the standard deviation of the distribution of shot angles.
> Fitting this model to the above data with a ﬂat prior on σ yields a posterior estimate ˆσ = 1.53◦

### 日本語訳（自動翻訳）

> −1、
> Φは累積的な正常な配分機能です。 このモデルで唯一の未知のパラメータ
> σ、ショットアングルの分布の標準的な偏差です。
> 上記のデータに、σの直前のフラットでこのモデルを合わせると、ポスター推定値が1.53◦になります。

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- −1、 Φは累積的な正常な配分機能です。

## Chunk 0525

### English（抽出4行）

> with standard error 0.02. Figure 27 shows the ﬁtted model, along with the logistic regression ﬁt
> earlier. The custom nonlinear model ﬁts the data much better. This is not to say that the model is
> perfect—any experience of golf will reveal that the angle is not the only factor determining whether
> the ball goes in the hole—but it seems like a useful start, and it demonstrates the advantages of

### 日本語訳（自動翻訳）

> 標準的な間違い 0.02 を使って。 図27は、ロジスティックの回帰適合性に合わせて、適合したモデルを示しています
> 早いです。 カスタム非線形モデルは、はるかに優れたデータに適合します。 モデルはモデルが
> 完璧な - ゴルフのあらゆる経験は、角度が唯一の要因であるかどうかを判断します
> ボールは穴の中を行くが、それは有用なスタートのように思える、そしてそれは利点を実証します

### 熟語・専門語

- **ESS**: 有効サンプルサイズ。自己相関を考慮した独立サンプル相当数。

### 要約

- 標準的な間違い 0.02 を使って。

## Chunk 0526

### English（抽出4行）

> building up a model directly rather than simply working with a conventional form.
> 10.3.
> Testing the fitted model on new data
> Several years after ﬁtting the above model, we were presented with a newer and more comprehensive

### 日本語訳（自動翻訳）

> 従来型ではなくモデルを直接構築する。
> 10.3。
> 新しいデータに装着したモデルのテスト
> 上記モデルを装着してから数年後、新品とより総合的に発表しました。

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- 従来型ではなくモデルを直接構築する。

## Chunk 0527

### English（抽出4行）

> dataset on professional golf putting (Broadie, 2018). For simplicity we just look here at the summary
> data, probabilities of the ball going into the hole for shots up to 75 feet from the hole. Figure 28
> these new data, along with our earlier dataset and the already-ﬁt geometry-based model from before,
> extending to the range of the new data.

### 日本語訳（自動翻訳）

> プロのゴルフパッティングに関するデータセット(2018年ブロードウェイ) シンプルさのために、我々はちょうどまとめを参照してください
> データ、穴から75フィートまでのショットのための穴に入るボールの確率。 図28
> これらの新しいデータ、以前のデータセットと、以前から既にフィットしたジオメトリベースのモデルとともに、
> 新しいデータの範囲に拡張します。

### 熟語・専門語

- **ESS**: 有効サンプルサイズ。自己相関を考慮した独立サンプル相当数。

### 要約

- プロのゴルフパッティングに関するデータセット(2018年ブロードウェイ) シンプルさのために、我々はちょうどまとめを参照してください データ、穴から75フィートまでのショットのための穴に入るボールの確率。

## Chunk 0528

### English（抽出4行）

> Comparing the two datasets in the range 0–20 feet, the success rate is similar for longer putts but
> is much higher than before for the short putts. This could be a measurement issue, if the distances
> Figure 28: Checking the already-ﬁt model to new golf putting data. At equivalent distances, the
> success rate is higher for the new data, which may represent improvement over time or just a

### 日本語訳（自動翻訳）

> 範囲0〜20フィートの2つのデータセットを比較すると、成功率は長いパットに似ていますが、
> ショートパットよりもはるかに高いです。 距離がかかると測定問題になる可能性があります。
> 図28:既にフィットしたモデルを新しいゴルフパッティングデータにチェック。 同等距離では、
> 成功率は、新しいデータにとってより高いです。これは、時間や時間だけの改善を表すことができます。

### 熟語・専門語

- **ESS**: 有効サンプルサイズ。自己相関を考慮した独立サンプル相当数。

### 要約

- 範囲0〜20フィートの2つのデータセットを比較すると、成功率は長いパットに似ていますが、 ショートパットよりもはるかに高いです。

## Chunk 0529

### English（抽出4行）

> diﬀerence in the datasets. In addition, the new data show a systematic model failure at higher
> distances, motivating a model improvement.
> to the hole are only approximate for the old data, and it could also be that golfers are better than
> they used to be.

### 日本語訳（自動翻訳）

> データセットの違い。 さらに、新しいデータは、より高価なモデルの故障を示す
> モデル改善をモチベーションする距離。
> ホールは、古いデータだけに近接し、ゴルファーがより優れている可能性がある
> それに使われる。

### 熟語・専門語

- **approximate**: 近似。速度や扱いやすさのため、正確な推論・モデルを緩めること。

### 要約

- データセットの違い。

## Chunk 0530

### English（抽出4行）

> Beyond 20 feet, the empirical success rates become lower than would be predicted by the old
> model. These are much more diﬃcult attempts, even after accounting for the increased angular
> precision required as distance goes up. In addition, the new data look smoother, which perhaps is
> a reﬂection of more comprehensive data collection.

### 日本語訳（自動翻訳）

> 20フィートを超えて、帝国の成功率は、古いによって予測されるよりも低くなります
> モデル。 これらは、増加した角度の会計後でさえ、はるかに困難な試みです
> 距離が上がるにつれて必要な精度。 さらに、新しいデータはスムーザーに見えます。
> より包括的なデータ収集の反射。

### 熟語・専門語

- **ESS**: 有効サンプルサイズ。自己相関を考慮した独立サンプル相当数。

### 要約

- 20フィートを超えて、帝国の成功率は、古いによって予測されるよりも低くなります モデル。

## Chunk 0531

### English（抽出4行）

> 10.4.
> A new model accounting for how hard the ball is hit
> To get the ball in the hole, the angle is not the only thing you need to control; you also need to hit
> the ball just hard enough.

### 日本語訳（自動翻訳）

> 10.4.
> ボールが打たれにくい新しいモデル
> 穴の球を得るためには、角度はあなたが制御する必要があるだけではありません。 また、ヒットする必要があります
> ボールは十分に困難です。

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- 10.4. ボールが打たれにくい新しいモデル 穴の球を得るためには、角度はあなたが制御する必要があるだけではありません。

## Chunk 0532

### English（抽出4行）

> Broadie (2018) added this to the geometric model by introducing another parameter corre-
> sponding to the golfer’s control over distance. Supposing u is the distance that golfer’s shot would
> travel if there were no hole, Broadie assumes that the putt will go in if (a) the angle allows the ball
> to go over the hole, and (b) u is in the range [x, x + 3]. That is the ball must be hit hard enough to

### 日本語訳（自動翻訳）

> Broadie (2018) は、別のパラメーターの相関を導入することで幾何学モデルにこれを追加しました。
> ゴルファーの走行距離を抑える スプポーズuは、ゴルファーのショットがする距離です
> 穴がなかったら旅行、ブロードイは、(a)角度がボールを可能にする場合、パットが行くと仮定します
> 穴を上に移動し、(b) u は範囲 [x, x + 3] にあります。 つまり、ボールは十分にハードに打つ必要があります

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- Broadie (2018) は、別のパラメーターの相関を導入することで幾何学モデルにこれを追加しました。

## Chunk 0533

### English（抽出4行）

> reach the whole but not go too far. Factor (a) is what we have considered earlier; we must now add
> factor (b).
> Figure 29 illustrates the need for the distance as well as the angle of the shot to be in some
> range, in this case the gray zone which represents the trajectories for which the ball would reach

### 日本語訳（自動翻訳）

> 全体に到達するが、あまりにも遠く行くことはありません。 Factor(a) は、以前に考慮したものです。 今度は追加しなければなりません
> 要因(b)。
> 図29は、距離やショットの角度の必要性をいくつか示します
> 範囲、この場合、ボールが到達する軌跡を表すグレーゾーン

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- 全体に到達するが、あまりにも遠く行くことはありません。

## Chunk 0534

### English（抽出4行）

> the hole and stay in it.
> Broadie supposes that a golfer will aim to hit the ball one foot past the hole but with a
> multiplicative error in the shot’s potential distance, so that u = (x + 1) · (1 + ϵ), where the error
> ϵ has a normal distribution with mean 0 and standard deviation σdistance. In statistics notation, this

### 日本語訳（自動翻訳）

> 穴をあけて、
> ブロードイは、ゴルファーが穴を過ぎてボール1足を打つことを目指していると仮定しますが、
> ショットの潜在的な距離における多重化エラー, その u = (x + 1) · (1 + ε), エラー
> ε は平均 0 および標準的な偏差のσdistance の正常な配分があります。 統計表記では、これは

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- 穴をあけて、 ブロードイは、ゴルファーが穴を過ぎてボール1足を打つことを目指していると仮定しますが、 ショットの潜在的な距離における多重化エラー, その u = (x + 1) · (1 + ε), エラー ε は平均 0 および標準…

## Chunk 0535

### English（抽出4行）

> Figure 29: Geometric model of golf putting, also including the constraint that the ball must be hit
> hard enough to reach the hole but not so hard that it hops over. Not to scale.
> model is, u ∼normal(x+1, (x+1)σdistance), and the distance is acceptable if u ∈[x, x+3], an event
> that has probability Φ

### 日本語訳（自動翻訳）

> 図29:ボールがヒットしなければならない制約を含むゴルフパッティングの幾何学的モデル
> 穴に到達するのに十分な硬いが、それが飛び越えるほど難しい。 スケールしない
> モデルは、u〜normal(x+1,(x+1)σdistance)で、u〜normal(x+1,(x+1)σdistance())で、u〜normal(x+1,(x+1)σdistance)で、u〜normal(x+1)σdistance(=============================================================================================================================================================================================
> 確率を持つこと Φ

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- 図29:ボールがヒットしなければならない制約を含むゴルフパッティングの幾何学的モデル 穴に到達するのに十分な硬いが、それが飛び越えるほど難しい。

## Chunk 0536

### English（抽出4行）

> 
> (x+1)σdistance
> 
> −Φ

### 日本語訳（自動翻訳）

> (x+1)σdistance
> ツイート

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- (x+1)σdistance ツイート

## Chunk 0537

### English（抽出4行）

> 
> −1
> (x+1)σdistance
> 

### 日本語訳（自動翻訳）

> −1
> (x+1)σdistance

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- −1 (x+1)σdistance

## Chunk 0538

### English（抽出4行）

> . Putting these together, the probability a
> shot goes in becomes,
> 
> 2Φ

### 日本語訳（自動翻訳）

> . これらを一緒に入れ、確率 a
> ショットは、
> 2インチ

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- . これらを一緒に入れ、確率 a ショットは、 2インチ

## Chunk 0539

### English（抽出4行）

> 
> sin−1((R−r)/x)
> σangle
> 

### 日本語訳（自動翻訳）

> 罪−1(R−r)/x
> ログイン

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- 罪−1(R−r)/x ログイン

## Chunk 0540

### English（抽出4行）

> −1
>  
> Φ
> 

### 日本語訳（自動翻訳）

> −1
> 仕様

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- −1 仕様

## Chunk 0541

### English（抽出4行）

> (x+1)σdistance
> 
> −Φ
> 

### 日本語訳（自動翻訳）

> (x+1)σdistance
> ツイート

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- (x+1)σdistance ツイート

## Chunk 0542

### English（抽出4行）

> −1
> (x+1)σdistance
> 
> , where

### 日本語訳（自動翻訳）

> −1
> (x+1)σdistance
> , どこ

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- −1 (x+1)σdistance , どこ

## Chunk 0543

### English（抽出4行）

> we have renamed the parameter σ from our earlier model to σangle to distinguish it from the new
> σdistance parameter.
> The result is a model with two parameters, σangle and σdistance. Even this improved geometry-
> based model is a gross oversimpliﬁcation of putting, and the average distances in the binned data

### 日本語訳（自動翻訳）

> 以前のモデルから σangle に改名し、新しいモデルから区別します。
> σdistance パラメータ。
> 結果は、2つのパラメータ、角、およびσdistance のモデルです。 この改良された幾何学でも-
> ベースモデルは、パッティングの過小化と、埋め込まれたデータの平均距離です。

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- 以前のモデルから σangle に改名し、新しいモデルから区別します。

## Chunk 0544

### English（抽出4行）

> are not the exact distances for each shot. But it should be an advance on the earlier one-parameter
> model; the next step is to see how it ﬁts the data.
> We ﬁrst try to ﬁt this model with ﬂat priors, but the result is computationally unstable, so we
> assign weakly informative half-normal(0, 1) priors. Even after this, we have poor convergence.

### 日本語訳（自動翻訳）

> 各ショットの正確な距離ではありません。 しかし、それは以前の1パラメータに先立ってする必要があります
> モデル;次のステップは、それがデータに合う方法を見ることです。
> まずは、このモデルをフラットな先物と合わせようとしますが、結果は計算的に不安定なので、
> 弱く非公式なハーフノーマル(0, 1) 前記を割り当てます。 この後も、不寛大さを抱えています。

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- 各ショットの正確な距離ではありません。

## Chunk 0545

### English（抽出4行）

> Running 4 chains, each with 2000 iterations, yields high values of bR, indicating poor mixing and
> making us concerned about the model, following the folk theorem (see Section 5.1).
> In this case, rather than examining traceplots and otherwise studying the pathologies of the
> Markov chain simulation, we just directly to examine the ﬁt of the model, as estimated using the

### 日本語訳（自動翻訳）

> ランニング4チェーン、それぞれ2000の反復、貧しい混合を示すbRの高い値、および
> 民俗的な理論(セクション5.1参照)に従うモデルについて私達を心配させます。
> この場合、トレースプロットを調べるのではなく、それ以外の場合の病理を研究する
> Markovのチェーン シミュレーション、私達はモデルの適合を、推定使用と見なすように直接調べます

### 熟語・専門語

- **Markov chain**: マルコフ連鎖。MCMCで事後分布からサンプルを得るための確率過程。

### 要約

- ランニング4チェーン、それぞれ2000の反復、貧しい混合を示すbRの高い値、および 民俗的な理論(セクション5.1参照)に従うモデルについて私達を心配させます。

## Chunk 0546

### English（抽出4行）

> crude estimates of the parameters obtained by averaging the simulations over the poorly-mixing
> chains.
> Figure 30a shows the result. The overall ﬁt is not terrible, but there are problems in the middle
> of the curve, and after some thought we realized that the model is struggling because the binomial

### 日本語訳（自動翻訳）

> crude は、微小混合の上でシミュレーションを平均化することによって得られるパラメータの推定値
> チェーン。
> 図30aは結果を表示します。 全体的な適合はひどくありませんが、中間に問題があります
> カーブのあとは、モデルがボナミアルだから苦労していることに気付きました。

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- crude は、微小混合の上でシミュレーションを平均化することによって得られるパラメータの推定値 チェーン。

## Chunk 0547

### English（抽出4行）

> likelihood is constraining it too strongly at the upper left part of the curve where the counts are
> higher. Look at how closely the ﬁtted curve hugs the data at the very lowest values of x.
> Figure 30b displays the data, which was given to us in binned form, for putts from the shortest
> distances. Because of the vary large sample sizes, the binomial model tries very hard to ﬁt these

### 日本語訳（自動翻訳）

> 好適性は数がであるカーブの上部の左部分でそれを余りに強く禁忌です
> 高い。 フィットした曲線がxの非常に低い値でデータを抱く方法を見てください。
> 図30bは、最小限の小文字から小文字の小文字の小文字の小文字の小文字の小文字の小文字の小文字の小文字の小文字の小文字の小文字の小文字の小文字の小文字の小文字の小文字の小文字の小文字の小文字の小文字の小文字の小文字の小文字の小文字の小文字の小文字の小文字の小文字の小文字の小文字の小文字の小文字の小文字と小文字の小文字の小文字の小文字の小文字の小文字の小文字の小文字の小文字の小文字の小文字の小文字の小文字の小文字の小文字の小文字の小文字の小文字の小文字の小文字の小文字の小文字の小文字の小文字の小文字の小文字の小文字の小文字の小文字の小文字の小文字の小文字の小文字の小文字の小文字の小文字の小文字の小文字の小文字の小文字の小文字の小文字の小文字の小文字の小文字の小文字の小文字の小文字
> 距離。 さまざまな大きなサンプルサイズのため、ビンオミアルモデルはこれらに合うように非常に困難をしようとします

### 熟語・専門語

- **likelihood**: 尤度。パラメータが与えられたときデータがどれだけ起こりやすいか。

### 要約

- 好適性は数がであるカーブの上部の左部分でそれを余りに強く禁忌です 高い。

## Chunk 0548

### English（抽出4行）

> probabilities as exactly as possible. The likelihood function gives by far its biggest weight to these
> ﬁrst few data points. If we were sure the model was correct, this would be the right thing to do, but
> given inevitable model error, the result is a problematic ﬁt to the entire curve. In addition, the poor
> MCMC convergence is understandable: there are no parameter values that ﬁt all the data, and it is

### 日本語訳（自動翻訳）

> できるだけ正確に能力。 このような機能により、これらに最も大きな重量を与えます
> 最初のデータポイント数。 もしモデルが正しいと確信していたら、これは正しいことですが、
> 必然的なモデルの間違いを与えられた、結果はカーブ全体に問題のある適合です。 加えて、貧しい
> MCMCのconvergenceは理解可能です:すべてのデータに合うパラメータ値はありません。

### 熟語・専門語

- **likelihood**: 尤度。パラメータが与えられたときデータがどれだけ起こりやすいか。

### 要約

- できるだけ正確に能力。

## Chunk 0549

### English（抽出4行）

> diﬃcult for the chains to move smoothly between values that ﬁt the bulk of the data and those that
> ﬁt the ﬁrst few data points.
> 10.5.
> Expanding the model by including a fudge factor

### 日本語訳（自動翻訳）

> チェーンがデータの大きさやその値に収まる値間で円滑に動くのが難しい
> 最初のデータポイントに収まる。
> 10.5。
> 汚泥因子を含むモデルの拡大

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- チェーンがデータの大きさやその値に収まる値間で円滑に動くのが難しい 最初のデータポイントに収まる。

## Chunk 0550

### English（抽出4行）

> As the data are binned, the individual putt distances have been rounded to the bin center values,
> which has the biggest eﬀect in very short distances. We could incorporate a rounding error model
> x
> n

### 日本語訳（自動翻訳）

> データを埋め込むと、個々のパット距離がビンの中心値に丸められ、
> 非常に短い間隔で最大の効果がある。 ラウンドエラーモデルを組み込むことができます
> ツイート
> ログイン

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- データを埋め込むと、個々のパット距離がビンの中心値に丸められ、 非常に短い間隔で最大の効果がある。

## Chunk 0551

### English（抽出4行）

> y
> 0.28
> 0.97
> 1.93

### 日本語訳（自動翻訳）

> ログイン
> 0.28の
> 0.97の
> 1.93号

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- ログイン 0.28の 0.97の 1.93号

## Chunk 0552

### English（抽出4行）

> 2.92
> 3.93
> . . .
> . . .

### 日本語訳（自動翻訳）

> 2.92
> 3.93号
> . . .
> . . .

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- 2.92 3.93号 . . . . . .

## Chunk 0553

### English（抽出4行）

> . . .
> Figure 30: Working to understand the poor convergence of the expanded golf putting model that
> had showed poor convergence. (a) A graph of data and ﬁtted model reveals problems with the
> ﬁt near the middle of the curve, and we realized that the poor behavior of the Markov simulation

### 日本語訳（自動翻訳）

> . . .
> 図30:拡張されたゴルフパッティングモデルの悪い収斂を理解するための作業
> 不寛容さが認められた。(a) データと適合したモデルのグラフは、問題を明らかにする
> カーブの中央付近に収まり、Markovのシミュレーションの悪い動作に気付いた

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- . . . 図30:拡張されたゴルフパッティングモデルの悪い収斂を理解するための作業 不寛容さが認められた。

## Chunk 0554

### English（抽出4行）

> arose from the model trying too hard to ﬁt the data at the upper left of the curve. (b) Data for putts
> from the shortest distances, with x being the average distance for the putts in each bin (presumably
> 0–0.5 feet, 0.5–1.5 feet, 1.5–2.5, etc.). Sample sizes are very large in the initial bins, hence the
> binomial model tries to ﬁt these points nearly exactly.

### 日本語訳（自動翻訳）

> カーブの左上にあるデータに収まるのが難しいモデルからアローズ。 (b) パットのデータ
> 最短距離から、x は各ビンのパットの平均距離(おそらく
> 0〜0.5フィート、0.5〜1.5フィート、1.5〜2.5インチなど。 サンプル サイズは初期のビンで非常に大きいです、従って
> binomialモデルは、これらのポイントをほぼ正確にフィットしようとします。

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- カーブの左上にあるデータに収まるのが難しいモデルからアローズ。

## Chunk 0555

### English（抽出4行）

> for the putting distances, but we opt for a simpler error model. To allow for a model that can ﬁt
> reasonably well to all the data without being required to have a hyper-precise ﬁt to the data at the
> shortest distances, we took the data model, yj ∼binomial(nj, pj), and added an independent error
> term to each observation. There is no easy way to add error directly to the binomial distribution—

### 日本語訳（自動翻訳）

> 設定距離のため、単純なエラーモデルを選択します。 フィットするモデルを可能にするため
> データを高価に収まる必要のないすべてのデータに合理的に十分
> 最短距離で、データモデル、yj〜binomial(nj、pj)を取り、独立したエラーを追加
> 各観察の用語 バイナリ分布に直接エラーを追加する簡単な方法はありません。

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- 設定距離のため、単純なエラーモデルを選択します。

## Chunk 0556

### English（抽出4行）

> we could replace it with its overdispersed generalization, the beta-binomial, but this would not be
> appropriate here because the variance for each data point j would still be roughly proportional to
> the sample size nj, and our whole point here is to get away from that assumption and allow for
> model misspeciﬁcation—so instead we ﬁrst approximate the binomial data distribution by a normal

### 日本語訳（自動翻訳）

> 分散型一般化、β-binomial に置き換えることができましたが、これはそうではありません
> 各データポイント j の variance が大まかに比例するので、ここで適切です。
> サンプルサイズnj、およびここに私達の全ポイントは仮定から離れ、許可します
> モデルの誤差 - つまり、最初は通常のバイナリデータ分布を近似します

### 熟語・専門語

- **approximate**: 近似。速度や扱いやすさのため、正確な推論・モデルを緩めること。

### 要約

- 分散型一般化、β-binomial に置き換えることができましたが、これはそうではありません 各データポイント j の variance が大まかに比例するので、ここで適切です。

## Chunk 0557

### English（抽出4行）

> and then add independent variance; thus:
> yj/nj ∼normal
> 
> pj,

### 日本語訳（自動翻訳）

> そして独立した分散を加えて下さい;従って:
> yj/nj〜normal(通常)
> pj,

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- そして独立した分散を加えて下さい;従って: yj/nj〜normal(通常) pj,

## Chunk 0558

### English（抽出4行）

> q
> pj(1 −pj)/nj + σ2
> y
> 

### 日本語訳（自動翻訳）

> お問い合わせ
> pj(1 −pj)/nj + σ2
> ログイン

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- お問い合わせ pj(1 −pj)/nj + σ2 ログイン

## Chunk 0559

### English（抽出4行）

> .
> This model has its own problems and would fall apart if the counts in any cell were small enough,
> but it is transparent and easy to set up and code, and so we try it out, with the understanding that
> we can clean it up later on if necessary.

### 日本語訳（自動翻訳）

> . .
> このモデルは独自の問題を持っており、任意のセルのカウントが十分に小さい場合は、落ちるだろう、
> しかし、それは透明で設定しやすく、コード化しやすいので、それを試してみましょう。
> 必要であれば後日清掃できます。

### 熟語・専門語

- **ESS**: 有効サンプルサイズ。自己相関を考慮した独立サンプル相当数。

### 要約

- . . このモデルは独自の問題を持っており、任意のセルのカウントが十分に小さい場合は、落ちるだろう、 しかし、それは透明で設定しやすく、コード化しやすいので、それを試してみましょう。

## Chunk 0560

### English（抽出4行）

> After assigning independent half-normal(0, 1) priors to all three parameters of this new model,
> it ﬁts with no problem in Stan, yielding the posterior mean estimates σangle = 1.02◦, σdistance = 0.08
> (implying that shots can be hit to an uncertainty of about 8% in distance), and σy = 0.003 (implying
> that the geometric model sketched in ﬁgure 29 ﬁts the aggregate success rate as a function of distance

### 日本語訳（自動翻訳）

> この新しいモデルのすべての3つのパラメーターの前に独立した半常(0、1)を割り当てた後、
> スタンで問題なくフィットし、ポスターの平均推定のσangle = 1.02◦、σdistance = 0.08
> (距離の約8%の不確実性に打撃を打つことができること)、およびσy = 0.003 (即ち
> 図29でスケッチされた幾何学モデルが、距離の関数として集計成功率に合うこと

### 熟語・専門語

- **ESS**: 有効サンプルサイズ。自己相関を考慮した独立サンプル相当数。
- **uncertainty**: 不確実性。観測・パラメータ・モデル構造・意思決定に残る曖昧さ。

### 要約

- この新しいモデルのすべての3つのパラメーターの前に独立した半常(0、1)を割り当てた後、 スタンで問題なくフィットし、ポスターの平均推定のσangle = 1.02◦、σdistance = 0.08 (距離の約8%の不確実性に打撃を…

## Chunk 0561

### English（抽出4行）

> to an accuracy of 0.3 percentage points).
> Figure 31: (a) With the additional error term added, the model sketched in Figure 29 provides an
> excellent ﬁt to the expanded golf putting data. (b) The residuals from the ﬁtted model are small and
> show no pattern, thus we see no obvious directions of improvement at this point.

### 日本語訳（自動翻訳）

> 0.3パーセントポイントの精度に。
> 図31:(a) 追加エラーの期間を追加したと、図29でスケッチしたモデルは、
> 拡張されたゴルフパッティングデータに優れたフィット。(b) 装着したモデルの残留物は小さく、
> パターンがないので、この点で改善の明らかな指示は見ません。

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- 0.3パーセントポイントの精度に。

## Chunk 0562

### English（抽出4行）

> Figure 31 shows the ﬁtted model and the residuals, yj/nj −ˆpj, as a function of distance. The ﬁt
> is good, and the residuals show no strong pattern, also they are low in absolute value—the model
> predicts the success rate to within half a percentage point at most distances, suggesting not that the
> model is perfect but that there are no clear ways to develop it further just given the current data.

### 日本語訳（自動翻訳）

> 図31は、適合したモデルと残留物、yj/nj −pj、距離の関数として示します。 フィット
> よい、残留物は強いパターンを、また絶対値の低い示しませんモデル示します
> ほとんどの距離で半分のパーセンテージポイントに成功率を予測します。
> モデルは完璧ですが、現在のデータだけを与えられただけで、それを開発するための明確な方法はありません。

### 熟語・専門語

- **ESS**: 有効サンプルサイズ。自己相関を考慮した独立サンプル相当数。

### 要約

- 図31は、適合したモデルと残留物、yj/nj −pj、距離の関数として示します。

## Chunk 0563

### English（抽出4行）

> There are various ways the model could be improved, most obviously by breaking down the
> data and allowing the two parameters to vary by golfer, hole, and weather conditions. As discussed
> earlier, a key motivation for model expansion is to allow the inclusion of more data, in this case
> classifying who was taking the shot and where.

### 日本語訳（自動翻訳）

> モデルが改善されることができるさまざまな方法があります、最も明らかに破壊することによって
> 2つのパラメータがゴルファー、穴、気象条件によって異なるようにデータと可能。 議論として
> 以前は、モデル拡張のための重要なモチベーションは、この場合、より多くのデータを含めることを可能にすることです
> 誰が撮影したか、どこを撮影したかを分類する。

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- モデルが改善されることができるさまざまな方法があります、最も明らかに破壊することによって 2つのパラメータがゴルファー、穴、気象条件によって異なるようにデータと可能。

## Chunk 0564

### English（抽出4行）

> 10.6.
> General lessons from the golf example
> This was an appealing example in that a simple one-parameter model ﬁt the initial dataset, and then
> the new data were ﬁt by adding just one more parameter to capture uncertainty in distance as well

### 日本語訳（自動翻訳）

> 10月6日
> ゴルフのレッスン例
> これは、単純な1パラメータモデルが初期データセットに収まるという魅力的な例でした。
> 新しいデータは、距離の不確実性を捉えるために複数のパラメータを追加することによって適合しました

### 熟語・専門語

- **ESS**: 有効サンプルサイズ。自己相関を考慮した独立サンプル相当数。
- **uncertainty**: 不確実性。観測・パラメータ・モデル構造・意思決定に残る曖昧さ。

### 要約

- 10月6日 ゴルフのレッスン例 これは、単純な1パラメータモデルが初期データセットに収まるという魅力的な例でした。

## Chunk 0565

### English（抽出4行）

> as angle of the shot. A notable feature of the model expansion was that the binomial likelihood
> was too strong and made it diﬃcult for the new model to ﬁt all the data at once. Such problems
> of stickiness—which appear in the computation as well as with the inference—are implicit in any
> Bayesian model, but they can become more prominent when as sample size increases.

### 日本語訳（自動翻訳）

> ショットの角度として。 モデル拡張の注目すべき特徴は、binomial likelihoodでした
> 新しいモデルが一度にすべてのデータを収まるのが難しかったです。 このような問題
> 複雑さ - 計算だけでなく、推論で現れる - 任意の
> ベイジアンモデルですが、サンプルサイズが増加するとより顕著になることができます。

### 熟語・専門語

- **likelihood**: 尤度。パラメータが与えられたときデータがどれだけ起こりやすいか。
- **ESS**: 有効サンプルサイズ。自己相関を考慮した独立サンプル相当数。

### 要約

- ショットの角度として。

## Chunk 0566

### English（抽出4行）

> This is an example of the general principle that bigger data need bigger models. In this case, we
> expanded our second model by adding an error term which had no underlying golf interpretation,
> but allowed the model to ﬂexibly ﬁt the data. This is similar to how, in a multi-center trial, we
> might allow the treatment eﬀect to vary by area, even if we are not particularly interested in this

### 日本語訳（自動翻訳）

> より大きなデータを必要とする一般的な原則の例です。 この場合、
> 基礎的なゴルフ解釈がなかった間違いの規定を加えることによって私達の第2モデルを拡大して下さい、
> しかし、モデルがデータを柔軟に収まるように許可しました。 これは、マルチセンタートライアルで、どのように似ています。
> 特に興味を起こさない場合でも、治療効果が地域によって変化する可能性がある

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- より大きなデータを必要とする一般的な原則の例です。

## Chunk 0567

### English（抽出4行）

> variation, just because this can capture otherwise unexplained aspects of the data, and it is also
> similar to the idea in classical analysis of variance of including a fully saturated interaction term to
> represent residual error.
> The golf example also illustrates the way that inferences from a sequence of models can be

### 日本語訳（自動翻訳）

> バリエーションは、データの不明確な側面をキャプチャできるだけでなく、
> 十分に飽和された相互作用の用語を含む分散の古典的な分析の考えに類似
> 残留エラーを表します。
> ゴルフの例では、モデルのシーケンスから推論する方法も説明しています。

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- バリエーションは、データの不明確な側面をキャプチャできるだけでなく、 十分に飽和された相互作用の用語を含む分散の古典的な分析の考えに類似 残留エラーを表します。

## Chunk 0568

### English（抽出4行）

> compared, both by graphing predictions along with data and by studying the way that parameter
> estimates change as the model is expanded. For example, when we add uncertainty in the distance
> of the shot, our estimate of the angular uncertainty decreases. Finally, we recognize that even the
> ﬁnal ﬁtted model is a work in progress, and so we want to work in a probabilistic programming

### 日本語訳（自動翻訳）

> 比較し、データとともに予測をグラフ化し、そのパラメータを調べることにより
> 機種変更に伴い、機種変更を見積もります。 例えば、距離に不確実性を加えるとき
> 被写体では、角度の不確実性が低下します。 ついに、さらには、
> 最終装着モデルは進行中の作業なので、確率的プログラミングで作業したい

### 熟語・専門語

- **probabilistic programming**: 確率的プログラミング。Stanなどで確率モデルをコードとして記述し推論する方法。
- **ESS**: 有効サンプルサイズ。自己相関を考慮した独立サンプル相当数。
- **uncertainty**: 不確実性。観測・パラメータ・モデル構造・意思決定に残る曖昧さ。
- **prediction**: 予測。未知/将来/除外データに対する分布や点推定。

### 要約

- 比較し、データとともに予測をグラフ化し、そのパラメータを調べることにより 機種変更に伴い、機種変更を見積もります。

## Chunk 0569

### English（抽出4行）

> environment where we can expand it by allowing the parameters to vary by player and condition of
> the course.
> 11.
> Example of workflow for a model with unexpected multimodality: Planetary

### 日本語訳（自動翻訳）

> パラメータがプレイヤーや条件によって変化することを可能にすることで展開できる環境
> コース。
> 11月11日
> 予期しない多項性を持つモデルのワークフローの例: 惑星

### 熟語・専門語

- **multimodality**: 多峰性。事後分布に複数の山があり、MCMCが混合しにくい状態。
- **workflow**: ワークフロー。実務分析の反復手順全体。

### 要約

- パラメータがプレイヤーや条件によって変化することを可能にすることで展開できる環境 コース。

## Chunk 0570

### English（抽出4行）

> motion
> The previous example was relatively straightforward in that we built a model and gradually improved
> it. Next we consider a case study in which we start with a complicated model, encounter problems
> with our inference, and have to ﬁgure out what is going on.

### 日本語訳（自動翻訳）

> アクション
> 以前の例は、モデルをビルドし、徐々に改善したということで比較的簡単です。
> お問い合わせ 次に、複雑なモデルから始まるケーススタディを考え、問題に遭遇
> わたしたちの推論で、何が起こっているのかを把握しなければなりません。

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- アクション 以前の例は、モデルをビルドし、徐々に改善したということで比較的簡単です。

## Chunk 0571

### English（抽出4行）

> Section 3.4 alludes to measurements of a planet’s motion. Let us now investigate this example
> from a slightly diﬀerent perspective. While simple in appearance, this problem illustrates many
> of the concepts we have discussed and highlights that the workﬂow draws on both statistical and
> ﬁeld expertise. It also cautions us that the workﬂow is not an automated process; each step requires

### 日本語訳（自動翻訳）

> 3.4節は、惑星の動きの測定に全力を尽くします。 この例を調べる
> 少し違った視点から。 見た目が単純ですが、この問題は多くのことを示しています
> 我々が議論し、ワークフローが統計的に描画し、強調した概念の
> フィールドの専門知識。 また、ワークフローが自動化されたプロセスではないことを警告します。各ステップは必要です

### 熟語・専門語

- **ESS**: 有効サンプルサイズ。自己相関を考慮した独立サンプル相当数。

### 要約

- 3.4節は、惑星の動きの測定に全力を尽くします。

## Chunk 0572

### English（抽出4行）

> careful reasoning. For many problems we have encountered ﬁnding the right visualization tools
> is often the key to understand our model, its limitations, and how to improve it. This example is
> no exception. We monitor various intermediate quantities as prescribed in Section 5.4, and make
> extensive use of predictive checks (Sections 2.4 and 6.1).

### 日本語訳（自動翻訳）

> 注意すべき理由 多くの問題に対して、正しい視覚化ツールを見つけ出しました
> 多くの場合、当社のモデル、その制限、およびそれを改善する方法を理解するための鍵です。 この例は
> 例外はありません。 セクション5.4で規定されているように、さまざまな中間量を監視し、
> 予測チェックの広範な使用 (セクション 2.4 と 6.1).

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- 注意すべき理由 多くの問題に対して、正しい視覚化ツールを見つけ出しました 多くの場合、当社のモデル、その制限、およびそれを改善する方法を理解するための鍵です。

## Chunk 0573

### English（抽出4行）

> 11.1.
> Mechanistic model of motion
> Instead of ﬁtting an ellipse, we use a mechanistic model based on elementary notions of classical
> mechanics. This allows us to estimate quantities of physical interest, such as stellar mass, and more

### 日本語訳（自動翻訳）

> 11月11日
> モーションのメカニスティックモデル
> 楕円をフィッティングする代わりに、古典的概念に基づいて機械的なモデルを使用します
> メカニクス。 これは、ステラ質量などの物理的興味の量を推定することができます。

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- 11月11日 モーションのメカニスティックモデル 楕円をフィッティングする代わりに、古典的概念に基づいて機械的なモデルを使用します メカニクス。

## Chunk 0574

### English（抽出4行）

> readily apply domain knowledge, as well as track the planet’s trajectory in space and time.
> We can describe the planet’s motion using Newton’s laws, which is a second-order diﬀerential
> equation or equivalently a system of two ﬁrst-order diﬀerential equations, which yields Hamilton’s
> formulation:

### 日本語訳（自動翻訳）

> ドメインの知識をすぐに適用し、宇宙や時間に惑星の軌跡を追跡します。
> ニュートンの法則を用いて地球の動きを記述することができます。
> 同等に、Hamilton の 2 の第一次差分程式のシステム、
> 処方:

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- ドメインの知識をすぐに適用し、宇宙や時間に惑星の軌跡を追跡します。

## Chunk 0575

### English（抽出4行）

> dq
> dt
> =
> p

### 日本語訳（自動翻訳）

> ログイン
> ログイン
> パスワード
> お問い合わせ

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- ログイン ログイン パスワード お問い合わせ

## Chunk 0576

### English（抽出4行）

> m
> dp
> dt
> =

### 日本語訳（自動翻訳）

> m 点
> ログイン
> ログイン
> パスワード

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- m 点 ログイン ログイン パスワード

## Chunk 0577

### English（抽出4行）

> −k
> r3(q −q∗),
> where
> • q(t) is the planet’s position vector over time,

### 日本語訳（自動翻訳）

> ツイート
> r3(q-q **),
> アクセス
> • q(t) は、惑星の位置ベクトルを時間とともに上回っています。

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- ツイート r3(q-q **), アクセス • q(t) は、惑星の位置ベクトルを時間とともに上回っています。

## Chunk 0578

### English（抽出4行）

> • p(t) is the planet’s momentum vector over time,
> • m is the planet’s mass (assumed to be 1 in some units),
> • k = GmM, with G = 10−3, the gravitational constant in the appropriate units, and M the
> stellar mass; hence k = 10−3M,

### 日本語訳（自動翻訳）

> •p(t)は、惑星の勢いのベクトルを時間とともに、
> •mは惑星の固まりです(ある単位の1つであると仮定される)、
> • k = GmM、G = 10−3、適切な単位の重力定数、M
> ステラー質量; ヒース k = 10-3M,

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- •p(t)は、惑星の勢いのベクトルを時間とともに、 •mは惑星の固まりです(ある単位の1つであると仮定される)、 • k = GmM、G = 10−3、適切な単位の重力定数、M ステラー質量; ヒース k = 10-3M,

## Chunk 0579

### English（抽出4行）

> • and r =
> p
> (q −q∗)T(q −q∗) is the distance between the planet and the star, with q∗denoting
> the star’s position (assumed to be ﬁxed).

### 日本語訳（自動翻訳）

> • と r =
> お問い合わせ
> (q-q•)T(q-q•)は、q *デノッティングで、惑星と星の間の距離です。
> 星の位置(固定されると仮定される)。

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- • と r = お問い合わせ (q-q•)T(q-q•)は、q *デノッティングで、惑星と星の間の距離です。

## Chunk 0580

### English（抽出4行）

> The planet moves on a plane, hence p and q are each vectors of length 2. The diﬀerential equations
> tell us that the change in position is determined by the planet’s momentum and that the change in
> momentum is itself driven by gravity.
> We would like to infer the gravitational force between the star and the planet, and in particular

### 日本語訳（自動翻訳）

> 惑星は平面に移動し、pとqは長さ2の各ベクトルです。 差分式
> 位置の変化は、惑星の勢力によって決定され、変化が変化していることを私たちに伝えます
> 重力によって運動量はそれ自体運転されます。
> 星と惑星の間を重力で侵入し、特に

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- 惑星は平面に移動し、pとqは長さ2の各ベクトルです。

## Chunk 0581

### English（抽出4行）

> the latent variable k. Other latent variables include the initial position and momentum of the
> planet, respectively q0 and p0, the subsequent positions of the planet, q(t), and the position of the
> star, q∗. Realistically, an astronomer would use cylindrical coordinates but for simplicity we stick
> to Cartesian coordinates. We record the planet’s position over regular time intervals, and assume

### 日本語訳（自動翻訳）

> 潜在変数 k. その他のラテン変数には、初期位置とモーメントの初期値が含まれます。
> 惑星、それぞれq0とp0、惑星、q(t)のその後の位置、および
> star, q **. リアルに, アストロンマーは、円筒座標を使用しますが、単純性のために、我々はスティック
> カルチェシアン座標に。 惑星の位置を定期的に記録し、想定

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- 潜在変数 k. その他のラテン変数には、初期位置とモーメントの初期値が含まれます。

## Chunk 0582

### English（抽出4行）

> measurements qobs,1, . . . , qobs,n at times t1, . . . , tn, where each observation qobs,i is two-dimensional
> with independent normally distributed errors,
> qobs,i ∼N2(q(ti), σ2I).
> We follow our general workﬂow and ﬁt the model using fake data to see if we can recover the

### 日本語訳（自動翻訳）

> 測定 qobs,1, . . , qobs,n 時 t1, . , tn, 各観察 qobs,i は二次元
> 独立した普通分散された間違いを使って、
> qobs、i〜N2(q(ti)、σ2I)。
> 一般的なワークフローをフォローし、偽データを使用してモデルにフィットして復元できるかどうかを確認します。

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- 測定 qobs,1, . . , qobs,n 時 t1, . , tn, 各観察 qobs,i は二次元 独立した普通分散された間違いを使って、 qobs、i〜N2(q(ti)、σ2I)。

## Chunk 0583

### English（抽出4行）

> assumed parameter values. We run an MCMC sampler for this model with Stan, which supports a
> numerical ordinary diﬀerential equation (ODE) solver. A ﬁrst attempt fails dramatically: the chains
> do not converge and take a long time to run. This is an invitation to start with a simpler model,
> again working in the controlled setting oﬀered by simulated data, where we know the true value of

### 日本語訳（自動翻訳）

> 想定されるパラメータ値。 このモデルのMCMCサンプラーをスタンで実行し、
> 数値通常の差動式(ODE)ソルバー。 最初の試みは劇的に失敗します:チェーン
> 長時間走って走るのは無理ではありません。 よりシンプルなモデルで始めるための招待状です。
> シミュレートされたデータによって提供される制御された設定で、私達が本当の価値を知っています

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- 想定されるパラメータ値。

## Chunk 0584

### English（抽出4行）

> each parameter.
> 11.2.
> Fitting a simplified model
> Ideally, we would ﬁnd a simpliﬁcation which is more manageable but still demonstrates the

### 日本語訳（自動翻訳）

> 各パラメータ。
> 11.2.
> 単純化されたモデルに適合
> 理想的には、より管理可能なが、まだ実証する単純化が見つかります

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- 各パラメータ。

## Chunk 0585

### English（抽出4行）

> issues our algorithm encounters.
> Our ﬁrst simpliﬁed model only estimates k, with prior
> k ∼normal+(0, 1), and an assumed true value of k = 1. We set the other parameters of the
> model at m = 1, q∗= (0, 0), q0 = (1, 0), and p0 = (0, 1). Since the parameter space is 1-

### 日本語訳（自動翻訳）

> アルゴリズムが発生した問題。
> 最初に単純化されたモデルは、事前にkを推定するだけです。
> k 〜normal+(0, 1) および k = 1. の真の値を想定した。 その他のパラメータを設定
> m = 1, q•= (0, 0), q0 = (1, 0), p0 = (0, 1). パラメータ空間は1～

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- アルゴリズムが発生した問題。

## Chunk 0586

### English（抽出4行）

> dimensional, we can compute the posterior distribution using quadrature; nevertheless we use
> MCMC, because our goal is to understand the challenges that frustrate our sampling algorithm.
> We run 8 chains, each with 500 iterations for the warmup phase and 500 more for the sampling
> phase, and we see:

### 日本語訳（自動翻訳）

> 寸法は、我々は量子を使用してポスター分布を計算することができます。 それにもかかわらず、我々は使用
> MCMCは、サンプリングアルゴリズムを不満させる課題を理解することです。
> 8つのチェーンを、それぞれ500の反復と500以上のサンプリングを実行します。
> フェーズ、および私達は見ます:

### 熟語・専門語

- **posterior distribution**: 事後分布。データ観測後の未知量の不確実性を表す分布。
- **ESS**: 有効サンプルサイズ。自己相関を考慮した独立サンプル相当数。

### 要約

- 寸法は、我々は量子を使用してポスター分布を計算することができます。

## Chunk 0587

### English（抽出4行）

> • The run time varies widely between chains, ranging from ∼2 seconds to ∼2000 seconds.
> While not necessarily a concern in itself, this indicates the chains are behaving in substantially
> diﬀerent ways.
> • bR for some parameters are large, implying that the chains have not mixed. Typically, we are

### 日本語訳（自動翻訳）

> ・2秒〜2秒〜2000秒の範囲で、チェーン間での走行時間は大きく異なります。
> 必ずしもそれ自体に関心がないので、これはチェーンが大幅に節約されていることを示しています
> さまざまな方法。
> • いくつかのパラメータのbRは大きく、チェーンが混合されていないことを暗示しています。 通常、私達はあります

### 熟語・専門語

- **ESS**: 有効サンプルサイズ。自己相関を考慮した独立サンプル相当数。

### 要約

- ・2秒〜2秒〜2000秒の範囲で、チェーン間での走行時間は大きく異なります。

## Chunk 0588

### English（抽出4行）

> comfortable with bR < 1.01. When bR > 2, this is an indication that the chains are not mixing
> well.
> Faced with these issues, we examine the traceplots (Figure 32). The chains seem to be stuck at
> local modes and do not cohesively explore the posterior space. Some chains have much lower log

### 日本語訳（自動翻訳）

> bR < 1.01 で快適に。 bR >2の場合、チェーンが混入していないことを示す
> お問い合わせ
> これらの問題に直面して、トレースプロット(図32)を調べます。 チェーンは立ち止まっているようです
> 局所的なモードをし、ポスター空間を凝らして探索しません。 一部のチェーンでは、はるかに低いログがあります

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- bR < 1.01 で快適に。

## Chunk 0589

### English（抽出4行）

> posterior densities than others. When doing posterior predictive checks for these chains speciﬁcally,
> we ﬁnd that the simulated data does not agree with the observations. For reasons we will uncover,
> the chains with the lowest log posterior and highest k also turn out to be the ones with the longest
> run times. Departing from Stan’s defaults, we also plot iterations during the warmup phase. The

### 日本語訳（自動翻訳）

> 他の人よりもポスターの密度. 特にこれらのチェーンの予測チェックを行うとき,
> シミュレーションされたデータは、観察に合意しないと見つかります。 私たちが発見する理由のために、
> 最も低いログのポスターおよび最も高いkの鎖はまた最長のものであることに向けます
> 実行時間。 Stanのデフォルトから出発し、ウォームアップフェーズ中に反復をプロットします。 ザ・オブ・ザ・

### 熟語・専門語

- **posterior predictive**: 事後予測。推定後のモデルが観測データの特徴を再現できるかを見る診断。

### 要約

- 他の人よりもポスターの密度. 特にこれらのチェーンの予測チェックを行うとき, シミュレーションされたデータは、観察に合意しないと見つかります。

## Chunk 0590

### English（抽出4行）

> plot now clearly indicates that which mode each chain converges to is determined by its initial value,
> suggesting these modes are strongly attractive for the Markov chain. This is an important practical
> log−posterior
> k

### 日本語訳（自動翻訳）

> プロットは現在、各チェーンコンバージが初期値で決定するモードであることを明確に示しています。
> これらのモードを提案することは、Markovチェーンにとって非常に魅力的です。 これは重要な実用的です
> log-posterior(ログ)
> ログイン

### 熟語・専門語

- **Markov chain**: マルコフ連鎖。MCMCで事後分布からサンプルを得るための確率過程。

### 要約

- プロットは現在、各チェーンコンバージが初期値で決定するモードであることを明確に示しています。

## Chunk 0591

### English（抽出4行）

> −3e+05
> −2e+05
> −1e+05
> 0e+00

### 日本語訳（自動翻訳）

> −3e+05
> −2e+05
> −1e+05
> 0e+00の

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- −3e+05 −2e+05 −1e+05 0e+00の

## Chunk 0592

### English（抽出4行）

> chain
> Figure 32: Traceplots for our simpliﬁed model of planetary motion. The chains fail to mix, and
> they converge to several diﬀerent local modes, depending on their initial values. The varying log
> posterior suggests some modes are more consistent with the data than others. The shaded area

### 日本語訳（自動翻訳）

> チェーン
> 図32:惑星の動きの単純化されたモデルのためのトレースプロット。 チェーンはミックスに失敗し、
> 初期値に応じて複数のローカルモードに対応します。 さまざまなログ
> ポスターは、他のモードよりもデータとより一貫性のあるモードを提案します。 陰影エリア

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- チェーン 図32:惑星の動きの単純化されたモデルのためのトレースプロット。

## Chunk 0593

### English（抽出4行）

> represents samples during the warmup phase.
> point: the right plot can help us diagnose the problem almost instantaneously, but unfortunately,
> and despite our best eﬀorts, the default plot need not be the right plot.
> It is important to ﬁgure out whether these modes describe a latent phenomenon of interest

### 日本語訳（自動翻訳）

> ウォームアップフェーズ中にサンプルを表します。
> point: 適切なプロットは、ほぼ瞬時に問題を診断するのに役立ちますが、残念ながら、
> 最高の努力にもかかわらず、デフォルトのプロットは正しいプロットを必要としません。
> これらのモードが関心の潜在現象を説明するかどうかを把握することが重要です。

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- ウォームアップフェーズ中にサンプルを表します。

## Chunk 0594

### English（抽出4行）

> which we must account for in our analysis or whether they are caused by a mathematical artifact.
> Because we have the luxury of ﬁtting a simpliﬁed model, we can exactly work out what is going on
> and use the gained insight for more elaborate models. Figure 33 plots the likelihood computed via
> a quadrature scheme and conﬁrms the existence of local modes. To understand how these modes

### 日本語訳（自動翻訳）

> 分析や数学的なアーティファクトによって引き起こされるかどうかを考慮しなければなりません。
> シンプルモデルのフィッティングのラグジュアリー性を持たせるため、
> 得られたインサイトを、より精巧なモデルに利用します。 図33は、同胞を経由して計算する
> 地形スキームとローカルモードの存在を確認します。 これらのモードを理解するため

### 熟語・専門語

- **likelihood**: 尤度。パラメータが与えられたときデータがどれだけ起こりやすいか。

### 要約

- 分析や数学的なアーティファクトによって引き起こされるかどうかを考慮しなければなりません。

## Chunk 0595

### English（抽出4行）

> arise, we may reason about the log likelihood as a function that penalizes distance between qobs and
> q(k), the positions of the planet simulated for a certain value of k. Indeed,
> log p(qobs|k) = C −1
> 2σ||qobs −q(k)||2

### 日本語訳（自動翻訳）

> 上昇すると、qobs との間の距離を貫通する関数として、ログの尤度について理由があります。
> q(k)、kの特定の値のためにシミュレートされた惑星の位置。 確かに、
> ログ p(qobs|k) = C −1
> 2σ|qobs −q(k)|2

### 熟語・専門語

- **likelihood**: 尤度。パラメータが与えられたときデータがどれだけ起こりやすいか。

### 要約

- 上昇すると、qobs との間の距離を貫通する関数として、ログの尤度について理由があります。

## Chunk 0596

### English（抽出4行）

> 2,
> where C is a constant that does not depend on k. Figure 34 displays the planet’s simulated motion
> given diﬀerent values of k. Recall that k controls the strength of the gravitational interaction: a
> higher value implies a closer and shorter orbit. The assumed value is k = 1. The other values of k

### 日本語訳（自動翻訳）

> 2,200円
> C は k に依存しない定数です。 図34 惑星のシミュレートされた動きを表示
> k の異なる値を指定します。 k が重力相互作用の強さを制御することを思い出させる: a
> より高い値は、より近い、より短い軌道を意味します。 想定値が k = 1. kの他の値

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- 2,200円 C は k に依存しない定数です。

## Chunk 0597

### English（抽出4行）

> fail to generate data consistent with the observed data. For k < 1, the trajectory can drift arbitrarily
> far away from the observed ellipse. But for k > 1, the simulated ellipse must be contained inside
> the observed ellipse, which bounds the distance between qobs and q. Finally, as we change k and
> rotate the ellipse, some of the observed and simulated positions happen to become relatively close,

### 日本語訳（自動翻訳）

> 観察されたデータと一貫性のあるデータを生成できません。 k < 1、軌跡は任意に漂流できます
> 観察された楕円から遠く離れた。 しかし、k > 1のために、シミュレートされた楕円は内部に含まれている必要があります
> 観察された楕円は、qobsとqの間の距離をバインドします。 最後に、k を変更し、
> 楕円を回転させ、観察された位置とシミュレートされた位置のいくつかは比較的閉じるために起こります、

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- 観察されたデータと一貫性のあるデータを生成できません。

## Chunk 0598

### English（抽出4行）

> which induces local modes that appear as wiggles in the tail of the likelihood. The parameter values
> at the mode do not induce simulations that are in close agreement with the data; but they do better
> than neighboring parameter values, which is enough to create a bump in the likelihood.
> The tail modes are a mathematical artifact of the periodic structure of the data and do not

### 日本語訳（自動翻訳）

> 同胞の尾にウイグルとして現れる局所モードを誘導する。 パラメータ値
> モードでは、データと密接な合意にあるシミュレーションを誘発しません。しかし、それらはより良いことをします
> 隣接するパラメータ値よりも、それは可能性のバンプを作成するのに十分です。
> tailモードは、データの周期構造の数学的アーティファクトであり、そうではありません

### 熟語・専門語

- **likelihood**: 尤度。パラメータが与えられたときデータがどれだけ起こりやすいか。

### 要約

- 同胞の尾にウイグルとして現れる局所モードを誘導する。

## Chunk 0599

### English（抽出4行）

> characterize a latent phenomenon of interest. Moreover they only contribute negligible probability
> mass.
> Hence, any chain that does not focus on the dominating mode wastes our precious
> −9e+05

### 日本語訳（自動翻訳）

> 興味の潜在現象を特徴付ける。 さらに、彼らは唯一の必須の確率に貢献します
> マス。
> それゆえ、ドミネーションモードに焦点を合わせないチェーンは、貴重品を無駄に
> −9e+05

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- 興味の潜在現象を特徴付ける。

## Chunk 0600

### English（抽出4行）

> −6e+05
> −3e+05
> 0e+00
> 0.0

### 日本語訳（自動翻訳）

> −6e+05
> −3e+05
> 0e+00の
> ツイート

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- −6e+05 −3e+05 0e+00の ツイート

## Chunk 0601

### English（抽出4行）

> 2.5
> 5.0
> 7.5
> k

### 日本語訳（自動翻訳）

> 2.5マイル
> 5月5日
> 7.5 の
> ログイン

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- 2.5マイル 5月5日 7.5 の ログイン

## Chunk 0602

### English（抽出4行）

> log likelihood
> Figure 33: Log likelihood across various values of k for our simpliﬁed planetary motion model.
> There is a dominating mode near k = 1, followed by local modes as k increases. These modes are
> due to the cyclical trajectory, which allows the possibility of approximate aliasing.

### 日本語訳（自動翻訳）

> ログの可能性
> 図33: 単純化された惑星の動きモデルの k のさまざまな値を渡るログの可能性。
> k = 1の近くのドミネーションモードがあり、その後kのローカルモードが増加します。 これらのモードは
> 循環軌跡により、近接するエイリアシングの可能性を発揮します。

### 熟語・専門語

- **likelihood**: 尤度。パラメータが与えられたときデータがどれだけ起こりやすいか。
- **approximate**: 近似。速度や扱いやすさのため、正確な推論・モデルを緩めること。

### 要約

- ログの可能性 図33: 単純化された惑星の動きモデルの k のさまざまな値を渡るログの可能性。

## Chunk 0603

### English（抽出4行）

> −1.0
> −0.5
> 0.0
> 0.5

### 日本語訳（自動翻訳）

> ツイート
> −0.5 まで
> ツイート
> 0.5パーセント

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- ツイート −0.5 まで ツイート 0.5パーセント

## Chunk 0604

### English（抽出4行）

> 1.0
> qx
> qy
> k

### 日本語訳（自動翻訳）

> 1.0 の
> カートン
> ログイン
> ログイン

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- 1.0 の カートン ログイン ログイン

## Chunk 0605

### English（抽出4行）

> 0.5
> 1.0
> 1.6
> 2.16

### 日本語訳（自動翻訳）

> 0.5パーセント
> 1.0 の
> 1.6マイル
> 2.16

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- 0.5パーセント 1.0 の 1.6マイル 2.16

## Chunk 0606

### English（抽出4行）

> 3.00
> Figure 34: Orbits simulated for various values of k for the planetary motion model. There is no
> strong degeneracy in k, but as this parameter changes, some of the simulated points by chance
> get closer to their observed counterparts, inducing wiggles in the tails of the log likelihood and

### 日本語訳（自動翻訳）

> 3.00円
> 図34:惑星の動きモデルのkのさまざまな値に対してシミュレートされる軌道。 ありません
> k の強い degeneracy が、このパラメータの変更として、チャンスによってシミュレートされたポイントのいくつか
> 観察されたカウンターパートに近づくと、ログの可能性の尾のウィグルを誘導し、

### 熟語・専門語

- **likelihood**: 尤度。パラメータが与えられたときデータがどれだけ起こりやすいか。

### 要約

- 3.00円 図34:惑星の動きモデルのkのさまざまな値に対してシミュレートされる軌道。

## Chunk 0607

### English（抽出4行）

> creating local modes. For example, the 35th observation (solid dot, on the k = 1 orbit) is closer to
> the corresponding position simulated with k = 2.2 (cross on the blue line) than the one obtained
> with k = 1.6 (cross on the green line).
> computational resources. So, what can we do?

### 日本語訳（自動翻訳）

> ローカルモードを作成します。 たとえば、第35回観測(固形点、k = 1軌道)は、
> k = 2.2 でシミュレートする対応する位置(青線の交差)は、
> k = 1.6(緑色線の交差)。
> 計算リソース。 それでは、どうすればいいですか?

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- ローカルモードを作成します。

## Chunk 0608

### English（抽出4行）

> Building stronger priors. One option is to build a more informative prior to reﬂect our belief
> that a high value of k is implausible; or that any data generating process that suggests the planet
> undergoes several orbits over the observation time is unlikely. When such information is available,
> stronger priors can indeed improve computation.

### 日本語訳（自動翻訳）

> より強い優先順位を造って下さい。 1つの選択肢は、私たちの信念を反映する前により有益な構築することです
> k の高値が不可視であること、または惑星を示唆するデータ生成プロセス
> 観察時間が経つにつれて、いくつかの軌道が起こりません。 そのような情報があれば、
> 強い優先順位は確かに計算を改善することができます。

### 熟語・専門語

- **ESS**: 有効サンプルサイズ。自己相関を考慮した独立サンプル相当数。

### 要約

- より強い優先順位を造って下さい。

## Chunk 0609

### English（抽出4行）

> This is unfortunately not the case here.
> A
> stronger prior would reduce the density at the mode, but the wiggles in the tail of the joint would
> persist. Paradoxically, with more data, these wiggles become stronger: the model is fundamentally

### 日本語訳（自動翻訳）

> 申し訳ございません。
> ツイート
> 以前は、モードの密度を低下させますが、ジョイントの尾のwigglesは、
> パーシスト。 並列的に、より多くのデータで、これらのウィグルはより強くなります:モデルは根本的にあります

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- 申し訳ございません。

## Chunk 0610

### English（抽出4行）

> multi-modal. Note also that our current prior, k ∼normal+(0, 1), is already inconsistent with
> the values k takes at the minor modes. In principle we could go a step further and add a hard
> constraint on orbital time or velocity to remove the modes.
> Reweighting draws from each chain. One issue is that the Markov chains fail to transition from one

### 日本語訳（自動翻訳）

> マルチモーダル。 なお、k normal〜+(0, 1) の前の現在のところは、既に矛盾しています。
> k の値がマイナーモードで取り扱われます。 原則的にステップをさらに進め、ハードを追加することができます
> モードを取除く軌道の時間か速度の制約。
> 各チェーンから描画をリウェイトする。 1つの問題は、Markovチェーンが1つから移行できないことです

### 熟語・専門語

- **Markov chain**: マルコフ連鎖。MCMCで事後分布からサンプルを得るための確率過程。

### 要約

- マルチモーダル。

## Chunk 0611

### English（抽出4行）

> mode to the other, meaning some chains sample over a region with a low probability mass. We
> can correct our Monte Carlo estimate using a re-weighting scheme, such as stacking. This strategy
> likely gives us reasonable Monte Carlo estimates, but: (i) we will not comprehensively explore all
> the modes with 8 chains, so stacking should really be treated as discarding the chains stuck at local

### 日本語訳（自動翻訳）

> つまり、低確率の質量を持つ領域上のチェーンサンプルを意味する、他のモード。 お問い合わせ
> モンテカルロ見積りは、積み込みなどの再重み付け方式で修正できます。 この戦略
> 多分私達を適度なモンテカルロの見積もりを与えます、しかし:(i)私達は広範囲にすべてを探検しません
> 8つのチェーンを持つモードなので、スタックはローカルで立ち往生するチェーンを破棄するように処理されるべきです

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- つまり、低確率の質量を持つ領域上のチェーンサンプルを意味する、他のモード。

## Chunk 0612

### English（抽出4行）

> modes and (ii) we still pay a heavy computational price, as the chains in minor modes take up to
> ∼1000 times longer to run.
> Tuning the starting points. We did not specify the Markov chain’s starting points and instead relied
> on Stan’s defaults, which sample the initial point from a uniform(−2, 2) over the unconstrained

### 日本語訳（自動翻訳）

> モードと(ii) マイナーモードのチェーンが最大になるため、依然として重なる計算価格を支払う
> 〜1000回以上走る。
> スタートポイントの調整 Markov チェーンの開始点を指定せず、依存しない
> Stan のデフォルトでは、未禁で一元(−2, 2) から初期点を標本化します。

### 熟語・専門語

- **Markov chain**: マルコフ連鎖。MCMCで事後分布からサンプルを得るための確率過程。

### 要約

- モードと(ii) マイナーモードのチェーンが最大になるため、依然として重なる計算価格を支払う 〜1000回以上走る。

## Chunk 0613

### English（抽出4行）

> space, that is, the starting points are drawn from log k(0) ∼uniform(−2, 2). This default, designed
> for unconstrained parameters on the unit scale, indulges values of k which are widely inconsistent
> with our prior and our domain expertise. In a non-asymptotic regime, the Markov chain does not
> always “forget” its starting point, and it is unlikely to do so here even if we run the chain for many

### 日本語訳（自動翻訳）

> つまり、開始点はログ k(0)〜uniform(−2, 2) から描画されます。 このデフォルトは、設計しました
> ユニットスケールの未使用パラメータ、広範囲に矛盾するkの負の値
> 弊社では、事前および当社のドメインの専門知識を保有しております。 ノンアシンプトティック政権では、Markovチェーンはノー
> 常に「忘れ」の始点であり、多くのチェーンを走る場合でも、ここまではそうするとは違っています。

### 熟語・専門語

- **Markov chain**: マルコフ連鎖。MCMCで事後分布からサンプルを得るための確率過程。

### 要約

- つまり、開始点はログ k(0)〜uniform(−2, 2) から描画されます。

## Chunk 0614

### English（抽出4行）

> many more iterations. We can therefore not ignore this tuning parameter of our algorithm. An
> alternative to the default is to sample k(0) from our prior, thereby imposing that the chains start in a
> range of values deemed reasonable. In this setup, the chains converge quickly and our computation
> focuses on the relevant region.

### 日本語訳（自動翻訳）

> より多くの反復。 したがって、このチューニングパラメータを無視することはできません。 ログイン
> デフォルトに代わるのは k(0) を前にサンプルすることです。これにより、チェーンが始まることを示唆しています。
> 合理的な値の範囲。 このセットアップでは、チェーンはすぐに収束し、私たちの計算
> 関連する地域に焦点を当てます。

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- より多くの反復。

## Chunk 0615

### English（抽出4行）

> Whether with stacking, tuned starting points, or perhaps another mean, we need to give MCMC
> a helping hand to avoid local modes. In general, ignoring non-converging chains is poor practice,
> so we want to highlight how the here presented process diﬀers from that. First, we examine all
> the chains, using posterior predictive checks, and work out exactly how the local modes arise.

### 日本語訳（自動翻訳）

> 積み重ね、調整された開始ポイント、または多分別の平均と、私達MCMCを与える必要がありますかどうか
> ローカルモードを避けるためのヘルプハンド。 一般的に、ノンコンバージチェーンを無視することは、悪い練習です。
> そこで、ここに提示されたプロセスが異なっているかを強調したいと思います。 まずは、すべて調べてみる
> チェーンは、ポスター予測チェックを使用して、ローカルモードの上昇を正確に動作させます。

### 熟語・専門語

- **posterior predictive**: 事後予測。推定後のモデルが観測データの特徴を再現できるかを見る診断。
- **ESS**: 有効サンプルサイズ。自己相関を考慮した独立サンプル相当数。

### 要約

- 積み重ね、調整された開始ポイント、または多分別の平均と、私達MCMCを与える必要がありますかどうか ローカルモードを避けるためのヘルプハンド。

## Chunk 0616

### English（抽出4行）

> We decisively demonstrate that they do not describe data generating processes of interest, nor do
> they contribute more than a negligible amount of probability mass. Only then do we redirect our
> computational resources to focus on the mode around which all the probability mass concentrates.
> 11.3.

### 日本語訳（自動翻訳）

> 私たちは、データ生成プロセスの利益を記述しないと判断し、
> 確率の大量化よりも多くの貢献をしています。 それをリダイレクトするだけ
> すべての確率質量が濃縮するモードに焦点を合わせる計算リソース。
> 11.3.

### 熟語・専門語

- **ESS**: 有効サンプルサイズ。自己相関を考慮した独立サンプル相当数。

### 要約

- 私たちは、データ生成プロセスの利益を記述しないと判断し、 確率の大量化よりも多くの貢献をしています。

## Chunk 0617

### English（抽出4行）

> Bad Markov chain, slow Markov chain?
> Recall that the chains that yielded the lowest log posteriors were also the ones that were the
> slowest—an instance of the folk theorem of statistical computing (see Section 5.1). We can in fact
> show that Hamilton’s equations become more diﬃcult to solve as k increases. The intuition is the

### 日本語訳（自動翻訳）

> 悪いMarkovチェーン、遅いMarkovチェーン?
> 最も低いログのポスターを収穫したチェーンもあったことを思い出させます
> 統計計算の民間理論の最も遅いインスタンス(セクション 5.1)を参照してください。 実際にできる
> ハミルトンの方程式の方がk増加すると解決し難しくなることを示します。 直感は

### 熟語・専門語

- **Markov chain**: マルコフ連鎖。MCMCで事後分布からサンプルを得るための確率過程。

### 要約

- 悪いMarkovチェーン、遅いMarkovチェーン? 最も低いログのポスターを収穫したチェーンもあったことを思い出させます 統計計算の民間理論の最も遅いインスタンス(セクション 5.1)を参照してください。

## Chunk 0618

### English（抽出4行）

> following: if the gravitational interaction is strong, then the planet moves at a much faster rate.
> From a numerical perspective, this means each time step, dt, incurs a greater change in q(t) and
> the integrator’s step size must accordingly be adjusted.
> There is wisdom is this anecdote: an easy deterministic problem can become diﬃcult in a

### 日本語訳（自動翻訳）

> 以下: 重力相互作用が強い場合、惑星ははるかに高速な速度で移動します。
> 数値的な観点から、これは、各ステップ、dt、q(t) で大きな変化を宿ることを意味します。
> インテグレーターのステップ サイズはそれに応じて調節されなければなりません。
> 知恵は、この逸品です:簡単な決定的な問題は困難になることができます

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- 以下: 重力相互作用が強い場合、惑星ははるかに高速な速度で移動します。

## Chunk 0619

### English（抽出4行）

> Bayesian analysis. Indeed Bayesian inference requires us to solve the problem across a range
> of parameter values, which means we must sometimes confront unsuspected versions of the said
> problem. In our experience, notably with diﬀerential equation based models in pharmacology and
> epidemiology, we sometime require a more computationally expensive stiﬀsolver to tackle diﬃcult

### 日本語訳（自動翻訳）

> ベイジアン分析 確かにベイジアン推論は、範囲全体で問題を解決するために私たちを必要とします
> パラメータ値の, つまり、我々は時々、述べたバージョンを見極める必要があります
> 問題。 私たちの経験では、薬理学の差動式ベースのモデルと、
> 疫学、私達は時々困難に取り組むためにより計算的に高価な剛体を要求します

### 熟語・専門語

- **Bayesian inference**: ベイズ推論。事前分布と尤度から事後分布を計算する中核処理。

### 要約

- ベイジアン分析 確かにベイジアン推論は、範囲全体で問題を解決するために私たちを必要とします パラメータ値の, つまり、我々は時々、述べたバージョンを見極める必要があります 問題。

## Chunk 0620

### English（抽出4行）

> ODEs generated during the warmup phase.
> Other times slow computation can alert us that our inference is allowing for absurd parameter
> values and that we need either better priors or more reasonable initial points.
> Unfortunately this goes against the “fail fast” principle outlined in Section 3.4. Our current

### 日本語訳（自動翻訳）

> ウォームアップフェーズ中に生成されたODE。
> その他の時間遅い計算は、私たちの推論がabsurdパラメータを可能にすることを警告することができます
> 値と、より優れた優先順位またはより合理的な初期ポイントが必要であること。
> 残念ながら、これはセクション3.4で概説された「失敗の速い」原則に向かいます。 私達の流れ

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- ウォームアップフェーズ中に生成されたODE。

## Chunk 0621

### English（抽出4行）

> tools tend to be much slower when the ﬁt is bad, hence an important research topic in Bayesian
> computational workﬂow is to ﬂag potential problems quickly to avoid wasting too much time on
> dead ends.
> 11.4.

### 日本語訳（自動翻訳）

> フィットが悪いとき、ツールははるかに遅くなる傾向があります, ベイジアンの重要な研究トピック以来
> 計算ワークフローは、潜在的な問題の問題を迅速にフラグを立てることです。
> デッドエンド。
> 11月4日

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- フィットが悪いとき、ツールははるかに遅くなる傾向があります, ベイジアンの重要な研究トピック以来 計算ワークフローは、潜在的な問題の問題を迅速にフラグを立てることです。

## Chunk 0622

### English（抽出4行）

> Building up the model
> Starting from the simpliﬁed model, we now gradually build our way back to the original model. This
> turns out to be not quite straightforward, but we can put what we have learned from the simpliﬁed
> model to good use. Most inference problems we encounter across the models we ﬁt can be traced

### 日本語訳（自動翻訳）

> モデルの構築
> 単純化されたモデルから始めて、オリジナルモデルに戻り、徐々にその道をビルドします。 お問い合わせ
> 単純化されてから学んだことを置くことができます。
> よい使用へのモデル。 私たちがフィットするモデルに遭遇するほとんどの推論の問題は、追跡することができます

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- モデルの構築 単純化されたモデルから始めて、オリジナルモデルに戻り、徐々にその道をビルドします。

## Chunk 0623

### English（抽出4行）

> back to the interaction between the likelihood and the cyclical observations—an elementary notion,
> once grasped, but which would have been diﬃcult to discover in a less simple setting than the one
> we used.
> Here is an example. In the complete model, we estimate the position of the star, q∗, and ﬁnd that

### 日本語訳（自動翻訳）

> 可能性と周期的観察の相互作用に戻って、小数の概念、
> 一度把握したが、一つよりも少ない簡単な設定で発見しにくい
> 使用しました。
> 例です。 完全なモデルでは、星の位置、q*を推定し、それを調べます

### 熟語・専門語

- **likelihood**: 尤度。パラメータが与えられたときデータがどれだけ起こりやすいか。
- **ESS**: 有効サンプルサイズ。自己相関を考慮した独立サンプル相当数。

### 要約

- 可能性と周期的観察の相互作用に戻って、小数の概念、 一度把握したが、一つよりも少ない簡単な設定で発見しにくい 使用しました。

## Chunk 0624

### English（抽出4行）

> the chains converge to many diﬀerent values, yielding simulations which, depending on the chain,
> agree or disagree with the observations. There is however, based on the traceplots, no obvious
> connection between the starting points and the neighborhoods of convergence. It is diﬃcult to
> examine this type of connections because the model has now 7 parameters, some with strong

### 日本語訳（自動翻訳）

> チェーンは、チェーンに応じて、さまざまな値に収斂し、シミュレーションを収穫します。
> 観察に同意または同意する。 しかし、トレースプロットに基づいて、明らかではありません
> スタートポイントとコンバージェンス地区間の接続。 難しいこと
> モデルが現在7つのパラメーターを持っているので、このタイプの接続を調べてください。

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- チェーンは、チェーンに応じて、さまざまな値に収斂し、シミュレーションを収穫します。

## Chunk 0625

### English（抽出4行）

> posterior correlations. Fortunately, we can reason about the physics of the problem and realize that
> tweaking the star’s position, q∗, and implicitly, r, the star-planet distance, is not unlike modifying
> k. Recall that
> dp

### 日本語訳（自動翻訳）

> ポスターの相関。 幸いなことに、問題の物理を推論し、それを実現することができます
> 星の位置、q*、および暗黙的に調整する、r、スタープレーン距離は、変更とは異なります
> k. それを思い出させる
> ログイン

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- ポスターの相関。

## Chunk 0626

### English（抽出4行）

> dt = −k
> r3(q −q∗),
> whence both k and r control the gravitational interaction.
> We cannot do a quadrature across all 7 parameters of our model. Instead, we look at the

### 日本語訳（自動翻訳）

> dt = −k
> r3(q-q **),
> k と r の両方が重力相互作用を制御するとき。
> 弊社のモデルの7つのパラメーターを全7つにまとめて作成することはできません。 代わりに、私達は見ます

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- dt = −k r3(q-q **), k と r の両方が重力相互作用を制御するとき。

## Chunk 0627

### English（抽出4行）

> conditional likelihood, wherein we keep all parameters (k, q0, and p0) ﬁxed, except for q∗. In
> a sense, this amounts to investigating another simpliﬁcation of our model. Figure 35 shows the
> suspected modes, thereby supporting our conjecture. At this point, with some level of conﬁdence,
> we construct starting points to guide our Markov chains towards the dominating mode and obtain

### 日本語訳（自動翻訳）

> 条件付き尤度, どこに, 我々は、すべてのパラメータを維持します (k, q0, そして、p0) 固定, q *を除きます. で
> つまり、モデルの別の単純化を調べる量です。 図35は、
> 疑われたモード、それによって私達のconjectureを支える。 この点では、自信がいくつかあります。
> 開始点を組み立てて、マーコフチェーンをドミネーションモードに導き、

### 熟語・専門語

- **likelihood**: 尤度。パラメータが与えられたときデータがどれだけ起こりやすいか。
- **Markov chain**: マルコフ連鎖。MCMCで事後分布からサンプルを得るための確率過程。

### 要約

- 条件付き尤度, どこに, 我々は、すべてのパラメータを維持します (k, q0, そして、p0) 固定, q *を除きます. で つまり、モデルの別の単純化を調べる量です。

## Chunk 0628

### English（抽出4行）

> a good ﬁt of the complete model.
> 11.5.
> General lessons from the planetary motion example
> When we fail to ﬁt a model, examining a simpliﬁed model can help us understand the challenges

### 日本語訳（自動翻訳）

> 完全なモデルのよい適合。
> 11.5.1
> 惑星の動きの例からの一般的なレッスン
> モデルに合わないと、単純化されたモデルを調べると、課題を理解することができます

### 熟語・専門語

- **ESS**: 有効サンプルサイズ。自己相関を考慮した独立サンプル相当数。

### 要約

- 完全なモデルのよい適合。

## Chunk 0629

### English（抽出4行）

> that frustrate our inference algorithm. In practice it is diﬃcult to ﬁnd a simpliﬁcation which is
> −4e+05
> −2e+05
> 0e+00

### 日本語訳（自動翻訳）

> 推論アルゴリズムを無視する。 練習では、単純化を見つけることは困難です
> −4e+05
> −2e+05
> 0e+00の

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- 推論アルゴリズムを無視する。

## Chunk 0630

### English（抽出4行）

> −0.5
> 0.0
> 0.5
> q∗

### 日本語訳（自動翻訳）

> −0.5 まで
> ツイート
> 0.5パーセント
> お問い合わせ

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- −0.5 まで ツイート 0.5パーセント お問い合わせ

## Chunk 0631

### English（抽出4行）

> x
> Conditional log likelihood
> −0.3
> 0.0

### 日本語訳（自動翻訳）

> ツイート
> 条件付きログの可能性
> -0.3 の
> ツイート

### 熟語・専門語

- **likelihood**: 尤度。パラメータが与えられたときデータがどれだけ起こりやすいか。

### 要約

- ツイート 条件付きログの可能性 -0.3 の ツイート

## Chunk 0632

### English（抽出4行）

> 0.3
> −0.5
> 0.0
> 0.5

### 日本語訳（自動翻訳）

> 0.35パーセント
> −0.5 まで
> ツイート
> 0.5パーセント

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- 0.35パーセント −0.5 まで ツイート 0.5パーセント

## Chunk 0633

### English（抽出4行）

> q∗
> x
> q∗
> y

### 日本語訳（自動翻訳）

> お問い合わせ
> ツイート
> お問い合わせ
> ログイン

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- お問い合わせ ツイート お問い合わせ ログイン

## Chunk 0634

### English（抽出4行）

> −6e+05
> −4e+05
> −2e+05
> 0e+00

### 日本語訳（自動翻訳）

> −6e+05
> −4e+05
> −2e+05
> 0e+00の

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- −6e+05 −4e+05 −2e+05 0e+00の

## Chunk 0635

### English（抽出4行）

> log likelihood
> Figure 35: For the planetary motion example, log conditional likelihood when varying the star’s
> position, q∗. Left: All parameters are kept ﬁxed, except for the x-coordinate of q∗. Right: This time
> both coordinates of q∗are allowed to vary. The quadrature computation allows us to expose the

### 日本語訳（自動翻訳）

> ログの可能性
> 図35:惑星の動きの例では、星のさまざまな時、ログ条件の尤度
> position, q*。 left: q*のx座標以外の全てのパラメータは固定されます。 右: 今回は
> q*の両座標は異なります。 量子計算は、私たちを露出することができます

### 熟語・専門語

- **likelihood**: 尤度。パラメータが与えられたときデータがどれだけ起こりやすいか。

### 要約

- ログの可能性 図35:惑星の動きの例では、星のさまざまな時、ログ条件の尤度 position, q*。

## Chunk 0636

### English（抽出4行）

> multimodality of the problem.
> manageable and still exhibits the pathology we wish to understand. Reasoning about the topology
> surrounding our model, as alluded to in section 7.4, can help us in this process. A straightforward
> way of simplifying is to ﬁx some of the model parameters.

### 日本語訳（自動翻訳）

> 問題の多様性。
> 管理可能であり、まだ理解したい病理学を展示します。 トポロジーについて考える
> 7.4のセクションに割り当てられたように、私たちのモデルを囲んで、このプロセスで私たちを助けることができます。 ストレートフォワード
> 単純化方法は、モデルパラメーターの一部を修正することです。

### 熟語・専門語

- **multimodality**: 多峰性。事後分布に複数の山があり、MCMCが混合しにくい状態。
- **ESS**: 有効サンプルサイズ。自己相関を考慮した独立サンプル相当数。

### 要約

- 問題の多様性。

## Chunk 0637

### English（抽出4行）

> In the planetary motion example, we are confronted with a multi-modal posterior distribution.
> This geometry prevents our chains from cohesively exploring the parameter space and leads to
> biased Monte Carlo estimates. It is important to understand how these local modes arise and what
> their contribution to the posterior probability mass might be. We do so using posterior predictive

### 日本語訳（自動翻訳）

> 惑星の動き例では、多品種のポスター分布に対向しています。
> このジオメトリは、パラメーター空間を探索し、パラメーター空間を誘導し、
> 偏ったモンテカルロ推定値。 これらのローカルモードが上昇し、どのような方法を理解することが重要です。
> ポスターの確率質量への貢献はかもしれない。 ポスターの予測を使っています

### 熟語・専門語

- **posterior predictive**: 事後予測。推定後のモデルが観測データの特徴を再現できるかを見る診断。
- **posterior distribution**: 事後分布。データ観測後の未知量の不確実性を表す分布。

### 要約

- 惑星の動き例では、多品種のポスター分布に対向しています。

## Chunk 0638

### English（抽出4行）

> checks. It is not uncommon for minor modes, with negligible probability mass, to “trap” a Markov
> chain. The possibility of such ill-ﬁtting modes implies we should always run multiple chains,
> perhaps more than our current default of 4.
> This case study also raises the question of what role starting points may play. Ideally a Markov

### 日本語訳（自動翻訳）

> チェックイン 少数のモードでは珍しいことではありません。必須の確率で、Markovを「トラップ」する
> チェーン。 そのようなイルフィッティングモードの可能性は、私たちが常に複数のチェーンを実行するべきであることを意味します。
> おそらく4の現在のデフォルトよりも多くなります。
> このケーススタディでは、ポイントの開始点の質問を上げます。 理想的にはMarkov

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- チェックイン 少数のモードでは珍しいことではありません。

## Chunk 0639

### English（抽出4行）

> chain forgets its initial value but in a non-asymptotic regime this may not be the case. This is not a
> widely discussed topic but nevertheless one of central importance for practitioners and thence for
> Bayesian workﬂow. Just as there is no universal default prior, there is no universal default initial
> point. Modelers often need to depart from defaults to insure a numerically stable evaluation of

### 日本語訳（自動翻訳）

> チェーンは初期値を忘れるが、非非非非非非同化の政権では、これはケースではないかもしれません。 これは、
> 広く議論されたトピックしかし、決して、開業医やそのために中心的な重要性の一つ
> ベイジアンワークフロー。 万能のデフォルトがないので、ユニバーサルのデフォルト初期設定はありません。
> ポイント。 モデラーは、デフォルトから出発し、数値的に安定した評価を保証する必要があります。

### 熟語・専門語

- **ESS**: 有効サンプルサイズ。自己相関を考慮した独立サンプル相当数。

### 要約

- チェーンは初期値を忘れるが、非非非非非非同化の政権では、これはケースではないかもしれません。

## Chunk 0640

### English（抽出4行）

> the joint density and improve MCMC computation. At the same time we want dispersed initial
> points in order to have reliable convergence diagnostics and to potentially explore all the relevant
> modes. Like for other tuning parameters of an inference algorithm, picking starting points can be
> an iterative process, with adjustments made after a ﬁrst attempt at ﬁtting the model.

### 日本語訳（自動翻訳）

> ジョイント密度を高め、MCMCの計算を改善して下さい。 同時に、分散した初期値が欲しい
> 信頼できるコンバージェンス診断および潜在的なすべての関連を探検するためにポイント
> モード。 推論アルゴリズムの他の調整パラメータと同様に、開始点を選ぶことができます
> 反復的なプロセスは、モデルをフィッティングする最初の試みの後に行われた調整で行われます。

### 熟語・専門語

- **ESS**: 有効サンプルサイズ。自己相関を考慮した独立サンプル相当数。

### 要約

- ジョイント密度を高め、MCMCの計算を改善して下さい。

## Chunk 0641

### English（抽出4行）

> We do not advocate mindlessly discarding misbehaving chains. It is important to analyze where
> this poor behavior comes from, and whether it hints at serious ﬂaws in our model and in our
> inference. Our choice to adjust the initial estimates is based on: (a) the realization that the defaults
> are widely inconsistent with our expertise and (b) the understanding that the local modes do not

### 日本語訳（自動翻訳）

> 不注意な不備のチェーンを捨てないよう、念頭に置きません。 どこで分析することが重要です
> この悪い行動は、私たちのモデルと私たちのモデルで深刻な欠陥にヒントかどうかから来ています
> インフェレンス 初期の推定値を調整する当社の選択肢は、デフォルトで実現する(a)に基づいています。
> ローカルモードがそうでないという理解は、当社の専門知識と(b)と広く矛盾しています

### 熟語・専門語

- **ESS**: 有効サンプルサイズ。自己相関を考慮した独立サンプル相当数。

### 要約

- 不注意な不備のチェーンを捨てないよう、念頭に置きません。

## Chunk 0642

### English（抽出4行）

> describe a latent phenomenon of interest, as shown by our detailed analysis of how cyclical data
> interacts with a normal likelihood.
> 12.
> Discussion

### 日本語訳（自動翻訳）

> サイクルデータの詳細な分析で示されているように、関心の潜在現象を記述します
> 通常の可能性と相互作用します。.
> 12月12日
> ディスカッション

### 熟語・専門語

- **likelihood**: 尤度。パラメータが与えられたときデータがどれだけ起こりやすいか。

### 要約

- サイクルデータの詳細な分析で示されているように、関心の潜在現象を記述します 通常の可能性と相互作用します。

## Chunk 0643

### English（抽出4行）

> 12.1.
> Different perspectives on statistical modeling and prediction
> Consider three diﬀerent ways to think about modeling and prediction:
> • Traditional statistical perspective. In textbooks, statistical inference is typically set up as a

### 日本語訳（自動翻訳）

> 12.1.
> 統計モデリングと予測に関する異なる視点
> モデリングと予測について考える3つの異なる方法を考える:
> •従来の統計的観点。 テキストブックでは、統計的な推論は通常、として設定されます

### 熟語・専門語

- **prediction**: 予測。未知/将来/除外データに対する分布や点推定。

### 要約

- 12.1. 統計モデリングと予測に関する異なる視点 モデリングと予測について考える3つの異なる方法を考える: •従来の統計的観点。

## Chunk 0644

### English（抽出4行）

> problem in which a model has been chosen ahead of time, and in the Bayesian context the
> goal is to accurately summarize the posterior distribution. Computation is supposed to be
> done as long as necessary to reach approximate convergence.
> • Machine learning perspective. In machine learning, the usual goal is prediction, not pa-

### 日本語訳（自動翻訳）

> 以前モデルが選ばれている問題、ベイジアンのコンテキストでは、
> 目標は、ポスターの配布を正確にまとめることです。 計算は、
> おおよその収斂に達するために必要とされる限り。
> •機械学習の視点。 機械学習では、通常の目標は予測ではなく、pa-

### 熟語・専門語

- **posterior distribution**: 事後分布。データ観測後の未知量の不確実性を表す分布。
- **ESS**: 有効サンプルサイズ。自己相関を考慮した独立サンプル相当数。
- **approximate**: 近似。速度や扱いやすさのため、正確な推論・モデルを緩めること。
- **prediction**: 予測。未知/将来/除外データに対する分布や点推定。

### 要約

- 以前モデルが選ばれている問題、ベイジアンのコンテキストでは、 目標は、ポスターの配布を正確にまとめることです。

## Chunk 0645

### English（抽出4行）

> rameter estimation, and computation can stop when cross validation prediction accuracy has
> plateaued.
> • Model exploration perspective. In applied statistical work, much of our modeling eﬀort is
> spent in exploration, trying out a series of models, many of which will have terrible ﬁt to

### 日本語訳（自動翻訳）

> rameterの推定および計算は十字の検証の予測の正確さが持っているとき停止できます
> プレート。
> • モデル調査の視点。 応用統計作業では、モデリングの努力の多くが
> 探査に費やされて、モデルのシリーズを試してみると、その多くはひどくフィットする

### 熟語・専門語

- **cross validation**: 交差検証。汎化性能を推定するためにデータを分割/近似除外する評価法。
- **validation**: 検証。モデルが目的・データ・外部知識に照らして妥当かを確認すること。
- **prediction**: 予測。未知/将来/除外データに対する分布や点推定。

### 要約

- rameterの推定および計算は十字の検証の予測の正確さが持っているとき停止できます プレート。

## Chunk 0646

### English（抽出4行）

> data, poor predictive performance, and slow convergence (see also Section 5.1).
> These three scenarios imply diﬀerent inferential goals. In a traditional statistical modeling
> problem, it can make sense to run computation for a long time, using approximations only when
> absolutely necessary. Another way of saying this is that in traditional statistics, the approximation

### 日本語訳（自動翻訳）

> データ、予期しないパフォーマンス、および低収束(セクション 5.1)を参照してください。
> これら3つのシナリオは、非対比的な目標を意味します。 伝統的な統計モデリング
> 問題は、時だけ近似を使用して、長い間計算を実行する感覚を作ることができます
> 絶対に必要です。 これは、伝統的な統計、近似であると言うもう一つの方法は、

### 熟語・専門語

- **ESS**: 有効サンプルサイズ。自己相関を考慮した独立サンプル相当数。

### 要約

- データ、予期しないパフォーマンス、および低収束(セクション 5.1)を参照してください。

## Chunk 0647

### English（抽出4行）

> might be in the choice of model rather than in the computation. In machine learning, we want to
> pick an algorithm that trades oﬀpredictive accuracy, generalizability, and scalability, so as to make
> use of as much data as possible within a ﬁxed computational budget and predictive goal. In model
> exploration, we want to cycle through many models, which makes approximations attractive. But

### 日本語訳（自動翻訳）

> 計算ではなく、モデルの選択にある可能性があります。 機械学習では、私達はほしいです
> 予測の精度、汎用性、スケーラビリティを取引するアルゴリズムを選択する
> 固定計算予算と予測目標内で可能な限り多くのデータの使用。 モデル
> 探査、近似を魅力的にする多くのモデルを循環させたい。 しかし、

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- 計算ではなく、モデルの選択にある可能性があります。

## Chunk 0648

### English（抽出4行）

> there is a caveat here: if we are to eﬃciently and accurately explore the model space rather than the
> algorithm space, we require any approximation to be suﬃciently faithful as to reproduce the salient
> features of the posterior.
> The distinction here is not about inference vs. prediction, or exploratory vs. conﬁrmatory

### 日本語訳（自動翻訳）

> ここには、モデル空間を効率的かつ正確に探索することです。
> アルゴリズム空間は、十分な忠実に敬意を払い、敬意を表します。
> ポスターの特徴。
> ここでの区別は、推論対予測、または探索対の検証についてではありません

### 熟語・専門語

- **prediction**: 予測。未知/将来/除外データに対する分布や点推定。

### 要約

- ここには、モデル空間を効率的かつ正確に探索することです。

## Chunk 0649

### English（抽出4行）

> analysis. Indeed all parameters in inference can be viewed as some quantities to predict, and all of
> our modeling can be viewed as having exploratory goals (Gelman, 2003). Rather, the distinction is
> how much we trust a given model and allow the computation to approximate.
> As the examples in Sections 10 and 11 illustrate, problems with a statistical model in hindsight

### 日本語訳（自動翻訳）

> 分析。 確かに推論中のすべてのパラメータは、予測するいくつかの量として表示することができ、すべての
> 弊社のモデリングは、明示的なゴール(Gelman, 2003)として閲覧できます。 むしろ、区別は
> 与えられたモデルを信頼し、計算を近似できるようにする量。
> セクション10と11の例として、ヒドサイトにおける統計モデルの問題

### 熟語・専門語

- **approximate**: 近似。速度や扱いやすさのため、正確な推論・モデルを緩めること。

### 要約

- 分析。

## Chunk 0650

### English（抽出4行）

> often seem obvious, but we needed the workﬂow to identify them and understand the obviousness.
> Another important feature of these examples, which often happens with applied problems, is that
> particular challenges in modeling arise in the context of the data at hand: had the data been diﬀerent,
> we might never have encountered these particular issues, but others might well have arisen. This

### 日本語訳（自動翻訳）

> 多くの場合、明らかなようですが、それらを特定し、明白を理解するためのワークフローが必要でした。
> これらの例のもう一つの重要な特徴は、多くの場合、適用された問題で起こることです。
> データの文脈で発生する特定の課題:データが異なる
> 私たちは、これらの特定の問題に遭遇したことがないかもしれませんが、他の人はよくアリスセンを持っているかもしれません。 お問い合わせ

### 熟語・専門語

- **ESS**: 有効サンプルサイズ。自己相関を考慮した独立サンプル相当数。

### 要約

- 多くの場合、明らかなようですが、それらを特定し、明白を理解するためのワークフローが必要でした。

## Chunk 0651

### English（抽出4行）

> is one reason that subﬁelds in applied statistics advance from application to application, as new
> wrinkles become apparent in existing models. A central motivation of this paper is to make more
> transparent the steps by which we can uncover and then resolve these modeling problems.
> 12.2.

### 日本語訳（自動翻訳）

> サブフィールドは、アプリケーションからアプリケーションへの応用の事前の事前統計で、新しいものとして
> しわは既存のモデルで明らかになります。 この紙の中央のモチベーションは、もっと作ることです
> これらのモデリングの問題を発見し、解決できるステップを透明にします。
> 12.2.

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- サブフィールドは、アプリケーションからアプリケーションへの応用の事前の事前統計で、新しいものとして しわは既存のモデルで明らかになります。

## Chunk 0652

### English（抽出4行）

> Justification of iterative model building
> We view the process of model navigation as the next transformative step in data science. The ﬁrst
> big step of data science, up to 1900 or so, was data summarization, centering on the gathering of
> relevant data and summarizing through averages, correlations, least-squares ﬁts, and the like. The

### 日本語訳（自動翻訳）

> 反復モデル構築の正当化
> データサイエンスの次の変容ステップとしてモデルナビゲーションのプロセスを表示します。 初めての方へ
> 1900年までのデータサイエンスの大きなステップは、収集を中心にデータ集約でした
> 関連するデータと平均、相関、少なくとも正方形の適合、等を通して要約。 ザ・オブ・ザ・

### 熟語・専門語

- **ESS**: 有効サンプルサイズ。自己相関を考慮した独立サンプル相当数。
- **model building**: モデル構築。仮定・データ構造・prior・likelihoodを組み合わせる工程。

### 要約

- 反復モデル構築の正当化 データサイエンスの次の変容ステップとしてモデルナビゲーションのプロセスを表示します。

## Chunk 0653

### English（抽出4行）

> next big step, beginning with Gauss and Laplace and continuing to the present day, was modeling:
> the realization that a probabilistic model with scientiﬁc content could greatly enhance the value
> from any given dataset, and also make it more feasible to combine diﬀerent sources of data. We
> are currently in the midst of another big step, computation: with modern Bayesian and machine

### 日本語訳（自動翻訳）

> 次の大きなステップは、ガウスとラプレースから始まり、現在まで続くとモデル化しました。
> 科学的な内容の確率的モデルが価値を非常に高めることができる実現
> 任意のデータセットから、また、異なるデータソースを組み合わせるために、より可能になります。 お問い合わせ
> 現在、別の大きなステップ、計算の真下にあります。現代のベイジアンとマシン

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- 次の大きなステップは、ガウスとラプレースから始まり、現在まで続くとモデル化しました。

## Chunk 0654

### English（抽出4行）

> learning methods, increases in algorithmic and computational eﬃciency have eﬀected a qualitative
> improvement in our ability to make predictions and causal inferences. We would like to move
> beyond good practice and workﬂow in particular case studies, to a formulation of the process of
> model navigation, “facilitating the exploration of model space” (Devezer et al., 2019).

### 日本語訳（自動翻訳）

> 学習方法、アルゴリズムおよび計算効率の増加は質的な効果をもたらしました
> 予測と因果性を生む能力の向上 移動したい
> 特定のケーススタディで優れた実践とワークフローを超えて、プロセスの公式化
> モデルナビゲーション、「モデル空間の探索の促進」(Devezer et al., 2019)

### 熟語・専門語

- **ESS**: 有効サンプルサイズ。自己相関を考慮した独立サンプル相当数。
- **prediction**: 予測。未知/将来/除外データに対する分布や点推定。

### 要約

- 学習方法、アルゴリズムおよび計算効率の増加は質的な効果をもたらしました 予測と因果性を生む能力の向上 移動したい 特定のケーススタディで優れた実践とワークフローを超えて、プロセスの公式化 モデルナビゲーション、「モデル空間の探索の促進…

## Chunk 0655

### English（抽出4行）

> In the ideal world we would build one perfect model and solve the math. In the real world we
> need to take into account the limitations of humans and computers, and this should be included in
> models of science and models of statistics (Navarro, 2019, Devezer et al., 2020).
> From a human perspective, our limited cognitive capabilities make it easier to learn gradually.

### 日本語訳（自動翻訳）

> 理想的な世界では、完璧なモデルを1つ作り、数学を解決します。 私たちが真の世界へ
> 人間とコンピュータの制限を考慮する必要があります。
> 統計の科学モデルとモデル(Navarro、2019、Devezer et al.、2020)。
> 人間の視点から、限られた認知能力で、徐々に学びやすくなります。

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- 理想的な世界では、完璧なモデルを1つ作り、数学を解決します。

## Chunk 0656

### English（抽出4行）

> Iterative model building starting from a simple model is gradual learning and helps us better
> understand the modeled phenomenon. Furthermore, building a rich model takes eﬀort, and it
> can be eﬃcient in human time to start from a simpler model and stop when the model seems to
> be suﬃciently good. We gave an example in Section 10. One goal of workﬂow is to make the

### 日本語訳（自動翻訳）

> シンプルなモデルから始まる反復的なモデルの構築は、段階的な学習とより良い私たちを助けます
> モデリングされた現象を理解する。 さらに、豊富なモデルをつくりながら、
> シンプルモデルからスタートし、モデルが見えるときに止まるのは、人間の時間で効率よくできます。
> お問い合わせ セクション10で例を挙げました。 ワークフローの1つの目標は、ワークフローを作ることです

### 熟語・専門語

- **model building**: モデル構築。仮定・データ構造・prior・likelihoodを組み合わせる工程。

### 要約

- シンプルなモデルから始まる反復的なモデルの構築は、段階的な学習とより良い私たちを助けます モデリングされた現象を理解する。

## Chunk 0657

### English（抽出4行）

> process easier for humans even in the idealized setting where exact computation can be performed
> automatically.
> Iterating over a set of models is also useful from a computational standpoint. Given a proper
> posterior, computation in Bayesian inference is theoretically solved. In practice we must contend

### 日本語訳（自動翻訳）

> 正確な計算が実行できる理想的な設定であっても、人間にとってプロセスが容易
> 自動的に。
> モデルのセットを反復することは計算の立場からまた有用です。 適切な
> ベイジアン・インフェレンスにおけるポスター、計算は理論的に解決されます。 練習では、私たちは理解しなければなりません

### 熟語・専門語

- **Bayesian inference**: ベイズ推論。事前分布と尤度から事後分布を計算する中核処理。
- **ESS**: 有効サンプルサイズ。自己相関を考慮した独立サンプル相当数。

### 要約

- 正確な計算が実行できる理想的な設定であっても、人間にとってプロセスが容易 自動的に。

## Chunk 0658

### English（抽出4行）

> with ﬁnite computational resources. An algorithm for which asymptotic guarantees exist can fail
> when run for a ﬁnite time. There is no fully automated computation that yields perfect results,
> at least not across the vast range of models practitioners care about. Another goal of workﬂow
> is to avoid some computational problems and be able to eﬃciently diagnose the remaining ones.

### 日本語訳（自動翻訳）

> 有限計算リソースを使って。 アシンプトティック保証が存在するアルゴリズムが失敗する
> 有限の時間のために動くとき。 完璧な結果をもたらす完全自動化された計算はありません。
> より広範囲なモデルの実務家が心配しています。 ワークフローのもう一つの目標
> 計算上の問題を回避し、残りの問題を効率的に診断できるようにすることです。

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- 有限計算リソースを使って。

## Chunk 0659

### English（抽出4行）

> Here too deconstructing the model into simpler versions can be helpful: it is easier to understand
> computational challenges when there are fewer moving parts.
> Hence, even if a mathematical
> description of a model is given, correctly implementing the model tends to require iteration.

### 日本語訳（自動翻訳）

> モデルを単純バージョンに分解しても便利です:理解しやすい
> 可動部が少ない場合の計算課題。
> したがって、数学的であっても
> モデルの記述は、正しくモデルを実装することは、反復を必要とする傾向にあります。

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- モデルを単純バージョンに分解しても便利です:理解しやすい 可動部が少ない場合の計算課題。

## Chunk 0660

### English（抽出4行）

> Not only is iterative model building beneﬁcial from a cognitive and computational standpoint,
> but the complexity of complicated computational models makes it diﬃcult for the human user to
> disentangle computational concerns, modeling issues, data quality problems, and bugs in the code.
> By building models iteratively, we can employ software engineering techniques in our modeling

### 日本語訳（自動翻訳）

> 認知と計算の観点から有益な反復的なモデルの構築だけでなく、
> しかし、複雑な計算モデルの複雑さは、人間にとっては困難になります
> 複雑な問題、課題のモデル化、データ品質の問題、バグのコード化
> 独自にモデルを構築することで、モデリングにおけるソフトウェアエンジニアリング技術を採用

### 熟語・専門語

- **model building**: モデル構築。仮定・データ構造・prior・likelihoodを組み合わせる工程。

### 要約

- 認知と計算の観点から有益な反復的なモデルの構築だけでなく、 しかし、複雑な計算モデルの複雑さは、人間にとっては困難になります 複雑な問題、課題のモデル化、データ品質の問題、バグのコード化 独自にモデルを構築することで、モデリングにおけ…

## Chunk 0661

### English（抽出4行）

> procedure. Simple model components can be checked to make sure they act in an expected way
> before more complicated components are added.
> 12.3.
> Model selection and overfitting

### 日本語訳（自動翻訳）

> 手順。 シンプルなモデルコンポーネントは、期待される方法で動作するようにチェックすることができます
> 複雑なコンポーネントを追加する前に。
> 12.3.
> モデル選定とオーバーフィッティング

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- 手順。

## Chunk 0662

### English（抽出4行）

> A potential issue with the proposed iterative workﬂow is that model improvement is conditioned
> on discrepancy between the currently considered model and the data, and thus at least some aspects
> of the data are used more than once. This “double dipping” can in principle threaten the frequency
> properties of our inferences, and it is important to be aware of the possibility of overﬁtting arising

### 日本語訳（自動翻訳）

> 提案された反復ワークフローの潜在的な問題は、モデルの改善が調整されることです
> 現在検討しているモデルとデータとの間の矛盾にしたがって、少なくともいくつかの側面
> データを一度以上使用しています。 この「ダブルディッピング」は、原則として周波数を脅かすことができます
> 当社の推論の性質、およびそれが原因で生じる過度の可能性を認識することが重要である

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- 提案された反復ワークフローの潜在的な問題は、モデルの改善が調整されることです 現在検討しているモデルとデータとの間の矛盾にしたがって、少なくともいくつかの側面 データを一度以上使用しています。

## Chunk 0663

### English（抽出4行）

> from model selection, as considered for example by Fithian et al. (2015) and Loftus (2015). A
> related issue is the garden of forking paths, the idea that diﬀerent models would have been ﬁt had
> the data come out diﬀerently (Gelman and Loken, 2013). We do not advocate selecting the best
> ﬁt among some such set of models. Instead, we describe a process of building to a more complex

### 日本語訳（自動翻訳）

> モデル選択から、例えばFithian et al. (2015)とLoftus (2015)によって考慮される。 ツイート
> 関連する問題は、フォークパスの庭です, 異なるモデルがフィットしていたアイデア
> データは別々に出てきます(GelmanとLoken、2013)。 最高の選択を支持しない
> そのようなモデルのセットの中で合う。 ではなく、より複雑に構築するプロセスを記述します。

### 熟語・専門語

- **ESS**: 有効サンプルサイズ。自己相関を考慮した独立サンプル相当数。

### 要約

- モデル選択から、例えばFithian et al. (2015)とLoftus (2015)によって考慮される。

## Chunk 0664

### English（抽出4行）

> model taking the time to understand and justify each decision.
> To put it in general terms: suppose we ﬁt model M1, then a posterior predictive check reveals
> problems with its ﬁt to data, so we move to an improved M2 that, we hope, includes more prior
> information and makes more sense with respect to the data and the applied problem under study. But

### 日本語訳（自動翻訳）

> 各決定を理解し、正当化する時間を取るモデル.
> 一般的な用語でそれを置くために:モデルM1に合うと仮定します, その後、ポスター予測チェックは明らかにします
> データに合致した問題は、改善されたM2に移行するので、優先してほしい。
> 情報は、データと応用問題に関してより感覚的になり、研究下にある。 しかし、

### 熟語・専門語

- **posterior predictive**: 事後予測。推定後のモデルが観測データの特徴を再現できるかを見る診断。
- **decision**: 意思決定。予測分布を損失・効用・行動選択へ接続する工程。

### 要約

- 各決定を理解し、正当化する時間を取るモデル. 一般的な用語でそれを置くために:モデルM1に合うと仮定します, その後、ポスター予測チェックは明らかにします データに合致した問題は、改善されたM2に移行するので、優先してほしい。

## Chunk 0665

### English（抽出4行）

> had the data been diﬀerent, we would have been satisﬁed with M1. The steps of model checking and
> improvement, while absolutely necessary, represent an aspect of ﬁtting to data that is not captured
> in the likelihood or the prior.
> This is an example of the problem of post-selection inference (Berk et al., 2013, Efron, 2013).

### 日本語訳（自動翻訳）

> データは異なるため、M1に満足しています。 モデルチェックのステップと
> 絶対に必要とされている間、改善は捕獲されないデータへの付属品の側面を表します
> 可能性や優先順位。
> これは、後選択推論の問題の例です (Berk et al., 2013, Efron, 2013).

### 熟語・専門語

- **model checking**: モデルチェック。モデルの仮定・予測・計算結果がデータや目的に合うか検査すること。
- **likelihood**: 尤度。パラメータが与えられたときデータがどれだけ起こりやすいか。
- **ESS**: 有効サンプルサイズ。自己相関を考慮した独立サンプル相当数。

### 要約

- データは異なるため、M1に満足しています。

## Chunk 0666

### English（抽出4行）

> Much of the research in this area has been on how to adjust p-values and conﬁdence intervals
> to have appropriate frequency properties conditional on the entire ﬁtting procedure, but Bayesian
> inferences are subject to this concern as well. For example, here is the story of one of the adaptations
> we made in election forecasting (Gelman, Hullman, et al., 2020):

### 日本語訳（自動翻訳）

> この領域の研究の多くは、p値と自信の間隔を調整する方法についてありました
> 適切な周波数特性がフィッティング手順全体に条件付きであるが、ベイジアン
> この懸念事項は、同様にこの問題の対象となります。 例えば、ここは適応の1つの物語です。
> 選挙予測(Gelman, Hullman, et al., 2020):

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- この領域の研究の多くは、p値と自信の間隔を調整する方法についてありました 適切な周波数特性がフィッティング手順全体に条件付きであるが、ベイジアン この懸念事項は、同様にこの問題の対象となります。

## Chunk 0667

### English（抽出4行）

> A few weeks after we released our ﬁrst model of the election cycle for The Economist,
> we were disturbed at the narrowness of some of its national predictions. In particular,
> at one point the model gave Biden 99% chance of winning the national vote. Biden was
> clearly in the lead, but 99% seemed like too high a probability given the information

### 日本語訳（自動翻訳）

> エコノミストの選挙サイクルの第1モデルを発売してから数週間後、
> 国家の予測の一部の狭さで、私たちは混乱していました。 特に、
> 一方、モデルが国家投票を獲得するBiden 99%チャンスを与えた。 バイデン
> 明らかに鉛に, しかし、 99% あまりにも高い確率が情報を与えているように見えた

### 熟語・専門語

- **ESS**: 有効サンプルサイズ。自己相関を考慮した独立サンプル相当数。
- **prediction**: 予測。未知/将来/除外データに対する分布や点推定。

### 要約

- エコノミストの選挙サイクルの第1モデルを発売してから数週間後、 国家の予測の一部の狭さで、私たちは混乱していました。

## Chunk 0668

### English（抽出4行）

> available at that time.
> Seeing this implausible predictive interval motivated us to
> refactor our model, and we found some bugs in our code and some other places where
> the model could be improved—including an increase in between-state correlations,

### 日本語訳（自動翻訳）

> その際にご利用いただけます。
> この不可分予測間隔を調べて、私たちをモチベーション
> 私たちのモデルを再ファクタリングし、コードと他の場所にあるいくつかのバグを発見しました。
> モデルは、状態の相関の増加を含む、改善することができ、

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- その際にご利用いただけます。

## Chunk 0669

### English（抽出4行）

> which increased uncertainty of national aggregates. The changes in our model did not
> have huge eﬀects—not surprisingly given that we had tested our earlier model on 2008,
> 2012, and 2016—but the revision did lower Biden’s estimated probability of winning
> the popular vote to 98%. This was still a high value, but it was consistent with the

### 日本語訳（自動翻訳）

> 国民の総計の不確実性を高めた。 私たちのモデルの変更はなかった
> 2008年の以前のモデルをテストしたのは驚くべきことに、大きな効果があります。
> 2012年と2016年は、リビジョンは、バイデンの賞金の推定確率を下げた。
> 98%の人気投票。 まだまだ価値が高かったが、一貫して

### 熟語・専門語

- **uncertainty**: 不確実性。観測・パラメータ・モデル構造・意思決定に残る曖昧さ。

### 要約

- 国民の総計の不確実性を高めた。

## Chunk 0670

### English（抽出4行）

> polling and what we’d seen of variation in the polls during the campaign.
> The errors we caught were real, but if we had not been aware of these particular problematic
> predictions, we might have never gone back to check. This data-dependence of our analysis implies
> a problem with a fully Bayesian interpretation of the probability statements based on the ﬁnal

### 日本語訳（自動翻訳）

> キャンペーン中に投票や投票で見たこと。
> 我々がキャッチしたエラーは本物だったが、これらの特定の問題に気付いていなかった場合
> 予測、私たちは決してチェックに戻っていません。 当社の分析のこのデータ依存性は、
> 最終的なに基づく確率論の完全バイジアン解釈の問題

### 熟語・専門語

- **prediction**: 予測。未知/将来/除外データに対する分布や点推定。

### 要約

- キャンペーン中に投票や投票で見たこと。

## Chunk 0671

### English（抽出4行）

> model we settled on. And, in this case, model averaging would not resolve this problem: we would
> not want to average our ﬁnal model with its buggy predecessor. We might want to average its
> predictions with those of some improved future model, but we can’t do that either, as this future
> model does not yet exist!

### 日本語訳（自動翻訳）

> 解決するモデル。 そして、この場合、モデルの平均化はこの問題を解決しません。
> 当社の最終モデルをバギーの前身と平均したくない。 私たちは、その平均を望むかもしれません
> 未来モデルを改良した者たちと予測するが、この未来のように、それを行うことはできません。
> モデルはまだ存在しません!

### 熟語・専門語

- **ESS**: 有効サンプルサイズ。自己相関を考慮した独立サンプル相当数。
- **prediction**: 予測。未知/将来/除外データに対する分布や点推定。

### 要約

- 解決するモデル。

## Chunk 0672

### English（抽出4行）

> That said, we think that Bayesian workﬂow as described here will avoid the worst problems of
> overﬁtting. Taylor and Tibshirani (2015) warn of the problem of inference conditional on having
> “searched for the strongest associations.” But our workﬂow does not involve searching for optimally-
> ﬁtting models or making hard model selection under uncertainty. Rather, we use problems with

### 日本語訳（自動翻訳）

> とはいえ、ベイジアンのワークフローは、ここに記載されているとおりの最悪の問題を回避すると思います。
> オーバーフィット。 テイラーとチブシラニ (2015) 持っていることに対する推論条件の問題の警告
> 「最強の協会の調査」 しかし、ワークフローは最適な検索を行わない
> フィッティングモデル、または不確実性の下でハードモデル選択を作る。 むしろ、私たちは問題を使っています

### 熟語・専門語

- **uncertainty**: 不確実性。観測・パラメータ・モデル構造・意思決定に残る曖昧さ。

### 要約

- とはいえ、ベイジアンのワークフローは、ここに記載されているとおりの最悪の問題を回避すると思います。

## Chunk 0673

### English（抽出4行）

> ﬁtted models to reassess our modeling choices and, where possible, include additional information.
> For our purposes, the main message we take from concerns about post-selection inference is that our
> ﬁnal model should account for as much information as possible, and when we might be selecting
> among a large set of possible models, we instead embed these in a larger model, perform predictive

### 日本語訳（自動翻訳）

> モデリングの選択肢を再評価する適合モデルと、可能な場所は、追加情報を含みます。
> そのためには、選択後の推論に関する懸念から取り寄せるメインメッセージは、
> 最終モデルは、できるだけ多くの情報について考慮すべきであり、私たちが選んだ場合
> 可能なモデルの大きなセットの中で、より大きなモデルでそれらを埋め込む代わりに、予測を実行します

### 熟語・専門語

- **ESS**: 有効サンプルサイズ。自己相関を考慮した独立サンプル相当数。

### 要約

- モデリングの選択肢を再評価する適合モデルと、可能な場所は、追加情報を含みます。

## Chunk 0674

### English（抽出4行）

> model averaging, or use all of the models simultaneously (see Section 8). As discussed by Gelman,
> Hill, and Yajima (2012), we expect that would work better than trying to formally model the process
> of model checking and expansion.
> We also believe that our workﬂow enables practitioners to perform severe tests of many of the

### 日本語訳（自動翻訳）

> 全てのモデルを同時に使用(セクション8参照)。 ゲルマンが語る通り、
> ヒルとヤジマ(2012年)は、プロセスを正式にモデル化しようとするよりもうまくいくと期待しています。
> モデルのチェックと拡張。
> また、当社のワークフローにより、開業医が多くの厳しい試験を実施できるという確信があります。

### 熟語・専門語

- **model checking**: モデルチェック。モデルの仮定・予測・計算結果がデータや目的に合うか検査すること。
- **ESS**: 有効サンプルサイズ。自己相関を考慮した独立サンプル相当数。

### 要約

- 全てのモデルを同時に使用(セクション8参照)。

## Chunk 0675

### English（抽出4行）

> assumptions that underlie the models being examined (Mayo, 2018). Our claim is that often a
> model whose assumptions withstood such severe tests is, despite being the result of data-dependent
> iterative workﬂow, more trustworthy than a preregistered model that has not been tested at all.
> On a slightly diﬀerent tack, iterative model building is fully justiﬁed as a way to understand a

### 日本語訳（自動翻訳）

> 2018年5月(Mayo, 2018)のモデルを調べるという前提。 私たちの主張は、多くの場合、
> このような厳しいテストを想定したモデルは、データに依存する結果にもかかわらず、
> 反復的なワークフローは、事前登録済みモデルよりも信頼性が高く、テストされていない。
> 少し異なるタックでは、反復的なモデルビルディングは完全に理解する方法として正当化されます

### 熟語・専門語

- **model building**: モデル構築。仮定・データ構造・prior・likelihoodを組み合わせる工程。

### 要約

- 2018年5月(Mayo, 2018)のモデルを調べるという前提。

## Chunk 0676

### English（抽出4行）

> ﬁxed, complex model. This is an important part of workﬂow as it is well known that components
> in complex models can interact in complex ways. For example, Hodges and Reich (2010) describe
> how structured model components such as spatial eﬀects can have complex interactions with linear
> covariate eﬀects.

### 日本語訳（自動翻訳）

> 固定、複雑なモデル。 これは、コンポーネントがよく知られているので、ワークフローの重要な部分です
> 複雑なモデルでは複雑な方法でやり取りすることができます。 たとえば、ホッジとレイチ(2010)は、
> 空間効果などの構造モデルコンポーネントは、線形との複雑な相互作用を持つことができます
> 共変数効果。

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- 固定、複雑なモデル。

## Chunk 0677

### English（抽出4行）

> 12.4.
> Bigger datasets demand bigger models
> Great progress has been made in recent decades on learning from data using methods developed
> in statistics, machine learning, and applied ﬁelds ranging from psychometrics to pharmacology.

### 日本語訳（自動翻訳）

> 12.4 .
> より大きいデータセットはより大きいモデルを要求します
> 開発方法を用いたデータから学習する10年以上に渡る大進展
> 統計、機械学習、および心理測定から薬理まで及ぶ応用分野。

### 熟語・専門語

- **ESS**: 有効サンプルサイズ。自己相関を考慮した独立サンプル相当数。

### 要約

- 12.4 . より大きいデータセットはより大きいモデルを要求します 開発方法を用いたデータから学習する10年以上に渡る大進展 統計、機械学習、および心理測定から薬理まで及ぶ応用分野。

## Chunk 0678

### English（抽出4行）

> Hierarchical Bayesian modeling, deep learning, and other regularization-based approaches are
> allowing researchers to ﬁt larger, more complex models to real-world data, enabling information
> aggregation and partial pooling of inferences from diﬀerent sources of data.
> While the proposed workﬂow oﬀers advantages regardless of the size of the dataset, the case

### 日本語訳（自動翻訳）

> Hierarchical Bayesianモデリング、ディープラーニング、その他正規化ベースのアプローチは、
> 研究者は、より大きな複雑なモデルを現実的なデータに収まるようにし、情報を有効にします
> データの異なるソースからの推論の集計と部分的なプール。
> 提案されたワークフローは、データセットのサイズに関係なく利点を提供しますが、ケース

### 熟語・専門語

- **ESS**: 有効サンプルサイズ。自己相関を考慮した独立サンプル相当数。

### 要約

- Hierarchical Bayesianモデリング、ディープラーニング、その他正規化ベースのアプローチは、 研究者は、より大きな複雑なモデルを現実的なデータに収まるようにし、情報を有効にします データの異なるソースからの推論の集計と…

## Chunk 0679

### English（抽出4行）

> of big data deserves a special mention. “Big data” is sometimes deﬁned as being too big to ﬁt in
> memory on your machine, but here we use the term more generally to also include datasets that are
> so large that our usual algorithms do not run in reasonable time. In either case, the deﬁnition is
> relative to your current computing capacity and inferential goals.

### 日本語訳（自動翻訳）

> ビッグデータの特別な言及に値する。 「ビッグデータ」は、大きすぎて収まるように定義されることもあります。
> あなたの機械のメモリ、しかしここに私達はまたあるデータセットを含むためにもっと一般に言葉を使用します
> いつものアルゴリズムが時間通りに走らないので大きめです。 どちらの場合も定義は
> 現行の計算能力と不当な目標に準じます。

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- ビッグデータの特別な言及に値する。

## Chunk 0680

### English（抽出4行）

> It is frequently assumed that big data can alleviate the need for careful modeling. We do
> not believe this is the case. Quantity does not always substitute for quality. Big data is messy
> data. Big data prioritizes availability over randomization, which means Big data is almost always
> observational rather than from designed experiments. Big data frequently uses available proxies

### 日本語訳（自動翻訳）

> ビッグデータが慎重にモデリングの必要性を軽減できると頻繁に想定されます。 お問い合わせ
> このケースは信じられない。 量は質のために常に取り替えません。 ビッグデータがメッシー
> データ。 ビッグデータは、ランダム化よりも可用性を優先します。つまり、ビッグデータはほとんど常に
> 設計実験ではなく観察。 ビッグデータが頻繁に利用可能なプロキシを使用する

### 熟語・専門語

- **ESS**: 有効サンプルサイズ。自己相関を考慮した独立サンプル相当数。

### 要約

- ビッグデータが慎重にモデリングの必要性を軽減できると頻繁に想定されます。

## Chunk 0681

### English（抽出4行）

> rather than direct measurements of underlying constructs of interest. To make relevant inferences
> from big data, we need to extrapolate from sample to population, from control to treatment group,
> and from measurements to latent variables. All these steps require statistical assumptions and
> adjustment of some sort, which in the Bayesian framework is done using probability modeling

### 日本語訳（自動翻訳）

> 興味の根底構造の直接測定ではなく。 関連する推論を行うため
> 大きいデータから、私達は制御から処置のグループへのサンプルから人口まで、余分に膨脹する必要があります
> 測定から遅延変数まで。 これらのすべての手順では、統計的な仮定が必要です。
> ベイジアンフレームワークでは、確率モデリングを使ってある種の調整を行います。

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- 興味の根底構造の直接測定ではなく。

## Chunk 0682

### English（抽出4行）

> and mathematical connections to inferential goals. For example, we might ﬁt a multilevel model
> for data given respondents’ demographic and geographic characteristics and then poststratify to
> connect the predictions from this model to the goal of inference about the general population.
> Each of these steps of statistical extrapolation should be more eﬀective if we adjust for more

### 日本語訳（自動翻訳）

> そして重要な目的への数学的な関係。 たとえば、マルチレベルモデルにフィットする場合があります。
> 回答者の人口統計的および地理的特性を与えられたデータのために、そしてpoststratifyに
> このモデルから一般人口に対する推論の目標に予測を接続します。
> 統計的な extrapolation のこれらのステップのそれぞれは、より効果的です。

### 熟語・専門語

- **prediction**: 予測。未知/将来/除外データに対する分布や点推定。

### 要約

- そして重要な目的への数学的な関係。

## Chunk 0683

### English（抽出4行）

> factors—that is, include more information—but we quickly reach a technical barrier.
> Models
> that adjust for many of factors can become hard to estimate, and eﬀective modeling requires (a)
> regularization to get more stable estimates (and in turn to allow us to adjust for more factors),

### 日本語訳（自動翻訳）

> 要因は、より多くの情報を含みますが、私たちはすぐに技術的な障壁に到達します。
> モデル
> 要因の多くが推定しにくい、効果的なモデリングが必要です(a)
> より安定した見積もりを得るための正規化(そして、我々はより多くの要因のために調整できるようにするために)、

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- 要因は、より多くの情報を含みますが、私たちはすぐに技術的な障壁に到達します。

## Chunk 0684

### English（抽出4行）

> and (b) modeling of latent variables (for example parameters that vary by person when modeling
> longitudinal data), missingness, and measurement error.
> A key part of Bayesian workﬂow is adapting the model to the data at hand and the questions
> of interest. The model does not exist in isolation and is not speciﬁed from the outside; it emerges

### 日本語訳（自動翻訳）

> および(b) 潜在変数のモデリング(モデル化時に人によって変化するパラメータなど)
> 縦方向データ)、欠損、測定エラー。
> ベイジアンワークフローの重要な部分は、モデルを手元や質問でデータに適応させます
> 関心の. モデルは分離に存在せず、外部から指定されていない。

### 熟語・専門語

- **ESS**: 有効サンプルサイズ。自己相関を考慮した独立サンプル相当数。

### 要約

- および(b) 潜在変数のモデリング(モデル化時に人によって変化するパラメータなど) 縦方向データ)、欠損、測定エラー。

## Chunk 0685

### English（抽出4行）

> from engagement with the application and the available data.
> 12.5.
> Prediction, generalization, and poststratification
> The three core tasks of statistics are generalizing from sample to population, generalizing from

### 日本語訳（自動翻訳）

> アプリケーションと利用可能なデータとのエンゲージメントから。
> 12.5.
> 予測、一般化、延期
> 統計の3つのコアタスクは、サンプルから人口まで、一般化から

### 熟語・専門語

- **prediction**: 予測。未知/将来/除外データに対する分布や点推定。

### 要約

- アプリケーションと利用可能なデータとのエンゲージメントから。

## Chunk 0686

### English（抽出4行）

> control to treatment group, and generalizing from observed data to underlying constructs of interest.
> In machine learning and causal inference, the terms “domain adaptation” and “transportability” have
> been used to represent the challenges of taking inference from a particular dataset and applying it in
> a new problem (Blitzer, Dredze, and Pereira, 2007, Pearl and Bareinboim, 2011). Many statistical

### 日本語訳（自動翻訳）

> 治療グループに制御し、観察されたデータを一般化し、興味の根本的な構成に。
> 機械学習と因果推論では、用語「ドメインの適応」と「輸送性」は、
> 特定のデータセットから推論を取ることの課題を表現し、それを適用するために使用されました
> 新たな問題(Blitzer、Dredze、Pereira、2007、Pearl and Bareinboim、2011)。 多くの統計

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- 治療グループに制御し、観察されたデータを一般化し、興味の根本的な構成に。

## Chunk 0687

### English（抽出4行）

> tools have been developed over the years to attack problems of generalization, for example weighting
> and poststratiﬁcation in sample surveys, matching and regression in causal inference, and latent
> variable modeling in areas such as psychometrics and econometrics where there is concern about
> indirect or biased observations.

### 日本語訳（自動翻訳）

> ツールは、増大の問題を攻撃するために長年にわたって開発されています, 例えば重み
> サンプル調査のpoststratification、causalのinferenceの一致し、そしてregression
> 心理測定やエコノメトリなどの分野における変数モデリング
> 間接的または偏見観察。

### 熟語・専門語

- **ESS**: 有効サンプルサイズ。自己相関を考慮した独立サンプル相当数。

### 要約

- ツールは、増大の問題を攻撃するために長年にわたって開発されています, 例えば重み サンプル調査のpoststratification、causalのinferenceの一致し、そしてregression 心理測定やエコノメトリなどの分…

## Chunk 0688

### English（抽出4行）

> Bayesian methods enter in various ways, including the idea of hierarchical modeling or par-
> tial pooling to appropriately generalize across similar but not identical settings, which has been
> rediscovered in many ﬁelds (e.g., Henderson, 1950, Novick et al., 1972, Gelman and Hill, 2007,
> Finkel and Manning, 2009, Daumé, 2009), regularization to facilitate the use of large nonparamet-

### 日本語訳（自動翻訳）

> ベイジアンメソッドは、階層モデリングやパーペアのアイデアなど、さまざまな方法で入力します。
> 同様に、同じ設定ではなく、適切に一般化するための道的なプール
> 1972年、ゲルマン・ヒル、2007年、ノミック・エ・アルに師事。
> フィンケルとマニング, 2009, ダム, 2009), 大規模なノンパラメットの使用を容易にするための正規化 -

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- ベイジアンメソッドは、階層モデリングやパーペアのアイデアなど、さまざまな方法で入力します。

## Chunk 0689

### English（抽出4行）

> ric models (Hill, 2011), and multilevel modeling for latent variables (Skrondal and Rabe-Hesketh,
> 2004), and there are connections between transportability and Bayesian graph models (Pearl and
> Bareinboim, 2014).
> Bayesian workﬂow does not stop with inference for the ﬁtted model. We are also interested

### 日本語訳（自動翻訳）

> ricモデル(Hill, 2011)、およびラベント変数(SkrondalとRabe-Hesketh、
> 2004) トランスポータビリティとベイジアングラフモデル(Pearl との間の接続があります。
> Bareinboim、2014年。
> ベイジアンワークフローは、適合したモデルの推論を止めません。 お問い合わせ

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- ricモデル(Hill, 2011)、およびラベント変数(SkrondalとRabe-Hesketh、 2004) トランスポータビリティとベイジアングラフモデル(Pearl との間の接続があります。

## Chunk 0690

### English（抽出4行）

> in inferences for new real-world situations, which implies that the usual prior and data model is
> embedded in a larger framework including predictions and inferences for new settings, including
> potentially diﬀerent modes of measurement and treatment assignments. Statistical models can also
> go into production, which provides future opportunities for feedback and improvement.

### 日本語訳（自動翻訳）

> 新しい現実世界の状況に影響を及ぼすため、通常の前後のデータモデルが
> 新しい設定のための予測と推論を含むより大きなフレームワークに組み込まれています。
> 測定および処置の割り当ての潜在的に異なったモード。 統計的なモデルも
> フィードバックと改善のための将来の機会を提供する生産に行きます。

### 熟語・専門語

- **prediction**: 予測。未知/将来/除外データに対する分布や点推定。

### 要約

- 新しい現実世界の状況に影響を及ぼすため、通常の前後のデータモデルが 新しい設定のための予測と推論を含むより大きなフレームワークに組み込まれています。

## Chunk 0691

### English（抽出4行）

> Just as the prior can often only be understood in the context of the likelihood (Gelman et al.,
> 2017, Kennedy et al., 2019), so should the model be understood in light of how it will be used.
> For example, Singer et al. (1999) and Gelman, Stevens, and Chan (2003) ﬁt a series of models
> to estimate the eﬀects of ﬁnancial incentives on response rates in surveys. The aspects of these

### 日本語訳（自動翻訳）

> 前のことは、多くの場合、唯一の可能性のコンテキストで理解することができます (Gelman et al.,
> 2017年、ケネディ・エ・アル。、2019年)は、モデルの使い方の光で理解すべきである。
> 例えば、シンガーら. (1999) と ゲルマン, スティーブンス, チャン (2003) モデルのシリーズに合う
> 調査の応答率に対する財務インセンティブの影響を推定する。 これらの側面

### 熟語・専門語

- **likelihood**: 尤度。パラメータが与えられたときデータがどれだけ起こりやすいか。

### 要約

- 前のことは、多くの場合、唯一の可能性のコンテキストで理解することができます (Gelman et al., 2017年、ケネディ・エ・アル。

## Chunk 0692

### English（抽出4行）

> models that will be relevant for predicting eﬀects for small incentives in mail surveys are diﬀerent
> from what is relevant for predictions for large incentives in telephone surveys. This is related to
> the discussion of sensitivity analysis in Sections 6.3 and 8.1. For another illustration of this point,
> Rubin (1983) gives an example where the choice of transformation has minor eﬀects on inference

### 日本語訳（自動翻訳）

> メール調査における小規模なインセンティブの影響を予測するモデルは異なる
> 電話調査における大きなインセンティブの予測に関連しているものから。 これは関連しています
> セクション6.3および8.1における感度解析の議論。 この点の別のイラストは、
> ルビン(1983)は、変換の選択が推論にマイナーな効果をもたらす例を与えます

### 熟語・専門語

- **prediction**: 予測。未知/将来/除外データに対する分布や点推定。

### 要約

- メール調査における小規模なインセンティブの影響を予測するモデルは異なる 電話調査における大きなインセンティブの予測に関連しているものから。

## Chunk 0693

### English（抽出4行）

> for the median of a distribution while having large eﬀects on inference for the mean.
> 12.6.
> Going forward
> All workﬂows have holes, and we cannot hope to exhaust all potential ﬂaws of applied data analysis.

### 日本語訳（自動翻訳）

> 意味のための推論に大きな影響を与えている間分布の中央のため。
> 12.6.
> 前へ進む
> ワークフロー全体に穴があり、適用されたデータ分析のあらゆる潜在的な欠陥を排出したいと考えています。

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- 意味のための推論に大きな影響を与えている間分布の中央のため。

## Chunk 0694

### English（抽出4行）

> In the prior and posterior predictive check, a wrong model will pass the check silently for overﬁtting
> all output at the observed values. In simulation based calibration, an incorrect computation program
> can satisfy the diagnostics if the posterior stays in the prior. In cross validation, the consistency
> relies on conditional independence and stationarity of the covariates. In causal inference, there are

### 日本語訳（自動翻訳）

> 前者と後者予測チェックでは、間違ったモデルは、過度にチェックをサイレントに渡します
> 観察値のすべての出力。 シミュレーションベースの校正、誤った計算プログラム
> ポスターが事前に滞在する場合、診断を満たすことができます。 相互検証では、一貫性
> 品種の条件付き独立性と静性に依存します。 原因の侵入では、そこにあります

### 熟語・専門語

- **posterior predictive**: 事後予測。推定後のモデルが観測データの特徴を再現できるかを見る診断。
- **cross validation**: 交差検証。汎化性能を推定するためにデータを分割/近似除外する評価法。
- **validation**: 検証。モデルが目的・データ・外部知識に照らして妥当かを確認すること。

### 要約

- 前者と後者予測チェックでは、間違ったモデルは、過度にチェックをサイレントに渡します 観察値のすべての出力。

## Chunk 0695

### English（抽出4行）

> always untestable causal assumptions, no matter how many models we have ﬁt. More generally,
> statistics relies on some extrapolation, for which some assumption is always needed. To ultimately
> check the model and push the workﬂow forward, we often need to collect more data, along the way
> expanding the model, and an appropriate experiment design will be part of this larger workﬂow.

### 日本語訳（自動翻訳）

> どんなに多くのモデルが合っているか、常に証明できない原因の仮定。 より一般的に、
> 統計はいくつかの余分に頼ります。, いくつかの仮定は常に必要です。. 究極の
> モデルを確認し、ワークフローを先に押します。多くの場合、より多くのデータを収集する必要があります。
> モデルを拡大し、適切な実験設計がこの大きなワークフローの一部です。

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- どんなに多くのモデルが合っているか、常に証明できない原因の仮定。

## Chunk 0696

### English（抽出4行）

> This article has focused on data analysis: the steps leading from data and assumptions to
> scientiﬁc inferences and predictions. Other important aspects of Bayesian statistics not discussed
> here include design, measurement, and data collection (coming before the data analysis) and
> decision making and communication (coming after data analysis). We also have not gone into the

### 日本語訳（自動翻訳）

> この記事はデータ分析に重点を置いています:データと仮定から導き出す手順
> 科学的推論と予測。 ベイジアン統計の他の重要な側面は議論されていない
> 設計、測定、データ収集(データ解析前の対応)、
> 意思決定とコミュニケーション(データ解析後の対応) 私達にまた入っていません

### 熟語・専門語

- **prediction**: 予測。未知/将来/除外データに対する分布や点推定。
- **decision**: 意思決定。予測分布を損失・効用・行動選択へ接続する工程。

### 要約

- この記事はデータ分析に重点を置いています:データと仮定から導き出す手順 科学的推論と予測。

## Chunk 0697

### English（抽出4行）

> details of computing environments or the social and economic aspects of collaboration, sharing of
> data and code, and so forth.
> The list of workﬂow steps we have provided is too long to be a useful guide to practice. What
> can be done? Rather than giving users a 25-item checklist, we hope that we can clarify these

### 日本語訳（自動翻訳）

> コンピューティング環境やコラボレーションの社会的・経済的側面の詳細、共有
> データやコードなど、
> 提供したワークフローの手順のリストは、練習するのに便利なガイドになるまで長いです。 新着情報
> できますか? ユーザに25項目のチェックリストを与えるよりもむしろ、これを明らかにできると願っています

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- コンピューティング環境やコラボレーションの社会的・経済的側面の詳細、共有 データやコードなど、 提供したワークフローの手順のリストは、練習するのに便利なガイドになるまで長いです。

## Chunk 0698

### English（抽出4行）

> processes so they can be applied in a structured or even automated framework. Our rough plan is
> as follows:
> • Abstract these principles from our current understanding of best practice, thus producing the
> present article.

### 日本語訳（自動翻訳）

> プロセスは構造化された、あるいは自動化されたフレームワークでも適用できます。 ラフプランは
> 次のようにします。
> • 最高の練習の私達の現在の理解からのこれらの原則を妨げて下さい、従って作り出します
> 現在の記事。

### 熟語・専門語

- **ESS**: 有効サンプルサイズ。自己相関を考慮した独立サンプル相当数。

### 要約

- プロセスは構造化された、あるいは自動化されたフレームワークでも適用できます。

## Chunk 0699

### English（抽出4行）

> • Apply this workﬂow to some applied problems and write these up as case studies.
> • Implement as much of the workﬂow as possible in software tools for general application.
> Automating what can be automated should enable the statistician or applied researcher to go beyond
> button pushing and integrate data with domain expertise. The ultimate goal of this project is to

### 日本語訳（自動翻訳）

> • このワークフローをいくつかの応用問題に適用し、ケーススタディとしてこれらを書いてください。
> •一般的なアプリケーション用のソフトウェアツールで可能なワークフローの多くを実装します。
> 自動化できるものの自動化は、統計学や応用研究者が、を超えて行くことを可能にする必要があります
> ドメインの専門知識でデータをプッシュおよび統合するボタン。 このプロジェクトの究極の目標は、

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- • このワークフローをいくつかの応用問題に適用し、ケーススタディとしてこれらを書いてください。

## Chunk 0700

### English（抽出4行）

> enable ourselves and other data analysts to use statistical modeling more eﬀectively, and to allow
> us to build conﬁdence in the inferences and decisions that we come to.
> This article is a review, a survey of the territory, a reminder of methods we have used, procedures
> we have followed, and ideas we would like to pursue. To be useful to practitioners, we need worked

### 日本語訳（自動翻訳）

> 自分自身や他のデータアナリストがより効果的に統計的なモデリングを使用することを可能にします。
> 私たちは、私たちが来るべき本質と決定において自信を築きます。
> この記事では、領土の調査、使用した方法のリマインダー、手順のレビューです
> 続いていくと、追求したいアイデア。 実務者にとっては、働きがいのある方

### 熟語・専門語

- **decision**: 意思決定。予測分布を損失・効用・行動選択へ接続する工程。

### 要約

- 自分自身や他のデータアナリストがより効果的に統計的なモデリングを使用することを可能にします。

## Chunk 0701

### English（抽出4行）

> examples with code. We would also like to provide more structure: if not a checklist, at least a
> some paths to follow in a Bayesian analysis. Some guidance is given in the Stan User’s Guide
> (Stan Development Team, 2020), and we are working on a book on Bayesian workﬂow using Stan
> to provide such a resource to novice and experienced statisticians alike. That said, we believe this

### 日本語訳（自動翻訳）

> コードの例 また、より多くの構造を提供したいと思います:チェックリストではない場合、少なくとも
> ベイジアン分析に従うためのいくつかのパス。 スタンユーザーズガイドでガイダンスが与えられる
> (Stan Development Team, 2020) は、Stanを用いたベイジアンワークフローに関する書籍を運営しています。
> 初心者や経験豊富な統計学者にそのようなリソースを提供すること。 つまり、このことを信じます。

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- コードの例 また、より多くの構造を提供したいと思います:チェックリストではない場合、少なくとも ベイジアン分析に従うためのいくつかのパス。

## Chunk 0702

### English（抽出4行）

> paper has value as a ﬁrst step toward putting the many diﬀerent activities of Bayesian workﬂow
> under a single roof.
> References
> Afrabandpey, H., Peltola, T., Piironen, J., Vehtari, A., and Kaski, S. (2020). Making Bayesian

### 日本語訳（自動翻訳）

> 紙はベイジアンのワークフローのさまざまな活動を置くための最初のステップとして価値があります
> 1つの屋根の下に。
> 参考文献
> Afrabandpey, H., Peltola, T., Piironen, J., Vehtari, A., Kaski, S. (2020). ベイジアンを作る

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- 紙はベイジアンのワークフローのさまざまな活動を置くための最初のステップとして価値があります 1つの屋根の下に。

## Chunk 0703

### English（抽出4行）

> predictive models interpretable: A decision theoretic approach. Machine Learning 109, 1855–
> 1876.
> Akaike, H. (1973). Information theory and an extension of the maximum likelihood principle. In
> Proceedings of the Second International Symposium on Information Theory, ed. B. N. Petrov

### 日本語訳（自動翻訳）

> 予測モデル解釈可能:決定理論的アプローチ。 機械学習 109, 1855–
> 1876年(昭和27年)
> 赤池、H. (1973). 情報理論と最大の可能性原則の拡張。 インスタグラム
> 情報理論に関する第2回国際シンポジウムの発表, ed. B. N. Petrov

### 熟語・専門語

- **likelihood**: 尤度。パラメータが与えられたときデータがどれだけ起こりやすいか。
- **decision**: 意思決定。予測分布を損失・効用・行動選択へ接続する工程。

### 要約

- 予測モデル解釈可能:決定理論的アプローチ。

## Chunk 0704

### English（抽出4行）

> and F. Csaki, 267–281. Budapest: Akademiai Kiado. Reprinted in Breakthroughs in Statistics,
> ed. S. Kotz, 610–624. New York: Springer (1992).
> Berger, J. O., Bernardo, J. M., and Sun, D. (2009). The formal deﬁnition of reference priors.
> Annals of Statistics 37, 905–938.

### 日本語訳（自動翻訳）

> F. Csaki, 267–281. ブダペスト: アカデミアキド. 統計のブレークスルーで転載、
> ed. S. Kotz, 610–624. ニューヨーク: スプリング (1992).
> ベルガー、J.O.、ベルナルド、J.M.、サン、D.(2009)。 参照先の正式な定義。
> 統計のアンナルス 37, 905–938.

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- F. Csaki, 267–281. ブダペスト: アカデミアキド. 統計のブレークスルーで転載、 ed. S. Kotz, 610–624. ニューヨーク: スプリング (1992). ベルガー、J.O.、ベルナルド、J.M.、サン…

## Chunk 0705

### English（抽出4行）

> Berk, R., Brown, L., Buja, A., Zhang, K., and Zhao, L. (2013). Valid post-selection inference.
> Annals of Statistics 41, 802–837.
> Berry, D. (1995). Statistics: A Bayesian Perspective. Duxbury Press.
> Betancourt, M. (2017a). A conceptual introduction to Hamiltonian Monte Carlo. arxiv.org/abs/

### 日本語訳（自動翻訳）

> Berk、R.、ブラウン、L.、Buja、A.、Zhang、K.、およびZhao、L.(2013)。 有効なポスト選択の推論。
> 統計のアンナルス 41, 802–837.
> ベリー, D. (1995). 統計:ベイジアンの視点。 ダックスベリープレス。
> Betancourt、M。(2017a)。 ハミルトニアン・モンテ・カルロのコンセプトをご紹介します。 arxiv.org/abs/の

### 熟語・専門語

- **ESS**: 有効サンプルサイズ。自己相関を考慮した独立サンプル相当数。

### 要約

- Berk、R.、ブラウン、L.、Buja、A.、Zhang、K.、およびZhao、L.(2013)。

## Chunk 0706

### English（抽出4行）

> 1701.02434
> Betancourt, M. (2017b). Identifying Bayesian mixture models. Stan Case Studies 4. mc-stan.org/
> users/documentation/case-studies/identifying_mixture_models.html
> Betancourt, M. (2018).

### 日本語訳（自動翻訳）

> 1701.02434
> Betancourt、M。(2017b)。 ベイジアンの混合モデルを識別します。 スタンケーススタディ 4. mc-stan.org/
> user/documentation/case-studies/identification mixture models.html の一覧です。
> Betancourt、M.(2018)。

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- 1701.02434 Betancourt、M。

## Chunk 0707

### English（抽出4行）

> Underdetermined linear regression.
> betanalpha.github.io/assets/case_
> studies/underdetermined_linear_regression.html
> Betancourt, M. (2020a). Towards a principled Bayesian workﬂow. betanalpha.github.io/assets/

### 日本語訳（自動翻訳）

> アンダーデテルミン線形回帰。
> betanalpha.github.io/assets/case  は、
> 学習/理解 linear regression.html
> Betancourt、M。 (2020a)。 Bayesian の原則的なワークフローに向けて betanalpha.github.io/assets/ は、

### 熟語・専門語

- **ESS**: 有効サンプルサイズ。自己相関を考慮した独立サンプル相当数。

### 要約

- アンダーデテルミン線形回帰。

## Chunk 0708

### English（抽出4行）

> case_studies/principled_bayesian_workﬂow.html
> Betancourt, M. (2020b). Robust Gaussian Process Modeling. github.com/betanalpha/knitr_case_
> studies/tree/master/gaussian_processes
> Betancourt, M., and Girolami, M. (2015). Hamiltonian Monte Carlo for hierarchical models. In

### 日本語訳（自動翻訳）

> ケース studies/principled bayesian workflow.html
> Betancourt、M。 (2020b)。 強力なガウスのプロセスモデリング。 github.com/betanalpha/knitr case 
> 勉強/ツリー/マスター/ガウス プロセス
> Betancourt、M.、Girolami、M.(2015)。 階層モデルのハミルトニアモンテカルロ。 インスタグラム

### 熟語・専門語

- **ESS**: 有効サンプルサイズ。自己相関を考慮した独立サンプル相当数。

### 要約

- ケース studies/principled bayesian workflow.html Betancourt、M。

## Chunk 0709

### English（抽出4行）

> Current Trends in Bayesian Methodology with Applications, ed. S. K. Upadhyay, U. Singh, D.
> K. Dey, and A. Loganathan, 79–102.
> Blei, D. M., Kucukelbir, A., and McAuliﬀe, J. D. (2017). Variational inference: A review for
> statisticians. Journal of the American Statistical Association 112, 859–877.

### 日本語訳（自動翻訳）

> ベイジアン法医学における応用動向, ed. S. K. Upadhyay, U. Singh, D.
> K. ディー, A. ロラナサン, 79–102.
> Blei、D.M.、Kucukelbir、A.、McAuliffe、J. D.(2017)。 変種推論:レビュー
> 統計学者。 米国統計協会のジャーナル 112, 859–877.

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- ベイジアン法医学における応用動向, ed. S. K. Upadhyay, U. Singh, D. K. ディー, A. ロラナサン, 79–102. Blei、D.M.、Kucukelbir、A.、McAuliffe、J. D.(…

## Chunk 0710

### English（抽出4行）

> Blitzer, J., Dredze, M., and Pereira, F. (2007). Biographies, Bollywood, boom-boxes and blenders:
> Domain adaptation for sentiment classiﬁcation. In Proceedings of the 45th Annual Meeting of
> the Association of Computational Linguistics, 440–447.
> Box, G. E. P. (1980). Sampling and Bayes inference in scientiﬁc modelling and robustness. Journal

### 日本語訳（自動翻訳）

> Blitzer、J.、Dredze、M.、Pereira、F.(2007)。 バイオグラフィー、ボリウッド、ブームボックス、ブレンダー:
> 送信分類のためのドメイン適応。 第45回定時株主総会招集ご通知
> 計算言語学協会 440–447.
> ボックス, G. E. P. (1980). 科学的モデリングと堅牢性におけるサンプリングとベイスの影響。 セミナー

### 熟語・専門語

- **ESS**: 有効サンプルサイズ。自己相関を考慮した独立サンプル相当数。

### 要約

- Blitzer、J.、Dredze、M.、Pereira、F.(2007)。

## Chunk 0711

### English（抽出4行）

> of the Royal Statistical Society A 143, 383–430.
> Broadie, M. (2018).
> Two simple putting models in golf.
> statmodeling.stat.columbia.edu/

### 日本語訳（自動翻訳）

> ロイヤル統計協会 A 143, 383–430.
> ブロードイ、M.(2018)。
> ゴルフの2つのシンプルなパッティングモデル。
> statmodeling.stat.columbia.edu/

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- ロイヤル統計協会 A 143, 383–430. ブロードイ、M.(2018)。

## Chunk 0712

### English（抽出4行）

> wp-content/uploads/2019/03/putt_models_20181017.pdf
> Bryan, J. (2017). Project-oriented workﬂow. www.tidyverse.org/blog/2017/12/workﬂow-vs-script
> Bürkner, P.-C. (2017). brms: An R Package for Bayesian multilevel models using Stan. Journal of
> Statistical Software 80, 1–28.

### 日本語訳（自動翻訳）

> wp-content/uploads/2019/03/putt models 20181017.pdf
> ブライアン、J.(2017)。 プロジェクト指向のワークフロー。 www.tidyverse.org/blog/2017/12/workflow-vs-script の使い方
> ビュルクナー、P.-C.(2017)。 brms: スタンを使用してベイジアンマルチレベルモデル用のRパッケージ。 ジャーナル
> 統計ソフトウェア 80, 1–28.

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- wp-content/uploads/2019/03/putt models 20181017.pdf ブライアン、J.(2017)。

## Chunk 0713

### English（抽出4行）

> Carpenter, B. (2017). Typical sets and the curse of dimensionality. Stan Case Studies 4. mc-stan.
> org/users/documentation/case-studies/curse-dims.html
> Carpenter, B. (2018). Predator-prey population dynamics: The Lotka-Volterra model in Stan. Stan
> Case Studies 5.

### 日本語訳（自動翻訳）

> カルペンター、B.(2017)。 典型的なセットと寸法の曲線。 スタン・ケース・スタディ 4. mc-stan.
> org/users/documentation/case-studies/curse-dims.html (日本語)
> カルペンター、B.(2018)。 Predator-prey 人口動態: スタンのロッカ・ボルテラモデル。 スタン
> ケーススタディ 5.

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- カルペンター、B.(2017)。

## Chunk 0714

### English（抽出4行）

> mc-stan.org/users/documentation/case-studies/lotka-volterra-predator-prey.
> html
> Carpenter, B., Gelman, A., Hoﬀman, M., Lee, D., Goodrich, B., Betancourt, M., Brubaker, M.,
> Guo, J., Li, P., and Riddell, A. (2017). Stan: A probabilistic programming language. Journal

### 日本語訳（自動翻訳）

> mc-stan.org/users/documentation/case-studies/lotka-volterra-predator-prey.
> ツイート
> Carpenter、B.、Gelman、A.、Hoffman、M.、Lee、D.、Goodrich、B.、Betancourt、M.、Brunbaker、M.、
> Guo、J.、Li、P.、Riddell、A.(2017)。 スタン: 確率的プログラミング言語。 セミナー

### 熟語・専門語

- **probabilistic programming**: 確率的プログラミング。Stanなどで確率モデルをコードとして記述し推論する方法。

### 要約

- mc-stan.org/users/documentation/case-studies/lotka-volterra-predator-prey. ツイート Carpenter、B.、Gelman、A.、Hoffman、M.、Lee…

## Chunk 0715

### English（抽出4行）

> of Statistical Software 76 (1).
> Chen,
> C.,
> Li,

### 日本語訳（自動翻訳）

> 統計ソフトウェア 76 (1).
> チェン,
> C.、
> 李、

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- 統計ソフトウェア 76 (1). チェン, C.、 李、

## Chunk 0716

### English（抽出4行）

> O.,
> Barnett,
> A.,
> Su,

### 日本語訳（自動翻訳）

> お問い合わせ
> バーネット、
> お問い合わせ
> お問い合わせ

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- お問い合わせ バーネット、 お問い合わせ お問い合わせ

## Chunk 0717

### English（抽出4行）

> J.,
> and Rudin,
> C. (2019).
> This looks like

### 日本語訳（自動翻訳）

> J.、
> そしてルディン、
> (2019年)
> こんな感じです

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- J.、 そしてルディン、 (2019年) こんな感じです

## Chunk 0718

### English（抽出4行）

> that:
> Deep learning for interpretable image recognition.
> 33rd Conference on Neu-
> ral Information Processing Systems.

### 日本語訳（自動翻訳）

> その:
> 通訳可能な画像認識のためのディープラーニング
> 第33回Neu会議
> ラル情報処理システム。

### 熟語・専門語

- **ESS**: 有効サンプルサイズ。自己相関を考慮した独立サンプル相当数。

### 要約

- その: 通訳可能な画像認識のためのディープラーニング 第33回Neu会議 ラル情報処理システム。

## Chunk 0719

### English（抽出4行）

> papers.nips.cc/paper/9095-this-looks-like-that-deep-
> learning-for-interpretable-image-recognition.pdf
> Chiu, W. A., Wright, F. A., and Rusyn, I. (2017). A tiered, Bayesian approach to estimating of
> population variability for regulatory decision-making. ALTEX 34, 377–388.

### 日本語訳（自動翻訳）

> papers.nips.cc/paper/9095-this-looks-like-that-deep-
> 学習のための解釈可能な画像認識.pdf
> Chiu、W. A.、Wright、F. A.、Rusyn、I.(2017)。 結ばれたベイジアンは、
> 規制決定のための人口の変動性。 ALTEX 34、377-388。

### 熟語・専門語

- **decision**: 意思決定。予測分布を損失・効用・行動選択へ接続する工程。

### 要約

- papers.nips.cc/paper/9095-this-looks-like-that-deep- 学習のための解釈可能な画像認識.pdf Chiu、W. A.、Wright、F. A.、Rusyn、I.(2017)。

## Chunk 0720

### English（抽出4行）

> Chung, Y., Rabe-Hesketh, S., Gelman, A., Liu, J. C., and Dorie, A. (2013). A non-degenerate
> penalized likelihood estimator for hierarchical variance parameters in multilevel models. Psy-
> chometrika 78, 685–709.
> Chung, Y., Rabe-Hesketh, S., Gelman, A., Liu, J. C., and Dorie, A. (2014). Nonsingular covariance

### 日本語訳（自動翻訳）

> Chung, Y., Rabe-Hesketh, S., ゲルマン, A., 劉, J. C., ドリー, A. (2013). 非生成
> 多重レベルのモデルの階層的な分散変数のための浸透させた尤度推定器。 プッシー
> chometrika 78, 685–709.
> Chung, Y., Rabe-Hesketh, S., ゲルマン, A., 劉, J. C., ドリー, A. (2014). ノンシンギュラー共鳴

### 熟語・専門語

- **likelihood**: 尤度。パラメータが与えられたときデータがどれだけ起こりやすいか。

### 要約

- Chung, Y., Rabe-Hesketh, S., ゲルマン, A., 劉, J. C., ドリー, A. (2013). 非生成 多重レベルのモデルの階層的な分散変数のための浸透させた尤度推定器。

## Chunk 0721

### English（抽出4行）

> estimation in linear mixed models through weakly informative priors. Journal of Educational
> and Behavioral Statistics 40, 136–157.
> Clayton, D. G. (1992). Models for the analysis of cohort and case-control studies with inaccurately
> measured exposures. In Statistical Models for Longitudinal Studies of Exposure and Health, ed.

### 日本語訳（自動翻訳）

> 弱く有益な事前による線形混合モデルの推定。 教育ジャーナル
> 行動統計 40, 136–157.
> クレイトン, D. G. (1992). 不正確でコホートとケースコントロールの研究の分析のためのモデル
> 測定された露出。 長期間にわたる曝露と健康に関する統計的モデルで、ed。

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- 弱く有益な事前による線形混合モデルの推定。

## Chunk 0722

### English（抽出4行）

> J. H. Dwyer, M. Feinleib, P. Lippert, and H. Hoﬀmeister, 301–331. Oxford University Press.
> Cook, S., Gelman, A., and Rubin, D. B. (2006). Validation of software for Bayesian models using
> posterior quantiles. Journal of Computational and Graphical Statistics 15, 675–692.
> Daumé, H. (2009). Frustratingly easy domain adaptation. arxiv.org/abs/0907.1815

### 日本語訳（自動翻訳）

> J. H. Dwyer、M. Feinleib、P. Lippert、H. H. H.ホフマイスター、301–331。 オックスフォード大学プレス
> クック、S.、ゲルマン、A.、ルビン、D.B.(2006)。 ベイジアンモデルのソフトウェアの検証
> ポスター 量子。 計算統計とグラフィック統計のジャーナル 15, 675–692.
> ダムエ、H.(2009)。 非常に容易なドメイン適応。 arxiv.org/abs/0907.1815の特長

### 熟語・専門語

- **ESS**: 有効サンプルサイズ。自己相関を考慮した独立サンプル相当数。
- **validation**: 検証。モデルが目的・データ・外部知識に照らして妥当かを確認すること。

### 要約

- J. H. Dwyer、M. Feinleib、P. Lippert、H. H. H.ホフマイスター、301–331。

## Chunk 0723

### English（抽出4行）

> Deming, W. E., and Stephan, F. F. (1940). On a least squares adjustment of a sampled frequency
> table when the expected marginal totals are known. Annals of Mathematical Statistics 11,
> 427–444.
> Devezer, B., Nardin, L. G., Baumgaertner, B., and Buzbas, E. O. (2019). Scientiﬁc discovery in a

### 日本語訳（自動翻訳）

> デミング、W.E.、ステファン、F.F.(1940)。 サンプル頻度の少なくとも正方形の調節
> 予想された総数が知られているテーブル。 数学統計のアンナルス 11,
> 427-444.(昭和45年)
> Devezer、B.、Nadin、L. G.、Baumgaertner、B.、Buzbas、E. O.(2019)。 科学研究

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- デミング、W.E.、ステファン、F.F.(1940)。

## Chunk 0724

### English（抽出4行）

> model-centric framework: Reproducibility, innovation, and epistemic diversity. PLoS One 14,
> e0216125.
> Devezer, B., Navarro, D. J., Vanderkerckhove, J., and Buzbas, E. O. (2020). The case for formal
> methodology in scientiﬁc reform. doi.org/10.1101/2020.04.26.048306

### 日本語訳（自動翻訳）

> モデル中心のフレームワーク: 再現性、革新および流行の多様性。 PLoS 1、14
> e0216125。
> Devezer、B.、Navarro、D. J.、Vanderkerckhove、J.、およびBuzbas、E. O.(2020)。 正式な場合
> 科学的改革における方法論。 2018年10月10日

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- モデル中心のフレームワーク: 再現性、革新および流行の多様性。

## Chunk 0725

### English（抽出4行）

> Dragicevic, P., Jansen, Y., Sarma, A., Kay, M., and Chevalier, F. (2019). Increasing the trans-
> parency of research papers with explorable multiverse analyses. Proceedings of the 2019 CHI
> Conference on Human Factors in Computing Systems, paper no. 65.
> Efron, B. (2013).

### 日本語訳（自動翻訳）

> Dragicevic、P.、Jansen、Y.、サルマ、A.、ケイ、M.、およびChevalier、F.(2019)。 トランスを増やす-
> 探索可能な多面分析による研究論文のパーテンシー。 2019 CHIの実績
> コンピュータシステム、紙番号65の人的要因に関する会議。
> エフロン、B.(2013)。

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- Dragicevic、P.、Jansen、Y.、サルマ、A.、ケイ、M.、およびChevalier、F.(2019)。

## Chunk 0726

### English（抽出4行）

> Estimation and accuracy after model selection.
> Journal of the American
> Statistical Association 109, 991–1007.
> Finkel, J. R., and Manning, C. D. (2009). Hierarchical Bayesian domain adaptation. In Proceedings

### 日本語訳（自動翻訳）

> モデル選択後の見積もりと精度。
> アメリカジャーナル
> 統計協会 109,991–1007.
> フィンケル、J. R.、マニング、C. D.(2009)。 Hierarchical Bayesianドメインの適応。 職業紹介

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- モデル選択後の見積もりと精度。

## Chunk 0727

### English（抽出4行）

> of Human Language Technologies: The 2009 Annual Conference of the North American Chapter
> of the Association for Computational Linguistics, 602–610.
> Fithian, W., Taylor, J., Tibshirani, R., and Tibshirani, R. J. (2015). Selective sequential model
> selection. arxiv.org/pdf/1512.02565.pdf

### 日本語訳（自動翻訳）

> ヒューマン・ランゲージ・テクノロジーズ:2009年北米支部年次会議
> 計算言語学協会, 602–610.
> Fithian、W.、テイラー、J.、Tibshirani、R.、Tibshirani、R. J.(2015)。 選択式シーケンシャルモデル
> 選択。 arxiv.org/pdf/1512.02565.pdf

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- ヒューマン・ランゲージ・テクノロジーズ:2009年北米支部年次会議 計算言語学協会, 602–610. Fithian、W.、テイラー、J.、Tibshirani、R.、Tibshirani、R. J.(2015)。

## Chunk 0728

### English（抽出4行）

> Flaxman, S., Mishra, S., Gandy, A., et al. (2020). Estimating the eﬀects of non-pharmaceutical
> interventions on COVID-19 in Europe. Nature 584, 257–261. Data and code at github.com/
> ImperialCollegeLondon/covid19model
> Fuglstad, G. A., Simpson, D., Lindgren, F., and Rue, H. (2019). Constructing priors that penalize

### 日本語訳（自動翻訳）

> フラックスマン、S.、ミシュラ、S.、ガンディー、A.、ら。 (2020) 非医薬品の効果を推定する
> 欧州でCOVID-19の介入. 自然 584, 257–261. github.com/でのデータとコード
> ImperialCollegeLondon/covid19モデル
> Fuglstad、G. A.、シンプソン、D.、リンドレン、F.、Rue、H.(2019)。 罰する前の指示

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- フラックスマン、S.、ミシュラ、S.、ガンディー、A.、ら。

## Chunk 0729

### English（抽出4行）

> the complexity of Gaussian random ﬁelds. Journal of the American Statistical Association 114,
> 445–452.
> Gabry, J., et al. (2020a). rstanarm: Bayesian applied regression modeling via Stan, version 2.19.3.
> cran.r-project.org/package=rstanarm

### 日本語訳（自動翻訳）

> Gaussianランダムフィールドの複雑さ。 アメリカ統計協会のジャーナル 114,
> 445–452.
> Gabry, J., ら. (2020a). rstanarm: Bayesian は Stan 版 2.19.3 による回帰モデルを適用しました。
> cran.rプロジェクト.org/package=rstanarm

### 熟語・専門語

- **ESS**: 有効サンプルサイズ。自己相関を考慮した独立サンプル相当数。

### 要約

- Gaussianランダムフィールドの複雑さ。

## Chunk 0730

### English（抽出4行）

> Gabry, J., et al. (2020b). bayesplot: Plotting for Bayesian models, version 1.7.2. cran.r-project.
> org/package=bayesplot
> Gabry, J., Simpson, D., Vehtari, A., Betancourt, M., and Gelman, A. (2019). Visualization in
> Bayesian workﬂow (with discussion and rejoinder). Journal of the Royal Statistical Society A

### 日本語訳（自動翻訳）

> Gabry, J., ら. (2020b). bayesplot: ベイジアンモデルのプロット, バージョン 1.7.2. cran.r-project.
> org/package=ベイズプロット
> Gabry、J.、Simpson、D.、Vehtari、A.、Betancourt、M.、およびGelman、A.(2019)。 可視化
> ベイジアンワークフロー(ディスカッションとリバインダー付き)。 ロイヤル統計協会Aのジャーナル

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- Gabry, J., ら. (2020b). bayesplot: ベイジアンモデルのプロット, バージョン 1.7.2. cran.r-project. org/package=ベイズプロット Gabry、J.、Simpson、D.…

## Chunk 0731

### English（抽出4行）

> 182, 389–441.
> Gelman, A., Bois, F. Y., and Jiang, J. (1996).
> Physiological pharmacokinetic analysis using
> population modeling and informative prior distributions. Journal of the American Statistical

### 日本語訳（自動翻訳）

> 182、389–441。
> ゲルマン、A.、Bois、F. Y、江、J. (1996)。
> 生理学的医薬品分析による
> 人口のモデリングと有益な事前分布。 アメリカン統計ジャーナル

### 熟語・専門語

- **prior distribution**: 事前分布。データ観測前の知識・制約を表す分布。

### 要約

- 182、389–441。

## Chunk 0732

### English（抽出4行）

> Association 91, 1400–1412.
> Gelman, A. (2003).
> A Bayesian formulation of exploratory data analysis and goodness-of-ﬁt
> testing. International Statistical Review 71, 369–382.

### 日本語訳（自動翻訳）

> 協会 91,1400–1412.
> ゲルマン、A.(2003)。
> 探索的データ解析と適性性に関するベイジアン処方
> テスト。 国際統計レビュー 71, 369–382.

### 熟語・専門語

- **ESS**: 有効サンプルサイズ。自己相関を考慮した独立サンプル相当数。

### 要約

- 協会 91,1400–1412. ゲルマン、A.(2003)。

## Chunk 0733

### English（抽出4行）

> Gelman, A. (2004). Parameterization and Bayesian modeling. Journal of the American Statistical
> Association 99, 537–545.
> Gelman, A. (2011).
> Expanded graphical models:

### 日本語訳（自動翻訳）

> ゲルマン、A.(2004)。 パラメータ化とベイジアンモデリング。 アメリカン統計ジャーナル
> 協会 99, 537–545.
> ゲルマン、A.(2011)。
> 拡大された写実的なモデル:

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- ゲルマン、A.(2004)。

## Chunk 0734

### English（抽出4行）

> Inference, model comparison, model
> checking, fake-data debugging, and model understanding. www.stat.columbia.edu/~gelman/
> presentations/ggr2handout.pdf
> Gelman, A. (2014). How do we choose our default methods? In Past, Present, and Future of

### 日本語訳（自動翻訳）

> 推論、モデル比較、モデル
> チェック、偽データデバッグ、モデル理解。 www.stat.columbia.edu/~ゲルマン/
> プレゼンテーション/ggr2handout.pdf
> ゲルマン、A.(2014)。 デフォルトメソッドを選択するにはどうすればよいですか? 過去・現在・未来

### 熟語・専門語

- **model comparison**: モデル比較。LOO-CVなどで複数モデルの予測性能や弱点を比較すること。

### 要約

- 推論、モデル比較、モデル チェック、偽データデバッグ、モデル理解。

## Chunk 0735

### English（抽出4行）

> Statistical Science, ed. X. Lin, C. Genest, D. L. Banks, G. Molenberghs, D. W. Scott, and J. L.
> Wang. London: CRC Press.
> Gelman, A. (2019). Model building and expansion for golf putting. Stan Case Studies 6. mc-stan.
> org/users/documentation/case-studies/golf.html

### 日本語訳（自動翻訳）

> 統計科学, ed. X. Lin, C. Genest, D. L. Banks, G. Molenberghs, D. W. スコット, J. L.
> ワン。 ロンドン:CRCプレス。
> ゲルマン、A.(2019)。 ゴルフパッティングのモデル構築と展開 スタンケーススタディ 6. mc-スタン.
> org/users/ドキュメント/case-studies/golf.html

### 熟語・専門語

- **ESS**: 有効サンプルサイズ。自己相関を考慮した独立サンプル相当数。
- **model building**: モデル構築。仮定・データ構造・prior・likelihoodを組み合わせる工程。

### 要約

- 統計科学, ed. X. Lin, C. Genest, D. L. Banks, G. Molenberghs, D. W. スコット, J. L. ワン。

## Chunk 0736

### English（抽出4行）

> Gelman, A., et al. (2020).
> Prior choice recommendations.
> github.com/stan-dev/stan/wiki/
> Prior-Choice-Recommendations

### 日本語訳（自動翻訳）

> ゲルマン, A., ら. (2020).
> 事前の推奨事項。
> github.com/stan-dev/stan/wiki/
> 事前選択推奨事項

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- ゲルマン, A., ら. (2020). 事前の推奨事項。

## Chunk 0737

### English（抽出4行）

> Gelman, A., and Azari, J. (2017). 19 things we learned from the 2016 election (with discussion).
> Statistics and Public Policy 4, 1–10.
> Gelman, A., Carlin, J. B., Stern, H. S., Dunson, D. B., Vehtari, A., and Rubin, D. B. (2013).
> Bayesian Data Analysis, third edition. London: CRC Press.

### 日本語訳（自動翻訳）

> ゲルマン、A、アザーリ、J(2017)。 2016年選挙で学んだ19点(ディスカッション付き)
> 統計と公共政策4、1～10。
> ゲルマン、A.、カーリン、J.B.、スタン、H.S.、ダンソン、D.B.、Vehtari、A.、およびルビン、D.B.(2013)。
> ベイジアンデータ分析、第3版。 ロンドン:CRCプレス。

### 熟語・専門語

- **ESS**: 有効サンプルサイズ。自己相関を考慮した独立サンプル相当数。

### 要約

- ゲルマン、A、アザーリ、J(2017)。

## Chunk 0738

### English（抽出4行）

> Gelman, A., and Hill, J. (2007). Data Analysis Using Regression and Multilevel/Hierarchical
> Models. Cambridge University Press.
> Gelman, A., Hill, J., and Vehtari, A. (2020). Regression and Other Stories. Cambridge University
> Press.

### 日本語訳（自動翻訳）

> ゲルマン、A.、ヒル、J.(2007) 回帰とマルチレベル/階層を用いたデータ解析
> モデル。 ケンブリッジ大学プレス。
> ゲルマン、A.、ヒル、J.、Vehtari、A.(2020)。 回帰とその他のストーリー。 ケンブリッジ大学
> プレス。

### 熟語・専門語

- **ESS**: 有効サンプルサイズ。自己相関を考慮した独立サンプル相当数。

### 要約

- ゲルマン、A.、ヒル、J.(2007) 回帰とマルチレベル/階層を用いたデータ解析 モデル。

## Chunk 0739

### English（抽出4行）

> Gelman, A., Hill, J., and Yajima, M. (2012). Why we (usually) don’t have to worry about multiple
> comparisons. Journal of Research on Educational Eﬀectiveness 5, 189–211.
> Gelman, A., Hullman, J., Wlezien, C., and Morris, G. E. (2020). Information, incentives, and goals
> in election forecasts. Judgment and Decision Making 15, 863–880.

### 日本語訳（自動翻訳）

> ゲルマン、A.、ヒル、J.、矢島、M.(2012)。 なぜ私たちは(通常)複数の心配する必要はありません
> 比較。 教育効果に関する研究のジャーナル 5, 189–211.
> ゲルマン、A.、ハルマン、J.、Wlezien、C.、モーリス、G.E.(2020)。 情報、インセンティブ、目標
> 選挙予測で. 判決と意思決定 15, 863–880.

### 熟語・専門語

- **ESS**: 有効サンプルサイズ。自己相関を考慮した独立サンプル相当数。
- **decision**: 意思決定。予測分布を損失・効用・行動選択へ接続する工程。

### 要約

- ゲルマン、A.、ヒル、J.、矢島、M.(2012)。

## Chunk 0740

### English（抽出4行）

> Gelman, A., and Loken, E. (2013). The garden of forking paths: Why multiple comparisons can be a
> problem, even when there is no “ﬁshing expedition” or “p-hacking” and the research hypothesis
> was posited ahead of time. www.stat.columbia.edu/~gelman/research/unpublished/forking.pdf
> Gelman, A., Meng, X. L., and Stern, H. S. (1996). Posterior predictive assessment of model ﬁtness

### 日本語訳（自動翻訳）

> ゲルマン、A.、ロケン、E.(2013)。 フォークパスの庭: 複数の比較が複数ある理由
> 問題は、「釣りのexpedition」または「p-hacking」および研究の仮説がない場合でも
> 先ほど前々にポジショニングされた。 www.stat.columbia.edu/~gelman/research/unpublished/forking.pdf
> ゲルマン、A.、メング、X.L.、Stern、H.S.(1996)。 モデルフィットネスのポスター予測評価

### 熟語・専門語

- **posterior predictive**: 事後予測。推定後のモデルが観測データの特徴を再現できるかを見る診断。
- **ESS**: 有効サンプルサイズ。自己相関を考慮した独立サンプル相当数。

### 要約

- ゲルマン、A.、ロケン、E.(2013)。

## Chunk 0741

### English（抽出4行）

> via realized discrepancies (with discussion). Statistica Sinica 6, 733–807.
> Gelman, A., Simpson, D., and Betancourt, M. (2017). The prior can often only be understood in
> the context of the likelihood. Entropy 19, 555.
> Gelman, A., Stevens, M., and Chan, V. (2003). Regression modeling and meta-analysis for decision

### 日本語訳（自動翻訳）

> 気づいた矛盾(ディスカッション付き)で。 統計学 Sinica 6, 733–807.
> ゲルマン、A.、シンプソン、D.、ベタクール、M.(2017)。 事前に理解できるのは、
> 可能性の状況。 エントロピー 19, 555.
> ゲルマン、A.、スティーブンス、M.、チャン、V.(2003)。 決定のための回帰モデリングとメタ解析

### 熟語・専門語

- **likelihood**: 尤度。パラメータが与えられたときデータがどれだけ起こりやすいか。
- **ESS**: 有効サンプルサイズ。自己相関を考慮した独立サンプル相当数。
- **decision**: 意思決定。予測分布を損失・効用・行動選択へ接続する工程。

### 要約

- 気づいた矛盾(ディスカッション付き)で。

## Chunk 0742

### English（抽出4行）

> making: A cost-beneﬁt analysis of a incentives in telephone surveys. Journal of Business and
> Economic Statistics 21, 213–225.
> Gharamani, Z., Steinruecken, C., Smith, E., Janz, E., and Peharz, R. (2019). The Automatic
> Statistician: An artiﬁcial intelligence for data science. www.automaticstatistician.com/index

### 日本語訳（自動翻訳）

> 作り:電話調査のインセンティブの費用対効果分析。 ビジネスジャーナル
> 経済統計 21, 213–225.
> Gharamani、Z.、Steinruecken、C.、Smith、E.、Jans、E.、およびPeharz、R.(2019)。 自動化
> 統計学:データサイエンスの人工知能 www.automaticstatistician.com/index.html からのツイート

### 熟語・専門語

- **ESS**: 有効サンプルサイズ。自己相関を考慮した独立サンプル相当数。

### 要約

- 作り:電話調査のインセンティブの費用対効果分析。

## Chunk 0743

### English（抽出4行）

> Ghitza, Y., and Gelman, A. (2020). Voter registration databases and MRP: Toward the use of large
> scale databases in public opinion research. Political Analysis 28, 507–531.
> Giordano, R. (2018). StanSensitivity. github.com/rgiordan/StanSensitivity
> Giordano, R., Broderick, T., and Jordan, M. I. (2018). Covariances, robustness, and variational

### 日本語訳（自動翻訳）

> Ghitza、Y、ゲルマン、A.(2020)。 投票者登録データベースとMRP:大規模な利用に向けて
> パブリック・オピニオン研究のスケール・データベース。 政治分析 28, 507–531.
> Giordano、R.(2018)。 スタンセンシティブ。 github.com/rgiordan/StanSensitivity
> Giordano、R.、Broderick、T.、ヨルダン、M.I.(2018)。 品種、堅牢性、バリエーション

### 熟語・専門語

- **ESS**: 有効サンプルサイズ。自己相関を考慮した独立サンプル相当数。

### 要約

- Ghitza、Y、ゲルマン、A.(2020)。

## Chunk 0744

### English（抽出4行）

> Bayes. Journal of Machine Learning Research 19, 1981–2029.
> Goel, P. K., and DeGroot, M. H. (1981). Information about hyperparameters in hierarchical models.
> Journal of the American Statistical Association 76, 140–147.
> Grinsztajn, L., Semenova, E., Margossian, C. C., and Riou, J. (2020). Bayesian workﬂow for dis-

### 日本語訳（自動翻訳）

> ベイズ。 1981年～2029年 機械学習研究ジャーナル
> ゴエル、P.K、DeGroot、M.H.(1981)。 階層モデルのハイパーパラメータに関する情報。
> 米国統計協会のジャーナル 76, 140–147.
> Grinsztajn, L., Semenova, E., マルゴシアン, C., リオウ, J. (2020). ベイジアンワークフローを解除

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- ベイズ。

## Chunk 0745

### English（抽出4行）

> ease transmission modeling in Stan. mc-stan.org/users/documentation/case-studies/boarding_
> school_case_study.html
> Grolemund, G., and Wickham, H. (2017). R for Data Science. Sebastopol, Calif.: O’Reilly Media.
> Gunning, D. (2017). Explainable artiﬁcial intelligence (xai). U.S. Defense Advanced Research

### 日本語訳（自動翻訳）

> スタンで送信モデリングを容易にします。 mc-stan.org/users/documentation/case-studies/boarding 
> 学校 case study.html
> Grolemund、G.、Wickham、H.(2017)。 データサイエンスの研究開発 Sebastopol、Calif。:O'Reillyメディア。
> ガンニング, D. (2017). 卓越した人工知能(xai)。 米国防衛高度研究

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- スタンで送信モデリングを容易にします。

## Chunk 0746

### English（抽出4行）

> Projects Agency (DARPA) Program.
> Henderson, C. R. (1950). Estimation of genetic parameters (abstract). Annals of Mathematical
> Statistics 21, 309–310.
> Hill, J. L. (2011). Bayesian nonparametric modeling for causal inference. Journal of Computational

### 日本語訳（自動翻訳）

> プロジェクトエージェンシー(DARPA)プログラム
> ヘンダーソン, C. R. (1950). 遺伝的パラメータ(抽象)の推定。 数学のアンナルス
> 統計 21, 309–310.
> ヒル, J. L. (2011). 航海用非パラメトリックモデリング。 計算ジャーナル

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- プロジェクトエージェンシー(DARPA)プログラム ヘンダーソン, C. R. (1950). 遺伝的パラメータ(抽象)の推定。

## Chunk 0747

### English（抽出4行）

> and Graphical Statistics 20, 217–240.
> Hodges, J. S., and Reich, B. J. (2010). Adding spatially-correlated errors can mess up the ﬁxed
> eﬀect you love. American Statistician 64, 325–334.
> Hoﬀman, M., and Ma, Y. (2020). Black-box variational inference as a parametric approximation

### 日本語訳（自動翻訳）

> 統計データ 20, 217–240.
> ホッジ、J.S.、レイチ、B.J.(2010)。 空間的に関連したエラーを追加すると、固定されたエラーを混乱させることができます
> あなたが愛する効果。 アメリカの統計学 64, 325–334.
> Hoffman, M., Ma, Y. (2020). パラメトリック近似としてのブラックボックスのバリエーション推論

### 熟語・専門語

- **ESS**: 有効サンプルサイズ。自己相関を考慮した独立サンプル相当数。

### 要約

- 統計データ 20, 217–240. ホッジ、J.S.、レイチ、B.J.(2010)。

## Chunk 0748

### English（抽出4行）

> to Langevin dynamics. Proceedings of Machine Learning and Systems, in press.
> Hunt, A., and Thomas, D. (1999). The Pragmatic Programmer. Addison-Wesley.
> Hwang, Y., Tong, A. and Choi, J. (2016). The Automatic Statistician: A relational perspective.
> ICML 2016: Proceedings of the 33rd International Conference on Machine Learning.

### 日本語訳（自動翻訳）

> ランゲビンダイナミクスに。 プレスで機械学習とシステムの生産
> Hunt, A., トーマス, D. (1999). 実用的なプログラマー。 アディソン・ウェスレー
> Hwang、Y.、Tong、A.、Cei、J.(2016)。 自動統計学: リレーショナルな視点。
> ICML 2016:第33回機械学習国際会議の発表

### 熟語・専門語

- **ESS**: 有効サンプルサイズ。自己相関を考慮した独立サンプル相当数。

### 要約

- ランゲビンダイナミクスに。

## Chunk 0749

### English（抽出4行）

> Jacquez, J. A. (1972). Compartmental Analysis in Biology and Medicine. Elsevier.
> Kale, A., Kay, M., and Hullman, J. (2019).
> Decision-making under uncertainty in research
> synthesis: Designing for the garden of forking paths. Proceedings of the 2019 CHI Conference

### 日本語訳（自動翻訳）

> ジャック, J. A. (1972). 生物学と医学におけるコンパートメント分析 エルセビア。
> ケール、A.、ケイ、M.、ハルマン、J.(2019)。
> 研究における不確実性に基づく意思決定
> 合成: フォークパスの庭の設計。 2019 CHI会議の実績

### 熟語・専門語

- **uncertainty**: 不確実性。観測・パラメータ・モデル構造・意思決定に残る曖昧さ。
- **decision**: 意思決定。予測分布を損失・効用・行動選択へ接続する工程。

### 要約

- ジャック, J. A. (1972). 生物学と医学におけるコンパートメント分析 エルセビア。

## Chunk 0750

### English（抽出4行）

> on Human Factors in Computing Systems, paper no. 202.
> Kamary, K., Mengersen, K., Robert, C. P., and Rousseau, J. (2019). Testing hypotheses via a
> mixture estimation model. arxiv.org/abs/1412.2044
> Katz,

### 日本語訳（自動翻訳）

> 計算システム、紙番号202の人的要因。
> カマリー、K.、メンガーセン、K.、ロバート、C.P.、ルソー、J.(2019)。 による仮説のテスト
> 混合推定モデル。 arxiv.org/abs/1412.2044の特長
> カッツ、

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- 計算システム、紙番号202の人的要因。

## Chunk 0751

### English（抽出4行）

> J. (2016).
> Who will be president?
> www.nytimes.com/interactive/2016/upshot/
> presidential-polls-forecast.html

### 日本語訳（自動翻訳）

> (2016年)
> 社長は誰ですか?
> www.nytimes.com/interactive/2016/upshot/
> プレジデンシャルポール・フォレキャスト.html

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- (2016年) 社長は誰ですか? www.nytimes.com/interactive/2016/upshot/ プレジデンシャルポール・フォレキャスト.html

## Chunk 0752

### English（抽出4行）

> Kay, M. (2020a). ggdist: Visualizations of distributions and uncertainty. R package version 2.2.0.
> mjskay.github.io/ggdist. doi:10.5281/zenodo.3879620.
> Kay, M. (2020b). tidybayes: Tidy data and geoms for Bayesian models. R package version 2.1.1.
> mjskay.github.io/tidybayes. doi:10.5281/zenodo.1308151.

### 日本語訳（自動翻訳）

> ケイ, M. (2020a). ggdist:分布と不確実性の可視化 Rパッケージバージョン 2.2.0.
> mjskay.github.io/ggdist. doi:10.5281/zenodo.3879620.
> ケイ, M. (2020b). tidybayes:ベイジアンモデルのティディデータとジオム。 Rパッケージバージョン 2.1.1.
> mjskay.github.io/tidybayes. doi:10.5281/zenodo.1308151.

### 熟語・専門語

- **uncertainty**: 不確実性。観測・パラメータ・モデル構造・意思決定に残る曖昧さ。

### 要約

- ケイ, M. (2020a). ggdist:分布と不確実性の可視化 Rパッケージバージョン 2.2.0. mjskay.github.io/ggdist. doi:10.5281/zenodo.3879620. ケイ, M. (20…

## Chunk 0753

### English（抽出4行）

> Kennedy, L., Simpson, D., and Gelman, A. (2019).
> The experiment is just as important as
> the likelihood in understanding the prior: A cautionary note on robust cognitive modeling.
> Computational Brain and Behavior 2, 210–217.

### 日本語訳（自動翻訳）

> ケネディ、L.、シンプソン、D.、ゲルマン、A.(2019)。
> 実験は、まさに重要なことです。
> 前の理解の可能性: 強力な認知モデルに関する注意深いメモ。
> 計算脳と行動2、210–217。

### 熟語・専門語

- **likelihood**: 尤度。パラメータが与えられたときデータがどれだけ起こりやすいか。

### 要約

- ケネディ、L.、シンプソン、D.、ゲルマン、A.(2019)。

## Chunk 0754

### English（抽出4行）

> Kerman, J., and Gelman, A. (2004). Fully Bayesian computing. www.stat.columbia.edu/~gelman/
> research/unpublished/fullybayesiancomputing-nonblinded.pdf
> Kerman, J., and Gelman, A. (2007). Manipulating and summarizing posterior simulations using
> random variable objects. Statistics and Computing 17, 235–244.

### 日本語訳（自動翻訳）

> ケルマン、J、ゲルマン、A.(2004)。 ベイジアン・コンピューティング www.stat.columbia.edu/~ゲルマン/
> 研究/未発表/fullybayesiancomputing-nonblinded.pdf
> ケルマン、J、ゲルマン、A.(2007) ポスターシミュレーションの操作とまとめ
> ランダム変数オブジェクト。 統計と計算 17, 235–244.

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- ケルマン、J、ゲルマン、A.(2004)。

## Chunk 0755

### English（抽出4行）

> Kucukelbir, A., Tran, D., Ranganath, R., Gelman, A., and Blei, D. M. (2017). Automatic diﬀeren-
> tiation variational inference. Journal of Machine Learning Research 18, 1–45.
> Kumar, R., Carroll, C., Hartikainen, A., and Martin, O. A. (2019).
> ArviZ a uniﬁed library

### 日本語訳（自動翻訳）

> Kucukelbir、A.、Tran、D.、Ranganath、R.、Gelman、A.、Blei、D.M.(2017)。 自動差異-
> 結束の変動推論。 機械学習研究のジャーナル 18, 1–45.
> クマール、R.、カルロール、C.、ハルチカイン、A.、マーティン、O.A.(2019)。
> ArviZ の統一されたライブラリ

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- Kucukelbir、A.、Tran、D.、Ranganath、R.、Gelman、A.、Blei、D.M.(2017)。

## Chunk 0756

### English（抽出4行）

> for exploratory analysis of Bayesian models in Python. Journal of Open Source Software,
> doi:10.21105/joss.01143.
> Lambert, B., and Vehtari, A. (2020). R∗: A robust MCMC convergence diagnostic with uncertainty
> using gradient-boosted machines. arxiv.org/abs/2003.07900

### 日本語訳（自動翻訳）

> Pythonのベイジアンモデルの探索解析 オープンソースソフトウェアのジャーナル、
> 土井:10.21105/jos.01143.
> Lambert、B、Vehtari、A.(2020)。 R∗: 堅牢なMCMCコンバージェンス診断と不確実性
> グラデーション・ブームの機械を使用して。 arxiv.org/abs/2003.07900の特長

### 熟語・専門語

- **uncertainty**: 不確実性。観測・パラメータ・モデル構造・意思決定に残る曖昧さ。

### 要約

- Pythonのベイジアンモデルの探索解析 オープンソースソフトウェアのジャーナル、 土井:10.21105/jos.01143. Lambert、B、Vehtari、A.(2020)。

## Chunk 0757

### English（抽出4行）

> Lee, M. D., Criss, A. H., Devezer, B., Donkin, C., Etz, A., Leite, F. P., Matzke, D., Rouder, J. N.,
> Trueblood, J. S., White, C. N., and Vandekerckhove, J. (2019). Robust modeling in cognitive
> science. Computational Brain and Behavior 2, 141–153.
> Lin, C. Y., Gelman, A., Price, P. N., and Krantz, D. H. (1999). Analysis of local decisions using

### 日本語訳（自動翻訳）

> 李、M. D.、Criss、A. H.、Devezer、B.、Donkin、C.、Etz、A.、Leite、F. P.、Matzke、D.、Ruader、J.、
> Trueblood、J. S.、White、C.N.、Vanddekerckhove、J.(2019)。 認知の強力なモデリング
> 科学。 計算式脳と行動2、141–153。
> リン、C.Y.、ゲルマン、A.、価格、P.N.、Krantz、D.H.(1999)。 ローカル意思決定の分析

### 熟語・専門語

- **decision**: 意思決定。予測分布を損失・効用・行動選択へ接続する工程。

### 要約

- 李、M. D.、Criss、A. H.、Devezer、B.、Donkin、C.、Etz、A.、Leite、F. P.、Matzke、D.、Ruader、J.、 Trueblood、J. S.、White、C.N.、Vanddeker…

## Chunk 0758

### English（抽出4行）

> hierarchical modeling, applied to home radon measurement and remediation (with discussion).
> Statistical Science 14, 305–337.
> Lindley, D. V. (1956). On a measure of the information provided by an experiment. Annals of
> Mathematical Statistics 27, 986–1005.

### 日本語訳（自動翻訳）

> 階層モデリング、ホームラドン測定および修復(ディスカッション付き)に適用されます。
> 統計科学 14, 305–337.
> リンドリー、D.V.(1956)。 実験で提供した情報の計測について アナルス
> 数学統計 27, 986–1005.

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- 階層モデリング、ホームラドン測定および修復(ディスカッション付き)に適用されます。

## Chunk 0759

### English（抽出4行）

> Lins, L., Koop, D., Anderson, E. W., Callahan, S. P., Santos, E., Scheidegger, C. E., Freire, J.,
> and Silva, C. T. (2008). Examining statistics of workﬂow evolution provenance: A ﬁrst study.
> In Scientiﬁc and Statistical Database Management, SSDBM 2008, ed. B. Ludäscher and N.
> Mamoulis, 573–579. Berlin: Springer.

### 日本語訳（自動翻訳）

> リンス, L., クープ, D., アンダーソン, E. W., カラハン, S. P., サントス, E., Scheidegger, C. E., フレア, J.,
> シルバ, C. T. (2008). ワークフローの進化実証の統計:最初の研究。
> 科学と統計データベース管理、SSDBM 2008、ed。 B. LudäscherとN.
> マモーリス、573〜579。 ベルリン:スプリングー。

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- リンス, L., クープ, D., アンダーソン, E. W., カラハン, S. P., サントス, E., Scheidegger, C. E., フレア, J., シルバ, C. T. (2008). ワークフローの進化実証の統…

## Chunk 0760

### English（抽出4行）

> Linzer, D. A. (2013). Dynamic Bayesian forecasting of presidential elections in the states. Journal
> of the American Statistical Association 108, 124–134.
> Liu, Y., Harding, A., Gilbert, R., and Journel, A. G. (2005).
> A workﬂow for multiple-point

### 日本語訳（自動翻訳）

> リンザー、D. A.(2013)。 国家における大統領選挙の動的ベイジアン予測。 セミナー
> アメリカ統計協会 108, 124–134.
> 劉、Y.、Harding、A.、Gilbert、R.、Journel、A. G.(2005)。
> 複数のポイントのワークフロー

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- リンザー、D. A.(2013)。

## Chunk 0761

### English（抽出4行）

> geostatistical simulation. In Geostatistics Banﬀ2004, ed. O. Leuangthong and C. V. Deutsch.
> Dordrecht: Springer.
> Loftus, J. (2015). Selective inference after cross-validation. arxiv.org/pdf/1511.08866.pdf
> Long, J. S. (2009). The Workﬂow of Data Analysis Using Stata. London: CRC Press.

### 日本語訳（自動翻訳）

> 地理的シミュレーション。 Geostatistics Banff2004、ed。 O. LeuangthongとC. V.ドイツ。
> Dordrecht: スプリング
> ロフトス、J.(2015)。 クロスバリデーション後の選択的推論。 arxiv.org/pdf/1511.08866.pdf
> ロング、J.S.(2009)。 スタッタを用いたデータ解析のワークフロー ロンドン:CRCプレス。

### 熟語・専門語

- **ESS**: 有効サンプルサイズ。自己相関を考慮した独立サンプル相当数。
- **validation**: 検証。モデルが目的・データ・外部知識に照らして妥当かを確認すること。

### 要約

- 地理的シミュレーション。

## Chunk 0762

### English（抽出4行）

> Mallows, C. L. (1973). Some comments on Cp. Technometrics 15, 661–675.
> Margossian, C. C, and Gelman, A (2020).
> Bayesian Model of Planetary Motion: exploring
> ideas for a modeling workﬂow when dealing with ordinary diﬀerential equations and mul-

### 日本語訳（自動翻訳）

> マロ, C. L. (1973). Cp. Technometrics 15, 661–675 に関するコメントがあります。
> マルゴシアン、C.C.、ゲルマン、A(2020)。
> 惑星の動きのベイジアンモデル:探索
> 通常の差動式とmul-を扱うときにモデリングワークフローのためのアイデア

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- マロ, C. L. (1973). Cp. Technometrics 15, 661–675 に関するコメントがあります。

## Chunk 0763

### English（抽出4行）

> timodality.
> Technical Report, https://github.com/stan-dev/example-models/tree/case-study/
> planet/knitr/planetary_motion
> Margossian, C. C., Vehtari, A., Simpson, D., and Agrawal, R. (2020a). Hamiltonian Monte Carlo

### 日本語訳（自動翻訳）

> ティモダリティ。
> テクニカルレポート、https://github.com/stan-dev/example-models/tree/case-study/
> 惑星/ニット/惑星 感情
> マルゴシアン、C. C.、Vehtari、A.、Simpson、D.、Agrawal、R.(2020a)。 ハミルトニア モンテ カルロ

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- ティモダリティ。

## Chunk 0764

### English（抽出4行）

> using an adjoint-diﬀerentiated Laplace approximation: Bayesian inference for latent Gaussian
> models and beyond. Advances in Neural Information Processing Systems 34, page to appear,
> arXiv:2004.12550
> Margossian, C. C., Vehtari, A., Simpson, D., and Agrawal, R. (2020b). Approximate Bayesian

### 日本語訳（自動翻訳）

> アドジョイント・ディフュージョン・ラプレース・オフィメーションの使用:ベイジアン・インフェレンス・フォー・ラテント・ガウス
> モデルとそれを超えて。 神経情報処理システム34、表示するページ、
> arXiv:2004.12550の
> Margosian、C. C.、Vehtari、A.、Simpson、D.、Agrawal、R.(2020b)。 ベイエリア

### 熟語・専門語

- **Bayesian inference**: ベイズ推論。事前分布と尤度から事後分布を計算する中核処理。
- **ESS**: 有効サンプルサイズ。自己相関を考慮した独立サンプル相当数。
- **approximate**: 近似。速度や扱いやすさのため、正確な推論・モデルを緩めること。

### 要約

- アドジョイント・ディフュージョン・ラプレース・オフィメーションの使用:ベイジアン・インフェレンス・フォー・ラテント・ガウス モデルとそれを超えて。

## Chunk 0765

### English（抽出4行）

> inference for latent Gaussian models in Stan. Stan Con 2020, researchgate.net/publication/
> 343690329_Approximate_Bayesian_inference_for_latent_Gaussian_models_in_Stan
> Mayo, D. (2018). Statistical Inference as Severe Testing: How to Get Beyond the Statistics Wars.
> Cambridge University Press.

### 日本語訳（自動翻訳）

> StanのGaussianモデルの遅延の影響。 スタンコン2020、searchgate.net/publication/
> 343690329 Approximate Bayesian inference for latent Gaussian models in Stanの 
> Mayo、D.(2018)。 重度のテストとしての統計的推論: 統計戦争を超えて取得する方法.
> ケンブリッジ大学プレス。

### 熟語・専門語

- **ESS**: 有効サンプルサイズ。自己相関を考慮した独立サンプル相当数。
- **approximate**: 近似。速度や扱いやすさのため、正確な推論・モデルを緩めること。

### 要約

- StanのGaussianモデルの遅延の影響。

## Chunk 0766

### English（抽出4行）

> McConnell, S. (2004). Code Complete, second edition. Microsoft Press.
> Meng, X. L., and van Dyk, D. A. (2001). The art of data augmentation. Journal of Computational
> and Graphical Statistics 10, 1–50.
> Merkle, E. C., Furr, D., and Rabe-Hesketh, S. (2019). Bayesian comparison of latent variable

### 日本語訳（自動翻訳）

> マッコネル, S. (2004). コード 完了, 第二版. マイクロソフトプレス。
> メング、X. L.、およびヴァン・ディク、D. A.(2001)。 データの拡張の芸術。 計算ジャーナル
> 統計データ 10, 1–50.
> メルクル、E.C.、ファール、D.、ラベ・ヘルツ、S.(2019)。 潜在変数のベイジアン比較

### 熟語・専門語

- **ESS**: 有効サンプルサイズ。自己相関を考慮した独立サンプル相当数。

### 要約

- マッコネル, S. (2004). コード 完了, 第二版. マイクロソフトプレス。

## Chunk 0767

### English（抽出4行）

> models: Conditional versus marginal likelihoods. Psychometrika 84, 802–829.
> Millar, R. B. (2018). Conditional vs marginal estimation of the predictive loss of hierarchical
> models using WAIC and cross-validation. Statistics and Computing 28, 375–385.
> Modrák, M. (2018). Reparameterizing the sigmoid model of gene regulation for Bayesian inference.

### 日本語訳（自動翻訳）

> モデル: 条件付き対余白の尤度。 エスチョメトリカ 84, 802–829.
> ミラー、R.B.(2018)。 階層の予測損失の条件的対比推定
> WAICとクロスバリデーションを使ったモデル。 統計と計算 28,375–385.
> Modrák, M. (2018). ベイジアン推論のための遺伝子規則のシグマイドモデルを再現。

### 熟語・専門語

- **Bayesian inference**: ベイズ推論。事前分布と尤度から事後分布を計算する中核処理。
- **likelihood**: 尤度。パラメータが与えられたときデータがどれだけ起こりやすいか。
- **validation**: 検証。モデルが目的・データ・外部知識に照らして妥当かを確認すること。

### 要約

- モデル: 条件付き対余白の尤度。

## Chunk 0768

### English（抽出4行）

> Computational Methods in Systems Biology. CMSB 2018. Lecture Notes in Computer Science,
> vol. 11095, 309–312.
> Montgomery, J. M., and Nyhan, B. (2010). Bayesian model averaging: Theoretical developments
> and practical applications. Political Analysis 18, 245–270.

### 日本語訳（自動翻訳）

> システム生物学における計算方法。 CMSB 2018 出展のお知らせ コンピュータサイエンスの講義ノート、
> 電圧 11095、309-312
> モンゴメリー、J.M.、Nyhan、B.(2010)。 ベイジアンモデル平均化:理論的開発
> そして実用的な適用。 政治分析 18, 245–270.

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- システム生物学における計算方法。

## Chunk 0769

### English（抽出4行）

> Morgan, S. L., and Winship, C. (2014). Counterfactuals and Causal Inference: Methods and
> Principles for Social Research, second edition. Cambridge University Press.
> Morris, G. E., Gelman, A., and Heidemanns, M. (2020). How the Economist presidential forecast
> works. projects.economist.com/us-2020-forecast/president/how-this-works

### 日本語訳（自動翻訳）

> モーガン、S. L.、Winship、C.(2014)。 偽物と因果推論:方法と
> 第2回社会研究原則 ケンブリッジ大学プレス。
> モリス、G.E.、ゲルマン、A.、ハイドマン、M.(2020)。 エコノミスト大統領の予測方法
> 作品紹介 project.economist.com/us-2020-forecast/president/how-this-Works は、

### 熟語・専門語

- **ESS**: 有効サンプルサイズ。自己相関を考慮した独立サンプル相当数。

### 要約

- モーガン、S. L.、Winship、C.(2014)。

## Chunk 0770

### English（抽出4行）

> Navarro, D. J. (2019). Between the devil and the deep blue sea: Tensions between scientiﬁc
> judgement and statistical model selection. Computational Brain and Behavior 2, 28–34.
> Navarro, D. J. (2020). If mathematical psychology did not exist we might need to invent it: A
> comment on theory building in psychology. Perspectives on Psychological Science. psyarxiv.

### 日本語訳（自動翻訳）

> ナワロ、D. J. (2019)。 悪魔と深い青の海の間:科学の緊張
> 判定・統計モデル選定 計算脳と行動2、28–34。
> ナワロ、D. J. (2020). 数学心理学が存在しなかった場合は、それを発明する必要があります: A
> 心理学の理論構築に関するコメント。 心理学的科学の視点。 サイアレクシブ。

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- ナワロ、D. J. (2019)。

## Chunk 0771

### English（抽出4行）

> com/ygbjp
> Neal, R. M. (1993). Probabilistic inference using Markov chain Monte Carlo methods. Technical
> Report CRG-TR-93-1, Department of Computer Science, University of Toronto.
> Neal, R. M. (2011). MCMC using Hamiltonian dynamics. In Handbook of Markov Chain Monte

### 日本語訳（自動翻訳）

> com/ygbjp からのツイート
> ニール、R.M.(1993)。 Markovチェーンモンテカルロメソッドを使用した確率的推論。 テクニカル
> トロント大学コンピュータサイエンス学部CRG-TR-93-1報告
> ニール、R.M.(2011)。 ハミルトニアンダイナミクスを使用したMCMC。 Markovチェーンモンテのハンドブック

### 熟語・専門語

- **Markov chain**: マルコフ連鎖。MCMCで事後分布からサンプルを得るための確率過程。

### 要約

- com/ygbjp からのツイート ニール、R.M.(1993)。

## Chunk 0772

### English（抽出4行）

> Carlo, ed. S. Brooks, A. Gelman, G. L. Jones, and X. L. Meng, 113–162. London: CRC Press.
> Niederlová, V., Modrák, M., Tsyklauri, O., Huranová, M., and Štěpánek, O. (2019). Meta-analysis
> of genotype-phenotype associations in Bardet-Biedl Syndrome uncovers diﬀerences among
> causative genes. Human Mutation 40, 2068–2087.

### 日本語訳（自動翻訳）

> Carlo, ed. S. Brooks, A. Gelman, G. L. Jones, X. L. Meng, 113–162. ロンドン: CRC Press.
> Niederlová、V.、Modrák、M.、Tsyklauri、O.、Huranová、M.、Sitěpánek、O.(2019)。 メタ解析
> Bardet-Biedl Syndrome における genotype-phenotype の関連付けは、
> 原因遺伝子。 ヒューマンミュテーション40、2068〜2087。

### 熟語・専門語

- **ESS**: 有効サンプルサイズ。自己相関を考慮した独立サンプル相当数。

### 要約

- Carlo, ed. S. Brooks, A. Gelman, G. L. Jones, X. L. Meng, 113–162. ロンドン: CRC Press. Niederlová、V.、Modrák、M.、Tsyklauri…

## Chunk 0773

### English（抽出4行）

> Nott, D. J., Wang, X., Evans, M., and Englert, B. G. (2020). Checking for prior-data conﬂict using
> prior-to-posterior divergences. Statistical Science 35, 234–253.
> Novick, M. R., Jackson, P. H., Thayer, D. T., and Cole, N. S. (1972).
> Estimating multiple

### 日本語訳（自動翻訳）

> ノット、D. J.、王、X.、エヴァンス、M.、およびエングルルト、B.G.(2020)。 事前データの競合確認
> 前の投稿者ダイバーゲンス。 統計科学 35,234–253.
> ノミック、M.R.、ジャクソン、P.H.、タイヤー、D.T.、コール、N.S.(1972)。
> 複数の見積り

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- ノット、D. J.、王、X.、エヴァンス、M.、およびエングルルト、B.G.(2020)。

## Chunk 0774

### English（抽出4行）

> regressions in m-groups: a cross validation study.
> British Journal of Mathematical and
> Statistical Psychology 25, 33–50.
> O’Hagan, A., Buck, C. E., Daneshkhah, A., Eiser, J. R., Garthwaite, P. H., Jenkinson, D. J., Oakely,

### 日本語訳（自動翻訳）

> m-groupsの回帰:クロスバリデーション調査。
> 数学と英国のジャーナル
> 統計心理学 25, 33–50.
> O'Hagan、A.、Buck、C. E.、Daneshkhah、A.、Eiser、J. R.、Garthwaite、P.H.、Jenkinson、D. J.、Okely、

### 熟語・専門語

- **cross validation**: 交差検証。汎化性能を推定するためにデータを分割/近似除外する評価法。
- **ESS**: 有効サンプルサイズ。自己相関を考慮した独立サンプル相当数。
- **validation**: 検証。モデルが目的・データ・外部知識に照らして妥当かを確認すること。

### 要約

- m-groupsの回帰:クロスバリデーション調査。

## Chunk 0775

### English（抽出4行）

> J. E., and Rakow, T. (2006). Uncertain Judgements: Eliciting Experts’ Probabilities. Wiley.
> Paananen, T., Piironen, J., Bürkner, P.-C., and Vehtari, A. (2020). Implicitly adaptive importance
> sampling. Statistics and Computing, in press.
> Pearl, J., and Bareinboim, E. (2011). Transportability of causal and statistical relations: A formal

### 日本語訳（自動翻訳）

> J. E.、およびRakow、T.(2006)。 判断の不確実性:エキスパートの能力を排除する。 ウィリー。
> Paananen、T.、Piironen、J.、Bürkner、P.-C.、Vehtari、A.(2020)。 適応的な重要性
> サンプリング。 統計とコンピューティング, プレスで.
> 真珠、J、Bareinboim、E.(2011)。 原因・統計関係の運送性:正式

### 熟語・専門語

- **ESS**: 有効サンプルサイズ。自己相関を考慮した独立サンプル相当数。

### 要約

- J. E.、およびRakow、T.(2006)。

## Chunk 0776

### English（抽出4行）

> approach. In Data Mining Workshops (ICDMW), 2011 IEEE 11th International Conference,
> 540–547.
> Pearl, J., and Bareinboim, E. (2014). External validity: From do-calculus to transportability across
> populations. Statistical Science 29, 579–595.

### 日本語訳（自動翻訳）

> アプローチ。 データマイニングワークショップ(ICDMW)、2011 IEEE 第11回国際会議、
> 540–547.(税抜き)
> 真珠, J., ベアインボイム, E. (2014). 外部の妥当性: 計算から輸送性まで
> 人口. 統計科学 29, 579–595.

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- アプローチ。

## Chunk 0777

### English（抽出4行）

> Piironen, J., and Vehtari, A. (2017). Sparsity information and regularization in the horseshoe and
> other shrinkage priors. Electronic Journal of Statistics 11, 5018–5051.
> Pirš, G., and Štrumbelj, E. (2009). Bayesian combination of probabilistic classiﬁers using multi-
> variate normal mixtures. Journal of Machine Learning Research 20, 1–18.

### 日本語訳（自動翻訳）

> ピロレン、J、Vehtari、A.(2017)。 馬蹄と馬蹄のスパリティー情報と正規化
> 他の収縮の優先順位。 統計電子ジャーナル 11, 5018–5051.
> Pirš、G、Sitrumbelj、E.(2009)。 多品種を用いた確率的分類器のベイジアンの組み合わせ
> 通常の混合物を分散させます。 機械学習研究ジャーナル 20, 1–18.

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- ピロレン、J、Vehtari、A.(2017)。

## Chunk 0778

### English（抽出4行）

> Price, P. N., Nero, A. V., and Gelman, A. (1996). Bayesian prediction of mean indoor radon
> concentrations for Minnesota counties. Health Physics 71, 922–936.
> Rasmussen, C. E., and Williams, C. K. I. (2006). Gaussian Processes for Machine Learning. MIT
> Press.

### 日本語訳（自動翻訳）

> 価格, P. N., Nero, A. V., ゲルマン, A. (1996). ベイジアンは平均屋内ラドンの予測
> ミネソタ州の郡のための集中。 健康物理学 71, 922–936.
> ラスムセン、C.E.、ウィリアムズ、C.K.I.(2006)。 機械学習のためのガウスのプロセス。 ログイン
> プレス。

### 熟語・専門語

- **ESS**: 有効サンプルサイズ。自己相関を考慮した独立サンプル相当数。
- **prediction**: 予測。未知/将来/除外データに対する分布や点推定。

### 要約

- 価格, P. N., Nero, A. V., ゲルマン, A. (1996). ベイジアンは平均屋内ラドンの予測 ミネソタ州の郡のための集中。

## Chunk 0779

### English（抽出4行）

> Raudenbush, S. W., and Bryk, A. S. (2002). Hierarchical Linear Models, second edition. Sage
> Publications.
> Richardson, S., and Gilks, W. R. (1993). A Bayesian approach to measurement error problems
> in epidemiology using conditional independence models. American Journal of Epidemiology

### 日本語訳（自動翻訳）

> Raudenbush、S.W.、Bryk、A.S.(2002)。 階層線形モデル、第2版。 セージ
> 出版物
> リチャードソン、S.、ギルクス、W.R.(1993)。 測定エラーの問題に対するベイジアンアプローチ
> 条件付き独立モデルを用いた疫学 米国疫学会

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- Raudenbush、S.W.、Bryk、A.S.(2002)。

## Chunk 0780

### English（抽出4行）

> 138, 430–442.
> Riebler, A., Sørbye, S. H., Simpson, D., and Rue, H. (2018). An intuitive Bayesian spatial model
> for disease mapping that accounts for scaling. Statistical Methods in Medical Research 25,
> 1145–1165.

### 日本語訳（自動翻訳）

> 138, 430–442.
> リベラー、A.、Sørbye、S.H.、Simpson、D.、Rue、H.(2018)。 直感的なベイジアン空間モデル
> 病気マッピングでは、スケーリングのアカウントをマッピングします。 医学研究25の統計的方法
> 1145–1165.(1145–1165)

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- 138, 430–442. リベラー、A.、Sørbye、S.H.、Simpson、D.、Rue、H.(2018)。

## Chunk 0781

### English（抽出4行）

> Robert, C., and Casella, G. (2011). A short history of Markov chain Monte Carlo: Subjective
> recollections from incomplete data. Statistical Science 26, 102–115.
> Rubin, D. B. (1984). Bayesianly justiﬁable and relevant frequency calculations for the applied
> statistician. Annals of Statistics 12, 1151–1172.

### 日本語訳（自動翻訳）

> ロバート、C.、カセラ、G.(2011)。 Markovチェーンモンテカルロの短い歴史:主観的
> 不完全なデータからのリコレクション。 統計科学 26, 102–115.
> ルビン, D. B. (1984). ベイジアンの正当性および適用のための関連の頻度計算
> 統計学. 統計のアンナルス 12, 1151–1172.

### 熟語・専門語

- **Markov chain**: マルコフ連鎖。MCMCで事後分布からサンプルを得るための確率過程。

### 要約

- ロバート、C.、カセラ、G.(2011)。

## Chunk 0782

### English（抽出4行）

> Rudin, C. (2018). Please stop explaining black box models for high stakes decisions. NeurIPS 2018
> Workshop on Critiquing and Correcting Trends in Machine Learning. arxiv.org/abs/1811.10154
> Rue, H., Martino, S., and Chopin, N. (2009). Approximate Bayesian inference for latent Gaussian
> models by using integrated nested Laplace approximations. Journal of the Royal Statistical

### 日本語訳（自動翻訳）

> 2018年12月14日 高精細の決定を下すために、ブラックボックスのモデルの説明を中止してください。 ヌルIPS 2018
> マシン学習の危機と修正の傾向に関するワークショップ. arxiv.org/abs/1811.10154 - ダウンロード
> Rue, H., Martino, S., ショパン, N. (2009). レイト・ガウジアンの約ベイジアン・インフェレンス
> 統合されたネストされたランスの近似を使用してモデル。 ロイヤル・統計ジャーナル

### 熟語・専門語

- **Bayesian inference**: ベイズ推論。事前分布と尤度から事後分布を計算する中核処理。
- **approximate**: 近似。速度や扱いやすさのため、正確な推論・モデルを緩めること。
- **decision**: 意思決定。予測分布を損失・効用・行動選択へ接続する工程。

### 要約

- 2018年12月14日 高精細の決定を下すために、ブラックボックスのモデルの説明を中止してください。

## Chunk 0783

### English（抽出4行）

> Society B 71, 319–392.
> Sarma, A., and Kay, M. (2020). Prior setting in practice: Strategies and rationales used in choosing
> prior distributions for Bayesian analysis. Proceedings of the 2020 CHI Conference on Human
> Factors in Computing Systems.

### 日本語訳（自動翻訳）

> 社会 B 71, 319–392.
> サルマ、A.、ケイ、M.(2020)。 練習の事前設定:選択に使用される戦略と合理的
> ベイジアン分析のための事前の配布。 ヒトにおける2020年CH会議の発表
> コンピューティングシステムにおける要因。

### 熟語・専門語

- **prior distribution**: 事前分布。データ観測前の知識・制約を表す分布。

### 要約

- 社会 B 71, 319–392. サルマ、A.、ケイ、M.(2020)。

## Chunk 0784

### English（抽出4行）

> Savage, J. (2016). What is modern statistical workﬂow? khakieconomics.github.io/2016/08/29/
> What-is-a-modern-statistical-workﬂow.html
> Shi, X., and Stevens, R. (2008). SWARM: a scientiﬁc workﬂow for supporting bayesian approaches
> to improve metabolic models. CLADE ’08: Proceedings of the 6th International Workshop on

### 日本語訳（自動翻訳）

> Savage、J.(2016)。 現代の統計ワークフローとは? カルキ経済学.github.io/2016/08/29/
> What-is-a-modern-statistical-workflow.html は、
> シ、X.、スティーブンス、R.(2008)。 SWARM:ベイジアンのアプローチをサポートする科学的なワークフロー
> 代謝モデルを改善するために。 CLADE ’08:第6回国際ワークショップの発表

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- Savage、J.(2016)。

## Chunk 0785

### English（抽出4行）

> Challenges of Large Applications in Distributed Environments, 25–34.
> Shirani-Mehr, H., Rothschild, D., Goel, S., and Gelman, A. (2018). Disentangling bias and variance
> in election polls. Journal of the American Statistical Association 118, 607–614.
> Simmons, J., Nelson, L., and Simonsohn, U. (2011). False-positive psychology: Undisclosed

### 日本語訳（自動翻訳）

> 分散型環境における大型用途の課題25～34
> シラニ・メア、H.、ロスシルド、D.、ゴエル、S.、ゲルマン、A.(2018)。 偏見と分散
> 選挙投票で. 米国統計協会のジャーナル 118, 607–614.
> シモンズ、J.、ネルソン、L.、シモンズ、U.(2011)。 偽陽性心理学:Undisclosed

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- 分散型環境における大型用途の課題25～34 シラニ・メア、H.、ロスシルド、D.、ゴエル、S.、ゲルマン、A.(2018)。

## Chunk 0786

### English（抽出4行）

> ﬂexibility in data collection and analysis allow presenting anything as signiﬁcant. Psychological
> Science 22, 1359–1366.
> Simpson, D., Rue, H., Riebler, A., Martins, T. G., and Sørbye, S. H. (2017). Penalising model
> component complexity: A principled, practical approach to constructing priors. Statistical

### 日本語訳（自動翻訳）

> データ収集および分析の柔軟性により、重要なことを示すことができます。 心理学的
> 科学 22, 1359–1366.
> Simpson, D., Rue, H., Riebler, A., Martins, T. G., Sørbye, S. H. (2017). 貫通モデル
> コンポーネントの複雑性: 原則的に、事前に構築する実用的なアプローチ。 統計学

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- データ収集および分析の柔軟性により、重要なことを示すことができます。

## Chunk 0787

### English（抽出4行）

> Science 32, 1–28.
> Singer, E., Van Hoewyk, J., Gebler, N., Raghunathan, T., and McGonagle, K. (1999). The eﬀects
> of incentives on response rates in interviewer-mediated surveys. Journal of Oﬃcial Statistics
> 15, 217–230.

### 日本語訳（自動翻訳）

> 科学 32, 1–28.
> Singer、E.、Van Hoewyk、J.、Gebler、N.、Rangunathan、T.、McGonagle、K.(1999)。 効果
> インタビュー担当者による調査における応答率に関するインセンティブ。 公式統計ジャーナル
> 15, 217–230.

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- 科学 32, 1–28. Singer、E.、Van Hoewyk、J.、Gebler、N.、Rangunathan、T.、McGonagle、K.(1999)。

## Chunk 0788

### English（抽出4行）

> Sivula, T., Magnusson, M, and Vehtari, A. (2020). Uncertainty in Bayesian leave-one-out cross-
> validation based model comparison. arxiv.org./abs/2008.10296
> Skrondal, A. and Rabe-Hesketh, S. (2004). Generalized Latent Variable Modeling: Multilevel,
> Longitudinal and Structural Equation Models. London: CRC Press.

### 日本語訳（自動翻訳）

> Sivula、T.、Magnusson、M、Vehtari、A.(2020)。 ベイジアンの残忍な十字の不確実性
> バリデーションベースのモデル比較。 arxiv.org./abs/2008.10296
> Skrondal、A.、Rabe-Hesketh、S.(2004)。 汎用ラテント変数モデリング:マルチレベル、
> 縦方向および構造式モデル。 ロンドン:CRCプレス。

### 熟語・専門語

- **model comparison**: モデル比較。LOO-CVなどで複数モデルの予測性能や弱点を比較すること。
- **leave-one-out**: LOO。一点ずつ除外した予測評価を効率的に近似する交差検証。
- **ESS**: 有効サンプルサイズ。自己相関を考慮した独立サンプル相当数。
- **uncertainty**: 不確実性。観測・パラメータ・モデル構造・意思決定に残る曖昧さ。
- **validation**: 検証。モデルが目的・データ・外部知識に照らして妥当かを確認すること。

### 要約

- Sivula、T.、Magnusson、M、Vehtari、A.(2020)。

## Chunk 0789

### English（抽出4行）

> Smith, A. (2013). Sequential Monte Carlo Methods in Practice. New York: Springer.
> Stan Development Team (2020). Stan User’s Guide. mc-stan.org
> Steegen, S., Tuerlinckx, F., Gelman, A., and Vanpaemel, W. (2016).
> Increasing transparency

### 日本語訳（自動翻訳）

> スミス, A. (2013). 練習中の連続モンテカルロ法。 ニューヨーク: スプリングス
> スタン開発チーム(2020) スタンユーザーガイド mc-stan.orgの
> Steegen、S.、Tuerlinckx、F.、Gelman、A.、Vanpaemel、W.(2016)。
> 透明性を高める

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- スミス, A. (2013). 練習中の連続モンテカルロ法。

## Chunk 0790

### English（抽出4行）

> through a multiverse analysis. Perspectives on Psychological Science 11, 702–712.
> Stone, M. (1974). Cross-validatory choice and assessment of statistical predictions (with discus-
> sion). Journal of the Royal Statistical Society B 36, 111–147.
> Stone, M. (1977). An asymptotic equivalence of choice of model cross-validation and Akaike’s

### 日本語訳（自動翻訳）

> 多重解析による 心理科学11、702–712の視点。
> ストーン, M. (1974). 横断的選択と統計予測の評価(ディスクス付き)
> セクション ロイヤル統計学会誌 B 36, 111–147.
> ストーン, M. (1977). モデルの交差validationとAkaike'sの選択肢の同化程式

### 熟語・専門語

- **ESS**: 有効サンプルサイズ。自己相関を考慮した独立サンプル相当数。
- **validation**: 検証。モデルが目的・データ・外部知識に照らして妥当かを確認すること。
- **prediction**: 予測。未知/将来/除外データに対する分布や点推定。

### 要約

- 多重解析による 心理科学11、702–712の視点。

## Chunk 0791

### English（抽出4行）

> criterion. Journal of the Royal Statistical Society B 36, 44–47.
> Talts, S., Betancourt, M., Simpson, D., Vehtari, A., and Gelman, A. (2020). Validating Bayesian
> inference algorithms with simulation-based calibration.
> www.stat.columbia.edu/~gelman/

### 日本語訳（自動翻訳）

> 基準。 王立統計学会誌 B 36, 44–47.
> Talts、S.、Bebancourt、M.、Simpson、D.、Vehtari、A.、およびGelman、A.(2020)。 検証ベイジアン
> シミュレーションベースの口径測定を用いる推論アルゴリズム。
> www.stat.columbia.edu/~ゲルマン/

### 熟語・専門語

- **simulation-based calibration**: SBC。シミュレーション真値と事後rankを比べ、実装・推論の校正を検査する方法。

### 要約

- 基準。

## Chunk 0792

### English（抽出4行）

> research/unpublished/sbc.pdf
> Taylor, J., and Tibshirani, R. J. (2015). Statistical learning and selective inference. Proceedings of
> the National Academy of Sciences 112, 7629–7634.
> Taylor, S. J., and Lethem, B. (2018). Forecasting at scale. American Statistician 72, 37–45.

### 日本語訳（自動翻訳）

> 研究/公開/sbc.pdf
> テイラー、J.、チブシラニ、R. J.(2015)。 統計的学習と選択的推論。 職業紹介
> 国立科学アカデミー 112, 7629–7634.
> テイラー、S. J.、レヘム、B.(2018)。 スケールでの予測。 アメリカン統計学 72, 37–45.

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- 研究/公開/sbc.pdf テイラー、J.、チブシラニ、R. J.(2015)。

## Chunk 0793

### English（抽出4行）

> Tierney, L., and Kardane, J.B. (1986). Accurate approximations for posterior moments and marginal
> densities. Journal of the American Statistical Association, 81(393):82–86.
> Turner, K. J., and Lambert, P. S. (2015). Workﬂows for quantitative data analysis in the social
> sciences. International Journal on Software Tools for Technology Transfer 17, 321–338.

### 日本語訳（自動翻訳）

> Tierney、L、Kardane、J.B.(1986)。 ポスターの瞬間とマージンの正確な近似
> 密度。 米国統計協会のジャーナル, 81(393):82–86.
> ターナー、J.、ランバート、P.S.(2015)。 社会的における量的データ解析のためのワークフロー
> 科学研究 技術転送のためのソフトウェアツールに関する国際ジャーナル 17,321–338.

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- Tierney、L、Kardane、J.B.(1986)。

## Chunk 0794

### English（抽出4行）

> Unwin, A., Volinsky, C., and Winkler, S. (2003). Parallel coordinates for exploratory modelling
> analysis. Computational Statistics and Data Analysis 43, 553–564.
> Vehtari, A. (2019). Cross-validation for hierarchical models. avehtari.github.io/modelselection/
> rats_kcv.html

### 日本語訳（自動翻訳）

> Unwin、A.、Volinsky、C.、Winkler、S.(2003)。 Parallel は、実験的なモデリングのための調整
> 分析。 計算統計とデータ分析 43, 553–564.
> ヴェッタリ、A.(2019)。 階層モデルのクロスバリデーション avehtari.github.io/モデル選択/
> ラッツ kcv.html

### 熟語・専門語

- **validation**: 検証。モデルが目的・データ・外部知識に照らして妥当かを確認すること。

### 要約

- Unwin、A.、Volinsky、C.、Winkler、S.(2003)。

## Chunk 0795

### English（抽出4行）

> Vehtari A., Gabry J., Magnusson M., Yao Y., Bürkner P., Paananen T., Gelman A. (2020). loo:
> Eﬃcient leave-one-out cross-validation and WAIC for Bayesian models. R package version
> 2.3.1, mc-stan.org/loo.
> Vehtari, A., and Gabry, J. (2020). Bayesian stacking and pseudo-BMA weights using the loo

### 日本語訳（自動翻訳）

> Vehtari A., Gabry J., Magnusson M., Yao Y., Bürkner P., Paanen T., ゲルマンA. (2020). ロオ:
> ベイジアンモデルの効率的な離脱式とWAIC。 Rパッケージバージョン
> 2.3.1、mc-stan.org/loo。
> Vehtari、A.、Gabry、J.(2020)。 looを使用してベイジアンの積み重ねおよび擬似BMAの重量

### 熟語・専門語

- **leave-one-out**: LOO。一点ずつ除外した予測評価を効率的に近似する交差検証。
- **validation**: 検証。モデルが目的・データ・外部知識に照らして妥当かを確認すること。

### 要約

- Vehtari A., Gabry J., Magnusson M., Yao Y., Bürkner P., Paanen T., ゲルマンA. (2020). ロオ: ベイジアンモデルの効率的な離脱式とWAIC。

## Chunk 0796

### English（抽出4行）

> package. mc-stan.org/loo/articles/loo2-weights.html
> Vehtari, A., Gelman, A., and Gabry, J. (2017). Practical Bayesian model evaluation using leave-
> one-out cross-validation and WAIC. Statistics and Computing 27, 1413–1432.
> Vehtari, A., Gelman, A., Simpson, D., Carpenter, D., and Bürkner, P.-C. (2020).

### 日本語訳（自動翻訳）

> パッケージ。 mc-stan.org/loo/articles/loo2-weights.html
> Vehtari、A.、Gelman、A.、Gabry、J.(2017)。 休暇を利用した実用ベイジアンモデル評価
> 1アウトの断線とWAIC。 統計と計算 27, 1413–1432.
> Vehtari、A.、Gelman、A.、Simpson、D.、Carpenter、D.、Bürkner、P.-C.(2020)。

### 熟語・専門語

- **validation**: 検証。モデルが目的・データ・外部知識に照らして妥当かを確認すること。

### 要約

- パッケージ。

## Chunk 0797

### English（抽出4行）

> Rank-
> normalization, folding, and localization: An improved R-hat for assessing convergence of
> MCMC. Bayesian Analysis.
> Vehtari, A., Gelman, A., Sivula, T., Jylanki, P., Tran, D., Sahai, S., Blomstedt, P., Cunningham,

### 日本語訳（自動翻訳）

> ランク -
> 正規化、折りたたみ、ローカリゼーション: 収束を評価するための改善されたR-hat
> MCMC。 ベイジアン分析。
> Vehtari、A.、Gelman、A.、Sivula、T.、Jylanki、P.、Tran、D.、Sahai、S.、Blomstedt、P.、Cunningham、

### 熟語・専門語

- **R-hat**: R-hat。複数chainの収束を測る診断量。1から離れるほど問題。
- **ESS**: 有効サンプルサイズ。自己相関を考慮した独立サンプル相当数。

### 要約

- ランク - 正規化、折りたたみ、ローカリゼーション: 収束を評価するための改善されたR-hat MCMC。

## Chunk 0798

### English（抽出4行）

> J. P., Schiminovich, D., and Robert, C. P. (2020). Expectation propagation as a way of life: A
> framework for Bayesian inference on partitioned data. Journal of Machine Learning Research
> 21, 1–53.
> Vehtari, A., Simpson, D., Gelman, A., Yao, Y., and Gabry, J. (2015). Pareto smoothed importance

### 日本語訳（自動翻訳）

> J.P.、シミノヴィチ、D.、ロバート、C.P.(2020)。 人生の道としての期待伝搬: A
> 分割されたデータに対するベイジアン推論のためのフレームワーク。 機械学習研究ジャーナル
> 21,1–53
> Vehtari、A.、シンプソン、D.、ゲルマン、A.、ヤオ、Y.、およびGabry、J.(2015)。 Pareto スムーズな重要性

### 熟語・専門語

- **Bayesian inference**: ベイズ推論。事前分布と尤度から事後分布を計算する中核処理。
- **Pareto**: Pareto-k診断。PSIS-LOOの信頼性を示す診断量。大きいと再推定やモデル修正が必要。

### 要約

- J.P.、シミノヴィチ、D.、ロバート、C.P.(2020)。

## Chunk 0799

### English（抽出4行）

> sampling. arxiv.org/abs/1507.02646
> Wang, W., and Gelman, A. (2015). Diﬃculty of selecting among multilevel models using predictive
> accuracy. Statistics and Its Interface 8 (2), 153–160.
> Weber, S., Gelman, A., Lee, D., Betancourt, M., Vehtari, A., and Racine-Poon, A. (2018). Bayesian

### 日本語訳（自動翻訳）

> サンプリング。 arxiv.org/abs/1507.02646
> 王、W、ゲルマン、A.(2015)。 予測を使用してマルチレベルモデルの中から選択する困難
> 精度。 統計とそのインタフェース 8 (2), 153–160.
> Weber、S.、Gelman、A.、Lee、D.、Betancourt、M.、Vehtari、A.、およびRacine-Poon、A.(2018)。 ベイジアン

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- サンプリング。

## Chunk 0800

### English（抽出4行）

> aggregation of average data: An application in drug development. Annals of Applied Statistics
> 12, 1583–1604.
> Wickham, H. (2006).
> Exploratory model analysis with R and GGobi.

### 日本語訳（自動翻訳）

> 平均データの集計:医薬品開発の応用。 応用統計のアンナルス
> 12、1583–1604。
> ウィッカム, H. (2006).
> RとGGobiによる実験モデル解析

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- 平均データの集計:医薬品開発の応用。

## Chunk 0801

### English（抽出4行）

> had.co.nz/model-vis/
> 2007-jsm.pdf
> Wickham, H., Cook, D., and Hofmann, H. (2015). Visualizing statistical models: Removing the
> blindfold. Statistical Analysis and Data Mining: The ASA Data Science Journal 8, 203–225.

### 日本語訳（自動翻訳）

> was.co.nz/model-vis/ は、
> 2007-jsm.pdf
> Wickham、H.、Cook、D.、Hofmann、H.(2015)。 統計モデルの可視化:削除
> 目隠し。 統計分析とデータマイニング:ASAデータサイエンスジャーナル 8, 203–225.

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- was.co.nz/model-vis/ は、 2007-jsm.pdf Wickham、H.、Cook、D.、Hofmann、H.(2015)。

## Chunk 0802

### English（抽出4行）

> Wickham, H., and Groelmund, G. (2017). R for Data Science. Sebastopol, Calif.: O’Reilly.
> Wilson, G., Aruliah, D. A., Brown, C. T., Hong, N. P. C., Davis, M., Guy, R. T., Haddock, S. H. D.,
> Huﬀ, K. D., Mitchell, I. M., Plumbley, M. D., Waugh, B., White, E. P., and Wilson, P. (2014).
> Best practices for scientiﬁc computing. PLoS Biology 12, e1001745.

### 日本語訳（自動翻訳）

> ウィッカム、H.、およびグルムンド、G.(2017)。 データサイエンスの研究開発 Sebastopol, カリフ.: 明らかに.
> ウィルソン, G., Aruliah, D. A., ブラウン, C. T., 香港, N. P. C., Davis, M., ガイ, R. T., Haddock, S. H. D.,
> Huff, K. D., Mitchell, I. M., Plumbley, M. D., Waugh, B., White, E. P., ウィルソン, P. (2014).
> 科学的な計算のためのベストプラクティス。 PLoSの生物学12、e1001745。

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- ウィッカム、H.、およびグルムンド、G.(2017)。

## Chunk 0803

### English（抽出4行）

> Wilson, G., Bryan, J., Cranston, K., Kitzes, J. Nederbragt, L., and Teal, T. K. (2017). Good enough
> practices in scientiﬁc computing. PLoS Computational Biololgy 13, e1005510.
> Yao, Y., Cademartori, C., Vehtari, A., and Gelman, A. (2020). Adaptive path sampling in metastable
> posterior distributions. arxiv.org/abs/2009.00471

### 日本語訳（自動翻訳）

> ウィルソン、G.、ブライアン、J.、クランストン、K.、キッツェス、J. Nederbragt、L.、T.K.(2017)。 十分によい
> 科学的コンピューティングの実践。 PLoS計算バイオロギー13、e1005510。
> Yao、Y.、Cademartori、C.、Vehtari、A.、ゲルマン、A.(2020)。 メタテーブルの適応パスサンプリング
> ポスター分布。 arxiv.org/abs/2009.00471の特長

### 熟語・専門語

- **posterior distribution**: 事後分布。データ観測後の未知量の不確実性を表す分布。

### 要約

- ウィルソン、G.、ブライアン、J.、クランストン、K.、キッツェス、J. Nederbragt、L.、T.K.(2017)。

## Chunk 0804

### English（抽出4行）

> Yao, Y., Vehtari, A., and Gelman, A. (2020). Stacking for non-mixing Bayesian computations: The
> curse and blessing of multimodal posteriors. arxiv.org/abs/2006.12335
> Yao, Y., Vehtari, A., Simpson, D., and Gelman, A. (2018a). Yes, but did it work?: Evaluating
> variational inference. In Proceedings of International Conference on Machine Learning, 5581–

### 日本語訳（自動翻訳）

> ヤオ、Y.、Vehtari、A.、ゲルマン、A.(2020)。 非混合ベイジアン計算のための積み重ね:
> 複数のポスターの呪いと祝福。 arxiv.org/abs/2006年12335
> ヤオ、Y.、Vehtari、A.、シンプソン、D.、ゲルマン、A.(2018a)。 はい、しかし、それは機能しましたか?: 評価評価
> 変動推論。 機械学習に関する国際会議の発表、5581～

### 熟語・専門語

- **ESS**: 有効サンプルサイズ。自己相関を考慮した独立サンプル相当数。

### 要約

- ヤオ、Y.、Vehtari、A.、ゲルマン、A.(2020)。

## Chunk 0805

### English（抽出4行）

> 5590.
> Yao, Y., Vehtari, A., Simpson, D., and Gelman, A. (2018b). Using stacking to average Bayesian
> predictive distributions (with discussion). Bayesian Analysis 13, 917–1003.
> Yu, B., and Kumbier, K. (2020). Veridical data science. Proceedings of the National Academy of

### 日本語訳（自動翻訳）

> 5590.5
> ヤオ、Y.、Vehtari、A.、シンプソン、D.、ゲルマン、A.(2018b)。 平均ベイジアンへのスタッキングの使用
> 予測分布(ディスカッション付き)。 ベイジアン分析 13, 917–1003.
> ユ、B、Kumbier、K.(2020)。 検証的なデータサイエンス。 国立国立国立アカデミーの職業

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- 5590.5 ヤオ、Y.、Vehtari、A.、シンプソン、D.、ゲルマン、A.(2018b)。

## Chunk 0806

### English（抽出4行）

> Sciences 117, 3920–3929.
> Zhang, Y. D., Naughton, B. P., Bondell, H. D., and Reich, B. J. (2020). Bayesian regression
> using a prior on the model ﬁt: The R2-D2 shrinkage prior. Journal of the American Statistical
> Association, doi:10.1080/01621459.2020.1825449

### 日本語訳（自動翻訳）

> 科学 117, 3920-3929.
> Zhang、Y. D.、Naughton、B. P.、ボンデル、H. D.、およびレイチ、B. J.(2020)。 ベイジアン回帰
> モデルの前の使用: R2-D2 収縮前の。 アメリカン統計ジャーナル
> 協会, 土井:10.1080/01621459.2020.1825449

### 熟語・専門語

- **ESS**: 有効サンプルサイズ。自己相関を考慮した独立サンプル相当数。

### 要約

- 科学 117, 3920-3929. Zhang、Y. D.、Naughton、B. P.、ボンデル、H. D.、およびレイチ、B. J.(2020)。
