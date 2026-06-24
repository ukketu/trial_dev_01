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

> 10 モデルの構築と拡張を含むワークフローの例: ゴルフのパッティング
> 10.1 最初のモデル: ロジスティック回帰。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。
> 10.2 第一原理に基づくモデル化
> 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。

### 熟語・専門語

- **ESS**: 有効サンプルサイズ。自己相関を考慮した独立サンプル相当数。
- **model building**: モデル構築。仮定・データ構造・prior・likelihoodを組み合わせる工程。

### 要約

- 10 モデルの構築と拡張を含むワークフローの例: ゴルフのパッティング 10.1 最初のモデル: ロジスティック回帰。

## Chunk 0038

### English（抽出4行）

> 10.3 Testing the ﬁtted model on new data . . . . . . . . . . . . . . . . . . . . . . . . .
> 10.4 A new model accounting for how hard the ball is hit . . . . . . . . . . . . . . . . .
> 10.5 Expanding the model by including a fudge factor
> . . . . . . . . . . . . . . . . . .

### 日本語訳（自動翻訳）

> 10.3 新しいデータでの適合モデルのテスト。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。
> 10.4 ボールの強さを考慮した新モデル。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。
> 10.5 ファッジ要素を含めてモデルを拡張する
> 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- 10.3 新しいデータでの適合モデルのテスト。

## Chunk 0039

### English（抽出4行）

> 10.6 General lessons from the golf example . . . . . . . . . . . . . . . . . . . . . . . .
> 11 Example of workﬂow for a model with unexpected multimodality: Planetary motion
> 11.1 Mechanistic model of motion . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
> 11.2 Fitting a simpliﬁed model . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

### 日本語訳（自動翻訳）

> 10.6 ゴルフの例から得られる一般的な教訓。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。
> 11 予期せぬ多峰性を持つモデルのワークフローの例: 惑星運動
> 11.1 運動の機構モデル。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。
> 11.2 単純化されたモデルのフィッティング。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。

### 熟語・専門語

- **multimodality**: 多峰性。事後分布に複数の山があり、MCMCが混合しにくい状態。
- **ESS**: 有効サンプルサイズ。自己相関を考慮した独立サンプル相当数。

### 要約

- 10.6 ゴルフの例から得られる一般的な教訓。

## Chunk 0040

### English（抽出4行）

> 11.3 Bad Markov chain, slow Markov chain? . . . . . . . . . . . . . . . . . . . . . . .
> 11.4 Building up the model
> . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
> 11.5 General lessons from the planetary motion example . . . . . . . . . . . . . . . . .

### 日本語訳（自動翻訳）

> 11.3 悪いマルコフ連鎖、遅いマルコフ連鎖? 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。
> 11.4 モデルの構築
> 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。
> 11.5 惑星運動の例から得られる一般的な教訓。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。

### 熟語・専門語

- **ESS**: 有効サンプルサイズ。自己相関を考慮した独立サンプル相当数。
- **Markov chain**: マルコフ連鎖。MCMCで事後分布からサンプルを得るための確率過程。

### 要約

- 11.3 悪いマルコフ連鎖、遅いマルコフ連鎖? 。

## Chunk 0041

### English（抽出4行）

> 12 Discussion
> 12.1 Diﬀerent perspectives on statistical modeling and prediction
> . . . . . . . . . . . .
> 12.2 Justiﬁcation of iterative model building

### 日本語訳（自動翻訳）

> 12 ディスカッション
> 12.1 統計モデリングと予測に関するさまざまな視点
> 。 。 。 。 。 。 。 。 。 。 。 。
> 12.2 反復モデル構築の正当性

### 熟語・専門語

- **model building**: モデル構築。仮定・データ構造・prior・likelihoodを組み合わせる工程。
- **prediction**: 予測。未知/将来/除外データに対する分布や点推定。

### 要約

- 12 ディスカッション 12.1 統計モデリングと予測に関するさまざまな視点 。

## Chunk 0042

### English（抽出4行）

> . . . . . . . . . . . . . . . . . . . . . . .
> 12.3 Model selection and overﬁtting . . . . . . . . . . . . . . . . . . . . . . . . . . . .
> 12.4 Bigger datasets demand bigger models . . . . . . . . . . . . . . . . . . . . . . . .
> 12.5 Prediction, generalization, and poststratiﬁcation . . . . . . . . . . . . . . . . . . .

### 日本語訳（自動翻訳）

> 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。
> 12.3 モデルの選択とオーバーフィッティング。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。
> 12.4 より大きなデータセットにはより大きなモデルが必要です。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。
> 12.5 予測、一般化、および事後層別化。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。

### 熟語・専門語

- **prediction**: 予測。未知/将来/除外データに対する分布や点推定。

### 要約

- 。

## Chunk 0043

### English（抽出4行）

> 12.6 Going forward . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
> 1.
> Introduction
> 1.1.

### 日本語訳（自動翻訳）

> 12.6 今後の展開。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。 。
> 1.
> はじめに
> 1.1.

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- 12.6 今後の展開。

## Chunk 0044

### English（抽出4行）

> From Bayesian inference to Bayesian workflow
> If mathematical statistics is to be the theory of applied statistics, then any serious discussion of
> Bayesian methods needs to be clear about how they are used in practice. In particular, we need to
> clearly separate concepts of Bayesian inference from Bayesian data analysis and, critically, from

### 日本語訳（自動翻訳）

> ベイズ推論からベイズ ワークフローへ
> 数理統計が応用統計の理論であるならば、それについての真剣な議論は必要ありません。
> ベイジアン手法は、実際にどのように使用されるかを明確にする必要があります。特に、次のことを行う必要があります。
> ベイズ推論の概念とベイズデータ分析、そして重要なことに、

### 熟語・専門語

- **Bayesian workflow**: ベイズワークフロー。モデル構築・推論・診断・改善・比較を反復する実務プロセス。
- **Bayesian inference**: ベイズ推論。事前分布と尤度から事後分布を計算する中核処理。
- **workflow**: ワークフロー。実務分析の反復手順全体。

### 要約

- ベイズ推論からベイズ ワークフローへ 数理統計が応用統計の理論であるならば、それについての真剣な議論は必要ありません。

## Chunk 0045

### English（抽出4行）

> full Bayesian workﬂow (the object of our attention).
> Bayesian inference is just the formulation and computation of conditional probability or proba-
> bility densities, p(θ|y) ∝p(θ)p(y|θ). Bayesian workﬂow includes the three steps of model building,
> inference, and model checking/improvement, along with the comparison of diﬀerent models, not

### 日本語訳（自動翻訳）

> 完全なベイジアン ワークフロー (注目の対象)。
> ベイズ推論は、条件付き確率または確率の定式化と計算にすぎません。
> 能力密度、p(θ|y) ∝p(θ)p(y|θ)。ベイジアン ワークフローには、モデル構築の 3 つのステップが含まれます。
> 推論、モデルのチェック/改善、およびさまざまなモデルの比較。

### 熟語・専門語

- **Bayesian inference**: ベイズ推論。事前分布と尤度から事後分布を計算する中核処理。
- **model checking**: モデルチェック。モデルの仮定・予測・計算結果がデータや目的に合うか検査すること。
- **model building**: モデル構築。仮定・データ構造・prior・likelihoodを組み合わせる工程。

### 要約

- 完全なベイジアン ワークフロー (注目の対象)。

## Chunk 0046

### English（抽出4行）

> just for the purpose of model choice or model averaging but more importantly to better understand
> these models. That is, for example, why some models have trouble predicting certain aspects of the
> data, or why uncertainty estimates of important parameters can vary across models. Even when
> we have a model we like, it will be useful to compare its inferences to those from simpler and

### 日本語訳（自動翻訳）

> 単にモデルの選択やモデルの平均化を目的としていますが、より深く理解することがより重要です。
> これらのモデル。たとえば、一部のモデルが環境の特定の側面を予測するのが難しいのはこのためです。
> データ、または重要なパラメータの不確実性推定値がモデル間で異なる可能性がある理由。いつでも
> 気に入ったモデルがあるので、その推論をより単純な推論と比較すると便利です。

### 熟語・専門語

- **uncertainty**: 不確実性。観測・パラメータ・モデル構造・意思決定に残る曖昧さ。

### 要約

- 単にモデルの選択やモデルの平均化を目的としていますが、より深く理解することがより重要です。

## Chunk 0047

### English（抽出4行）

> more complicated models as a way to understand what the model is doing. Figure 1 provides an
> outline. An extended Bayesian workﬂow would also include pre-data design of data collection and
> measurement and after-inference decision making, but we focus here on modeling the data.
> In a typical Bayesian workﬂow we end up ﬁtting a series of models, some of which are

### 日本語訳（自動翻訳）

> モデルが何をしているのかを理解する方法として、より複雑なモデルを使用します。図 1 は、
> 概要。拡張ベイジアン ワークフローには、データ収集の事前データ設計も含まれます。
> 測定と推論後の意思決定ですが、ここではデータのモデル化に焦点を当てます。
> 典型的なベイジアン ワークフローでは、最終的に一連のモデルを当てはめることになります。

### 熟語・専門語

- **decision**: 意思決定。予測分布を損失・効用・行動選択へ接続する工程。

### 要約

- モデルが何をしているのかを理解する方法として、より複雑なモデルを使用します。

## Chunk 0048

### English（抽出4行）

> in retrospect poor choices (for reasons including poor ﬁt to data; lack of connection to relevant
> substantive theory or practical goals; priors that are too weak, too strong, or otherwise inappropriate;
> or simply from programming errors), some of which are useful but ﬂawed (for example, a regression
> that adjusts for some confounders but excludes others, or a parametric form that captures some

### 日本語訳（自動翻訳）

> 振り返ってみると、不適切な選択（データへの適合性の低さ、関連する情報とのつながりの欠如などの理由）
> 実質的な理論または実践的な目標。事前分布が弱すぎる、強すぎる、またはその他の点で不適切である。
> または単にプログラミングエラーによるものなど）、中には便利ですが欠陥のあるものもあります（回帰など）
> 一部の交絡因子を調整して他の交絡因子を除外するもの、または一部を捕捉するパラメトリック形式

### 熟語・専門語

- **ESS**: 有効サンプルサイズ。自己相関を考慮した独立サンプル相当数。

### 要約

- 振り返ってみると、不適切な選択（データへの適合性の低さ、関連する情報とのつながりの欠如などの理由） 実質的な理論または実践的な目標。

## Chunk 0049

### English（抽出4行）

> but not all of a functional relationship), and some of which are ultimately worth reporting. The
> hopelessly wrong models and the seriously ﬂawed models are, in practice, unavoidable steps along
> the way toward ﬁtting the useful models. Recognizing this can change how we set up and apply
> statistical methods.

### 日本語訳（自動翻訳）

> ただし、機能的な関係のすべてではありません）、そのうちのいくつかは最終的に報告する価値があります。の
> 絶望的に間違ったモデルや深刻な欠陥のあるモデルは、実際には避けられないステップです。
> 有用なモデルを当てはめる方法。これを認識すると、設定と適用の方法が変わる可能性があります
> 統計的手法。

### 熟語・専門語

- **ESS**: 有効サンプルサイズ。自己相関を考慮した独立サンプル相当数。

### 要約

- ただし、機能的な関係のすべてではありません）、そのうちのいくつかは最終的に報告する価値があります。

## Chunk 0050

### English（抽出4行）

> 1.2.
> Why do we need a Bayesian workflow?
> We need a Bayesian workﬂow, rather than mere Bayesian inference, for several reasons.
> • Computation can be a challenge, and we often need to work through various steps including

### 日本語訳（自動翻訳）

> 1.2.
> なぜベイズ ワークフローが必要なのでしょうか?
> いくつかの理由から、単なるベイズ推論ではなく、ベイズ ワークフローが必要です。
> • 計算は難しい場合があり、多くの場合、次のようなさまざまな手順を実行する必要があります。

### 熟語・専門語

- **Bayesian workflow**: ベイズワークフロー。モデル構築・推論・診断・改善・比較を反復する実務プロセス。
- **Bayesian inference**: ベイズ推論。事前分布と尤度から事後分布を計算する中核処理。
- **workflow**: ワークフロー。実務分析の反復手順全体。

### 要約

- 1.2. なぜベイズ ワークフローが必要なのでしょうか? いくつかの理由から、単なるベイズ推論ではなく、ベイズ ワークフローが必要です。

## Chunk 0051

### English（抽出4行）

> ﬁtting simpler or alternative models, approximate computation that is less accurate but faster,
> and exploration of the ﬁtting process, in order to get to inferences that we trust.
> • In diﬃcult problems we typically do not know ahead of time what model we want to ﬁt, and
> even in those rare cases that an acceptable model has been chosen ahead of time, we will

### 日本語訳（自動翻訳）

> より単純なモデルまたは代替モデルのフィッティング、精度は低いが高速な近似計算、
> そして、信頼できる推論を得るために、フィッティングプロセスを調査します。
> • 難しい問題では、通常、どのモデルを当てはめたいのか事前にわかりません。
> まれに、許容可能なモデルが事前に選択されている場合でも、

### 熟語・専門語

- **ESS**: 有効サンプルサイズ。自己相関を考慮した独立サンプル相当数。
- **approximate**: 近似。速度や扱いやすさのため、正確な推論・モデルを緩めること。

### 要約

- より単純なモデルまたは代替モデルのフィッティング、精度は低いが高速な近似計算、 そして、信頼できる推論を得るために、フィッティングプロセスを調査します。

## Chunk 0052

### English（抽出4行）

> generally want to expand it as we gather more data or want to ask more detailed questions of
> the data we have.
> • Even if our data were static, and we knew what model to ﬁt, and we had no problems ﬁtting
> it, we still would want to understand the ﬁtted model and its relation to the data, and that

### 日本語訳（自動翻訳）

> 一般に、より多くのデータを収集するにつれてそれを拡張したい、またはより詳細な質問をしたいと考えています。
> 私たちが持っているデータ。
> • データが静的で、どのモデルを当てはめるべきかが分かっていて、問題なく当てはめることができたとしても
> それでも、適合モデルとそのデータとの関係を理解したいと思うでしょう。

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- 一般に、より多くのデータを収集するにつれてそれを拡張したい、またはより詳細な質問をしたいと考えています。

## Chunk 0053

### English（抽出4行）

> understanding can often best be achieved by comparing inferences from a series of related
> models.
> • Sometimes diﬀerent models yield diﬀerent conclusions, without one of them being clearly
> favourable. In such cases, presenting multiple models is helpful to illustrate the uncertainty

### 日本語訳（自動翻訳）

> 多くの場合、関連する一連の推論からの推論を比較することで最もよく理解できます。
> モデル。
> • 異なるモデルは、いずれかが明確ではないにもかかわらず、異なる結論をもたらす場合があります。
> 好ましい。このような場合、複数のモデルを提示すると、不確実性を説明するのに役立ちます。

### 熟語・専門語

- **uncertainty**: 不確実性。観測・パラメータ・モデル構造・意思決定に残る曖昧さ。

### 要約

- 多くの場合、関連する一連の推論からの推論を比較することで最もよく理解できます。

## Chunk 0054

### English（抽出4行）

> in model choice.
> 1.3.
> “Workflow” and its relation to statistical theory and practice
> “Workﬂow” has diﬀerent meanings in diﬀerent contexts. For the purposes of this paper it should

### 日本語訳（自動翻訳）

> モデル選択において。
> 1.3.
> 「ワークフロー」と統計理論および実践との関係
> 「ワークフロー」は、さまざまな文脈でさまざまな意味を持ちます。この文書の目的上、次のようにする必要があります。

### 熟語・専門語

- **workflow**: ワークフロー。実務分析の反復手順全体。

### 要約

- モデル選択において。

## Chunk 0055

### English（抽出4行）

> suﬃce that workﬂow is more general than an example but less precisely speciﬁed than a method.
> We have been inﬂuenced by the ideas about workﬂow in computing that are in the air, including
> statistical developments such as the tidyverse which are not particularly Bayesian but have a similar
> feel of experiential learning (Wickham and Groelmund, 2017). Many of the recent developments in

### 日本語訳（自動翻訳）

> ワークフローは例よりも一般的ですが、メソッドよりも厳密に指定されているわけではありません。
> 私たちは、現在進行中のコンピューティングのワークフローに関するアイデアに影響を受けてきました。
> Tidyverse などの統計的開発は、特にベイズ主義ではありませんが、同様の特徴を持っています。
> 経験的な学習の感覚 (Wickham と Groelmund、2017)。最近の開発の多くは、

### 熟語・専門語

- **ESS**: 有効サンプルサイズ。自己相関を考慮した独立サンプル相当数。

### 要約

- ワークフローは例よりも一般的ですが、メソッドよりも厳密に指定されているわけではありません。

## Chunk 0056

### English（抽出4行）

> machine learning have a similar plug-and-play feel: they are easy to use, easy to experiment with,
> and users have the healthy sense that ﬁtting a model is a way of learning something from the data
> without representing a commitment to some probability model or set of statistical assumptions.
> Figure 2 shows our perspective on the development of statistical methodology as a process

### 日本語訳（自動翻訳）

> 機械学習も同様のプラグアンドプレイ感覚を持っています。使いやすく、実験も簡単です。
> ユーザーは、モデルの適合がデータから何かを学ぶ方法であるという健全な感覚を持っています。
> 何らかの確率モデルや一連の統計的仮定へのコミットメントを表すものではありません。
> 図 2 は、プロセスとしての統計的方法論の開発に関する私たちの視点を示しています。

### 熟語・専門語

- **ESS**: 有効サンプルサイズ。自己相関を考慮した独立サンプル相当数。

### 要約

- 機械学習も同様のプラグアンドプレイ感覚を持っています。

## Chunk 0057

### English（抽出4行）

> of increasing codiﬁcation, from example to case study to workﬂow to method to theory. Not
> all methods will reach these ﬁnal levels of mathematical abstraction, but looking at the history
> Figure 1: Overview of the steps we currently consider in Bayesian workﬂow. Numbers in brackets
> refer to sections of this paper where the steps are discussed. The chart aims to show possible

### 日本語訳（自動翻訳）

> 例からケーススタディ、ワークフロー、メソッド、理論に至るまで、成文化が増加しています。そうではない
> すべてのメソッドは数学的抽象化の最終レベルに到達しますが、歴史を見ると
> 図 1: ベイジアン ワークフローで現在検討しているステップの概要。括弧内の数字
> この文書の手順について説明しているセクションを参照してください。チャートは可能性を示すことを目的としています

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- 例からケーススタディ、ワークフロー、メソッド、理論に至るまで、成文化が増加しています。

## Chunk 0058

### English（抽出4行）

> steps and paths an individual analysis may go through, with the understanding that any particular
> analysis will most likely not involve all of these steps. One of our goals in studying workﬂow is to
> understand how these ideas ﬁt together so they can be applied more systematically.
> Example · · · Case study · · · Workﬂow · · · Method · · · Theory

### 日本語訳（自動翻訳）

> 特定の分析が実行される可能性のあるステップとパス。
> 分析にはこれらすべての手順が含まれない可能性が高くなります。ワークフローを研究する私たちの目標の 1 つは、
> これらのアイデアがどのように組み合わされるかを理解して、より体系的に適用できるようにします。
> 例 · · · ケーススタディ · · · ワークフロー · · · 手法 · · · 理論

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- 特定の分析が実行される可能性のあるステップとパス。

## Chunk 0059

### English（抽出4行）

> Figure 2: Meta-workﬂow of statistical methodology, representing the way in which new ideas ﬁrst
> appear in examples, then get formalized into case studies, codiﬁed as workﬂows, are given general
> implementation as algorithms, and become the subject of theories.
> of statistics we have seen new methods being developed in the context of particular examples,

### 日本語訳（自動翻訳）

> 図 2: 新しいアイデアが最初に生まれる方法を表す統計的方法論のメタワークフロー
> 例に登場し、その後ケーススタディとして形式化され、ワークフローとして体系化され、一般的な説明が与えられます。
> アルゴリズムとして実装され、理論の主題になります。
> 統計に関しては、特定の例に基づいて新しい手法が開発されているのを見てきました。

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- 図 2: 新しいアイデアが最初に生まれる方法を表す統計的方法論のメタワークフロー 例に登場し、その後ケーススタディとして形式化され、ワークフローとして体系化され、一般的な説明が与えられます。

## Chunk 0060

### English（抽出4行）

> stylized into case studies, set up as templates or workﬂows for new problems, and, when possible,
> formalized, coded, and studied theoretically.
> One way to understand Figure 2 is through important ideas in the history of statistics that have
> moved from left to right along that path. There have been many ideas that started out as hacks or

### 日本語訳（自動翻訳）

> ケーススタディに定型化され、新しい問題のテンプレートまたはワークフローとして設定され、可能であれば、
> 形式化され、コード化され、理論的に研究されます。
> 図 2 を理解する 1 つの方法は、統計の歴史における重要な考え方を通して見ることです。
> その道に沿って左から右に移動しました。ハックやアイデアとして始まったアイデアはたくさんあります。

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- ケーススタディに定型化され、新しい問題のテンプレートまたはワークフローとして設定され、可能であれば、 形式化され、コード化され、理論的に研究されます。

## Chunk 0061

### English（抽出4行）

> statistics-adjacent tools and eventually were formalized as methods and brought into the core of
> statistics. Multilevel modeling is a formalization of what has been called empirical Bayes estimation
> of prior distributions, expanding the model so as to fold inference about priors into a fully Bayesian
> framework. Exploratory data analysis can be understood as a form of predictive model checking

### 日本語訳（自動翻訳）

> 統計に隣接するツールであり、最終的にはメソッドとして形式化され、統計の中核に組み込まれました。
> 統計。マルチレベル モデリングは、いわゆる経験的ベイズ推定を形式化したものです。
> 事前分布の推論を完全なベイジアンに折り畳むようにモデルを拡張します。
> フレームワーク。探索的データ分析は、予測モデル チェックの一種として理解できます。

### 熟語・専門語

- **model checking**: モデルチェック。モデルの仮定・予測・計算結果がデータや目的に合うか検査すること。
- **prior distribution**: 事前分布。データ観測前の知識・制約を表す分布。

### 要約

- 統計に隣接するツールであり、最終的にはメソッドとして形式化され、統計の中核に組み込まれました。

## Chunk 0062

### English（抽出4行）

> (Gelman, 2003). Regularization methods such as lasso (Tibshirani, 1996) and horseshoe (Piironen
> et al., 2020) have replaced ad hoc variable selection tools in regression. Nonparametric models
> such as Gaussian processes (O’Hagan, 1978, Rasumussen and Williams, 2006) can be thought of as
> Bayesian replacements for procedures such as kernel smoothing. In each of these cases and many

### 日本語訳（自動翻訳）

> (ゲルマン、2003)。なげなわ (Tibshirani、1996) やホースシュー (Piironen) などの正則化手法
> et al., 2020) は、回帰におけるアドホック変数選択ツールを置き換えました。ノンパラメトリックモデル
> ガウス過程 (O'Hagan、1978、Rasumussen および Williams、2006) のようなものは、次のように考えることができます。
> カーネル スムージングなどの手順のベイジアン置換。これらのそれぞれの場合と多くの場合、

### 熟語・専門語

- **ESS**: 有効サンプルサイズ。自己相関を考慮した独立サンプル相当数。

### 要約

- (ゲルマン、2003)。

## Chunk 0063

### English（抽出4行）

> others, a framework of statistical methodology has been expanded to include existing methods,
> along the way making the methods more modular and potentially useful.
> The term “workﬂow” has been gradually coming into use in statistics and data science; see for
> example Liu et al. (2005), Lins et al. (2008), Long (2009), and Turner and Lambert (2015). Related

### 日本語訳（自動翻訳）

> 他には、統計的方法論の枠組みが拡張され、既存の方法が含まれるようになりました。
> その過程で、メソッドはよりモジュール化され、潜在的に有用なものになります。
> 「ワークフロー」という用語は、統計とデータ サイエンスの分野で徐々に使用されるようになってきています。見てください
> 例：Liuら。 (2005)、リンズら。 （2008）、ロング（2009）、ターナーとランバート（2015）。関連

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- 他には、統計的方法論の枠組みが拡張され、既存の方法が含まれるようになりました。

## Chunk 0064

### English（抽出4行）

> ideas of workﬂow are in the air in software development and other ﬁelds of informatics; recent
> discussions for practitioners include Wilson et al. (2014, 2017). Applied statistics (not just Bayesian
> statistics) has become increasingly computational and algorithmic, and this has placed workﬂow at
> the center of statistical practice (see, for example, Grolemund and Wickham, 2017, Bryan, 2017,

### 日本語訳（自動翻訳）

> ワークフローのアイデアは、ソフトウェア開発やその他の情報学の分野で広まっています。最近の
> 実践者向けのディスカッションには、Wilson et al. が含まれます。 （2014年、2017年）。応用統計学 (ベイジアンだけではない)
> 統計) はますます計算的かつアルゴリズム的になり、これによりワークフローは次のようなものになっています。
> 統計実践の中心地 (例: Grolemund and Wickham、2017、Bryan、2017、

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- ワークフローのアイデアは、ソフトウェア開発やその他の情報学の分野で広まっています。

## Chunk 0065

### English（抽出4行）

> and Yu and Kumbier, 2020), as well as in application areas (for example, Lee et al., 2019, discuss
> modeling workﬂow in psychology research). “Bayesian workﬂow” has been expressed as a general
> concept by Savage (2016), Gabry et al. (2019), and Betancourt (2020a). Several of the individual
> components of Bayesian workﬂow were discussed by Gelman (2011) but not in a coherent way. In

### 日本語訳（自動翻訳）

> Yu と Kumbier、2020 年）、および応用分野でも同様です（たとえば、Lee et al.、2019 年、
> 心理学研究におけるワークフローのモデリング）。 「ベイズ ワークフロー」は一般的に表現されています。
> Savage (2016)、Gabry らによるコンセプト（2019）、およびベタンクール（2020a）。個体の何人かが
> ベイジアン ワークフローのコンポーネントについては、Gelman (2011) によって議論されましたが、一貫した方法ではありませんでした。で

### 熟語・専門語

- **ESS**: 有効サンプルサイズ。自己相関を考慮した独立サンプル相当数。

### 要約

- Yu と Kumbier、2020 年）、および応用分野でも同様です（たとえば、Lee et al.、2019 年、 心理学研究におけるワークフローのモデリング）。

## Chunk 0066

### English（抽出4行）

> addition there has been development of Bayesian workﬂow for particular problems, as by Shi and
> Stevens (2008) and Chiu et al. (2017).
> In this paper we go through several aspects of Bayesian workﬂow with the hope that these can
> ultimately make their way into routine practice and automatic software. We set up much of our

### 日本語訳（自動翻訳）

> さらに、Shi や Shi らによる、特定の問題に対するベイジアン ワークフローの開発も行われています。
> Stevens (2008) および Chiu et al. （2017年）。
> このホワイト ペーパーでは、ベイズ ワークフローのいくつかの側面について説明します。これらの側面が実現できることを期待しています。
> 最終的には、日常的な実践や自動ソフトウェアに組み込まれます。私たちは多くのことをセットアップしました

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- さらに、Shi や Shi らによる、特定の問題に対するベイジアン ワークフローの開発も行われています。

## Chunk 0067

### English（抽出4行）

> workﬂow in the probabilistic programming language Stan (Carpenter et al., 2017, Stan Development
> Team, 2020), but similar ideas apply in other computing environments.1
> 1.4.
> Organizing the many aspects of Bayesian workflow

### 日本語訳（自動翻訳）

> 確率的プログラミング言語 Stan のワークフロー (Carpenter et al.、2017、Stan Development)
> Team、2020) ですが、同様の考え方が他のコンピューティング環境にも当てはまります。1
> 1.4.
> ベイジアン ワークフローのさまざまな側面を整理する

### 熟語・専門語

- **Bayesian workflow**: ベイズワークフロー。モデル構築・推論・診断・改善・比較を反復する実務プロセス。
- **probabilistic programming**: 確率的プログラミング。Stanなどで確率モデルをコードとして記述し推論する方法。
- **workflow**: ワークフロー。実務分析の反復手順全体。

### 要約

- 確率的プログラミング言語 Stan のワークフロー (Carpenter et al.、2017、Stan Development) Team、2020) ですが、同様の考え方が他のコンピューティング環境にも当てはまります。

## Chunk 0068

### English（抽出4行）

> Textbook presentations of statistical workﬂow are often linear, with diﬀerent paths corresponding
> to diﬀerent problem situations. For example, a clinical trial in medicine conventionally begins with
> 1Wikipedia currently lists more than 50 probabilistic programming frameworks:
> en.wikipedia.org/wiki/

### 日本語訳（自動翻訳）

> 統計ワークフローの教科書的な表現は、多くの場合、対応するさまざまなパスを持つ直線的なものです。
> さまざまな問題状況に対応します。たとえば、医学における臨床試験は通常、次のように始まります。
> 1Wikipedia には現在、50 を超える確率的プログラミング フレームワークがリストされています。
> en.wikipedia.org/wiki/

### 熟語・専門語

- **probabilistic programming**: 確率的プログラミング。Stanなどで確率モデルをコードとして記述し推論する方法。

### 要約

- 統計ワークフローの教科書的な表現は、多くの場合、対応するさまざまなパスを持つ直線的なものです。

## Chunk 0069

### English（抽出4行）

> Probabilistic_programming.
> a sample size calculation and analysis plan, followed by data collection, cleaning, and statistical
> analysis, and concluding with the reporting of p-values and conﬁdence intervals. An observational
> study in economics might begin with exploratory data analysis, which then informs choices of

### 日本語訳（自動翻訳）

> 確率的プログラミング。
> サンプルサイズの計算と分析計画、その後のデータ収集、クリーニング、統計
> 分析し、p 値と信頼区間のレポートで終了します。観察
> 経済学の研究は、探索的なデータ分析から始まり、その後、次の選択肢が得られます。

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- 確率的プログラミング。

## Chunk 0070

### English（抽出4行）

> transformations of variables, followed by a set of regression analyses and then an array of alternative
> speciﬁcations and robustness studies.
> The statistical workﬂow discussed in this article is more tangled than the usual data analysis
> workﬂows presented in textbooks and research articles. The additional complexity comes in several

### 日本語訳（自動翻訳）

> 変数の変換、その後の回帰分析のセット、そして代替の配列
> 仕様と堅牢性の研究。
> この記事で説明する統計ワークフローは、通常のデータ分析よりも複雑です
> 教科書や研究論文で紹介されているワークフロー。追加の複雑さはいくつかあります

### 熟語・専門語

- **ESS**: 有効サンプルサイズ。自己相関を考慮した独立サンプル相当数。

### 要約

- 変数の変換、その後の回帰分析のセット、そして代替の配列 仕様と堅牢性の研究。

## Chunk 0071

### English（抽出4行）

> places and there are many sub-workﬂows inside the higher level workﬂow:
> 1. Computation to ﬁt a complex model can itself be diﬃcult, requiring a certain amount of
> experimentation to solve the problem of computing, approximating, or simulating from the
> desired posterior distribution, along with checking that the computational algorithm did what

### 日本語訳（自動翻訳）

> 上位レベルのワークフロー内には多くのサブワークフローがあります。
> 1. 複雑なモデルに適合させるための計算自体が難しい場合があり、ある程度の量の計算が必要になります。
> 計算、近似、またはシミュレーションの問題を解決するための実験。
> 計算アルゴリズムが何を行ったかを確認するとともに、望ましい事後分布を確認します。

### 熟語・専門語

- **posterior distribution**: 事後分布。データ観測後の未知量の不確実性を表す分布。

### 要約

- 上位レベルのワークフロー内には多くのサブワークフローがあります。

## Chunk 0072

### English（抽出4行）

> it was intended to do.
> 2. With complex problems we typically have an idea of a general model that is more complex
> than we can easily computationally ﬁt (for example including features such as correlations,
> hierarchical structure, and parameters varying over time), and so we start with a model that

### 日本語訳（自動翻訳）

> それはするつもりだった。
> 2. 複雑な問題の場合、私たちは通常、より複雑な一般的なモデルのアイデアを持っています。
> 計算的に適合させるのは簡単ではありません (たとえば、相関関係などの特徴を含める)。
> 階層構造、および時間の経過とともに変化するパラメーター)、したがって、次のモデルから始めます。

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- それはするつもりだった。

## Chunk 0073

### English（抽出4行）

> we know is missing some important features, in the hope it will be computationally easier,
> with the understanding that we will gradually add in features.
> 3. Relatedly, we often consider problems where the data are not ﬁxed, either because data
> collection is ongoing or because we have the ability to draw in related datasets, for example

### 日本語訳（自動翻訳）

> いくつかの重要な機能が欠けていることはわかっていますが、計算が簡単になることを願っています。
> 徐々に機能を追加していきますのでご了承ください。
> 3. これに関連して、データが修正されていない問題をよく考えます。
> 収集が進行中であるか、関連するデータセットを取り込む機能があるためです。

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- いくつかの重要な機能が欠けていることはわかっていますが、計算が簡単になることを願っています。

## Chunk 0074

### English（抽出4行）

> new surveys in a public opinion analysis or data from other experiments in a drug trial.
> Adding new data often requires model extensions to allow parameters to vary or to extend
> functional forms, as for example a linear model might ﬁt well at ﬁrst but then break down
> with data are added under new conditions.

### 日本語訳（自動翻訳）

> 世論分析における新しい調査や、薬物治験における他の実験からのデータ。
> 新しいデータを追加するには、多くの場合、パラメーターを変更または拡張できるようにするためのモデル拡張が必要になります。
> 関数形式。たとえば、線形モデルは最初はうまく適合するかもしれませんが、その後破綻します。
> 新たな条件でデータを追加しました。

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- 世論分析における新しい調査や、薬物治験における他の実験からのデータ。

## Chunk 0075

### English（抽出4行）

> 4. Beyond all the challenges of ﬁtting and expansion, models can often be best understood by
> comparing to inferences under alternative models. Hence our workﬂow includes tools for
> understanding and comparing multiple models ﬁt to the same data.
> Statistics is all about uncertainty. In addition to the usual uncertainties in the data and model

### 日本語訳（自動翻訳）

> 4. フィッティングと拡張というあらゆる課題を超えて、モデルを最もよく理解できるのは、多くの場合、
> 代替モデルでの推論との比較。したがって、私たちのワークフローには、
> 同じデータに適合する複数のモデルを理解し、比較します。
> 統計には不確実性がつきものです。データとモデルの通常の不確実性に加えて、

### 熟語・専門語

- **uncertainty**: 不確実性。観測・パラメータ・モデル構造・意思決定に残る曖昧さ。

### 要約

- 4. フィッティングと拡張というあらゆる課題を超えて、モデルを最もよく理解できるのは、多くの場合、 代替モデルでの推論との比較。

## Chunk 0076

### English（抽出4行）

> parameters, we are often uncertain whether we are ﬁtting our models correctly, uncertain about
> how best to set up and expand our models, and uncertain in their interpretation. Once we go
> beyond simple preassigned designs and analysis, our workﬂow can be disorderly, with our focus
> moving back and forth between data exploration, substantive theory, computing, and interpretation

### 日本語訳（自動翻訳）

> パラメータを使用すると、モデルを正しく当てはめているかどうかが不確かになることがよくあります。
> モデルをどのように設定して拡張するのが最適か、その解釈は不確かです。行ったら
> 事前に割り当てられた単純な設計と分析を超えて、私たちのワークフローは無秩序になる可能性があります。
> データ探索、実体理論、コンピューティング、解釈の間を行き来する

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- パラメータを使用すると、モデルを正しく当てはめているかどうかが不確かになることがよくあります。

## Chunk 0077

### English（抽出4行）

> of results.
> Thus, any attempt to organize the steps of workﬂow will oversimplify and many
> sub-workﬂows are complex enough to justify their own articles or book chapters.
> We discuss many aspects of workﬂow, but practical considerations—especially available time,

### 日本語訳（自動翻訳）

> 結果の。
> したがって、ワークフローのステップを整理しようとすると、過度に単純化されてしまい、
> サブワークフローは、独自の記事や本の章を正当化するのに十分なほど複雑です。
> 私たちはワークフローの多くの側面について議論しますが、実際的な考慮事項、特に利用可能な時間、

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- 結果の。

## Chunk 0078

### English（抽出4行）

> computational resources and the severity of penalty for being wrong—can compel a practitioner
> to take shortcuts. Such shortcuts can make interpretation of results more diﬃcult, but we must
> be aware that they will be taken, and not ﬁtting a model at all could be worse than ﬁtting it using
> an approximate computation (where approximate can be deﬁned as not giving exact summaries

### 日本語訳（自動翻訳）

> 計算リソースと間違った場合のペナルティの重さ - 実践者が強いられる可能性がある
> ショートカットするため。このようなショートカットは結果の解釈をより困難にする可能性がありますが、
> モデルをまったく当てはめないことは、モデルを使って当てはめるより悪い可能性があることに注意してください。
> 近似計算 (近似とは正確な要約を与えないものとして定義できます)

### 熟語・専門語

- **approximate**: 近似。速度や扱いやすさのため、正確な推論・モデルを緩めること。

### 要約

- 計算リソースと間違った場合のペナルティの重さ - 実践者が強いられる可能性がある ショートカットするため。

## Chunk 0079

### English（抽出4行）

> of the posterior distribution even in the limit of inﬁnite compute time). Our aim in describing
> statistical workﬂow is thus also to explicitly understand various shortcuts as approximations to
> the full workﬂow, letting practitioners to make more informed choices about where to invest their
> limited time and energy.

### 日本語訳（自動翻訳）

> 無限の計算時間の制限内であっても事後分布の変化を考慮します)。説明における私たちの目的
> したがって、統計的ワークフローは、さまざまなショートカットを次の近似として明示的に理解することでもあります。
> 完全なワークフローにより、実務者はどこに投資するかについてより多くの情報に基づいた選択が可能になります。
> 限られた時間とエネルギー。

### 熟語・専門語

- **posterior distribution**: 事後分布。データ観測後の未知量の不確実性を表す分布。

### 要約

- 無限の計算時間の制限内であっても事後分布の変化を考慮します)。

## Chunk 0080

### English（抽出4行）

> 1.5.
> Aim and structure of this article
> There is all sorts of tacit knowledge in applied statistics that does not always make it into published
> papers and textbooks. The present article is intended to put some of these ideas out in the open, both

### 日本語訳（自動翻訳）

> 1.5.
> この記事の目的と構成
> 応用統計にはあらゆる種類の暗黙知があり、必ずしも公表されるわけではありません
> 論文と教科書。この記事は、これらのアイデアの一部を公開することを目的としています。

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- 1.5. この記事の目的と構成 応用統計にはあらゆる種類の暗黙知があり、必ずしも公表されるわけではありません 論文と教科書。

## Chunk 0081

### English（抽出4行）

> to improve applied Bayesian analyses and to suggest directions for future development of theory,
> methods, and software.
> Our target audience is (a) practitioners of applied Bayesian statistics, especially users of proba-
> bilistic programming languages such as Stan, and (b) developers of methods and software intended

### 日本語訳（自動翻訳）

> 応用ベイズ分析を改善し、理論の将来の発展の方向性を示唆すること。
> メソッドもソフトウェアも。
> 私たちの対象読者は、(a) 応用ベイズ統計の実践者、特に検定統計のユーザーです。
> Stan などのバイリスティック プログラミング言語、および (b) 対象となるメソッドおよびソフトウェアの開発者

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- 応用ベイズ分析を改善し、理論の将来の発展の方向性を示唆すること。

## Chunk 0082

### English（抽出4行）

> for these users. We are also targeting researchers of Bayesian theory and methods, as we believe
> that many of these aspects of workﬂow have been under-studied.
> In the rest of the paper we go more slowly through individual aspects of Bayesian workﬂow
> as outlined in Figure 1, starting with steps to be done before a model is ﬁt (Section 2), through

### 日本語訳（自動翻訳）

> このようなユーザーのために。私たちは、ベイズ理論と手法の研究者もターゲットにしていると考えています。
> ワークフローのこれらの側面の多くは十分に研究されていません。
> この文書の残りの部分では、ベイジアン ワークフローの個々の側面をゆっくりと見ていきます。
> 図 1 に概要を示したように、モデルを適合させる前に実行する手順 (セクション 2) から始まり、

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- このようなユーザーのために。

## Chunk 0083

### English（抽出4行）

> ﬁtting, debugging and evaluating models (Sections 3–6), and then modifying models (Section 7)
> and understanding and comparing a series of models (Section 8).
> Sections 10 and 11 then go through these steps in two examples, one in which we add features
> step by step to a model of golf putting, and one in which we go through a series of investigations

### 日本語訳（自動翻訳）

> モデルのフィッティング、デバッグ、評価 (セクション 3 ～ 6)、その後のモデルの変更 (セクション 7)
> 一連のモデルの理解と比較 (セクション 8)。
> 次に、セクション 10 と 11 では、2 つの例でこれらの手順を説明します。1 つは機能を追加する例です。
> ゴルフパッティングのモデルに段階的に到達し、その中で一連の調査を経ます。

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- モデルのフィッティング、デバッグ、評価 (セクション 3 ～ 6)、その後のモデルの変更 (セクション 7) 一連のモデルの理解と比較 (セクション 8)。

## Chunk 0084

### English（抽出4行）

> to resolve diﬃculties in ﬁtting a simple model of planetary motion. The ﬁrst of these examples
> shows how new data can motivate model improvements, and also illustrates some of the unexpected
> challenges that arise when expanding a model. The second example demonstrates the way in which
> challenges in computation can point to modeling diﬃculties. These two small examples do not

### 日本語訳（自動翻訳）

> 惑星運動の単純なモデルを当てはめる際の困難を解決する。これらの例の最初のもの
> 新しいデータがどのようにモデルの改善を促すことができるかを示し、予期せぬ問題のいくつかも示します
> モデルを拡張するときに生じる課題。 2 番目の例は、次の方法を示しています。
> 計算における課題は、モデリングの困難を示している可能性があります。これら 2 つの小さな例は、

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- 惑星運動の単純なモデルを当てはめる際の困難を解決する。

## Chunk 0085

### English（抽出4行）

> illustrate all the aspects of Bayesian workﬂow, but they should at least suggest that there could be a
> beneﬁt to systematizing the many aspects of Bayesian model development. We conclude in Section
> 12 with some general discussion and our responses to potential criticism of the workﬂow.
> 2.

### 日本語訳（自動翻訳）

> ベイジアン ワークフローのあらゆる側面を示していますが、少なくとも次のような可能性があることを示唆しているはずです。
> ベイジアン モデル開発のさまざまな側面を体系化するのに役立ちます。セクションで結論を述べます
> 12 では、一般的な議論と、ワークフローに対する潜在的な批判に対する私たちの対応を示します。
> 2.

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- ベイジアン ワークフローのあらゆる側面を示していますが、少なくとも次のような可能性があることを示唆しているはずです。

## Chunk 0086

### English（抽出4行）

> Before fitting a model
> 2.1.
> Choosing an initial model
> The starting point of almost all analyses is to adapt what has been done before, using a model from

### 日本語訳（自動翻訳）

> モデルをフィッティングする前に
> 2.1.
> 初期モデルの選択
> ほとんどすべての分析の開始点は、次のモデルを使用して、以前に行われたことを適応させることです。

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- モデルをフィッティングする前に 2.1. 初期モデルの選択 ほとんどすべての分析の開始点は、次のモデルを使用して、以前に行われたことを適応させることです。

## Chunk 0087

### English（抽出4行）

> a textbook or case study or published paper that has been applied to a similar problem (a strongly
> related concept in software engineering is software design pattern). Using a model taken from
> some previous analysis and altering it can be seen as a shortcut to eﬀective data analysis, and by
> looking at the results from the model template we know in which direction of the model space there

### 日本語訳（自動翻訳）

> 同様の問題に適用された教科書、事例研究、または出版された論文（強力な問題）
> ソフトウェア工学における関連概念はソフトウェア設計パターンです)。から取得したモデルを使用する
> 以前の分析とそれを変更することは、効果的なデータ分析への近道と見なすことができます。
> モデル テンプレートの結果を見ると、モデル空間のどの方向にあるかがわかります。

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- 同様の問題に適用された教科書、事例研究、または出版された論文（強力な問題） ソフトウェア工学における関連概念はソフトウェア設計パターンです)。

## Chunk 0088

### English（抽出4行）

> are likely to be useful elaborations or simpliﬁcations. Templates can save time in model building
> and computing, and we should also take into account the cognitive load for the person who needs
> to understand the results. Shortcuts are important for humans as well as computers, and shortcuts
> help explain why the typical workﬂow is iterative (see more in Section 12.2). Similarly, if we were

### 日本語訳（自動翻訳）

> 役立つ詳細または簡略化になる可能性があります。テンプレートによりモデル構築の時間を節約できます
> そしてコンピューティングを必要とする人の認知的負荷も考慮する必要があります。
> 結果を理解するために。ショートカットはコンピューターだけでなく人間にとっても重要であり、ショートカットは
> 一般的なワークフローが反復的である理由を説明するのに役立ちます (詳細はセクション 12.2 を参照)。同様に、私たちがもし

### 熟語・専門語

- **model building**: モデル構築。仮定・データ構造・prior・likelihoodを組み合わせる工程。

### 要約

- 役立つ詳細または簡略化になる可能性があります。

## Chunk 0089

### English（抽出4行）

> to try to program a computer to perform data analysis automatically, it would have to work through
> some algorithm to construct models, and the building blocks of such an algorithm would represent
> templates of a sort. Despite the negative connotations of “cookbook analysis,” we think templates
> can be useful as starting points and comparison points to more elaborate analyses. Conversely, we

### 日本語訳（自動翻訳）

> データ分析を自動的に実行するようにコンピューターをプログラムしようとすると、次の手順を実行する必要があります。
> モデルを構築するためのアルゴリズム、およびそのようなアルゴリズムの構成要素は次のことを表します。
> ある種のテンプレート。 「料理本分析」というネガティブな意味にもかかわらず、私たちはテンプレートを次のように考えています。
> より詳細な分析の開始点および比較点として役立ちます。逆に、私たちは、

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- データ分析を自動的に実行するようにコンピューターをプログラムしようとすると、次の手順を実行する必要があります。

## Chunk 0090

### English（抽出4行）

> should recognize that theories are not static, and the process of development of scientiﬁc theories
> is not the same as that of statistical models (Navarro, 2020).
> Sometimes our workﬂow starts with a simple model with the aim to add features later (modeling
> varying parameters, including measurement errors, correlations, and so forth). Other times we start

### 日本語訳（自動翻訳）

> 理論は静的なものではなく、科学理論の発展の過程であることを認識すべきである
> は統計モデルのそれと同じではありません (Navarro, 2020)。
> 私たちのワークフローは、後で機能を追加することを目的として、単純なモデルから始まることがあります (モデリング
> 測定誤差、相関関係などを含むさまざまなパラメータ）。それ以外の場合は開始します

### 熟語・専門語

- **ESS**: 有効サンプルサイズ。自己相関を考慮した独立サンプル相当数。

### 要約

- 理論は静的なものではなく、科学理論の発展の過程であることを認識すべきである は統計モデルのそれと同じではありません (Navarro, 2020)。

## Chunk 0091

### English（抽出4行）

> with a big model and aim to strip it down in next steps, trying to ﬁnd something that is simple and
> understandable that still captures key features of the data. Sometimes we even consider multiple
> completely diﬀerent approaches to modeling the same data and thus have multiple starting points
> to choose from.

### 日本語訳（自動翻訳）

> 大きなモデルを使用し、次のステップでそれを取り除き、シンプルでシンプルなものを見つけようとします。
> データの主要な特徴を捉えていることは理解できます。場合によっては複数のことを考慮することもあります
> 同じデータをモデル化するのにまったく異なるアプローチがあるため、複数の開始点があります
> から選択します。

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- 大きなモデルを使用し、次のステップでそれを取り除き、シンプルでシンプルなものを見つけようとします。

## Chunk 0092

### English（抽出4行）

> 2.2.
> Modular construction
> A Bayesian model is built from modules which can often be viewed as placeholders to be replaced
> as necessary. For example, we model data with a normal distribution and then replace this with a

### 日本語訳（自動翻訳）

> 2.2.
> モジュール構造
> ベイジアン モデルは、多くの場合、置き換えられるプレースホルダーとして見なされるモジュールから構築されます。
> 必要に応じて。たとえば、正規分布を使用してデータをモデル化し、これを正規分布に置き換えます。

### 熟語・専門語

- **ESS**: 有効サンプルサイズ。自己相関を考慮した独立サンプル相当数。

### 要約

- 2.2. モジュール構造 ベイジアン モデルは、多くの場合、置き換えられるプレースホルダーとして見なされるモジュールから構築されます。

## Chunk 0093

### English（抽出4行）

> longer-tailed or mixture distribution; we model a latent regression function as linear and replace it
> with nonlinear splines or Gaussian processes; we can treat a set of observations as exact and then
> add a measurement-error model; we can start with a weak prior and then make it stronger when
> we ﬁnd the posterior inference includes unrealistic parameter values. Thinking of components as

### 日本語訳（自動翻訳）

> 裾の長い分布または混合分布。潜在回帰関数を線形としてモデル化し、それを置き換えます
> 非線形スプラインまたはガウス過程を使用します。一連の観測値を正確なものとして扱うことができます。
> 測定誤差モデルを追加します。弱い事前分布から始めて、次の場合にそれをより強くすることができます。
> 事後推論には非現実的なパラメータ値が含まれていることがわかります。コンポーネントを次のように考える

### 熟語・専門語

- **ESS**: 有効サンプルサイズ。自己相関を考慮した独立サンプル相当数。

### 要約

- 裾の長い分布または混合分布。

## Chunk 0094

### English（抽出4行）

> placeholders takes some of the pressure oﬀthe model-building process, because you can always go
> back and generalize or add information as necessary.
> The idea of modular construction goes against a long-term tradition in the statistical literature
> where whole models were given names and a new name was given every time a slight change to an

### 日本語訳（自動翻訳）

> プレースホルダーは、いつでも実行できるため、モデル構築プロセスのプレッシャーの一部を軽減します。
> 必要に応じて情報を元に戻して一般化または追加します。
> モジュール構造の考え方は統計文献における長年の伝統に反する
> モデル全体に名前が付けられ、モデルにわずかな変更が加えられるたびに新しい名前が付けられました。

### 熟語・専門語

- **ESS**: 有効サンプルサイズ。自己相関を考慮した独立サンプル相当数。

### 要約

- プレースホルダーは、いつでも実行できるため、モデル構築プロセスのプレッシャーの一部を軽減します。

## Chunk 0095

### English（抽出4行）

> existing model was proposed. Naming model modules rather than whole models makes it easier to
> see connections between seemingly diﬀerent models and adapt them to the speciﬁc requirements
> of the given analysis project.
> 2.3.

### 日本語訳（自動翻訳）

> 既存モデルを提案した。モデル全体ではなくモデルモジュールに名前を付けると、
> 一見異なるモデル間の接続を確認し、特定の要件に適応させる
> 指定された分析プロジェクトの。
> 2.3.

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- 既存モデルを提案した。

## Chunk 0096

### English（抽出4行）

> Scaling and transforming the parameters
> We like our parameters to be interpretable for both practical and ethical reasons.
> This leads
> to wanting them on natural scales and modeling them as independent, if possible, or with an

### 日本語訳（自動翻訳）

> パラメータのスケーリングと変換
> 私たちはパラメータが実用的および倫理的な理由から解釈可能であることを望んでいます。
> これが導きます
> それらを自然なスケールで実現し、可能であれば独立したものとしてモデル化するか、

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- パラメータのスケーリングと変換 私たちはパラメータが実用的および倫理的な理由から解釈可能であることを望んでいます。

## Chunk 0097

### English（抽出4行）

> interpretable dependence structure, as this facilitates the use of informative priors (Gelman, 2004).
> It can also help to separate out the scale so that the unknown parameters are scale-free. For example,
> in a problem in pharmacology (Weber et al., 2018) we had a parameter that we expected would
> take on values of approximately 50 on the scale of measurement; following the principle of scaling

### 日本語訳（自動翻訳）

> 解釈可能な依存構造。これにより、有益な事前分布の使用が容易になります (Gelman、2004)。
> また、未知のパラメーターがスケールフリーになるようにスケールを分離することも役立ちます。たとえば、
> 薬理学の問題 (Weber et al., 2018) では、次のようになると予想されるパラメーターがありました。
> 測定スケールで約 50 の値を取る。スケーリングの原理に従って

### 熟語・専門語

- **approximate**: 近似。速度や扱いやすさのため、正確な推論・モデルを緩めること。

### 要約

- 解釈可能な依存構造。

## Chunk 0098

### English（抽出4行）

> we might set up a model on log(θ/50), so that 0 corresponds to an interpretable value (50 on the
> original scale) and a diﬀerence of 0.1, for example, on the log scale corresponds to increasing or
> decreasing by approximately 10%. This sort of transformation is not just for ease of interpretation;
> it also sets up the parameters in a way that readies them for eﬀective hierarchical modeling. As

### 日本語訳（自動翻訳）

> log(θ/50) にモデルを設定して、0 が解釈可能な値 (
> 元のスケール) と 0.1 の差は、たとえば対数スケールでは増加または増加に対応します。
> 約10％減少します。この種の変換は、解釈を容易にするためだけではありません。
> また、効果的な階層モデリングを準備できるようにパラメータを設定します。として

### 熟語・専門語

- **approximate**: 近似。速度や扱いやすさのため、正確な推論・モデルを緩めること。

### 要約

- log(θ/50) にモデルを設定して、0 が解釈可能な値 ( 元のスケール) と 0.1 の差は、たとえば対数スケールでは増加または増加に対応します。

## Chunk 0099

### English（抽出4行）

> we build larger models, for example by incorporating data from additional groups of patients or
> additional drugs, it will make sense to allow parameters to vary by group (as we discuss in Section
> 12.5), and partial pooling can be more eﬀective on scale-free parameters. For example, a model
> in toxicology required the volume of the liver for each person in the study. Rather than ﬁtting a

### 日本語訳（自動翻訳）

> たとえば追加の患者グループからのデータを組み込むことによって、より大きなモデルを構築します。
> 追加の薬物を使用する場合は、パラメータをグループごとに変更できるようにすることが合理的です (セクションで説明します)。
> 12.5)、部分プーリングはスケールフリー パラメーターでより効果的です。たとえば、モデル
> 毒物学では、研究対象者ごとに肝臓の容積が必要でした。フィッティングするのではなく、

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- たとえば追加の患者グループからのデータを組み込むことによって、より大きなモデルを構築します。

## Chunk 0100

### English（抽出4行）

> hierarchical model to these volumes, we expressed each as the volume of the person multiplied
> by the proportion of volume that the liver; we would expect these scale-free factors to vary less
> across people and so the ﬁtted model can do more partial pooling compared to the result from
> modeling absolute volumes. The scaling transformation is a decomposition that facilitates eﬀective

### 日本語訳（自動翻訳）

> これらの体積を階層モデル化し、それぞれを人の体積の掛け算で表現しました。
> 肝臓の体積の割合による。これらのスケールフリー係数の変動は小さくなると予想されます
> 複数の人々にまたがるため、適合モデルは、
> 絶対ボリュームのモデリング。スケーリング変換は、効果的な変換を容易にする分解です。

### 熟語・専門語

- **ESS**: 有効サンプルサイズ。自己相関を考慮した独立サンプル相当数。

### 要約

- これらの体積を階層モデル化し、それぞれを人の体積の掛け算で表現しました。

## Chunk 0101

### English（抽出4行）

> hierarchical modeling.
> In many cases we can put parameters roughly on unit scale by using logarithmic or logit
> transformations or by standardizing, subtracting a center and dividing by a scale. If the center and
> scale are themselves computed from the data, as we do for default priors in regression coeﬃcients

### 日本語訳（自動翻訳）

> 階層モデリング。
> 多くの場合、対数またはロジットを使用して、パラメータをおおよそ単位スケールに合わせることができます。
> 変換、または標準化、中心を引いてスケールで割ることによって。もしセンターと
> 回帰係数のデフォルト事前分布の場合と同様に、スケール自体がデータから計算されます。

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

> 2 つの予測子
> 4 つの予測子
> 15 個の予測子
> 0.00

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- 2 つの予測子 4 つの予測子 15 個の予測子 0.00

## Chunk 0103

### English（抽出4行）

> 0.25
> 0.50
> 0.75
> 1.00 0.00

### 日本語訳（自動翻訳）

> 0.25
> 0.50
> 0.75
> 1.00 0.00

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- 0.25 0.50 0.75 1.00 0.00

## Chunk 0104

### English（抽出4行）

> 0.25
> 0.50
> 0.75
> 1.00 0.00

### 日本語訳（自動翻訳）

> 0.25
> 0.50
> 0.75
> 1.00 0.00

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- 0.25 0.50 0.75 1.00 0.00

## Chunk 0105

### English（抽出4行）

> 0.25
> 0.50
> 0.75
> 1.00

### 日本語訳（自動翻訳）

> 0.25
> 0.50
> 0.75
> 1.00

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- 0.25 0.50 0.75 1.00

## Chunk 0106

### English（抽出4行）

> Response mean (per data row)
> count
> Figure 3: Demonstration of the use of prior predictive checking to gain understanding of non-
> obvious features of a model. The above graphs correspond to logistic regression models with 100

### 日本語訳（自動翻訳）

> 応答平均 (データ行ごと)
> 数える
> 図 3: 非依存性を理解するための事前予測チェックの使用のデモンストレーション
> モデルの明らかな特徴。上のグラフは、100 のロジスティック回帰モデルに対応します。

### 熟語・専門語

- **prior predictive**: 事前予測。データを見る前のpriorだけで生成される予測分布を確認する診断。
- **ESS**: 有効サンプルサイズ。自己相関を考慮した独立サンプル相当数。

### 要約

- 応答平均 (データ行ごと) 数える 図 3: 非依存性を理解するための事前予測チェックの使用のデモンストレーション モデルの明らかな特徴。

## Chunk 0107

### English（抽出4行）

> data points and 2, 4, or 15 binary covariates. In each case, the regression coeﬃcients were given
> independent normal(0, 1) prior distributions. For each model, we performed a prior predictive
> check, 1000 times simulating the vector of coeﬃcients θ from the prior, then simulating a dataset y
> from the logistic model, and then summarizing this by the mean of the simulated data, ¯y. Each plot

### 日本語訳（自動翻訳）

> データ点と 2、4、または 15 のバイナリ共変量。それぞれの場合において、回帰係数は与えられました。
> 独立した正規(0, 1)事前分布。各モデルについて、事前予測を実行しました。
> 事前の係数 θ のベクトルを 1000 回シミュレートしてから、データセット y をシミュレートします。
> ロジスティック モデルから計算し、これをシミュレートされたデータの平均値 ￣y で要約します。各プロット

### 熟語・専門語

- **prior predictive**: 事前予測。データを見る前のpriorだけで生成される予測分布を確認する診断。
- **prior distribution**: 事前分布。データ観測前の知識・制約を表す分布。
- **ESS**: 有効サンプルサイズ。自己相関を考慮した独立サンプル相当数。

### 要約

- データ点と 2、4、または 15 のバイナリ共変量。

## Chunk 0108

### English（抽出4行）

> shows the prior predictive distribution of this summary statistic, that is, the 1000 simulations of ¯y.
> When the number of covariates in the model is small, this prior predictive distribution is spread out,
> indicating that the model is compatible with a wide range of regimes of data. But as the number
> of covariates increases, the posterior predictive distribution becomes concentrated near ¯y = 0 or

### 日本語訳（自動翻訳）

> は、この要約統計量の事前予測分布、つまり ￣y の 1000 回のシミュレーションを示します。
> モデル内の共変量の数が少ない場合、この事前予測分布は広がります。
> これは、モデルが広範囲のデータ領域と互換性があることを示しています。しかし、数字としては
> 共変量が増加すると、事後予測分布は ￣y = 0 付近に集中するか、

### 熟語・専門語

- **prior predictive**: 事前予測。データを見る前のpriorだけで生成される予測分布を確認する診断。
- **posterior predictive**: 事後予測。推定後のモデルが観測データの特徴を再現できるかを見る診断。

### 要約

- は、この要約統計量の事前予測分布、つまり ￣y の 1000 回のシミュレーションを示します。

## Chunk 0109

### English（抽出4行）

> 1, indicating that weak priors on the individual coeﬃcients of the model imply a strong prior on
> this particular predictive quantity. If we wanted a more moderate prior predictive distribution on
> ¯y, the prior on the coeﬃcients would need to be strongly concentrated near zero.
> in rstanarm (Gabry et al., 2020a), we can consider this as an approximation to a hierarchical model

### 日本語訳（自動翻訳）

> 1、モデルの個々の係数の弱い事前分布が、モデルの強い事前分布を暗示していることを示します。
> この特定の予測量。より穏やかな事前予測分布が必要な場合は、
> y、係数の事前分布はゼロ付近に強く集中する必要があります。
> rstanarm (Gabry et al., 2020a) では、これを階層モデルの近似として考えることができます。

### 熟語・専門語

- **prior predictive**: 事前予測。データを見る前のpriorだけで生成される予測分布を確認する診断。

### 要約

- 1、モデルの個々の係数の弱い事前分布が、モデルの強い事前分布を暗示していることを示します。

## Chunk 0110

### English（抽出4行）

> in which the center and scale are hyperparameters that are estimated from the data.
> More complicated transformations can also serve the purpose of making parameters more
> interpretable and thus facilitating the use of prior information; Riebler et al. (2016) give an example
> for a class of spatial correlation models, and Simpson et al. (2017) consider this idea more generally.

### 日本語訳（自動翻訳）

> ここで、中心とスケールはデータから推定されるハイパーパラメータです。
> より複雑な変換は、パラメータをより詳細にする目的にも役立ちます。
> 解釈可能であるため、事前情報の利用が容易になります。リーブラーら。 (2016) 例を挙げてください
> 空間相関モデルのクラスについては、Simpson et al. (2017) このアイデアをより一般的に検討してください。

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- ここで、中心とスケールはデータから推定されるハイパーパラメータです。

## Chunk 0111

### English（抽出4行）

> 2.4.
> Prior predictive checking
> Prior predictive checks are a useful tool to understand the implications of a prior distribution in
> the context of a generative model (Box, 1980, Gabry et al., 2019; see also Section 7.3 for details

### 日本語訳（自動翻訳）

> 2.4.
> 事前の予測チェック
> 事前予測チェックは、事前分布の影響を理解するのに役立つツールです。
> 生成モデルのコンテキスト (Box, 1980、Gabry et al., 2019; 詳細についてはセクション 7.3 も参照)

### 熟語・専門語

- **prior predictive**: 事前予測。データを見る前のpriorだけで生成される予測分布を確認する診断。
- **prior distribution**: 事前分布。データ観測前の知識・制約を表す分布。
- **generative model**: 生成モデル。データ生成過程を確率的に記述するモデル。

### 要約

- 2.4. 事前の予測チェック 事前予測チェックは、事前分布の影響を理解するのに役立つツールです。

## Chunk 0112

### English（抽出4行）

> on how to work with prior distributions). In particular, because prior predictive checks make use
> of simulations from the model rather than observed data, they provide a way to reﬁne the model
> without using the data multiple times. Figure 3 shows a simple prior predictive check for a logistic
> regression model. The simulation shows that even independent priors on the individual coeﬃcients

### 日本語訳（自動翻訳）

> 以前のディストリビューションを操作する方法について)。特に、事前の予測チェックでは
> 観察されたデータではなくモデルからのシミュレーションを利用して、モデルを改良する方法を提供します。
> データを何度も使用することなく。図 3 は、ロジスティックスに関する簡単な事前予測チェックを示しています。
> 回帰モデル。シミュレーションでは、個々の係数に関する独立した事前分布であっても、

### 熟語・専門語

- **prior predictive**: 事前予測。データを見る前のpriorだけで生成される予測分布を確認する診断。
- **prior distribution**: 事前分布。データ観測前の知識・制約を表す分布。
- **ESS**: 有効サンプルサイズ。自己相関を考慮した独立サンプル相当数。

### 要約

- 以前のディストリビューションを操作する方法について)。

## Chunk 0113

### English（抽出4行）

> have diﬀerent implications as the number of covariates in the model increases. This is a general
> phenomenon in regression models where as the number of predictors increases, we need stronger
> priors on model coeﬃcients (or enough data) if we want to push the model away from extreme
> predictions.

### 日本語訳（自動翻訳）

> モデル内の共変量の数が増加するにつれて、異なる意味を持ちます。これは一般的なものです
> 回帰モデルにおける現象で、予測変数の数が増加するにつれて、より強力な予測変数が必要になります。
> モデルを極端な値から遠ざけたい場合は、モデル係数 (または十分なデータ) の事前分布
> 予測。

### 熟語・専門語

- **ESS**: 有効サンプルサイズ。自己相関を考慮した独立サンプル相当数。
- **prediction**: 予測。未知/将来/除外データに対する分布や点推定。

### 要約

- モデル内の共変量の数が増加するにつれて、異なる意味を持ちます。

## Chunk 0114

### English（抽出4行）

> A useful approach is to consider priors on outcomes and then derive a corresponding joint prior
> on parameters (see, e.g., Piironen and Vehtari, 2017, and Zhang et al., 2020). More generally, joint
> priors allow us to control the overall complexity of larger parameter sets, which helps generate more
> sensible prior predictions that would be hard or impossible to achieve with independent priors.

### 日本語訳（自動翻訳）

> 有用なアプローチは、結果に関する事前分布を考慮し、対応する結合事前分布を導き出すことです。
> パラメータに関する（例えば、Piironen and Vehtari、2017、および Zhang et al.、2020 を参照）。より一般的には、ジョイント
> 事前分布により、より大きなパラメータセットの全体的な複雑さを制御できるようになり、より多くのパラメータを生成するのに役立ちます
> 独立した事前予測では達成が困難または不可能な賢明な事前予測。

### 熟語・専門語

- **prediction**: 予測。未知/将来/除外データに対する分布や点推定。

### 要約

- 有用なアプローチは、結果に関する事前分布を考慮し、対応する結合事前分布を導き出すことです。

## Chunk 0115

### English（抽出4行）

> Figure 4: Prior predictive draws from the Gaussian process model with squared exponential co-
> variance function and diﬀerent values of the amplitude parameter τ and the length scale parameter
> l. From Gelman et al. (2013).
> Figure 4 shows an example of prior predictive checking for three choices of prior distribution for

### 日本語訳（自動翻訳）

> 図 4: 二乗指数共関数を使用したガウス過程モデルからの事前予測の描画
> 分散関数と、振幅パラメータ τ および長さスケール パラメータのさまざまな値
> l.ゲルマンらより。 （2013年）。
> 図 4 は、事前分布の 3 つの選択肢に対する事前予測チェックの例を示しています。

### 熟語・専門語

- **prior predictive**: 事前予測。データを見る前のpriorだけで生成される予測分布を確認する診断。
- **prior distribution**: 事前分布。データ観測前の知識・制約を表す分布。
- **ESS**: 有効サンプルサイズ。自己相関を考慮した独立サンプル相当数。

### 要約

- 図 4: 二乗指数共関数を使用したガウス過程モデルからの事前予測の描画 分散関数と、振幅パラメータ τ および長さスケール パラメータのさまざまな値 l.ゲルマンらより。

## Chunk 0116

### English（抽出4行）

> a Gaussian process model (Rasmussen and Willams, 2006). This sort of simulation and graphical
> comparison is useful when working with any model and essential when setting up unfamiliar or
> complicated models.
> Another beneﬁt of prior predictive simulations is that they can be used to elicit expert prior

### 日本語訳（自動翻訳）

> ガウス過程モデル (Rasmussen and Willams、2006)。この種のシミュレーションとグラフィック
> 比較は、どのモデルでも作業する場合に役立ち、不慣れなモデルやモデルをセットアップする場合には不可欠です。
> 複雑なモデル。
> 事前予測シミュレーションのもう 1 つの利点は、専門家の事前予測シミュレーションを利用できることです。

### 熟語・専門語

- **prior predictive**: 事前予測。データを見る前のpriorだけで生成される予測分布を確認する診断。
- **ESS**: 有効サンプルサイズ。自己相関を考慮した独立サンプル相当数。

### 要約

- ガウス過程モデル (Rasmussen and Willams、2006)。

## Chunk 0117

### English（抽出4行）

> knowledge on the measurable quantities of interest, which is often easier than soliciting expert
> opinion on model parameters that are not observable (O’Hagan et al., 2006).
> Finally, even when we skip computational prior predictive checking, it might be useful to think
> about how the priors we have chosen would aﬀect a hypothetical simulated dataset.

### 日本語訳（自動翻訳）

> 関心のある測定可能な量に関する知識。多くの場合、専門家に頼むよりも簡単です。
> 観察できないモデルパラメータに関する意見 (O’Hagan et al., 2006)。
> 最後に、計算による事前予測チェックを省略する場合でも、次のように考えると役立つかもしれません。
> 私たちが選択した事前分布が、仮説的にシミュレートされたデータセットにどのような影響を与えるかについて。

### 熟語・専門語

- **prior predictive**: 事前予測。データを見る前のpriorだけで生成される予測分布を確認する診断。

### 要約

- 関心のある測定可能な量に関する知識。

## Chunk 0118

### English（抽出4行）

> 2.5.
> Generative and partially generative models
> Fully Bayesian data analysis requires a generative model—that is, a joint probability distribution
> for all the data and parameters. The point is subtle: Bayesian inference does not actually require

### 日本語訳（自動翻訳）

> 2.5.
> 生成モデルおよび部分生成モデル
> 完全なベイジアン データ分析には生成モデル、つまり同時確率分布が必要です。
> すべてのデータとパラメータに対して。ポイントは微妙です: ベイズ推論は実際には必要ありません

### 熟語・専門語

- **Bayesian inference**: ベイズ推論。事前分布と尤度から事後分布を計算する中核処理。
- **generative model**: 生成モデル。データ生成過程を確率的に記述するモデル。

### 要約

- 2.5. 生成モデルおよび部分生成モデル 完全なベイジアン データ分析には生成モデル、つまり同時確率分布が必要です。

## Chunk 0119

### English（抽出4行）

> the generative model; all it needs from the data is the likelihood, and diﬀerent generative models
> can have the same likelihood. But Bayesian data analysis requires the generative model to be able
> to perform predictive simulation and model checking (Sections 2.4, 4.1, 4.2, 6.1, and 6.2), and
> Bayesian workﬂow will consider a series of generative models.

### 日本語訳（自動翻訳）

> 生成モデル。データから必要なのは可能性とさまざまな生成モデルだけです
> 同じ可能性があるかもしれません。しかし、ベイジアン データ分析では、生成モデルが次のことを実行できる必要があります。
> 予測シミュレーションとモデルのチェックを実行する (セクション 2.4、4.1、4.2、6.1、および 6.2)、および
> ベイジアン ワークフローでは、一連の生成モデルが考慮されます。

### 熟語・専門語

- **model checking**: モデルチェック。モデルの仮定・予測・計算結果がデータや目的に合うか検査すること。
- **likelihood**: 尤度。パラメータが与えられたときデータがどれだけ起こりやすいか。
- **generative model**: 生成モデル。データ生成過程を確率的に記述するモデル。

### 要約

- 生成モデル。

## Chunk 0120

### English（抽出4行）

> For a simple example, suppose we have data y ∼binomial(n, θ), where n and y are observed
> and we wish to make inference about θ. For the purpose of Bayesian inference it is irrelevant
> if the data were sampled with ﬁxed n (binomial sampling) or sampled until a speciﬁed number
> of successes occurred (negative binomial sampling): the two likelihoods are equivalent for the

### 日本語訳（自動翻訳）

> 簡単な例として、n と y が観測されるデータ y 〜binomial(n, θ) があるとします。
> そして θ について推論したいと考えています。ベイズ推論の目的では、それは無関係です
> データが固定 n (二項サンプリング) でサンプリングされたか、指定された数までサンプリングされた場合
> 発生した成功の割合 (負の二項サンプリング): 2 つの可能性は、

### 熟語・専門語

- **Bayesian inference**: ベイズ推論。事前分布と尤度から事後分布を計算する中核処理。
- **likelihood**: 尤度。パラメータが与えられたときデータがどれだけ起こりやすいか。
- **ESS**: 有効サンプルサイズ。自己相関を考慮した独立サンプル相当数。

### 要約

- 簡単な例として、n と y が観測されるデータ y 〜binomial(n, θ) があるとします。

## Chunk 0121

### English（抽出4行）

> purpose of estimating θ because they diﬀer only by a multiplicative factor that depends on y and
> n but not θ. However, if we want to simulate new data from the predictive model, the two models
> are diﬀerent, as the binomial model yields replications with a ﬁxed value of n and the negative
> binomial model yields replications with a ﬁxed value of y. Prior and posterior predictive checks

### 日本語訳（自動翻訳）

> θ を推定する目的は、それらは y と に依存する乗算係数によってのみ異なるためです。
> n ですが θ ではありません。ただし、予測モデルからの新しいデータをシミュレートする場合は、2 つのモデル
> 二項モデルは固定値 n と負の値で複製を生成するため、異なります。
> 二項モデルは、y の固定値で複製を生成します。事前および事後の予測チェック

### 熟語・専門語

- **posterior predictive**: 事後予測。推定後のモデルが観測データの特徴を再現できるかを見る診断。

### 要約

- θ を推定する目的は、それらは y と に依存する乗算係数によってのみ異なるためです。

## Chunk 0122

### English（抽出4行）

> (Sections 2.4 and 6.1) will look diﬀerent under these two diﬀerent generative models.
> This is not to say that the Bayesian approach is necessarily better; the assumptions of a generative
> model can increase inferential eﬃciency but can also go wrong, and this motivates much of our
> workﬂow.

### 日本語訳（自動翻訳）

> (セクション 2.4 と 6.1) は、これら 2 つの異なる生成モデルの下では異なって見えます。
> これは、ベイジアンアプローチが必ずしも優れているということではありません。生成の仮定
> モデルは推論効率を向上させることはできますが、間違った方向に進む可能性もあり、これが私たちの多くのモチベーションを高めます。
> ワークフロー。

### 熟語・専門語

- **generative model**: 生成モデル。データ生成過程を確率的に記述するモデル。
- **ESS**: 有効サンプルサイズ。自己相関を考慮した独立サンプル相当数。

### 要約

- (セクション 2.4 と 6.1) は、これら 2 つの異なる生成モデルの下では異なって見えます。

## Chunk 0123

### English（抽出4行）

> It is common in Bayesian analysis to use models that are not fully generative. For example, in
> regression we will typically model an outcome y given predictors x without a generative model
> for x. Another example is survival data with censoring, where the censoring process is not usually
> modeled. When performing predictive checks for such models, we either need to condition on the

### 日本語訳（自動翻訳）

> ベイジアン分析では、完全に生成的ではないモデルを使用するのが一般的です。たとえば、
> 回帰では、通常、生成モデルを使用せずに、予測子 x が与えられた結果 y をモデル化します。
> xの場合。別の例は、打ち切りを伴う生存データです。打ち切りプロセスは通常は行われません。
> モデル化された。このようなモデルの予測チェックを実行するときは、次のいずれかの条件を付ける必要があります。

### 熟語・専門語

- **generative model**: 生成モデル。データ生成過程を確率的に記述するモデル。
- **ESS**: 有効サンプルサイズ。自己相関を考慮した独立サンプル相当数。

### 要約

- ベイジアン分析では、完全に生成的ではないモデルを使用するのが一般的です。

## Chunk 0124

### English（抽出4行）

> observed predictors or else extend the model to allow new values of the predictors to be sampled.
> It is also possible that there is no stochastic generative process for some parts of the model, for
> example if x has been chosen by a deterministic design of experiment.
> Thinking in terms of generative models can help illuminate the limitations of what can be

### 日本語訳（自動翻訳）

> 観察された予測子を使用するか、モデルを拡張して予測子の新しい値をサンプリングできるようにします。
> モデルの一部には確率的生成プロセスが存在しない可能性もあります。
> たとえば、x が決定論的な実験計画によって選択された場合です。
> 生成モデルの観点から考えると、実現できるものの限界を明らかにすることができます。

### 熟語・専門語

- **generative model**: 生成モデル。データ生成過程を確率的に記述するモデル。
- **ESS**: 有効サンプルサイズ。自己相関を考慮した独立サンプル相当数。

### 要約

- 観察された予測子を使用するか、モデルを拡張して予測子の新しい値をサンプリングできるようにします。

## Chunk 0125

### English（抽出4行）

> learned from the observations. For example, we might want to model a temporal process with a
> complicated autocorrelation structure, but if our actual data are spaced far apart in time, we might
> not be able to distinguish this model from a simpler process with nearly independent errors.
> In addition, Bayesian models that use improper priors are not fully generative, in the sense that

### 日本語訳（自動翻訳）

> 観察から学びました。たとえば、時間的プロセスをモデル化したい場合があります。
> 複雑な自己相関構造ですが、実際のデータが時間的に遠く離れている場合、
> このモデルを、ほぼ独立したエラーを伴う単純なプロセスと区別することはできません。
> さらに、不適切な事前分布を使用するベイジアン モデルは、次のような意味で完全に生成的ではありません。

### 熟語・専門語

- **ESS**: 有効サンプルサイズ。自己相関を考慮した独立サンプル相当数。

### 要約

- 観察から学びました。

## Chunk 0126

### English（抽出4行）

> they do not have a joint distribution for data and parameters and it would not be possible to sample
> from the prior predictive distribution. When we do use improper priors, we think of them as being
> placeholders or steps along the road to a full Bayesian model with a proper joint distribution over
> parameters and data.

### 日本語訳（自動翻訳）

> データとパラメータの同時分布がないため、サンプリングすることはできません。
> 事前の予測分布から。不適切な事前分布を使用する場合、私たちはそれらが次のようなものであると考えます。
> 適切な結合分布を備えた完全なベイジアン モデルへの道に沿ったプレースホルダーまたはステップ
> パラメータとデータ。

### 熟語・専門語

- **prior predictive**: 事前予測。データを見る前のpriorだけで生成される予測分布を確認する診断。

### 要約

- データとパラメータの同時分布がないため、サンプリングすることはできません。

## Chunk 0127

### English（抽出4行）

> In applied work, complexity often arises from incorporating diﬀerent sources of data. For
> example, we ﬁt a Bayesian model for the 2020 presidential election using state and national
> polls, partially pooling toward a forecast based on political and economic “fundamentals” (Morris,
> Gelman, and Heidemanns, 2020). The model includes a stochastic process for latent time trends

### 日本語訳（自動翻訳）

> 応用作業では、さまざまなデータ ソースを組み込むことで複雑さが生じることがよくあります。のために
> たとえば、州と国を使用して 2020 年の大統領選挙にベイジアン モデルを当てはめます。
> 世論調査は、政治的および経済的な「ファンダメンタルズ」に基づいた予測に部分的に一致している（モリス、
> ゲルマン、ハイデマンス、2020)。モデルには、潜在時間の傾向に対する確率的プロセスが含まれています

### 熟語・専門語

- **ESS**: 有効サンプルサイズ。自己相関を考慮した独立サンプル相当数。

### 要約

- 応用作業では、さまざまなデータ ソースを組み込むことで複雑さが生じることがよくあります。

## Chunk 0128

### English（抽出4行）

> in state and national opinion. Fitting the model using Stan yields posterior simulations which
> are used to compute probabilities for election outcomes. The Bayesian model-based approach is
> superﬁcially similar to poll aggregations such as described by Katz (2016), which also summarize
> uncertainty by random simulations. The diﬀerence is that our model could be run forward to

### 日本語訳（自動翻訳）

> 州および国民の世論において。 Stan を使用してモデルをフィッティングすると、事後シミュレーションが得られます。
> 選挙結果の確率を計算するために使用されます。ベイズモデルベースのアプローチは次のとおりです。
> Katz (2016) によって説明されているような世論調査の集計と表面的には似ていますが、これも要約されています。
> ランダムなシミュレーションによる不確実性。違いは、私たちのモデルは次のように実行できることです。

### 熟語・専門語

- **uncertainty**: 不確実性。観測・パラメータ・モデル構造・意思決定に残る曖昧さ。

### 要約

- 州および国民の世論において。

## Chunk 0129

### English（抽出4行）

> generate polling data; it is not just a data analysis procedure but also provides a probabilistic model
> for public opinion at the national and state levels.
> Thinking more generally, we can consider a progression from least to most generative models.
> At one extreme are completely non-generative methods which are deﬁned simply as data summaries,

### 日本語訳（自動翻訳）

> ポーリングデータを生成します。これは単なるデータ分析手順ではなく、確率モデルも提供します。
> 国および州レベルの世論のために。
> より一般的に考えると、最小生成モデルから最大生成モデルへの進行を考えることができます。
> 極端な例としては、単にデータの要約として定義される完全に非生成的な方法があります。

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

> データのモデルがまったくありません。次に登場するのは、確率によって特徴付けられる古典的な統計モデルです。
> パラメータ θ が与えられたデータ y の分布 p(y; θ) ですが、θ の確率分布はありません。で
> 次のステップは、通常フィッティングするベイジアン モデルです。これは y と θ で生成的ですが、次のものが含まれます。
> 追加のモデル化されていないデータ x (サンプル サイズ、設計設定、ハイパーパラメーターなど)。私たちは書きます

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- データのモデルがまったくありません。

## Chunk 0131

### English（抽出4行）

> such models as p(y, θ|x). The ﬁnal step would be a completely generative model p(y, θ, x) with no
> “left out” data, x.
> In statistical workﬂow we can move up and down this ladder, for example starting with an
> unmodeled data-reduction algorithm and then formulating it as a probability model, or starting

### 日本語訳（自動翻訳）

> p(y, θ|x) などのモデル。最後のステップは、何も含まない完全な生成モデル p(y, θ, x) です。
> 「取り残された」データ、x。
> 統計ワークフローでは、このはしごを上下に移動できます。たとえば、
> モデル化されていないデータ削減アルゴリズムを使用し、それを確率モデルとして定式化するか、開始します。

### 熟語・専門語

- **generative model**: 生成モデル。データ生成過程を確率的に記述するモデル。

### 要約

- p(y, θ|x) などのモデル。

## Chunk 0132

### English（抽出4行）

> with the inference from a probability model, considering it as a data-based estimate, and tweaking
> it in some way to improve performance. In Bayesian workﬂow we can move data in and out of the
> model, for example taking an unmodeled predictor x and allowing it to have measurement error,
> so that the model then includes a new level of latent data (Clayton, 1992, Richardson and Gilks,

### 日本語訳（自動翻訳）

> 確率モデルからの推論を使用し、それをデータベースの推定値として考慮し、微調整します。
> 何らかの方法でパフォーマンスを向上させるためです。ベイジアン ワークフローでは、データを
> モデル、たとえばモデル化されていない予測子 x を使用し、それに測定誤差があることを許可します。
> そのため、モデルには新しいレベルの潜在データが含まれます (Clayton、1992、Richardson と Gilks、

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- 確率モデルからの推論を使用し、それをデータベースの推定値として考慮し、微調整します。

## Chunk 0133

### English（抽出4行）

> 1993).
> 3.
> Fitting a model
> Traditionally, Bayesian computation has been performed using a combination of analytic calculation

### 日本語訳（自動翻訳）

> 1993年）。
> 3.
> モデルのフィッティング
> 従来、ベイズ計算は解析計算を組み合わせて実行されてきました。

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- 1993年）。

## Chunk 0134

### English（抽出4行）

> and normal approximation. Then in the 1990s, it became possible to perform Bayesian inference
> for a wide range of models using Gibbs and Metropolis algorithms (Robert and Casella, 2011).
> The current state of the art algorithms for ﬁtting open-ended Bayesian models include variational
> inference (Blei and Kucukelbir, 2017), sequential Monte Carlo (Smith, 2013), and Hamiltonian

### 日本語訳（自動翻訳）

> そして正規近似。そして 1990 年代にはベイズ推論が可能になりました。
> Gibbs および Metropolis アルゴリズムを使用した幅広いモデル用 (Robert および Casella、2011)。
> オープンエンド ベイジアン モデルを近似するための現在の最先端のアルゴリズムには、変分アルゴリズムが含まれます。
> 推論 (Blei および Kucukelbir、2017)、逐次モンテカルロ (Smith、2013)、およびハミルトニアン

### 熟語・専門語

- **Bayesian inference**: ベイズ推論。事前分布と尤度から事後分布を計算する中核処理。

### 要約

- そして正規近似。

## Chunk 0135

### English（抽出4行）

> Monte Carlo (HMC; Neal, 2011, Betancourt, 2017a). Variational inference is a generalization of
> the expectation-maximization (EM) algorithm and can, in the Bayesian context, be considered as
> providing a fast but possibly inaccurate approximation to the posterior distribution. Variational
> inference is the current standard for computationally intensive models such as deep neural networks.

### 日本語訳（自動翻訳）

> モンテカルロ (HMC; Neal、2011、Betancourt、2017a)。変分推論は次の一般化です。
> 期待値最大化 (EM) アルゴリズムであり、ベイジアンの文脈では次のように考えることができます。
> 事後分布の近似は高速ですが不正確になる可能性があります。変分
> 推論は、ディープ ニューラル ネットワークなどの計算集約型モデルの現在の標準です。

### 熟語・専門語

- **posterior distribution**: 事後分布。データ観測後の未知量の不確実性を表す分布。

### 要約

- モンテカルロ (HMC; Neal、2011、Betancourt、2017a)。

## Chunk 0136

### English（抽出4行）

> Sequential Monte Carlo is a generalization of the Metropolis algorithm that can be applied to any
> Bayesian computation, and HMC is a diﬀerent generalization of Metropolis that uses gradient
> computation to move eﬃciently through continuous probability spaces.
> In the present article we focus on ﬁtting Bayesian models using HMC and its variants, as

### 日本語訳（自動翻訳）

> 逐次モンテカルロは、メトロポリス アルゴリズムを一般化したもので、あらゆるものに適用できます。
> ベイジアン計算、HMC は勾配を使用する Metropolis の別の一般化です
> 連続確率空間を効率的に移動するための計算。
> この記事では、次のように、HMC とそのバリアントを使用したベイジアン モデルのフィッティングに焦点を当てます。

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- 逐次モンテカルロは、メトロポリス アルゴリズムを一般化したもので、あらゆるものに適用できます。

## Chunk 0137

### English（抽出4行）

> implemented in Stan and other probabilistic programming languages. While similar principles
> should apply also to other software and other algorithms, there will be diﬀerences in the details.
> To safely use an inference algorithm in Bayesian workﬂow, it is vital that the algorithm provides
> strong diagnostics to determine when the computation is unreliable. In the present paper we discuss

### 日本語訳（自動翻訳）

> Stan およびその他の確率的プログラミング言語で実装されています。同様の原理ですが、
> 他のソフトウェアや他のアルゴリズムにも適用する必要がありますが、詳細には違いがあります。
> ベイジアン ワークフローで推論アルゴリズムを安全に使用するには、アルゴリズムが提供することが重要です。
> 計算の信頼性がいつ低いかを判断するための強力な診断機能。この論文では、

### 熟語・専門語

- **probabilistic programming**: 確率的プログラミング。Stanなどで確率モデルをコードとして記述し推論する方法。

### 要約

- Stan およびその他の確率的プログラミング言語で実装されています。

## Chunk 0138

### English（抽出4行）

> such diagnostics for HMC.
> 3.1.
> Initial values, adaptation, and warmup
> Except in the simplest case, Markov chain simulation algorithms operate in multiple stages. First

### 日本語訳（自動翻訳）

> HMC の診断など。
> 3.1.
> 初期値、適応、ウォームアップ
> 最も単純な場合を除いて、マルコフ連鎖シミュレーション アルゴリズムは複数の段階で動作します。まず

### 熟語・専門語

- **Markov chain**: マルコフ連鎖。MCMCで事後分布からサンプルを得るための確率過程。

### 要約

- HMC の診断など。

## Chunk 0139

### English（抽出4行）

> there is a warmup phase which is intended to move the simulations from their possibly unrepresen-
> tative initial values to something closer to the region of parameter space where the log posterior
> density is close to its expected value, which is related to the concept of “typical set” in information
> theory (Carpenter, 2017). Initial values are not supposed to matter in the asymptotic limit, but they

### 日本語訳（自動翻訳）

> シミュレーションを表現されていない状態から移行することを目的としたウォームアップ フェーズがあります。
> 推定の初期値は、事後対数が得られるパラメータ空間の領域に近い値に設定されます。
> 密度は期待値に近く、これは情報の「典型的なセット」の概念に関連しています
> 理論（カーペンター、2017）。漸近限界では初期値は重要ではないと考えられていますが、

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- シミュレーションを表現されていない状態から移行することを目的としたウォームアップ フェーズがあります。

## Chunk 0140

### English（抽出4行）

> can matter in practice, and a wrong choice can threaten the validity of the results.
> Also during warmup there needs to be some procedure to set the algorithm’s tuning parameters;
> this can be done using information gathered from the warmup runs. Third is the sampling phase,
> which ideally is run until multiple chains have mixed (Vehtari et al., 2020).

### 日本語訳（自動翻訳）

> 実際には重要になる可能性があり、間違った選択は結果の妥当性を脅かす可能性があります。
> また、ウォームアップ中に、アルゴリズムの調整パラメーターを設定するための何らかの手順が必要です。
> これは、ウォームアップ実行から収集された情報を使用して行うことができます。 3 番目はサンプリングフェーズです。
> 理想的には、複数のチェーンが混合するまで実行されます (Vehtari et al., 2020)。

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- 実際には重要になる可能性があり、間違った選択は結果の妥当性を脅かす可能性があります。

## Chunk 0141

### English（抽出4行）

> When ﬁtting a model that has been correctly speciﬁed, warmup thus has two purposes: (a) to
> run through a transient phase to reduce the bias due to dependence on the initial values, and (b)
> to provide information about the target distribution to use in setting tuning parameters. In model
> exploration, warmup has a third role, which is to quickly ﬂag computationally problematic models.

### 日本語訳（自動翻訳）

> したがって、正しく指定されたモデルをフィッティングする場合、ウォームアップには次の 2 つの目的があります。(a)
> 初期値への依存によるバイアスを低減するために過渡フェーズを実行する、および (b)
> チューニングパラメータの設定に使用するターゲットディストリビューションに関する情報を提供します。モデル内
> 探索、ウォームアップには 3 番目の役割があり、計算上問題のあるモデルに迅速にフラグを立てることです。

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- したがって、正しく指定されたモデルをフィッティングする場合、ウォームアップには次の 2 つの目的があります。

## Chunk 0142

### English（抽出4行）

> 3.2.
> How long to run an iterative algorithm
> We similarly would like to consider decisions in the operation of iterative algorithms in the context
> of the larger workﬂow. Recommended standard practice is to run at least until bR, the measure

### 日本語訳（自動翻訳）

> 3.2.
> 反復アルゴリズムの実行時間
> 同様に、コンテキスト内の反復アルゴリズムの操作における決定を検討したいと考えています。
> より大きなワークフローの一部。推奨される標準的な方法は、少なくとも bR (メジャー) まで実行することです。

### 熟語・専門語

- **decision**: 意思決定。予測分布を損失・効用・行動選択へ接続する工程。

### 要約

- 3.2. 反復アルゴリズムの実行時間 同様に、コンテキスト内の反復アルゴリズムの操作における決定を検討したいと考えています。

## Chunk 0143

### English（抽出4行）

> of mixing of chains, is less than 1.01 for all parameters and quantities of interest (Vehtari et al.,
> 2020), and to also monitor the multivariate mixing statistic R∗(Lambert and Vehtari, 2020). There
> are times when earlier stopping can make sense in the early stages of modeling. For example, it
> might seem like a safe and conservative choice to run MCMC until the eﬀective sample size is

### 日本語訳（自動翻訳）

> チェーンの混合の割合は、対象となるすべてのパラメーターと量について 1.01 未満です (Vehtari et al.、
> 2020)、多変量混合統計 R∗ (Lambert and Vehtari、2020) も監視します。そこに
> モデリングの初期段階では、早期に停止することが意味がある場合があります。たとえば、それは
> 有効サンプルサイズが一定になるまで MCMC を実行するのは、安全で保守的な選択のように思えるかもしれません。

### 熟語・専門語

- **ESS**: 有効サンプルサイズ。自己相関を考慮した独立サンプル相当数。

### 要約

- チェーンの混合の割合は、対象となるすべてのパラメーターと量について 1.01 未満です (Vehtari et al.、 2020)、多変量混合統計 R∗ (Lambert and Vehtari、2020) も監視します。

## Chunk 0144

### English（抽出4行）

> in the thousands or Monte Carlo standard error is tiny in comparison to the required precision for
> parameter interpretation—but if this takes a long time, it limits the number of models that can be
> ﬁt in the exploration stage. More often than not, our model also has some big issues (especially
> coding errors) that become apparent after running only a few iterations, so that the remaining

### 日本語訳（自動翻訳）

> 数千単位またはモンテカルロ標準誤差は、必要な精度に比べて小さいです。
> パラメーターの解釈 - ただし、これに時間がかかると、解釈できるモデルの数が制限されます。
> 探索段階にぴったりです。多くの場合、私たちのモデルにはいくつかの大きな問題もあります (特に
> コーディングエラー）は、数回の反復を実行しただけで明らかになるため、残りの

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- 数千単位またはモンテカルロ標準誤差は、必要な精度に比べて小さいです。

## Chunk 0145

### English（抽出4行）

> Computation time
> Distance from
> target distribution
> MCMC

### 日本語訳（自動翻訳）

> 計算時間
> からの距離
> ターゲット分布
> MCMC

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- 計算時間 からの距離 ターゲット分布 MCMC

## Chunk 0146

### English（抽出4行）

> algorithm
> Approximate algorithm
> Figure 5: Idealized sketch of the tradeoﬀbetween approximate algorithms and MCMC in Bayesian
> computation. If the goal is to get the best ﬁt to the target distribution, MCMC should ultimately

### 日本語訳（自動翻訳）

> アルゴリズム
> 近似アルゴリズム
> 図 5: ベイジアンにおける近似アルゴリズムと MCMC の間のトレードオフの理想的なスケッチ
> 計算。目標がターゲットの分布に最適に適合することである場合、MCMC は最終的に次のことを行う必要があります。

### 熟語・専門語

- **approximate**: 近似。速度や扱いやすさのため、正確な推論・モデルを緩めること。

### 要約

- アルゴリズム 近似アルゴリズム 図 5: ベイジアンにおける近似アルゴリズムと MCMC の間のトレードオフの理想的なスケッチ 計算。

## Chunk 0147

### English（抽出4行）

> win out. But if we are currently ﬁtting just one in a series of models, it can make sense to use
> approximate algorithms so as to be able to move through model space more rapidly. Which of
> these algorithms performs better depends on the time budget of the user and where the two curves
> intersect.

### 日本語訳（自動翻訳）

> 勝ち抜く。しかし、現在一連のモデルの 1 つだけを当てはめている場合は、次のようにするのが合理的です。
> 近似アルゴリズムを使用して、モデル空間をより迅速に移動できるようにします。どれ
> これらのアルゴリズムのパフォーマンスが向上するかどうかは、ユーザーの時間予算と 2 つの曲線がどこで交差するかによって異なります。
> 交差する。

### 熟語・専門語

- **approximate**: 近似。速度や扱いやすさのため、正確な推論・モデルを緩めること。

### 要約

- 勝ち抜く。

## Chunk 0148

### English（抽出4行）

> computation is wasted. In this respect, running many iterations for a newly-written model is similar
> to premature optimization in software engineering. For the ﬁnal model, the required number of
> iterations depends on the desired Monte Carlo accuracy for the quantities of interest.
> Another choice in computation is how to best make use of available parallelism, beyond the

### 日本語訳（自動翻訳）

> 計算が無駄になります。この点では、新しく作成されたモデルに対して多くの反復を実行することは似ています。
> ソフトウェアエンジニアリングにおける時期尚早の最適化につながります。最終モデルの必要数は、
> 反復回数は、対象量に対して必要なモンテカルロ精度によって異なります。
> 計算におけるもう 1 つの選択肢は、利用可能な並列処理を最大限に活用する方法です。

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- 計算が無駄になります。

## Chunk 0149

### English（抽出4行）

> default of running 4 or 8 separate chains on multiple cores. Instead of increasing the number of
> iterations, eﬀective variance reduction can also be obtained by increasing the number of parallel
> chains (see, e.g., Hoﬀman and Ma, 2020).
> 3.3.

### 日本語訳（自動翻訳）

> デフォルトでは、複数のコアで 4 つまたは 8 つの個別のチェーンが実行されます。数を増やすのではなく、
> 反復回数を増やすと、並列数を増やすことによって効果的な分散を削減することもできます。
> チェーン（例：Hoﬀman and Ma、2020 を参照）。
> 3.3.

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- デフォルトでは、複数のコアで 4 つまたは 8 つの個別のチェーンが実行されます。

## Chunk 0150

### English（抽出4行）

> Approximate algorithms and approximate models
> Bayesian inference typically involves intractable integrals, hence the need for approximations.
> Markov chain simulation is a form of approximation where the theoretical error approaches zero
> as the number of simulations increases. If our chains have mixed, we can make a good estimate

### 日本語訳（自動翻訳）

> 近似アルゴリズムと近似モデル
> ベイズ推論には通常、扱いにくい積分が含まれるため、近似が必要になります。
> マルコフ連鎖シミュレーションは、理論上の誤差がゼロに近づく近似形式です。
> シミュレーションの数が増えるにつれて。チェーンが混在している場合でも、適切な推定を行うことができます

### 熟語・専門語

- **Bayesian inference**: ベイズ推論。事前分布と尤度から事後分布を計算する中核処理。
- **Markov chain**: マルコフ連鎖。MCMCで事後分布からサンプルを得るための確率過程。
- **approximate**: 近似。速度や扱いやすさのため、正確な推論・モデルを緩めること。

### 要約

- 近似アルゴリズムと近似モデル ベイズ推論には通常、扱いにくい積分が含まれるため、近似が必要になります。

## Chunk 0151

### English（抽出4行）

> of the Monte Carlo standard error (Vehtari et al., 2020), and for practical purposes we often treat
> these computations as exact.
> Unfortunately, running MCMC to convergence is not always a scalable solution as data and
> models get large, hence the desire for faster approximations. Figure 5 shows the resulting tradeoﬀ

### 日本語訳（自動翻訳）

> モンテカルロの標準誤差 (Vehtari et al., 2020) であり、実用的な目的でよく扱われます。
> これらの計算は正確です。
> 残念ながら、MCMC を実行して収束させることは、データとデータの点で常にスケーラブルなソリューションであるとは限りません。
> モデルが大きくなるため、より高速な近似が求められます。図 5 は、結果として生じるトレードオフを示しています

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- モンテカルロの標準誤差 (Vehtari et al., 2020) であり、実用的な目的でよく扱われます。

## Chunk 0152

### English（抽出4行）

> between speed and accuracy. This graph is only conceptual; in a real problem, the positions of
> these lines would be unknown, and indeed in some problems an approximate algorithm can perform
> worse than MCMC even at short time scales.
> Depending on where we are in the workﬂow, we have diﬀerent requirements of our computed

### 日本語訳（自動翻訳）

> スピードと正確さの間で。このグラフは概念的なものにすぎません。実際の問題では、
> これらの線は未知であり、実際、一部の問題では近似アルゴリズムで実行できます。
> 短い時間スケールでも MCMC よりも悪い。
> ワークフローのどの位置にいるかに応じて、計算されたデータの要件は異なります。

### 熟語・専門語

- **approximate**: 近似。速度や扱いやすさのため、正確な推論・モデルを緩めること。

### 要約

- スピードと正確さの間で。

## Chunk 0153

### English（抽出4行）

> posteriors. Near the end of the workﬂow, where we are examining ﬁne-scale and delicate features,
> we require accurate exploration of the posterior distribution. This usually requires MCMC. On the
> other hand, at the beginning of the workﬂow, we can frequently make our modeling decisions based
> on large-scale features of the posterior that can be accurately estimated using relatively simple

### 日本語訳（自動翻訳）

> 後部。ワークフローの終わり近くで、細かいスケールの繊細な特徴を調べます。
> 事後分布を正確に調査する必要があります。通常、これには MCMC が必要です。で
> 一方、ワークフローの開始時には、多くの場合、以下に基づいてモデリングの決定を下すことができます。
> 比較的単純な方法を使用して正確に推定できる事後部の大規模な特徴について

### 熟語・専門語

- **posterior distribution**: 事後分布。データ観測後の未知量の不確実性を表す分布。
- **decision**: 意思決定。予測分布を損失・効用・行動選択へ接続する工程。

### 要約

- 後部。

## Chunk 0154

### English（抽出4行）

> methods such as empirical Bayes, linearization or Laplace approximation, nested approximations
> like INLA (Rue et al., 2009), or even sometimes data-splitting methods like expectation propagation
> (Vehtari, Gelman, Siivola, et al., 2020), mode-ﬁnding approximations like variational inference
> (Kucukelbir et al., 2017), or penalized maximum likelihood. The point is to use a suitable tool for

### 日本語訳（自動翻訳）

> 経験的ベイズ、線形化またはラプラス近似、入れ子近似などの手法
> INLA (Rue et al., 2009) のような、または場合によっては期待伝播のようなデータ分割手法も使用されます。
> (Vehtari、Gelman、Siivola、他、2020)、変分推論のようなモード探索近似
> (Kucukelbir et al., 2017)、またはペナルティ付き最尤法。ポイントは適切なツールを使用することです

### 熟語・専門語

- **likelihood**: 尤度。パラメータが与えられたときデータがどれだけ起こりやすいか。

### 要約

- 経験的ベイズ、線形化またはラプラス近似、入れ子近似などの手法 INLA (Rue et al., 2009) のような、または場合によっては期待伝播のようなデータ分割手法も使用されます。

## Chunk 0155

### English（抽出4行）

> the job and to not try to knock down a retaining wall using a sculptor’s chisel.
> All of these approximate methods have at least a decade of practical experience, theory, and
> diagnostics behind them. There is no one-size-ﬁts-all approximate inference algorithm, but when
> a workﬂow includes relatively well-understood components such as generalized linear models,

### 日本語訳（自動翻訳）

> 彫刻家のノミを使って擁壁を破壊しようとしないでください。
> これらの近似手法はすべて、少なくとも 10 年にわたる実践的な経験、理論、
> その背後にある診断。万能の近似推論アルゴリズムはありませんが、
> ワークフローには、一般化された線形モデルなどの比較的よく理解されているコンポーネントが含まれています。

### 熟語・専門語

- **approximate**: 近似。速度や扱いやすさのため、正確な推論・モデルを緩めること。

### 要約

- 彫刻家のノミを使って擁壁を破壊しようとしないでください。

## Chunk 0156

### English（抽出4行）

> multilevel regression, autoregressive time series models, or Gaussian processes, it is often possi-
> ble to construct an appropriate approximate algorithm. Furthermore, depending on the speciﬁc
> approximation being used, generic diagnostic tools described by Yao et al. (2018a) and Talts et al.
> (2020) can be used to verify that a particular approximate algorithm reproduces the features of the

### 日本語訳（自動翻訳）

> 多段階回帰、自己回帰時系列モデル、またはガウス過程では、多くの場合、可能です。
> 適切な近似アルゴリズムを構築できます。さらに、具体的な内容によっては、
> 近似が使用されており、Yao et al. によって説明された一般的な診断ツールが使用されます。 (2018a) およびタルツら。
> (2020) を使用して、特定の近似アルゴリズムがその特徴を再現することを検証できます。

### 熟語・専門語

- **ESS**: 有効サンプルサイズ。自己相関を考慮した独立サンプル相当数。
- **approximate**: 近似。速度や扱いやすさのため、正確な推論・モデルを緩めること。

### 要約

- 多段階回帰、自己回帰時系列モデル、またはガウス過程では、多くの場合、可能です。

## Chunk 0157

### English（抽出4行）

> posterior that you care about for a speciﬁc model.
> An alternative view is to understand an approximate algorithm as an exact algorithm for an
> approximate model. In this sense, a workﬂow is a sequence of steps in an abstract computational
> scheme aiming to infer some ultimate, unstated model. More usefully, we can think of things

### 日本語訳（自動翻訳）

> 特定のモデルで気になる後部。
> 別の見方としては、近似アルゴリズムを正確なアルゴリズムとして理解することです。
> 近似モデル。この意味で、ワークフローは抽象的な計算処理における一連のステップです。
> 何らかの究極的な、明言されていないモデルを推測することを目的としたスキーム。さらに便利なことに、物事を考えることができます

### 熟語・専門語

- **approximate**: 近似。速度や扱いやすさのため、正確な推論・モデルを緩めること。

### 要約

- 特定のモデルで気になる後部。

## Chunk 0158

### English（抽出4行）

> like empirical Bayes approximations as replacing a model’s prior distributions with a particular
> data-dependent point-mass prior. Similarly a Laplace approximation can be viewed as a data-
> dependent linearization of the desired model, while a nested Laplace approximation (Rue et al.,
> 2009, Margossian et al., 2020a) uses a linearized conditional posterior in place of the posited

### 日本語訳（自動翻訳）

> モデルの以前の分布を特定の分布に置き換える経験的なベイズ近似のようなもの
> データ依存の事前点質量。同様に、ラプラス近似はデータとして見ることができます。
> ネストされたラプラス近似 (Rue et al.,
> 2009、Margossian et al.、2020a) は、仮定されたものの代わりに線形化された条件付き事後分布を使用します。

### 熟語・専門語

- **prior distribution**: 事前分布。データ観測前の知識・制約を表す分布。

### 要約

- モデルの以前の分布を特定の分布に置き換える経験的なベイズ近似のようなもの データ依存の事前点質量。

## Chunk 0159

### English（抽出4行）

> conditional posterior.
> 3.4.
> Fit fast, fail fast
> An important intermediate goal is to be able to fail fast when ﬁtting bad models. This can be

### 日本語訳（自動翻訳）

> 条件付き後部。
> 3.4.
> 素早く適合し、素早く失敗する
> 重要な中間目標は、不適切なモデルを適合させるときに迅速に失敗できるようにすることです。これは可能です

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- 条件付き後部。

## Chunk 0160

### English（抽出4行）

> considered as a shortcut that avoids spending a lot of time for (near) perfect inference for a bad
> model. There is a large literature on approximate algorithms to ﬁt the desired model fast, but little
> on algorithms designed to waste as little time as possible on the models that we will ultimately
> abandon. We believe it is important to evaluate methods on this criterion, especially because

### 日本語訳（自動翻訳）

> 悪い問題に対する（ほぼ）完璧な推論に多くの時間を費やすことを避ける近道と考えられています。
> モデル。目的のモデルを迅速に適合させるための近似アルゴリズムに関する大量の文献がありますが、ほとんどありません。
> 最終的に作成するモデルに費やす時間をできるだけ少なくするように設計されたアルゴリズムに基づいて、
> 放棄する。私たちは、この基準に基づいてメソッドを評価することが重要であると信じています。

### 熟語・専門語

- **approximate**: 近似。速度や扱いやすさのため、正確な推論・モデルを緩めること。

### 要約

- 悪い問題に対する（ほぼ）完璧な推論に多くの時間を費やすことを避ける近道と考えられています。

## Chunk 0161

### English（抽出4行）

> inappropriate and poorly ﬁtting models can often be more diﬃcult to ﬁt.
> For a simple idealized example, suppose you are an astronomer several centuries ago ﬁtting
> ellipses to a planetary orbit based on 10 data points measured with error. Figure 6a shows the sort
> of data that might arise, and just about any algorithm will ﬁt reasonably well. For example, you

### 日本語訳（自動翻訳）

> 不適切で適合度の低いモデルは、多くの場合、適合がより困難になる可能性があります。
> 簡単な理想化された例として、あなたが数世紀前の天文学者であると仮定します。
> 誤差を含めて測定された 10 個のデータ ポイントに基づいて、楕円を惑星軌道に変換します。図 6a はソートを示しています
> 発生する可能性のあるデータを考慮すると、ほぼすべてのアルゴリズムが適切に適合します。たとえば、あなたは

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- 不適切で適合度の低いモデルは、多くの場合、適合がより困難になる可能性があります。

## Chunk 0162

### English（抽出4行）

> could take various sets of ﬁve points and ﬁt the exact ellipse to each, and then take the average of
> these ﬁts. Or you could ﬁt an ellipse to the ﬁrst ﬁve points, then perturb it slightly to ﬁt the sixth
> point, then perturb that slightly to ﬁt the seventh, and so forth. Or you could implement some sort
> of least squares algorithm.

### 日本語訳（自動翻訳）

> さまざまな 5 つの点のセットを取得し、それぞれに正確な楕円を当てはめて、次の平均を取ることができます。
> これらはぴったりです。あるいは、楕円を最初の 5 つの点に当てはめてから、6 番目の点に合わせるために少し摂動させることもできます。
> ポイントを調整し、それをわずかに摂動させて 7 度に合わせる、というようになります。あるいは、ある種の実装を行うこともできます
> 最小二乗アルゴリズムの。

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- さまざまな 5 つの点のセットを取得し、それぞれに正確な楕円を当てはめて、次の平均を取ることができます。

## Chunk 0163

### English（抽出4行）

> Now suppose some Death Star comes along and alters the orbit—in this case, we are purposely
> choosing an unrealistic example to create a gross discrepancy between model and data—so that
> your 10 data points look like Figure 6b. In this case, convergence will be much harder to attain.
> If you start with the ellipse ﬁt to the ﬁrst ﬁve points, it will be diﬃcult to take any set of small

### 日本語訳（自動翻訳）

> ここで、デス・スターがやって来て軌道を変えたと仮定します。この場合、私たちは意図的に
> 非現実的な例を選択して、モデルとデータの間に大きな不一致が生じると、
> 10 個のデータ ポイントは図 6b のようになります。この場合、収束を達成するのは非常に困難になります。
> 最初の 5 つの点に適合する楕円から始めると、小さな集合を取得するのが難しくなります。

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- ここで、デス・スターがやって来て軌道を変えたと仮定します。

## Chunk 0164

### English（抽出4行）

> perturbations that will allow the curve to ﬁt the later points in the series. But, more than that, even
> if you could obtain a least squares solution, any ellipse would be a terrible ﬁt to the data. It’s just
> an inappropriate model. If you ﬁt an ellipse to these data, you should want the ﬁt to fail fast so you
> Figure 6: Illustration of the need for “ﬁt fast, fail fast”: (a) Idealized data representing measure-

### 日本語訳（自動翻訳）

> 曲線を系列の後の点に適合させる摂動。しかし、それ以上に、
> 最小二乗解を得ることができたとしても、どんな楕円もデータにうまく適合しません。それはただ
> 不適切なモデル。これらのデータに楕円を当てはめる場合は、当てはめが早く失敗するようにする必要があります。
> 図 6: 「フィット ファスト、フェイル ファスト」の必要性の図: (a) 測定値を表す理想化されたデータ

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- 曲線を系列の後の点に適合させる摂動。

## Chunk 0165

### English（抽出4行）

> ments of planetary orbit which could be ﬁt as an ellipse with measurement error, (b) Measurements
> of a hypothetical orbit that was perturbed by a Death Star. In the second example, it would be
> challenging to ﬁt a single ellipse to the data—but we have no particular interest in an omnibus
> elliptical ﬁt in any case. We would like any attempt to ﬁt an ellipse to the second dataset to fail fast.

### 日本語訳（自動翻訳）

> 測定誤差を伴う楕円として適合する可能性のある惑星軌道の部分、(b) 測定
> デス・スターによって撹乱された仮想の軌道。 2 番目の例では、次のようになります。
> 単一の楕円をデータに適合させるのは難しいですが、オムニバスには特に興味がありません
> いずれにしても楕円フィットです。 2 番目のデータセットに楕円を当てはめる試みはすべて失敗するようにしたいと考えています。

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- 測定誤差を伴う楕円として適合する可能性のある惑星軌道の部分、(b) 測定 デス・スターによって撹乱された仮想の軌道。

## Chunk 0166

### English（抽出4行）

> can quickly move on to something more reasonable.
> This example has, in extreme form, a common pattern of diﬃcult statistical computations, that
> ﬁtting to diﬀerent subsets of the data yields much diﬀerent parameter estimates.
> 4.

### 日本語訳（自動翻訳）

> より合理的な方法にすぐに移ることができます。
> この例には、極端な形で、難しい統計計算の共通パターンが含まれています。
> データの異なるサブセットにフィッティングすると、はるかに異なるパラメータ推定値が得られます。
> 4.

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- より合理的な方法にすぐに移ることができます。

## Chunk 0167

### English（抽出4行）

> Using constructed data to find and understand problems
> The ﬁrst step in validating computation is to check that the model actually ﬁnishes the ﬁtting
> process in an acceptable time frame and the convergence diagnostics are reasonable. In the context
> of HMC, this is primarily the absence of divergent transitions, bR diagnostic near 1, and suﬃcient

### 日本語訳（自動翻訳）

> 構築されたデータを使用して問題を見つけて理解する
> 計算を検証する最初のステップは、モデルが実際にフィッティングを完了していることを確認することです。
> 許容可能な時間枠内でプロセスが完了し、収束診断が妥当であること。文脈の中で
> HMC の場合、これは主に発散遷移が存在せず、bR 診断が 1 に近く、十分な値であることです。

### 熟語・専門語

- **divergent**: divergence。HMC/NUTSで幾何が悪く積分が破綻した警告。
- **ESS**: 有効サンプルサイズ。自己相関を考慮した独立サンプル相当数。

### 要約

- 構築されたデータを使用して問題を見つけて理解する 計算を検証する最初のステップは、モデルが実際にフィッティングを完了していることを確認することです。

## Chunk 0168

### English（抽出4行）

> eﬀective sample sizes for the central tendency, the tail quantiles, and the energy (Vehtari et al.,
> 2020). However, those diagnostics cannot protect against a probabilistic program that is computed
> correctly but encodes a diﬀerent model than the user intended.
> The main tool we have for ensuring that the statistical computation is done reasonably well is

### 日本語訳（自動翻訳）

> 中心傾向、尾部分位数、およびエネルギーの有効なサンプル サイズ (Vehtari et al.,
> 2020年）。ただし、これらの診断は、計算される確率的プログラムから保護することはできません。
> 正しくはエンコードされますが、ユーザーが意図したものとは異なるモデルがエンコードされます。
> 統計計算が適切に行われることを保証するための主なツールは次のとおりです。

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- 中心傾向、尾部分位数、およびエネルギーの有効なサンプル サイズ (Vehtari et al., 2020年）。

## Chunk 0169

### English（抽出4行）

> to actually ﬁt the model to some data and check that the ﬁt is good. Real data can be awkward for
> this purpose because modeling issues can collide with computational issues and make it impossible
> to tell if the problem is the computation or the model itself. To get around this challenge, we ﬁrst
> explore models by ﬁtting them to simulated data.

### 日本語訳（自動翻訳）

> 実際にモデルをいくつかのデータに適合させ、適合が良好であることを確認します。実際のデータは扱いにくい場合があります
> モデリングの問題が計算の問題と衝突して不可能になる可能性があるため、これが目的です。
> 問題が計算にあるのかモデル自体にあるのかを判断します。この課題を回避するには、まず、
> モデルをシミュレートされたデータに適合させてモデルを探索します。

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- 実際にモデルをいくつかのデータに適合させ、適合が良好であることを確認します。

## Chunk 0170

### English（抽出4行）

> 4.1.
> Fake-data simulation
> Working in a controlled setting where the true parameters are known can help us understand our
> data model and priors, what can be learned from an experiment, and the validity of the applied

### 日本語訳（自動翻訳）

> 4.1.
> 偽データのシミュレーション
> 真のパラメータがわかっている制御された設定で作業することは、私たちの理解を助けることができます。
> データモデルと事前分布、実験から何が学べるか、適用されたデータの妥当性

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- 4.1. 偽データのシミュレーション 真のパラメータがわかっている制御された設定で作業することは、私たちの理解を助けることができます。

## Chunk 0171

### English（抽出4行）

> inference methods. The basic idea is to check whether our procedure recovers the correct parameter
> values when ﬁtting fake data. Typically we choose parameter values that seem reasonable a priori
> and then simulate a fake dataset of the same size, shape, and structure as the original data. We next
> ﬁt the model to the fake data to check several things.

### 日本語訳（自動翻訳）

> 推論方法。基本的な考え方は、手順が正しいパラメータを回復するかどうかを確認することです。
> 偽のデータを当てはめるときの値。通常、私たちは先験的に合理的であると思われるパラメータ値を選択します
> そして、元のデータと同じサイズ、形状、構造の偽のデータセットをシミュレートします。次は私たち
> モデルを偽のデータに当てはめて、いくつかのことを確認します。

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

> 最初にチェックするのは、厳密には計算上のものではなく、データの設計の側面です。
> すべてのパラメータについて、観察されたデータが追加情報を提供できるかどうかを確認します。
> 以前を超えて。この手順では、固定された既知のモデルから偽のデータをシミュレートします。
> パラメータを調べて、私たちの方法が既知の真実の再現に近づいているかどうかを確認します。できます

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- 最初にチェックするのは、厳密には計算上のものではなく、データの設計の側面です。

## Chunk 0173

### English（抽出4行）

> look at point estimates and also the coverage of posterior intervals.
> If our fake-data check fails, in the sense that the inferences are not close to the assumed parameter
> values or if there seem to be model components that are not gaining any information from the data
> (Lindley, 1956, Goel and DeGroot, 1981), we recommend breaking down the model. Go simpler

### 日本語訳（自動翻訳）

> 点推定と事後間隔の範囲も確認してください。
> 偽データのチェックが失敗した場合、推論が想定されたパラメータに近くないという意味で
> 値、またはデータから情報を取得していないモデル コンポーネントがあるように見える場合
> (Lindley、1956 年、Goel と DeGroot、1981 年)、モデルを細分化することをお勧めします。もっとシンプルに

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- 点推定と事後間隔の範囲も確認してください。

## Chunk 0174

### English（抽出4行）

> and simpler until we get the model to work. Then, from there, we can try to identify the problem,
> as illustrated in Section 5.2.
> The second thing that we check is if the true parameters can be recovered to roughly within
> the uncertainty implied by the ﬁtted posterior distribution. This will not be possible if the data

### 日本語訳（自動翻訳）

> モデルを動作させるまではもっと簡単です。その後、そこから問題を特定していきます。
> セクション 5.2 で説明されているとおりです。
> 次にチェックするのは、実際のパラメータがおおよその範囲内に回復できるかどうかです。
> 当てはめられた事後分布によって暗示される不確実性。データが次の場合はこれは不可能です。

### 熟語・専門語

- **posterior distribution**: 事後分布。データ観測後の未知量の不確実性を表す分布。
- **uncertainty**: 不確実性。観測・パラメータ・モデル構造・意思決定に残る曖昧さ。

### 要約

- モデルを動作させるまではもっと簡単です。

## Chunk 0175

### English（抽出4行）

> are not informative for a parameter, but it should typically happen otherwise. It is not possible
> to run a single fake data simulation, compute the associated posterior distribution, and declare
> that everything works well. We will see in the next section that a more elaborate setup is needed.
> However, a single simulation run will often reveal blatant errors. For instance, if the code has an

### 日本語訳（自動翻訳）

> これはパラメータに関しては有益ではありませんが、通常はそれ以外の場合に発生するはずです。それは不可能です
> 単一の偽データ シミュレーションを実行し、関連する事後分布を計算し、宣言します。
> すべてがうまくいくこと。次のセクションでは、より複雑な設定が必要であることを見ていきます。
> ただし、シミュレーションを 1 回実行すると、明らかなエラーが明らかになることがよくあります。たとえば、コードに

### 熟語・専門語

- **posterior distribution**: 事後分布。データ観測後の未知量の不確実性を表す分布。

### 要約

- これはパラメータに関しては有益ではありませんが、通常はそれ以外の場合に発生するはずです。

## Chunk 0176

### English（抽出4行）

> error in it and ﬁts the wrong model this will often be clear from a catastrophic failure of parameter
> recovery.
> The third thing that we can do is use fake data simulations to understand how the behavior
> of a model can change across diﬀerent parts of the parameter space. In this sense, a statistical

### 日本語訳（自動翻訳）

> エラーがあり、間違ったモデルに適合している場合、これは多くの場合、パラメーターの致命的な障害から明らかです。
> 回復。
> 私たちができる 3 番目のことは、偽のデータ シミュレーションを使用して、動作がどのように行われるかを理解することです。
> モデルの変化はパラメータ空間のさまざまな部分で変化する可能性があります。この意味で、統計的には、

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- エラーがあり、間違ったモデルに適合している場合、これは多くの場合、パラメーターの致命的な障害から明らかです。

## Chunk 0177

### English（抽出4行）

> model can contain many stories of how the data get generated. As illustrated in Section 5.9, the
> data are informative about the parameters for a sum of declining exponentials when the exponents
> are well separated, but not so informative when the two components are close to each other. This
> sort of instability contingent on parameter values is also a common phenomenon in diﬀerential

### 日本語訳（自動翻訳）

> モデルには、データがどのように生成されるかについての多くのストーリーを含めることができます。セクション 5.9 で説明したように、
> データは、指数が減少するときの合計のパラメータに関する情報を提供します。
> は十分に分離されていますが、2 つのコンポーネントが互いに近い場合はあまり有益ではありません。これ
> パラメータ値に依存するある種の不安定性も、差分動作ではよく見られる現象です。

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- モデルには、データがどのように生成されるかについての多くのストーリーを含めることができます。

## Chunk 0178

### English（抽出4行）

> equation models, as can been seen in Section 11. For another example, the posterior distribution
> of a hierarchical model looks much diﬀerent at the neck than at the mouth of the funnel geometry
> implied by the hierarchical prior. Similar issues arise in Gaussian process models, depending on
> the length scale of the process and the resolution of the data.

### 日本語訳（自動翻訳）

> セクション 11 で見られるように、方程式モデル。別の例として、事後分布
> 階層モデルのファネル ジオメトリは、首部と口部で大きく異なって見えます。
> 階層的な事前分布によって暗示されます。ガウス過程モデルでも同様の問題が発生します。
> プロセスの長さのスケールとデータの解像度。

### 熟語・専門語

- **posterior distribution**: 事後分布。データ観測後の未知量の不確実性を表す分布。
- **ESS**: 有効サンプルサイズ。自己相関を考慮した独立サンプル相当数。

### 要約

- セクション 11 で見られるように、方程式モデル。

## Chunk 0179

### English（抽出4行）

> All this implies that fake data simulation can be particularly relevant in the zone of the parameter
> space that is predictive of the data. This in turn suggests a two-step procedure in which we ﬁrst
> ﬁt the model to real data, then draw parameters from the resulting posterior distribution to use in
> fake-data checking. The statistical properties of such a procedure are unclear but in practice we

### 日本語訳（自動翻訳）

> これらすべては、偽のデータ シミュレーションがパラメーターのゾーンに特に関係している可能性があることを意味します。
> データを予測する空間。これは、次の 2 段階の手順を示唆しています。
> モデルを実際のデータに適合させ、結果の事後分布からパラメータを引き出して使用します。
> 偽データチェック。このような手順の統計的特性は不明ですが、実際には

### 熟語・専門語

- **posterior distribution**: 事後分布。データ観測後の未知量の不確実性を表す分布。

### 要約

- これらすべては、偽のデータ シミュレーションがパラメーターのゾーンに特に関係している可能性があることを意味します。

## Chunk 0180

### English（抽出4行）

> have found such checks to be helpful, both for revealing problems with the computation or model,
> and for providing some reassurance when the fake-data-based inferences do reproduce the assumed
> parameter value.
> To carry this idea further, we may break our method by coming up with fake data that cause

### 日本語訳（自動翻訳）

> このようなチェックは、計算やモデルの問題を明らかにするために役立つことがわかりました。
> そして、偽のデータに基づいた推論が想定を再現した場合に、ある程度の安心感を提供してくれました。
> パラメータ値。
> この考えをさらに進めるために、偽のデータを考え出すことで私たちの方法を壊すかもしれません。

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- このようなチェックは、計算やモデルの問題を明らかにするために役立つことがわかりました。

## Chunk 0181

### English（抽出4行）

> our procedure to give bad answers. This sort of simulation-and-exploration can be the ﬁrst step in
> a deeper understanding of an inference method, which can be valuable even for a practitioner who
> plans to use this method for just one applied problem. It can also be useful for building up a set of
> more complex models to possibly explore later.

### 日本語訳（自動翻訳）

> 悪い回答をするための私たちの手順。この種のシミュレーションと調査は、
> 推論方法についてのより深い理解。これは、次のような実務家にとっても価値があります。
> は、この方法を 1 つの応用問題にのみ使用する予定です。セットを組み立てるのにも役立ちます。
> より複雑なモデルは後で検討する可能性があります。

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- 悪い回答をするための私たちの手順。

## Chunk 0182

### English（抽出4行）

> Fake-data simulation is a crucial component of our workﬂow because it is, arguably, the only
> point where we can directly check that our inference on latent variables is reliable. When ﬁtting the
> model to real data, we do not by deﬁnition observe the latent variables. Hence we can only evaluate
> how our model ﬁts the observed data. If our goal is not merely prediction but estimating the latent

### 日本語訳（自動翻訳）

> フェイクデータのシミュレーションは、おそらく、唯一のワークフローであるため、ワークフローの重要なコンポーネントです。
> 潜在変数に対する推論が信頼できるかどうかを直接確認できる点です。取り付けるときは、
> 実際のデータをモデル化する場合、定義上、潜在変数は観察されません。したがって、評価することしかできません
> 私たちのモデルが観察されたデータにどのように適合するか。私たちの目標が単なる予測ではなく、潜在的な予測を推定することである場合、

### 熟語・専門語

- **prediction**: 予測。未知/将来/除外データに対する分布や点推定。

### 要約

- フェイクデータのシミュレーションは、おそらく、唯一のワークフローであるため、ワークフローの重要なコンポーネントです。

## Chunk 0183

### English（抽出4行）

> variables, examining predictions only helps us so much. This is especially true of overparameterized
> models, where wildly diﬀerent parameter values can yield comparable predictions (e.g. Section 5.9
> and Gelman et al, 1996).
> In general, even when the model ﬁt is good, we should only draw

### 日本語訳（自動翻訳）

> 変数を考慮して、予測を調べるだけでも非常に役立ちます。これは特にオーバーパラメータ化された場合に当てはまります
> モデルでは、大きく異なるパラメータ値が同等の予測を生み出すことができます (例: セクション 5.9
> およびゲルマンら、1996)。
> 一般に、モデルの適合性が良好な場合でも、描画のみを行う必要があります。

### 熟語・専門語

- **prediction**: 予測。未知/将来/除外データに対する分布や点推定。

### 要約

- 変数を考慮して、予測を調べるだけでも非常に役立ちます。

## Chunk 0184

### English（抽出4行）

> conclusions about the estimated latent variables with caution. Fitting the model to simulated data
> helps us better understand what the model can and cannot learn about the latent process in a
> controlled setting where we know the ground truth. If a model is able to make good inference
> on fake-data generated from that very model, this provides no guarantee that its inference on real

### 日本語訳（自動翻訳）

> 推定された潜在変数に関する結論には注意が必要です。モデルをシミュレートされたデータに適合させる
> これは、モデルが潜在的なプロセスについて何を学習でき、何を学習できないかをより深く理解するのに役立ちます。
> 私たちが正確な情報を知ることができる、管理された設定。モデルが適切な推論を行うことができる場合
> そのモデルから生成された偽データについては、その推論が本物であるという保証はありません。

### 熟語・専門語

- **ESS**: 有効サンプルサイズ。自己相関を考慮した独立サンプル相当数。

### 要約

- 推定された潜在変数に関する結論には注意が必要です。

## Chunk 0185

### English（抽出4行）

> data will be sensible. But if a model is unable to make good inference on such fake data, then it’s
> hopeless to expect the model to provide reasonable inference on real data. Fake-data simulations
> provide an upper bound of what can be learned about a latent process.
> 4.2.

### 日本語訳（自動翻訳）

> データは賢明なものになるでしょう。しかし、モデルがそのような偽のデータに対して適切な推論を行うことができない場合、それは問題になります。
> モデルが実際のデータに対して合理的な推論を提供することを期待するのは絶望的です。偽データのシミュレーション
> 潜在的なプロセスについて学習できることの上限を提供します。
> 4.2.

### 熟語・専門語

- **ESS**: 有効サンプルサイズ。自己相関を考慮した独立サンプル相当数。

### 要約

- データは賢明なものになるでしょう。

## Chunk 0186

### English（抽出4行）

> Simulation-based calibration
> There is a formal, and at times practical, issue when comparing the result of Bayesian inference, a
> posterior distribution, to a single (true) point, as illustrated in Figure 7.
> Using a single fake data simulation to test a model will not necessarily “work,” even if the

### 日本語訳（自動翻訳）

> シミュレーションベースのキャリブレーション
> ベイズ推論の結果を比較する際には、形式的で、時には実際的な問題があります。
> 図 7 に示すように、単一 (真) 点への事後分布。
> モデルをテストするために単一の偽のデータ シミュレーションを使用しても、必ずしも「機能」するとは限りません。

### 熟語・専門語

- **Bayesian inference**: ベイズ推論。事前分布と尤度から事後分布を計算する中核処理。
- **simulation-based calibration**: SBC。シミュレーション真値と事後rankを比べ、実装・推論の校正を検査する方法。
- **posterior distribution**: 事後分布。データ観測後の未知量の不確実性を表す分布。
- **ESS**: 有効サンプルサイズ。自己相関を考慮した独立サンプル相当数。

### 要約

- シミュレーションベースのキャリブレーション ベイズ推論の結果を比較する際には、形式的で、時には実際的な問題があります。

## Chunk 0187

### English（抽出4行）

> computational algorithm is working correctly. The problem here arises not just because with one
> simulation anything can happen (there is a 5% chance that a random draw will be outside a 95%
> uncertainty interval) but also because Bayesian inference will in general only be calibrated when
> averaging over the prior, not for any single parameter value. Furthermore, parameter recovery may

### 日本語訳（自動翻訳）

> 計算アルゴリズムは正しく動作しています。ここで問題が発生するのは、単に
> シミュレーションでは何でも起こります (ランダムな抽選が 95% の範囲外になる確率は 5% です)
> 不確実性区間）だけでなく、ベイズ推論は一般に次の場合にのみ校正されるためでもあります。
> 単一のパラメータ値ではなく、以前の値の平均をとります。さらに、パラメータの回復は、

### 熟語・専門語

- **Bayesian inference**: ベイズ推論。事前分布と尤度から事後分布を計算する中核処理。
- **uncertainty**: 不確実性。観測・パラメータ・モデル構造・意思決定に残る曖昧さ。

### 要約

- 計算アルゴリズムは正しく動作しています。

## Chunk 0188

### English（抽出4行）

> fail not because the algorithm fails, but because the observed data are not providing information
> that could update the uncertainty quantiﬁed by the prior for a particular parameter. If the prior
> and posterior are approximately unimodal and the chosen parameter value is from the center of the
> prior, we can expect overcoverage of posterior intervals.

### 日本語訳（自動翻訳）

> 失敗するのは、アルゴリズムが失敗したからではなく、観察されたデータが情報を提供していないからです
> これにより、特定のパラメータの事前分布によって定量化された不確実性が更新される可能性があります。以前の場合
> および事後分布はほぼ単峰性であり、選択されたパラメータ値は中心からのものです。
> 事前に、後方間隔のオーバーカバレッジが期待できます。

### 熟語・専門語

- **uncertainty**: 不確実性。観測・パラメータ・モデル構造・意思決定に残る曖昧さ。
- **approximate**: 近似。速度や扱いやすさのため、正確な推論・モデルを緩めること。

### 要約

- 失敗するのは、アルゴリズムが失敗したからではなく、観察されたデータが情報を提供していないからです これにより、特定のパラメータの事前分布によって定量化された不確実性が更新される可能性があります。

## Chunk 0189

### English（抽出4行）

> A more comprehensive approach than what we present in Section 4.1 is simulation-based
> calibration (SBC; Cook et al., 2006, Talts et al., 2020). In this scheme, the model parameters are
> drawn from the prior; then data are simulated conditional on these parameter values; then the model
> is ﬁt to data; and ﬁnally the obtained posterior is compared to the simulated parameter values that

### 日本語訳（自動翻訳）

> セクション 4.1 で説明したものよりも包括的なアプローチは、シミュレーション ベースです。
> キャリブレーション (SBC; Cook et al., 2006、Talts et al., 2020)。このスキームでは、モデルパラメータは次のとおりです。
> 以前のものから抽出されます。次に、これらのパラメータ値に基づいてデータがシミュレートされます。それからモデル
> データに適合している。そして最後に、得られた事後分布がシミュレートされたパラメータ値と比較されます。

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- セクション 4.1 で説明したものよりも包括的なアプローチは、シミュレーション ベースです。

## Chunk 0190

### English（抽出4行）

> were used to generate the data. By repeating this procedure several times, it is possible to check
> the coherence of the inference algorithm. The idea is that by performing Bayesian inference across
> a range of datasets simulated using parameters drawn from the prior, we should recover the prior.
> Simulation-based calibration is useful to evaluate how closely approximate algorithms match the

### 日本語訳（自動翻訳）

> データの生成に使用されました。この手順を数回繰り返すことで確認できます。
> 推論アルゴリズムの一貫性。このアイデアは、ベイズ推論を実行することによって、
> 事前データから抽出されたパラメータを使用してシミュレートされたデータセットの範囲では、事前データを復元する必要があります。
> シミュレーションベースのキャリブレーションは、近似アルゴリズムがどの程度一致しているかを評価するのに役立ちます。

### 熟語・専門語

- **Bayesian inference**: ベイズ推論。事前分布と尤度から事後分布を計算する中核処理。
- **simulation-based calibration**: SBC。シミュレーション真値と事後rankを比べ、実装・推論の校正を検査する方法。
- **approximate**: 近似。速度や扱いやすさのため、正確な推論・モデルを緩めること。

### 要約

- データの生成に使用されました。

## Chunk 0191

### English（抽出4行）

> theoretical posterior even in cases when the posterior is not tractable.
> While in many ways superior to benchmarking against a truth point, simulation-based calibration
> requires ﬁtting the model multiple times, which incurs a substantial computational cost, especially
> if we do not use extensive parallelization. In our view, simulation-based calibration and truth-point

### 日本語訳（自動翻訳）

> 事後検査が扱いにくい場合でも、理論上の事後検査を行うことができます。
> 多くの点で真理点に対するベンチマークよりも優れていますが、シミュレーションベースのキャリブレーションは
> モデルを複数回フィッティングする必要があり、特に、かなりの計算コストがかかります。
> 大規模な並列化を使用しない場合。私たちの見解では、シミュレーションベースのキャリブレーションと真理点

### 熟語・専門語

- **simulation-based calibration**: SBC。シミュレーション真値と事後rankを比べ、実装・推論の校正を検査する方法。

### 要約

- 事後検査が扱いにくい場合でも、理論上の事後検査を行うことができます。

## Chunk 0192

### English（抽出4行）

> benchmarking are two ends of a spectrum. Roughly, a single truth-point benchmark will possibly
> ﬂag gross problems, but it does not guarantee anything. As we do more experiments, it is possible
> to see ﬁner and ﬁner problems in the computation. It is an open research question to understand
> SBC with a small number of draws. We expect that abandoning random draws for a more designed

### 日本語訳（自動翻訳）

> ベンチマークはスペクトルの両端です。おおよそ、単一の真理点ベンチマークは、
> 重大な問題を報告しますが、何も保証しません。さらに実験を行うと、可能性があります
> 計算におけるより細かい問題を確認できるようになります。それは理解することが未解決の研究課題です
> 引き分け数が少ないSBC。よりデザインされたものを得るために、ランダムな抽選を放棄することを期待しています。

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- ベンチマークはスペクトルの両端です。

## Chunk 0193

### English（抽出4行）

> exploration of the prior would make the method more eﬃcient, especially in models with a relatively
> small number of parameters.
> A serious problem with SBC is that it clashes somewhat with most modelers’ tendency to
> specify their priors wider than they believe necessary. The slightly conservative nature of weakly

### 日本語訳（自動翻訳）

> 事前分布を探索すると、特に比較的に複雑なモデルの場合、この方法がより効率的になります。
> パラメータの数が少ない。
> SBC の深刻な問題は、ほとんどのモデラーの傾向と多少衝突することです。
> 必要と思われるよりも広範囲に事前分布を指定します。弱気のやや保守的な性質

### 熟語・専門語

- **ESS**: 有効サンプルサイズ。自己相関を考慮した独立サンプル相当数。

### 要約

- 事前分布を探索すると、特に比較的に複雑なモデルの場合、この方法がより効率的になります。

## Chunk 0194

### English（抽出4行）

> informative priors can cause the data sets simulated during SBC to occasionally be extreme. Gabry
> et al. (2019) give an example in which fake air pollution datasets were simulated where the pollution
> is denser than a black hole. These extreme data sets can cause an algorithm that works well on
> realistic data to fail dramatically. But this isn’t really a problem with the computation so much as a

### 日本語訳（自動翻訳）

> 有益な事前分布により、SBC 中にシミュレートされたデータ セットが極端になる場合があります。ゲイブリー
> 他。 (2019) 偽の大気汚染データセットがシミュレートされた例を挙げてください。
> ブラックホールよりも密度が高い。これらの極端なデータセットにより、アルゴリズムが適切に機能する可能性があります。
> 現実的なデータは劇的に失敗する可能性があります。しかし、これは実際には計算上の問題ではなく、

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- 有益な事前分布により、SBC 中にシミュレートされたデータ セットが極端になる場合があります。

## Chunk 0195

### English（抽出4行）

> scenario 1
> scenario 2
> scenario 3
> −3

### 日本語訳（自動翻訳）

> シナリオ1
> シナリオ2
> シナリオ3
> −3

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- シナリオ1 シナリオ2 シナリオ3 −3

## Chunk 0196

### English（抽出4行）

> 9−3
> 9−3
> 0.00
> 0.25

### 日本語訳（自動翻訳）

> 9−3
> 9−3
> 0.00
> 0.25

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- 9−3 9−3 0.00 0.25

## Chunk 0197

### English（抽出4行）

> 0.50
> 0.75
> 1.00
> µ

### 日本語訳（自動翻訳）

> 0.50
> 0.75
> 1.00
> μ

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- 0.50 0.75 1.00 μ

## Chunk 0198

### English（抽出4行）

> Figure 7: Comparison of a posterior distribution to the assumed true parameter value. When
> ﬁtting the model to simulated data, we can examine whether the posterior sample (blue histogram)
> comports with the true parameter value (red line). In scenario 1, the posterior is centered at the
> true value, which suggests the ﬁt is reasonable. In scenario 2, the true parameter is now in the

### 日本語訳（自動翻訳）

> 図 7: 事後分布と想定される真のパラメータ値の比較。いつ
> モデルをシミュレートされたデータに当てはめると、事後サンプル (青色のヒストグラム) が
> 真のパラメータ値と一致します (赤線)。シナリオ 1 では、後部の中心は
> true 値は、適合が妥当であることを示しています。シナリオ 2 では、true パラメータは

### 熟語・専門語

- **posterior distribution**: 事後分布。データ観測後の未知量の不確実性を表す分布。

### 要約

- 図 7: 事後分布と想定される真のパラメータ値の比較。

## Chunk 0199

### English（抽出4行）

> tail of the posterior distribution. It is unclear whether this indicates a fault in our inference. In
> scenario 3, the posterior is multimodal and it becomes evident that comparing the posterior to a
> single point cannot validate the inference algorithm. A more comprehensive approach, such as
> simulation-based calibration, can teach us more.

### 日本語訳（自動翻訳）

> 事後分布の裾。これが私たちの推論に誤りがあることを示しているかどうかは不明です。で
> シナリオ 3 では、事後分布はマルチモーダルであり、事後分布を
> 単一ポイントでは推論アルゴリズムを検証できません。より包括的なアプローチ、たとえば、
> シミュレーションベースのキャリブレーションは、さらに多くのことを教えてくれます。

### 熟語・専門語

- **simulation-based calibration**: SBC。シミュレーション真値と事後rankを比べ、実装・推論の校正を検査する方法。
- **posterior distribution**: 事後分布。データ観測後の未知量の不確実性を表す分布。

### 要約

- 事後分布の裾。

## Chunk 0200

### English（抽出4行）

> If nobody gets the treatment
> Midterm exam score
> Final exam score
> Balanced treatment assignment

### 日本語訳（自動翻訳）

> 誰も治療を受けられなかったら
> 中間試験の得点
> 最終試験のスコア
> バランスの取れた治療の割り当て

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- 誰も治療を受けられなかったら 中間試験の得点 最終試験のスコア バランスの取れた治療の割り当て

## Chunk 0201

### English（抽出4行）

> Midterm exam score
> Final exam score
> Figure 8: Simulated data on 500 students from a hypothetical study of the eﬀect of an educational
> intervention.

### 日本語訳（自動翻訳）

> 中間試験の得点
> 最終試験のスコア
> 図 8: 教育の効果に関する仮説研究から得られた 500 人の生徒に関するシミュレーション データ
> 介入。

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- 中間試験の得点 最終試験のスコア 図 8: 教育の効果に関する仮説研究から得られた 500 人の生徒に関するシミュレーション データ 介入。

## Chunk 0202

### English（抽出4行）

> problem with the prior.
> One possible way around this is to ensure that the priors are very tight. However, a pragmatic
> idea is to keep the priors and compute reasonable parameter values using the real data. This can
> be done either through rough estimates or by computing the actual posterior. We then suggest

### 日本語訳（自動翻訳）

> 前回の問題。
> これを回避する可能な方法の 1 つは、事前分布を非常に厳密にすることです。ただし、実際的な
> アイデアは、事前分布を保持し、実際のデータを使用して妥当なパラメータ値を計算することです。これはできる
> 概算は、概算または実際の事後計算によって行われます。次に提案します

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- 前回の問題。

## Chunk 0203

### English（抽出4行）

> widening out the estimates slightly and using these as a prior for the SBC. This will ensure that all
> of the simulated data will be as realistic as the model allows.
> 4.3.
> Experimentation using constructed data

### 日本語訳（自動翻訳）

> 推定値をわずかに広げて、これらを SBC の事前分布として使用します。これにより、すべてのことが保証されます。
> シミュレートされたデータは、モデルが許す限り現実的になります。
> 4.3.
> 構築したデータを用いた実験

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- 推定値をわずかに広げて、これらを SBC の事前分布として使用します。

## Chunk 0204

### English（抽出4行）

> A good way to understand a model is to ﬁt it to data simulated from diﬀerent scenarios.
> For a simple case, suppose we are interested in the statistical properties of linear regression ﬁt
> to data from alternative distributional forms. To start, we could specify data xi, i = 1, . . . , n, draw
> coeﬃcients a and b and a residual standard deviation σ from our prior distribution, simulate data

### 日本語訳（自動翻訳）

> モデルを理解する良い方法は、さまざまなシナリオからシミュレートされたデータにモデルを当てはめることです。
> 単純なケースとして、線形回帰フィットの統計的特性に興味があると仮定します。
> 代替の配布形式からのデータに変換します。まず、データ xi、i = 1、... を指定できます。 。 。 、n、描画
> 係数 a と b、および事前分布からの残差標準偏差 σ、データをシミュレート

### 熟語・専門語

- **prior distribution**: 事前分布。データ観測前の知識・制約を表す分布。
- **ESS**: 有効サンプルサイズ。自己相関を考慮した独立サンプル相当数。

### 要約

- モデルを理解する良い方法は、さまざまなシナリオからシミュレートされたデータにモデルを当てはめることです。

## Chunk 0205

### English（抽出4行）

> from yi ∼normal(a + bxi, σ), and ﬁt the model to the simulated data. Repeat this 1000 times and
> we can check the coverage of interval estimates: that’s a version of simulation-based calibration.
> We could then ﬁt the same model but simulating data using diﬀerent assumptions, for example
> drawing independent data points yi from the t4 distribution rather than the normal. This will then

### 日本語訳（自動翻訳）

> yi 〜normal(a + bxi, σ) から計算し、モデルをシミュレートされたデータに適合させます。これを1000回繰り返すと、
> 間隔推定の範囲を確認できます。これは、シミュレーションベースのキャリブレーションのバージョンです。
> 次に、同じモデルを当てはめることができますが、たとえば、異なる仮定を使用してデータをシミュレートします。
> 正規分布ではなく t4 分布から独立したデータ点 yi を描画します。これにより、

### 熟語・専門語

- **simulation-based calibration**: SBC。シミュレーション真値と事後rankを比べ、実装・推論の校正を検査する方法。

### 要約

- yi 〜normal(a + bxi, σ) から計算し、モデルをシミュレートされたデータに適合させます。

## Chunk 0206

### English（抽出4行）

> fail simulation-based calibration—the wrong model is being ﬁt—but the interesting question here
> is, how bad will these inferences be? One could, for example, use SBC simulations to examine
> coverage of posterior 50% and 95% intervals for the coeﬃcients.
> For a more elaborate example, we perform a series of simulations to understand assumptions

### 日本語訳（自動翻訳）

> シミュレーションベースのキャリブレーションが失敗する - 間違ったモデルが適合している - しかし、ここで興味深い質問があります。
> ということは、これらの推論はどれほど悪いものになるでしょうか？たとえば、SBC シミュレーションを使用して調べることができます。
> 係数の事後 50% および 95% 間隔をカバーします。
> より複雑な例として、仮定を理解するために一連のシミュレーションを実行します。

### 熟語・専門語

- **simulation-based calibration**: SBC。シミュレーション真値と事後rankを比べ、実装・推論の校正を検査する方法。

### 要約

- シミュレーションベースのキャリブレーションが失敗する - 間違ったモデルが適合している - しかし、ここで興味深い質問があります。

## Chunk 0207

### English（抽出4行）

> and bias correction in observational studies. We start with a scenario in which 500 students in a
> class take a midterm and ﬁnal exam. We simulate the data by ﬁrst drawing students’ true abilities
> ηi from a normal(50, 20) distribution, then drawing the two exam scores xi, yi as independent
> normal(ηi, 10) distributions. This induces the two scores to have a correlation of

### 日本語訳（自動翻訳）

> 観察研究におけるバイアス補正。 500 人の生徒が 1 つのグループに参加するシナリオから始めます。
> クラスは中間試験と期末試験を受けます。生徒の真の能力を最初に引き出してデータをシミュレーションします
> 正規 (50, 20) 分布から ηi を取得し、2 つの試験スコア xi と yi を独立したものとして描画します
> 正規分布(ηi, 10)。これにより、2 つのスコアには次の相関関係があることがわかります。

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
> グラフでパターンを明確にするために、この高い値を使用してシミュレーションを設計しました。図
> 8a は、基礎となる回帰直線 E(y|x) とともに結果を表示します。次に、
> 中間期後に実行される治療のランダム化実験で 10 が追加されるという仮定の実験

### 熟語・専門語

- **ESS**: 有効サンプルサイズ。自己相関を考慮した独立サンプル相当数。

### 要約

- 202+52 = 0.94; グラフでパターンを明確にするために、この高い値を使用してシミュレーションを設計しました。

## Chunk 0209

### English（抽出4行）

> Pre−test score
> Pr (z=1)
> 0.0
> 0.5

### 日本語訳（自動翻訳）

> プレテストのスコア
> Pr (z=1)
> 0.0
> 0.5

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- プレテストのスコア Pr (z=1) 0.0 0.5

## Chunk 0210

### English（抽出4行）

> 1.0
> (assigned to treatment group, z=1)
> (assigned to control group, z=0)
> Unalanced treatment assignment

### 日本語訳（自動翻訳）

> 1.0
> (治療グループに割り当て、z=1)
> (コントロールグループに割り当て、z=0)
> アンバランスな治療割り当て

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- 1.0 (治療グループに割り当て、z=1) (コントロールグループに割り当て、z=0) アンバランスな治療割り当て

## Chunk 0211

### English（抽出4行）

> Midterm exam score
> Final exam score
> Figure 9: Alternative simulation in which the treatment assignment is unbalanced, with less well-
> performing students being more likely to receive the treatment.

### 日本語訳（自動翻訳）

> 中間試験の得点
> 最終試験のスコア
> 図 9: 治療の割り当てが不均衡であり、治療効果が低い場合の代替シミュレーション。
> 成績の良い生徒は治療を受ける可能性が高くなります。

### 熟語・専門語

- **ESS**: 有効サンプルサイズ。自己相関を考慮した独立サンプル相当数。

### 要約

- 中間試験の得点 最終試験のスコア 図 9: 治療の割り当てが不均衡であり、治療効果が低い場合の代替シミュレーション。

## Chunk 0212

### English（抽出4行）

> points to any student’s ﬁnal exam score. We give each student an equal chance of receiving the
> treatment or control. Figure 8b shows the simulated data and underlying regression lines.
> In this example we can estimate the treatment eﬀect by simply taking the diﬀerence between
> the two groups, which for these simulated data yields an estimate of 10.7 with standard error 1.8.

### 日本語訳（自動翻訳）

> 学生の最終試験の得点を指します。私たちは各学生に平等なチャンスを与えます。
> 治療または制御。図 8b は、シミュレートされたデータと基礎となる回帰直線を示しています。
> この例では、単純に以下の差を取ることで治療効果を推定できます。
> 2 つのグループでは、これらのシミュレートされたデータの推定値は 10.7、標準誤差は 1.8 です。

### 熟語・専門語

- **ESS**: 有効サンプルサイズ。自己相関を考慮した独立サンプル相当数。

### 要約

- 学生の最終試験の得点を指します。

## Chunk 0213

### English（抽出4行）

> Or we can ﬁt a regression adjusting for midterm score, yielding an estimate of 9.7 ± 0.6.
> We next consider an unbalanced assignment mechanism in which the probability of receiving
> the treatment depends on the midterm score: Pr(z = 1) = logit−1((x −50)/10). Figure 9a shows
> simulated treatment assignments for the 200 students and Figure 9a displays the simulated exam

### 日本語訳（自動翻訳）

> あるいは、中間スコアを調整した回帰を当てはめて、9.7 ± 0.6 の推定値を得ることができます。
> 次に、受信確率が異なる不均衡な割り当てメカニズムを検討します。
> 治療は中間スコアに依存します: Pr(z = 1) = logit−1((x −50)/10)。図 9a は、
> 200 人の学生に対する模擬治療割り当てと図 9a は模擬試験を示しています。

### 熟語・専門語

- **ESS**: 有効サンプルサイズ。自己相関を考慮した独立サンプル相当数。

### 要約

- あるいは、中間スコアを調整した回帰を当てはめて、9.7 ± 0.6 の推定値を得ることができます。

## Chunk 0214

### English（抽出4行）

> scores. The underlying regression lines are the same as before, as this simulation changes the
> distribution of z but not the model for y|x, z. Under this design, the treatment is preferentially
> given to the less well-performing students, hence a simple comparison of ﬁnal exam scores will
> give a poor estimate. For this particular simulation, the diﬀerence in average grades comparing the

### 日本語訳（自動翻訳）

> 得点。このシミュレーションでは、
> z の分布ではなく、y|x, z のモデルではありません。この設計では、処理が優先されます。
> 成績の悪い生徒に与えられるため、最終試験の得点を単純に比較すると、
> 悪い見積もりを出します。この特定のシミュレーションでは、次の結果を比較した平均成績の差は、

### 熟語・専門語

- **ESS**: 有効サンプルサイズ。自己相関を考慮した独立サンプル相当数。

### 要約

- 得点。

## Chunk 0215

### English（抽出4行）

> two groups is −13.8 ± 1.5, a terrible inference given that the true eﬀect is, by construction, 10.
> In this case, though, the linear regression adjusting for x recovers the treatment eﬀect, yielding an
> estimate of 9.7 ± 0.8.
> But this new estimate is sensitive to the functional form of the adjustment for x. We can see this

### 日本語訳（自動翻訳）

> 2 つのグループは -13.8 ± 1.5 であり、真の効果が構造的に 10 であることを考えると、ひどい推論です。
> ただし、この場合、x を調整した線形回帰により治療効果が回復し、次の結果が得られます。
> 推定値は 9.7 ± 0.8 です。
> しかし、この新しい推定値は、x の調整の関数形式に影響されます。これがわかります

### 熟語・専門語

- **ESS**: 有効サンプルサイズ。自己相関を考慮した独立サンプル相当数。

### 要約

- 2 つのグループは -13.8 ± 1.5 であり、真の効果が構造的に 10 であることを考えると、ひどい推論です。

## Chunk 0216

### English（抽出4行）

> by simulating data from an alternative model in which the true treatment eﬀect is 10 but the function
> E(y|x, z) is no longer linear. In this case we construct such a model by drawing the midterm exam
> score given true ability from normal(ηi, 10) as before, but transforming the ﬁnal ﬁnal exam score,
> as displayed in Figure 10. We again consider two hypothetical experiments: Figure 10a shows

### 日本語訳（自動翻訳）

> 真の治療効果が 10 であるが関数が 10 である代替モデルからのデータをシミュレートすることによって
> E(y|x, z) はもはや線形ではありません。この場合、中間試験を描画することによってそのようなモデルを構築します。
> 前と同様に通常(ηi, 10)から真の能力を与えられたスコアを計算しますが、最終的な期末試験のスコアを変換します。
> 図 10 に示すように、もう一度 2 つの仮説実験を検討します。図 10a は次のとおりです。

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- 真の治療効果が 10 であるが関数が 10 である代替モデルからのデータをシミュレートすることによって E(y|x, z) はもはや線形ではありません。

## Chunk 0217

### English（抽出4行）

> data from the completely randomized assignment, and Figure 10b displays the result using the
> unbalanced treatment assignment rule from Figure 9a. Both graphs show the underlying regression
> curves as well.
> What happens when we now ﬁt a linear regression to estimate the treatment eﬀect? The estimate

### 日本語訳（自動翻訳）

> 完全にランダム化された割り当てからのデータ。図 10b は、
> 図 9a の不均衡な治療割り当てルール。両方のグラフは基礎となる回帰を示しています
> 曲線も同様に。
> 治療効果を推定するために線形回帰を当てはめるとどうなるでしょうか?見積もり

### 熟語・専門語

- **ESS**: 有効サンプルサイズ。自己相関を考慮した独立サンプル相当数。

### 要約

- 完全にランダム化された割り当てからのデータ。

## Chunk 0218

### English（抽出4行）

> from the design in Figure 10a is reasonable: even though the linear model is wrong and thus the
> resulting estimate is not fully statistically eﬃcient, the balance in the design ensures that on average
> the speciﬁcation errors will cancel, and the estimate is 10.5 ± 0.8. But the unbalanced design has
> problems: even after adjusting for x in the linear regression, the estimate is 7.3 ± 0.9.

### 日本語訳（自動翻訳）

> 図 10a の設計からの結果は合理的です。線形モデルが間違っているため、
> 結果として得られる推定値は完全に統計的に効率的ではありませんが、設計のバランスにより、平均して
> 仕様の誤差は相殺され、推定値は 10.5 ± 0.8 になります。しかし、そのアンバランスなデザインは、
> 問題: 線形回帰で x を調整した後でも、推定値は 7.3 ± 0.9 です。

### 熟語・専門語

- **ESS**: 有効サンプルサイズ。自己相関を考慮した独立サンプル相当数。

### 要約

- 図 10a の設計からの結果は合理的です。

## Chunk 0219

### English（抽出4行）

> Nonlinear model, balanced assignment
> Midterm exam score
> Final exam score
> Nonlinear model, unbalanced assignment

### 日本語訳（自動翻訳）

> 非線形モデル、バランスの取れた割り当て
> 中間試験の得点
> 最終試験のスコア
> 非線形モデル、不均衡な割り当て

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- 非線形モデル、バランスの取れた割り当て 中間試験の得点 最終試験のスコア 非線形モデル、不均衡な割り当て

## Chunk 0220

### English（抽出4行）

> Midterm exam score
> Final exam score
> Figure 10: Again comparing two diﬀerent treatment assignments, this time in a setting where the
> relation between ﬁnal and midterm exam scores is nonlinear.

### 日本語訳（自動翻訳）

> 中間試験の得点
> 最終試験のスコア
> 図 10: 2 つの異なる治療割り当てを再度比較します。今回は、
> 期末試験の得点と中間試験の得点の関係は非線形です。

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- 中間試験の得点 最終試験のスコア 図 10: 2 つの異なる治療割り当てを再度比較します。

## Chunk 0221

### English（抽出4行）

> In the context of the present article, the point of this example is to demonstrate how simulation of
> a statistical system under diﬀerent conditions can give us insight, not just about computational issues
> but also about data and inference more generally. One could go further in this particular example
> by considering varying treatment eﬀects, selection on unobservables, and other complications, and

### 日本語訳（自動翻訳）

> この記事の文脈において、この例のポイントは、次のシミュレーションがどのように行われるかを示すことです。
> さまざまな条件下での統計システムは、計算の問題だけでなく洞察を与えてくれます
> だけでなく、より一般的なデータと推論についても同様です。この特定の例ではさらに詳しく進めることができます
> さまざまな治療効果、観察できないもの、その他の合併症の選択を考慮して、

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- この記事の文脈において、この例のポイントは、次のシミュレーションがどのように行われるかを示すことです。

## Chunk 0222

### English（抽出4行）

> this is generally true that such theoretical explorations can be considered indeﬁnitely to address
> whatever concerns might arise.
> 5.
> Addressing computational problems

### 日本語訳（自動翻訳）

> これは一般に真実であり、そのような理論的探求は無限に解決できると考えられます。
> どのような懸念が生じても。
> 5.
> 計算上の問題に対処する

### 熟語・専門語

- **ESS**: 有効サンプルサイズ。自己相関を考慮した独立サンプル相当数。

### 要約

- これは一般に真実であり、そのような理論的探求は無限に解決できると考えられます。

## Chunk 0223

### English（抽出4行）

> 5.1.
> The folk theorem of statistical computing
> When you have computational problems, often there’s a problem with your model (Yao, Vehtari,
> and Gelman, 2020). Not always—sometimes you will have a model that is legitimately diﬃcult to

### 日本語訳（自動翻訳）

> 5.1.
> 統計計算の民間定理
> 計算上の問題がある場合、多くの場合、モデル (Yao、Vehtari、
> およびゲルマン、2020)。常にそうとは限りません。場合によっては、モデルが正当に困難である場合もあります。

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- 5.1. 統計計算の民間定理 計算上の問題がある場合、多くの場合、モデル (Yao、Vehtari、 およびゲルマン、2020)。

## Chunk 0224

### English（抽出4行）

> ﬁt—but many cases of poor convergence correspond to regions of parameter space that are not of
> substantive interest or even to a nonsensical model. An example of pathologies in irrelevant regions
> of parameter space is given in Figure 6. Examples of fundamentally problematic models would be
> bugs in code or using a Gaussian-distributed varying intercept for each individual observation in a

### 日本語訳（自動翻訳）

> フィットしますが、収束が不十分な多くのケースは、パラメータ空間の領域が一致していません。
> 実質的な関心、あるいは無意味なモデルにさえ。無関係な領域の病状の例
> パラメータ空間の例を図 6 に示します。根本的に問題のあるモデルの例は次のとおりです。
> コード内のバグ、またはガウス分布の可変切片を個々の観測ごとに使用する

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- フィットしますが、収束が不十分な多くのケースは、パラメータ空間の領域が一致していません。

## Chunk 0225

### English（抽出4行）

> Gaussian or logistic regression context, where they cannot be informed by data. Our ﬁrst instinct
> when faced with a problematic model should not be to throw more computational resources on
> the model (e.g., by running the sampler for more iterations or reducing the step size of the HMC
> algorithm), but to check whether our model contains some substantive pathology.

### 日本語訳（自動翻訳）

> データから情報を得ることができないガウス回帰またはロジスティック回帰コンテキスト。私たちの最初の本能
> 問題のあるモデルに直面した場合、これ以上の計算リソースを投入すべきではありません。
> モデル (例: サンプラーをさらに反復実行するか、HMC のステップ サイズを減らすことによって)
> アルゴリズム）を使用しますが、モデルに重大な病理が含まれているかどうかを確認するためです。

### 熟語・専門語

- **ESS**: 有効サンプルサイズ。自己相関を考慮した独立サンプル相当数。

### 要約

- データから情報を得ることができないガウス回帰またはロジスティック回帰コンテキスト。

## Chunk 0226

### English（抽出4行）

> 5.2.
> Starting at simple and complex models and meeting in the middle
> Figure 11 illustrates a commonly useful approach to debugging. The starting point is that a model
> is not performing well, possibly not converging or being able to reproduce the true parameter

### 日本語訳（自動翻訳）

> 5.2.
> 単純なモデルと複雑なモデルから始めて途中で出会う
> 図 11 は、デバッグに一般的に役立つアプローチを示しています。出発点はモデルです
> パフォーマンスが悪く、収束していないか、真のパラメータを再現できない可能性があります

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- 5.2. 単純なモデルと複雑なモデルから始めて途中で出会う 図 11 は、デバッグに一般的に役立つアプローチを示しています。

## Chunk 0227

### English（抽出4行）

> values in fake-data simulation, or not ﬁtting the data well, or yielding unreasonable inferences.
> The path toward diagnosing the problem is to move from two directions: to gradually simplify the
> Figure 11: Diagram of advice for debugging. The asterisk on the lower right represents the scenario
> in which problems arise when trying to ﬁt the desired complex model. The dots on the upper left

### 日本語訳（自動翻訳）

> 偽のデータのシミュレーションで値が変化したり、データがうまく適合しなかったり、不合理な推論が生じたりする可能性があります。
> 問題を診断するための道は、2 つの方向から進むことです。1 つは段階的に単純化することです。
> 図 11: デバッグのためのアドバイスの図。右下のアスタリスクはシナリオを表します
> 目的の複雑なモデルを当てはめようとすると問題が発生します。左上の点々

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- 偽のデータのシミュレーションで値が変化したり、データがうまく適合しなかったり、不合理な推論が生じたりする可能性があります。

## Chunk 0228

### English（抽出4行）

> represent successes at ﬁtting various simple versions, and the dots on the lower right represent
> failures at ﬁtting various simpliﬁcations of the full model. The dotted line represents the idea
> that the problems can be identiﬁed somewhere between the simple models that ﬁt and the complex
> models that don’t. From Gelman and Hill (2007).

### 日本語訳（自動翻訳）

> はさまざまな単純なバージョンの適合が成功したことを表し、右下の点は
> 完全なモデルのさまざまな単純化を当てはめる際の失敗。点線はアイデアを表します
> 問題は適合する単純なモデルと複雑なモデルの間のどこかで特定できるということ
> そうでないモデル。ゲルマンとヒル（2007）より。

### 熟語・専門語

- **ESS**: 有効サンプルサイズ。自己相関を考慮した独立サンプル相当数。

### 要約

- はさまざまな単純なバージョンの適合が成功したことを表し、右下の点は 完全なモデルのさまざまな単純化を当てはめる際の失敗。

## Chunk 0229

### English（抽出4行）

> poorly-performing model, stripping it down until you get something that works; and from the other
> direction starting with a simple and well-understood model and gradually adding features until the
> problem appears. Similarly, if the model has multiple components (e.g., a diﬀerential equation and
> a linear predictor for parameters of the equation), it is usually sensible to perform a sort of unit test

### 日本語訳（自動翻訳）

> パフォーマンスの低いモデルは、機能するものが得られるまで削除します。そして相手からも
> シンプルでわかりやすいモデルから始めて、段階的に機能を追加していき、
> という問題が現れます。同様に、モデルに複数のコンポーネント (例: 微分方程式と
> 方程式のパラメータの線形予測子)、通常は一種の単体テストを実行することが賢明です

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- パフォーマンスの低いモデルは、機能するものが得られるまで削除します。

## Chunk 0230

### English（抽出4行）

> by ﬁrst making sure each component can be ﬁt separately, using simulated data.
> We may never end up ﬁtting the complex model we had intended to ﬁt at ﬁrst, either because
> it was too diﬃcult to ﬁt using currently available computational algorithms, or because existing
> data and prior information are not informative enough to allow useful inferences from the model,

### 日本語訳（自動翻訳）

> まず、シミュレートされたデータを使用して、各コンポーネントが個別に適合できることを確認します。
> 最初に当てはめるつもりだった複雑なモデルを結局当てはめることができない可能性もあります。
> 現在利用可能な計算アルゴリズムを使用して適合させるのは難しすぎた、または既存の
> データと以前の情報は、モデルから有用な推論を可能にするほど十分な情報を提供していません。

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- まず、シミュレートされたデータを使用して、各コンポーネントが個別に適合できることを確認します。

## Chunk 0231

### English（抽出4行）

> or simply because the process of model exploration lead us in a diﬀerent direction than we had
> originally planned.
> 5.3.
> Getting a handle on models that take a long time to fit

### 日本語訳（自動翻訳）

> あるいは単にモデル探索のプロセスが私たちをこれまでとは異なる方向に導いたからです
> 当初の予定。
> 5.3.
> 適合に時間がかかるモデルを把握する

### 熟語・専門語

- **ESS**: 有効サンプルサイズ。自己相関を考慮した独立サンプル相当数。

### 要約

- あるいは単にモデル探索のプロセスが私たちをこれまでとは異なる方向に導いたからです 当初の予定。

## Chunk 0232

### English（抽出4行）

> We generally ﬁt our models using HMC, which can run slowly for various reasons, including expen-
> sive gradient evaluations as in diﬀerential equation models, high dimensionality of the parameter
> space, or a posterior geometry in which HMC steps that are eﬃcient in one part of the space are
> too large or too small in other regions of the posterior distribution. Slow computation is often a

### 日本語訳（自動翻訳）

> 通常、HMC を使用してモデルを適合させますが、費用などのさまざまな理由で実行が遅くなることがあります。
> 微分方程式モデルのような高度な勾配評価、パラメータの高次元性
> 空間、または空間の一部で効率的な HMC ステップが配置される事後幾何学
> 事後分布の他の領域では大きすぎるか小さすぎます。計算が遅いのは、多くの場合、

### 熟語・専門語

- **posterior distribution**: 事後分布。データ観測後の未知量の不確実性を表す分布。

### 要約

- 通常、HMC を使用してモデルを適合させますが、費用などのさまざまな理由で実行が遅くなることがあります。

## Chunk 0233

### English（抽出4行）

> sign of other problems, as it indicates a poorly-performing HMC. However the very fact that the ﬁt
> takes long means the model is harder to debug.
> For example, we recently received a query in the Stan users group regarding a multilevel logistic
> regression with 35,000 data points, 14 predictors, and 9 batches of varying intercepts, which failed

### 日本語訳（自動翻訳）

> これは HMC のパフォーマンスが低下していることを示しているため、他の問題の兆候です。しかし、フィット感そのものが
> 時間がかかるということは、モデルのデバッグが困難であることを意味します。
> たとえば、最近、Stan ユーザー グループからマルチレベル ロジスティックスに関する問い合わせを受けました。
> 35,000 のデータ ポイント、14 の予測子、およびさまざまな切片の 9 バッチを使用した回帰 (失敗しました)

### 熟語・専門語

- **ESS**: 有効サンプルサイズ。自己相関を考慮した独立サンプル相当数。

### 要約

- これは HMC のパフォーマンスが低下していることを示しているため、他の問題の兆候です。

## Chunk 0234

### English（抽出4行）

> to ﬁnish running after several hours in Stan using default settings from rstanarm.
> We gave the following suggestions, in no particular order:
> • Simulate fake data from the model and try ﬁtting the model to the fake data (Section 4.1).
> Frequently a badly speciﬁed model is slow, and working with simulated data allows us not to

### 日本語訳（自動翻訳）

> rstanarm のデフォルト設定を使用して、Stan で数時間後に実行を終了します。
> 私たちは、順不同で次の提案を行いました。
> • モデルから偽のデータをシミュレートし、モデルを偽のデータに当てはめてみます (セクション 4.1)。
> 多くの場合、不適切に指定されたモデルは遅くなり、シミュレートされたデータを使用すると、

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- rstanarm のデフォルト設定を使用して、Stan で数時間後に実行を終了します。

## Chunk 0235

### English（抽出4行）

> worry about lack of ﬁt.
> • Since the big model is too slow, you should start with a smaller model and build up from there.
> First ﬁt the model with no varying intercepts. Then add one batch of varying intercepts, then
> the next, and so forth.

### 日本語訳（自動翻訳）

> フィット感のなさが心配。
> • 大きなモデルは遅すぎるため、小さなモデルから始めて、そこから構築していく必要があります。
> まず、切片を変化させずにモデルを近似します。次に、さまざまな切片の 1 つのバッチを追加し、
> 次、というように。

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- フィット感のなさが心配。

## Chunk 0236

### English（抽出4行）

> • Run for 200 iterations, rather than the default (at the time of this writing). Eventually you can
> run for 2000 iterations, but there is no point in doing that while you’re still trying to ﬁgure
> out what’s going on. If, after 200 iterations, bR is large, you can run longer, but there is no
> need to start with 2000.

### 日本語訳（自動翻訳）

> • デフォルト (この記事の執筆時点) ではなく、200 回反復して実行します。最終的にはできるようになります
> 2000 回の反復を実行しますが、まだ考えている間にそれを実行しても意味がありません。
> 何が起こっているのかを明らかにします。 200 回の反復後、bR が大きい場合は、より長く実行できますが、
> 2000 から始める必要があります。

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- • デフォルト (この記事の執筆時点) ではなく、200 回反復して実行します。

## Chunk 0237

### English（抽出4行）

> • Put at least moderately informative priors on the regression coeﬃcients and group-level
> variance parameters (Section 7.3).
> • Consider some interactions of the group-level predictors. It seems strange to have an additive
> model with 14 terms and no interactions. This suggestion may seem irrelevant to the user’s

### 日本語訳（自動翻訳）

> • 回帰係数とグループレベルに少なくとも適度に有益な事前分布を置く
> 分散パラメータ (セクション 7.3)。
> • グループレベルの予測変数の相互作用をいくつか考えてみましょう。添加物が入っているのは不思議な気がします
> 14 項を持ち交互作用のないモデル。この提案はユーザーの意見とは無関係に見えるかもしれません。

### 熟語・専門語

- **ESS**: 有効サンプルサイズ。自己相関を考慮した独立サンプル相当数。

### 要約

- • 回帰係数とグループレベルに少なくとも適度に有益な事前分布を置く 分散パラメータ (セクション 7.3)。

## Chunk 0238

### English（抽出4行）

> concern about speed—indeed, adding interactions should only increase run time—but it
> is a reminder that ultimately the goal is to make predictions or learn something about the
> underlying process, not merely to get some arbitrary pre-chosen model to converge.
> • Fit the model on a subset of your data. Again, this is part of the general advice to understand

### 日本語訳（自動翻訳）

> 速度については懸念があります。実際、インタラクションを追加すると実行時間が増加するだけです。しかし、
> 最終的な目標は、予測を行ったり、それについて何かを学ぶことであることを思い出させてくれます。
> 単に任意の事前に選択されたモデルを収束させるためだけではなく、基礎となるプロセスに影響を与えます。
> • データのサブセットにモデルを当てはめます。繰り返しになりますが、これは理解するための一般的なアドバイスの一部です。

### 熟語・専門語

- **ESS**: 有効サンプルサイズ。自己相関を考慮した独立サンプル相当数。
- **prediction**: 予測。未知/将来/除外データに対する分布や点推定。

### 要約

- 速度については懸念があります。

## Chunk 0239

### English（抽出4行）

> the ﬁtting process and get it to work well, before throwing the model at all the data.
> The common theme in all these tips is to think of any particular model choice as provisional, and to
> recognize that data analysis requires many models to be ﬁt in order to gain control over the process
> of computation and inference for a particular applied problem.

### 日本語訳（自動翻訳）

> モデルにすべてのデータを投入する前に、フィッティング プロセスを実行してうまく機能するようにしてください。
> これらすべてのヒントに共通するテーマは、特定のモデルの選択を暫定的なものと考え、次のことを行うことです。
> データ分析では、プロセスを制御するために多くのモデルを適合させる必要があることを認識する
> 特定の応用問題に対する計算と推論。

### 熟語・専門語

- **ESS**: 有効サンプルサイズ。自己相関を考慮した独立サンプル相当数。

### 要約

- モデルにすべてのデータを投入する前に、フィッティング プロセスを実行してうまく機能するようにしてください。

## Chunk 0240

### English（抽出4行）

> 5.4.
> Monitoring intermediate quantities
> Another useful approach to diagnosing model issues is to save intermediate quantities in our
> computations and plot them along with other MCMC output, for example using bayesplot (Gabry

### 日本語訳（自動翻訳）

> 5.4.
> 中間量のモニタリング
> モデルの問題を診断するためのもう 1 つの有用なアプローチは、中間数量を
> たとえば、bayesplot を使用して、計算を他の MCMC 出力とともにプロットします (Gabry

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- 5.4. 中間量のモニタリング モデルの問題を診断するためのもう 1 つの有用なアプローチは、中間数量を たとえば、bayesplot を使用して、計算を他の MCMC 出力とともにプロットします (Gabry

## Chunk 0241

### English（抽出4行）

> et al., 2020a) or ArviZ (Kumar et al., 2019). These displays are an alternative to inserting print
> statements inside the code. In our experience, we typically learn more from a visualization than
> from a stream of numbers in the console.
> One problem that sometimes arises is chains getting stuck in out-of-the-way places in parameter

### 日本語訳（自動翻訳）

> et al.、2020a) または ArviZ (Kumar et al.、2019)。これらの表示は、印刷物を挿入する代わりに使用できます。
> コード内のステートメント。私たちの経験では、通常、ビジュアライゼーションからより多くのことを学びます。
> コンソール内の一連の数字から。
> 時々発生する問題の 1 つは、パラメータ内の邪魔にならない場所にチェーンが引っかかってしまうことです。

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- et al.、2020a) または ArviZ (Kumar et al.、2019)。

## Chunk 0242

### English（抽出4行）

> space where the posterior density is very low and where it can be baﬄing why the MCMC algorithm
> does not drift back toward the region where the log posterior density is near its expectation and
> where most of the posterior mass is. Here it can be helpful to look at predictions from the model
> given these parameter values to understand what is going wrong, as we illustrate in Section 11. But

### 日本語訳（自動翻訳）

> 事後密度が非常に低く、なぜ MCMC アルゴリズムを使用するのかを妨げる可能性がある空間
> 対数事後密度が予想に近い領域に向かってドリフトバックすることはなく、
> 後部塊の大部分が存在する場所。ここで、モデルからの予測を確認すると役立ちます。
> セクション 11 で説明するように、これらのパラメータ値を指定すると、何が問題なのかを理解できます。

### 熟語・専門語

- **prediction**: 予測。未知/将来/除外データに対する分布や点推定。

### 要約

- 事後密度が非常に低く、なぜ MCMC アルゴリズムを使用するのかを妨げる可能性がある空間 対数事後密度が予想に近い領域に向かってドリフトバックすることはなく、 後部塊の大部分が存在する場所。

## Chunk 0243

### English（抽出4行）

> the most direct approach is to plot the expected data conditional on the parameter values in these
> stuck chains, and then to transform the gradient of the parameters to the gradient of the expected
> data. This should give some insight as to how the parameters map to expected data in the relevant
> regions of the posterior distribution.

### 日本語訳（自動翻訳）

> 最も直接的なアプローチは、これらのパラメータ値を条件として予想されるデータをプロットすることです。
> スタックしたチェーンを作成し、パラメータの勾配を予想される勾配に変換します。
> データ。これにより、パラメータが関連する予測データにどのようにマッピングされるかについてある程度の洞察が得られるはずです。
> 事後分布の領域。

### 熟語・専門語

- **posterior distribution**: 事後分布。データ観測後の未知量の不確実性を表す分布。

### 要約

- 最も直接的なアプローチは、これらのパラメータ値を条件として予想されるデータをプロットすることです。

## Chunk 0244

### English（抽出4行）

> 5.5.
> Stacking to reweight poorly mixing chains
> In practice, often our MCMC algorithms mix just ﬁne. Other times, the simulations quickly move
> to unreasonable areas of parameter space, indicating the possibility of model misspeciﬁcation,

### 日本語訳（自動翻訳）

> 5.5.
> 混合が不十分なチェーンの重みを再調整するためのスタッキング
> 実際には、多くの場合、MCMC アルゴリズムは適切に混合されます。また、シミュレーションが急速に進む場合もあります。
> パラメータ空間の不合理な領域に影響を及ぼし、モデルの仕様ミスの可能性を示します。

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- 5.5. 混合が不十分なチェーンの重みを再調整するためのスタッキング 実際には、多くの場合、MCMC アルゴリズムは適切に混合されます。

## Chunk 0245

### English（抽出4行）

> non-informative or weakly informative observations, or just diﬃcult geometry.
> But it is also common to be in an intermediate situation where multiple chains are slow to
> mix but they are in a generally reasonable range. In this case we can use stacking to combine
> the simulations, using cross validation to assign weights to the diﬀerent chains (Yao, Vehtari,

### 日本語訳（自動翻訳）

> 有益でない、またはあまり有益でない観察、または単に難しい幾何学。
> しかし、複数のチェーンの処理が遅いという中間的な状況に陥ることもよくあります。
> 混合していますが、それらは一般的に妥当な範囲内にあります。この場合、スタッキングを使用して結合できます。
> シミュレーションでは、相互検証を使用して異なるチェーン (Yao、Vehtari、

### 熟語・専門語

- **cross validation**: 交差検証。汎化性能を推定するためにデータを分割/近似除外する評価法。
- **validation**: 検証。モデルが目的・データ・外部知識に照らして妥当かを確認すること。

### 要約

- 有益でない、またはあまり有益でない観察、または単に難しい幾何学。

## Chunk 0246

### English（抽出4行）

> and Gelman, 2020). This will have the approximate eﬀect of discarding chains that are stuck in
> out-of-the-way low-probability modes of the target distribution. The result from stacking is not
> necessarily equivalent, even asymptotically, to fully Bayesian inference, but it serves many of the
> same goals, and is especially suitable during the model exploration phase, allowing us to move

### 日本語訳（自動翻訳）

> およびゲルマン、2020)。これは、詰まっているチェーンを破棄するのとほぼ同じ効果があります。
> ターゲット分布の邪魔にならない低確率モード。積み重ねの結果はそうではありません
> 漸近的であっても完全なベイズ推論と必然的に等価ですが、これは多くの機能に役立ちます。
> 同じ目標を達成しており、特にモデル探索フェーズに適しており、次のステップに進むことができます。

### 熟語・専門語

- **Bayesian inference**: ベイズ推論。事前分布と尤度から事後分布を計算する中核処理。
- **ESS**: 有効サンプルサイズ。自己相関を考慮した独立サンプル相当数。
- **approximate**: 近似。速度や扱いやすさのため、正確な推論・モデルを緩めること。

### 要約

- およびゲルマン、2020)。

## Chunk 0247

### English（抽出4行）

> forward and spend more time and energy in other part of Bayesian workﬂow without getting hung
> up on exactly ﬁtting one particular model. In addition, non-uniform stacking weights, when used
> in concert with traceplots and other diagnostic tools, can help us understand where to focus that
> eﬀort in an iterative way.

### 日本語訳（自動翻訳）

> ハングすることなく、ベイジアン ワークフローの他の部分により多くの時間とエネルギーを費やすことができます。
> 特定の 1 つのモデルに正確に適合することに取り組んでいます。さらに、使用時のスタッキング重量が不均一になります。
> トレースプロットや他の診断ツールと連携して、どこに焦点を当てるべきかを理解するのに役立ちます。
> 反復的な方法で努力します。

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- ハングすることなく、ベイジアン ワークフローの他の部分により多くの時間とエネルギーを費やすことができます。

## Chunk 0248

### English（抽出4行）

> 5.6.
> Posterior distributions with multimodality and other difficult geometry
> We can roughly distinguish four sorts of problems with MCMC related to multimodality and other
> diﬃcult posterior geometries:

### 日本語訳（自動翻訳）

> 5.6.
> 多峰性およびその他の困難な幾何学による事後分布
> MCMC では、マルチモダリティなどに関連する 4 種類の問題を大まかに区別できます。
> 難しい後部形状:

### 熟語・専門語

- **posterior distribution**: 事後分布。データ観測後の未知量の不確実性を表す分布。
- **multimodality**: 多峰性。事後分布に複数の山があり、MCMCが混合しにくい状態。

### 要約

- 5.6. 多峰性およびその他の困難な幾何学による事後分布 MCMC では、マルチモダリティなどに関連する 4 種類の問題を大まかに区別できます。

## Chunk 0249

### English（抽出4行）

> • Eﬀectively disjoint posterior volumes, where all but one of the modes have near-zero mass.
> An example appears in Section 11. In such problems, the minor modes can be avoided
> using judicious choices of initial values for the simulation, adding prior information or hard
> constraints for parameters or they can be pruned by approximately estimating the mass in

### 日本語訳（自動翻訳）

> • 1 つを除くすべてのモードの質量がゼロに近い、実質的に独立した後部ボリューム。
> 例はセクション 11 にあります。このような問題では、マイナー モードを回避できます。
> シミュレーションの初期値を賢明に選択し、事前情報を追加したり、ハードウェアを追加したりする
> パラメータの制約を使用するか、パラメータの質量を近似的に推定することで制約を取り除くことができます。

### 熟語・専門語

- **approximate**: 近似。速度や扱いやすさのため、正確な推論・モデルを緩めること。

### 要約

- • 1 つを除くすべてのモードの質量がゼロに近い、実質的に独立した後部ボリューム。

## Chunk 0250

### English（抽出4行）

> each mode.
> • Eﬀectively disjoint posterior volumes of high probability mass that are trivially symmetric,
> such as label switching in a mixture model. It is standard practice here to restrict the model
> in some way to identify the mode of interest; see for example Bafumi et al. (2005) and

### 日本語訳（自動翻訳）

> 各モード。
> • 自明の対称性を持つ、高確率の塊の後部ボリュームを効果的に分離し、
> 混合モデルでのラベル切り替えなど。ここではモデルを制限するのが標準的な方法です
> 何らかの方法で対象のモードを特定する。たとえば、Bafumi et al.を参照してください。 (2005) と

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

> ベタンクール (2017b)。
> • 異なる可能性の高い質量の後部ボリュームを効果的に分離します。たとえば
> 遺伝子制御のモデル (Modrák、2018) では、いくつかのデータは 2 つの異なる制御体制を認めています。
> 効果の符号は反対ですが、ゼロに近い効果は事後密度がはるかに低くなります。

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- ベタンクール (2017b)。

## Chunk 0252

### English（抽出4行）

> This problem is more challenging. In some settings, we can use stacking (predictive model
> averaging) as an approximate solution, recognizing that this is not completely general as
> it requires deﬁning a predictive quantity of interest. A more fully Bayesian alternative is
> to divide the model into pieces by introducing a strong mixture prior and then ﬁtting the

### 日本語訳（自動翻訳）

> この問題はさらに困難です。一部の設定では、スタッキング (予測モデル) を使用できます。
> 平均化）を近似解として使用しますが、これは完全に一般的ではないことを認識しています。
> 予測対象量を定義する必要があります。より完全なベイズ主義の代替案は次のとおりです。
> 事前に強力な混合物を導入してモデルを部分に分割し、その後、

### 熟語・専門語

- **approximate**: 近似。速度や扱いやすさのため、正確な推論・モデルを緩めること。

### 要約

- この問題はさらに困難です。

## Chunk 0253

### English（抽出4行）

> model separately given each of the components of the prior. Other times the problem can be
> addressed using strong priors that have the eﬀect of ruling out some of the possible modes.
> • A single posterior volume of high probability mass with an arithmetically unstable tail.
> If you initialize near the mass of the distribution, there should not be problems for most

### 日本語訳（自動翻訳）

> 事前のコンポーネントのそれぞれを個別に与えられたモデル。また、問題が発生する可能性があるのは、
> 考えられるモードの一部を除外する効果のある強力な事前確率を使用して対処します。
> • 算術的に不安定な尾部を持つ高確率質量の単一後部ボリューム。
> ディストリビューションの質量近くで初期化すれば、ほとんどの問題は発生しないはずです。

### 熟語・専門語

- **ESS**: 有効サンプルサイズ。自己相関を考慮した独立サンプル相当数。

### 要約

- 事前のコンポーネントのそれぞれを個別に与えられたモデル。

## Chunk 0254

### English（抽出4行）

> inferences. If there is particular interest in extremely rare events, then the problem should
> be reparameterized anyway, as there is a limit to what can be learned from the usual default
> eﬀective sample size of a few hundred to a few thousand.
> 5.7.

### 日本語訳（自動翻訳）

> 推論。非常にまれなイベントに特に関心がある場合、問題は次のようになります。
> 通常のデフォルトから学習できることには限界があるため、とにかく再パラメータ化する必要があります。
> 有効サンプルサイズは数百から数千です。
> 5.7.

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- 推論。

## Chunk 0255

### English（抽出4行）

> Reparameterization
> Generally, an HMC-based sampler will work best if its mass matrix is appropriately tuned and the
> geometry of the joint posterior distribution is relatively uninteresting, in that it has no sharp corners,
> cusps, or other irregularities. This is easily satisﬁed for many classical models, where results like

### 日本語訳（自動翻訳）

> 再パラメータ化
> 一般に、HMC ベースのサンプラーは、その質量マトリックスが適切に調整されており、
> 関節事後分布の幾何学的形状は、鋭い角がないため、比較的興味がありません。
> カスプ、またはその他の不規則性。これは多くの古典的なモデルでは容易に満たされ、次のような結果が得られます。

### 熟語・専門語

- **posterior distribution**: 事後分布。データ観測後の未知量の不確実性を表す分布。
- **reparameterization**: 再パラメータ化。計算しやすい幾何に変えるためのパラメータ表現変更。

### 要約

- 再パラメータ化 一般に、HMC ベースのサンプラーは、その質量マトリックスが適切に調整されており、 関節事後分布の幾何学的形状は、鋭い角がないため、比較的興味がありません。

## Chunk 0256

### English（抽出4行）

> the Bernstein-von Mises theorem suggest that the posterior will become fairly simple when there
> is enough data. Unfortunately, the moment a model becomes even slightly complex, we can no
> longer guarantee that we will have enough data to reach this asymptotic utopia (or, for that matter,
> that a Bernstein-von Mises theorem holds). For these models, the behavior of HMC can be greatly

### 日本語訳（自動翻訳）

> バーンスタイン・フォン・ミーゼスの定理は、次の場合に事後関数がかなり単純になることを示唆しています。
> 十分なデータです。残念ながら、モデルが少しでも複雑になった瞬間に、
> この漸近的なユートピアに到達するのに十分なデータが得られる保証が長くなります（さらに言えば、
> バーンスタイン・フォン・ミーゼスの定理が成り立つ）。これらのモデルの場合、HMC の動作は大きく変化する可能性があります。

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- バーンスタイン・フォン・ミーゼスの定理は、次の場合に事後関数がかなり単純になることを示唆しています。

## Chunk 0257

### English（抽出4行）

> improved by judiciously choosing a parameterization that makes the posterior geometry simpler.
> For example, hierarchical models can have diﬃcult funnel pathologies in the limit when group-
> level variance parameters approach zero (Neal, 2011), but in many such problems these computa-
> tional diﬃculties can be resolved using reparameterization, following the principles discussed by

### 日本語訳（自動翻訳）

> 事後ジオメトリをより単純にするパラメータ化を慎重に選択することで改善されました。
> たとえば、階層モデルでは、グループ化した場合、限界内で困難な漏斗病理が発生する可能性があります。
> レベル分散パラメーターはゼロに近づきます (Neal、2011) が、多くのそのような問題では、これらの計算は
> 問題は、で説明されている原則に従って、再パラメータ化を使用して解決できます。

### 熟語・専門語

- **reparameterization**: 再パラメータ化。計算しやすい幾何に変えるためのパラメータ表現変更。

### 要約

- 事後ジオメトリをより単純にするパラメータ化を慎重に選択することで改善されました。

## Chunk 0258

### English（抽出4行）

> Meng and van Dyk (2001); see also Betancourt and Girolami (2015).
> 5.8.
> Marginalization
> Challenging geometries in the posterior distribution are often due to interactions between param-

### 日本語訳（自動翻訳）

> メンとファン・ダイク (2001)。 Betancourt と Girolami (2015) も参照してください。
> 5.8.
> 疎外化
> 事後分布における困難なジオメトリは、パラメータ間の相互作用が原因であることがよくあります。

### 熟語・専門語

- **posterior distribution**: 事後分布。データ観測後の未知量の不確実性を表す分布。

### 要約

- メンとファン・ダイク (2001)。

## Chunk 0259

### English（抽出4行）

> eters. An example is the above-mentioned funnel shape, which we may observe when plotting the
> joint density of the group-level scale parameter, φ, and the individual-level mean, θ. By contrast,
> the marginal density of φ is well behaved. Hence we can eﬃciently draw MCMC samples from the
> marginal posterior,

### 日本語訳（自動翻訳）

> エーテル。例としては、前述の漏斗の形状が挙げられます。これは、
> グループレベルの尺度パラメーター φ と個人レベルの平均 θ の結合密度。対照的に、
> φ の限界密度は正常に動作します。したがって、MCMC サンプルを効率的に抽出できます。
> 後縁縁、

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- エーテル。

## Chunk 0260

### English（抽出4行）

> p(φ|y) =
> Z
> Θ
> p(φ, θ|y)dθ.

### 日本語訳（自動翻訳）

> p(φ|y) =
> Z
> Θ
> p(φ, θ|y)dθ。

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- p(φ|y) = Z Θ p(φ, θ|y)dθ。

## Chunk 0261

### English（抽出4行）

> To draw posterior draws with MCMC, Bayes’ rule teaches us we only need the marginal likelihood,
> p(y|φ). It is then possible to recover posterior draws for θ by doing exact sampling from the
> conditional distribution p(θ|φ, y), at a small computational cost. This marginalization strategy is
> notably used for Gaussian processes with a normal likelihood (e.g. Rasmussen and Williams, 2006,

### 日本語訳（自動翻訳）

> MCMC で事後引きを引くには、ベイズの法則は限界尤度のみが必要であることを教えてくれます。
> p(y|φ)。次に、
> 条件付き分布 p(θ|φ, y) を少ない計算コストで実現します。この疎外戦略は、
> 特に正規尤度のガウス過程に使用されます (例: Rasmussen and Williams, 2006,

### 熟語・専門語

- **likelihood**: 尤度。パラメータが与えられたときデータがどれだけ起こりやすいか。
- **ESS**: 有効サンプルサイズ。自己相関を考慮した独立サンプル相当数。
- **posterior draws**: 事後ドロー。事後分布から得たサンプル。

### 要約

- MCMC で事後引きを引くには、ベイズの法則は限界尤度のみが必要であることを教えてくれます。

## Chunk 0262

### English（抽出4行）

> Betancourt, 2020b).
> In general, the densities p(y|φ) and p(θ|φ, y) are not available to us. Exploiting the structure
> of the problem, we can approximate these distributions using a Laplace approximation, notably for
> latent Gaussian models (e.g., Tierney and Kadane, 1986, Rasmussen and Williams, 2006, Rue et

### 日本語訳（自動翻訳）

> ベタンコート、2020b)。
> 一般に、密度 p(y|φ) および p(θ|φ, y) は利用できません。構造を悪用する
> この問題に関しては、ラプラス近似を使用してこれらの分布を近似できます。特に
> 潜在ガウス モデル (例: Tierney and Kadane, 1986、Rasmussen and Williams, 2006、Rue et)

### 熟語・専門語

- **approximate**: 近似。速度や扱いやすさのため、正確な推論・モデルを緩めること。

### 要約

- ベタンコート、2020b)。

## Chunk 0263

### English（抽出4行）

> al., 2009, Margossian et al., 2020b). When coupled with HMC, this marginalization scheme can,
> depending on the cases, be more eﬀective than reparameterization, if sometimes at the cost of a
> bias; for a discussion on the topic, see Margossian et al. (2020a).
> 5.9.

### 日本語訳（自動翻訳）

> al.、2009、Margossian et al.、2020b）。この疎外スキームを HMC と組み合わせると、次のことが可能になります。
> 場合によっては、たとえコストがかかるとしても、再パラメータ化よりも効果的です。
> 偏見;このトピックに関する議論については、Margossian et al. を参照してください。 (2020a)。
> 5.9.

### 熟語・専門語

- **reparameterization**: 再パラメータ化。計算しやすい幾何に変えるためのパラメータ表現変更。

### 要約

- al.、2009、Margossian et al.、2020b）。

## Chunk 0264

### English（抽出4行）

> Adding prior information
> Often the problems in computation can be ﬁxed by including prior information that is already
> available but which had not yet been included in the model, for example, because prior elicitation
> from domain experts has substantial cost (O’Hagan et al., 2006, Sarma and Kay, 2020) and we

### 日本語訳（自動翻訳）

> 事前情報の追加
> 多くの場合、計算上の問題は、既に存在する事前情報を組み込むことで解決できます。
> 利用可能だがまだモデルに含まれていなかったもの。たとえば、事前の引き出しがあったため。
> ドメイン専門家からの情報提供にはかなりの費用がかかります (O’Hagan et al., 2006、Sarma and Kay, 2020)。

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- 事前情報の追加 多くの場合、計算上の問題は、既に存在する事前情報を組み込むことで解決できます。

## Chunk 0265

### English（抽出4行）

> started with some template model and prior (Section 2.1). In some cases, running for more iterations
> can also help. But many ﬁtting problems go away when reasonable prior information is added,
> which is not to say that the primary use of priors is to resolve ﬁtting problems.
> We may have assumed (or hoped) that the data would suﬃciently informative for all parts of the

### 日本語訳（自動翻訳）

> 一部のテンプレート モデル以前から始まりました (セクション 2.1)。場合によっては、さらに反復を実行する
> も役立ちます。しかし、適切な事前情報が追加されると、フィッティングの問題の多くは解決します。
> これは、事前分布の主な用途がフィッティングの問題を解決することであるということではありません。
> 私たちは、データがすべての部分について十分な情報を提供すると仮定した (または期待した) かもしれません。

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- 一部のテンプレート モデル以前から始まりました (セクション 2.1)。

## Chunk 0266

### English（抽出4行）

> model, but with careful inspection or as the byproduct of computational diagnostics, we may ﬁnd out
> 0.0
> 0.5
> 1.0

### 日本語訳（自動翻訳）

> モデルではありますが、注意深く検査するか、コンピューターによる診断の副産物として、次のことが判明する可能性があります。
> 0.0
> 0.5
> 1.0

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- モデルではありますが、注意深く検査するか、コンピューターによる診断の副産物として、次のことが判明する可能性があります。

## Chunk 0267

### English（抽出4行）

> 1.5
> 2.0
> y = (a1e−0.1x + a2e−2x) × error
> x

### 日本語訳（自動翻訳）

> 1.5
> 2.0
> y = (a1e−0.1x + a2e−2x) × 誤差
> ×

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- 1.5 2.0 y = (a1e−0.1x + a2e−2x) × 誤差 ×

## Chunk 0268

### English（抽出4行）

> y
> 0.0
> 1.0
> 2.0

### 日本語訳（自動翻訳）

> y
> 0.0
> 1.0
> 2.0

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- y 0.0 1.0 2.0

## Chunk 0269

### English（抽出4行）

> 3.0
> y = (a1e−0.1x + a2e−0.2x) × error
> x
> y

### 日本語訳（自動翻訳）

> 3.0
> y = (a1e−0.1x + a2e−0.2x) × 誤差
> ×
> y

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- 3.0 y = (a1e−0.1x + a2e−0.2x) × 誤差 × y

## Chunk 0270

### English（抽出4行）

> Figure 12: Simulated data from the model, y = (a1e−b1x + a2e−b2x) ∗error: (a) setting (b1, b2) =
> (0.1, 2.0), and (b) setting (b1, b2) = (0.1, 0.2). In addition, the dotted line in the second plot shows
> the curve, y = 1.8e−0.135x, which almost exactly coincides with the true curve over the range of
> these data. It was easy to ﬁt the model to the data in the left graph and recover the true parameter

### 日本語訳（自動翻訳）

> 図 12: モデルからのシミュレーション データ、y = (a1e−b1x + a2e−b2x) ∗誤差: (a) 設定 (b1, b2) =
> (0.1, 2.0)、(b) (b1, b2) = (0.1, 0.2) と設定します。さらに、2 番目のプロットの点線は、
> 曲線 y = 1.8e−0.135x は、次の範囲にわたって真の曲線とほぼ正確に一致します。
> これらのデータ。モデルを左側のグラフのデータに当てはめて、真のパラメータを復元するのは簡単でした。

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- 図 12: モデルからのシミュレーション データ、y = (a1e−b1x + a2e−b2x) ∗誤差: (a) 設定 (b1, b2) = (0.1, 2.0)、(b) (b1, b2) = (0.1, 0.2) と設定します。

## Chunk 0271

### English（抽出4行）

> values. For the data in the right graph, however, the observations did not provide information
> to reduce the uncertainty suﬃciently, and and the model could only be stably ﬁt using a prior
> distribution that provided that needed missing information.
> that this is not the case. In classical statistics, models are sometimes classiﬁed as identiﬁable or non-

### 日本語訳（自動翻訳）

> 価値観。ただし、右のグラフのデータについては、観測結果から情報は得られませんでした。
> 不確実性を十分に低減するには、事前のモデルを使用した場合にのみモデルを安定して適合させることができます
> 必要な欠落情報を提供する配布。
> そうではないということ。古典的な統計では、モデルは識別可能または識別不可能に分類されることがあります。

### 熟語・専門語

- **uncertainty**: 不確実性。観測・パラメータ・モデル構造・意思決定に残る曖昧さ。

### 要約

- 価値観。

## Chunk 0272

### English（抽出4行）

> identiﬁable, but this can be misleading (even after adding intermediate categories such as partial or
> weak identiﬁability), as the amount of information that can be learned from observations depends
> also on the speciﬁc realization of the data that was actually obtained. In addition, “identiﬁcation”
> is formally deﬁned in statistics as an asymptotic property, but in Bayesian inference we care about

### 日本語訳（自動翻訳）

> 識別可能ですが、これは誤解を招く可能性があります（部分的なカテゴリや、
> 識別可能性が低い）、観察から学習できる情報の量は依存するため
> 実際に得られたデータの具体的な実現についても説明します。また、「身分証明書」
> は統計学では漸近特性として正式に定義されていますが、ベイズ推論では次の点が考慮されます。

### 熟語・専門語

- **Bayesian inference**: ベイズ推論。事前分布と尤度から事後分布を計算する中核処理。

### 要約

- 識別可能ですが、これは誤解を招く可能性があります（部分的なカテゴリや、 識別可能性が低い）、観察から学習できる情報の量は依存するため 実際に得られたデータの具体的な実現についても説明します。

## Chunk 0273

### English（抽出4行）

> inference with ﬁnite data, especially given that our models often increase in size and complexity
> as more data are included into the analysis. Asymptotic results can supply some insight into ﬁnite-
> sample performance, but we generally prefer to consider the posterior distribution that is in front of
> us. Lindley (1956) and Goel and DeGroot (1981) discuss how to measure the information provided

### 日本語訳（自動翻訳）

> 有限データを使用した推論、特にモデルのサイズと複雑さが増大することが多いことを考慮すると
> より多くのデータが分析に含まれるためです。漸近的な結果は、有限に関する洞察を提供することができます。
> サンプルのパフォーマンスを考慮しますが、一般的には、前にある事後分布を考慮することを好みます。
> 私たち。 Lindley (1956) と Goel と DeGroot (1981) は、提供された情報を測定する方法について議論しています。

### 熟語・専門語

- **posterior distribution**: 事後分布。データ観測後の未知量の不確実性を表す分布。

### 要約

- 有限データを使用した推論、特にモデルのサイズと複雑さが増大することが多いことを考慮すると より多くのデータが分析に含まれるためです。

## Chunk 0274

### English（抽出4行）

> by an experiment as how diﬀerent the posterior is from the prior. If the data are not informative on
> some aspects of the model, we may improve the situation by providing more information via priors.
> Furthermore, we often prefer to use a model with parameters that can be updated by the information
> in the data instead of a model that may be closer to the truth but where data are not able to provide

### 日本語訳（自動翻訳）

> 事後が事前とどれだけ異なるかを実験によって調べます。データが有益でない場合は、
> モデルの一部の側面については、事前分布を通じてより多くの情報を提供することで状況を改善できる可能性があります。
> さらに、多くの場合、情報によって更新できるパラメーターを持つモデルを使用することを好みます。
> 真実に近いかもしれないがデータでは提供できないモデルの代わりにデータで

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- 事後が事前とどれだけ異なるかを実験によって調べます。

## Chunk 0275

### English（抽出4行）

> suﬃcient information. In Sections 6.2–6.3 we discuss tools for assessing the informativeness of
> individual data points or hyperparameters.
> We illustrate with the problem of estimating the sum of declining exponentials with unknown
> decay rates. This task is a well-known ill-conditioned problem in numerical analysis and also arises

### 日本語訳（自動翻訳）

> 十分な情報。セクション 6.2 ～ 6.3 では、情報の有益性を評価するためのツールについて説明します。
> 個々のデータポイントまたはハイパーパラメータ。
> 未知の指数関数の減少の合計を推定する問題で説明します。
> 減衰率。このタスクは数値解析におけるよく知られた悪条件問題であり、また、

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

> 薬理学などの用途に使用されます (Jacquez、1972)。データを想定します
> yi = (a1e−b1xi + a2e−b2xi) × eϵi、i = 1、...の場合。 。 。 、ん、
> 独立誤差 ϵi 〜normal(0, σ) あり。係数 a1、a2、および残差標準
> 偏差 σ は正になるように制約されます。パラメータ b1 と b2 も正です。これらは次のとおりです。

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- 薬理学などの用途に使用されます (Jacquez、1972)。

## Chunk 0277

### English（抽出4行）

> supposed to be declining, not increasing, exponentials—and are also constrained to be ordered,
> b1 < b2, so as to uniquely deﬁne the two model components.
> We start by simulating fake data from a model where the two curves should be cleanly distin-
> guished, setting b1 = 0.1 and b2 = 2.0, a factor of 20 apart in scale. We simulate 1000 data points

### 日本語訳（自動翻訳）

> 指数関数的に増加するのではなく、減少するはずです。また、順序付けされることも制約されています。
> b1 < b2 であり、2 つのモデル コンポーネントを一意に定義します。
> まず、2 つの曲線が明確に区別できるモデルから偽のデータをシミュレートします。
> b1 = 0.1 と b2 = 2.0 を設定し、スケールが 20 倍離れています。 1000 個のデータポイントをシミュレートします

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- 指数関数的に増加するのではなく、減少するはずです。

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
> −3 −2 −1 0 1 2 3 −3 −2 −1 0 1 2 3 −3 −2 −1 0 1 2 3

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- N = 1 N = 2 N = 8 −3 −2 −1 0 1 2 3 −3 −2 −1 0 1 2 3 −3 −2 −1 0 1 2 3

## Chunk 0279

### English（抽出4行）

> −2
> −1
> mu
> log(sigma)

### 日本語訳（自動翻訳）

> −2
> −1
> む
> ログ(シグマ)

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- −2 −1 む ログ(シグマ)

## Chunk 0280

### English（抽出4行）

> A
> N = 6
> N = 9
> N = 21

### 日本語訳（自動翻訳）

> あ
> N = 6
> N = 9
> N = 21

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- あ N = 6 N = 9 N = 21

## Chunk 0281

### English（抽出4行）

> 0.3
> 0.6
> 0.9
> 0.3

### 日本語訳（自動翻訳）

> 0.3
> 0.6
> 0.9
> 0.3

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- 0.3 0.6 0.9 0.3

## Chunk 0282

### English（抽出4行）

> 0.6
> 0.9
> 0.3
> 0.6

### 日本語訳（自動翻訳）

> 0.6
> 0.9
> 0.3
> 0.6

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- 0.6 0.9 0.3 0.6

## Chunk 0283

### English（抽出4行）

> 0.9
> −3
> −2
> −1

### 日本語訳（自動翻訳）

> 0.9
> −3
> −2
> −1

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- 0.9 −3 −2 −1

## Chunk 0284

### English（抽出4行）

> log(theta[1])
> log(sigma[1])
> B
> Figure 13: Example of how adding data changes the geometry of the posterior distribution. (A)

### 日本語訳（自動翻訳）

> ログ(θ[1])
> ログ(シグマ[1])
> B
> 図 13: データを追加すると事後分布の形状がどのように変化するかの例。 (A)

### 熟語・専門語

- **posterior distribution**: 事後分布。データ観測後の未知量の不確実性を表す分布。

### 要約

- ログ(θ[1]) ログ(シグマ[1]) B 図 13: データを追加すると事後分布の形状がどのように変化するかの例。

## Chunk 0285

### English（抽出4行）

> Normal likelihood as a function of mean µ and standard deviation σ with increasing number
> of available observations N drawn from the standard normal distribution.
> For N = 1 the
> likelihood increases without bounds and for N = 2 the geometry is still funnel-like which can

### 日本語訳（自動翻訳）

> 数値の増加に伴う平均μと標準偏差σの関数としての正規尤度
> 標準正規分布から抽出された利用可能な観測値 N の数。
> N = 1 の場合、
> 可能性は際限なく増加し、N = 2 の場合でもジオメトリは依然として漏斗状であるため、

### 熟語・専門語

- **likelihood**: 尤度。パラメータが与えられたときデータがどれだけ起こりやすいか。

### 要約

- 数値の増加に伴う平均μと標準偏差σの関数としての正規尤度 標準正規分布から抽出された利用可能な観測値 N の数。

## Chunk 0286

### English（抽出4行）

> cause computational problems.
> For N = 8 the funnel-like shape is mostly suppressed.
> (B)
> Practical example using an Lotka-Volterra model of population dynamics (8 parameters total) as

### 日本語訳（自動翻訳）

> 計算上の問題を引き起こす。
> N = 8 の場合、漏斗状の形状はほとんど抑制されます。
> (B)
> 人口動態のロトカ・ヴォルテラ モデル (合計 8 パラメータ) を次のように使用した実践例

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

> Carpenter (2018) で説明されており、描画された 2 つのパラメーターの事後サンプルの散布図を示しています。
> Stan でのモデルのフィッティングから。 6 つのデータ点のフィットは漏斗状の形状を示します。赤い点は
> サンプラーが困難なジオメトリに遭遇したことを示す発散遷移を示します。
> 結果は信頼できません。 Stan は、9 個のデータポイントを使用すると、モデルを当てはめることができるようになります。

### 熟語・専門語

- **divergent**: divergence。HMC/NUTSで幾何が悪く積分が破綻した警告。

### 要約

- Carpenter (2018) で説明されており、描画された 2 つのパラメーターの事後サンプルの散布図を示しています。

## Chunk 0288

### English（抽出4行）

> the slightly uneven geometry. The model is well behaved when ﬁt to 21 data points.
> where the predictor values x are uniformly spaced from 0 to 10, and, somewhat arbitrarily, set
> a1 = 1.0, a2 = 0.8, σ = 0.2. Figure 12a shows true curve and the simulated data. We then use Stan
> to ﬁt the model from the data. The simulations run smoothly and the posterior inference recovers

### 日本語訳（自動翻訳）

> わずかに凹凸のある幾何学形状。モデルは 21 個のデータポイントに適合すると適切に動作します。
> ここで、予測子の値 x は 0 から 10 まで均一に配置され、ある程度任意に設定されます。
> a1 = 1.0、a2 = 0.8、σ = 0.2。図 12a は、真の曲線とシミュレートされたデータを示しています。次にスタンを使用します
> データからモデルを当てはめます。シミュレーションはスムーズに実行され、事後推論が回復します

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- わずかに凹凸のある幾何学形状。

## Chunk 0289

### English（抽出4行）

> the ﬁve parameters of the model, which is no surprise given that the data have been simulated from
> the model we are ﬁtting.
> But now we make the problem slightly more diﬃcult. The model is still, by construction, true,
> but instead of setting (b1, b2) to (0.1, 2.0), we make them (0.1, 0.2), so now only a factor of 2

### 日本語訳（自動翻訳）

> モデルの 5 つのパラメーター。データが次からシミュレートされたものであることを考えると、これは驚くべきことではありません。
> 私たちが当てはめているモデル。
> しかし、ここでは問題を少し難しくしてみます。このモデルは構造的には依然として真実ですが、
> ただし、(b1, b2) を (0.1, 2.0) に設定する代わりに、(0.1, 0.2) にするので、係数は 2 だけになります。

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- モデルの 5 つのパラメーター。

## Chunk 0290

### English（抽出4行）

> separates the scales of the two declining exponentials. The simulated data are shown in Figure
> 12b. But now when we try to ﬁt the model in Stan, we get terrible convergence. The two declining
> exponentials have become very hard to tell apart, as we have indicated in the graph by also including
> the curve, y = 1.8e−0.135x, which is essentially impossible to distinguish from the true model given

### 日本語訳（自動翻訳）

> 2 つの減少する指数関数のスケールを分離します。シミュレーションされたデータを図に示します。
> 12b.しかし、Stan にモデルを当てはめようとすると、ひどい収束が生じます。衰退する二人
> グラフにも含めて示したように、指数関数を区別するのは非常に困難になっています。
> 曲線 y = 1.8e−0.135x は、与えられた真のモデルと区別することが本質的に不可能です。

### 熟語・専門語

- **ESS**: 有効サンプルサイズ。自己相関を考慮した独立サンプル相当数。

### 要約

- 2 つの減少する指数関数のスケールを分離します。

## Chunk 0291

### English（抽出4行）

> these data.
> We can make this computation more stable by adding prior information. For example, default
> normal(0, 1) priors on all the parameters does suﬃcient regularization, while still being weak if the
> model has been set up so the parameters are roughly on unit scale, as discussed in Section 2.3. In

### 日本語訳（自動翻訳）

> これらのデータ。
> 事前情報を追加することで、この計算をより安定させることができます。たとえば、デフォルト
> すべてのパラメータに対するnormal(0, 1)事前確率は十分な正則化を行いますが、
> セクション 2.3 で説明したように、モデルはパラメータがほぼ単位スケールになるように設定されています。で

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

> この場合、これが完了していると仮定します。後部の感度をチェックすることもできます
> Normal(0, 0.5) や Normal(0, 0.5) や
> Normal(0, 2) または、で説明したように、前のスケールに関して推論を微分することによって
> セクション6.3。

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- この場合、これが完了していると仮定します。

## Chunk 0293

### English（抽出4行）

> Using an informative normal distribution for the prior adds to the tail-log-concavity of the
> posterior density, which leads to a quicker MCMC mixing time. But the informative prior does
> not represent a tradeoﬀof model bias vs. computational eﬃciency; rather, in this case the model
> ﬁtting is improved as the computation burden is eased, an instance of the folk theorem discussed in

### 日本語訳（自動翻訳）

> 事前分布に有益な正規分布を使用すると、末尾の対数凹面が増加します。
> 事後密度が向上し、MCMC の混合時間が短縮されます。しかし、有益な事前情報は、
> モデルのバイアスと計算効率のトレードオフを表すものではありません。むしろ、この場合はモデル
> 計算負荷が軽減されるとフィッティングが向上します。これは、で説明したフォーク定理の例です。

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- 事前分布に有益な正規分布を使用すると、末尾の対数凹面が増加します。

## Chunk 0294

### English（抽出4行）

> Section 5.1. More generally, there can be strong priors with thick tails, and thus the tail behavior
> is not guaranteed to be more log concave. On the other hand, the prior can be weak in the context
> of the likelihood while still guaranteeing a log-concave tail. This is related to the point that the
> informativeness of a model depends on what questions are being asked.

### 日本語訳（自動翻訳）

> セクション5.1。より一般的には、太いテールを持つ強力な事前分布が存在する可能性があるため、テールの動作は
> ログ凹面が大きくなるという保証はありません。一方で、事前確率は状況によっては弱い場合があります。
> 対数凹状の尾部を保証しながら、可能性を推定します。という点に関係しますが、
> モデルの情報量は、どのような質問が行われているかによって異なります。

### 熟語・専門語

- **likelihood**: 尤度。パラメータが与えられたときデータがどれだけ起こりやすいか。
- **ESS**: 有効サンプルサイズ。自己相関を考慮した独立サンプル相当数。

### 要約

- セクション5.1。

## Chunk 0295

### English（抽出4行）

> Consider four steps on a ladder of abstraction:
> 1. Poor mixing of MCMC;
> 2. Diﬃcult geometry as a mathematical explanation for the above;
> 3. Weakly informative data for some parts of the model as a statistical explanation for the above;

### 日本語訳（自動翻訳）

> 抽象化のはしごの 4 つのステップを考えてみましょう。
> 1. MCMC の混合が不十分である。
> 2. 上記の数学的説明としての難しい幾何学。
> 3. 上記を統計的に説明するモデルの一部の情報が弱いデータ。

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- 抽象化のはしごの 4 つのステップを考えてみましょう。

## Chunk 0296

### English（抽出4行）

> 4. Substantive prior information as a solution to the above.
> Starting from the beginning of this ladder, we have computational troubleshooting; starting from
> the end, computational workﬂow.
> As another example, when trying to avoid the funnel pathologies of hierarchical models in the

### 日本語訳（自動翻訳）

> 4. 上記の解決策としての実質的な事前情報。
> このはしごの最初から計算によるトラブルシューティングを行っていきます。から始まる
> 最後に、計算ワークフローです。
> 別の例として、階層モデルのファネル病状を回避しようとする場合、

### 熟語・専門語

- **troubleshooting**: トラブルシュート。計算・モデル・データの失敗原因を切り分けること。

### 要約

- 4. 上記の解決策としての実質的な事前情報。

## Chunk 0297

### English（抽出4行）

> limit when group-level variance parameters approach zero, one could use zero-avoiding priors (for
> example, lognormal or inverse gamma distributions) to avoid the regions of high curvature of the
> likelihood; a related idea is discussed for penalized marginal likelihood estimation by Chung et al.
> (2013, 2014). Zero-avoiding priors can make sense when such prior information is available—such

### 日本語訳（自動翻訳）

> グループレベルの分散パラメータがゼロに近づくと、ゼロ回避事前分布を使用できるようになります（
> たとえば、対数正規分布や逆ガンマ分布など）、曲率の高い領域を避けるため、
> 可能性;関連するアイデアは、Chung らによるペナルティ付き周辺尤度推定について議論されています。
> (2013、2014)。ゼロ回避事前確率は、そのような事前情報が利用可能な場合に意味を持ちます。

### 熟語・専門語

- **likelihood**: 尤度。パラメータが与えられたときデータがどれだけ起こりやすいか。

### 要約

- グループレベルの分散パラメータがゼロに近づくと、ゼロ回避事前分布を使用できるようになります（ たとえば、対数正規分布や逆ガンマ分布など）、曲率の高い領域を避けるため、 可能性;関連するアイデアは、Chung らによるペナルティ付き周辺…

## Chunk 0298

### English（抽出4行）

> as for the length-scale parameter of a Gaussian process (Fuglstad et al., 2019)—but we want to be
> careful when using such a restriction merely to make the algorithm run faster. At the very least,
> if we use a restrictive prior to speed computation, we should make it clear that this is information
> being added to the model.

### 日本語訳（自動翻訳）

> ガウス過程の長さスケールパラメータについては (Fuglstad et al., 2019)、しかし我々はこうありたいと考えています。
> 単にアルゴリズムの実行を高速化するためにこのような制限を使用する場合は注意してください。少なくとも、
> 速度の計算の前に制限を使用する場合、これが情報であることを明確にする必要があります。
> モデルに追加中です。

### 熟語・専門語

- **ESS**: 有効サンプルサイズ。自己相関を考慮した独立サンプル相当数。

### 要約

- ガウス過程の長さスケールパラメータについては (Fuglstad et al., 2019)、しかし我々はこうありたいと考えています。

## Chunk 0299

### English（抽出4行）

> More generally, we have found that poor mixing of statistical ﬁtting algorithms can often be
> ﬁxed by stronger regularization. This does not come free, though: in order to eﬀectively regularize
> without blurring the very aspects of the model we want to estimate, we need some subject-
> matter knowledge—actual prior information. Haphazardly tweaking the model until computational

### 日本語訳（自動翻訳）

> より一般的には、統計的フィッティング アルゴリズムを適切に混合しないと、多くの場合、問題が発生する可能性があることがわかりました。
> より強力な正則化によって修正されました。ただし、これは無料ではありません。効果的に規則化するためです。
> 推定したいモデルのまさにその側面をぼかさずに、いくつかの主題が必要です。
> 事柄の知識 - 実際の事前情報。計算可能になるまでモデルを無計画に微調整する

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- より一般的には、統計的フィッティング アルゴリズムを適切に混合しないと、多くの場合、問題が発生する可能性があることがわかりました。

## Chunk 0300

### English（抽出4行）

> problems disappear is dangerous and can threaten the validity of inferences without there being a
> good way to diagnose the problem.
> 5.10.
> Adding data

### 日本語訳（自動翻訳）

> 問題が消えることは危険であり、問題がなければ推論の妥当性が脅かされる可能性があります。
> 問題を診断する良い方法です。
> 5.10.
> データの追加

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- 問題が消えることは危険であり、問題がなければ推論の妥当性が脅かされる可能性があります。

## Chunk 0301

### English（抽出4行）

> Similarly to adding prior information, one can constrain the model by adding new data sources
> that are handled within the model. For example, a calibration experiment can inform the standard
> deviation of a response.
> In other cases, models that are well behaved for larger datasets can have computational issues

### 日本語訳（自動翻訳）

> 以前の情報を追加するのと同様に、新しいデータ ソースを追加することでモデルを制約できます。
> モデル内で処理されます。たとえば、キャリブレーション実験により、標準の情報を得ることができます。
> 応答のずれ。
> 他のケースでは、大規模なデータセットに対して適切に動作するモデルでも計算上の問題が発生する可能性があります。

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- 以前の情報を追加するのと同様に、新しいデータ ソースを追加することでモデルを制約できます。

## Chunk 0302

### English（抽出4行）

> in small data regimes; Figure 13 shows an example. While the funnel-like shape of the posterior
> in such cases looks similar to the funnel in hierarchical models, this pathology is much harder to
> avoid, and we can often only acknowledge that the full model is not informed by the data and a
> simpler model needs to be used. Betancourt (2018) further discusses this issue.

### 日本語訳（自動翻訳）

> 小規模なデータ領域では。図 13 に例を示します。後部の漏斗状の形状ながら、
> このような場合、階層モデルの漏斗に似ていますが、この病理を特定するのははるかに困難です。
> 多くの場合、完全なモデルはデータと
> より単純なモデルを使用する必要があります。 Betancourt (2018) はこの問題についてさらに議論しています。

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- 小規模なデータ領域では。

## Chunk 0303

### English（抽出4行）

> 6.
> Evaluating and using a fitted model
> Once a model has been ﬁt, the workﬂow of evaluating that ﬁt is more convoluted, because there are
> many diﬀerent things that can be checked, and each of these checks can lead in many directions.

### 日本語訳（自動翻訳）

> 6.
> 適合モデルの評価と使用
> モデルが適合すると、その適合を評価するワークフローはさらに複雑になります。
> さまざまな項目をチェックでき、それぞれのチェックはさまざまな方向につながる可能性があります。

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- 6. 適合モデルの評価と使用 モデルが適合すると、その適合を評価するワークフローはさらに複雑になります。

## Chunk 0304

### English（抽出4行）

> Statistical models can be ﬁt with multiple goals in mind, and statistical methods are developed for
> diﬀerent groups of users. The aspects of a model that needs to be checked will depend on the
> application.
> 6.1.

### 日本語訳（自動翻訳）

> 統計モデルは複数の目標を念頭に置いて適合させることができ、統計手法は目的に合わせて開発されています。
> さまざまなユーザーのグループ。モデルのどの側面をチェックする必要があるかは、
> アプリケーション。
> 6.1.

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- 統計モデルは複数の目標を念頭に置いて適合させることができ、統計手法は目的に合わせて開発されています。

## Chunk 0305

### English（抽出4行）

> Posterior predictive checking
> Posterior predictive checking is analogous to prior predictive checking (Section 2.4), but the
> parameter draws used in the simulations come from the posterior distribution rather than the prior.
> While prior predictive checking is a way to understand a model and the implications of the speciﬁed

### 日本語訳（自動翻訳）

> 事後予測チェック
> 事後予測チェックは事前予測チェック (セクション 2.4) に似ていますが、
> シミュレーションで使用されるパラメータの描画は、事前分布ではなく事後分布から取得されます。
> 事前の予測チェックはモデルと指定されたものの影響を理解する方法です。

### 熟語・専門語

- **prior predictive**: 事前予測。データを見る前のpriorだけで生成される予測分布を確認する診断。
- **posterior predictive**: 事後予測。推定後のモデルが観測データの特徴を再現できるかを見る診断。
- **posterior distribution**: 事後分布。データ観測後の未知量の不確実性を表す分布。

### 要約

- 事後予測チェック 事後予測チェックは事前予測チェック (セクション 2.4) に似ていますが、 シミュレーションで使用されるパラメータの描画は、事前分布ではなく事後分布から取得されます。

## Chunk 0306

### English（抽出4行）

> priors, posterior predictive checking also allows one to examine the ﬁt of a model to real data (Box,
> 1980, Rubin, 1984, Gelman, Meng, and Stern, 1996).
> When comparing simulated datasets from the posterior predictive distribution to the actual
> dataset, if the dataset we are analyzing is unrepresentative of the posterior predictive distribution,

### 日本語訳（自動翻訳）

> 事前予測チェック、事後予測チェックにより、実際のデータに対するモデルの適合性を調べることもできます (ボックス、
> 1980 年、ルービン、1984 年、ゲルマン、メン、スターン、1996 年）。
> シミュレートされたデータセットを事後予測分布から実際のデータセットと比較する場合
> データセット、分析しているデータセットが事後予測分布を代表していない場合、

### 熟語・専門語

- **posterior predictive**: 事後予測。推定後のモデルが観測データの特徴を再現できるかを見る診断。

### 要約

- 事前予測チェック、事後予測チェックにより、実際のデータに対するモデルの適合性を調べることもできます (ボックス、 1980 年、ルービン、1984 年、ゲルマン、メン、スターン、1996 年）。

## Chunk 0307

### English（抽出4行）

> this indicates a failure of the model to describe an aspect of the data. The most direct checks compare
> the simulations from the predictive distribution to the full distribution of the data or a summary
> statistic computed from the data or subgroups of the data, especially for groupings not included in
> the model (see Figure 14). There is no general way to choose which checks one should perform on

### 日本語訳（自動翻訳）

> これは、モデルがデータの側面を記述するのに失敗していることを示します。最も直接的なチェックの比較
> 予測分布からデータまたはサマリーの完全な分布までのシミュレーション
> データまたはデータのサブグループから計算された統計、特にグループ化に含まれないもの
> モデル (図 14 を参照)。どのチェックを実行するかを選択する一般的な方法はありません

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- これは、モデルがデータの側面を記述するのに失敗していることを示します。

## Chunk 0308

### English（抽出4行）

> a model, but running a few such direct checks is a good safeguard against gross misspeciﬁcation.
> There is also no general way to decide when a check that fails requires adjustments to the model.
> Depending on the goals of the analysis and the costs and beneﬁts speciﬁc to the circumstances,
> we may tolerate that the model fails to capture certain aspects of the data or it may be essential to

### 日本語訳（自動翻訳）

> モデルではありますが、そのような直接チェックをいくつか実行することは、重大な仕様の誤りに対する適切な保護手段となります。
> また、チェックが失敗した場合にモデルの調整が必要になるかどうかを判断する一般的な方法もありません。
> 分析の目的と、状況に特有のコストと利点に応じて、
> モデルがデータの特定の側面をキャプチャできないことを許容する場合もあれば、それが不可欠である場合もあります。

### 熟語・専門語

- **ESS**: 有効サンプルサイズ。自己相関を考慮した独立サンプル相当数。

### 要約

- モデルではありますが、そのような直接チェックをいくつか実行することは、重大な仕様の誤りに対する適切な保護手段となります。

## Chunk 0309

### English（抽出4行）

> invest in improving the model. In general, we try to ﬁnd “severe tests” (Mayo, 2018): checks that
> are likely to fail if the model would give misleading answers to the questions we care most about.
> Figure 15 shows a more involved posterior predictive check from an applied project. This
> example demonstrates the way that predictive simulation can be combined with graphical display,

### 日本語訳（自動翻訳）

> モデルの改善に投資します。一般に、私たちは「厳しいテスト」 (Mayo、2018) を見つけようとします。
> 私たちが最も関心のある質問に対してモデルが誤解を招く答えを与える場合、このモデルは失敗する可能性が高くなります。
> 図 15 は、適用されたプロジェクトからのより複雑な事後予測チェックを示しています。これ
> この例は、予測シミュレーションをグラフィック表示と組み合わせる方法を示しています。

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

> また、予測チェックがしばしば必要になるという点で、実際的な課題も感じられます。
> 当面の特定の問題に合わせた独自のビジュアライゼーションを考案します。
> 6.2.
> 個々のデータポイントとデータのサブセットの相互検証と影響

### 熟語・専門語

- **cross validation**: 交差検証。汎化性能を推定するためにデータを分割/近似除外する評価法。
- **ESS**: 有効サンプルサイズ。自己相関を考慮した独立サンプル相当数。
- **validation**: 検証。モデルが目的・データ・外部知識に照らして妥当かを確認すること。

### 要約

- また、予測チェックがしばしば必要になるという点で、実際的な課題も感じられます。

## Chunk 0311

### English（抽出4行）

> Posterior predictive checking is often suﬃcient for revealing model misﬁt, but as it uses data both
> for model ﬁtting and misﬁt evaluation, it can be overly optimistic. In cross validation, part of the
> data is left out, the model is ﬁt to the remaining data, and predictive performance is checked on
> the left-out data. This improves predictive checking diagnostics, especially for ﬂexible models (for

### 日本語訳（自動翻訳）

> 事後予測チェックは、多くの場合、モデルの不適合を明らかにするのに十分ですが、データを使用するため、
> モデルの適合と不適合の評価に関しては、楽観的すぎる可能性があります。相互検証では、
> データは省略され、モデルは残りのデータに適合し、予測パフォーマンスがチェックされます。
> 取り残されたデータ。これにより、特に柔軟なモデル (

### 熟語・専門語

- **posterior predictive**: 事後予測。推定後のモデルが観測データの特徴を再現できるかを見る診断。
- **cross validation**: 交差検証。汎化性能を推定するためにデータを分割/近似除外する評価法。
- **validation**: 検証。モデルが目的・データ・外部知識に照らして妥当かを確認すること。

### 要約

- 事後予測チェックは、多くの場合、モデルの不適合を明らかにするのに十分ですが、データを使用するため、 モデルの適合と不適合の評価に関しては、楽観的すぎる可能性があります。

## Chunk 0312

### English（抽出4行）

> example, overparameterized models with more parameters than observations).
> Three diagnostic approaches using cross validation that we have found useful for further evalu-
> ating models are
> 1. calibration checks using the cross validation predictive distribution,

### 日本語訳（自動翻訳）

> たとえば、観測値よりも多くのパラメータを持つ過剰パラメータ化されたモデルなど）。
> さらなる評価に役立つことが判明した、相互検証を使用した 3 つの診断アプローチ
> 食べるモデルは
> 1. 相互検証予測分布を使用した校正チェック、

### 熟語・専門語

- **cross validation**: 交差検証。汎化性能を推定するためにデータを分割/近似除外する評価法。
- **validation**: 検証。モデルが目的・データ・外部知識に照らして妥当かを確認すること。

### 要約

- たとえば、観測値よりも多くのパラメータを持つ過剰パラメータ化されたモデルなど）。

## Chunk 0313

### English（抽出4行）

> 2. identifying which observations or groups of observations are most diﬃcult to predict,
> 3. identifying how inﬂuential particular observations are, that is, how much information they
> provide on top of other observations.
> In all three cases, eﬃcient approximations to leave-one-out cross-validation using importance

### 日本語訳（自動翻訳）

> 2. どの観測値または観測値のグループが予測するのが最も難しいかを特定する。
> 3. 特定の観察がどの程度影響を与えるか、つまり、どの程度の情報が含まれるかを特定する
> 他の観察に加えて提供します。
> 3 つのケースすべてにおいて、重要度を使用した 1 つ抜き相互検証の効率的な近似

### 熟語・専門語

- **leave-one-out**: LOO。一点ずつ除外した予測評価を効率的に近似する交差検証。
- **validation**: 検証。モデルが目的・データ・外部知識に照らして妥当かを確認すること。

### 要約

- 2. どの観測値または観測値のグループが予測するのが最も難しいかを特定する。

## Chunk 0314

### English（抽出4行）

> sampling can facilitate practical use by removing the need to re-ﬁt the model when each data point
> is left out (Vehtari et al., 2017, Paananen et al., 2020).
> −40
> y

### 日本語訳（自動翻訳）

> サンプリングにより、各データポイントの時点でモデルを再適合する必要がなくなり、実用化が容易になります。
> は省略されます (Vehtari et al., 2017、Paananen et al., 2020)。
> −40
> y

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- サンプリングにより、各データポイントの時点でモデルを再適合する必要がなくなり、実用化が容易になります。

## Chunk 0315

### English（抽出4行）

> yrep
> A
> 0.5
> 1.0

### 日本語訳（自動翻訳）

> イレップ
> あ
> 0.5
> 1.0

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- イレップ あ 0.5 1.0

## Chunk 0316

### English（抽出4行）

> 1.5
> 2.0
> T = sd
> T(yrep)

### 日本語訳（自動翻訳）

> 1.5
> 2.0
> T = SD
> T(イレップ)

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- 1.5 2.0 T = SD T(イレップ)

## Chunk 0317

### English（抽出4行）

> T(y)
> B
> Count
> yrep

### 日本語訳（自動翻訳）

> T(y)
> B
> カウント
> イレップ

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- T(y) B カウント イレップ

## Chunk 0318

### English（抽出4行）

> y
> C
> High
> Low

### 日本語訳（自動翻訳）

> y
> C
> 高
> 低い

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- y C 高 低い

## Chunk 0319

### English（抽出4行）

> Count
> yrep
> y
> D

### 日本語訳（自動翻訳）

> カウント
> イレップ
> y
> D

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- カウント イレップ y D

## Chunk 0320

### English（抽出4行）

> Figure 14: Examples of diagnosing model misﬁt with simple posterior predictive checks as imple-
> mented in the bayesplot R package. In all plots y is plotted based on the input data and yrep based
> on the distribution of posterior simulations. (A) A “density” check for a normal distribution being
> ﬁt to data simulated from a lognormal distribution: the tails of the yrep behave very diﬀerently

### 日本語訳（自動翻訳）

> 図 14: 単純な事後予測チェックを単純な方法として使用してモデルの不適合を診断する例
> Bayesplot R パッケージに記載されています。すべてのプロットで、y は入力データと yrep に基づいてプロットされます。
> 事後シミュレーションの分布について。 (A) 正規分布の「密度」チェック
> 対数正規分布からシミュレートされたデータに適合: yrep の裾は非常に異なる動作をします

### 熟語・専門語

- **posterior predictive**: 事後予測。推定後のモデルが観測データの特徴を再現できるかを見る診断。

### 要約

- 図 14: 単純な事後予測チェックを単純な方法として使用してモデルの不適合を診断する例 Bayesplot R パッケージに記載されています。

## Chunk 0321

### English（抽出4行）

> than for y. (B) A “statistic” check for a binomial distribution being ﬁt to data simulated from a
> beta-binomial distribution. Histogram of standard deviation (sd) of the yrep datasets is compared to
> sd of y. The check shows that the data have larger sd than what the model can handle. (C) A “bars”
> check for discrete data (note the switch of colors between y and yrep). This check looks good: the

### 日本語訳（自動翻訳）

> yよりも。 (B) 二項分布がデータからシミュレートされたデータに適合しているかどうかの「統計」チェック
> ベータ二項分布。 yrep データセットの標準偏差 (sd) のヒストグラムは、次と比較されます。
> YのSD。このチェックでは、モデルが処理できるものよりも大きな sd がデータにあることが示されます。 (C) 「バー」
> 離散データをチェックします (y と yrep の間の色の切り替えに注意してください)。このチェックは良さそうです:

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- yよりも。

## Chunk 0322

### English（抽出4行）

> distribution of frequencies of individual counts in y falls well within those in yrep. (D) The same
> model and data but with the check grouped by a covariate that was not included in the model but
> in fact inﬂuenced the response. The High subgroup systematically deviates from the range of yrep,
> indicating that there is an additional source of variability that the model fails to capture.

### 日本語訳（自動翻訳）

> y の個々のカウントの頻度の分布は、yrep の頻度の分布内に十分に収まります。 (D)同じ
> モデルとデータですが、モデルに含まれていない共変量によってグループ化されたチェックが含まれていますが、
> 実際、反応に影響を与えました。 High サブグループは系統的に yrep の範囲から逸脱します。
> これは、モデルが捉えることができない変動要因が他にも存在することを示しています。

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- y の個々のカウントの頻度の分布は、yrep の頻度の分布内に十分に収まります。

## Chunk 0323

### English（抽出4行）

> Although perfect calibration of predictive distributions is not the ultimate goal of Bayesian
> inference, looking at how well calibrated leave-one-out cross validation (LOO-CV) predictive dis-
> tributions are, can reveal opportunities to improve the model. While posterior predictive checking
> often compares the marginal distribution of the predictions to the data distribution, leave-one-out

### 日本語訳（自動翻訳）

> 予測分布の完璧な校正はベイジアンの最終目標ではありませんが、
> 推論、リーブワンアウト相互検証 (LOO-CV) の予測障害がどの程度適切に調整されているかを調べます。
> 貢献は、モデルを改善する機会を明らかにすることができます。事後予測チェック中
> 多くの場合、予測の周辺分布とデータ分布を比較します。

### 熟語・専門語

- **posterior predictive**: 事後予測。推定後のモデルが観測データの特徴を再現できるかを見る診断。
- **cross validation**: 交差検証。汎化性能を推定するためにデータを分割/近似除外する評価法。
- **leave-one-out**: LOO。一点ずつ除外した予測評価を効率的に近似する交差検証。
- **validation**: 検証。モデルが目的・データ・外部知識に照らして妥当かを確認すること。
- **prediction**: 予測。未知/将来/除外データに対する分布や点推定。

### 要約

- 予測分布の完璧な校正はベイジアンの最終目標ではありませんが、 推論、リーブワンアウト相互検証 (LOO-CV) の予測障害がどの程度適切に調整されているかを調べます。

## Chunk 0324

### English（抽出4行）

> cross validation predictive checking looks at the calibration of conditional predictive distributions.
> Under a good calibration, the conditional cumulative probability distribution of the predictive dis-
> tributions (also known as probability integral transformations, PIT) given the left-out observations
> are uniform. Deviations from uniformity can reveal, for example, under or overdispersion of the

### 日本語訳（自動翻訳）

> 相互検証の予測チェックでは、条件付き予測分布の調整が検討されます。
> 適切なキャリブレーションの下では、予測誤差の条件付き累積確率分布は、
> 取り残された観測値を考慮した分布 (確率積分変換、PIT とも呼ばれます)
> 均一です。均一性からの逸脱により、たとえば、分散の過小または過剰が明らかになる可能性があります。

### 熟語・専門語

- **cross validation**: 交差検証。汎化性能を推定するためにデータを分割/近似除外する評価法。
- **validation**: 検証。モデルが目的・データ・外部知識に照らして妥当かを確認すること。

### 要約

- 相互検証の予測チェックでは、条件付き予測分布の調整が検討されます。

## Chunk 0325

### English（抽出4行）

> predictive distributions. Figure 16 shows an example from Gabry et al. (2019) where leave-one-out
> cross validation probability integral transformation (LOO-PIT) values are too concentrated near
> Figure 15: Example of a posterior predictive check. The left column shows observed data from a
> psychology experiment, displayed as a 15×23 array of binary responses from each of 6 participants,

### 日本語訳（自動翻訳）

> 予測分布。図 16 は、Gabry らの例を示しています。 (2019) ワンアウトの場合
> 相互検証確率積分変換 (LOO-PIT) 値が近くに集中しすぎています。
> 図 15: 事後予測チェックの例。左の列は、観測データを示しています。
> 心理学実験。6 人の参加者それぞれからの 2 値応答の 15×23 配列として表示されます。

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

> 行、列、人物順に並べます。
> 右側の列には、
> 近似モデルの事後予測分布。複製された各データセットは次のように順序付けされています。
> これはディスプレイの一部です。このチェックにより、観察されたものには現れないいくつかのパターンが明らかになります。

### 熟語・専門語

- **posterior predictive**: 事後予測。推定後のモデルが観測データの特徴を再現できるかを見る診断。

### 要約

- 行、列、人物順に並べます。

## Chunk 0327

### English（抽出4行）

> the replications, indicating a aspect of lack of ﬁt of model to data. From Gelman et al. (2013).
> the middle, revealing that the predictive distributions are overdispersed compared to the actual
> conditional observations.
> In addition to looking at the calibration of the conditional predictive distributions, we can also

### 日本語訳（自動翻訳）

> レプリケーションは、モデルがデータに適合していない側面を示しています。ゲルマンらより。 （2013年）。
> 中央は、予測分布が実際の分布に比べて過度に分散していることを明らかにしています。
> 条件付き観察。
> 条件付き予測分布の調整を確認することに加えて、次のこともできます。

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- レプリケーションは、モデルがデータに適合していない側面を示しています。

## Chunk 0328

### English（抽出4行）

> look at which observations are hard to predict and see if there is a pattern or explanation for why
> some are harder to predict than others. This approach can reveal potential problems in the data or
> data processing, or point to directions for model improvement (Vehtari et al., 2017, Gabry et al.,
> 2019). We illustrate with an analysis of a survey of residents from a small area in Bangladesh that

### 日本語訳（自動翻訳）

> どの観測結果が予測困難であるかを調べ、その理由のパターンや説明があるかどうかを確認します。
> 他のものよりも予測が難しいものもあります。このアプローチにより、データ内の潜在的な問題が明らかになったり、
> データ処理、またはモデル改善の方向性を示す (Vehtari et al.、2017、Gabry et al.、
> 2019）。私たちは、バングラデシュの小さな地域の住民を対象とした調査の分析を用いて、次のことを説明します。

### 熟語・専門語

- **ESS**: 有効サンプルサイズ。自己相関を考慮した独立サンプル相当数。

### 要約

- どの観測結果が予測困難であるかを調べ、その理由のパターンや説明があるかどうかを確認します。

## Chunk 0329

### English（抽出4行）

> was aﬀected by arsenic in drinking water. Respondents with elevated arsenic levels in their wells
> were asked if they were interested in switching to water from a neighbor’s well, and a series of
> models were ﬁt to predict this binary response given household information (Vehtari et al., 2017).
> Figure 17 compares the pointwise log scores for two of the models. The scattered blue dots on

### 日本語訳（自動翻訳）

> 飲料水中のヒ素の影響を受けました。井戸内のヒ素レベルが上昇した回答者
> 近所の井戸の水に切り替えることに興味があるかどうかを尋ねると、一連の質問があった。
> モデルは、世帯情報を考慮してこの二項反応を予測するのに適合しました (Vehtari et al., 2017)。
> 図 17 は、2 つのモデルの点ごとのログ スコアを比較しています。散りばめられた青い点々は、

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- 飲料水中のヒ素の影響を受けました。

## Chunk 0330

### English（抽出4行）

> the left side of Figure 17a and on the lower right of Figure 17b correspond to data points for which
> one of the models ﬁts particularly poorly—that is, large negative contributions to the expected log
> predictive density. We can sum all of the pointwise diﬀerences to yield an estimated diﬀerence in
> expected log predictive densities elpdloo of 16.4 with a standard error of just 4.4, but beyond that

### 日本語訳（自動翻訳）

> 図 17a の左側と図 17b の右下は、データ ポイントに対応します。
> モデルの 1 つが特に適合度が低い、つまり、予想される対数に対するマイナスの寄与が大きい
> 予測密度。すべての点ごとの差を合計して、推定差を求めることができます。
> 期待される対数予測密度 elpdloo は 16.4 で、標準誤差はわずか 4.4 ですが、それを超えています。

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- 図 17a の左側と図 17b の右下は、データ ポイントに対応します。

## Chunk 0331

### English（抽出4行）

> we can use this plot to ﬁnd which data points create problems for the model, in this case 10–15
> non-switchers with very high existing arsenic levels.
> In this particular example, we did not follow up on this modeling issue, because even more
> elaborate models that ﬁt the data better do not change the conclusions and thus would not change

### 日本語訳（自動翻訳）

> このプロットを使用して、どのデータ ポイントがモデルに問題を引き起こしているかを見つけることができます (この場合は 10 ～ 15)。
> 既存のヒ素レベルが非常に高い非スイッチャー。
> この特定の例では、このモデリングの問題についてはフォローアップしませんでした。
> データによりよく適合する精巧なモデルは結論を変えず、したがって変更されない

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- このプロットを使用して、どのデータ ポイントがモデルに問題を引き起こしているかを見つけることができます (この場合は 10 ～ 15)。

## Chunk 0332

### English（抽出4行）

> any recommended actions in Bangladesh. Gabry et al. (2019) provide an example where LOO-CV
> indicated problems that motivated eﬀorts to improve the statistical model.
> The above two approaches focus on the predictions, but we can also look at how parameter
> Figure 16: Leave-one-out cross validation probability integral transformation (LOO-PIT) plot

### 日本語訳（自動翻訳）

> バングラデシュで推奨される行動。ギャブリーら。 (2019) LOO-CV の例を提供します。
> 統計モデルを改善する取り組みの動機となる問題を指摘しました。
> 上記の 2 つのアプローチは予測に焦点を当てていますが、パラメーターがどのように変化するかを見ることもできます。
> 図 16: リーブワンアウト相互検証確率積分変換 (LOO-PIT) プロット

### 熟語・専門語

- **cross validation**: 交差検証。汎化性能を推定するためにデータを分割/近似除外する評価法。
- **leave-one-out**: LOO。一点ずつ除外した予測評価を効率的に近似する交差検証。
- **validation**: 検証。モデルが目的・データ・外部知識に照らして妥当かを確認すること。
- **prediction**: 予測。未知/将来/除外データに対する分布や点推定。

### 要約

- バングラデシュで推奨される行動。

## Chunk 0333

### English（抽出4行）

> evaluating the calibration of predictions from a ﬁtted model. Under perfect calibration, LOO-PIT
> values would be uniform. In this case the values are concentrated near the middle, indicating
> predictive distributions that are too wide. From Gabry et al. (2019).
> −3.5

### 日本語訳（自動翻訳）

> 適合モデルからの予測の校正を評価する。完璧なキャリブレーションのもと、LOO-PIT
> 値は均一になります。この場合、値は中央付近に集中しており、
> 予測分布が広すぎる。ガブリーらより。 （2019年）。
> −3.5

### 熟語・専門語

- **prediction**: 予測。未知/将来/除外データに対する分布や点推定。

### 要約

- 適合モデルからの予測の校正を評価する。

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
> −0.5
> −3
> −2

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- −1 −0.5 −3 −2

## Chunk 0336

### English（抽出4行）

> −1
> LOO1
> LOO2
> Didn’t switch

### 日本語訳（自動翻訳）

> −1
> LOO1
> LOO2
> 切り替わらなかった

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- −1 LOO1 LOO2 切り替わらなかった

## Chunk 0337

### English（抽出4行）

> Switched
> −1
> −0.5
> 0.5

### 日本語訳（自動翻訳）

> 切り替え済み
> −1
> −0.5
> 0.5

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- 切り替え済み −1 −0.5 0.5

## Chunk 0338

### English（抽出4行）

> 1.5
> 2.5
> −1
> −0.5

### 日本語訳（自動翻訳）

> 1.5
> 2.5
> −1
> −0.5

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- 1.5 2.5 −1 −0.5

## Chunk 0339

### English（抽出4行）

> log(arsenic)
> LOO1 −LOO2
> Didn’t switch
> Switched

### 日本語訳（自動翻訳）

> 丸太(ヒ素)
> LOO1 −LOO2
> 切り替わらなかった
> 切り替え済み

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- 丸太(ヒ素) LOO1 −LOO2 切り替わらなかった 切り替え済み

## Chunk 0340

### English（抽出4行）

> Figure 17: Logistic regression example, comparing two models in terms of their pointwise contribu-
> tions to leave one out (LOO) cross validation error: (a) comparing contributions of LOO directly;
> (b) plotting the diﬀerence in LOO as a function of a key predictor (the existing arsenic level). To
> aid insight, we have colored the data according to the (binary) output, with red corresponding to

### 日本語訳（自動翻訳）

> 図 17: ロジスティック回帰の例、点ごとの寄与の観点から 2 つのモデルを比較
> 1 つを除外する (LOO) 相互検証エラーのオプション: (a) LOO の寄与を直接比較する。
> (b) LOO の差を主要な予測因子 (既存のヒ素レベル) の関数としてプロットする。に
> 洞察を助けるため、(バイナリ) 出力に従ってデータを色付けしました。赤色は次の値に対応します。

### 熟語・専門語

- **cross validation**: 交差検証。汎化性能を推定するためにデータを分割/近似除外する評価法。
- **ESS**: 有効サンプルサイズ。自己相関を考慮した独立サンプル相当数。
- **validation**: 検証。モデルが目的・データ・外部知識に照らして妥当かを確認すること。

### 要約

- 図 17: ロジスティック回帰の例、点ごとの寄与の観点から 2 つのモデルを比較 1 つを除外する (LOO) 相互検証エラーのオプション: (a) LOO の寄与を直接比較する。

## Chunk 0341

### English（抽出4行）

> y = 1 and blue representing y = 0. For any given data point, one model will ﬁt better than another,
> but for this example the graphs reveal that the diﬀerence in LOO between the models arises from
> the linear model’s poor predictions for 10–15 particular data points. From Vehtari et al. (2017).
> inferences change when each data point is left out, which provides a sense of the inﬂuence of each

### 日本語訳（自動翻訳）

> y = 1、青は y = 0 を表します。任意のデータ ポイントに対して、あるモデルは別のモデルよりよく適合します。
> しかし、この例では、モデル間の LOO の違いが次の点から生じていることがグラフからわかります。
> 10 ～ 15 個の特定のデータ ポイントに対する線形モデルの予測が不十分です。 Vehtariらより。 （2017年）。
> 各データ ポイントが省略されると推論が変化するため、それぞれのデータ ポイントの影響を把握できます。

### 熟語・専門語

- **prediction**: 予測。未知/将来/除外データに対する分布や点推定。

### 要約

- y = 1、青は y = 0 を表します。

## Chunk 0342

### English（抽出4行）

> observation. As with cross validation more generally, this approach has limitations if the data are
> clustered or otherwise structured so that multiple points would need to be removed to have an eﬀect,
> but it can still be part of general Bayesian workﬂow, given that it is computationally inexpensive
> and can be valuable in many applied settings. Following this cross validation idea, the inﬂuence

### 日本語訳（自動翻訳）

> 観察。より一般的な相互検証と同様に、データが以下の場合、このアプローチには制限があります。
> クラスター化されているか、効果を発揮するには複数のポイントを削除する必要があるように構造化されている、
> しかし、計算コストが低いため、一般的なベイジアン ワークフローの一部として使用することもできます。
> 多くの応用設定で価値を発揮します。この相互検証のアイデアに従うと、次のような影響が生じます。

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

> 個々のデータ点 yi の分布の特性に従って要約できます。
> LOO-CV を近似するときに計算される重要度の重み (詳細については、Vehtari et al.、2017 を参照)
> 近似と、loo R パッケージでの対応する実装について (Vehtari et al.
> 2020））。

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- 個々のデータ点 yi の分布の特性に従って要約できます。

## Chunk 0344

### English（抽出4行）

> An alternative approach to importance weighting is to frame the removal of data points as a
> gradient in a larger model space. Suppose we have a simple independent likelihood, Qn
> i=1 p(yi|θ),
> and we work with the more general form, Qn

### 日本語訳（自動翻訳）

> 重要度の重み付けに対する別のアプローチは、データ ポイントの削除を次のように組み立てることです。
> より大きなモデル空間での勾配。単純な独立尤度 Qn があると仮定します。
> i=1 p(yi|θ)、
> そして、より一般的な形式である Qn を使用します。

### 熟語・専門語

- **likelihood**: 尤度。パラメータが与えられたときデータがどれだけ起こりやすいか。

### 要約

- 重要度の重み付けに対する別のアプローチは、データ ポイントの削除を次のように組み立てることです。

## Chunk 0345

### English（抽出4行）

> i=1 p(yi|θ)αi, which reduces to the likelihood of the
> original model when αi = 1 for all i.
> Leave-one-out cross validation corresponds to setting
> αi = 0 for one observation at a time. But another option, discussed by Giordano et al. (2018) and

### 日本語訳（自動翻訳）

> i=1 p(yi|θ)αi、これは、
> すべての i について αi = 1 の場合の元のモデル。
> リーブワンアウト相互検証は設定に対応します
> 一度に 1 つの観測では αi = 0。しかし、Giordanoらによって議論された別のオプション。 （2018年）と

### 熟語・専門語

- **cross validation**: 交差検証。汎化性能を推定するためにデータを分割/近似除外する評価法。
- **leave-one-out**: LOO。一点ずつ除外した予測評価を効率的に近似する交差検証。
- **likelihood**: 尤度。パラメータが与えられたときデータがどれだけ起こりやすいか。
- **validation**: 検証。モデルが目的・データ・外部知識に照らして妥当かを確認すること。

### 要約

- i=1 p(yi|θ)αi、これは、 すべての i について αi = 1 の場合の元のモデル。

## Chunk 0346

### English（抽出4行）

> implemented by Giordano (2018), is to compute the gradient of the augmented log likelihood as a
> function of α: this can be interpreted as a sort of diﬀerential cross validation or inﬂuence function.
> Cross validation for multilevel (hierarchical) models requires more thought. Leave-one-out is
> still possible, but it does not always match our inferential goals. For example, when performing

### 日本語訳（自動翻訳）

> Giordano (2018) によって実装された、拡張対数尤度の勾配を次のように計算します。
> α の関数: これは、一種の差分相互検証または影響関数として解釈できます。
> マルチレベル (階層) モデルの相互検証には、さらに考慮する必要があります。リーブワンアウトとは、
> まだ可能性はありますが、それは私たちの推論上の目標と常に一致するとは限りません。たとえば、演奏するとき、

### 熟語・専門語

- **cross validation**: 交差検証。汎化性能を推定するためにデータを分割/近似除外する評価法。
- **leave-one-out**: LOO。一点ずつ除外した予測評価を効率的に近似する交差検証。
- **likelihood**: 尤度。パラメータが与えられたときデータがどれだけ起こりやすいか。
- **validation**: 検証。モデルが目的・データ・外部知識に照らして妥当かを確認すること。

### 要約

- Giordano (2018) によって実装された、拡張対数尤度の勾配を次のように計算します。

## Chunk 0347

### English（抽出4行）

> multilevel regression for adjusting political surveys, we are often interested in estimating opinion at
> the state level. A model can show real improvements at the state level with this being undetectable
> at the level of cross validation of individual observations (Wang and Gelman, 2016). Millar (2018),
> Merkle, Furr, and Rabe-Hesketh (2019), and Vehtari (2019) demonstrate diﬀerent cross validation

### 日本語訳（自動翻訳）

> 政治調査を調整するための多段階回帰では、多くの場合、意見の推定に興味があります。
> 州レベル。モデルは州レベルで実際の改善を示すことができますが、これは検出できません
> 個々の観察の相互検証のレベルで (Wang および Gelman、2016)。ミラー (2018)、
> Merkle、Furr、Rabe-Hesketh (2019)、および Vehtari (2019) は、さまざまな相互検証を実証しています

### 熟語・専門語

- **cross validation**: 交差検証。汎化性能を推定するためにデータを分割/近似除外する評価法。
- **ESS**: 有効サンプルサイズ。自己相関を考慮した独立サンプル相当数。
- **validation**: 検証。モデルが目的・データ・外部知識に照らして妥当かを確認すること。

### 要約

- 政治調査を調整するための多段階回帰では、多くの場合、意見の推定に興味があります。

## Chunk 0348

### English（抽出4行）

> variants and their approximations in hierarchical models, including leave-one-unit-out and leave-
> one-group-out.
> In applied problems we have performed a mix, holding out some individual
> observations and some groups and then evaluating predictions at both levels (Price et al., 1996).

### 日本語訳（自動翻訳）

> 階層モデルにおけるバリアントとその近似 (leave-one-unit-out や Leave-one-unit-out など)
> 1グループアウト。
> 応用問題では、いくつかの個別問題を保持しながらミックスを実行しました。
> 観察といくつかのグループを比較し、両方のレベルで予測を評価します (Price et al., 1996)。

### 熟語・専門語

- **prediction**: 予測。未知/将来/除外データに対する分布や点推定。

### 要約

- 階層モデルにおけるバリアントとその近似 (leave-one-unit-out や Leave-one-unit-out など) 1グループアウト。

## Chunk 0349

### English（抽出4行）

> Unfortunately, approximating such cross validation procedures using importance sampling tends
> to be much harder than in the leave-one-out case. This is because more observations are left out at
> a time which implies stronger changes in the posterior distributions from the full to the subsetted
> model. As a result, we may have to rely on more costly model reﬁts to obtain leave-one-unit-out

### 日本語訳（自動翻訳）

> 残念ながら、重要度サンプリングを使用してこのような相互検証手順を近似すると、
> ワンアウトの場合よりもはるかに困難になります。これは、より多くの観測が省略されるためです。
> 完全な分布から部分集合化された分布への事後分布のより強い変化を意味する時間
> モデル。その結果、1 ユニットアウトを実現するには、よりコストのかかるモデルの再調整に頼らなければならない可能性があります。

### 熟語・専門語

- **cross validation**: 交差検証。汎化性能を推定するためにデータを分割/近似除外する評価法。
- **leave-one-out**: LOO。一点ずつ除外した予測評価を効率的に近似する交差検証。
- **posterior distribution**: 事後分布。データ観測後の未知量の不確実性を表す分布。
- **validation**: 検証。モデルが目的・データ・外部知識に照らして妥当かを確認すること。

### 要約

- 残念ながら、重要度サンプリングを使用してこのような相互検証手順を近似すると、 ワンアウトの場合よりもはるかに困難になります。

## Chunk 0350

### English（抽出4行）

> and leave-one-group-out cross validation results.
> 6.3.
> Influence of prior information
> Complex models can be diﬃcult to understand, hence the need for exploratory model analysis

### 日本語訳（自動翻訳）

> そして、1 つのグループを除外した相互検証の結果。
> 6.3.
> 事前情報の影響
> 複雑なモデルは理解するのが難しい場合があるため、探索的なモデル分析が必要です

### 熟語・専門語

- **cross validation**: 交差検証。汎化性能を推定するためにデータを分割/近似除外する評価法。
- **validation**: 検証。モデルが目的・データ・外部知識に照らして妥当かを確認すること。

### 要約

- そして、1 つのグループを除外した相互検証の結果。

## Chunk 0351

### English（抽出4行）

> (Unwin et al., 2003, Wickham, 2006) and explainable AI (Chen et al., 2018, Gunning, 2017, Rudin,
> 2018), which complements methods for evaluating, comparing, and averaging models using a range
> of interrelated approaches, including cross validation, stacking, boosting, and Bayesian evaluation.
> In this section we discuss methods to understand how posterior inferences under a ﬁtted model

### 日本語訳（自動翻訳）

> (Unwin et al.、2003、Wickham、2006) および説明可能な AI (Chen et al.、2018、Gunning、2017、Rudin、
> 2018)、範囲を使用してモデルを評価、比較、平均する方法を補完します。
> 相互検証、スタッキング、ブースティング、ベイジアン評価など、相互に関連するアプローチの統合。
> このセクションでは、適合モデルの下で事後推論がどのように行われるかを理解する方法について説明します。

### 熟語・専門語

- **cross validation**: 交差検証。汎化性能を推定するためにデータを分割/近似除外する評価法。
- **validation**: 検証。モデルが目的・データ・外部知識に照らして妥当かを確認すること。

### 要約

- (Unwin et al.、2003、Wickham、2006) および説明可能な AI (Chen et al.、2018、Gunning、2017、Rudin、 2018)、範囲を使用してモデルを評価、比較、平均する方法を補完します。

## Chunk 0352

### English（抽出4行）

> depend on the data and priors.
> A statistical model can be understood in two ways: generatively and inferentially. From the
> generative perspective, we want to understand how the parameters map to the data. We can perform
> prior predictive simulation to visualize possible data from the model (as in Figure 4). From the

### 日本語訳（自動翻訳）

> データと事前分布に依存します。
> 統計モデルは、生成的および推論的という 2 つの方法で理解できます。から
> 生成的な観点から、パラメーターがデータにどのようにマッピングされるかを理解したいと考えています。パフォーマンスができる
> 事前の予測シミュレーションを使用して、モデルから得られる可能性のあるデータを視覚化します (図 4 を参照)。から

### 熟語・専門語

- **prior predictive**: 事前予測。データを見る前のpriorだけで生成される予測分布を確認する診断。

### 要約

- データと事前分布に依存します。

## Chunk 0353

### English（抽出4行）

> inferential perspective, we want to understand the path from inputs (data and prior distributions) to
> outputs (estimates and uncertainties).
> The most direct way to understand the inﬂuence of priors is to run sensitivity analysis by reﬁtting
> Figure 18: Example of static sensitivity analysis from a statistical model ﬁt to a problem in

### 日本語訳（自動翻訳）

> 推論的な観点から、入力 (データと事前分布) から
> 出力（推定値と不確実性）。
> 事前分布の影響を理解する最も直接的な方法は、再適合して感度分析を実行することです。
> 図 18: 問題に適合した統計モデルからの静的感度分析の例

### 熟語・専門語

- **prior distribution**: 事前分布。データ観測前の知識・制約を表す分布。

### 要約

- 推論的な観点から、入力 (データと事前分布) から 出力（推定値と不確実性）。

## Chunk 0354

### English（抽出4行）

> toxicology. Each graph shows posterior simulation draws of the percent metabolized under two
> conditions (hence the clusters of points at the top and bottom of each graph), plotted vs. two of
> the parameters in the model. The plots reveal little sensitivity to either parameter on inference for
> percent metabolized under one condition, but strong sensitivity for the other. This sort of graph

### 日本語訳（自動翻訳）

> 毒物学。各グラフは、2 日間の代謝率の事後シミュレーション結果を示しています。
> 条件 (したがって、各グラフの上部と下部にある点のクラスター) を 2 つに対してプロットします。
> モデル内のパラメータ。プロットでは、推論においてどちらのパラメータに対しても感度がほとんどないことがわかります。
> ある条件下で代謝されるパーセントですが、他の条件に対しては強い感受性を示します。このようなグラフ

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- 毒物学。

## Chunk 0355

### English（抽出4行）

> can be used to assess sensitivity to alternative prior distributions, without requiring the model to
> be re-ﬁt. From Gelman, Bois, and Jiang (1996).
> the model with multiple priors, this can however be prohibitively expensive if the models take a
> long time to ﬁt. However, there are some shortcuts.

### 日本語訳（自動翻訳）

> モデルを必要とせずに、代替事前分布に対する感度を評価するために使用できます。
> 再びフィットすること。ゲルマン、ボワ、ジャン (1996) より。
> 複数の事前分布をもつモデルですが、モデルが
> フィットするまで長い時間。ただし、いくつかの近道があります。

### 熟語・専門語

- **prior distribution**: 事前分布。データ観測前の知識・制約を表す分布。
- **ESS**: 有効サンプルサイズ。自己相関を考慮した独立サンプル相当数。

### 要約

- モデルを必要とせずに、代替事前分布に対する感度を評価するために使用できます。

## Chunk 0356

### English（抽出4行）

> One approach is to compute the shrinkage between prior and posterior, for example, by compar-
> ing prior to posterior standard deviations for each parameter or by comparing prior and posterior
> quantiles. If the data relative to the prior are informative for a particular parameter, shrinkage
> for that parameter should be stronger. This type of check has been extensively developed in the

### 日本語訳（自動翻訳）

> 1 つのアプローチは、たとえば、比較することによって、前と後の収縮を計算することです。
> 各パラメータの事後標準偏差に先立って、または事前と事後を比較することによって
> 分位数。以前のデータと比較したデータが特定のパラメータについて有益である場合、収縮
> そのパラメータはより強力である必要があります。このタイプのチェックは、世界で広範囲に開発されています。

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- 1 つのアプローチは、たとえば、比較することによって、前と後の収縮を計算することです。

## Chunk 0357

### English（抽出4行）

> literature; see, for example, Nott et al. (2020).
> Another approach is to use importance sampling to approximate the posterior of the new model
> using the posterior of old model, provided the two posteriors are similar enough for importance
> sampling to bridge (Vehtari et al., 2019, Paananen et al., 2020). And if they are not, this is also

### 日本語訳（自動翻訳）

> 文学;たとえば、Nott et al. を参照してください。 （2020年）。
> 別のアプローチは、重要度サンプリングを使用して新しいモデルの事後係数を近似することです。
> 2 つの事後分布が重要性を考慮して十分に類似している場合は、古いモデルの事後分布を使用します。
> サンプリングからブリッジへ (Vehtari et al., 2019、Paananen et al., 2020)。そうでない場合、これも同様です

### 熟語・専門語

- **approximate**: 近似。速度や扱いやすさのため、正確な推論・モデルを緩めること。

### 要約

- 文学;たとえば、Nott et al. を参照してください。

## Chunk 0358

### English（抽出4行）

> valuable information in itself (see Section 6.2).
> Yet another approach is to perform static sensitivity analysis, which is a way to study sensitivity
> of posterior inferences to perturbations in the prior without requiring that the model be re-ﬁt using
> alternative prior distributions (Gelman, Bois, and Jiang, 1996; see Figure 18 for an example). Each

### 日本語訳（自動翻訳）

> それ自体が貴重な情報です (セクション 6.2 を参照)。
> さらに別のアプローチは、静的感度分析を実行することです。これは、感度を研究する方法です。
> を使用してモデルを再フィッティングする必要なく、事前の摂動に対する事後推論を行うことができます。
> 代替事前分布 (Gelman、Bois、および Jiang、1996、例については図 18 を参照)。それぞれ

### 熟語・専門語

- **prior distribution**: 事前分布。データ観測前の知識・制約を表す分布。

### 要約

- それ自体が貴重な情報です (セクション 6.2 を参照)。

## Chunk 0359

### English（抽出4行）

> graph in Figure 18 shows posterior simulations revealing the posterior dependence of a quantity of
> interest (in this example, the percentage of a toxin that is metabolized by the body) as a function of
> a parameter in the model.
> Consider Figure 18 as four scatterplots, as each of the two graphs is really two plots super-

### 日本語訳（自動翻訳）

> 図 18 のグラフは、量の事後依存性を明らかにする事後シミュレーションを示しています。
> の関数としての関心（この例では、身体によって代謝される毒素の割合）
> モデル内のパラメータ。
> 2 つのグラフのそれぞれは、実際には 2 つのスーパープロットであるため、図 18 を 4 つの散布図と考えてください。

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- 図 18 のグラフは、量の事後依存性を明らかにする事後シミュレーションを示しています。

## Chunk 0360

### English（抽出4行）

> imposed, one for a condition of low exposure to the toxin and one for high exposure. Each of
> these four plots can be interpreted in two ways. First, the direct interpretation shows the posterior
> correlation between the predictive quantity of interest (the percentage metabolized in the body)
> and a particular parameter (for example, the scaling coeﬃcient of the toxin’s metabolism). Second,

### 日本語訳（自動翻訳）

> 1 つは毒素への低曝露状態に、もう 1 つは高曝露状態に課されます。それぞれの
> これら 4 つのプロットは 2 つの方法で解釈できます。まず、直接解釈は事後結果を示します。
> 予測対象量（体内で代謝される割合）間の相関関係
> そして特定のパラメータ（例えば、毒素の代謝のスケーリング係数）。 2番、

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- 1 つは毒素への低曝露状態に、もう 1 つは高曝露状態に課されます。

## Chunk 0361

### English（抽出4行）

> each scatterplot can be read indirectly to reveal sensitivity of the quantity plotted on the y-axis to
> the prior of the parameter plotted on the x-axis. The interpretation goes as follows: a change in the
> prior distribution for the parameter plotted on the x-axis can be performed by reweighting of the
> points on the graph according to the ratio of the new prior to that used in the analysis. With these

### 日本語訳（自動翻訳）

> 各散布図を間接的に読み取ることで、y 軸にプロットされた量の感度を明らかにすることができます。
> x 軸にプロットされたパラメータの事前分布。解釈は次のようになります。
> X 軸にプロットされたパラメータの事前分布は、
> 分析で使用された前の新しいポイントの比率に従ってグラフ上のポイントが表示されます。これらを使って

### 熟語・専門語

- **prior distribution**: 事前分布。データ観測前の知識・制約を表す分布。

### 要約

- 各散布図を間接的に読み取ることで、y 軸にプロットされた量の感度を明らかにすることができます。

## Chunk 0362

### English（抽出4行）

> graphs, the importance weighing can be visualized implicitly: the impact of changes in the prior
> distribution can be seen based on the dependence in the scatterplot.
> The mapping of prior and data to posterior can also be studied more formally, as discussed in
> Section 6.2.

### 日本語訳（自動翻訳）

> グラフを使用すると、重要度の重み付けを暗黙的に視覚化できます。以前の変更の影響
> 散布図の依存性に基づいて分布を確認できます。
> 事前データと事後データのマッピングは、以下で説明するように、より形式的に研究することもできます。
> セクション6.2。

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- グラフを使用すると、重要度の重み付けを暗黙的に視覚化できます。

## Chunk 0363

### English（抽出4行）

> 6.4.
> Summarizing inference and propagating uncertainty
> Bayesian inference is well suited for problems with latent variables and other settings with unresolv-
> able uncertainty. In addition, we often use hierarchical models that include batches of parameters

### 日本語訳（自動翻訳）

> 6.4.
> 推論の要約と不確実性の伝播
> ベイズ推論は、潜在変数やその他の未解決の設定の問題に適しています。
> 可能性のある不確実性。さらに、パラメータのバッチを含む階層モデルをよく使用します。

### 熟語・専門語

- **Bayesian inference**: ベイズ推論。事前分布と尤度から事後分布を計算する中核処理。
- **uncertainty**: 不確実性。観測・パラメータ・モデル構造・意思決定に残る曖昧さ。

### 要約

- 6.4. 推論の要約と不確実性の伝播 ベイズ推論は、潜在変数やその他の未解決の設定の問題に適しています。

## Chunk 0364

### English（抽出4行）

> representing variation.
> For example, when reporting the results from our election forecasting
> model, we are interested in uncertainty in the forecast votes and also variation among states.
> Unfortunately, the usual ways of displaying Bayesian inference do not fully capture the multiple

### 日本語訳（自動翻訳）

> バリエーションを表します。
> たとえば、選挙予想の結果を報告するとき
> モデルでは、予測投票の不確実性と州間のばらつきに興味があります。
> 残念ながら、ベイズ推論を表示する通常の方法では、複数の要素を完全には捉えることができません。

### 熟語・専門語

- **Bayesian inference**: ベイズ推論。事前分布と尤度から事後分布を計算する中核処理。
- **uncertainty**: 不確実性。観測・パラメータ・モデル構造・意思決定に残る曖昧さ。

### 要約

- バリエーションを表します。

## Chunk 0365

### English（抽出4行）

> levels of variation and uncertainty in our inferences.
> A table or even a graph of parameter
> estimates, uncertainties, and standard errors is only showing one-dimensional margins, while
> graphs of marginal posterior distributions are unwieldy for models with many parameters and also

### 日本語訳（自動翻訳）

> 私たちの推論における変動と不確実性のレベル。
> パラメータの表またはグラフ
> 推定値、不確かさ、標準誤差は 1 次元のマージンのみを示していますが、
> 周辺事後分布のグラフは、多くのパラメータを持つモデルでは扱いにくく、また

### 熟語・専門語

- **posterior distribution**: 事後分布。データ観測後の未知量の不確実性を表す分布。
- **uncertainty**: 不確実性。観測・パラメータ・モデル構造・意思決定に残る曖昧さ。

### 要約

- 私たちの推論における変動と不確実性のレベル。

## Chunk 0366

### English（抽出4行）

> fail to capture the interplay between uncertainty and variation in a hierarchical model.
> To start with, we should follow general principles of good statistical practice and graph data and
> ﬁtted models, both for the “exploratory data analysis” purpose of uncovering unexpected patterns
> in the data and also more directly to understand how the model relates to the data used to ﬁt it.

### 日本語訳（自動翻訳）

> 階層モデルにおける不確実性と変動の間の相互作用を捉えることができません。
> まず、適切な統計手法とグラフ データの一般原則に従う必要があります。
> フィッティングされたモデル、どちらも予期せぬパターンを明らかにする「探索的データ分析」目的
> また、モデルが、モデルの適合に使用されるデータとどのように関連しているかをより直接的に理解することもできます。

### 熟語・専門語

- **uncertainty**: 不確実性。観測・パラメータ・モデル構造・意思決定に残る曖昧さ。

### 要約

- 階層モデルにおける不確実性と変動の間の相互作用を捉えることができません。

## Chunk 0367

### English（抽出4行）

> We illustrate some uses of graphical model exploration and summary from an analysis by Ghitza
> and Gelman (2020) of vote preferences in the 2016 U.S. presidential election. Figure 19 shows
> the estimated gender gap in support for the two candidates, ﬁrst displayed as a map and then as
> a scatterplot. The map, which is the natural ﬁrst step to visualizing these estimates, reveals some

### 日本語訳（自動翻訳）

> グラフィカル モデルの探索と Ghitza による分析からの要約のいくつかの使用法を示します。
> およびゲルマン (2020) は、2016 年の米国大統領選挙における投票選好について述べています。図 19 は、
> 2 人の候補者に対する支持率の推定男女差。最初は地図として表示され、次に地図として表示されます。
> 散布図。マップは、これらの推定値を視覚化する自然な最初のステップであり、いくつかのことを明らかにします。

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- グラフィカル モデルの探索と Ghitza による分析からの要約のいくつかの使用法を示します。

## Chunk 0368

### English（抽出4行）

> intriguing geographic patterns which are then explored in a more focused way in the scatterplot.
> Figure 20 evaluates the model by comparing to simpler county-level estimates. This example
> demonstrates a general workﬂow in exploratory graphics, in which the results from inferential
> summary motivates future exploration.

### 日本語訳（自動翻訳）

> 興味深い地理的パターンは、散布図でより焦点を絞った方法で調査されます。
> 図 20 は、より単純な郡レベルの推定値と比較してモデルを評価しています。この例
> 探索的グラフィックスの一般的なワークフローを示します。推論の結果が表示されます。
> 要約は将来の探索の動機になります。

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- 興味深い地理的パターンは、散布図でより焦点を絞った方法で調査されます。

## Chunk 0369

### English（抽出4行）

> Gabry et al. (2019) present some of our ideas on graphics for Bayesian workﬂow, and some of
> this has been implemented in the R package bayesplot (Gabry et al., 2020b, see also Kay, 2020ab,
> Kumar, 2019). Probabilistic programming ultimately has the potential to allow random variables
> to manipulated like any other data objects, with uncertainty implicit in all the plots and calculations

### 日本語訳（自動翻訳）

> ギャブリーら。 (2019) ベイジアン ワークフローのグラフィックスに関するアイデアのいくつかを紹介します。
> これは R パッケージの Bayesplot で実装されています (Gabry et al., 2020b、Kay, 2020ab も参照)
> クマール、2019)。確率的プログラミングは最終的には確率変数を可能にする可能性を秘めています
> すべてのプロットと計算に不確実性が含まれるため、他のデータ オブジェクトと同様に操作できます。

### 熟語・専門語

- **probabilistic programming**: 確率的プログラミング。Stanなどで確率モデルをコードとして記述し推論する方法。
- **uncertainty**: 不確実性。観測・パラメータ・モデル構造・意思決定に残る曖昧さ。

### 要約

- ギャブリーら。

## Chunk 0370

### English（抽出4行）

> (Kerman and Gelman, 2004, 2007), but much more work needs to be done to turn this possibility
> into reality, going beyond point and interval estimation so that we can make full use of the models
> we ﬁt.
> 7.

### 日本語訳（自動翻訳）

> (Kerman と Gelman、2004、2007) しかし、この可能性を変えるにはさらに多くの作業を行う必要があります。
> 点と区間の推定を超えて、モデルを最大限に活用できるように現実化します。
> 私たちはぴったりです。
> 7.

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- (Kerman と Gelman、2004、2007) しかし、この可能性を変えるにはさらに多くの作業を行う必要があります。

## Chunk 0371

### English（抽出4行）

> Modifying a model
> Model building is a language-like task in which the modeler puts together existing components
> (linear, logistic, and exponential functions; additive and multiplicative models; binomial, Poisson,
> and normal distributions; varying coeﬃcients; and so forth) in order to encompass new data

### 日本語訳（自動翻訳）

> モデルの変更
> モデル構築は、モデラーが既存のコンポーネントを組み合わせる言語に似たタスクです。
> (線形関数、ロジスティック関数、指数関数、加法モデルと乗法モデル、二項関数、ポアソン関数、
> そして正規分布。さまざまな係数。など) 新しいデータを包含するため

### 熟語・専門語

- **model building**: モデル構築。仮定・データ構造・prior・likelihoodを組み合わせる工程。

### 要約

- モデルの変更 モデル構築は、モデラーが既存のコンポーネントを組み合わせる言語に似たタスクです。

## Chunk 0372

### English（抽出4行）

> and additional features of existing data, along with links to underlying processes of interest.
> As mentioned in Section 2.2, most parts of the models can be seen as placeholders that allow
> Figure 19: From a model ﬁt to survey data during the 2016 U.S. presidential election campaign:
> (a) estimate of the gender gap among white voters, (b) estimated gender gap plotted vs. Obama’s

### 日本語訳（自動翻訳）

> 既存データの追加機能と、対象となる基礎プロセスへのリンク。
> セクション 2.2 で述べたように、モデルのほとんどの部分は、次のことを可能にするプレースホルダーとして見ることができます。
> 図 19: 2016 年の米国大統領選挙キャンペーン中の調査データに適合したモデルから:
> (a) 白人有権者間の男女差の推定値、(b) オバマ大統領との対比でプロットされた男女差の推定値

### 熟語・専門語

- **ESS**: 有効サンプルサイズ。自己相関を考慮した独立サンプル相当数。

### 要約

- 既存データの追加機能と、対象となる基礎プロセスへのリンク。

## Chunk 0373

### English（抽出4行）

> estimated county-level vote share in 2012 among white votes. The area of each circle is proportional
> to the number of voters in the county, and the colors on the map represent a range going from
> dark purple (no diﬀerence in voting patterns comparing white men and white women) through
> light gray (white women supporting Clinton 7.5 percentage points more than white men) to dark

### 日本語訳（自動翻訳）

> 2012 年の白人投票における郡レベルの推定得票率。各円の面積は比例する
> から郡内の有権者の数まで、地図上の色は以下の範囲を表します。
> 濃い紫（白人男性と白人女性の投票パターンに違いはない）
> ライトグレー（白人女性は白人男性より7.5パーセントポイント高くクリントンを支持）からダークグレー

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- 2012 年の白人投票における郡レベルの推定得票率。

## Chunk 0374

### English（抽出4行）

> green (a white gender gap of 15 percentage points). The striking geographic patterns—a white
> gender gap that is low in much of the south and high in the west and much of the northeast and
> midwest—motivates the scatterplot, which reveals that the white gender gap tends to be highest in
> counties where the white vote is close to evenly split. From Ghitza and Gelman (2020).

### 日本語訳（自動翻訳）

> 緑（白人の男女差は15パーセントポイント）。印象的な幾何学模様、白
> 男女格差は南部の多くの地域で低く、西部と北東部の多くの地域で高い。
> 中西部 - 散布図の動機となり、白人の男女格差が最も高くなる傾向があることがわかります。
> 白人の票がほぼ均等に分かれている郡。ギッツァとゲルマン（2020）より。

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- 緑（白人の男女差は15パーセントポイント）。

## Chunk 0375

### English（抽出4行）

> Figure 20: Evaluation of one aspect of the model shown in Figure 19, comparing county-level
> support for Clinton as estimated from two diﬀerent models. We include this here to illustrate the
> way that graphical methods can be used to summarize, understand, evaluate, and compare ﬁtted
> models. From Ghitza and Gelman (2020).

### 日本語訳（自動翻訳）

> 図 20: 図 19 に示したモデルの一側面の評価、郡レベルの比較
> 2 つの異なるモデルから推定されたクリントンへの支持率。これを説明するためにここに含めます。
> グラフィカルな方法を使用して、適合したデータを要約、理解、評価、比較できる方法
> モデル。ギッツァとゲルマン（2020）より。

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- 図 20: 図 19 に示したモデルの一側面の評価、郡レベルの比較 2 つの異なるモデルから推定されたクリントンへの支持率。

## Chunk 0376

### English（抽出4行）

> replacement or expansion. Alternatively we may ﬁnd the need to use an approximate model or an
> approximate algorithm, as discussed in Section 3.3.
> Model expansion can come in response to new data, failures of models ﬁt to existing data,
> or computational struggles with existing ﬁtting procedures. For the election forecast described in

### 日本語訳（自動翻訳）

> 交換または拡張。あるいは、近似モデルまたは
> セクション 3.3 で説明した近似アルゴリズム。
> モデルの拡張は、新しいデータ、既存のデータに適合するモデルの失敗、
> または、既存のフィッティング手順との計算上の困難。に記載されている選挙予想については、

### 熟語・専門語

- **approximate**: 近似。速度や扱いやすさのため、正確な推論・モデルを緩めること。

### 要約

- 交換または拡張。

## Chunk 0377

### English（抽出4行）

> Gelman, Hullman, et al. (2020), we started with the poll-aggregation model of Linzer (2013) which
> we had adapted in 2016 but with a notable failure of predictions in certain swing states, which we
> attributed to poor modeling of correlations of vote swings between states, along with nonsampling
> errors in the polls (Gelman and Azari, 2017). In our revision we expanded the model to include

### 日本語訳（自動翻訳）

> ゲルマン、ハルマン、他(2020) に続き、Linzer (2013) の投票集計モデルから始めました。
> 私たちは 2016 年に適応していましたが、特定の激動州での予測が著しく失敗しました。
> 非サンプリングに加え、州間の投票変動の相関関係のモデル化が不十分であることが原因と考えられる
> 世論調査の誤り (Gelman and Azari、2017)。私たちの改訂版では、以下を含むモデルを拡張しました。

### 熟語・専門語

- **prediction**: 予測。未知/将来/除外データに対する分布や点推定。

### 要約

- ゲルマン、ハルマン、他(2020) に続き、Linzer (2013) の投票集計モデルから始めました。

## Chunk 0378

### English（抽出4行）

> both these features. Sections 10 and 11 give extended examples of iterative model building and
> evaluation.
> 7.1.
> Constructing a model for the data

### 日本語訳（自動翻訳）

> これら両方の機能。セクション 10 と 11 では、反復モデル構築の拡張例を示します。
> 評価。
> 7.1.
> データのモデルの構築

### 熟語・専門語

- **model building**: モデル構築。仮定・データ構造・prior・likelihoodを組み合わせる工程。

### 要約

- これら両方の機能。

## Chunk 0379

### English（抽出4行）

> In textbook treatments of statistics, the distribution of data given parameters is typically just given.
> In applications, though, we want to set up a data model based on some combination of ﬁt to the
> data (as found in posterior predictive checks) and domain expertise. If the model is being chosen
> from a small menu, we would like to at least be open about that. Often the most important aspect of

### 日本語訳（自動翻訳）

> 教科書的な統計処理では、通常、パラメーターが与えられたデータの分布が与えられるだけです。
> ただし、アプリケーションでは、データへの適合性の組み合わせに基づいてデータ モデルをセットアップしたいと考えます。
> データ (事後予測チェックで見つかる) とドメインの専門知識。モデルを選択している場合
> 小さなメニューについては、少なくともオープンにしたいと考えています。多くの場合、最も重要な側面は、

### 熟語・専門語

- **posterior predictive**: 事後予測。推定後のモデルが観測データの特徴を再現できるかを見る診断。

### 要約

- 教科書的な統計処理では、通常、パラメーターが与えられたデータの分布が与えられるだけです。

## Chunk 0380

### English（抽出4行）

> the data model is not its distributional form but how the data are linked to underlying parameters of
> interest. For example, in election forecasting, our model for polls includes terms for nonsampling
> error for individual polls and for polling averages, following Shirani-Mehr et al. (2018).
> A related challenge arises because data are typically preprocessed before they come to us, so that

### 日本語訳（自動翻訳）

> データ モデルは、その分布形式ではなく、データがその基礎となるパラメータにどのようにリンクされているかです。
> 興味。たとえば、選挙予測では、世論調査のモデルに非サンプリングの項が含まれています。
> 個々の世論調査と世論調査の平均に関する誤差は、Shirani-Mehr らに従っています。 （2018年）。
> データは通常、私たちに届く前に前処理されるため、関連する課題が発生します。

### 熟語・専門語

- **ESS**: 有効サンプルサイズ。自己相関を考慮した独立サンプル相当数。

### 要約

- データ モデルは、その分布形式ではなく、データがその基礎となるパラメータにどのようにリンクされているかです。

## Chunk 0381

### English（抽出4行）

> any generative model is necessarily an approximation. This can arise in meta-analysis or in settings
> where some large set of predictors have been combined into one or two numerical summaries using
> a machine learning algorithm or another dimensionality reduction technique. As always, we need
> to be concerned about data quality, and the most important aspect of the data model can be bias

### 日本語訳（自動翻訳）

> 生成モデルは必ず近似値になります。これはメタ分析または設定で発生する可能性があります
> ここでは、いくつかの大規模な予測子のセットが、次の方法を使用して 1 つまたは 2 つの数値要約に結合されています。
> 機械学習アルゴリズムまたは別の次元削減技術。いつものように、必要なのは
> データの品質を気にする必要があり、データ モデルの最も重要な側面はバイアスである可能性があります

### 熟語・専門語

- **generative model**: 生成モデル。データ生成過程を確率的に記述するモデル。
- **ESS**: 有効サンプルサイズ。自己相関を考慮した独立サンプル相当数。

### 要約

- 生成モデルは必ず近似値になります。

## Chunk 0382

### English（抽出4行）

> rather than what would traditionally be considered measurement error. Understanding this aﬀects
> Bayesian workﬂow in that it can make sense to expand a model to allow for systematic error; we
> give an example in Section 10.5.
> 7.2.

### 日本語訳（自動翻訳）

> 従来は測定誤差と考えられていたものではなく、これを理解すると影響が出ます
> 体系的な誤差を考慮してモデルを拡張することが合理的であるという点でベイジアン ワークフロー。私たち
> セクション 10.5 に例を示します。
> 7.2.

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- 従来は測定誤差と考えられていたものではなく、これを理解すると影響が出ます 体系的な誤差を考慮してモデルを拡張することが合理的であるという点でベイジアン ワークフロー。

## Chunk 0383

### English（抽出4行）

> Incorporating additional data
> It is sometimes said that the most important aspect of a statistical method is not what it does with
> the data, but what data are used. A key part of Bayesian workﬂow is expanding a model to make use
> of more data. This can be as simple as adding regression predictors—but when more parameters

### 日本語訳（自動翻訳）

> 追加データの組み込み
> 統計手法の最も重要な側面は、何を行うかではない、と言われることがあります。
> データではなく、どのようなデータが使用されるか。ベイズ ワークフローの重要な部分は、使用するモデルを拡張することです
> より多くのデータを。これは回帰予測変数を追加するのと同じくらい簡単ですが、パラメータが増えると

### 熟語・専門語

- **ESS**: 有効サンプルサイズ。自己相関を考慮した独立サンプル相当数。

### 要約

- 追加データの組み込み 統計手法の最も重要な側面は、何を行うかではない、と言われることがあります。

## Chunk 0384

### English（抽出4行）

> are added, it can be necessary to assume that not all of them can have a big eﬀect in the model at
> the same time. One way to see this is to consider the addition of a parameter as a relaxation of a
> prior distribution that was previously concentrated at zero. For example, we expanded our election
> model to account for political polarization by adding interaction terms to the regression, allowing

### 日本語訳（自動翻訳）

> が追加される場合、そのすべてがモデルに大きな影響を与えるわけではないことを想定する必要がある場合があります。
> 同じ時間です。これを確認する 1 つの方法は、パラメータの追加をパラメータの緩和として考慮することです。
> 以前はゼロに集中していた事前分布。たとえば、私たちは選挙を拡大しました
> 交互作用項を回帰に追加することで政治的二極化を説明するモデル。

### 熟語・専門語

- **prior distribution**: 事前分布。データ観測前の知識・制約を表す分布。
- **ESS**: 有効サンプルサイズ。自己相関を考慮した独立サンプル相当数。

### 要約

- が追加される場合、そのすべてがモデルに大きな影響を与えるわけではないことを想定する必要がある場合があります。

## Chunk 0385

### English（抽出4行）

> the coeﬃcients for the national economic predictor to be lower in recent years.
> It sometimes happens that we have two forms of measurement of similar data, thus requiring a
> generative model for both data sources. Sometimes this creates technical challenges, as when we
> are combining direct measurements on a sample with population summary statistics, or integrating

### 日本語訳（自動翻訳）

> 国家経済予測の係数は近年低下している。
> 場合によっては、同様のデータに対して 2 つの形式の測定が必要となる場合があります。
> 両方のデータ ソースの生成モデル。場合によっては、これにより技術的な問題が発生することがあります。
> サンプルの直接測定値と母集団概要統計を組み合わせたり、統合したりしている

### 熟語・専門語

- **generative model**: 生成モデル。データ生成過程を確率的に記述するモデル。

### 要約

- 国家経済予測の係数は近年低下している。

## Chunk 0386

### English（抽出4行）

> measurements of diﬀerent quality (for example, Lin et al., 1999), or when information is available
> on partial margins of a table (Deming and Stephan, 1940).
> In Weber et al. (2018), we ﬁt a
> pharmacological model with direct data for a set of patients taking one drug but only average data

### 日本語訳（自動翻訳）

> さまざまな品質の測定 (たとえば、Lin et al.、1999)、または情報が利用可能な場合
> 表の部分的な余白に（デミングとステファン、1940）。
> ウェーバーらでは、 (2018) に当てはめると、
> 1つの薬を服用している一連の患者の直接データを含むが、平均データのみを含む薬理学的モデル

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- さまざまな品質の測定 (たとえば、Lin et al.、1999)、または情報が利用可能な場合 表の部分的な余白に（デミングとステファン、1940）。

## Chunk 0387

### English（抽出4行）

> for a set of patients that had received a competitor’s product. In order to avoid the computational
> cost of modeling as latent data the outcomes of all the averaged patients, we devised an analytic
> method to approximate the relevant integral so that we could include the averaged data in the
> likelihood function.

### 日本語訳（自動翻訳）

> 競合他社の製品の投与を受けた一連の患者を対象としています。計算的な問題を避けるために、
> すべての平均化された患者の転帰を潜在データとしてモデル化するコストを考慮して、私たちは分析手法を考案しました。
> 関連する積分を近似する方法を使用して、平均化されたデータを
> 尤度関数。

### 熟語・専門語

- **likelihood**: 尤度。パラメータが与えられたときデータがどれだけ起こりやすいか。
- **approximate**: 近似。速度や扱いやすさのため、正確な推論・モデルを緩めること。

### 要約

- 競合他社の製品の投与を受けた一連の患者を対象としています。

## Chunk 0388

### English（抽出4行）

> 7.3.
> Working with prior distributions
> Traditionally in Bayesian statistics we speak of noninformative or fully informative priors, but
> neither of these generally exist: a uniform prior contains some information, as it depends on the

### 日本語訳（自動翻訳）

> 7.3.
> 以前のディストリビューションの操作
> 伝統的にベイズ統計では、非有益な事前分布または完全に有益な事前分布について話していますが、
> これらは一般にどちらも存在しません。均一事前分布には、状況に依存するため、いくつかの情報が含まれています。

### 熟語・専門語

- **prior distribution**: 事前分布。データ観測前の知識・制約を表す分布。

### 要約

- 7.3. 以前のディストリビューションの操作 伝統的にベイズ統計では、非有益な事前分布または完全に有益な事前分布について話していますが、 これらは一般にどちらも存在しません。

## Chunk 0389

### English（抽出4行）

> parameterization of the model; a reference prior depends on an assumed asymptotic regime for
> collecting new, ﬁctional data (Berger et al., 2009); and even an informative prior rarely includes all
> available knowledge. Rather, we prefer to think of a ladder of possibilities: (improper) ﬂat prior;
> super-vague but proper prior; very weakly informative prior; generic weakly informative prior;

### 日本語訳（自動翻訳）

> モデルのパラメータ化。基準事前分布は、想定される漸近領域に依存します。
> 新しい架空のデータを収集する (Berger et al., 2009)。そして、有益な事前情報であっても、すべてが含まれることはほとんどありません。
> 利用可能な知識。むしろ、私たちは可能性のはしごを考えることを好みます: (不適切な) フラット事前。
> 非常に曖昧ですが、適切な事前設定。事前の情報提供が非常に弱い。一般的な事前情報が弱く、

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- モデルのパラメータ化。

## Chunk 0390

### English（抽出4行）

> speciﬁc informative prior. For example, our election model includes random walk terms to allow
> variation in opinion at the state and national level. Each of these random walks has a standard
> deviation parameter corresponding to the unexplained variation (on the logit scale) in one day.
> This innovation standard deviation could be given a uniform prior, a super-vague but proper prior

### 日本語訳（自動翻訳）

> 事前に具体的な情報を提供します。たとえば、私たちの選挙モデルには、以下を可能にするランダム ウォーク条件が含まれています。
> 州および国家レベルでの意見の違い。これらのランダム ウォークにはそれぞれ標準があります。
> 1 日の説明のつかない変動 (ロジット スケール上の) に対応する偏差パラメータ。
> このイノベーションの標準偏差には、均一事前分布、つまり非常に曖昧だが適切な事前分布を与えることができます。

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- 事前に具体的な情報を提供します。

## Chunk 0391

### English（抽出4行）

> (for example, normal+(0, 1000), where we are using the notation normal+ to represent the normal
> distribution truncated to be positive), a weak prior (for example, normal+(0, 1) on the percentage
> scale, which would allow unrealistically large day-to-day changes on the order of 0.25 percentage
> points in the probability of support for a candidate, but would still keep the distribution away from

### 日本語訳（自動翻訳）

> (たとえば、normal+(0, 1000)、ここでは法線を表すためにnormal+という表記を使用しています。
> 分布は正になるように切り捨てられます）、弱い事前分布（たとえば、パーセンテージの正規+(0, 1)）
> このスケールでは、0.25 パーセント程度の非現実的に大きな日々の変化が許容されます。
> 候補者を支持する確率は上昇しますが、それでも分布は遠ざかります。

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- (たとえば、normal+(0, 1000)、ここでは法線を表すためにnormal+という表記を使用しています。

## Chunk 0392

### English（抽出4行）

> extreme parameter values), or a more informative prior such as normal+(0, 0.1) which does not
> encapsulate all our prior knowledge but does softly constrain this parameter to within a reasonable
> range. Our point here is that in choosing a prior, one is also choosing the amount of subject-matter
> information to include in the analysis.

### 日本語訳（自動翻訳）

> 極端なパラメータ値）、またはより有益な事前分布（normal+(0, 0.1) など）
> すべての事前知識をカプセル化しますが、このパラメータを妥当な範囲内にソフトに制限します。
> 範囲。ここでのポイントは、事前を選択するということは、主題の量も選択するということです
> 分析に含める情報。

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- 極端なパラメータ値）、またはより有益な事前分布（normal+(0, 0.1) など） すべての事前知識をカプセル化しますが、このパラメータを妥当な範囲内にソフトに制限します。

## Chunk 0393

### English（抽出4行）

> Another way to view a prior distribution, or a statistical model more generally, is as a constraint.
> For example, if we ﬁt a linear model plus a spline or Gaussian process, y = b0 +b1x+g(x)+error,
> where the nonlinear function g has bounded variation, then with a strong enough prior on the g, we
> are ﬁtting a curve that is close to linear. The prior distribution in this example could represent prior

### 日本語訳（自動翻訳）

> 事前分布、つまり統計モデルをより一般的に見るもう 1 つの方法は、制約として見ることです。
> たとえば、線形モデルとスプラインまたはガウス過程を当てはめると、y = b0 +b1x+g(x)+error、
> ここで、非線形関数 g には有限の変動があり、g に十分に強い事前確率がある場合、次のようになります。
> 直線に近い曲線を当てはめています。この例の事前分布は、事前分布を表す可能性があります。

### 熟語・専門語

- **prior distribution**: 事前分布。データ観測前の知識・制約を表す分布。
- **ESS**: 有効サンプルサイズ。自己相関を考慮した独立サンプル相当数。

### 要約

- 事前分布、つまり統計モデルをより一般的に見るもう 1 つの方法は、制約として見ることです。

## Chunk 0394

### English（抽出4行）

> information, or it could just be considered as part of the model speciﬁcation, if there is a desire
> to ﬁt an approximately linear curve. Simpson et al. (2017) provide further discussion on using
> prior distributions to shrink towards simpler models. This also leads to the more general point that
> priors are just like any other part of a statistical model in which they can serve diﬀerent purposes.

### 日本語訳（自動翻訳）

> あるいは、必要に応じてモデル仕様の一部として考慮することもできます。
> ほぼ直線的な曲線にフィットします。シンプソンら。 (2017) の使用に関するさらなる議論を提供します。
> 以前の分布はより単純なモデルに向かって縮小します。これは、より一般的な点にもつながります。
> 事前分布は統計モデルの他の部分とまったく同様で、さまざまな目的に使用できます。

### 熟語・専門語

- **prior distribution**: 事前分布。データ観測前の知識・制約を表す分布。
- **approximate**: 近似。速度や扱いやすさのため、正確な推論・モデルを緩めること。

### 要約

- あるいは、必要に応じてモデル仕様の一部として考慮することもできます。

## Chunk 0395

### English（抽出4行）

> Any clear distinction between model and prior is largely arbitrary and often depends mostly on the
> conceptual background of the one making the distinction.
> The amount of prior information needed to get reasonable inference depends strongly on the
> role of the parameter in the model as well as the depth of the parameter in the hierarchy (Goel and

### 日本語訳（自動翻訳）

> モデルと事前の明確な区別はほとんど恣意的であり、多くの場合、主に
> 区別をする人の概念的な背景。
> 合理的な推論を得るために必要な事前情報の量は、
> モデル内のパラメータの役割と階層内のパラメータの深さ (Goel と

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- モデルと事前の明確な区別はほとんど恣意的であり、多くの場合、主に 区別をする人の概念的な背景。

## Chunk 0396

### English（抽出4行）

> DeGroot, 1981). For instance, parameters that mainly control central quantities (such as the mean
> or the median) typically tolerate vague priors more than scale parameters, which again are more
> forgiving of vague priors than parameters that control tail quantities, such as the shape parameter
> of a generalized extreme value distribution. When a model has a hierarchical structure, parameters

### 日本語訳（自動翻訳）

> デグルート、1981)。たとえば、主に中心量を制御するパラメータ（平均値など）
> または中央値）、通常、スケールパラメータよりも曖昧な事前分布を許容します。
> 形状パラメータなどのテール量を制御するパラメータよりも曖昧な事前分布を許容します。
> 一般化された極値分布の。モデルが階層構造を持つ場合、パラメータは

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- デグルート、1981)。

## Chunk 0397

### English（抽出4行）

> that are closer to the data are typically more willing to indulge vague priors than parameters further
> down the hierarchy.
> In Bayesian workﬂow, priors are needed for a sequence of models. Often as the model becomes
> more complex, all of the priors need to become tighter. The following simple example of multilevel

### 日本語訳（自動翻訳）

> データに近いものは、通常、パラメータをさらに詳細に設定するよりも、あいまいな事前情報を積極的に利用する傾向があります。
> 階層の下にあります。
> ベイジアン ワークフローでは、一連のモデルに事前分布が必要です。多くの場合、モデルになると、
> より複雑になると、すべての事前分布をより厳密にする必要があります。次のマルチレベルの簡単な例

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- データに近いものは、通常、パラメータをさらに詳細に設定するよりも、あいまいな事前情報を積極的に利用する傾向があります。

## Chunk 0398

### English（抽出4行）

> data (see, for example, Raudenbush and Bryk, 2002) shows why this can be necessary.
> Consider a workﬂow where the data are yij, i = 1, . . . , nj, j = 1, . . . , J. Here i indexes the
> observation and j indexes the group. Imagine that for the ﬁrst model in the workﬂow we elect to
> ignore the group structure and use a simple normal distribution for the deviation from the mean.

### 日本語訳（自動翻訳）

> データ (たとえば、Raudenbush と Bryk、2002 年を参照) は、なぜこれが必要なのかを示しています。
> データが yij, i = 1, ... であるワークフローを考えてみましょう。 。 。 、nj、j = 1、. 。 。 、J. ここで私はインデックスを付けます
> 観察値と j はグループのインデックスを付けます。ワークフローの最初のモデルとして次のことを選択すると想像してください。
> グループ構造を無視し、平均からの偏差に単純な正規分布を使用します。

### 熟語・専門語

- **ESS**: 有効サンプルサイズ。自己相関を考慮した独立サンプル相当数。

### 要約

- データ (たとえば、Raudenbush と Bryk、2002 年を参照) は、なぜこれが必要なのかを示しています。

## Chunk 0399

### English（抽出4行）

> In this case some of the information budget will be spent on estimating the overall mean and some
> of it is spent on the observation standard deviation. If we have a moderate amount of data, the
> mean will be approximately ¯y = Pn
> i=1 yi/n regardless of how weak the prior is. Furthermore,

### 日本語訳（自動翻訳）

> この場合、情報予算の一部は全体平均の推定に費やされ、残りの情報予算は全体の平均値の推定に費やされます。
> そのうちは観測標準偏差に費やされます。適度な量のデータがある場合、
> 平均はおおよそ ￣y = Pn になります
> 事前分布がどれほど弱いかに関係なく、i=1 yi/n。さらに、

### 熟語・専門語

- **ESS**: 有効サンプルサイズ。自己相関を考慮した独立サンプル相当数。
- **approximate**: 近似。速度や扱いやすさのため、正確な推論・モデルを緩めること。

### 要約

- この場合、情報予算の一部は全体平均の推定に費やされ、残りの情報予算は全体の平均値の推定に費やされます。

## Chunk 0400

### English（抽出4行）

> the predictive distribution for a new observation will be approximately normal(¯y, s), where s is
> the sample standard deviation. Again, this will be true for most sensible priors on the observation
> standard deviation, regardless of how vague they are.
> If the next step in the workﬂow is to allow the mean to vary by group using a multilevel model,

### 日本語訳（自動翻訳）

> 新しい観測値の予測分布はほぼ正規分布 (￣y, s) になります。ここで、s は
> サンプルの標準偏差。繰り返しますが、これは観察に関するほとんどの賢明な事前分布に当てはまります。
> どんなに曖昧であっても標準偏差。
> ワークフローの次のステップが、マルチレベル モデルを使用してグループごとに平均値を変更できるようにする場合、

### 熟語・専門語

- **ESS**: 有効サンプルサイズ。自己相関を考慮した独立サンプル相当数。
- **approximate**: 近似。速度や扱いやすさのため、正確な推論・モデルを緩めること。

### 要約

- 新しい観測値の予測分布はほぼ正規分布 (￣y, s) になります。

## Chunk 0401

### English（抽出4行）

> then the information budget still needs to be divided between the standard deviation and the mean.
> However, the model now has J + 1 extra parameters (one for each group plus one for the standard
> deviation across groups) so the budget for the mean needs to be further divided to model the group
> means, whereas the budget for the standard deviation needs to be split between the within group

### 日本語訳（自動翻訳）

> その場合でも、情報バジェットを標準偏差と平均の間で分割する必要があります。
> ただし、モデルには J + 1 個の追加パラメータ (各グループに 1 つと標準パラメータに 1 つ) が追加されました。
> グループ間の偏差）そのため、グループをモデル化するには平均値の予算をさらに分割する必要があります
> これは、標準偏差の予算をグループ内で分割する必要があることを意味します。

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- その場合でも、情報バジェットを標準偏差と平均の間で分割する必要があります。

## Chunk 0402

### English（抽出4行）

> variation and the between group variation. But we still have the same amount of data, so we need
> to be careful to ensure that this model expansion does not destabilize our estimates. This means
> that as well as putting appropriate priors on our new parameters, we probably need to tighten up
> the priors on the overall mean and observation standard deviation, lest a lack of information lead to

### 日本語訳（自動翻訳）

> 変動とグループ間の変動。しかし、依然として同じ量のデータがあるため、次のことが必要です。
> このモデルの拡張によって推定が不安定にならないように注意してください。これはつまり、
> 新しいパラメータに適切な事前分布を設定するだけでなく、おそらく強化する必要があるでしょう。
> 情報の欠如によって問題が発生しないように、全体の平均と観察の標準偏差に関する事前分布

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- 変動とグループ間の変動。

## Chunk 0403

### English（抽出4行）

> nonsense estimates.
> A related issue is the concentration of measure in higher-dimensional space. For example in
> regression with an increasing number of predictors, the prior on the vector of coeﬃcients needs to
> have higher density near the mode if we want to keep most of the prior mass near the mode (as

### 日本語訳（自動翻訳）

> ナンセンスな見積もり。
> 関連する問題は、高次元空間における測定の集中です。たとえば、
> 予測子の数が増加する回帰では、係数ベクトルの事前計算が必要になります。
> 以前の質量の大部分をモード近くに保持したい場合は、モード近くの密度が高くなります (

### 熟語・専門語

- **ESS**: 有効サンプルサイズ。自己相関を考慮した独立サンプル相当数。

### 要約

- ナンセンスな見積もり。

## Chunk 0404

### English（抽出4行）

> the volume further away from the mode increases faster as dimension increases; see, for example,
> Piironen and Vehtari, 2017). Consider linear or logistic regression and what happens to the prior
> on R2 if the marginal prior on weights is ﬁxed. If we want the prior on R2 to stay ﬁxed, the
> prior on weights needs to get tighter. Figure 21 uses prior predictive checking (see Section 2.4) to

### 日本語訳（自動翻訳）

> モードから離れると、次元が増加するにつれてボリュームがより速く増加します。たとえば、次を参照してください。
> ピイロネンとヴェフタリ、2017)。線形回帰またはロジスティック回帰と、前の回帰に何が起こるかを検討します。
> 重みの限界事前分布が固定されている場合、R2 で。 R2 の事前分布を固定したままにしたい場合は、
> 事前にウェイトを厳しくする必要があります。図 21 では、事前の予測チェック (セクション 2.4 を参照) を使用して、

### 熟語・専門語

- **prior predictive**: 事前予測。データを見る前のpriorだけで生成される予測分布を確認する診断。
- **ESS**: 有効サンプルサイズ。自己相関を考慮した独立サンプル相当数。

### 要約

- モードから離れると、次元が増加するにつれてボリュームがより速く増加します。

## Chunk 0405

### English（抽出4行）

> show how the usual weak prior on 26 weights in linear regression corresponds to a prior strongly
> favoring higher R2 values, aﬀecting also the posterior. From that perspective, weakly informative
> but independent priors may jointly be strongly informative if they appear in large numbers.
> Priors must be speciﬁed for each model within a workﬂow. An expanded model can require

### 日本語訳（自動翻訳）

> 線形回帰における 26 の重みの通常の弱い事前分布がどのように強い事前分布に対応するかを示します。
> より高い R2 値が優先され、事後分布にも影響します。その観点からすると、情報としては弱いですが、
> しかし、独立した事前分布が大量に出現する場合、それらが結合すると強力な情報となる可能性があります。
> 事前分布はワークフロー内のモデルごとに指定する必要があります。拡張モデルには必要な場合があります

### 熟語・専門語

- **ESS**: 有効サンプルサイズ。自己相関を考慮した独立サンプル相当数。

### 要約

- 線形回帰における 26 の重みの通常の弱い事前分布がどのように強い事前分布に対応するかを示します。

## Chunk 0406

### English（抽出4行）

> additional thought regarding parameterization. For example, when going from normal(µ, σ) to
> a t-distribution tν(µ, σ) with ν degrees of freedom, we have to be careful with the prior on σ.
> The scale parameter σ looks the same for the two models, but the variance of the t distribution
> is actually

### 日本語訳（自動翻訳）

> パラメータ化に関する追加の考え。たとえば、normal(μ, σ) から
> ν 自由度の t 分布 tν(μ, σ) では、σ の事前分布に注意する必要があります。
> スケール パラメーター σ は 2 つのモデルで同じに見えますが、t 分布の分散は
> 実は

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

> ν
> σ2ではなくν−2σ2。したがって、ν が小さい場合、σ は残差に近づきません。
> 標準偏差。
> 一般に、モデル内のすべてのパラメータよりも先にジョイントを考慮する必要があります。

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- ν σ2ではなくν−2σ2。

## Chunk 0408

### English（抽出4行）

> to be assessed in the context of the generative model for the data, lest unfortunate cancellations
> or resonances lead to less stabilizing or more informative priors than the modeler actually wants
> (Gelman et al., 2017, Kennedy et al., 2019). As discussed in Section 2.4, prior predictive checking
> is a good general approach to exploring and understanding a prior distribution in the context of a

### 日本語訳（自動翻訳）

> 不幸なキャンセルを避けるために、データの生成モデルのコンテキストで評価されること
> または、共鳴により、モデラーが実際に望んでいるよりも安定性が低下したり、より有益な事前分布が生成されたりします。
> (Gelman et al.、2017、Kennedy et al.、2019)。セクション 2.4 で説明したように、事前の予測チェック
> これは、事前分布を調査して理解するための優れた一般的なアプローチです。

### 熟語・専門語

- **prior predictive**: 事前予測。データを見る前のpriorだけで生成される予測分布を確認する診断。
- **prior distribution**: 事前分布。データ観測前の知識・制約を表す分布。
- **generative model**: 生成モデル。データ生成過程を確率的に記述するモデル。
- **ESS**: 有効サンプルサイズ。自己相関を考慮した独立サンプル相当数。

### 要約

- 不幸なキャンセルを避けるために、データの生成モデルのコンテキストで評価されること または、共鳴により、モデラーが実際に望んでいるよりも安定性が低下したり、より有益な事前分布が生成されたりします。

## Chunk 0409

### English（抽出4行）

> particular data model.
> The above examples carry particular messages about priors but also a meta-message about how
> we think about workﬂow when constructing statistical models. Phrases such as “the information
> budget still needs to be divided” represent important but somewhat informal decisions we make

### 日本語訳（自動翻訳）

> 特定のデータモデル。
> 上記の例は、事前分布に関する特定のメッセージだけでなく、どのようにするかについてのメタ メッセージも伝えます。
> 統計モデルを構築するときは、ワークフローについて考えます。 「その情報」などのフレーズ
> 「予算はまだ分割する必要がある」は、私たちが下す重要ではあるがやや非公式な決定を表しています

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

> 後部
> 以前
> 0.25
> 0.5

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- 後部 以前 0.25 0.5

## Chunk 0411

### English（抽出4行）

> 0.75
> 0.25
> 0.5
> 0.75

### 日本語訳（自動翻訳）

> 0.75
> 0.25
> 0.5
> 0.75

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- 0.75 0.25 0.5 0.75

## Chunk 0412

### English（抽出4行）

> Bayesian R^2
> Posterior
> Prior
> 0.25

### 日本語訳（自動翻訳）

> ベイジアン R^2
> 後部
> 以前
> 0.25

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- ベイジアン R^2 後部 以前 0.25

## Chunk 0413

### English（抽出4行）

> 0.5
> 0.75
> 0.25
> 0.5

### 日本語訳（自動翻訳）

> 0.5
> 0.75
> 0.25
> 0.5

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- 0.5 0.75 0.25 0.5

## Chunk 0414

### English（抽出4行）

> 0.75
> Bayesian R^2
> Posterior
> Prior

### 日本語訳（自動翻訳）

> 0.75
> ベイジアン R^2
> 後部
> 以前

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- 0.75 ベイジアン R^2 後部 以前

## Chunk 0415

### English（抽出4行）

> 0.25
> 0.5
> 0.75
> 0.25

### 日本語訳（自動翻訳）

> 0.25
> 0.5
> 0.75
> 0.25

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- 0.25 0.5 0.75 0.25

## Chunk 0416

### English（抽出4行）

> 0.5
> 0.75
> Bayesian R^2
> Figure 21: Prior and posterior distribution of Bayesian R2 for the regression predicting student

### 日本語訳（自動翻訳）

> 0.5
> 0.75
> ベイジアン R^2
> 図 21: 回帰予測学生のベイジアン R2 の事前分布と事後分布

### 熟語・専門語

- **posterior distribution**: 事後分布。データ観測後の未知量の不確実性を表す分布。
- **ESS**: 有効サンプルサイズ。自己相関を考慮した独立サンプル相当数。

### 要約

- 0.5 0.75 ベイジアン R^2 図 21: 回帰予測学生のベイジアン R2 の事前分布と事後分布

## Chunk 0417

### English（抽出4行）

> grades from 26 predictors, using three diﬀerent priors for the coeﬃcients: (a) default weak prior,
> (b) normal prior scaled with the number of predictors, and (c) regularized horseshoe prior. From
> Section 12.7 of Gelman, Hill, and Vehtari (2020).
> about how much eﬀort we put in to include prior information. Such concerns are not always clear

### 日本語訳（自動翻訳）

> 係数に 3 つの異なる事前分布を使用して、26 個の予測子からグレードを付けます: (a) デフォルトの弱い事前分布、
> (b) 予測子の数でスケーリングされた正規事前分布、および (c) 正規化されたホースシュー事前分布。から
> Gelman、Hill、Vehtari (2020) のセクション 12.7。
> 事前情報を含めるためにどれだけの労力を費やしたかについて。このような懸念は必ずしも明確ではありません

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- 係数に 3 つの異なる事前分布を使用して、26 個の予測子からグレードを付けます: (a) デフォルトの弱い事前分布、 (b) 予測子の数でスケーリングされた正規事前分布、および (c) 正規化されたホースシュー事前分布。

## Chunk 0418

### English（抽出4行）

> in articles or textbooks that present the ﬁnal model as is, without acknowledging the tradeoﬀs and
> choices that have been made.
> 7.4.
> A topology of models

### 日本語訳（自動翻訳）

> トレードオフを認識せずに、最終モデルをそのまま提示する記事や教科書では、
> 行われた選択。
> 7.4.
> モデルのトポロジー

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- トレードオフを認識せずに、最終モデルをそのまま提示する記事や教科書では、 行われた選択。

## Chunk 0419

### English（抽出4行）

> Consider a class of models, for simplicity in some particular restricted domain such as autoregressive
> moving average (ARMA) models, binary classiﬁcation trees, or linear regressions with some ﬁxed
> set of input variables. The models in any of these frameworks can be structured as a partial ordering:
> for example, AR(1) is simpler than AR(2) which is simpler than ARMA(2,1), and MA(1) is also

### 日本語訳（自動翻訳）

> 自己回帰などの特定の制限されたドメインを簡略化するために、モデルのクラスを検討します。
> 移動平均 (ARMA) モデル、二値分類ツリー、または一部の固定を含む線形回帰
> 入力変数のセット。これらのフレームワークのモデルはいずれも、部分順序付けとして構造化できます。
> たとえば、AR(1) は AR(2) よりも単純であり、AR(2) は ARMA(2,1) よりも単純であり、MA(1) もまた

### 熟語・専門語

- **ESS**: 有効サンプルサイズ。自己相関を考慮した独立サンプル相当数。

### 要約

- 自己回帰などの特定の制限されたドメインを簡略化するために、モデルのクラスを検討します。

## Chunk 0420

### English（抽出4行）

> simpler than ARMA(2,1), but AR(1) and MA(1) are not themselves ordered. Similarly, tree splits
> form a partial ordering, and the 2k possibilities of inclusion or exclusion in linear regression can be
> structured as the corners of a cube. As these examples illustrate, each of these model frameworks
> has its own topology or network structure as determined by the models in the class and their partial

### 日本語訳（自動翻訳）

> ARMA(2,1) より単純ですが、AR(1) と MA(1) 自体は順序付けされていません。木も同様に分かれます
> 部分的な順序付けを形成し、線形回帰における包含または除外の 2k の可能性が考えられます。
> 立方体の角として構造化されています。これらの例が示すように、これらのモデル フレームワークはそれぞれ
> クラス内のモデルとその部分的なモデルによって決定される独自のトポロジーまたはネットワーク構造を持ちます。

### 熟語・専門語

- **ESS**: 有効サンプルサイズ。自己相関を考慮した独立サンプル相当数。

### 要約

- ARMA(2,1) より単純ですが、AR(1) と MA(1) 自体は順序付けされていません。

## Chunk 0421

### English（抽出4行）

> ordering.
> We speak of this as a topology of models rather than a probability space because we are not
> necessarily interested in assigning probabilities to the individual models. Our interest here is not
> in averaging over models but in navigating among them, and the topology refers to the connections

### 日本語訳（自動翻訳）

> 注文すること。
> 私たちはこれを確率空間ではなくモデルのトポロジーとして話します。
> 必然的に、個々のモデルに確率を割り当てることに関心があります。ここでの私たちの関心はそうではありません
> モデル全体の平均化だけでなく、モデル間を移動する際にも使用され、トポロジは接続を指します。

### 熟語・専門語

- **ESS**: 有効サンプルサイズ。自己相関を考慮した独立サンプル相当数。

### 要約

- 注文すること。

## Chunk 0422

### English（抽出4行）

> between models and between parameters in neighboring models in the network.
> An example implementation of this idea is the Automatic Statistician (Hwang et al., 2016,
> Gharamani et al., 2019), which searches through models in speciﬁed but open-ended classes (for
> example, time series models and linear regression models), using inference and model criticism

### 日本語訳（自動翻訳）

> モデル間、およびネットワーク内の隣接するモデルのパラメータ間。
> このアイデアの実装例は、Automatic Statistician です (Hwang et al.、2016、
> Gharamani et al.、2019)、指定されているが制限のないクラス内のモデルを検索します (
> 時系列モデルや線形回帰モデルなど)、推論とモデル批判を使用

### 熟語・専門語

- **ESS**: 有効サンプルサイズ。自己相関を考慮した独立サンプル相当数。

### 要約

- モデル間、およびネットワーク内の隣接するモデルのパラメータ間。

## Chunk 0423

### English（抽出4行）

> to explore the model and data space. We believe such algorithms can be better understood and,
> ultimately, improved, through a more formal understanding of the topology of models induced by
> a statistical modeling language. From another direction are menu-based packages such as Prophet
> (Taylor and Lethem, 2018) that allow users to put together models (in this case, for time series

### 日本語訳（自動翻訳）

> モデルとデータ空間を探索します。私たちは、そのようなアルゴリズムをよりよく理解できると信じています。
> 最終的には、
> 統計モデリング言語。別の方向からは、Prophet などのメニューベースのパッケージがあります。
> (Taylor および Lethem、2018) これにより、ユーザーはモデル (この場合は時系列) をまとめることができます。

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- モデルとデータ空間を探索します。

## Chunk 0424

### English（抽出4行）

> forecasting) from some set of building blocks. It is important in such packages not just to be
> able to build and ﬁt these models but to understand each model in comparison to simpler or more
> complicated variants ﬁt to the same data.
> However, unlike combining variables, where in many cases a simple and often automated

### 日本語訳（自動翻訳）

> 予測) いくつかの構成要素のセットから。このようなパッケージでは、単に
> これらのモデルを構築して適合させることができるが、各モデルをより単純なモデルまたはより多くのモデルと比較して理解することができる
> 複雑なバリアントは同じデータに適合します。
> ただし、変数の結合とは異なり、多くの場合、単純で自動化されることが多くなります。

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- 予測) いくつかの構成要素のセットから。

## Chunk 0425

### English（抽出4行）

> additive model is enough, here each model itself is a high dimensional object. The outputs from
> diﬀerent models, as probabilistic random variables, can be added, multiplied, linearly mixed, log-
> linearly-mixed, pointwisely-mixed, etc, which is within the choice of model topology we need to
> specify.

### 日本語訳（自動翻訳）

> 加算モデルで十分です。ここでは、各モデル自体が高次元のオブジェクトです。からの出力
> さまざまなモデルを確率的確率変数として加算、乗算、線形混合、対数変換することができます。
> 線形混合、点ごと混合など、これは必要なモデル トポロジの選択の範囲内です。
> 指定します。

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- 加算モデルで十分です。

## Chunk 0426

### English（抽出4行）

> In addition, each model within a framework has its own internal structure involving parameters
> that can be estimated from data. And, importantly, the parameters within diﬀerent models in the
> network can “talk with each other” in the sense of having a shared, observable meaning outside
> the conﬁnes of the model itself. In machine learning and applied statistics, two familiar examples

### 日本語訳（自動翻訳）

> さらに、フレームワーク内の各モデルにはパラメータを含む独自の内部構造があります。
> それはデータから推定できます。そして重要なのは、さまざまなモデル内のパラメータです。
> ネットワークは、外部で共有された観察可能な意味を持つという意味で「互いに会話」することができます。
> モデル自体の範囲。機械学習と応用統計における 2 つのよく知られた例

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- さらに、フレームワーク内の各モデルにはパラメータを含む独自の内部構造があります。

## Chunk 0427

### English（抽出4行）

> with inferential quantities that are shared across models are forecasting and causal inference. In
> forecasting, an increasingly complicated set of procedures can be used for a particular predictive
> goal. And in causal inference, a treatment eﬀect can be estimated using a series of regressions,
> starting from a simple diﬀerence and moving to elaborate interaction models adjusting for diﬀer-

### 日本語訳（自動翻訳）

> モデル間で共有される推論量は、予測と因果推論です。で
> 予測の場合、ますます複雑になる一連の手順を特定の予測に使用できるようになります。
> 目標。そして因果推論では、一連の回帰を使用して治療効果を推定できます。
> 単純な差異から始まり、差異を調整する複雑な相互作用モデルに移行します。

### 熟語・専門語

- **ESS**: 有効サンプルサイズ。自己相関を考慮した独立サンプル相当数。

### 要約

- モデル間で共有される推論量は、予測と因果推論です。

## Chunk 0428

### English（抽出4行）

> ences between observed treated and control groups. Recall that causal inferences are a special case
> of predictions involving counterfactuals; see, for example, Morgan and Winship (2014).
> Thus, the topology of statistical or machine-learning models includes a partial ordering of
> models, and connections between parameters or functions of parameters and data across diﬀerent

### 日本語訳（自動翻訳）

> 観察された治療群と対照群の間の差異。因果推論は特殊なケースであることを思い出してください
> 反事実を含む予測。たとえば、Morgan と Winship (2014) を参照してください。
> したがって、統計モデルまたは機械学習モデルのトポロジーには、部分的な順序付けが含まれます。
> モデル、およびパラメータまたはパラメータの関数とさまざまなデータ間の接続

### 熟語・専門語

- **prediction**: 予測。未知/将来/除外データに対する分布や点推定。

### 要約

- 観察された治療群と対照群の間の差異。

## Chunk 0429

### English（抽出4行）

> models within the larger framework. Another twist is that prior distributions add a continuous
> dimension to the structure, bridging between models.
> 8.
> Understanding and comparing multiple models

### 日本語訳（自動翻訳）

> より大きなフレームワーク内のモデル。もう 1 つの工夫は、事前分布により連続的な分布が追加されることです。
> 構造への寸法を調整し、モデル間の橋渡しをします。
> 8.
> 複数のモデルの理解と比較

### 熟語・専門語

- **prior distribution**: 事前分布。データ観測前の知識・制約を表す分布。

### 要約

- より大きなフレームワーク内のモデル。

## Chunk 0430

### English（抽出4行）

> 8.1.
> Visualizing models in relation to each other
> The key aspect of Bayesian workﬂow, which takes it beyond Bayesian data analysis, is that we
> are ﬁtting many models while working on a single problem. We are not talking here about model

### 日本語訳（自動翻訳）

> 8.1.
> モデルを相互に関連付けて視覚化する
> ベイジアン データ分析を超えたベイジアン ワークフローの重要な側面は、
> 単一の問題に取り組みながら、多くのモデルを当てはめています。ここではモデルについて話しているのではありません

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- 8.1. モデルを相互に関連付けて視覚化する ベイジアン データ分析を超えたベイジアン ワークフローの重要な側面は、 単一の問題に取り組みながら、多くのモデルを当てはめています。

## Chunk 0431

### English（抽出4行）

> selection or model averaging but rather of the use of a series of ﬁtted models to better understand
> each one. In the words of Wickham, Cook, and Hofmann (2015), we seek to “explore the process
> of model ﬁtting, not just the end result.” We ﬁt multiple models for several reasons, including:
> • It can be hard to ﬁt and understand a big model, so we will build up to it from simple models.

### 日本語訳（自動翻訳）

> 選択やモデルの平均化ではなく、より深く理解するために一連の適合モデルを使用すること
> それぞれ。ウィッカム、クック、ホフマン (2015) の言葉を借りれば、私たちは「プロセスを探求する」ことを目指しています。
> 最終結果だけでなく、モデルのフィッティングを重視します。」以下のようないくつかの理由から、複数のモデルを適合させます。
> • 大きなモデルを当てはめて理解するのは難しい場合があるため、単純なモデルから構築していきます。

### 熟語・専門語

- **ESS**: 有効サンプルサイズ。自己相関を考慮した独立サンプル相当数。

### 要約

- 選択やモデルの平均化ではなく、より深く理解するために一連の適合モデルを使用すること それぞれ。

## Chunk 0432

### English（抽出4行）

> • When building our models, we make a lot of mistakes: typos, coding errors, conceptual
> errors (for example not realizing that the observations don’t contain useful information for
> some parts of the model), etc.
> • As we get more data, we typically expand our models accordingly. For example, if we’re doing

### 日本語訳（自動翻訳）

> • モデルを構築するとき、タイプミス、コーディングエラー、概念上の間違いなど、多くの間違いを犯します。
> エラー（たとえば、観測値に有益な情報が含まれていないことに気づかない）
> モデルの一部）など。
> • より多くのデータを取得すると、通常はそれに応じてモデルを拡張します。たとえば、次のことを行う場合

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- • モデルを構築するとき、タイプミス、コーディングエラー、概念上の間違いなど、多くの間違いを犯します。

## Chunk 0433

### English（抽出4行）

> pharmacology and we get data on a new group of patients, we might let certain parameters
> vary by group.
> • Often we ﬁt a model that is mathematically well speciﬁed, but once we ﬁt it to data we realize
> that there’s more we can do, so we expand it.

### 日本語訳（自動翻訳）

> 薬理学を研究し、新しい患者グループに関するデータを取得すると、特定のパラメータを使用できる可能性があります。
> グループによって異なります。
> • 多くの場合、私たちは数学的に明確に指定されたモデルを当てはめますが、それをデータに当てはめてみると次のことに気づきます。
> もっとできることがあるので、それを広げていきます。

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- 薬理学を研究し、新しい患者グループに関するデータを取得すると、特定のパラメータを使用できる可能性があります。

## Chunk 0434

### English（抽出4行）

> • Relatedly, when we ﬁrst ﬁt a model, we often put it together with various placeholders. We’re
> often starting with weak priors and making them stronger, or starting with strong priors and
> relaxing them.
> −2

### 日本語訳（自動翻訳）

> • これに関連して、最初にモデルを適合させるとき、多くの場合、モデルをさまざまなプレースホルダーと組み合わせます。私たちは
> 多くの場合、弱い事前分布から始めてそれを強化したり、強い事前分布から始めて、
> 彼らをリラックスさせます。
> −2

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- • これに関連して、最初にモデルを適合させるとき、多くの場合、モデルをさまざまなプレースホルダーと組み合わせます。

## Chunk 0435

### English（抽出4行）

> −1
> Complexity of model
> Inference for quantity of interest
> simpler

### 日本語訳（自動翻訳）

> −1
> モデルの複雑さ
> 関心のある量の推論
> より単純な

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- −1 モデルの複雑さ 関心のある量の推論 より単純な

## Chunk 0436

### English（抽出4行）

> more complex
> Figure 22: Hypothetical graph comparing inferences for a quantity of interest across multiple
> models. The goal here is not to perform model selection or model averaging but to understand
> how inference for a quantity of interest changes as we move from a simple comparison (on the left

### 日本語訳（自動翻訳）

> より複雑な
> 図 22: 複数の関心量の推論を比較する仮説のグラフ
> モデル。ここでの目標は、モデルの選択やモデルの平均化を実行することではなく、理解することです。
> 単純な比較 (左側) から移行するにつれて、対象量の推論がどのように変化するか

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- より複雑な 図 22: 複数の関心量の推論を比較する仮説のグラフ モデル。

## Chunk 0437

### English（抽出4行）

> side of the graph) through the ﬁnal model (on the right side of the graph), going through various
> intermediate alternatives.
> • We’ll check a model, ﬁnd problems, and then expand or replace it. This is part of “Bayesian
> data analysis”; the extra “workﬂow” part is that we still keep the old model, not for the

### 日本語訳（自動翻訳）

> グラフの右側）最終モデル（グラフの右側）を介して、さまざまなプロセスを経ます
> 中間の代替案。
> • モデルをチェックし、問題を見つけて、拡張または置き換えます。これは「ベイジアン」の一部です。
> データ分析」。追加の「ワークフロー」部分は、古いモデルを引き続き維持することであり、

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- グラフの右側）最終モデル（グラフの右側）を介して、さまざまなプロセスを経ます 中間の代替案。

## Chunk 0438

### English（抽出4行）

> purpose of averaging but for the purpose of understanding what we are doing.
> • Sometimes we ﬁt simple models as comparisons. For example, if you’re doing a big regression
> for causal inference, you’ll also want to do a simple unadjusted comparison and then see what
> the adjustments have done.

### 日本語訳（自動翻訳）

> 平均することが目的ですが、私たちが何をしているのかを理解することが目的です。
> • 比較として単純なモデルを当てはめることもあります。たとえば、大きな回帰を行っている場合、
> 因果推論の場合は、単純な未調整の比較を行って、結果を確認することもできます。
> 調整は完了しました。

### 熟語・専門語

- **ESS**: 有効サンプルサイズ。自己相関を考慮した独立サンプル相当数。

### 要約

- 平均することが目的ですが、私たちが何をしているのかを理解することが目的です。

## Chunk 0439

### English（抽出4行）

> • The above ideas are listed as being motivated by statistical considerations, but sometimes
> we’re jolted into action because of computational problems.
> Given that we are ﬁtting multiple models, we also have to be concerned with researcher degrees of
> freedom (Simmons et al., 2011), most directly from overﬁtting if a single best model is picked, or

### 日本語訳（自動翻訳）

> • 上記のアイデアは統計的考察によって動機付けられているものとしてリストされていますが、場合によっては
> 計算上の問題により、私たちは行動を起こさなければなりません。
> 複数のモデルを当てはめていることを考えると、研究者の学位も考慮する必要があります。
> 自由 (Simmons et al., 2011)、最も直接的には、単一の最良のモデルが選択された場合の過剰適合から生じる、または

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- • 上記のアイデアは統計的考察によって動機付けられているものとしてリストされていますが、場合によっては 計算上の問題により、私たちは行動を起こさなければなりません。

## Chunk 0440

### English（抽出4行）

> more subtly that if we are not careful, we can consider our inferences from a set of ﬁtted models to
> bracket some total uncertainty, without recognizing that there are other models we could have ﬁt.
> This concern arises in our election forecasting model, where ultimately we only have a handful of
> past presidential elections with which to calibrate our predictions.

### 日本語訳（自動翻訳）

> もっと微妙なことですが、注意しないと、一連の適合モデルからの推論を次のように考慮してしまう可能性があります。
> 適合できる他のモデルがあることを認識せずに、完全な不確実性をひとまとめにしてしまいます。
> この懸念は、最終的にはほんの一握りの選挙予測モデルで発生します。
> 私たちの予測を調整するための過去の大統領選挙。

### 熟語・専門語

- **uncertainty**: 不確実性。観測・パラメータ・モデル構造・意思決定に残る曖昧さ。
- **prediction**: 予測。未知/将来/除外データに対する分布や点推定。

### 要約

- もっと微妙なことですが、注意しないと、一連の適合モデルからの推論を次のように考慮してしまう可能性があります。

## Chunk 0441

### English（抽出4行）

> Figure 22 illustrates the basic idea: the diagram could represent, for example, a causal eﬀect
> estimated with a sequence of increasingly complicated models, starting with a simple treatment-
> control comparison and proceeding through a series of adjustments. Even if the ultimate interest
> is only in the ﬁnal model, it can be useful to understand how the inference changes as adjustments

### 日本語訳（自動翻訳）

> 図 22 は基本的な考え方を示しています。この図は、たとえば因果関係を表すことができます。
> 単純な処理から始めて、ますます複雑になる一連のモデルを使用して推定します。
> 比較を制御し、一連の調整を進めます。たとえ究極の利益だったとしても
> は最終モデルにのみ存在するため、調整によって推論がどのように変化するかを理解するのに役立ちます

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- 図 22 は基本的な考え方を示しています。

## Chunk 0442

### English（抽出4行）

> are added.
> Following the proposed workﬂow and exploring the topology of models can often lead us to
> multiple models that pass all the checks. Instead of selecting just one model, we can perform a
> multiverse analysis and use all of the models and see how the conclusions change across the models

### 日本語訳（自動翻訳）

> が追加されます。
> 提案されたワークフローに従い、モデルのトポロジーを調査すると、多くの場合、
> すべてのチェックに合格した複数のモデル。モデルを 1 つだけ選択する代わりに、次のことを実行できます。
> 多元宇宙分析を行い、すべてのモデルを使用し、モデル間で結論がどのように変化するかを確認します。

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- が追加されます。

## Chunk 0443

### English（抽出4行）

> Freq.
> frequentist all
> frequentist cLOF
> REN: BBS10 more frequent than BBS1

### 日本語訳（自動翻訳）

> 周波数
> 頻度主義者のすべて
> 頻度主義者 cLOF
> REN: BBS10 は BBS1 よりも頻度が高い

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- 周波数 頻度主義者のすべて 頻度主義者 cLOF REN: BBS10 は BBS1 よりも頻度が高い

## Chunk 0444

### English（抽出4行）

> REN: BBS2 more frequent than BBS1
> REN: BBS2,7,9 more frequent than BBS1,4,8
> REN: BBSome genes differ
> CI: BBS7 more frequent than others

### 日本語訳（自動翻訳）

> REN: BBS2 は BBS1 よりも頻繁に利用されます
> REN: BBS2、7、9 は BBS1、4、8 よりも頻繁です
> REN: BBいくつかの遺伝子が異なります
> CI: BBS7 は他よりも頻繁に利用されます

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- REN: BBS2 は BBS1 よりも頻繁に利用されます REN: BBS2、7、9 は BBS1、4、8 よりも頻繁です REN: BBいくつかの遺伝子が異なります CI: BBS7 は他よりも頻繁に利用されます

## Chunk 0445

### English（抽出4行）

> CI: BBSome more frequent than BBS3
> PD: BBS10 more frequent than BBS1
> PD: BBS2 more frequent than BBS1
> BBSome genes differ

### 日本語訳（自動翻訳）

> CI: BBSome は BBS3 よりも頻繁です
> PD: BBS10 は BBS1 よりも頻度が高い
> PD: BBS2 は BBS1 よりも頻度が高い
> BBいくつかの遺伝子が異なります

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- CI: BBSome は BBS3 よりも頻繁です PD: BBS10 は BBS1 よりも頻度が高い PD: BBS2 は BBS1 よりも頻度が高い BBいくつかの遺伝子が異なります

## Chunk 0446

### English（抽出4行）

> BBS4 most #phenotypes
> BBS4 top odds
> BBS3 less severe than Chaperonins
> BBS3 less severe than BBSome

### 日本語訳（自動翻訳）

> BBS4 で最も #表現型が多い
> BBS4 トップオッズ
> BBS3 はシャペロニンよりも重症度が低い
> BBS3 は BBSome よりも深刻ではありません

### 熟語・専門語

- **ESS**: 有効サンプルサイズ。自己相関を考慮した独立サンプル相当数。

### 要約

- BBS4 で最も #表現型が多い BBS4 トップオッズ BBS3 はシャペロニンよりも重症度が低い BBS3 は BBSome よりも深刻ではありません

## Chunk 0447

### English（抽出4行）

> cLOF mutations more severe
> Freq. type
> Conclusion
> Main

### 日本語訳（自動翻訳）

> cLOF変異はより重度である
> 周波数タイプ
> 結論
> メイン

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- cLOF変異はより重度である 周波数タイプ 結論 メイン

## Chunk 0448

### English（抽出4行）

> Secondary
> Problematic fits
> source
> source + cLOF

### 日本語訳（自動翻訳）

> 二次
> 問題のある適合
> ソース
> ソース + cLOF

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- 二次 問題のある適合 ソース ソース + cLOF

## Chunk 0449

### English（抽出4行）

> source + filtered cLOF
> source + gene corr.
> source + no corr.
> source + narrow

### 日本語訳（自動翻訳）

> ソース + フィルターされた cLOF
> ソース + 遺伝子の誤り。
> ソース+間違いなし。
> ソース + ナロー

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- ソース + フィルターされた cLOF ソース + 遺伝子の誤り。

## Chunk 0450

### English（抽出4行）

> source + wide
> source + cLOF + ethnic group
> source + cLOF + wide
> source + cLOF (by gene)

### 日本語訳（自動翻訳）

> ソース+ワイド
> ソース + cLOF + 民族グループ
> ソース + cLOF + ワイド
> ソース + cLOF (遺伝子による)

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- ソース+ワイド ソース + cLOF + 民族グループ ソース + cLOF + ワイド ソース + cLOF (遺伝子による)

## Chunk 0451

### English（抽出4行）

> source + family
> source + cLOF + family
> source + filtered sex
> source + filtered age

### 日本語訳（自動翻訳）

> ソース+家族
> ソース + cLOF + ファミリ
> ソース + フィルターされたセックス
> ソース + フィルターされた年齢

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- ソース+家族 ソース + cLOF + ファミリ ソース + フィルターされたセックス ソース + フィルターされた年齢

## Chunk 0452

### English（抽出4行）

> source + filtered cLOF + wide
> source + imputed sex
> source + imputed age
> source + imputed age + sex

### 日本語訳（自動翻訳）

> ソース + フィルターされた cLOF + ワイド
> ソース + 推定性別
> 情報源 + 推定年齢
> 情報源 + 推定年齢 + 性別

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- ソース + フィルターされた cLOF + ワイド ソース + 推定性別 情報源 + 推定年齢 情報源 + 推定年齢 + 性別

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
> 民族性

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- ソース + 非常に狭い なし 民族グループ 民族性

## Chunk 0454

### English（抽出4行）

> cLOF
> cLOF (by gene)
> ethnic group + cLOF
> ethnicity + cLOF

### 日本語訳（自動翻訳）

> cLOF
> cLOF (遺伝子による)
> 民族グループ + cLOF
> 民族性 + cLOF

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- cLOF cLOF (遺伝子による) 民族グループ + cLOF 民族性 + cLOF

## Chunk 0455

### English（抽出4行）

> ethnic group + cLOF (by gene)
> ethnicity + cLOF (by gene)
> family
> filtered age + sex

### 日本語訳（自動翻訳）

> 民族 + cLOF (遺伝子による)
> 民族性 + cLOF (遺伝子による)
> 家族
> フィルタリングされた年齢 + 性別

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- 民族 + cLOF (遺伝子による) 民族性 + cLOF (遺伝子による) 家族 フィルタリングされた年齢 + 性別

## Chunk 0456

### English（抽出4行）

> none + filtered cLOF
> cLOF + filtered age + sex
> cLOF (by gene) + filtered age + sex
> family + filtered age + sex + cLOF

### 日本語訳（自動翻訳）

> なし + フィルタリングされた cLOF
> cLOF + フィルターされた年齢 + 性別
> cLOF (遺伝子による) + フィルターされた年齢 + 性別
> 家族 + フィルターされた年齢 + 性別 + cLOF

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- なし + フィルタリングされた cLOF cLOF + フィルターされた年齢 + 性別 cLOF (遺伝子による) + フィルターされた年齢 + 性別 家族 + フィルターされた年齢 + 性別 + cLOF

## Chunk 0457

### English（抽出4行）

> imputed age + sex
> Model components/modifications besides gene
> 0.05
> 1e−4

### 日本語訳（自動翻訳）

> 推定年齢 + 性別
> 遺伝子以外のモデル構成要素・改変
> 0.05
> 1e−4

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- 推定年齢 + 性別 遺伝子以外のモデル構成要素・改変 0.05 1e−4

## Chunk 0458

### English（抽出4行）

> 1e−8
> p−value
> 0.01
> 0.10

### 日本語訳（自動翻訳）

> 1e−8
> p値
> 0.01
> 0.10

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- 1e−8 p値 0.01 0.10

## Chunk 0459

### English（抽出4行）

> 0.50
> 0.90
> 0.99
> Posterior prob.

### 日本語訳（自動翻訳）

> 0.50
> 0.90
> 0.99
> 事後確率

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- 0.50 0.90 0.99 事後確率

## Chunk 0460

### English（抽出4行）

> ND
> Figure 23: The results of a multiverse analysis from the supplementary material of Niederlová et al.
> (2019). The heat map shows statistical evaluation of selected conclusions about the relation between
> phenotypes (PD, CI, REN, HEART, LIV) and mutations in various genes of the BBSome (BBS01 -

### 日本語訳（自動翻訳）

> ND
> 図 23: Niederlová らの補足資料からの多元宇宙分析の結果。
> （2019年）。ヒート マップは、次の関係について選択された結論の統計的評価を示します。
> 表現型 (PD、CI、REN、HEART、LIV) および BBSome のさまざまな遺伝子の変異 (BBS01 -

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- ND 図 23: Niederlová らの補足資料からの多元宇宙分析の結果。

## Chunk 0461

### English（抽出4行）

> BBS8, cLOF - complete loss of function) using a set of Bayesian hierarchical logistic regression
> models and pairwise frequentist tests. Based on posterior predictive checks the Bayesian models
> were categorized as “Main” (passing all checks), “Secondary” (minor problems in some checks),
> and “Problematic ﬁts,” though we see that most conclusions hold across all possible models. The

### 日本語訳（自動翻訳）

> BBS8、cLOF - 完全な機能喪失）一連のベイジアン階層ロジスティック回帰を使用
> モデルとペアワイズ頻度主義検定。事後予測チェックに基づくベイジアン モデル
> 「メイン」（すべてのチェックに合格）、「セカンダリ」（一部のチェックに軽度の問題）、
> ただし、ほとんどの結論はすべての可能なモデルに当てはまります。の

### 熟語・専門語

- **posterior predictive**: 事後予測。推定後のモデルが観測データの特徴を再現できるかを見る診断。
- **ESS**: 有効サンプルサイズ。自己相関を考慮した独立サンプル相当数。

### 要約

- BBS8、cLOF - 完全な機能喪失）一連のベイジアン階層ロジスティック回帰を使用 モデルとペアワイズ頻度主義検定。

## Chunk 0462

### English（抽出4行）

> models diﬀer in both predictors that are included and priors (default/wide/narrow/very narrow).
> (Steegen et al., 2016, Dragicevic et al., 2019, Kale, Kay, and Hullman, 2019). Using multiverse
> analysis can also relieve some of the eﬀort in validating models and priors: if the conclusions do
> not change it is less important to decide which model is “best.” Figure 23 shows an example of

### 日本語訳（自動翻訳）

> モデルは、含まれる予測変数と事前予測変数 (デフォルト/広い/狭い/非常に狭い) の両方で異なります。
> (Steegen et al.、2016、Dragicevic et al.、2019、Kale、Kay、および Hullman、2019)。マルチバースの使用
> 分析は、モデルと事前分布を検証する際の労力の一部を軽減することもできます。
> 変更しないと、どのモデルが「最適」であるかを決定する重要性が低くなります。図 23 に例を示します。

### 熟語・専門語

- **ESS**: 有効サンプルサイズ。自己相関を考慮した独立サンプル相当数。

### 要約

- モデルは、含まれる予測変数と事前予測変数 (デフォルト/広い/狭い/非常に狭い) の両方で異なります。

## Chunk 0463

### English（抽出4行）

> a possible output. Other analytical choices (data preprocessing, response distribution, metric to
> evaluate, and so forth) can also be subject to multiverse analysis.
> 8.2.
> Cross validation and model averaging

### 日本語訳（自動翻訳）

> 可能な出力。その他の分析上の選択肢 (データの前処理、応答分布、測定基準)
> 評価など) も多元分析の対象にすることができます。
> 8.2.
> 相互検証とモデルの平均化

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

> 相互検証を使用して、同じデータに適合するモデルを比較できます (Vehtari et al.、2017)。いつ
> 比較に無視できない不確実性がある場合、モデル比較を実行します (Sivula et
> al., 2020)、最良の相互検証結果を持つ単一のモデルを単純に選択すべきではありません。
> これにより、相互検証プロセスからの不確実性がすべて破棄されるためです。

### 熟語・専門語

- **model comparison**: モデル比較。LOO-CVなどで複数モデルの予測性能や弱点を比較すること。
- **cross validation**: 交差検証。汎化性能を推定するためにデータを分割/近似除外する評価法。
- **ESS**: 有効サンプルサイズ。自己相関を考慮した独立サンプル相当数。
- **uncertainty**: 不確実性。観測・パラメータ・モデル構造・意思決定に残る曖昧さ。
- **validation**: 検証。モデルが目的・データ・外部知識に照らして妥当かを確認すること。

### 要約

- 相互検証を使用して、同じデータに適合するモデルを比較できます (Vehtari et al.、2017)。

## Chunk 0465

### English（抽出4行）

> Instead, we can
> maintain this information and use stacking to combine inferences using a weighting that is set up to
> minimize cross validation error (Yao et al., 2018b). We think that stacking makes more sense than
> traditional Bayesian model averaging, as the latter can depend strongly on aspects of the model

### 日本語訳（自動翻訳）

> 代わりに、次のことができます。
> この情報を維持し、スタッキングを使用して、設定された重み付けを使用して推論を結合します。
> 相互検証エラーを最小限に抑えます (Yao et al., 2018b)。私たちは、積み重ねることがより意味があると考えています。
> 従来のベイジアン モデルの平均化。後者はモデルの側面に強く依存する可能性があるため

### 熟語・専門語

- **cross validation**: 交差検証。汎化性能を推定するためにデータを分割/近似除外する評価法。
- **validation**: 検証。モデルが目的・データ・外部知識に照らして妥当かを確認すること。

### 要約

- 代わりに、次のことができます。

## Chunk 0466

### English（抽出4行）

> that have minimal eﬀect on predictions. For example, for a model that is well informed by the data
> and whose parameters are on unit scale, changing the prior on parameters from normal(0, 10) to
> normal(0, 100) will divide the marginal likelihood by roughly 10k (for a model with k parameters)
> while keeping all predictions essentially the same. In addition, stacking takes into account the

### 日本語訳（自動翻訳）

> 予測への影響は最小限です。たとえば、データから十分な情報を得たモデルの場合、
> パラメータは単位スケール上にあり、以前のパラメータを Normal(0, 10) から
> Normal(0, 100) は、周辺尤度をおよそ 10k で除算します (k パラメーターを持つモデルの場合)。
> すべての予測を本質的に同じに保ちながら。さらに、スタッキングでは、

### 熟語・専門語

- **likelihood**: 尤度。パラメータが与えられたときデータがどれだけ起こりやすいか。
- **ESS**: 有効サンプルサイズ。自己相関を考慮した独立サンプル相当数。
- **prediction**: 予測。未知/将来/除外データに対する分布や点推定。

### 要約

- 予測への影響は最小限です。

## Chunk 0467

### English（抽出4行）

> joint predictions and works well when there are a large number of similar but weak models in the
> candidate model list.
> In concept, stacking can sometimes be viewed as pointwise model selection.
> When there

### 日本語訳（自動翻訳）

> 共同予測を実行し、類似しているが弱いモデルが多数存在する場合にうまく機能します。
> 候補機種リスト。
> 概念上、スタッキングは点ごとのモデル選択とみなされる場合があります。
> そこにいるとき

### 熟語・専門語

- **prediction**: 予測。未知/将来/除外データに対する分布や点推定。

### 要約

- 共同予測を実行し、類似しているが弱いモデルが多数存在する場合にうまく機能します。

## Chunk 0468

### English（抽出4行）

> are two models and the ﬁrst model outperforms the second model 20% of the time, the stacking
> weights will be close to (0.2, 0.8). In light of this, stacking ﬁlls a gap between independent-error
> oriented machine learning validation and the grouped structure of modern big data. Model stacking
> is therefore also an indicator of heterogeneity of model ﬁtting, and this suggests we can further

### 日本語訳（自動翻訳）

> 2 つのモデルがあり、最初のモデルが 20% の確率で 2 番目のモデルよりも優れています。
> 重みは (0.2, 0.8) に近くなります。これを考慮すると、スタッキングは独立エラー間のギャップを埋めます。
> 機械学習指向の検証と最新のビッグデータのグループ化された構造。モデルのスタッキング
> したがって、これはモデルのフィッティングの不均一性の指標でもあり、これは、さらに次のことができることを示唆しています。

### 熟語・専門語

- **validation**: 検証。モデルが目的・データ・外部知識に照らして妥当かを確認すること。

### 要約

- 2 つのモデルがあり、最初のモデルが 20% の確率で 2 番目のモデルよりも優れています。

## Chunk 0469

### English（抽出4行）

> improve the aggregated model with a hierarchical model, so that the stacking is a step toward model
> improvement rather than an end to itself. In the extreme, model averaging can also be done so that
> diﬀerent models can apply to diﬀerent data points (Kamary et al., 2019, Pirš and Štrumbelj, 2019).
> In Bayesian workﬂow, we will ﬁt many models that we will not be interested in including in

### 日本語訳（自動翻訳）

> 階層モデルを使用して集約モデルを改善し、スタッキングがモデルへのステップとなるようにする
> それ自体が目的ではなく、改善すること。極端な場合、モデルの平均化を行うこともできます。
> 異なるモデルは異なるデータポイントに適用できます (Kamary et al., 2019、Pirš and Štrumbelj, 2019)。
> ベイジアン ワークフローでは、興味のない多くのモデルを適合させます。

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- 階層モデルを使用して集約モデルを改善し、スタッキングがモデルへのステップとなるようにする それ自体が目的ではなく、改善すること。

## Chunk 0470

### English（抽出4行）

> any average; such “scaﬀolds” include models that are deliberately overly simple (included just for
> comparison to the models of interest) and models constructed for purely experimental purposes,
> as well as models that have major ﬂaws or even coding errors. But even after these mistakes
> or deliberate oversimpliﬁcations have been removed, there might be several models over which

### 日本語訳（自動翻訳）

> 任意の平均。このような「足場」には、意図的に過度に単純になったモデルが含まれます（目的のためにのみ含まれています）。
> 対象のモデルとの比較）および純粋に実験目的で構築されたモデル、
> 重大な欠陥やコーディングエラーのあるモデルも同様です。しかし、これらの間違いの後でも
> または意図的な過度の単純化が削除されている場合、いくつかのモデルが存在する可能性があります。

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- 任意の平均。

## Chunk 0471

### English（抽出4行）

> to average when making predictions. In our own applied work we have not generally had many
> occasions to perform this sort of model averaging, as we prefer continuous model expansion,
> but there will be settings where users will reasonably want to make predictions averaging over
> competing Bayesian models, as in Montgomery and Nyhan (2010).

### 日本語訳（自動翻訳）

> 予測を行うときに平均化します。私たち自身の応用研究では、一般的にはそれほど多くはありません
> 継続的なモデル拡張を好むため、この種のモデルの平均化を実行する機会はありません。
> ただし、ユーザーが平均して予測を行うことを合理的に希望する設定も存在します。
> Montgomery and Nyhan (2010) のように、競合するベイジアン モデル。

### 熟語・専門語

- **prediction**: 予測。未知/将来/除外データに対する分布や点推定。

### 要約

- 予測を行うときに平均化します。

## Chunk 0472

### English（抽出4行）

> 8.3.
> Comparing a large number of models
> There are many problems, for example in linear regression with several potentially relevant predic-
> tors, where many candidate models are available, all of which can be described as special cases of a

### 日本語訳（自動翻訳）

> 8.3.
> 多数のモデルを比較する
> たとえば、関連する可能性のあるいくつかの予測を使用した線形回帰では、多くの問題があります。
> 多くの候補モデルが利用可能であり、それらはすべて、あるモデルの特殊なケースとして説明できます。

### 熟語・専門語

- **ESS**: 有効サンプルサイズ。自己相関を考慮した独立サンプル相当数。

### 要約

- 8.3. 多数のモデルを比較する たとえば、関連する可能性のあるいくつかの予測を使用した線形回帰では、多くの問題があります。

## Chunk 0473

### English（抽出4行）

> single expanded model. If the number of candidate models is large, we are often interested in ﬁnd-
> ing a comparably smaller model that has the same predictive performance as our expanded model.
> This leads to the problem of predictor (variable) selection. If we have many models making similar
> predictions, selecting one of these models based on minimizing cross validation error would lead

### 日本語訳（自動翻訳）

> 単一の拡張モデル。候補モデルの数が多い場合、多くの場合、
> 拡張モデルと同じ予測パフォーマンスを持つ比較的小さなモデルを作成します。
> これは、予測子 (変数) の選択の問題につながります。似たようなモデルをたくさん作っている場合
> 予測では、相互検証エラーの最小化に基づいてこれらのモデルの 1 つを選択すると、

### 熟語・専門語

- **cross validation**: 交差検証。汎化性能を推定するためにデータを分割/近似除外する評価法。
- **validation**: 検証。モデルが目的・データ・外部知識に照らして妥当かを確認すること。
- **prediction**: 予測。未知/将来/除外データに対する分布や点推定。

### 要約

- 単一の拡張モデル。

## Chunk 0474

### English（抽出4行）

> to overﬁtting and suboptimal model choices (Piironen and Vehtari, 2017). In contrast, projection
> predictive variable selection has been shown to be stable and reliable in ﬁnding smaller models
> with good predictive performance (Piironen and Vehtari, 2017, Piironen et al., 2020, Pavone et
> al., 2020). While searching through a big model space is usually associated with the danger of

### 日本語訳（自動翻訳）

> 過剰適合や次善のモデル選択に影響を及ぼします (Piironen と Vehtari、2017)。対照的に、投影
> 予測変数の選択は、より小さなモデルを見つける際に安定していて信頼できることが示されています。
> 優れた予測性能を備えています (Piironen and Vehtari、2017、Piironen et al.、2020、Pavone et
> al.、2020）。大きなモデル空間を探索する場合、通常、次のような危険が伴います。

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- 過剰適合や次善のモデル選択に影響を及ぼします (Piironen と Vehtari、2017)。

## Chunk 0475

### English（抽出4行）

> overﬁtting, the projection predictive approach avoids it by examining only the projected submodels
> based on the expanded model’s predictions and not ﬁtting each model independently to the data.
> In addition to variable selection, projection predictive model selection can be used for structure
> selection in generalized additive multilevel models (Catalina et al., 2020) and for creating simpler

### 日本語訳（自動翻訳）

> 過剰適合が発生した場合、投影予測アプローチでは、投影されたサブモデルのみを検査することでこれを回避します。
> 拡張モデルの予測に基づいており、各モデルをデータに個別に適合させるわけではありません。
> 変数選択に加えて、射影予測モデル選択を構造に使用できます。
> 一般化された加法マルチレベル モデル (Catalina et al., 2020) での選択と、より単純なモデルの作成用

### 熟語・専門語

- **prediction**: 予測。未知/将来/除外データに対する分布や点推定。

### 要約

- 過剰適合が発生した場合、投影予測アプローチでは、投影されたサブモデルのみを検査することでこれを回避します。

## Chunk 0476

### English（抽出4行）

> explanations for complex nonparametric models (Afrabandpey et al., 2020).
> 9.
> Modeling as software development
> Developing a statistical model in a probabilistic programming language means writing code and is

### 日本語訳（自動翻訳）

> 複雑なノンパラメトリック モデルの説明 (Afrabandpey et al., 2020)。
> 9.
> ソフトウェア開発としてのモデリング
> 確率的プログラミング言語で統計モデルを開発するということは、コードを書くことを意味し、

### 熟語・専門語

- **probabilistic programming**: 確率的プログラミング。Stanなどで確率モデルをコードとして記述し推論する方法。

### 要約

- 複雑なノンパラメトリック モデルの説明 (Afrabandpey et al., 2020)。

## Chunk 0477

### English（抽出4行）

> thus a form of software development, with several stages: writing and debugging the model itself;
> the preprocessing necessary to get the data into suitable form to be modeled; and the later steps of
> understanding, communicating, and using the resulting inferences. Developing software is hard.
> So many things can go wrong because there are so many moving parts that need to be carefully

### 日本語訳（自動翻訳）

> したがって、ソフトウェア開発の一形式であり、モデル自体の作成とデバッグといういくつかの段階があります。
> データをモデル化するのに適した形式にするために必要な前処理。そしてその後のステップ
> 結果として得られる推論を理解し、伝達し、使用すること。ソフトウェアの開発は大変です。
> 注意が必要な可動部分が非常に多いため、多くのことがうまくいかない可能性があります

### 熟語・専門語

- **ESS**: 有効サンプルサイズ。自己相関を考慮した独立サンプル相当数。

### 要約

- したがって、ソフトウェア開発の一形式であり、モデル自体の作成とデバッグといういくつかの段階があります。

## Chunk 0478

### English（抽出4行）

> synchronized.
> Software development practices are designed to mitigate the problems caused by the inherent
> complexity of writing computer programs. Unfortunately, many methodologies veer oﬀinto dogma,
> bean counting, or both. A couple references we can recommend that provide solid, practical advice

### 日本語訳（自動翻訳）

> 同期されました。
> ソフトウェア開発の実践は、固有の要因によって引き起こされる問題を軽減するように設計されています。
> コンピュータープログラムを書くことの複雑さ。残念なことに、多くの方法論は定説から外れています。
> 豆の数え方、またはその両方。確実で実践的なアドバイスを提供する、おすすめの参考文献をいくつか紹介します。

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- 同期されました。

## Chunk 0479

### English（抽出4行）

> for developers are Hunt and Thomas (1999) and McConnell (2004).
> 9.1.
> Version control smooths collaborations with others and with your past self
> Version control software, such as Git, should be should be the ﬁrst piece of infrastructure put in

### 日本語訳（自動翻訳）

> 開発者としては、Hunt と Thomas (1999) および McConnell (2004) が挙げられます。
> 9.1.
> バージョン管理により、他の人や過去の自分とのコラボレーションがスムーズになります
> Git などのバージョン管理ソフトウェアは、インフラストラクチャの最初の部分として配置する必要があります。

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- 開発者としては、Hunt と Thomas (1999) および McConnell (2004) が挙げられます。

## Chunk 0480

### English（抽出4行）

> place for a project. It may seem like a big investment to learn version control, but it’s well worth it
> to be able to type a single command to revert to a previously working version or to get the diﬀerence
> between the current version and an old version. It’s even better when you need to share work with
> others, even on a paper—work can be done independently and then automatically merged. While

### 日本語訳（自動翻訳）

> プロジェクトの場所。バージョン管理を学ぶのは多額の投資のように思えるかもしれませんが、それだけの価値は十分にあります
> 単一のコマンドを入力して、以前に動作していたバージョンに戻すか、差分を取得できるようにする
> 現在のバージョンと古いバージョンの間。仕事を共有する必要がある場合はさらに便利です
> 他の作業は紙の上であっても、個別に作業を行ってから自動的に結合できます。その間

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

> バージョン管理は、1 つのモデルの小さな変更を追跡します。明らかに異なるモデルを維持するのに役立ちます。
> モデルを異なるファイルに保存して、モデルを簡単に比較できるようにします。バージョン管理も維持に役立ちます
> 反復モデル構築での発見と決定に関するメモ。これにより、モデルの透明性が向上します。
> プロセス。

### 熟語・専門語

- **ESS**: 有効サンプルサイズ。自己相関を考慮した独立サンプル相当数。
- **model building**: モデル構築。仮定・データ構造・prior・likelihoodを組み合わせる工程。
- **decision**: 意思決定。予測分布を損失・効用・行動選択へ接続する工程。

### 要約

- バージョン管理は、1 つのモデルの小さな変更を追跡します。

## Chunk 0482

### English（抽出4行）

> Version control is not just for code. It is also for reports, graphs, and data. Version control is a
> critical part of ensuring that all of these components are synchronized and, more importantly, that
> it is possible to rewind the project to a previous state. Version control is particularly useful for its
> ability to package up and label “release candidate” versions of models and data that correspond to

### 日本語訳（自動翻訳）

> バージョン管理はコードだけのものではありません。レポート、グラフ、データにも使用できます。バージョン管理というのは、
> これは、これらすべてのコンポーネントが同期されていることを確認する上で重要な部分であり、さらに重要なことは、
> プロジェクトを前の状態に巻き戻すことができます。バージョン管理は特に便利です。
> に対応するモデルとデータの「リリース候補」バージョンをパッケージ化し、ラベルを付ける機能

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- バージョン管理はコードだけのものではありません。

## Chunk 0483

### English（抽出4行）

> milestone reports and publications and to store them in the same directory without resorting to the
> dreaded _final_final_161020.pdf-style naming conventions.
> When working on models that are used to guide policy decision making, a public version control
> repository increases transparency about what model, data, inference parameters, and scripts were

### 日本語訳（自動翻訳）

> マイルストーン レポートと出版物を保存し、それらを同じディレクトリに保存します。
> 恐ろしい _final_final_161020.pdf スタイルの命名規則。
> ポリシーの意思決定をガイドするために使用されるモデルに取り組む場合、公開バージョン管理
> リポジトリにより、どのようなモデル、データ、推論パラメータ、スクリプトが含まれていたかについての透明性が向上します。

### 熟語・専門語

- **decision**: 意思決定。予測分布を損失・効用・行動選択へ接続する工程。

### 要約

- マイルストーン レポートと出版物を保存し、それらを同じディレクトリに保存します。

## Chunk 0484

### English（抽出4行）

> used for speciﬁc reports. An excellent example of this is the Imperial College repository for models
> and scripts to estimate deaths and cases for COVID-19 (Flaxman et al., 2020).
> 9.2.
> Testing as you go

### 日本語訳（自動翻訳）

> 特定のレポートに使用されます。この優れた例は、モデルのインペリアル カレッジ リポジトリです。
> 新型コロナウイルス感染症（COVID-19）の死亡者数と感染者数を推定するためのスクリプト（Flaxman et al.、2020）。
> 9.2.
> 進行中のテスト

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- 特定のレポートに使用されます。

## Chunk 0485

### English（抽出4行）

> Software design ideally proceeds top down from the goals of the end user back to the technical
> machinery required to implement it. For a Bayesian statistical model, top-down design involves at
> least the data input format, the probabilistic model for the data, and the prior, but may also involve
> simulators and model testing like simulation-based calibration or posterior predictive checks.

### 日本語訳（自動翻訳）

> ソフトウェア設計は、理想的にはエンドユーザーの目標から技術的な目標に至るトップダウンで進められます。
> それを実現するために必要な機械。ベイズ統計モデルの場合、トップダウン設計には以下が含まれます。
> 少なくともデータ入力形式、データの確率モデル、および事前の情報が含まれますが、その他の情報も含まれる場合があります。
> シミュレータと、シミュレーションベースのキャリブレーションや事後予測チェックなどのモデルテスト。

### 熟語・専門語

- **posterior predictive**: 事後予測。推定後のモデルが観測データの特徴を再現できるかを見る診断。
- **simulation-based calibration**: SBC。シミュレーション真値と事後rankを比べ、実装・推論の校正を検査する方法。

### 要約

- ソフトウェア設計は、理想的にはエンドユーザーの目標から技術的な目標に至るトップダウンで進められます。

## Chunk 0486

### English（抽出4行）

> Software development ideally works bottom up from well-tested foundational functions to larger
> functional modules. That way, development proceeds through a series of well-tested steps, at each
> stage building only on tested pieces. The advantage to working this way as opposed to building a
> large program and then debugging it is the same as for incremental model development—it’s easier

### 日本語訳（自動翻訳）

> ソフトウェア開発は、十分にテストされた基本機能からより大きな機能に至るまでボトムアップで作業するのが理想的です。
> 機能モジュール。このようにして、開発は十分にテストされた一連のステップをそれぞれのステップで進めていきます。
> テストされたピースのみでステージを構築します。を構築するのとは対照的に、この方法で作業する利点は、
> 大規模なプログラムをデバッグする場合は、インクリメンタル モデル開発の場合と同じであり、より簡単です。

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- ソフトウェア開発は、十分にテストされた基本機能からより大きな機能に至るまでボトムアップで作業するのが理想的です。

## Chunk 0487

### English（抽出4行）

> to track where the development went wrong and you have more conﬁdence at each step working
> with well-tested foundations.
> The key to computational development, either in initial development or modifying code, is
> modularity. Big tangled functions are hard to document, harder to read, extraordinarily diﬃcult

### 日本語訳（自動翻訳）

> 開発のどこが間違っていたのかを追跡し、各ステップでより自信を持って作業できるようになります。
> 十分にテストされた基礎を備えています。
> 初期開発またはコード変更のいずれにおいても、計算開発の鍵は次のとおりです。
> モジュール性。大きく複雑に絡み合った関数は文書化するのが難しく、読みにくく、非常に困難です

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- 開発のどこが間違っていたのかを追跡し、各ステップでより自信を持って作業できるようになります。

## Chunk 0488

### English（抽出4行）

> to debug, and nearly impossible to maintain or modify. Modularity means building larger pieces
> out of smaller trusted pieces, such as low-level functions. Whenever code fragments are repeated,
> they should be encapsulated as functions. This results in code that is easier to read and easier to
> maintain.

### 日本語訳（自動翻訳）

> デバッグが困難であり、保守や変更はほぼ不可能です。モジュール性とは、より大きな部分を構築することを意味します
> 低レベルの関数など、より小さな信頼できる部分から構成されます。コードの断片が繰り返されるたびに、
> これらは関数としてカプセル化する必要があります。これにより、コードが読みやすくなり、理解しやすくなります。
> 維持する。

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- デバッグが困難であり、保守や変更はほぼ不可能です。

## Chunk 0489

### English（抽出4行）

> As an example of a low-level function, predictors might be rescaled for a generalized linear
> model by implementing the standardization, z(v) = (v −mean(v))/sd(v). Although this function
> seems simple, subtleties arise, starting with the sd function, which is sometimes deﬁned as sd(v) =
> pPn

### 日本語訳（自動翻訳）

> 低レベル関数の例として、予測子は一般化された線形関数用に再スケーリングされる可能性があります。
> 標準化 z(v) = (v −mean(v))/sd(v) を実装することによりモデル化します。この機能ですが、
> 単純そうに見えますが、sd 関数から始まる微妙な点が生じます。これは sd(v) = として定義されることもあります。
> ｐＰｎ

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- 低レベル関数の例として、予測子は一般化された線形関数用に再スケーリングされる可能性があります。

## Chunk 0490

### English（抽出4行）

> i=1(vi −mean(v))2/n and sometimes as sd(v) =
> pPn
> i=1(vi −mean(v))2/(n −1). If this
> isn’t sorted out at the level of the standardization function, it can produce mysterious biases during

### 日本語訳（自動翻訳）

> i=1(vi −mean(v))2/n、場合によっては sd(v) = となります。
> ｐＰｎ
> i=1(vi −平均(v))2/(n −1)。これなら
> 標準化機能のレベルで整理されていないため、作業中に謎のバイアスが生じる可能性があります。

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- i=1(vi −mean(v))2/n、場合によっては sd(v) = となります。

## Chunk 0491

### English（抽出4行）

> inference.
> Simple tests that don’t rely on the sd() function will sort this out during function
> development. If the choice is the estimate that divides by n −1, there needs to be decision of what
> to do when v is a vector of length 1. In cases where there are illegal inputs, it helps to put checks in

### 日本語訳（自動翻訳）

> 推論。
> sd() 関数に依存しない単純なテストは、関数の実行中にこれを解決します。
> 開発。 n −1 で割る推定値を選択する場合、何を選択するかを決定する必要があります。
> v が長さ 1 のベクトルの場合に実行します。不正な入力がある場合、チェックを入れると役立ちます。

### 熟語・専門語

- **decision**: 意思決定。予測分布を損失・効用・行動選択へ接続する工程。

### 要約

- 推論。

## Chunk 0492

### English（抽出4行）

> the input-output routines that let users know when the problem arises rather than allowing errors
> to percolate through to mysterious divide-by-zero errors later.
> An implementation of cubic splines or an Euler solver for a diﬀerential equation is an example
> of a higher-level function that should be tested before it is used. As functions get more complicated,

### 日本語訳（自動翻訳）

> エラーを許容するのではなく、問題が発生したときにユーザーに知らせる入出力ルーチン
> 後で謎のゼロ除算エラーに浸透します。
> 3 次スプラインの実装や微分方程式のオイラー ソルバーは一例です。
> 使用前にテストする必要がある高レベルの関数。機能が複雑になると、

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- エラーを許容するのではなく、問題が発生したときにユーザーに知らせる入出力ルーチン 後で謎のゼロ除算エラーに浸透します。

## Chunk 0493

### English（抽出4行）

> they become harder to test because of issues with boundary-condition combinatorics, more general
> inputs such as functions to integrate, numerical instability or imprecision over regions of their
> domain which may or may not be acceptable depending on the application, the need for stable
> derivatives, etc.

### 日本語訳（自動翻訳）

> より一般的な境界条件の組み合わせの問題により、テストが難しくなります。
> 積分する関数、数値の不安定性、領域全体にわたる不正確さなどの入力
> アプリケーションに応じて受け入れられる場合と受け入れられない場合があるドメイン、安定したドメインの必要性
> デリバティブなど

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- より一般的な境界条件の組み合わせの問題により、テストが難しくなります。

## Chunk 0494

### English（抽出4行）

> 9.3.
> Making it essentially reproducible
> A lofty goal for any project is to make it fully reproducible in the sense that another person on
> another machine could recreate the ﬁnal report. This is not the type of reproducibility that is

### 日本語訳（自動翻訳）

> 9.3.
> 本質的に再現可能にする
> あらゆるプロジェクトの高い目標は、別の人が参加するという意味で完全に再現可能にすることです。
> 別のマシンで最終レポートを再作成できます。これはそういう再現性ではありません

### 熟語・専門語

- **ESS**: 有効サンプルサイズ。自己相関を考慮した独立サンプル相当数。

### 要約

- 9.3. 本質的に再現可能にする あらゆるプロジェクトの高い目標は、別の人が参加するという意味で完全に再現可能にすることです。

## Chunk 0495

### English（抽出4行）

> considered in scientiﬁc ﬁelds, where the desire is to ensure that an eﬀect is conﬁrmed by new future
> data (nowadays often called “replicability” for a better distinction between the diﬀerent notions).
> Instead this is the more limited (but still vital) goal of ensuring that one particular analysis is
> consistently done. In particular, we would want to be able to produce analyses and ﬁgures that

### 日本語訳（自動翻訳）

> 科学分野で検討されており、その効果が新しい未来によって確実に確認されることが望まれます。
> データ (現在では、さまざまな概念をより明確に区別するために「複製可能性」と呼ばれることがよくあります)。
> 代わりに、これは、特定の分析を確実に行うという、より限定的な (それでも重要な) 目標です。
> 一貫して行われています。特に、次のような分析と数値を生成できるようにしたいと考えています。

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- 科学分野で検討されており、その効果が新しい未来によって確実に確認されることが望まれます。

## Chunk 0496

### English（抽出4行）

> are essentially equivalent to the original document. Bit-level reproducibility may not be possible,
> but we would still liken equivalence at a practical level. In the event that this type of reproduction
> changes the outcome of a paper, we would argue that the original results were not particularly
> robust.

### 日本語訳（自動翻訳）

> 基本的に元の文書と同等です。ビットレベルの再現は不可能かもしれませんが、
> しかし、私たちは依然として実用レベルでの等価性を比較します。このような複製が行われた場合には、
> 論文の結果が変わるとしても、元の結果は特別なものではなかったと主張するでしょう。
> 頑丈。

### 熟語・専門語

- **ESS**: 有効サンプルサイズ。自己相関を考慮した独立サンプル相当数。

### 要約

- 基本的に元の文書と同等です。

## Chunk 0497

### English（抽出4行）

> Rather than entering commands on the command line when running models (or entering
> commands directly into an interactive programming language like R or Python), write scripts to
> run the data through the models and produce whatever posterior analysis you need. Scripts can
> be written for the shell, R, Python, or any other programming language. The script should be

### 日本語訳（自動翻訳）

> モデルを実行するときにコマンドラインにコマンドを入力するのではなく（または次のように入力します）
> コマンドを R や Python などの対話型プログラミング言語に直接書き込む)、スクリプトを記述します。
> モデルを通してデータを実行し、必要な事後分析を生成します。スクリプトでできること
> シェル、R、Python、またはその他のプログラミング言語用に作成する必要があります。スクリプトは次のようにする必要があります

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- モデルを実行するときにコマンドラインにコマンドを入力するのではなく（または次のように入力します） コマンドを R や Python などの対話型プログラミング言語に直接書き込む)、スクリプトを記述します。

## Chunk 0498

### English（抽出4行）

> self-contained in the sense that it should run in a completely clean environment or, ideally, on a
> diﬀerent computer. This means that the script(s) must not depend on global variables having been
> set, other data being read in, or anything else that is not in the script.
> Scripts are good documentation. It may seem like overkill if running the project is only a single

### 日本語訳（自動翻訳）

> 完全にクリーンな環境、または理想的には、
> 別のコンピューター。これは、スクリプトがグローバル変数に依存してはいけないことを意味します。
> セット、読み込まれている他のデータ、またはスクリプトに含まれていないその他のデータ。
> スクリプトは優れたドキュメントです。プロジェクトの実行が 1 つだけである場合、それはやりすぎのように思えるかもしれません。

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- 完全にクリーンな環境、または理想的には、 別のコンピューター。

## Chunk 0499

### English（抽出4行）

> line of code, but the script provides not only a way to run the code, but also a form of concrete
> documentation for what is being run. For complex projects, we often ﬁnd that a well-constructed
> series of scripts can be more practical than one large R Markdown document or Jupyter notebook.
> Depending on long-term reproducibility needs, it’s important to choose the right tooling for the

### 日本語訳（自動翻訳）

> コード行ですが、スクリプトはコードを実行する方法だけでなく、具体的な形式も提供します。
> 何が実行されているかに関するドキュメント。複雑なプロジェクトの場合、よく構築されたものであることがよくあります。
> 一連のスクリプトは、1 つの大きな R Markdown ドキュメントや Jupyter ノートブックよりも実用的です。
> 長期的な再現性のニーズに応じて、適切なツールを選択することが重要です。

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- コード行ですが、スクリプトはコードを実行する方法だけでなく、具体的な形式も提供します。

## Chunk 0500

### English（抽出4行）

> job at hand. To guarantee bit-level reproducibility, and sometimes even just to get a program to
> run, everything from hardware, to the operating system, to every piece of software and setting must
> be speciﬁed with their version number. As time passes between the initial writing of the script and
> the attempt of reproduction, bit-level reproducibility can be almost impossible to achieve even if

### 日本語訳（自動翻訳）

> 目の前の仕事。ビットレベルの再現性を保証するため、場合によってはプログラムを
> 実行するには、ハードウェアからオペレーティング システム、あらゆるソフトウェアや設定に至るまで、すべてを実行する必要があります。
> バージョン番号を使用して指定します。最初に脚本を書いてから時間が経つにつれて、
> 再現を試みる場合、ビットレベルの再現性を達成することはほとんど不可能です。

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- 目の前の仕事。

## Chunk 0501

### English（抽出4行）

> the environment is shipped with the script, as in a Docker container.
> 9.4.
> Making it readable and maintainable
> Treating programs and scripts like other forms of writing for an audience provides an important

### 日本語訳（自動翻訳）

> 環境は、Docker コンテナーと同様に、スクリプトとともに出荷されます。
> 9.4.
> 読みやすく保守しやすいものにする
> プログラムやスクリプトを視聴者向けの他の形式の文章と同様に扱うことで、重要な効果が得られます。

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- 環境は、Docker コンテナーと同様に、スクリプトとともに出荷されます。

## Chunk 0502

### English（抽出4行）

> perspective on how the code will be used. Not only might others want to read and understand a
> program or model, the developers themselves will want to read and understand it later. One of the
> motivations of Stan’s design was to make models self-documenting in terms of variable usage (e.g.,
> data or parameters), types (e.g., covariance matrix or unconstrained matrix) and sizes. This allows

### 日本語訳（自動翻訳）

> コードがどのように使用されるかについての視点。他の人が読んで理解したいと思うだけでなく、
> プログラムやモデルについては、開発者自身が後で読んで理解したいと思うでしょう。の 1 つ
> Stan の設計の動機は、変数の使用に関してモデルを自己文書化することでした (例:
> データまたはパラメータ）、タイプ（共分散行列または制約なし行列など）、およびサイズ。これにより、

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- コードがどのように使用されるかについての視点。

## Chunk 0503

### English（抽出4行）

> us to understand Stan code (or code of other statically typed probabilistic programming languages)
> to be understandable without the context of the data it is applied on.
> A large part of readability is consistency, particularly in naming and layout, and not only of
> programs themselves, but the directories and ﬁles in which they are stored. Another key principle

### 日本語訳（自動翻訳）

> Stan コード (または他の静的に型付けされた確率的プログラミング言語のコード) を理解できるようになります。
> 適用されるデータのコンテキストなしで理解できること。
> 読みやすさの大部分は一貫性であり、特に名前とレイアウトにおける一貫性が重要です。
> プログラム自体だけでなく、プログラムが保存されているディレクトリやファイルも含まれます。もう一つの重要な原則

### 熟語・専門語

- **probabilistic programming**: 確率的プログラミング。Stanなどで確率モデルをコードとして記述し推論する方法。

### 要約

- Stan コード (または他の静的に型付けされた確率的プログラミング言語のコード) を理解できるようになります。

## Chunk 0504

### English（抽出4行）

> in coding is to avoid repetition, instead pulling shared code out into functions that can be reused.
> Readability of code is not just about comments—it is also about naming and organization for
> readability. Indeed, comments can made code less readable. The best approach is to write readable
> code, not opaque code with comments. For example, we don’t want to write this:

### 日本語訳（自動翻訳）

> コーディングでは、繰り返しを避け、代わりに共有コードを再利用可能な関数に抽出します。
> コードの読みやすさはコメントだけではなく、コードの名前付けと構成も重要です。
> 読みやすさ。実際、コメントによってコードが読みにくくなる可能性があります。最善のアプローチは読みやすいものを書くことです
> コメントを含む不透明なコードではありません。たとえば、次のようには書きたくありません。

### 熟語・専門語

- **ESS**: 有効サンプルサイズ。自己相関を考慮した独立サンプル相当数。

### 要約

- コーディングでは、繰り返しを避け、代わりに共有コードを再利用可能な関数に抽出します。

## Chunk 0505

### English（抽出4行）

> real x17;
> // oxygen level, should be positive
> when we can write this:
> real<lower = 0> oxygen_level;

### 日本語訳（自動翻訳）

> 実数 x17;
> // 酸素レベルは正である必要があります
> これを書けるようになったら:
> 実数<下位 = 0> 酸素レベル;

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- 実数 x17; // 酸素レベルは正である必要があります これを書けるようになったら: 実数<下位 = 0> 酸素レベル;

## Chunk 0506

### English（抽出4行）

> Similarly, we don’t want to do this:
> target += -0.5 * (y - mu)^2 / sigma^2;
> // y distributed normal(mu, sigma)
> when we can write,

### 日本語訳（自動翻訳）

> 同様に、次のようなことはしたくありません。
> ターゲット += -0.5 * (y - mu)^2 / sigma^2;
> // y 分布正規分布(mu, sigma)
> 書けるようになったら、

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- 同様に、次のようなことはしたくありません。

## Chunk 0507

### English（抽出4行）

> target += normal_lpdf(y | mu, sigma);
> Good practice is to minimize inline code comments and instead write readable code. As the above
> examples illustrate, clean code is facilitated by programming languages that gives users the tools
> they need to use.

### 日本語訳（自動翻訳）

> ターゲット += Normal_lpdf(y | mu, sigma);
> インライン コード コメントを最小限に抑え、代わりに読みやすいコードを作成することをお勧めします。上記のように
> 例が示すように、ユーザーにツールを提供するプログラミング言語によってクリーンなコードが容易になります。
> 彼らは使う必要がある。

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- ターゲット += Normal_lpdf(y | mu, sigma); インライン コード コメントを最小限に抑え、代わりに読みやすいコードを作成することをお勧めします。

## Chunk 0508

### English（抽出4行）

> User-facing functions should be documented at the function level in terms of their argument
> types, return types, error conditions, and behavior—that’s the application programming interface
> (API) that users see instead of code internals. The problem with inline code comments aimed at
> developers is that they quickly go stale during development and wind up doing more harm than good.

### 日本語訳（自動翻訳）

> ユーザー向け関数は、引数の観点から関数レベルで文書化する必要があります。
> 型、戻り値の型、エラー条件、および動作 - それがアプリケーション プログラミング インターフェイスです
> コード内部の代わりにユーザーに表示される (API)。インラインコードコメントの問題点
> 開発者にとって、それらは開発中にすぐに古くなり、結局は良いことよりも害を及ぼすことになるということです。

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- ユーザー向け関数は、引数の観点から関数レベルで文書化する必要があります。

## Chunk 0509

### English（抽出4行）

> Instead, rather than documenting the actual code inline, functions should be reduced to manageable
> size and names should be chosen so that the code is readable. Longer variable names are not always
> better, as they can make the structure of the code harder to scan. Code documentation should be
> written assuming the reader understands the programming language well; as such, documentation

### 日本語訳（自動翻訳）

> 実際のコードをインラインで文書化するのではなく、関数を管理しやすいものに減らす必要があります。
> コードが読み取れるようにサイズと名前を選択する必要があります。変数名が常に長いとは限りません
> コードの構造をスキャンするのが難しくなる可能性があるため、より良いです。コードのドキュメントは次のとおりです。
> 読者がプログラミング言語をよく理解していることを前提として書かれています。そのため、ドキュメント

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- 実際のコードをインラインで文書化するのではなく、関数を管理しやすいものに減らす必要があります。

## Chunk 0510

### English（抽出4行）

> is only called for when the code strays from idiomatic usage of the language or involves complex
> Figure 24: Success rate of putts of professional golfers, from a small dataset appearing in Berry
> (1995). The error bars associated with each point j in the graph are simple classical standard
> deviations,

### 日本語訳（自動翻訳）

> コードが言語の慣用的な使用法から逸脱している場合、または複雑なコードが含まれている場合にのみ呼び出されます。
> 図 24: Berry に表示される小さなデータセットからのプロゴルファーのパット成功率
> （1995年）。グラフ内の各点 j に関連付けられた誤差範囲は、単純な古典的な標準です。
> 偏差、

### 熟語・専門語

- **ESS**: 有効サンプルサイズ。自己相関を考慮した独立サンプル相当数。

### 要約

- コードが言語の慣用的な使用法から逸脱している場合、または複雑なコードが含まれている場合にのみ呼び出されます。

## Chunk 0511

### English（抽出4行）

> p
> ˆpj(1 −ˆpj)/nj, where ˆpj = yj/nj is the success rate for putts taken at distance xj.
> algorithms that need external documentation. When tempted to comment a long expression or
> block of code, instead consider replacing it with a well-named function.

### 日本語訳（自動翻訳）

> p
> ＾pj(1 −＾pj)/nj、ここで、＾pj = yj/nj は、距離 xj で行われたパットの成功率です。
> 外部ドキュメントを必要とするアルゴリズム。長い表現をコメントしたいときや、
> コードのブロックを削除する場合は、代わりに適切な名前の関数に置き換えることを検討してください。

### 熟語・専門語

- **ESS**: 有効サンプルサイズ。自己相関を考慮した独立サンプル相当数。

### 要約

- p ＾pj(1 −＾pj)/nj、ここで、＾pj = yj/nj は、距離 xj で行われたパットの成功率です。

## Chunk 0512

### English（抽出4行）

> Related to readability is the maintainability of the workﬂow code. When ﬁtting a series of
> similar models, a lot of modules will be shared between them (see Section 2.2) and so will be the
> corresponding code. If we had just copied all of the model code each time we wrote a new model,
> and then discovered an error in one of the shared modules, we would have to ﬁx it in all models

### 日本語訳（自動翻訳）

> 読みやすさに関連するのは、ワークフロー コードの保守性です。一連のフィッティングを行う場合、
> 同様のモデルでは、多くのモジュールがそれらの間で共有されるため (セクション 2.2 を参照)、
> 対応するコード。新しいモデルを作成するたびにすべてのモデル コードをコピーしていたら、
> その後、共有モジュールの 1 つでエラーが発見された場合は、すべてのモデルでそれを修正する必要があります

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- 読みやすさに関連するのは、ワークフロー コードの保守性です。

## Chunk 0513

### English（抽出4行）

> manually. This is again an error-prone process. Instead, it can be sensible not only to build models
> in a modular manner but also keep the corresponding code modular and load it into the models as
> needed. That way, ﬁxing an error in a module requires changing code in just one rather than many
> places. Errors and other requirements for later changes will inevitably occur as we move through

### 日本語訳（自動翻訳）

> 手動で。これもまたエラーが発生しやすいプロセスです。代わりに、モデルを構築するだけでなく、
> モジュール形式で行いますが、対応するコードもモジュール形式に保ち、それを次のようにモデルにロードします。
> 必要です。そうすれば、モジュール内のエラーを修正するには、多くのコードを変更するのではなく、1 つのコードのみを変更する必要があります。
> 場所。今後の変更に伴うエラーやその他の要件は、必然的に発生します。

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

> ワークフローに合わせてモデリング コードを準備すれば、時間を大幅に節約できます。
> 10.
> モデルの構築と拡張を含むワークフローの例: ゴルフのパッティング
> 適合するモデルのセットの例を使用して、ベイジアン モデリングの基本的なワークフローを示します。

### 熟語・専門語

- **workflow**: ワークフロー。実務分析の反復手順全体。
- **model building**: モデル構築。仮定・データ構造・prior・likelihoodを組み合わせる工程。

### 要約

- ワークフローに合わせてモデリング コードを準備すれば、時間を大幅に節約できます。

## Chunk 0515

### English（抽出4行）

> to data on golf putting (Gelman, 2019).
> Figure 24 shows data from professional golfers on the proportion of successful putts as a
> function of (rounded) distance from the hole. Unsurprisingly, the probability of making the shot
> declines as a function of distance.

### 日本語訳（自動翻訳）

> ゴルフパッティングに関するデータ (Gelman、2019)。
> 図 24 は、プロゴルファーのパット成功率に関するデータを示しています。
> 穴からの（四捨五入された）距離の関数。当然のことながら、シュートを打つ確率は
> 距離の関数として減少します。

### 熟語・専門語

- **ESS**: 有効サンプルサイズ。自己相関を考慮した独立サンプル相当数。

### 要約

- ゴルフパッティングに関するデータ (Gelman、2019)。

## Chunk 0516

### English（抽出4行）

> Figure 25: Golf data from Figure 24 along with ﬁtted logistic regression and draws of the ﬁtted
> curve, y = logit−1(a + bxj), given posterior draws of (a, b).
> Figure 26: Simple geometric model of golf putting, showing the range of angles with which the ball
> can be hit and still have a trajectory that goes entirely into the hole. Not to scale.

### 日本語訳（自動翻訳）

> 図 25: 図 24 のゴルフデータと、近似ロジスティック回帰および近似した結果の描画
> 曲線、y = logit−1(a + bxj)、(a, b) の事後描画を与えます。
> 図 26: ゴルフ パッティングの単純な幾何学的モデル。ボールが傾く角度の範囲を示しています。
> 打っても弾道はホールに完全に入ります。縮尺通りではありません。

### 熟語・専門語

- **ESS**: 有効サンプルサイズ。自己相関を考慮した独立サンプル相当数。
- **posterior draws**: 事後ドロー。事後分布から得たサンプル。

### 要約

- 図 25: 図 24 のゴルフデータと、近似ロジスティック回帰および近似した結果の描画 曲線、y = logit−1(a + bxj)、(a, b) の事後描画を与えます。

## Chunk 0517

### English（抽出4行）

> 10.1.
> First model: logistic regression
> Can we model the probability of success in golf putting as a function of distance from the hole?
> Given usual statistical practice, the natural starting point would be logistic regression:

### 日本語訳（自動翻訳）

> 10.1.
> 最初のモデル: ロジスティック回帰
> ゴルフパッティングの成功確率をホールからの距離の関数としてモデル化することはできるでしょうか?
> 通常の統計手法を考慮すると、自然な開始点はロジスティック回帰になります。

### 熟語・専門語

- **ESS**: 有効サンプルサイズ。自己相関を考慮した独立サンプル相当数。

### 要約

- 10.1. 最初のモデル: ロジスティック回帰 ゴルフパッティングの成功確率をホールからの距離の関数としてモデル化することはできるでしょうか? 通常の統計手法を考慮すると、自然な開始点はロジスティック回帰になります。

## Chunk 0518

### English（抽出4行）

> yj ∼binomial
>  nj, logit−1(a + bxj)
> 
> , for j = 1, . . . , J.

### 日本語訳（自動翻訳）

> yj 〜二項
> nj, logit−1(a + bxj)
> 
> 、j = 1 の場合、 。 。 。 、J.

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- yj 〜二項 nj, logit−1(a + bxj)  、j = 1 の場合、 。

## Chunk 0519

### English（抽出4行）

> Figure 25 shows the logistic ﬁtted regression along with draws form the posterior distribution.
> Here we ﬁt using a uniform prior on (a, b) which causes no problems given the large sample size.
> 10.2.
> Modeling from first principles

### 日本語訳（自動翻訳）

> 図 25 は、事後分布からの描画とともにロジスティック適合回帰を示しています。
> ここでは、(a, b) に均一な事前分布を使用して近似しますが、サンプル サイズが大きいため問題は発生しません。
> 10.2.
> 第一原理に基づいたモデリング

### 熟語・専門語

- **posterior distribution**: 事後分布。データ観測後の未知量の不確実性を表す分布。
- **ESS**: 有効サンプルサイズ。自己相関を考慮した独立サンプル相当数。

### 要約

- 図 25 は、事後分布からの描画とともにロジスティック適合回帰を示しています。

## Chunk 0520

### English（抽出4行）

> We next ﬁt the data using a simple mathematical model of the golf putting process. Figure 26
> shows a simpliﬁed sketch of a golf shot. The dotted line represents the angle within which the
> ball of radius r must be hit so that it falls within the hole of radius R. This threshold angle is
> sin−1((R −r)/x). The graph is intended to illustrate the geometry of the ball needing to go into

### 日本語訳（自動翻訳）

> 次に、ゴルフのパッティングプロセスの単純な数学モデルを使用してデータを適合させます。図26
> ゴルフショットの簡略化されたスケッチを示します。点線は、その範囲内の角度を表します。
> 半径 r のボールは、半径 R の穴に入るように打たれなければなりません。このしきい値角度は次のとおりです。
> sin−1((R −r)/x)。グラフは、ボールがボールに入る必要がある形状を示すことを目的としています。

### 熟語・専門語

- **ESS**: 有効サンプルサイズ。自己相関を考慮した独立サンプル相当数。

### 要約

- 次に、ゴルフのパッティングプロセスの単純な数学モデルを使用してデータを適合させます。

## Chunk 0521

### English（抽出4行）

> the hole.
> Figure 27: Two models ﬁt to the golf data. The geometry-based model ﬁts much better than the
> logistic regression even while using one fewer parameter.
> The next step is to model human error. We assume that the golfer is attempting to hit the ball

### 日本語訳（自動翻訳）

> 穴。
> 図 27: ゴルフ データに適合した 2 つのモデル。ジオメトリベースのモデルは、
> 使用するパラメーターが 1 つ少ない場合でも、ロジスティック回帰が可能になります。
> 次のステップは、人的エラーをモデル化することです。ゴルファーがボールを打とうとしていると仮定します。

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

> 完全に真っ直ぐですが、多くの小さな要因がこの目標を妨げるため、実際の角度は
> は、0 を中心とし、標準偏差 σ を伴う正規分布に従います。
> ボールがホールに入る確率は、角度が角度よりも小さい確率になります。
> しきい値;つまり、

### 熟語・専門語

- **ESS**: 有効サンプルサイズ。自己相関を考慮した独立サンプル相当数。

### 要約

- 完全に真っ直ぐですが、多くの小さな要因がこの目標を妨げるため、実際の角度は は、0 を中心とし、標準偏差 σ を伴う正規分布に従います。

## Chunk 0523

### English（抽出4行）

> Pr(|angle| < sin−1((R −r)/x)) = 2Φ
> sin−1((R −r)/x)
> σ
> 

### 日本語訳（自動翻訳）

> Pr(|角度| < sin−1((R −r)/x)) = 2Φ
> sin−1((R −r)/x)
> σ
> 

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- Pr(|角度| < sin−1((R −r)/x)) = 2Φ sin−1((R −r)/x) σ 

## Chunk 0524

### English（抽出4行）

> −1,
> where Φ is the cumulative normal distribution function. The only unknown parameter in this model
> is σ, the standard deviation of the distribution of shot angles.
> Fitting this model to the above data with a ﬂat prior on σ yields a posterior estimate ˆσ = 1.53◦

### 日本語訳（自動翻訳）

> −1、
> ここで、Φ は累積正規分布関数です。このモデルの唯一の未知のパラメータ
> σ はショット角度の分布の標準偏差です。
> このモデルを上記のデータに σ の事前フラットを使用して当てはめると、事後推定値 ＾σ = 1.53 が得られます。

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- −1、 ここで、Φ は累積正規分布関数です。

## Chunk 0525

### English（抽出4行）

> with standard error 0.02. Figure 27 shows the ﬁtted model, along with the logistic regression ﬁt
> earlier. The custom nonlinear model ﬁts the data much better. This is not to say that the model is
> perfect—any experience of golf will reveal that the angle is not the only factor determining whether
> the ball goes in the hole—but it seems like a useful start, and it demonstrates the advantages of

### 日本語訳（自動翻訳）

> 標準誤差は 0.02 です。図 27 は、フィッティングされたモデルとロジスティック回帰フィットを示しています。
> もっと前に。カスタム非線形モデルはデータにはるかによく適合します。これはモデルがそうだと言っているわけではありません
> 完璧 — ゴルフを経験すれば、角度だけが完璧かどうかを決める唯一の要素ではないことがわかります。
> ボールはホールに入りますが、それは有益なスタートのように見え、それは次の利点を示しています。

### 熟語・専門語

- **ESS**: 有効サンプルサイズ。自己相関を考慮した独立サンプル相当数。

### 要約

- 標準誤差は 0.02 です。

## Chunk 0526

### English（抽出4行）

> building up a model directly rather than simply working with a conventional form.
> 10.3.
> Testing the fitted model on new data
> Several years after ﬁtting the above model, we were presented with a newer and more comprehensive

### 日本語訳（自動翻訳）

> 従来の形式を単に操作するのではなく、モデルを直接構築します。
> 10.3.
> 新しいデータで適合モデルをテストする
> 上記のモデルを当てはめてから数年後、より新しく、より包括的なモデルが提示されました。

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- 従来の形式を単に操作するのではなく、モデルを直接構築します。

## Chunk 0527

### English（抽出4行）

> dataset on professional golf putting (Broadie, 2018). For simplicity we just look here at the summary
> data, probabilities of the ball going into the hole for shots up to 75 feet from the hole. Figure 28
> these new data, along with our earlier dataset and the already-ﬁt geometry-based model from before,
> extending to the range of the new data.

### 日本語訳（自動翻訳）

> プロのゴルフのパッティングに関するデータセット (Broadie、2018)。簡単にするために、ここでは概要だけを見ていきます
> データ、ホールから最大 75 フィートのショットでボールがホールに入る確率。図28
> これらの新しいデータは、以前のデータセットと以前からすでに適合されているジオメトリベースのモデルとともに、
> 新しいデータの範囲まで拡張します。

### 熟語・専門語

- **ESS**: 有効サンプルサイズ。自己相関を考慮した独立サンプル相当数。

### 要約

- プロのゴルフのパッティングに関するデータセット (Broadie、2018)。

## Chunk 0528

### English（抽出4行）

> Comparing the two datasets in the range 0–20 feet, the success rate is similar for longer putts but
> is much higher than before for the short putts. This could be a measurement issue, if the distances
> Figure 28: Checking the already-ﬁt model to new golf putting data. At equivalent distances, the
> success rate is higher for the new data, which may represent improvement over time or just a

### 日本語訳（自動翻訳）

> 0 ～ 20 フィートの範囲で 2 つのデータセットを比較すると、長いパットの成功率は同様ですが、
> ショートパットに関しては以前よりもはるかに高くなっています。距離が異なる場合、これは測定上の問題である可能性があります。
> 図 28: すでに適合しているモデルを新しいゴルフ パッティング データにチェックする。等距離では、
> 新しいデータの成功率はより高く、これは時間の経過による改善、または単なる改善を示している可能性があります。

### 熟語・専門語

- **ESS**: 有効サンプルサイズ。自己相関を考慮した独立サンプル相当数。

### 要約

- 0 ～ 20 フィートの範囲で 2 つのデータセットを比較すると、長いパットの成功率は同様ですが、 ショートパットに関しては以前よりもはるかに高くなっています。

## Chunk 0529

### English（抽出4行）

> diﬀerence in the datasets. In addition, the new data show a systematic model failure at higher
> distances, motivating a model improvement.
> to the hole are only approximate for the old data, and it could also be that golfers are better than
> they used to be.

### 日本語訳（自動翻訳）

> データセットの違い。さらに、新しいデータは、より高いレベルで系統的なモデルの失敗を示しています。
> 距離を測定し、モデルの改善を動機付けます。
> ホールまでの距離は古いデータの近似値にすぎず、ゴルファーの方が優れている可能性もあります。
> 彼らはかつてそうでした。

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

> 20 フィートを超えると、経験的な成功率は従来の予測よりも低くなります。
> モデル。これらは、角度の増加を考慮したとしても、はるかに困難な試みです。
> 距離が伸びるほど精度が求められます。さらに、新しいデータはより滑らかに見えます。
> より包括的なデータ収集を反映しています。

### 熟語・専門語

- **ESS**: 有効サンプルサイズ。自己相関を考慮した独立サンプル相当数。

### 要約

- 20 フィートを超えると、経験的な成功率は従来の予測よりも低くなります。

## Chunk 0531

### English（抽出4行）

> 10.4.
> A new model accounting for how hard the ball is hit
> To get the ball in the hole, the angle is not the only thing you need to control; you also need to hit
> the ball just hard enough.

### 日本語訳（自動翻訳）

> 10.4.
> 打球の強さを考慮した新モデル
> ボールをホールに入れるためにコントロールする必要があるのは角度だけではありません。あなたも叩く必要があります
> ボールは十分に硬いです。

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- 10.4. 打球の強さを考慮した新モデル ボールをホールに入れるためにコントロールする必要があるのは角度だけではありません。

## Chunk 0532

### English（抽出4行）

> Broadie (2018) added this to the geometric model by introducing another parameter corre-
> sponding to the golfer’s control over distance. Supposing u is the distance that golfer’s shot would
> travel if there were no hole, Broadie assumes that the putt will go in if (a) the angle allows the ball
> to go over the hole, and (b) u is in the range [x, x + 3]. That is the ball must be hit hard enough to

### 日本語訳（自動翻訳）

> Broadie (2018) は、別のパラメータ補正を導入することで、これを幾何モデルに追加しました。
> ゴルファーの距離コントロールに応えます。あなたがゴルファーのショットの飛距離であると仮定すると、
> ホールがなかった場合はトラベルし、ブローディは (a) ボールが入る角度であればパットが入ると想定します。
> (b) u は [x, x + 3] の範囲内にあります。つまり、ボールを十分に強く打たなければなりません。

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- Broadie (2018) は、別のパラメータ補正を導入することで、これを幾何モデルに追加しました。

## Chunk 0533

### English（抽出4行）

> reach the whole but not go too far. Factor (a) is what we have considered earlier; we must now add
> factor (b).
> Figure 29 illustrates the need for the distance as well as the angle of the shot to be in some
> range, in this case the gray zone which represents the trajectories for which the ball would reach

### 日本語訳（自動翻訳）

> 全体に到達しますが、行き過ぎないでください。要素 (a) は以前に検討したものです。ここで追加する必要があります
> 要因(b)。
> 図 29 は、ショットの距離と角度がある程度必要であることを示しています。
> 範囲、この場合はボールが到達する軌道を表すグレーゾーン

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- 全体に到達しますが、行き過ぎないでください。

## Chunk 0534

### English（抽出4行）

> the hole and stay in it.
> Broadie supposes that a golfer will aim to hit the ball one foot past the hole but with a
> multiplicative error in the shot’s potential distance, so that u = (x + 1) · (1 + ϵ), where the error
> ϵ has a normal distribution with mean 0 and standard deviation σdistance. In statistics notation, this

### 日本語訳（自動翻訳）

> 穴に留まってください。
> ブローディ氏は、ゴルファーはホールから 1 フィート先のボールを打つことを目標としているが、
> ショットの潜在的な距離の乗算誤差。u = (x + 1) · (1 + ϵ) になります。ここで、誤差は
> ϵ は、平均 0、標準偏差 σ distance の正規分布を持ちます。統計表記では、これは

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- 穴に留まってください。

## Chunk 0535

### English（抽出4行）

> Figure 29: Geometric model of golf putting, also including the constraint that the ball must be hit
> hard enough to reach the hole but not so hard that it hops over. Not to scale.
> model is, u ∼normal(x+1, (x+1)σdistance), and the distance is acceptable if u ∈[x, x+3], an event
> that has probability Φ

### 日本語訳（自動翻訳）

> 図 29: ボールを打たなければならないという制約も含む、ゴルフ パッティングの幾何学的モデル
> 穴に届くほどの硬さはありますが、飛び越えるほどではありません。縮尺通りではありません。
> モデルは u 〜normal(x+1, (x+1)σ distance) であり、u ∈[x, x+3]、イベントの場合、距離は許容されます。
> 確率Φを持つ

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- 図 29: ボールを打たなければならないという制約も含む、ゴルフ パッティングの幾何学的モデル 穴に届くほどの硬さはありますが、飛び越えるほどではありません。

## Chunk 0536

### English（抽出4行）

> 
> (x+1)σdistance
> 
> −Φ

### 日本語訳（自動翻訳）

> 
> (x+1)σ距離
> 
> −Φ

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

-  (x+1)σ距離  −Φ

## Chunk 0537

### English（抽出4行）

> 
> −1
> (x+1)σdistance
> 

### 日本語訳（自動翻訳）

> 
> −1
> (x+1)σ距離
> 

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

-  −1 (x+1)σ距離 

## Chunk 0538

### English（抽出4行）

> . Putting these together, the probability a
> shot goes in becomes,
> 
> 2Φ

### 日本語訳（自動翻訳）

> 。これらをまとめると、確率は
> ショットが入ります、
> 
> 2Φ

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- 。

## Chunk 0539

### English（抽出4行）

> 
> sin−1((R−r)/x)
> σangle
> 

### 日本語訳（自動翻訳）

> 
> sin−1((R−r)/x)
> σ角度
> 

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

-  sin−1((R−r)/x) σ角度 

## Chunk 0540

### English（抽出4行）

> −1
>  
> Φ
> 

### 日本語訳（自動翻訳）

> −1
>  
> Φ
> 

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- −1   Φ 

## Chunk 0541

### English（抽出4行）

> (x+1)σdistance
> 
> −Φ
> 

### 日本語訳（自動翻訳）

> (x+1)σ距離
> 
> −Φ
> 

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- (x+1)σ距離  −Φ 

## Chunk 0542

### English（抽出4行）

> −1
> (x+1)σdistance
> 
> , where

### 日本語訳（自動翻訳）

> −1
> (x+1)σ距離
> 
> 、ここで

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- −1 (x+1)σ距離  、ここで

## Chunk 0543

### English（抽出4行）

> we have renamed the parameter σ from our earlier model to σangle to distinguish it from the new
> σdistance parameter.
> The result is a model with two parameters, σangle and σdistance. Even this improved geometry-
> based model is a gross oversimpliﬁcation of putting, and the average distances in the binned data

### 日本語訳（自動翻訳）

> 新しいモデルと区別するために、以前のモデルのパラメーター σ の名前を σangle に変更しました。
> σ距離パラメータ。
> 結果は、σangle と σ distance という 2 つのパラメーターを持つモデルになります。この改善されたジオメトリでも、
> ベースのモデルはパッティングを著しく単純化しすぎており、ビン化されたデータの平均距離は

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- 新しいモデルと区別するために、以前のモデルのパラメーター σ の名前を σangle に変更しました。

## Chunk 0544

### English（抽出4行）

> are not the exact distances for each shot. But it should be an advance on the earlier one-parameter
> model; the next step is to see how it ﬁts the data.
> We ﬁrst try to ﬁt this model with ﬂat priors, but the result is computationally unstable, so we
> assign weakly informative half-normal(0, 1) priors. Even after this, we have poor convergence.

### 日本語訳（自動翻訳）

> 各ショットの正確な距離ではありません。しかし、これは以前の 1 つのパラメータよりも進歩しているはずです
> モデル;次のステップは、それがデータにどのように適合するかを確認することです。
> まずこのモデルをフラット事前確率で当てはめようとしますが、結果は計算的に不安定なので、
> 情報量の少ないhalf-normal(0, 1) 事前分布を割り当てます。この後でも、収束は不十分です。

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

> 4 つのチェーンをそれぞれ 2000 回反復して実行すると、高い bR 値が得られ、混合が不十分であることを示します。
> このため、民間定理 (セクション 5.1 を参照) に従ってモデルが心配になります。
> この場合、トレースプロットを調べたり、その他の方法で病状を研究したりするのではなく、
> マルコフ連鎖シミュレーションでは、次の式を使用して推定されたモデルの適合性を直接検査するだけです。

### 熟語・専門語

- **Markov chain**: マルコフ連鎖。MCMCで事後分布からサンプルを得るための確率過程。

### 要約

- 4 つのチェーンをそれぞれ 2000 回反復して実行すると、高い bR 値が得られ、混合が不十分であることを示します。

## Chunk 0546

### English（抽出4行）

> crude estimates of the parameters obtained by averaging the simulations over the poorly-mixing
> chains.
> Figure 30a shows the result. The overall ﬁt is not terrible, but there are problems in the middle
> of the curve, and after some thought we realized that the model is struggling because the binomial

### 日本語訳（自動翻訳）

> 混合が不十分な場合のシミュレーションを平均することで得られるパラメータの大まかな推定値
> 鎖。
> 図 30a は結果を示しています。全体的なフィット感は悪くありませんが、真ん中に問題があります
> 少し考えた後、二項式が原因でモデルが苦労していることに気付きました。

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- 混合が不十分な場合のシミュレーションを平均することで得られるパラメータの大まかな推定値 鎖。

## Chunk 0547

### English（抽出4行）

> likelihood is constraining it too strongly at the upper left part of the curve where the counts are
> higher. Look at how closely the ﬁtted curve hugs the data at the very lowest values of x.
> Figure 30b displays the data, which was given to us in binned form, for putts from the shortest
> distances. Because of the vary large sample sizes, the binomial model tries very hard to ﬁt these

### 日本語訳（自動翻訳）

> カウントが表示される曲線の左上の部分で、可能性が強く制限されすぎている可能性があります。
> より高い。フィッティングされた曲線が x の最も低い値でデータにどれだけ近似しているかを見てください。
> 図 30b は、ビン形式で提供された、最短からのパットのデータを示しています。
> 距離。サンプルサイズがさまざまであるため、二項モデルはこれらを適合させるために非常に努力します。

### 熟語・専門語

- **likelihood**: 尤度。パラメータが与えられたときデータがどれだけ起こりやすいか。

### 要約

- カウントが表示される曲線の左上の部分で、可能性が強く制限されすぎている可能性があります。

## Chunk 0548

### English（抽出4行）

> probabilities as exactly as possible. The likelihood function gives by far its biggest weight to these
> ﬁrst few data points. If we were sure the model was correct, this would be the right thing to do, but
> given inevitable model error, the result is a problematic ﬁt to the entire curve. In addition, the poor
> MCMC convergence is understandable: there are no parameter values that ﬁt all the data, and it is

### 日本語訳（自動翻訳）

> 可能な限り正確な確率。尤度関数はこれらに圧倒的に最大の重みを与えます。
> 最初のいくつかのデータポイント。モデルが正しいと確信できれば、これは正しいことですが、
> 避けられないモデル誤差を考慮すると、結果は曲線全体への適合に問題が生じます。さらに、貧しい人たちは、
> MCMC の収束は理解できます。すべてのデータに適合するパラメータ値は存在せず、

### 熟語・専門語

- **likelihood**: 尤度。パラメータが与えられたときデータがどれだけ起こりやすいか。

### 要約

- 可能な限り正確な確率。

## Chunk 0549

### English（抽出4行）

> diﬃcult for the chains to move smoothly between values that ﬁt the bulk of the data and those that
> ﬁt the ﬁrst few data points.
> 10.5.
> Expanding the model by including a fudge factor

### 日本語訳（自動翻訳）

> データの大部分に適合する値と、データの大部分に適合する値の間をチェーンがスムーズに移動することが困難です。
> 最初のいくつかのデータポイントを当てはめます。
> 10.5。
> ファッジ要素を含めてモデルを拡張する

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- データの大部分に適合する値と、データの大部分に適合する値の間をチェーンがスムーズに移動することが困難です。

## Chunk 0550

### English（抽出4行）

> As the data are binned, the individual putt distances have been rounded to the bin center values,
> which has the biggest eﬀect in very short distances. We could incorporate a rounding error model
> x
> n

### 日本語訳（自動翻訳）

> データがビン化されると、個々のパットの距離はビンの中心値に丸められます。
> 非常に短い距離で最も大きな効果を発揮します。丸め誤差モデルを組み込むことができます
> ×
> n

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- データがビン化されると、個々のパットの距離はビンの中心値に丸められます。

## Chunk 0551

### English（抽出4行）

> y
> 0.28
> 0.97
> 1.93

### 日本語訳（自動翻訳）

> y
> 0.28
> 0.97
> 1.93

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- y 0.28 0.97 1.93

## Chunk 0552

### English（抽出4行）

> 2.92
> 3.93
> . . .
> . . .

### 日本語訳（自動翻訳）

> 2.92
> 3.93
> 。 。 。
> 。 。 。

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- 2.92 3.93 。

## Chunk 0553

### English（抽出4行）

> . . .
> Figure 30: Working to understand the poor convergence of the expanded golf putting model that
> had showed poor convergence. (a) A graph of data and ﬁtted model reveals problems with the
> ﬁt near the middle of the curve, and we realized that the poor behavior of the Markov simulation

### 日本語訳（自動翻訳）

> 。 。 。
> 図 30: 拡張されたゴルフ パッティング モデルの収束が不十分であることを理解するための作業
> 収束性が悪いことが示されました。 (a) データと近似モデルのグラフから問題が明らかになります。
> 曲線の中央付近にフィットし、マルコフ シミュレーションの動作が悪いことがわかりました。

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- 。

## Chunk 0554

### English（抽出4行）

> arose from the model trying too hard to ﬁt the data at the upper left of the curve. (b) Data for putts
> from the shortest distances, with x being the average distance for the putts in each bin (presumably
> 0–0.5 feet, 0.5–1.5 feet, 1.5–2.5, etc.). Sample sizes are very large in the initial bins, hence the
> binomial model tries to ﬁt these points nearly exactly.

### 日本語訳（自動翻訳）

> これは、モデルが曲線の左上にデータを当てはめようとしすぎたために生じたものです。 (b) パットのデータ
> 最短距離からの距離。x は各ビン内のパットの平均距離 (おそらく
> 0 ～ 0.5 フィート、0.5 ～ 1.5 フィート、1.5 ～ 2.5 など）。初期ビンではサンプル サイズが非常に大きいため、
> 二項モデルは、これらの点をほぼ正確に当てはめようとします。

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- これは、モデルが曲線の左上にデータを当てはめようとしすぎたために生じたものです。

## Chunk 0555

### English（抽出4行）

> for the putting distances, but we opt for a simpler error model. To allow for a model that can ﬁt
> reasonably well to all the data without being required to have a hyper-precise ﬁt to the data at the
> shortest distances, we took the data model, yj ∼binomial(nj, pj), and added an independent error
> term to each observation. There is no easy way to add error directly to the binomial distribution—

### 日本語訳（自動翻訳）

> パッティングの距離については、より単純なエラー モデルを選択します。適合できるモデルを可能にするために
> データに非常に正確に適合する必要がなく、すべてのデータに対して適度に適合します。
> 最短距離では、データ モデル yj 〜binomial(nj, pj) を使用し、独立誤差を追加しました。
> 各観測に対する用語。二項分布に誤差を直接追加する簡単な方法はありません。

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- パッティングの距離については、より単純なエラー モデルを選択します。

## Chunk 0556

### English（抽出4行）

> we could replace it with its overdispersed generalization, the beta-binomial, but this would not be
> appropriate here because the variance for each data point j would still be roughly proportional to
> the sample size nj, and our whole point here is to get away from that assumption and allow for
> model misspeciﬁcation—so instead we ﬁrst approximate the binomial data distribution by a normal

### 日本語訳（自動翻訳）

> これを過分散一般化であるベータ二項式に置き換えることもできますが、これはそうではありません。
> 各データ点 j の分散は引き続き次の値にほぼ比例するため、ここでは適切です。
> サンプルサイズ nj ですが、ここでの重要な点は、その仮定から離れて、次のことを考慮することです。
> モデルの仕様が間違っているため、代わりに、まず二項データ分布を正規分布で近似します。

### 熟語・専門語

- **approximate**: 近似。速度や扱いやすさのため、正確な推論・モデルを緩めること。

### 要約

- これを過分散一般化であるベータ二項式に置き換えることもできますが、これはそうではありません。

## Chunk 0557

### English（抽出4行）

> and then add independent variance; thus:
> yj/nj ∼normal
> 
> pj,

### 日本語訳（自動翻訳）

> 次に独立分散を追加します。したがって:
> yj/nj 〜正常
> 
> パジャマ、

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- 次に独立分散を追加します。

## Chunk 0558

### English（抽出4行）

> q
> pj(1 −pj)/nj + σ2
> y
> 

### 日本語訳（自動翻訳）

> q
> pj(1 −pj)/nj + σ2
> y
> 

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- q pj(1 −pj)/nj + σ2 y 

## Chunk 0559

### English（抽出4行）

> .
> This model has its own problems and would fall apart if the counts in any cell were small enough,
> but it is transparent and easy to set up and code, and so we try it out, with the understanding that
> we can clean it up later on if necessary.

### 日本語訳（自動翻訳）

> 。
> このモデルには独自の問題があり、セルのカウントが十分に小さい場合には崩壊してしまいます。
> しかし、これは透過的で、セットアップとコーディングが簡単なので、次のことを理解した上で試してみます。
> 必要に応じて後でクリーンアップできます。

### 熟語・専門語

- **ESS**: 有効サンプルサイズ。自己相関を考慮した独立サンプル相当数。

### 要約

- 。

## Chunk 0560

### English（抽出4行）

> After assigning independent half-normal(0, 1) priors to all three parameters of this new model,
> it ﬁts with no problem in Stan, yielding the posterior mean estimates σangle = 1.02◦, σdistance = 0.08
> (implying that shots can be hit to an uncertainty of about 8% in distance), and σy = 0.003 (implying
> that the geometric model sketched in ﬁgure 29 ﬁts the aggregate success rate as a function of distance

### 日本語訳（自動翻訳）

> この新しいモデルの 3 つのパラメーターすべてに独立したhalf-normal(0, 1) 事前分布を割り当てた後、
> Stan では問題なく適合し、事後平均推定値 σangle = 1.02°、σ distance = 0.08 が得られます。
> (距離の不確実性が約 8% までショットを打つことができることを意味します)、σy = 0.003 (意味します)
> 図 29 にスケッチした幾何学的モデルは、距離の関数として総成功率に適合します。

### 熟語・専門語

- **ESS**: 有効サンプルサイズ。自己相関を考慮した独立サンプル相当数。
- **uncertainty**: 不確実性。観測・パラメータ・モデル構造・意思決定に残る曖昧さ。

### 要約

- この新しいモデルの 3 つのパラメーターすべてに独立したhalf-normal(0, 1) 事前分布を割り当てた後、 Stan では問題なく適合し、事後平均推定値 σangle = 1.02°、σ distance = 0.08 が得…

## Chunk 0561

### English（抽出4行）

> to an accuracy of 0.3 percentage points).
> Figure 31: (a) With the additional error term added, the model sketched in Figure 29 provides an
> excellent ﬁt to the expanded golf putting data. (b) The residuals from the ﬁtted model are small and
> show no pattern, thus we see no obvious directions of improvement at this point.

### 日本語訳（自動翻訳）

> 精度は 0.3 パーセント ポイントです）。
> 図 31: (a) 追加の誤差項を追加すると、図 29 でスケッチしたモデルは、
> 拡張されたゴルフパッティングデータへの優れた適合性。 (b) 適合モデルからの残差は小さく、
> パターンは示されていないため、現時点では明確な改善の方向性は見当たりません。

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- 精度は 0.3 パーセント ポイントです）。

## Chunk 0562

### English（抽出4行）

> Figure 31 shows the ﬁtted model and the residuals, yj/nj −ˆpj, as a function of distance. The ﬁt
> is good, and the residuals show no strong pattern, also they are low in absolute value—the model
> predicts the success rate to within half a percentage point at most distances, suggesting not that the
> model is perfect but that there are no clear ways to develop it further just given the current data.

### 日本語訳（自動翻訳）

> 図 31 は、近似モデルと残差 yj/nj − ^pj を距離の関数として示しています。フィット感
> 良好で、残差は強いパターンを示さず、絶対値も低い - モデル
> は、ほとんどの距離で成功率を 0.5 パーセント ポイント以内に予測します。
> モデルは完璧ですが、現在のデータを考慮すると、それをさらに発展させる明確な方法はありません。

### 熟語・専門語

- **ESS**: 有効サンプルサイズ。自己相関を考慮した独立サンプル相当数。

### 要約

- 図 31 は、近似モデルと残差 yj/nj − ^pj を距離の関数として示しています。

## Chunk 0563

### English（抽出4行）

> There are various ways the model could be improved, most obviously by breaking down the
> data and allowing the two parameters to vary by golfer, hole, and weather conditions. As discussed
> earlier, a key motivation for model expansion is to allow the inclusion of more data, in this case
> classifying who was taking the shot and where.

### 日本語訳（自動翻訳）

> モデルを改善するにはさまざまな方法がありますが、最も明白なのは、
> データを使用し、ゴルファー、ホール、気象条件によって 2 つのパラメーターを変更できるようにします。議論したように
> 前述したように、モデル拡張の主な動機は、より多くのデータを含めることができるようにすることです。この場合、
> 誰がどこで撮影したかを分類します。

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- モデルを改善するにはさまざまな方法がありますが、最も明白なのは、 データを使用し、ゴルファー、ホール、気象条件によって 2 つのパラメーターを変更できるようにします。

## Chunk 0564

### English（抽出4行）

> 10.6.
> General lessons from the golf example
> This was an appealing example in that a simple one-parameter model ﬁt the initial dataset, and then
> the new data were ﬁt by adding just one more parameter to capture uncertainty in distance as well

### 日本語訳（自動翻訳）

> 10.6。
> ゴルフの例から得られる一般的な教訓
> これは、単純な 1 パラメータ モデルが初期データセットに適合するという点で魅力的な例でした。
> 新しいデータは、距離の不確実性も捉えるためにパラメータを 1 つ追加するだけで適合されました

### 熟語・専門語

- **ESS**: 有効サンプルサイズ。自己相関を考慮した独立サンプル相当数。
- **uncertainty**: 不確実性。観測・パラメータ・モデル構造・意思決定に残る曖昧さ。

### 要約

- 10.6。

## Chunk 0565

### English（抽出4行）

> as angle of the shot. A notable feature of the model expansion was that the binomial likelihood
> was too strong and made it diﬃcult for the new model to ﬁt all the data at once. Such problems
> of stickiness—which appear in the computation as well as with the inference—are implicit in any
> Bayesian model, but they can become more prominent when as sample size increases.

### 日本語訳（自動翻訳）

> ショットの角度として。モデル拡張の注目すべき特徴は、二項尤度が
> 強すぎるため、新しいモデルがすべてのデータを一度に適合させることが困難になりました。このような問題
> スティッキー性（推論だけでなく計算にも現れます）は、あらゆるものに暗黙的に含まれています。
> ベイジアン モデルですが、サンプル サイズが増加すると、より顕著になる可能性があります。

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

> これは、より大きなデータにはより大きなモデルが必要であるという一般原則の一例です。この場合、私たちは
> 基礎的なゴルフ解釈を持たない誤差項を追加することで 2 番目のモデルを拡張しました。
> ただし、モデルをデータに柔軟に適合させることができました。これは、多施設共同治験で私たちがどのように行うかに似ています。
> 特に関心がなくても、治療効果が部位によって異なる可能性があります。

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- これは、より大きなデータにはより大きなモデルが必要であるという一般原則の一例です。

## Chunk 0567

### English（抽出4行）

> variation, just because this can capture otherwise unexplained aspects of the data, and it is also
> similar to the idea in classical analysis of variance of including a fully saturated interaction term to
> represent residual error.
> The golf example also illustrates the way that inferences from a sequence of models can be

### 日本語訳（自動翻訳）

> これは、他の方法では説明できないデータの側面を捉えることができるためであり、また、
> 完全に飽和した交互作用項を含めるという古典的な分散分析の考え方に似ています。
> 残留誤差を表します。
> ゴルフの例は、一連のモデルから推論を行う方法も示しています。

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- これは、他の方法では説明できないデータの側面を捉えることができるためであり、また、 完全に飽和した交互作用項を含めるという古典的な分散分析の考え方に似ています。

## Chunk 0568

### English（抽出4行）

> compared, both by graphing predictions along with data and by studying the way that parameter
> estimates change as the model is expanded. For example, when we add uncertainty in the distance
> of the shot, our estimate of the angular uncertainty decreases. Finally, we recognize that even the
> ﬁnal ﬁtted model is a work in progress, and so we want to work in a probabilistic programming

### 日本語訳（自動翻訳）

> データとともに予測をグラフ化することと、パラメーターがどのように変化するかを研究することによって比較します。
> 推定値はモデルが拡張されると変化します。たとえば、遠くに不確実性を加えると、
> ショットの角度が大きくなると、角度の不確実性の推定値が減少します。最後に、私たちは、
> 最終的な適合モデルは進行中の作業であるため、確率的プログラミングで作業したいと考えています。

### 熟語・専門語

- **probabilistic programming**: 確率的プログラミング。Stanなどで確率モデルをコードとして記述し推論する方法。
- **ESS**: 有効サンプルサイズ。自己相関を考慮した独立サンプル相当数。
- **uncertainty**: 不確実性。観測・パラメータ・モデル構造・意思決定に残る曖昧さ。
- **prediction**: 予測。未知/将来/除外データに対する分布や点推定。

### 要約

- データとともに予測をグラフ化することと、パラメーターがどのように変化するかを研究することによって比較します。

## Chunk 0569

### English（抽出4行）

> environment where we can expand it by allowing the parameters to vary by player and condition of
> the course.
> 11.
> Example of workflow for a model with unexpected multimodality: Planetary

### 日本語訳（自動翻訳）

> プレイヤーやコンディションに応じてパラメーターを変更できるようにすることで拡張できる環境
> コース。
> 11.
> 予期せぬマルチモダリティを持つモデルのワークフローの例: 惑星

### 熟語・専門語

- **multimodality**: 多峰性。事後分布に複数の山があり、MCMCが混合しにくい状態。
- **workflow**: ワークフロー。実務分析の反復手順全体。

### 要約

- プレイヤーやコンディションに応じてパラメーターを変更できるようにすることで拡張できる環境 コース。

## Chunk 0570

### English（抽出4行）

> motion
> The previous example was relatively straightforward in that we built a model and gradually improved
> it. Next we consider a case study in which we start with a complicated model, encounter problems
> with our inference, and have to ﬁgure out what is going on.

### 日本語訳（自動翻訳）

> 動き
> 前の例は、モデルを構築し、徐々に改善したという点で比較的単純でした。
> それ。次に、複雑なモデルから始めて問題が発生するケーススタディを検討します。
> 私たちの推論を使って、何が起こっているのかを理解する必要があります。

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- 動き 前の例は、モデルを構築し、徐々に改善したという点で比較的単純でした。

## Chunk 0571

### English（抽出4行）

> Section 3.4 alludes to measurements of a planet’s motion. Let us now investigate this example
> from a slightly diﬀerent perspective. While simple in appearance, this problem illustrates many
> of the concepts we have discussed and highlights that the workﬂow draws on both statistical and
> ﬁeld expertise. It also cautions us that the workﬂow is not an automated process; each step requires

### 日本語訳（自動翻訳）

> セクション 3.4 では、惑星の運動の測定について触れています。この例を調べてみましょう
> 少し違う視点から。一見単純ですが、この問題は多くのことを示しています。
> これまで説明してきた概念を説明し、ワークフローが統計と統計の両方に基づいていることを強調します。
> フィールドの専門知識。また、ワークフローは自動化されたプロセスではないことも警告しています。各ステップに必要なのは

### 熟語・専門語

- **ESS**: 有効サンプルサイズ。自己相関を考慮した独立サンプル相当数。

### 要約

- セクション 3.4 では、惑星の運動の測定について触れています。

## Chunk 0572

### English（抽出4行）

> careful reasoning. For many problems we have encountered ﬁnding the right visualization tools
> is often the key to understand our model, its limitations, and how to improve it. This example is
> no exception. We monitor various intermediate quantities as prescribed in Section 5.4, and make
> extensive use of predictive checks (Sections 2.4 and 6.1).

### 日本語訳（自動翻訳）

> 慎重な推論。適切な視覚化ツールを見つけるために遭遇した多くの問題
> 多くの場合、これがモデルとその限界、そしてそれを改善する方法を理解するための鍵となります。この例は
> 例外はありません。セクション 5.4 で規定されているさまざまな中間量を監視し、
> 予測チェックの広範な使用 (セクション 2.4 および 6.1)。

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- 慎重な推論。

## Chunk 0573

### English（抽出4行）

> 11.1.
> Mechanistic model of motion
> Instead of ﬁtting an ellipse, we use a mechanistic model based on elementary notions of classical
> mechanics. This allows us to estimate quantities of physical interest, such as stellar mass, and more

### 日本語訳（自動翻訳）

> 11.1.
> 運動の機構モデル
> 楕円を当てはめる代わりに、古典的な基本概念に基づいた機構モデルを使用します。
> 力学。これにより、星の質量など、物理的に興味深い量を推定できるようになります。

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- 11.1. 運動の機構モデル 楕円を当てはめる代わりに、古典的な基本概念に基づいた機構モデルを使用します。

## Chunk 0574

### English（抽出4行）

> readily apply domain knowledge, as well as track the planet’s trajectory in space and time.
> We can describe the planet’s motion using Newton’s laws, which is a second-order diﬀerential
> equation or equivalently a system of two ﬁrst-order diﬀerential equations, which yields Hamilton’s
> formulation:

### 日本語訳（自動翻訳）

> 専門分野の知識を容易に適用できるだけでなく、時空間における惑星の軌道を追跡することもできます。
> 惑星の運動は二次微分であるニュートンの法則を使って説明できます。
> 方程式、または同等の 2 つの一次微分方程式からなる系であり、ハミルトンの次の式が得られます。
> 配合:

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- 専門分野の知識を容易に適用できるだけでなく、時空間における惑星の軌道を追跡することもできます。

## Chunk 0575

### English（抽出4行）

> dq
> dt
> =
> p

### 日本語訳（自動翻訳）

> dq
> dt
> =
> p

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- dq dt = p

## Chunk 0576

### English（抽出4行）

> m
> dp
> dt
> =

### 日本語訳（自動翻訳）

> メートル
> DP
> dt
> =

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- メートル DP dt =

## Chunk 0577

### English（抽出4行）

> −k
> r3(q −q∗),
> where
> • q(t) is the planet’s position vector over time,

### 日本語訳（自動翻訳）

> −k
> r3(q −q∗),
> どこで
> • q(t) は時間の経過に伴う惑星の位置ベクトルです。

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- −k r3(q −q∗), どこで • q(t) は時間の経過に伴う惑星の位置ベクトルです。

## Chunk 0578

### English（抽出4行）

> • p(t) is the planet’s momentum vector over time,
> • m is the planet’s mass (assumed to be 1 in some units),
> • k = GmM, with G = 10−3, the gravitational constant in the appropriate units, and M the
> stellar mass; hence k = 10−3M,

### 日本語訳（自動翻訳）

> • p(t) は時間の経過に伴う惑星の運動量ベクトルです。
> • m は惑星の質量 (一部の単位では 1 であると想定されます)、
> • k = GmM、G = 10−3 は適切な単位の重力定数、M は
> 恒星の質量。したがって、k = 10−3M、

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- • p(t) は時間の経過に伴う惑星の運動量ベクトルです。

## Chunk 0579

### English（抽出4行）

> • and r =
> p
> (q −q∗)T(q −q∗) is the distance between the planet and the star, with q∗denoting
> the star’s position (assumed to be ﬁxed).

### 日本語訳（自動翻訳）

> • および r =
> p
> (q −q∗)T(q −q∗) は惑星と恒星の間の距離であり、q∗ は
> 星の位置 (固定されていると仮定します)。

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- • および r = p (q −q∗)T(q −q∗) は惑星と恒星の間の距離であり、q∗ は 星の位置 (固定されていると仮定します)。

## Chunk 0580

### English（抽出4行）

> The planet moves on a plane, hence p and q are each vectors of length 2. The diﬀerential equations
> tell us that the change in position is determined by the planet’s momentum and that the change in
> momentum is itself driven by gravity.
> We would like to infer the gravitational force between the star and the planet, and in particular

### 日本語訳（自動翻訳）

> 惑星は平面上を移動するため、p と q はそれぞれ長さ 2 のベクトルです。 微分方程式
> 位置の変化は惑星の運動量によって決まり、位置の変化は惑星の運動量によって決まると教えてください。
> 運動量自体は重力によって動かされます。
> 私たちは星と惑星の間の重力、特に

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- 惑星は平面上を移動するため、p と q はそれぞれ長さ 2 のベクトルです。

## Chunk 0581

### English（抽出4行）

> the latent variable k. Other latent variables include the initial position and momentum of the
> planet, respectively q0 and p0, the subsequent positions of the planet, q(t), and the position of the
> star, q∗. Realistically, an astronomer would use cylindrical coordinates but for simplicity we stick
> to Cartesian coordinates. We record the planet’s position over regular time intervals, and assume

### 日本語訳（自動翻訳）

> 潜在変数 k。他の潜在変数には、初期位置と運動量が含まれます。
> 惑星、それぞれ q0 と p0、その後の惑星の位置 q(t)、および
> 星、q∗。現実的には、天文学者は円筒座標を使用するでしょうが、簡単にするためにここでは円筒座標を使用します。
> デカルト座標に変換します。私たちは定期的に惑星の位置を記録し、次のように仮定します。

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- 潜在変数 k。

## Chunk 0582

### English（抽出4行）

> measurements qobs,1, . . . , qobs,n at times t1, . . . , tn, where each observation qobs,i is two-dimensional
> with independent normally distributed errors,
> qobs,i ∼N2(q(ti), σ2I).
> We follow our general workﬂow and ﬁt the model using fake data to see if we can recover the

### 日本語訳（自動翻訳）

> 測定値 qobs,1, . 。 。 、ｑｏｂｓ、ｎ、時刻ｔ１、． 。 。 、tn、各観測値 qobs,i は 2 次元です
> 独立した正規分布誤差を伴う、
> qobs,i 〜N2(q(ti), σ2I)。
> 一般的なワークフローに従い、偽のデータを使用してモデルを適合させ、データを復元できるかどうかを確認します。

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- 測定値 qobs,1, . 。

## Chunk 0583

### English（抽出4行）

> assumed parameter values. We run an MCMC sampler for this model with Stan, which supports a
> numerical ordinary diﬀerential equation (ODE) solver. A ﬁrst attempt fails dramatically: the chains
> do not converge and take a long time to run. This is an invitation to start with a simpler model,
> again working in the controlled setting oﬀered by simulated data, where we know the true value of

### 日本語訳（自動翻訳）

> 想定されるパラメータ値。このモデルの MCMC サンプラーを Stan で実行します。
> 数値常微分方程式 (ODE) ソルバー。最初の試みは劇的に失敗します: チェーン
> 収束せず、実行に時間がかかります。これは、より単純なモデルから始めることをお勧めします。
> シミュレートされたデータによって提供される制御された設定で再び作業し、そこで真の値がわかります。

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
> 単純化されたモデルのフィッティング
> 理想的には、より管理しやすく、なおかつ次のことを示す単純化を見つけることです。

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

> アルゴリズムが遭遇する問題。
> 最初の単純化されたモデルは、事前の
> k 〜normal+(0, 1)、および k = 1 の真の値を仮定します。他のパラメーターを設定します。
> m = 1、q∗= (0, 0)、q0 = (1, 0)、および p0 = (0, 1) でのモデル。パラメータ空間は 1- なので、

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- アルゴリズムが遭遇する問題。

## Chunk 0586

### English（抽出4行）

> dimensional, we can compute the posterior distribution using quadrature; nevertheless we use
> MCMC, because our goal is to understand the challenges that frustrate our sampling algorithm.
> We run 8 chains, each with 500 iterations for the warmup phase and 500 more for the sampling
> phase, and we see:

### 日本語訳（自動翻訳）

> 次元の場合、求積法を使用して事後分布を計算できます。それにもかかわらず、私たちは使用します
> MCMC さん。私たちの目標は、サンプリング アルゴリズムを妨げる課題を理解することだからです。
> 8 つのチェーンを実行します。各チェーンでは、ウォームアップ フェーズで 500 回の反復、サンプリングでさらに 500 回の反復が行われます。
> フェーズに進むと、次のようになります。

### 熟語・専門語

- **posterior distribution**: 事後分布。データ観測後の未知量の不確実性を表す分布。
- **ESS**: 有効サンプルサイズ。自己相関を考慮した独立サンプル相当数。

### 要約

- 次元の場合、求積法を使用して事後分布を計算できます。

## Chunk 0587

### English（抽出4行）

> • The run time varies widely between chains, ranging from ∼2 seconds to ∼2000 seconds.
> While not necessarily a concern in itself, this indicates the chains are behaving in substantially
> diﬀerent ways.
> • bR for some parameters are large, implying that the chains have not mixed. Typically, we are

### 日本語訳（自動翻訳）

> • 実行時間はチェーン間で大きく異なり、約 2 秒から約 2000 秒の範囲です。
> それ自体は必ずしも懸念事項ではありませんが、これはチェーンが大幅に動作していることを示しています。
> さまざまな方法。
> • 一部のパラメータの bR は大きく、チェーンが混合していないことを意味します。通常、私たちは

### 熟語・専門語

- **ESS**: 有効サンプルサイズ。自己相関を考慮した独立サンプル相当数。

### 要約

- • 実行時間はチェーン間で大きく異なり、約 2 秒から約 2000 秒の範囲です。

## Chunk 0588

### English（抽出4行）

> comfortable with bR < 1.01. When bR > 2, this is an indication that the chains are not mixing
> well.
> Faced with these issues, we examine the traceplots (Figure 32). The chains seem to be stuck at
> local modes and do not cohesively explore the posterior space. Some chains have much lower log

### 日本語訳（自動翻訳）

> bR < 1.01 で快適。 bR > 2 の場合、これはチェーンが混合していないことを示します。
> まあ。
> これらの問題に直面して、トレースプロットを調べます (図 32)。鎖が引っかかってしまったようです
> ローカルモードであり、事後空間を一貫して探索しません。一部のチェーンのログははるかに低い

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- bR < 1.01 で快適。

## Chunk 0589

### English（抽出4行）

> posterior densities than others. When doing posterior predictive checks for these chains speciﬁcally,
> we ﬁnd that the simulated data does not agree with the observations. For reasons we will uncover,
> the chains with the lowest log posterior and highest k also turn out to be the ones with the longest
> run times. Departing from Stan’s defaults, we also plot iterations during the warmup phase. The

### 日本語訳（自動翻訳）

> 他のものよりも事後密度。特にこれらのチェーンの事後予測チェックを行う場合、
> シミュレーションされたデータが観測結果と一致しないことがわかりました。その理由についてはこれから明らかにしていきますが、
> 事後対数が最も低く、k が最も高いチェーンは、最も長いチェーンでもあることがわかります。
> 実行時間。 Stan のデフォルトから離れて、ウォームアップ段階での反復もプロットします。の

### 熟語・専門語

- **posterior predictive**: 事後予測。推定後のモデルが観測データの特徴を再現できるかを見る診断。

### 要約

- 他のものよりも事後密度。

## Chunk 0590

### English（抽出4行）

> plot now clearly indicates that which mode each chain converges to is determined by its initial value,
> suggesting these modes are strongly attractive for the Markov chain. This is an important practical
> log−posterior
> k

### 日本語訳（自動翻訳）

> プロットは、各チェーンがどのモードに収束するかがその初期値によって決定されることを明確に示しています。
> これらのモードがマルコフ連鎖にとって非常に魅力的であることを示唆しています。これは重要な実践事項です
> 対数事後
> k

### 熟語・専門語

- **Markov chain**: マルコフ連鎖。MCMCで事後分布からサンプルを得るための確率過程。

### 要約

- プロットは、各チェーンがどのモードに収束するかがその初期値によって決定されることを明確に示しています。

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
> 0e+00

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- −3e+05 −2e+05 −1e+05 0e+00

## Chunk 0592

### English（抽出4行）

> chain
> Figure 32: Traceplots for our simpliﬁed model of planetary motion. The chains fail to mix, and
> they converge to several diﬀerent local modes, depending on their initial values. The varying log
> posterior suggests some modes are more consistent with the data than others. The shaded area

### 日本語訳（自動翻訳）

> チェーン
> 図 32: 惑星運動の単純化モデルのトレースプロット。チェーンが混ざり合わず、
> これらは、初期値に応じて、いくつかの異なるローカル モードに収束します。変化するログ
> 事後結果は、一部のモードが他のモードよりもデータとの一貫性が高いことを示唆しています。日陰のエリア

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- チェーン 図 32: 惑星運動の単純化モデルのトレースプロット。

## Chunk 0593

### English（抽出4行）

> represents samples during the warmup phase.
> point: the right plot can help us diagnose the problem almost instantaneously, but unfortunately,
> and despite our best eﬀorts, the default plot need not be the right plot.
> It is important to ﬁgure out whether these modes describe a latent phenomenon of interest

### 日本語訳（自動翻訳）

> はウォームアップ段階中のサンプルを表します。
> ポイント: 適切なプロットは問題をほぼ即座に診断するのに役立ちますが、残念ながら、
> 最善の努力にもかかわらず、デフォルトのプロットが正しいプロットである必要はありません。
> これらのモードが関心のある潜在的な現象を記述しているかどうかを把握することが重要です

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- はウォームアップ段階中のサンプルを表します。

## Chunk 0594

### English（抽出4行）

> which we must account for in our analysis or whether they are caused by a mathematical artifact.
> Because we have the luxury of ﬁtting a simpliﬁed model, we can exactly work out what is going on
> and use the gained insight for more elaborate models. Figure 33 plots the likelihood computed via
> a quadrature scheme and conﬁrms the existence of local modes. To understand how these modes

### 日本語訳（自動翻訳）

> 分析の際にそれを考慮する必要があるか、あるいはそれらが数学的アーチファクトによって引き起こされているかどうかを考慮する必要があります。
> 単純化されたモデルを当てはめる余裕があるので、何が起こっているのかを正確に把握できます。
> そして得られた洞察をより精巧なモデルに使用します。図 33 は、次の方法で計算された尤度をプロットしています。
> 直交方式を採用し、ローカルモードの存在を確認します。これらのモードの仕組みを理解するには

### 熟語・専門語

- **likelihood**: 尤度。パラメータが与えられたときデータがどれだけ起こりやすいか。

### 要約

- 分析の際にそれを考慮する必要があるか、あるいはそれらが数学的アーチファクトによって引き起こされているかどうかを考慮する必要があります。

## Chunk 0595

### English（抽出4行）

> arise, we may reason about the log likelihood as a function that penalizes distance between qobs and
> q(k), the positions of the planet simulated for a certain value of k. Indeed,
> log p(qobs|k) = C −1
> 2σ||qobs −q(k)||2

### 日本語訳（自動翻訳）

> 発生すると、qob と qob の間の距離にペナルティを与える関数として対数尤度について推論することができます。
> q(k)、k の特定の値に対してシミュレートされた惑星の位置。確かに、
> log p(qobs|k) = C −1
> 2σ||qobs −q(k)||2

### 熟語・専門語

- **likelihood**: 尤度。パラメータが与えられたときデータがどれだけ起こりやすいか。

### 要約

- 発生すると、qob と qob の間の距離にペナルティを与える関数として対数尤度について推論することができます。

## Chunk 0596

### English（抽出4行）

> 2,
> where C is a constant that does not depend on k. Figure 34 displays the planet’s simulated motion
> given diﬀerent values of k. Recall that k controls the strength of the gravitational interaction: a
> higher value implies a closer and shorter orbit. The assumed value is k = 1. The other values of k

### 日本語訳（自動翻訳）

> 2、
> ここで、C は k に依存しない定数です。図 34 は惑星のシミュレートされた動きを示しています
> k に異なる値を与えた場合。 k が重力相互作用の強さを制御することを思い出してください。
> 値が大きいほど、軌道が近くて短いことを意味します。仮定した値は k = 1 です。k のその他の値は

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- 2、 ここで、C は k に依存しない定数です。

## Chunk 0597

### English（抽出4行）

> fail to generate data consistent with the observed data. For k < 1, the trajectory can drift arbitrarily
> far away from the observed ellipse. But for k > 1, the simulated ellipse must be contained inside
> the observed ellipse, which bounds the distance between qobs and q. Finally, as we change k and
> rotate the ellipse, some of the observed and simulated positions happen to become relatively close,

### 日本語訳（自動翻訳）

> 観測データと一致するデータを生成できません。 k < 1 の場合、軌道は任意にドリフトする可能性があります
> 観測された楕円からはかなり離れています。ただし、k > 1 の場合、シミュレートされた楕円は内側に含まれている必要があります。
> qobs と q の間の距離を区切る観測された楕円。最後に、k と
> 楕円を回転すると、観察された位置とシミュレートされた位置の一部がたまたま比較的近くなります。

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- 観測データと一致するデータを生成できません。

## Chunk 0598

### English（抽出4行）

> which induces local modes that appear as wiggles in the tail of the likelihood. The parameter values
> at the mode do not induce simulations that are in close agreement with the data; but they do better
> than neighboring parameter values, which is enough to create a bump in the likelihood.
> The tail modes are a mathematical artifact of the periodic structure of the data and do not

### 日本語訳（自動翻訳）

> これにより、尤度の末尾に小刻みな動きとして現れる局所モードが誘発されます。パラメータ値
> このモードでは、データと厳密に一致するシミュレーションは引き起こされません。しかし、彼らはもっとうまくやる
> これは、可能性の隆起を生み出すのに十分です。
> テール モードはデータの周期構造の数学的成果物であり、

### 熟語・専門語

- **likelihood**: 尤度。パラメータが与えられたときデータがどれだけ起こりやすいか。

### 要約

- これにより、尤度の末尾に小刻みな動きとして現れる局所モードが誘発されます。

## Chunk 0599

### English（抽出4行）

> characterize a latent phenomenon of interest. Moreover they only contribute negligible probability
> mass.
> Hence, any chain that does not focus on the dominating mode wastes our precious
> −9e+05

### 日本語訳（自動翻訳）

> 潜在的な関心のある現象を特徴づけます。さらに、それらは無視できる確率にしか寄与しません
> 質量。
> したがって、支配的なモードに焦点を当てていないチェーンは、私たちの貴重な資源を無駄にします。
> −9e+05

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- 潜在的な関心のある現象を特徴づけます。

## Chunk 0600

### English（抽出4行）

> −6e+05
> −3e+05
> 0e+00
> 0.0

### 日本語訳（自動翻訳）

> −6e+05
> −3e+05
> 0e+00
> 0.0

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- −6e+05 −3e+05 0e+00 0.0

## Chunk 0601

### English（抽出4行）

> 2.5
> 5.0
> 7.5
> k

### 日本語訳（自動翻訳）

> 2.5
> 5.0
> 7.5
> k

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- 2.5 5.0 7.5 k

## Chunk 0602

### English（抽出4行）

> log likelihood
> Figure 33: Log likelihood across various values of k for our simpliﬁed planetary motion model.
> There is a dominating mode near k = 1, followed by local modes as k increases. These modes are
> due to the cyclical trajectory, which allows the possibility of approximate aliasing.

### 日本語訳（自動翻訳）

> 対数尤度
> 図 33: 単純化された惑星運動モデルのさまざまな k 値にわたる対数尤度。
> k = 1 付近に支配的なモードがあり、k が増加するにつれてローカル モードが続きます。これらのモードは、
> 周期的な軌道のため、近似的なエイリアシングが発生する可能性があります。

### 熟語・専門語

- **likelihood**: 尤度。パラメータが与えられたときデータがどれだけ起こりやすいか。
- **approximate**: 近似。速度や扱いやすさのため、正確な推論・モデルを緩めること。

### 要約

- 対数尤度 図 33: 単純化された惑星運動モデルのさまざまな k 値にわたる対数尤度。

## Chunk 0603

### English（抽出4行）

> −1.0
> −0.5
> 0.0
> 0.5

### 日本語訳（自動翻訳）

> −1.0
> −0.5
> 0.0
> 0.5

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- −1.0 −0.5 0.0 0.5

## Chunk 0604

### English（抽出4行）

> 1.0
> qx
> qy
> k

### 日本語訳（自動翻訳）

> 1.0
> qx
> やあ
> k

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- 1.0 qx やあ k

## Chunk 0605

### English（抽出4行）

> 0.5
> 1.0
> 1.6
> 2.16

### 日本語訳（自動翻訳）

> 0.5
> 1.0
> 1.6
> 2.16

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- 0.5 1.0 1.6 2.16

## Chunk 0606

### English（抽出4行）

> 3.00
> Figure 34: Orbits simulated for various values of k for the planetary motion model. There is no
> strong degeneracy in k, but as this parameter changes, some of the simulated points by chance
> get closer to their observed counterparts, inducing wiggles in the tails of the log likelihood and

### 日本語訳（自動翻訳）

> 3.00
> 図 34: 惑星運動モデルのさまざまな k 値に対してシミュレーションされた軌道。ありません
> k では強い縮退が発生しますが、このパラメータが変化すると、シミュレートされたポイントの一部が偶然に
> 観察された対応物に近づき、対数尤度の尾部の揺れを引き起こし、

### 熟語・専門語

- **likelihood**: 尤度。パラメータが与えられたときデータがどれだけ起こりやすいか。

### 要約

- 3.00 図 34: 惑星運動モデルのさまざまな k 値に対してシミュレーションされた軌道。

## Chunk 0607

### English（抽出4行）

> creating local modes. For example, the 35th observation (solid dot, on the k = 1 orbit) is closer to
> the corresponding position simulated with k = 2.2 (cross on the blue line) than the one obtained
> with k = 1.6 (cross on the green line).
> computational resources. So, what can we do?

### 日本語訳（自動翻訳）

> ローカルモードを作成しています。たとえば、35 番目の観測値 (黒点、k = 1 軌道上) は次のようになります。
> k = 2.2 (青い線の十字) でシミュレートされた対応する位置は、取得されたものよりも高くなります。
> k = 1.6 の場合 (緑色の線で交差)。
> 計算リソース。では、何ができるでしょうか？

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- ローカルモードを作成しています。

## Chunk 0608

### English（抽出4行）

> Building stronger priors. One option is to build a more informative prior to reﬂect our belief
> that a high value of k is implausible; or that any data generating process that suggests the planet
> undergoes several orbits over the observation time is unlikely. When such information is available,
> stronger priors can indeed improve computation.

### 日本語訳（自動翻訳）

> より強力な事前分布を構築します。 1 つのオプションは、私たちの信念を反映する前に、より有益な情報を構築することです。
> k の値が大きいことはありえないこと。または、惑星を示唆するデータ生成プロセス
> 観測時間中に複数の軌道を周回する可能性は低いです。そういった情報が出てきたら、
> より強力な事前分布により、実際に計算が向上します。

### 熟語・専門語

- **ESS**: 有効サンプルサイズ。自己相関を考慮した独立サンプル相当数。

### 要約

- より強力な事前分布を構築します。

## Chunk 0609

### English（抽出4行）

> This is unfortunately not the case here.
> A
> stronger prior would reduce the density at the mode, but the wiggles in the tail of the joint would
> persist. Paradoxically, with more data, these wiggles become stronger: the model is fundamentally

### 日本語訳（自動翻訳）

> 残念ながら、ここではそうではありません。
> あ
> プリアを強くするとモードの密度が下がりますが、ジョイントの尾部の揺れが大きくなります。
> 持続します。逆説的ですが、データが増えるほど、こうした変動はより強くなります。モデルは基本的に

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- 残念ながら、ここではそうではありません。

## Chunk 0610

### English（抽出4行）

> multi-modal. Note also that our current prior, k ∼normal+(0, 1), is already inconsistent with
> the values k takes at the minor modes. In principle we could go a step further and add a hard
> constraint on orbital time or velocity to remove the modes.
> Reweighting draws from each chain. One issue is that the Markov chains fail to transition from one

### 日本語訳（自動翻訳）

> マルチモーダル。現在の事前分布 k 〜normal+(0, 1) がすでに以下と矛盾していることにも注意してください。
> k がマイナーモードで取る値。原則として、さらに一歩進んでハードウェアを追加することもできます。
> 軌道時間または速度を制限してモードを削除します。
> 再重み付けは各チェーンからの描画を行います。問題の 1 つは、マルコフ連鎖が 1 つの連鎖から移行できないことです。

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

> これは、一部のチェーンが確率質量の低い領域をサンプリングすることを意味します。私たち
> スタッキングなどの再重み付けスキームを使用してモンテカルロ推定を修正できます。この戦略
> おそらく妥当なモンテカルロ推定値が得られると思われますが、(i) すべてを包括的に調査するわけではありません。
> モードには 8 チェーンがあるため、スタッキングはローカルでスタックしているチェーンを破棄するものとして扱う必要があります。

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- これは、一部のチェーンが確率質量の低い領域をサンプリングすることを意味します。

## Chunk 0612

### English（抽出4行）

> modes and (ii) we still pay a heavy computational price, as the chains in minor modes take up to
> ∼1000 times longer to run.
> Tuning the starting points. We did not specify the Markov chain’s starting points and instead relied
> on Stan’s defaults, which sample the initial point from a uniform(−2, 2) over the unconstrained

### 日本語訳（自動翻訳）

> (ii) マイナー モードのチェーンには最大で
> 実行時間が約 1000 倍長くなります。
> 開始点を調整します。マルコフ連鎖の開始点を指定せず、代わりに信頼しました。
> Stan のデフォルトでは、制約のない上で均一(−2, 2) から初期点をサンプリングします。

### 熟語・専門語

- **Markov chain**: マルコフ連鎖。MCMCで事後分布からサンプルを得るための確率過程。

### 要約

- (ii) マイナー モードのチェーンには最大で 実行時間が約 1000 倍長くなります。

## Chunk 0613

### English（抽出4行）

> space, that is, the starting points are drawn from log k(0) ∼uniform(−2, 2). This default, designed
> for unconstrained parameters on the unit scale, indulges values of k which are widely inconsistent
> with our prior and our domain expertise. In a non-asymptotic regime, the Markov chain does not
> always “forget” its starting point, and it is unlikely to do so here even if we run the chain for many

### 日本語訳（自動翻訳）

> 空間、つまり開始点は log k(0) 〜uniform(−2, 2) から引かれます。このデフォルト、設計された
> 単位スケール上の制約のないパラメータの場合、大きく矛盾した k の値が許容されます。
> 私たちのこれまでの専門知識とその分野の専門知識を活用して。非漸近領域では、マルコフ連鎖は
> 常にその出発点を「忘れる」ので、たとえ何回もチェーンを実行したとしても、ここでそうする可能性は低いです。

### 熟語・専門語

- **Markov chain**: マルコフ連鎖。MCMCで事後分布からサンプルを得るための確率過程。

### 要約

- 空間、つまり開始点は log k(0) 〜uniform(−2, 2) から引かれます。

## Chunk 0614

### English（抽出4行）

> many more iterations. We can therefore not ignore this tuning parameter of our algorithm. An
> alternative to the default is to sample k(0) from our prior, thereby imposing that the chains start in a
> range of values deemed reasonable. In this setup, the chains converge quickly and our computation
> focuses on the relevant region.

### 日本語訳（自動翻訳）

> さらに多くの繰り返し。したがって、アルゴリズムのこの調整パラメータを無視することはできません。アン
> デフォルトの代替案は、以前のデータから k(0) をサンプリングすることです。これにより、チェーンが
> 妥当と考えられる値の範囲。この設定では、チェーンはすぐに収束し、計算は
> 関連する地域に焦点を当てます。

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- さらに多くの繰り返し。

## Chunk 0615

### English（抽出4行）

> Whether with stacking, tuned starting points, or perhaps another mean, we need to give MCMC
> a helping hand to avoid local modes. In general, ignoring non-converging chains is poor practice,
> so we want to highlight how the here presented process diﬀers from that. First, we examine all
> the chains, using posterior predictive checks, and work out exactly how the local modes arise.

### 日本語訳（自動翻訳）

> スタッキング、調整された開始点、またはおそらく別の手段のいずれを使用する場合でも、MCMC を提供する必要があります。
> ローカルモードを回避するのに役立ちます。一般に、非収束チェーンを無視するのは悪い習慣です。
> そこで、ここで紹介するプロセスがそれとどのように異なるのかを強調したいと思います。まず、すべてを調べます
> 事後予測チェックを使用してチェーンを解析し、ローカル モードがどのように発生するかを正確に計算します。

### 熟語・専門語

- **posterior predictive**: 事後予測。推定後のモデルが観測データの特徴を再現できるかを見る診断。
- **ESS**: 有効サンプルサイズ。自己相関を考慮した独立サンプル相当数。

### 要約

- スタッキング、調整された開始点、またはおそらく別の手段のいずれを使用する場合でも、MCMC を提供する必要があります。

## Chunk 0616

### English（抽出4行）

> We decisively demonstrate that they do not describe data generating processes of interest, nor do
> they contribute more than a negligible amount of probability mass. Only then do we redirect our
> computational resources to focus on the mode around which all the probability mass concentrates.
> 11.3.

### 日本語訳（自動翻訳）

> 我々は、それらが関心のあるデータ生成プロセスを記述しておらず、また記述していないことを決定的に証明します。
> それらは確率質量の無視できる量以上に寄与します。その場合にのみ、リダイレクトします。
> 計算リソースを使用して、すべての確率質量が集中するモードに焦点を当てます。
> 11.3.

### 熟語・専門語

- **ESS**: 有効サンプルサイズ。自己相関を考慮した独立サンプル相当数。

### 要約

- 我々は、それらが関心のあるデータ生成プロセスを記述しておらず、また記述していないことを決定的に証明します。

## Chunk 0617

### English（抽出4行）

> Bad Markov chain, slow Markov chain?
> Recall that the chains that yielded the lowest log posteriors were also the ones that were the
> slowest—an instance of the folk theorem of statistical computing (see Section 5.1). We can in fact
> show that Hamilton’s equations become more diﬃcult to solve as k increases. The intuition is the

### 日本語訳（自動翻訳）

> 悪いマルコフ連鎖、遅いマルコフ連鎖?
> 最小の事後対数を生成したチェーンは、
> 最も遅い - 統計計算の民間定理の例 (セクション 5.1 を参照)。実際にできるのは
> k が増加するにつれてハミルトン方程式を解くのが難しくなることを示しています。直感というのは、

### 熟語・専門語

- **Markov chain**: マルコフ連鎖。MCMCで事後分布からサンプルを得るための確率過程。

### 要約

- 悪いマルコフ連鎖、遅いマルコフ連鎖? 最小の事後対数を生成したチェーンは、 最も遅い - 統計計算の民間定理の例 (セクション 5.1 を参照)。

## Chunk 0618

### English（抽出4行）

> following: if the gravitational interaction is strong, then the planet moves at a much faster rate.
> From a numerical perspective, this means each time step, dt, incurs a greater change in q(t) and
> the integrator’s step size must accordingly be adjusted.
> There is wisdom is this anecdote: an easy deterministic problem can become diﬃcult in a

### 日本語訳（自動翻訳）

> 以下: 重力相互作用が強い場合、惑星ははるかに速い速度で移動します。
> 数値的な観点から見ると、これは、時間ステップ dt ごとに q(t) に大きな変化が生じることを意味します。
> それに応じて積分器のステップ サイズを調整する必要があります。
> この逸話には知恵があります。簡単な決定論的な問題も、次のような状況では難しくなる可能性があります。

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- 以下: 重力相互作用が強い場合、惑星ははるかに速い速度で移動します。

## Chunk 0619

### English（抽出4行）

> Bayesian analysis. Indeed Bayesian inference requires us to solve the problem across a range
> of parameter values, which means we must sometimes confront unsuspected versions of the said
> problem. In our experience, notably with diﬀerential equation based models in pharmacology and
> epidemiology, we sometime require a more computationally expensive stiﬀsolver to tackle diﬃcult

### 日本語訳（自動翻訳）

> ベイジアン分析。実際、ベイズ推論では、範囲全体にわたって問題を解決する必要があります。
> パラメータ値の予期せぬバージョンに時々直面しなければならないことを意味します。
> 問題。私たちの経験では、特に薬理学や薬学における微分方程式ベースのモデルの場合、
> 疫学では、難しい問題に取り組むために、より計算コストの高いスティフソルバーが必要になることがあります。

### 熟語・専門語

- **Bayesian inference**: ベイズ推論。事前分布と尤度から事後分布を計算する中核処理。

### 要約

- ベイジアン分析。

## Chunk 0620

### English（抽出4行）

> ODEs generated during the warmup phase.
> Other times slow computation can alert us that our inference is allowing for absurd parameter
> values and that we need either better priors or more reasonable initial points.
> Unfortunately this goes against the “fail fast” principle outlined in Section 3.4. Our current

### 日本語訳（自動翻訳）

> ウォームアップ段階で生成される ODE。
> また、計算が遅いために、推論が不合理なパラメータを許容していることを警告する場合もあります。
> そして、より良い事前分布か、より合理的な初期点が必要であることを示しています。
> 残念ながら、これはセクション 3.4 で説明した「フェイルファスト」原則に反します。私たちの現在

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- ウォームアップ段階で生成される ODE。

## Chunk 0621

### English（抽出4行）

> tools tend to be much slower when the ﬁt is bad, hence an important research topic in Bayesian
> computational workﬂow is to ﬂag potential problems quickly to avoid wasting too much time on
> dead ends.
> 11.4.

### 日本語訳（自動翻訳）

> 適合度が悪い場合、ツールは非常に遅くなる傾向があるため、ベイジアンにおける重要な研究テーマとなります。
> 計算ワークフローは、潜在的な問題にすぐにフラグを立てて、時間の浪費を避けることです。
> 行き止まり。
> 11.4.

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- 適合度が悪い場合、ツールは非常に遅くなる傾向があるため、ベイジアンにおける重要な研究テーマとなります。

## Chunk 0622

### English（抽出4行）

> Building up the model
> Starting from the simpliﬁed model, we now gradually build our way back to the original model. This
> turns out to be not quite straightforward, but we can put what we have learned from the simpliﬁed
> model to good use. Most inference problems we encounter across the models we ﬁt can be traced

### 日本語訳（自動翻訳）

> モデルの構築
> 簡略化されたモデルから始めて、徐々に元のモデルに戻る方法を構築していきます。これ
> 完全に単純ではないことがわかりましたが、ここから学んだことを単純化して当てはめることができます。
> 上手に使えるモデル。当てはめたモデル全体で遭遇するほとんどの推論問題は追跡可能です

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- モデルの構築 簡略化されたモデルから始めて、徐々に元のモデルに戻る方法を構築していきます。

## Chunk 0623

### English（抽出4行）

> back to the interaction between the likelihood and the cyclical observations—an elementary notion,
> once grasped, but which would have been diﬃcult to discover in a less simple setting than the one
> we used.
> Here is an example. In the complete model, we estimate the position of the star, q∗, and ﬁnd that

### 日本語訳（自動翻訳）

> 尤度と周期的観測の間の相互作用、つまり初歩的な概念に戻ります。
> 一度は把握できましたが、以前の環境よりも単純ではない環境では発見するのは困難であったでしょう。
> 私たちが使った。
> ここに一例を示します。完全なモデルでは、星の位置 q∗ を推定し、次のことがわかります。

### 熟語・専門語

- **likelihood**: 尤度。パラメータが与えられたときデータがどれだけ起こりやすいか。
- **ESS**: 有効サンプルサイズ。自己相関を考慮した独立サンプル相当数。

### 要約

- 尤度と周期的観測の間の相互作用、つまり初歩的な概念に戻ります。

## Chunk 0624

### English（抽出4行）

> the chains converge to many diﬀerent values, yielding simulations which, depending on the chain,
> agree or disagree with the observations. There is however, based on the traceplots, no obvious
> connection between the starting points and the neighborhoods of convergence. It is diﬃcult to
> examine this type of connections because the model has now 7 parameters, some with strong

### 日本語訳（自動翻訳）

> チェーンは多くの異なる値に収束し、チェーンに応じて次のようなシミュレーションが生成されます。
> 観察に同意するか反対するか。ただし、トレースプロットに基づくと、明確な点はありません。
> 開始点と収束近傍の間の接続。難しいです
> モデルには現在 7 つのパラメーターがあり、その中には強力なパラメーターがあるため、このタイプの接続を調べてください。

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- チェーンは多くの異なる値に収束し、チェーンに応じて次のようなシミュレーションが生成されます。

## Chunk 0625

### English（抽出4行）

> posterior correlations. Fortunately, we can reason about the physics of the problem and realize that
> tweaking the star’s position, q∗, and implicitly, r, the star-planet distance, is not unlike modifying
> k. Recall that
> dp

### 日本語訳（自動翻訳）

> 事後相関。幸いなことに、私たちは問題の物理学を推論して次のことを理解できます。
> 星の位置 q∗ を微調整すること、そして暗黙のうちに星と惑星の距離 r を微調整することは、
> k.思い出してください
> DP

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- 事後相関。

## Chunk 0626

### English（抽出4行）

> dt = −k
> r3(q −q∗),
> whence both k and r control the gravitational interaction.
> We cannot do a quadrature across all 7 parameters of our model. Instead, we look at the

### 日本語訳（自動翻訳）

> dt = −k
> r3(q −q∗),
> したがって、k と r の両方が重力相互作用を制御します。
> モデルの 7 つのパラメーターすべてにわたって求積を行うことはできません。代わりに、

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- dt = −k r3(q −q∗), したがって、k と r の両方が重力相互作用を制御します。

## Chunk 0627

### English（抽出4行）

> conditional likelihood, wherein we keep all parameters (k, q0, and p0) ﬁxed, except for q∗. In
> a sense, this amounts to investigating another simpliﬁcation of our model. Figure 35 shows the
> suspected modes, thereby supporting our conjecture. At this point, with some level of conﬁdence,
> we construct starting points to guide our Markov chains towards the dominating mode and obtain

### 日本語訳（自動翻訳）

> 条件付き尤度では、q∗ を除くすべてのパラメーター (k、q0、および p0) を固定します。で
> ある意味、これはモデルの別の単純化を調査することに相当します。図 35 に、
> 疑わしいモードであるため、私たちの推測が裏付けられます。この時点で、ある程度の自信を持って、
> マルコフ連鎖を支配モードに導き、次の結果を得るために開始点を構築します。

### 熟語・専門語

- **likelihood**: 尤度。パラメータが与えられたときデータがどれだけ起こりやすいか。
- **Markov chain**: マルコフ連鎖。MCMCで事後分布からサンプルを得るための確率過程。

### 要約

- 条件付き尤度では、q∗ を除くすべてのパラメーター (k、q0、および p0) を固定します。

## Chunk 0628

### English（抽出4行）

> a good ﬁt of the complete model.
> 11.5.
> General lessons from the planetary motion example
> When we fail to ﬁt a model, examining a simpliﬁed model can help us understand the challenges

### 日本語訳（自動翻訳）

> 完全なモデルの適合性が良好です。
> 11.5。
> 惑星運動の例から得られる一般的な教訓
> モデルの適合に失敗した場合、単純化したモデルを調べると課題を理解するのに役立ちます。

### 熟語・専門語

- **ESS**: 有効サンプルサイズ。自己相関を考慮した独立サンプル相当数。

### 要約

- 完全なモデルの適合性が良好です。

## Chunk 0629

### English（抽出4行）

> that frustrate our inference algorithm. In practice it is diﬃcult to ﬁnd a simpliﬁcation which is
> −4e+05
> −2e+05
> 0e+00

### 日本語訳（自動翻訳）

> それは私たちの推論アルゴリズムを妨げます。実際には、次のような単純化を見つけるのは困難です。
> −4e+05
> −2e+05
> 0e+00

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- それは私たちの推論アルゴリズムを妨げます。

## Chunk 0630

### English（抽出4行）

> −0.5
> 0.0
> 0.5
> q∗

### 日本語訳（自動翻訳）

> −0.5
> 0.0
> 0.5
> q∗

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- −0.5 0.0 0.5 q∗

## Chunk 0631

### English（抽出4行）

> x
> Conditional log likelihood
> −0.3
> 0.0

### 日本語訳（自動翻訳）

> ×
> 条件付き対数尤度
> −0.3
> 0.0

### 熟語・専門語

- **likelihood**: 尤度。パラメータが与えられたときデータがどれだけ起こりやすいか。

### 要約

- × 条件付き対数尤度 −0.3 0.0

## Chunk 0632

### English（抽出4行）

> 0.3
> −0.5
> 0.0
> 0.5

### 日本語訳（自動翻訳）

> 0.3
> −0.5
> 0.0
> 0.5

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- 0.3 −0.5 0.0 0.5

## Chunk 0633

### English（抽出4行）

> q∗
> x
> q∗
> y

### 日本語訳（自動翻訳）

> q∗
> ×
> q∗
> y

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- q∗ × q∗ y

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
> 0e+00

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- −6e+05 −4e+05 −2e+05 0e+00

## Chunk 0635

### English（抽出4行）

> log likelihood
> Figure 35: For the planetary motion example, log conditional likelihood when varying the star’s
> position, q∗. Left: All parameters are kept ﬁxed, except for the x-coordinate of q∗. Right: This time
> both coordinates of q∗are allowed to vary. The quadrature computation allows us to expose the

### 日本語訳（自動翻訳）

> 対数尤度
> 図 35: 惑星の運動の例では、星の動きを変化させたときの条件付き尤度をログに記録します。
> 位置、q*。左: q∗ の x 座標を除いて、すべてのパラメーターは固定されたままです。右：今回は
> q∗ の両方の座標は変更できます。直角位相の計算により、

### 熟語・専門語

- **likelihood**: 尤度。パラメータが与えられたときデータがどれだけ起こりやすいか。

### 要約

- 対数尤度 図 35: 惑星の運動の例では、星の動きを変化させたときの条件付き尤度をログに記録します。

## Chunk 0636

### English（抽出4行）

> multimodality of the problem.
> manageable and still exhibits the pathology we wish to understand. Reasoning about the topology
> surrounding our model, as alluded to in section 7.4, can help us in this process. A straightforward
> way of simplifying is to ﬁx some of the model parameters.

### 日本語訳（自動翻訳）

> 問題の多面性。
> 管理可能であり、依然として理解したい病理を示しています。トポロジに関する推論
> セクション 7.4 で触れたように、モデルを囲むものは、このプロセスに役立ちます。率直な
> 簡素化する方法は、モデルパラメータの一部を修正することです。

### 熟語・専門語

- **multimodality**: 多峰性。事後分布に複数の山があり、MCMCが混合しにくい状態。
- **ESS**: 有効サンプルサイズ。自己相関を考慮した独立サンプル相当数。

### 要約

- 問題の多面性。

## Chunk 0637

### English（抽出4行）

> In the planetary motion example, we are confronted with a multi-modal posterior distribution.
> This geometry prevents our chains from cohesively exploring the parameter space and leads to
> biased Monte Carlo estimates. It is important to understand how these local modes arise and what
> their contribution to the posterior probability mass might be. We do so using posterior predictive

### 日本語訳（自動翻訳）

> 惑星運動の例では、マルチモーダル事後分布に直面します。
> このジオメトリにより、チェーンがパラメーター空間を一貫して探索することが妨げられ、次のような問題が発生します。
> 偏ったモンテカルロ推定。これらのローカル モードがどのように発生し、何が起こるのかを理解することが重要です。
> 事後確率質量への寄与は次のとおりである可能性があります。事後予測を使用してこれを行います

### 熟語・専門語

- **posterior predictive**: 事後予測。推定後のモデルが観測データの特徴を再現できるかを見る診断。
- **posterior distribution**: 事後分布。データ観測後の未知量の不確実性を表す分布。

### 要約

- 惑星運動の例では、マルチモーダル事後分布に直面します。

## Chunk 0638

### English（抽出4行）

> checks. It is not uncommon for minor modes, with negligible probability mass, to “trap” a Markov
> chain. The possibility of such ill-ﬁtting modes implies we should always run multiple chains,
> perhaps more than our current default of 4.
> This case study also raises the question of what role starting points may play. Ideally a Markov

### 日本語訳（自動翻訳）

> 小切手。確率質量が無視できるマイナーモードがマルコフを「トラップ」することは珍しいことではありません。
> チェーン。このような不適切なモードの可能性は、常に複数のチェーンを実行する必要があることを意味します。
> おそらく現在のデフォルトの 4 よりも多いでしょう。
> このケーススタディは、出発点がどのような役割を果たすことができるかという疑問も提起します。理想はマルコフ

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- 小切手。

## Chunk 0639

### English（抽出4行）

> chain forgets its initial value but in a non-asymptotic regime this may not be the case. This is not a
> widely discussed topic but nevertheless one of central importance for practitioners and thence for
> Bayesian workﬂow. Just as there is no universal default prior, there is no universal default initial
> point. Modelers often need to depart from defaults to insure a numerically stable evaluation of

### 日本語訳（自動翻訳）

> チェーンは初期値を忘れますが、非漸近領域ではそうでない可能性があります。これは、
> 広く議論されているトピックですが、それでもなお、実践者にとって、ひいては社会にとって最も重要なテーマの 1 つです。
> ベイジアンワークフロー。普遍的な初期値が存在しないのと同様に、普遍的なデフォルトの初期値も存在しません。
> ポイント。モデラーは多くの場合、数値的に安定した評価を保証するためにデフォルトから逸脱する必要があります。

### 熟語・専門語

- **ESS**: 有効サンプルサイズ。自己相関を考慮した独立サンプル相当数。

### 要約

- チェーンは初期値を忘れますが、非漸近領域ではそうでない可能性があります。

## Chunk 0640

### English（抽出4行）

> the joint density and improve MCMC computation. At the same time we want dispersed initial
> points in order to have reliable convergence diagnostics and to potentially explore all the relevant
> modes. Like for other tuning parameters of an inference algorithm, picking starting points can be
> an iterative process, with adjustments made after a ﬁrst attempt at ﬁtting the model.

### 日本語訳（自動翻訳）

> ジョイント密度を高め、MCMC 計算を改善します。同時に初期値を分散させたい
> 信頼性の高い収束診断を行い、関連するすべての点を潜在的に調査するためのポイント
> モード。推論アルゴリズムの他の調整パラメーターと同様に、開始点の選択は次のとおりです。
> モデルのフィッティングを最初に試みた後に調整が行われる反復プロセス。

### 熟語・専門語

- **ESS**: 有効サンプルサイズ。自己相関を考慮した独立サンプル相当数。

### 要約

- ジョイント密度を高め、MCMC 計算を改善します。

## Chunk 0641

### English（抽出4行）

> We do not advocate mindlessly discarding misbehaving chains. It is important to analyze where
> this poor behavior comes from, and whether it hints at serious ﬂaws in our model and in our
> inference. Our choice to adjust the initial estimates is based on: (a) the realization that the defaults
> are widely inconsistent with our expertise and (b) the understanding that the local modes do not

### 日本語訳（自動翻訳）

> 私たちは、不正行為を行っているチェーンをむやみに破棄することを推奨しません。どこにあるのかを分析することが重要です
> この不適切な動作はどこから来ているのか、またそれがモデルやシステムの重大な欠陥を示唆しているのかどうか
> 推論。初期推定値を調整するという私たちの選択は、次のことに基づいています。 (a) デフォルト値であるという認識
> 私たちの専門知識と大きく矛盾しており、(b) ローカルモードはそうではないという理解

### 熟語・専門語

- **ESS**: 有効サンプルサイズ。自己相関を考慮した独立サンプル相当数。

### 要約

- 私たちは、不正行為を行っているチェーンをむやみに破棄することを推奨しません。

## Chunk 0642

### English（抽出4行）

> describe a latent phenomenon of interest, as shown by our detailed analysis of how cyclical data
> interacts with a normal likelihood.
> 12.
> Discussion

### 日本語訳（自動翻訳）

> データの周期性に関する詳細な分析によって示されるように、関心のある潜在的な現象を説明します。
> 通常の確率と相互作用します。
> 12.
> ディスカッション

### 熟語・専門語

- **likelihood**: 尤度。パラメータが与えられたときデータがどれだけ起こりやすいか。

### 要約

- データの周期性に関する詳細な分析によって示されるように、関心のある潜在的な現象を説明します。

## Chunk 0643

### English（抽出4行）

> 12.1.
> Different perspectives on statistical modeling and prediction
> Consider three diﬀerent ways to think about modeling and prediction:
> • Traditional statistical perspective. In textbooks, statistical inference is typically set up as a

### 日本語訳（自動翻訳）

> 12.1.
> 統計モデリングと予測に関するさまざまな視点
> モデリングと予測について考えるための 3 つの異なる方法を検討してください。
> • 従来の統計的観点。教科書では、統計的推論は通常、

### 熟語・専門語

- **prediction**: 予測。未知/将来/除外データに対する分布や点推定。

### 要約

- 12.1. 統計モデリングと予測に関するさまざまな視点 モデリングと予測について考えるための 3 つの異なる方法を検討してください。

## Chunk 0644

### English（抽出4行）

> problem in which a model has been chosen ahead of time, and in the Bayesian context the
> goal is to accurately summarize the posterior distribution. Computation is supposed to be
> done as long as necessary to reach approximate convergence.
> • Machine learning perspective. In machine learning, the usual goal is prediction, not pa-

### 日本語訳（自動翻訳）

> モデルが事前に選択されている問題、およびベイジアンのコンテキストでは、
> 目標は、事後分布を正確に要約することです。計算は次のようになっているはずです
> ほぼ収束するまでに必要なだけ実行されます。
> • 機械学習の観点。機械学習では、通常の目標は予測ではなく、予測です。

### 熟語・専門語

- **posterior distribution**: 事後分布。データ観測後の未知量の不確実性を表す分布。
- **ESS**: 有効サンプルサイズ。自己相関を考慮した独立サンプル相当数。
- **approximate**: 近似。速度や扱いやすさのため、正確な推論・モデルを緩めること。
- **prediction**: 予測。未知/将来/除外データに対する分布や点推定。

### 要約

- モデルが事前に選択されている問題、およびベイジアンのコンテキストでは、 目標は、事後分布を正確に要約することです。

## Chunk 0645

### English（抽出4行）

> rameter estimation, and computation can stop when cross validation prediction accuracy has
> plateaued.
> • Model exploration perspective. In applied statistical work, much of our modeling eﬀort is
> spent in exploration, trying out a series of models, many of which will have terrible ﬁt to

### 日本語訳（自動翻訳）

> パラメータ推定、相互検証の予測精度が低下すると計算が停止する可能性があります。
> 頭打ちになった。
> • モデル探索の観点。応用統計作業では、モデリング作業の多くは
> 探索に費やし、一連のモデルを試してみましたが、その多くは適合性がひどいものでした。

### 熟語・専門語

- **cross validation**: 交差検証。汎化性能を推定するためにデータを分割/近似除外する評価法。
- **validation**: 検証。モデルが目的・データ・外部知識に照らして妥当かを確認すること。
- **prediction**: 予測。未知/将来/除外データに対する分布や点推定。

### 要約

- パラメータ推定、相互検証の予測精度が低下すると計算が停止する可能性があります。

## Chunk 0646

### English（抽出4行）

> data, poor predictive performance, and slow convergence (see also Section 5.1).
> These three scenarios imply diﬀerent inferential goals. In a traditional statistical modeling
> problem, it can make sense to run computation for a long time, using approximations only when
> absolutely necessary. Another way of saying this is that in traditional statistics, the approximation

### 日本語訳（自動翻訳）

> データ、予測パフォーマンスの低下、収束の遅さ (セクション 5.1 も参照)。
> これら 3 つのシナリオは、異なる推論目標を暗示しています。従来の統計モデリングでは
> 問題は、次の場合にのみ近似を使用して、長時間計算を実行することが合理的になる場合があります。
> 絶対に必要です。これを別の言い方で言えば、従来の統計では、近似は

### 熟語・専門語

- **ESS**: 有効サンプルサイズ。自己相関を考慮した独立サンプル相当数。

### 要約

- データ、予測パフォーマンスの低下、収束の遅さ (セクション 5.1 も参照)。

## Chunk 0647

### English（抽出4行）

> might be in the choice of model rather than in the computation. In machine learning, we want to
> pick an algorithm that trades oﬀpredictive accuracy, generalizability, and scalability, so as to make
> use of as much data as possible within a ﬁxed computational budget and predictive goal. In model
> exploration, we want to cycle through many models, which makes approximations attractive. But

### 日本語訳（自動翻訳）

> 計算ではなくモデルの選択にある可能性があります。機械学習において私たちが望んでいるのは、
> 予測精度、一般化性、拡張性を犠牲にするアルゴリズムを選択してください。
> 固定された計算予算と予測目標の範囲内でできるだけ多くのデータを使用します。モデル内
> 探索では、多くのモデルを循環させたいので、近似が魅力的になります。しかし、

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- 計算ではなくモデルの選択にある可能性があります。

## Chunk 0648

### English（抽出4行）

> there is a caveat here: if we are to eﬃciently and accurately explore the model space rather than the
> algorithm space, we require any approximation to be suﬃciently faithful as to reproduce the salient
> features of the posterior.
> The distinction here is not about inference vs. prediction, or exploratory vs. conﬁrmatory

### 日本語訳（自動翻訳）

> ここで注意点があります。つまり、モデル空間ではなくモデル空間を効率的かつ正確に探索する場合です。
> アルゴリズム空間では、顕著な結果を再現するために、近似が十分に忠実であることが必要です。
> 後部の特徴。
> ここでの区別は、推論と予測、あるいは探索的と確認的というものではありません。

### 熟語・専門語

- **prediction**: 予測。未知/将来/除外データに対する分布や点推定。

### 要約

- ここで注意点があります。

## Chunk 0649

### English（抽出4行）

> analysis. Indeed all parameters in inference can be viewed as some quantities to predict, and all of
> our modeling can be viewed as having exploratory goals (Gelman, 2003). Rather, the distinction is
> how much we trust a given model and allow the computation to approximate.
> As the examples in Sections 10 and 11 illustrate, problems with a statistical model in hindsight

### 日本語訳（自動翻訳）

> 分析。実際、推論におけるすべてのパラメータは、予測すべき量として見ることができ、
> 私たちのモデリングは探索的な目標を持っているとみなすことができます (Gelman、2003)。むしろその違いは、
> 特定のモデルをどの程度信頼し、計算による近似を許容するか。
> セクション 10 と 11 の例が示すように、後になって考えると統計モデルの問題点は次のとおりです。

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

> 多くの場合、明白に思えますが、それらを識別し、明白さを理解するためのワークフローが必要でした。
> これらの例のもう 1 つの重要な特徴は、応用問題でよく起こることです。
> モデリングにおける特定の課題は、手元のデータのコンテキストで発生します。データが異なっていたら、
> これらの特定の問題には遭遇しなかったかもしれませんが、他の問題が発生した可能性は十分にあります。これ

### 熟語・専門語

- **ESS**: 有効サンプルサイズ。自己相関を考慮した独立サンプル相当数。

### 要約

- 多くの場合、明白に思えますが、それらを識別し、明白さを理解するためのワークフローが必要でした。

## Chunk 0651

### English（抽出4行）

> is one reason that subﬁelds in applied statistics advance from application to application, as new
> wrinkles become apparent in existing models. A central motivation of this paper is to make more
> transparent the steps by which we can uncover and then resolve these modeling problems.
> 12.2.

### 日本語訳（自動翻訳）

> これが、応用統計のサブフィールドが新しいものとしてアプリケーションからアプリケーションへと進歩する理由の 1 つです。
> 既存モデルではシワが目立ちます。この文書の主な動機は、さらに多くのことを行うことです。
> これらのモデリングの問題を明らかにし、解決するための手順が透明になります。
> 12.2.

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- これが、応用統計のサブフィールドが新しいものとしてアプリケーションからアプリケーションへと進歩する理由の 1 つです。

## Chunk 0652

### English（抽出4行）

> Justification of iterative model building
> We view the process of model navigation as the next transformative step in data science. The ﬁrst
> big step of data science, up to 1900 or so, was data summarization, centering on the gathering of
> relevant data and summarizing through averages, correlations, least-squares ﬁts, and the like. The

### 日本語訳（自動翻訳）

> 反復モデル構築の正当性
> 私たちは、モデル ナビゲーションのプロセスをデータ サイエンスの次の変革的なステップとみなしています。最初の
> 1900 年頃までのデータ サイエンスの大きなステップは、データの収集を中心としたデータの要約でした。
> 関連データを収集し、平均、相関、最小二乗適合などを通じて要約します。の

### 熟語・専門語

- **ESS**: 有効サンプルサイズ。自己相関を考慮した独立サンプル相当数。
- **model building**: モデル構築。仮定・データ構造・prior・likelihoodを組み合わせる工程。

### 要約

- 反復モデル構築の正当性 私たちは、モデル ナビゲーションのプロセスをデータ サイエンスの次の変革的なステップとみなしています。

## Chunk 0653

### English（抽出4行）

> next big step, beginning with Gauss and Laplace and continuing to the present day, was modeling:
> the realization that a probabilistic model with scientiﬁc content could greatly enhance the value
> from any given dataset, and also make it more feasible to combine diﬀerent sources of data. We
> are currently in the midst of another big step, computation: with modern Bayesian and machine

### 日本語訳（自動翻訳）

> ガウスとラプラスから始まり現在に至るまでの次の大きなステップは、モデリングでした。
> 科学的内容を含む確率モデルが価値を大幅に高める可能性があるという認識
> 特定のデータセットからのデータを取得できるほか、さまざまなデータ ソースを組み合わせることがより実現可能になります。私たち
> 現在、現代のベイジアンと機械による計算という、もう一つの大きなステップの真っ最中です。

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- ガウスとラプラスから始まり現在に至るまでの次の大きなステップは、モデリングでした。

## Chunk 0654

### English（抽出4行）

> learning methods, increases in algorithmic and computational eﬃciency have eﬀected a qualitative
> improvement in our ability to make predictions and causal inferences. We would like to move
> beyond good practice and workﬂow in particular case studies, to a formulation of the process of
> model navigation, “facilitating the exploration of model space” (Devezer et al., 2019).

### 日本語訳（自動翻訳）

> 学習方法、アルゴリズム効率と計算効率の向上により、定性的なパフォーマンスが向上しました。
> 予測と因果推論を行う能力の向上。引っ越しをしたいのですが
> 特定のケーススタディにおけるグッドプラクティスやワークフローを超えて、プロセスの定式化まで
> モデル ナビゲーション、「モデル空間の探索を容易にする」(Devezer et al.、2019)。

### 熟語・専門語

- **ESS**: 有効サンプルサイズ。自己相関を考慮した独立サンプル相当数。
- **prediction**: 予測。未知/将来/除外データに対する分布や点推定。

### 要約

- 学習方法、アルゴリズム効率と計算効率の向上により、定性的なパフォーマンスが向上しました。

## Chunk 0655

### English（抽出4行）

> In the ideal world we would build one perfect model and solve the math. In the real world we
> need to take into account the limitations of humans and computers, and this should be included in
> models of science and models of statistics (Navarro, 2019, Devezer et al., 2020).
> From a human perspective, our limited cognitive capabilities make it easier to learn gradually.

### 日本語訳（自動翻訳）

> 理想的な世界では、1 つの完璧なモデルを構築し、数学を解くことができます。現実の世界では私たちは
> 人間とコンピューターの限界を考慮する必要があり、これを含める必要があります。
> 科学のモデルと統計のモデル (Navarro、2019、Devezer et al.、2020)。
> 人間の観点から見ると、私たちの認知能力は限られているため、徐々に学習することが容易になります。

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- 理想的な世界では、1 つの完璧なモデルを構築し、数学を解くことができます。

## Chunk 0656

### English（抽出4行）

> Iterative model building starting from a simple model is gradual learning and helps us better
> understand the modeled phenomenon. Furthermore, building a rich model takes eﬀort, and it
> can be eﬃcient in human time to start from a simpler model and stop when the model seems to
> be suﬃciently good. We gave an example in Section 10. One goal of workﬂow is to make the

### 日本語訳（自動翻訳）

> 単純なモデルから始める反復的なモデル構築は段階的に学習し、より良いものにします。
> モデル化された現象を理解します。さらに、リッチなモデルを構築するには時間がかかります。
> より単純なモデルから開始し、モデルが適切であると思われる時点で停止する方が人間の時間で効率的です。
> 十分に良くなる。セクション 10 で例を示しました。ワークフローの 1 つの目標は、

### 熟語・専門語

- **model building**: モデル構築。仮定・データ構造・prior・likelihoodを組み合わせる工程。

### 要約

- 単純なモデルから始める反復的なモデル構築は段階的に学習し、より良いものにします。

## Chunk 0657

### English（抽出4行）

> process easier for humans even in the idealized setting where exact computation can be performed
> automatically.
> Iterating over a set of models is also useful from a computational standpoint. Given a proper
> posterior, computation in Bayesian inference is theoretically solved. In practice we must contend

### 日本語訳（自動翻訳）

> 正確な計算が実行できる理想的な環境でも、人間にとってより簡単なプロセス
> 自動的に。
> 一連のモデルを反復処理することは、計算の観点からも役立ちます。適切な
> 事後的には、ベイズ推論における計算は理論的に解決されます。実際には私たちは争わなければならない

### 熟語・専門語

- **Bayesian inference**: ベイズ推論。事前分布と尤度から事後分布を計算する中核処理。
- **ESS**: 有効サンプルサイズ。自己相関を考慮した独立サンプル相当数。

### 要約

- 正確な計算が実行できる理想的な環境でも、人間にとってより簡単なプロセス 自動的に。

## Chunk 0658

### English（抽出4行）

> with ﬁnite computational resources. An algorithm for which asymptotic guarantees exist can fail
> when run for a ﬁnite time. There is no fully automated computation that yields perfect results,
> at least not across the vast range of models practitioners care about. Another goal of workﬂow
> is to avoid some computational problems and be able to eﬃciently diagnose the remaining ones.

### 日本語訳（自動翻訳）

> 有限の計算リソースを使用して。漸近的保証が存在するアルゴリズムは失敗する可能性がある
> 有限時間実行する場合。完璧な結果を生み出す完全に自動化された計算は存在しません。
> 少なくとも、実務者が関心を寄せる広範囲のモデルには当てはまりません。ワークフローのもう 1 つの目標
> いくつかの計算問題を回避し、残りの問題を効率的に診断できるようにすることです。

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- 有限の計算リソースを使用して。

## Chunk 0659

### English（抽出4行）

> Here too deconstructing the model into simpler versions can be helpful: it is easier to understand
> computational challenges when there are fewer moving parts.
> Hence, even if a mathematical
> description of a model is given, correctly implementing the model tends to require iteration.

### 日本語訳（自動翻訳）

> ここでも、モデルをより単純なバージョンに分解すると役に立ちます。理解しやすくなります。
> 可動部品が少ない場合、計算上の課題が生じます。
> したがって、たとえ数学的であっても、
> モデルの説明が与えられると、モデルを正しく実装するには反復が必要になる傾向があります。

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- ここでも、モデルをより単純なバージョンに分解すると役に立ちます。

## Chunk 0660

### English（抽出4行）

> Not only is iterative model building beneﬁcial from a cognitive and computational standpoint,
> but the complexity of complicated computational models makes it diﬃcult for the human user to
> disentangle computational concerns, modeling issues, data quality problems, and bugs in the code.
> By building models iteratively, we can employ software engineering techniques in our modeling

### 日本語訳（自動翻訳）

> 反復モデルの構築は、認知的および計算的観点から有益であるだけでなく、
> しかし、複雑な計算モデルの複雑さにより、人間のユーザーが
> 計算上の懸念、モデリングの問題、データ品質の問題、コードのバグを解きほぐします。
> モデルを繰り返し構築することで、モデリングにソフトウェア エンジニアリング手法を採用できます。

### 熟語・専門語

- **model building**: モデル構築。仮定・データ構造・prior・likelihoodを組み合わせる工程。

### 要約

- 反復モデルの構築は、認知的および計算的観点から有益であるだけでなく、 しかし、複雑な計算モデルの複雑さにより、人間のユーザーが 計算上の懸念、モデリングの問題、データ品質の問題、コードのバグを解きほぐします。

## Chunk 0661

### English（抽出4行）

> procedure. Simple model components can be checked to make sure they act in an expected way
> before more complicated components are added.
> 12.3.
> Model selection and overfitting

### 日本語訳（自動翻訳）

> 手順。単純なモデルコンポーネントをチェックして、期待どおりに動作することを確認できます。
> より複雑なコンポーネントが追加される前に。
> 12.3.
> モデルの選択とオーバーフィッティング

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

> 提案された反復ワークフローの潜在的な問題は、モデルの改善が条件付けされていることです。
> 現在検討されているモデルとデータの間の不一致、したがって少なくともいくつかの側面について
> データの一部は複数回使用されます。この「二重浸漬」は原理的に周波数を脅かす可能性があります。
> 推論の特性に影響を与えるため、過剰適合が発生する可能性を認識することが重要です。

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- 提案された反復ワークフローの潜在的な問題は、モデルの改善が条件付けされていることです。

## Chunk 0663

### English（抽出4行）

> from model selection, as considered for example by Fithian et al. (2015) and Loftus (2015). A
> related issue is the garden of forking paths, the idea that diﬀerent models would have been ﬁt had
> the data come out diﬀerently (Gelman and Loken, 2013). We do not advocate selecting the best
> ﬁt among some such set of models. Instead, we describe a process of building to a more complex

### 日本語訳（自動翻訳）

> たとえばFithianらによって検討されたように、モデルの選択から。 （2015）およびロフタス（2015）。あ
> 関連する問題は、分岐する道の庭であり、異なるモデルが適合していただろうという考えです。
> 得られるデータは異なります (Gelman と Loken、2013)。私たちは最良のものを選択することを推奨するものではありません
> このようないくつかのモデルのセットに適合します。代わりに、より複雑なシステムを構築するプロセスについて説明します。

### 熟語・専門語

- **ESS**: 有効サンプルサイズ。自己相関を考慮した独立サンプル相当数。

### 要約

- たとえばFithianらによって検討されたように、モデルの選択から。

## Chunk 0664

### English（抽出4行）

> model taking the time to understand and justify each decision.
> To put it in general terms: suppose we ﬁt model M1, then a posterior predictive check reveals
> problems with its ﬁt to data, so we move to an improved M2 that, we hope, includes more prior
> information and makes more sense with respect to the data and the applied problem under study. But

### 日本語訳（自動翻訳）

> それぞれの決定を理解し、正当化するために時間をかけてモデル化します。
> 一般的な言葉で言うと、モデル M1 に適合すると仮定すると、事後予測チェックにより次のことが明らかになります。
> データへの適合性に問題があるため、改善された M2 に移行します。
> 情報を提供し、データと研究中の応用問題に関してより意味をなすことができます。しかし、

### 熟語・専門語

- **posterior predictive**: 事後予測。推定後のモデルが観測データの特徴を再現できるかを見る診断。
- **decision**: 意思決定。予測分布を損失・効用・行動選択へ接続する工程。

### 要約

- それぞれの決定を理解し、正当化するために時間をかけてモデル化します。

## Chunk 0665

### English（抽出4行）

> had the data been diﬀerent, we would have been satisﬁed with M1. The steps of model checking and
> improvement, while absolutely necessary, represent an aspect of ﬁtting to data that is not captured
> in the likelihood or the prior.
> This is an example of the problem of post-selection inference (Berk et al., 2013, Efron, 2013).

### 日本語訳（自動翻訳）

> データが異なっていたら、M1 に満足していただろう。モデルチェックの手順と
> 改善は絶対に必要ですが、収集されていないデータへの適合という側面を表しています
> 可能性として、あるいは事前に。
> これは選択後の推論の問題の例です (Berk et al., 2013、Efron, 2013)。

### 熟語・専門語

- **model checking**: モデルチェック。モデルの仮定・予測・計算結果がデータや目的に合うか検査すること。
- **likelihood**: 尤度。パラメータが与えられたときデータがどれだけ起こりやすいか。
- **ESS**: 有効サンプルサイズ。自己相関を考慮した独立サンプル相当数。

### 要約

- データが異なっていたら、M1 に満足していただろう。

## Chunk 0666

### English（抽出4行）

> Much of the research in this area has been on how to adjust p-values and conﬁdence intervals
> to have appropriate frequency properties conditional on the entire ﬁtting procedure, but Bayesian
> inferences are subject to this concern as well. For example, here is the story of one of the adaptations
> we made in election forecasting (Gelman, Hullman, et al., 2020):

### 日本語訳（自動翻訳）

> この分野における研究の多くは、p 値と信頼区間を調整する方法に関するものでした。
> フィッティング手順全体を条件として適切な周波数特性を持つ必要がありますが、ベイジアン
> 推論もこの懸念の影響を受けます。たとえば、これは適応の 1 つの物語です。
> 私たちは選挙予測で次のようにしました（Gelman、Hullman、他、2020）。

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- この分野における研究の多くは、p 値と信頼区間を調整する方法に関するものでした。

## Chunk 0667

### English（抽出4行）

> A few weeks after we released our ﬁrst model of the election cycle for The Economist,
> we were disturbed at the narrowness of some of its national predictions. In particular,
> at one point the model gave Biden 99% chance of winning the national vote. Biden was
> clearly in the lead, but 99% seemed like too high a probability given the information

### 日本語訳（自動翻訳）

> エコノミスト誌に選挙サイクルの最初のモデルをリリースしてから数週間後、
> 私たちは、その国家的予測の一部が的外れであることに動揺しました。特に、
> ある時点では、このモデルによりバイデンが全国投票を獲得する確率が99％となった。バイデンは
> 明らかにリードしているが、情報を考えると99%の可能性は高すぎるように思えた

### 熟語・専門語

- **ESS**: 有効サンプルサイズ。自己相関を考慮した独立サンプル相当数。
- **prediction**: 予測。未知/将来/除外データに対する分布や点推定。

### 要約

- エコノミスト誌に選挙サイクルの最初のモデルをリリースしてから数週間後、 私たちは、その国家的予測の一部が的外れであることに動揺しました。

## Chunk 0668

### English（抽出4行）

> available at that time.
> Seeing this implausible predictive interval motivated us to
> refactor our model, and we found some bugs in our code and some other places where
> the model could be improved—including an increase in between-state correlations,

### 日本語訳（自動翻訳）

> その時点で利用可能です。
> この信じがたい予測間隔を見て、私たちは次のことをするようになりました。
> モデルをリファクタリングしたところ、コードやその他の場所にいくつかのバグが見つかりました。
> モデルは、状態間の相関関係の増加を含めて改善される可能性があります。

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- その時点で利用可能です。

## Chunk 0669

### English（抽出4行）

> which increased uncertainty of national aggregates. The changes in our model did not
> have huge eﬀects—not surprisingly given that we had tested our earlier model on 2008,
> 2012, and 2016—but the revision did lower Biden’s estimated probability of winning
> the popular vote to 98%. This was still a high value, but it was consistent with the

### 日本語訳（自動翻訳）

> これにより、国家集計の不確実性が増大しました。私たちのモデルの変更はそうではありませんでした
> 大きな効果があります。2008 年に以前のモデルをテストしていたことを考えると、驚くべきことではありませんが、
> 2012年と2016年 - しかし、この修正によりバイデンの推定勝利確率は低下した
> 人気投票は98％。これはまだ高い値ですが、

### 熟語・専門語

- **uncertainty**: 不確実性。観測・パラメータ・モデル構造・意思決定に残る曖昧さ。

### 要約

- これにより、国家集計の不確実性が増大しました。

## Chunk 0670

### English（抽出4行）

> polling and what we’d seen of variation in the polls during the campaign.
> The errors we caught were real, but if we had not been aware of these particular problematic
> predictions, we might have never gone back to check. This data-dependence of our analysis implies
> a problem with a fully Bayesian interpretation of the probability statements based on the ﬁnal

### 日本語訳（自動翻訳）

> 世論調査と、選挙期間中の世論調査の変動について私たちが観察したこと。
> 私たちが発見したエラーは本物でしたが、もしこれらの特定の問題に気づいていなかったら
> 予測した場合、私たちは戻って確認することはなかったかもしれません。私たちの分析のこのデータ依存性は、
> 最終的な確率ステートメントに基づく確率ステートメントの完全なベイズ解釈の問題

### 熟語・専門語

- **prediction**: 予測。未知/将来/除外データに対する分布や点推定。

### 要約

- 世論調査と、選挙期間中の世論調査の変動について私たちが観察したこと。

## Chunk 0671

### English（抽出4行）

> model we settled on. And, in this case, model averaging would not resolve this problem: we would
> not want to average our ﬁnal model with its buggy predecessor. We might want to average its
> predictions with those of some improved future model, but we can’t do that either, as this future
> model does not yet exist!

### 日本語訳（自動翻訳）

> 私たちが決めたモデル。そして、この場合、モデルの平均化ではこの問題は解決されません。
> 最終モデルをバグのある以前のモデルと平均化したくないのです。その平均値を求めたいかもしれません
> 改良された将来モデルの予測と併用することもできますが、それも不可能です。
> モデルはまだ存在しません!

### 熟語・専門語

- **ESS**: 有効サンプルサイズ。自己相関を考慮した独立サンプル相当数。
- **prediction**: 予測。未知/将来/除外データに対する分布や点推定。

### 要約

- 私たちが決めたモデル。

## Chunk 0672

### English（抽出4行）

> That said, we think that Bayesian workﬂow as described here will avoid the worst problems of
> overﬁtting. Taylor and Tibshirani (2015) warn of the problem of inference conditional on having
> “searched for the strongest associations.” But our workﬂow does not involve searching for optimally-
> ﬁtting models or making hard model selection under uncertainty. Rather, we use problems with

### 日本語訳（自動翻訳）

> そうは言っても、ここで説明するベイジアン ワークフローは、最悪の問題を回避すると考えています。
> 過学習。 Taylor と Tibshirani (2015) は、次のことを条件とする推論の問題について警告しています。
> 「最も強い関連性を探しました。」しかし、私たちのワークフローには、最適な検索は含まれていません。
> 不確実性の下でモデルをフィッティングしたり、難しいモデルを選択したりする。むしろ、次の問題を使用します。

### 熟語・専門語

- **uncertainty**: 不確実性。観測・パラメータ・モデル構造・意思決定に残る曖昧さ。

### 要約

- そうは言っても、ここで説明するベイジアン ワークフローは、最悪の問題を回避すると考えています。

## Chunk 0673

### English（抽出4行）

> ﬁtted models to reassess our modeling choices and, where possible, include additional information.
> For our purposes, the main message we take from concerns about post-selection inference is that our
> ﬁnal model should account for as much information as possible, and when we might be selecting
> among a large set of possible models, we instead embed these in a larger model, perform predictive

### 日本語訳（自動翻訳）

> モデリングの選択を再評価するためにモデルを適合させ、可能であれば追加情報を含めます。
> 私たちの目的のために、選択後の推論に関する懸念から私たちが受け取る主なメッセージは、
> 最終モデルでは、可能な限り多くの情報を考慮する必要があり、いつ選択するかを考慮する必要があります。
> 考えられるモデルの大きなセットの中から、代わりにこれらをより大きなモデルに埋め込み、予測を実行します。

### 熟語・専門語

- **ESS**: 有効サンプルサイズ。自己相関を考慮した独立サンプル相当数。

### 要約

- モデリングの選択を再評価するためにモデルを適合させ、可能であれば追加情報を含めます。

## Chunk 0674

### English（抽出4行）

> model averaging, or use all of the models simultaneously (see Section 8). As discussed by Gelman,
> Hill, and Yajima (2012), we expect that would work better than trying to formally model the process
> of model checking and expansion.
> We also believe that our workﬂow enables practitioners to perform severe tests of many of the

### 日本語訳（自動翻訳）

> モデルの平均化、またはすべてのモデルを同時に使用します (セクション 8 を参照)。ゲルマン氏が論じたように、
> Hill と Yajima (2012)、プロセスを正式にモデル化しようとするよりもうまく機能すると予想しています。
> モデルのチェックと拡張。
> また、私たちは、私たちのワークフローにより、専門家が多くの項目について厳しいテストを実行できると信じています。

### 熟語・専門語

- **model checking**: モデルチェック。モデルの仮定・予測・計算結果がデータや目的に合うか検査すること。
- **ESS**: 有効サンプルサイズ。自己相関を考慮した独立サンプル相当数。

### 要約

- モデルの平均化、またはすべてのモデルを同時に使用します (セクション 8 を参照)。

## Chunk 0675

### English（抽出4行）

> assumptions that underlie the models being examined (Mayo, 2018). Our claim is that often a
> model whose assumptions withstood such severe tests is, despite being the result of data-dependent
> iterative workﬂow, more trustworthy than a preregistered model that has not been tested at all.
> On a slightly diﬀerent tack, iterative model building is fully justiﬁed as a way to understand a

### 日本語訳（自動翻訳）

> 調査対象のモデルの基礎となる仮定 (Mayo、2018)。私たちの主張は、多くの場合、
> データに依存した結果であるにもかかわらず、このような厳しいテストに耐えた仮定を備えたモデルは、
> 反復的なワークフローであり、まったくテストされていない事前登録されたモデルよりも信頼性が高くなります。
> 少し異なる考え方では、反復モデルの構築は、問題を理解する方法として完全に正当化されます。

### 熟語・専門語

- **model building**: モデル構築。仮定・データ構造・prior・likelihoodを組み合わせる工程。

### 要約

- 調査対象のモデルの基礎となる仮定 (Mayo、2018)。

## Chunk 0676

### English（抽出4行）

> ﬁxed, complex model. This is an important part of workﬂow as it is well known that components
> in complex models can interact in complex ways. For example, Hodges and Reich (2010) describe
> how structured model components such as spatial eﬀects can have complex interactions with linear
> covariate eﬀects.

### 日本語訳（自動翻訳）

> 固定された複雑なモデル。よく知られているように、これはワークフローの重要な部分です。
> 複雑なモデルでは、複雑な方法で相互作用する可能性があります。たとえば、Hodges と Reich (2010) は次のように説明しています。
> 空間効果などの構造化モデルコンポーネントが線形とどのように複雑な相互作用を持ち得るか
> 共変量効果。

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- 固定された複雑なモデル。

## Chunk 0677

### English（抽出4行）

> 12.4.
> Bigger datasets demand bigger models
> Great progress has been made in recent decades on learning from data using methods developed
> in statistics, machine learning, and applied ﬁelds ranging from psychometrics to pharmacology.

### 日本語訳（自動翻訳）

> 12.4.
> より大きなデータセットにはより大きなモデルが必要です
> 開発された手法を使用したデータからの学習に関しては、ここ数十年で大きな進歩が見られました。
> 統計学、機械学習、および心理測定学から薬理学に至るまでの応用分野。

### 熟語・専門語

- **ESS**: 有効サンプルサイズ。自己相関を考慮した独立サンプル相当数。

### 要約

- 12.4. より大きなデータセットにはより大きなモデルが必要です 開発された手法を使用したデータからの学習に関しては、ここ数十年で大きな進歩が見られました。

## Chunk 0678

### English（抽出4行）

> Hierarchical Bayesian modeling, deep learning, and other regularization-based approaches are
> allowing researchers to ﬁt larger, more complex models to real-world data, enabling information
> aggregation and partial pooling of inferences from diﬀerent sources of data.
> While the proposed workﬂow oﬀers advantages regardless of the size of the dataset, the case

### 日本語訳（自動翻訳）

> 階層ベイジアン モデリング、深層学習、その他の正則化ベースのアプローチは、
> 研究者がより大規模で複雑なモデルを現実世界のデータに適合させ、情報を有効にすることができるようになります。
> さまざまなデータソースからの推論の集約と部分的なプール。
> 提案されたワークフローはデータセットのサイズに関係なく利点を提供しますが、

### 熟語・専門語

- **ESS**: 有効サンプルサイズ。自己相関を考慮した独立サンプル相当数。

### 要約

- 階層ベイジアン モデリング、深層学習、その他の正則化ベースのアプローチは、 研究者がより大規模で複雑なモデルを現実世界のデータに適合させ、情報を有効にすることができるようになります。

## Chunk 0679

### English（抽出4行）

> of big data deserves a special mention. “Big data” is sometimes deﬁned as being too big to ﬁt in
> memory on your machine, but here we use the term more generally to also include datasets that are
> so large that our usual algorithms do not run in reasonable time. In either case, the deﬁnition is
> relative to your current computing capacity and inferential goals.

### 日本語訳（自動翻訳）

> ビッグデータの重要性は特筆に値します。 「ビッグデータ」は、大きすぎて収まらないものとして定義されることがあります。
> マシン上のメモリですが、ここではこの用語をより一般的に、次のようなデータセットも含めて使用します。
> サイズが大きすぎるため、通常のアルゴリズムは適切な時間内に実行できません。いずれの場合も、定義は次のようになります。
> 現在のコンピューティング能力と推論の目標に応じて。

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- ビッグデータの重要性は特筆に値します。

## Chunk 0680

### English（抽出4行）

> It is frequently assumed that big data can alleviate the need for careful modeling. We do
> not believe this is the case. Quantity does not always substitute for quality. Big data is messy
> data. Big data prioritizes availability over randomization, which means Big data is almost always
> observational rather than from designed experiments. Big data frequently uses available proxies

### 日本語訳（自動翻訳）

> ビッグデータにより、慎重なモデリングの必要性が軽減されるとよく考えられています。私たちはそうします
> そんなことは信じられない。量が必ずしも質の代わりになるわけではありません。ビッグデータは厄介です
> データ。ビッグ データはランダム化よりも可用性を優先します。つまり、ビッグ データはほとんどの場合、
> 計画された実験によるものではなく、観察によるものです。ビッグデータは利用可能なプロキシを頻繁に使用します

### 熟語・専門語

- **ESS**: 有効サンプルサイズ。自己相関を考慮した独立サンプル相当数。

### 要約

- ビッグデータにより、慎重なモデリングの必要性が軽減されるとよく考えられています。

## Chunk 0681

### English（抽出4行）

> rather than direct measurements of underlying constructs of interest. To make relevant inferences
> from big data, we need to extrapolate from sample to population, from control to treatment group,
> and from measurements to latent variables. All these steps require statistical assumptions and
> adjustment of some sort, which in the Bayesian framework is done using probability modeling

### 日本語訳（自動翻訳）

> 対象となる基礎構造を直接測定するのではなく、関連する推論を行うため
> ビッグデータから、サンプルから母集団、対照群から治療群までを推定する必要があります。
> そして測定から潜在変数まで。これらすべてのステップには統計的な仮定が必要です。
> ある種の調整。ベイジアン フレームワークでは確率モデリングを使用して行われます。

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- 対象となる基礎構造を直接測定するのではなく、関連する推論を行うため ビッグデータから、サンプルから母集団、対照群から治療群までを推定する必要があります。

## Chunk 0682

### English（抽出4行）

> and mathematical connections to inferential goals. For example, we might ﬁt a multilevel model
> for data given respondents’ demographic and geographic characteristics and then poststratify to
> connect the predictions from this model to the goal of inference about the general population.
> Each of these steps of statistical extrapolation should be more eﬀective if we adjust for more

### 日本語訳（自動翻訳）

> そして推論目標への数学的つながり。たとえば、マルチレベル モデルを当てはめることができます。
> 回答者の人口統計的および地理的特徴を考慮したデータを対象として、事後階層化を行います。
> このモデルからの予測を一般集団に関する推論の目標に結び付けます。
> 統計的外挿のこれらの各ステップは、より多くの値を調整するとより効果的になるはずです。

### 熟語・専門語

- **prediction**: 予測。未知/将来/除外データに対する分布や点推定。

### 要約

- そして推論目標への数学的つながり。

## Chunk 0683

### English（抽出4行）

> factors—that is, include more information—but we quickly reach a technical barrier.
> Models
> that adjust for many of factors can become hard to estimate, and eﬀective modeling requires (a)
> regularization to get more stable estimates (and in turn to allow us to adjust for more factors),

### 日本語訳（自動翻訳）

> しかし、すぐに技術的な障壁に到達します。
> モデル
> 多くの要因を調整すると推定が困難になる可能性があり、効果的なモデリングには次のことが必要です。
> より安定した推定値を取得するための正規化 (そして、より多くの要素を調整できるようにするため)、

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- しかし、すぐに技術的な障壁に到達します。

## Chunk 0684

### English（抽出4行）

> and (b) modeling of latent variables (for example parameters that vary by person when modeling
> longitudinal data), missingness, and measurement error.
> A key part of Bayesian workﬂow is adapting the model to the data at hand and the questions
> of interest. The model does not exist in isolation and is not speciﬁed from the outside; it emerges

### 日本語訳（自動翻訳）

> (b) 潜在変数のモデリング (たとえば、モデリング時に人によって異なるパラメータなど)
> 縦方向データ）、欠損、測定誤差。
> ベイジアン ワークフローの重要な部分は、モデルを手元のデータと質問に適応させることです。
> 興味深い。モデルは孤立して存在するものではなく、外部から指定されるものでもありません。それは現れる

### 熟語・専門語

- **ESS**: 有効サンプルサイズ。自己相関を考慮した独立サンプル相当数。

### 要約

- (b) 潜在変数のモデリング (たとえば、モデリング時に人によって異なるパラメータなど) 縦方向データ）、欠損、測定誤差。

## Chunk 0685

### English（抽出4行）

> from engagement with the application and the available data.
> 12.5.
> Prediction, generalization, and poststratification
> The three core tasks of statistics are generalizing from sample to population, generalizing from

### 日本語訳（自動翻訳）

> アプリケーションと利用可能なデータとの関わりから。
> 12.5。
> 予測、一般化、事後層別化
> 統計の 3 つの中心的なタスクは、サンプルから母集団への一般化、サンプルから母集団への一般化です。

### 熟語・専門語

- **prediction**: 予測。未知/将来/除外データに対する分布や点推定。

### 要約

- アプリケーションと利用可能なデータとの関わりから。

## Chunk 0686

### English（抽出4行）

> control to treatment group, and generalizing from observed data to underlying constructs of interest.
> In machine learning and causal inference, the terms “domain adaptation” and “transportability” have
> been used to represent the challenges of taking inference from a particular dataset and applying it in
> a new problem (Blitzer, Dredze, and Pereira, 2007, Pearl and Bareinboim, 2011). Many statistical

### 日本語訳（自動翻訳）

> コントロールから治療グループへ、そして観察されたデータから基礎となる関心のある構造まで一般化します。
> 機械学習と因果推論では、「ドメイン適応」と「トランスポータビリティ」という用語が使われます。
> 特定のデータセットから推論を取得し、それを応用する際の課題を表すために使用されます。
> 新たな問題 (Blitzer、Dredze、Pereira、2007、Pearl と Bareinboim、2011)。多くの統計

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- コントロールから治療グループへ、そして観察されたデータから基礎となる関心のある構造まで一般化します。

## Chunk 0687

### English（抽出4行）

> tools have been developed over the years to attack problems of generalization, for example weighting
> and poststratiﬁcation in sample surveys, matching and regression in causal inference, and latent
> variable modeling in areas such as psychometrics and econometrics where there is concern about
> indirect or biased observations.

### 日本語訳（自動翻訳）

> ツールは、重み付けなどの一般化の問題を攻撃するために長年にわたって開発されてきました。
> サンプル調査における事後層別化、因果推論におけるマッチングと回帰、潜在的
> 心理測定や計量経済などの懸念がある分野における変数モデリング
> 間接的または偏った観察。

### 熟語・専門語

- **ESS**: 有効サンプルサイズ。自己相関を考慮した独立サンプル相当数。

### 要約

- ツールは、重み付けなどの一般化の問題を攻撃するために長年にわたって開発されてきました。

## Chunk 0688

### English（抽出4行）

> Bayesian methods enter in various ways, including the idea of hierarchical modeling or par-
> tial pooling to appropriately generalize across similar but not identical settings, which has been
> rediscovered in many ﬁelds (e.g., Henderson, 1950, Novick et al., 1972, Gelman and Hill, 2007,
> Finkel and Manning, 2009, Daumé, 2009), regularization to facilitate the use of large nonparamet-

### 日本語訳（自動翻訳）

> ベイジアン手法は、階層モデリングやパー
> tial プーリングを使用して、類似しているが同一ではない設定全体を適切に一般化します。
> 多くの分野で再発見された（例、Henderson、1950、Novic et al.、1972、Gelman and Hill、2007、
> Finkel と Manning、2009、Daumé、2009)、大規模な非パラメータの使用を容易にするための正則化。

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- ベイジアン手法は、階層モデリングやパー tial プーリングを使用して、類似しているが同一ではない設定全体を適切に一般化します。

## Chunk 0689

### English（抽出4行）

> ric models (Hill, 2011), and multilevel modeling for latent variables (Skrondal and Rabe-Hesketh,
> 2004), and there are connections between transportability and Bayesian graph models (Pearl and
> Bareinboim, 2014).
> Bayesian workﬂow does not stop with inference for the ﬁtted model. We are also interested

### 日本語訳（自動翻訳）

> ric モデル (Hill、2011)、および潜在変数のマルチレベル モデリング (Skrondal および Rabe-Hesketh、
> 2004)、可搬性とベイジアン グラフ モデルの間には関連性があります (Pearl と
> バレインボイム、2014)。
> ベイジアン ワークフローは、適合モデルの推論で終わりません。私たちも興味があります

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- ric モデル (Hill、2011)、および潜在変数のマルチレベル モデリング (Skrondal および Rabe-Hesketh、 2004)、可搬性とベイジアン グラフ モデルの間には関連性があります (Pearl と バレイ…

## Chunk 0690

### English（抽出4行）

> in inferences for new real-world situations, which implies that the usual prior and data model is
> embedded in a larger framework including predictions and inferences for new settings, including
> potentially diﬀerent modes of measurement and treatment assignments. Statistical models can also
> go into production, which provides future opportunities for feedback and improvement.

### 日本語訳（自動翻訳）

> 新しい現実世界の状況の推論では、通常の事前モデルとデータ モデルが
> 新しい設定の予測と推論を含む、より大きなフレームワークに組み込まれています。
> 潜在的に異なる測定モードと治療割り当て。統計モデルでは次のこともできます。
> 本番環境に入ることで、将来のフィードバックと改善の機会が得られます。

### 熟語・専門語

- **prediction**: 予測。未知/将来/除外データに対する分布や点推定。

### 要約

- 新しい現実世界の状況の推論では、通常の事前モデルとデータ モデルが 新しい設定の予測と推論を含む、より大きなフレームワークに組み込まれています。

## Chunk 0691

### English（抽出4行）

> Just as the prior can often only be understood in the context of the likelihood (Gelman et al.,
> 2017, Kennedy et al., 2019), so should the model be understood in light of how it will be used.
> For example, Singer et al. (1999) and Gelman, Stevens, and Chan (2003) ﬁt a series of models
> to estimate the eﬀects of ﬁnancial incentives on response rates in surveys. The aspects of these

### 日本語訳（自動翻訳）

> 事前確率は尤度の文脈でのみ理解できることが多いのと同様に (Gelman et al.、
> 2017、Kennedy et al.、2019)、モデルはそれがどのように使用されるかを考慮して理解する必要があります。
> 例えば、シンガーら。 (1999) および Gelman、Stevens、Chan (2003) は一連のモデルに適合
> 調査の回答率に対する金銭的インセンティブの影響を推定するため。これらの側面

### 熟語・専門語

- **likelihood**: 尤度。パラメータが与えられたときデータがどれだけ起こりやすいか。

### 要約

- 事前確率は尤度の文脈でのみ理解できることが多いのと同様に (Gelman et al.、 2017、Kennedy et al.、2019)、モデルはそれがどのように使用されるかを考慮して理解する必要があります。

## Chunk 0692

### English（抽出4行）

> models that will be relevant for predicting eﬀects for small incentives in mail surveys are diﬀerent
> from what is relevant for predictions for large incentives in telephone surveys. This is related to
> the discussion of sensitivity analysis in Sections 6.3 and 8.1. For another illustration of this point,
> Rubin (1983) gives an example where the choice of transformation has minor eﬀects on inference

### 日本語訳（自動翻訳）

> 郵便調査における少額のインセンティブの効果を予測するのに関連するモデルは異なります。
> 電話調査における高額なインセンティブの予測に関連するものから。これに関連するのは、
> 感度分析についてはセクション 6.3 および 8.1 で説明します。この点を別の例で説明すると、
> Rubin (1983) は、変換の選択が推論にわずかな影響を与える例を示しています。

### 熟語・専門語

- **prediction**: 予測。未知/将来/除外データに対する分布や点推定。

### 要約

- 郵便調査における少額のインセンティブの効果を予測するのに関連するモデルは異なります。

## Chunk 0693

### English（抽出4行）

> for the median of a distribution while having large eﬀects on inference for the mean.
> 12.6.
> Going forward
> All workﬂows have holes, and we cannot hope to exhaust all potential ﬂaws of applied data analysis.

### 日本語訳（自動翻訳）

> 分布の中央値については、平均値の推論に大きな影響を与えます。
> 12.6。
> 今後に向けて
> すべてのワークフローには穴があり、応用データ分析の潜在的な欠陥をすべて網羅することは期待できません。

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- 分布の中央値については、平均値の推論に大きな影響を与えます。

## Chunk 0694

### English（抽出4行）

> In the prior and posterior predictive check, a wrong model will pass the check silently for overﬁtting
> all output at the observed values. In simulation based calibration, an incorrect computation program
> can satisfy the diagnostics if the posterior stays in the prior. In cross validation, the consistency
> relies on conditional independence and stationarity of the covariates. In causal inference, there are

### 日本語訳（自動翻訳）

> 事前および事後予測チェックでは、間違ったモデルは過剰適合のチェックを黙って通過します。
> すべての出力は観測値で行われます。シミュレーションベースのキャリブレーションでは、不正な計算プログラム
> 事後値が事前値内に留まる場合、診断を満たすことができます。相互検証では、一貫性が
> 共変量の条件付き独立性と定常性に依存します。因果推論には、

### 熟語・専門語

- **posterior predictive**: 事後予測。推定後のモデルが観測データの特徴を再現できるかを見る診断。
- **cross validation**: 交差検証。汎化性能を推定するためにデータを分割/近似除外する評価法。
- **validation**: 検証。モデルが目的・データ・外部知識に照らして妥当かを確認すること。

### 要約

- 事前および事後予測チェックでは、間違ったモデルは過剰適合のチェックを黙って通過します。

## Chunk 0695

### English（抽出4行）

> always untestable causal assumptions, no matter how many models we have ﬁt. More generally,
> statistics relies on some extrapolation, for which some assumption is always needed. To ultimately
> check the model and push the workﬂow forward, we often need to collect more data, along the way
> expanding the model, and an appropriate experiment design will be part of this larger workﬂow.

### 日本語訳（自動翻訳）

> どれだけ多くのモデルを適合させたとしても、因果関係の仮定は常にテストできません。より一般的には、
> 統計は何らかの外挿に依存しており、そのためには常に何らかの仮定が必要です。最終的には
> モデルをチェックしてワークフローを前進させると、途中でさらに多くのデータを収集する必要が生じることがよくあります。
> モデルを拡張すると、適切な実験計画がこのより大きなワークフローの一部になります。

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- どれだけ多くのモデルを適合させたとしても、因果関係の仮定は常にテストできません。

## Chunk 0696

### English（抽出4行）

> This article has focused on data analysis: the steps leading from data and assumptions to
> scientiﬁc inferences and predictions. Other important aspects of Bayesian statistics not discussed
> here include design, measurement, and data collection (coming before the data analysis) and
> decision making and communication (coming after data analysis). We also have not gone into the

### 日本語訳（自動翻訳）

> この記事では、データ分析、つまりデータと仮定からデータ分析に至るまでのステップに焦点を当てました。
> 科学的な推論と予測。ベイズ統計のその他の重要な側面については議論されていない
> ここには設計、測定、データ収集（データ分析の前に行われます）が含まれます。
> 意思決定とコミュニケーション (データ分析の後に行われます)。私たちも入っていません。

### 熟語・専門語

- **prediction**: 予測。未知/将来/除外データに対する分布や点推定。
- **decision**: 意思決定。予測分布を損失・効用・行動選択へ接続する工程。

### 要約

- この記事では、データ分析、つまりデータと仮定からデータ分析に至るまでのステップに焦点を当てました。

## Chunk 0697

### English（抽出4行）

> details of computing environments or the social and economic aspects of collaboration, sharing of
> data and code, and so forth.
> The list of workﬂow steps we have provided is too long to be a useful guide to practice. What
> can be done? Rather than giving users a 25-item checklist, we hope that we can clarify these

### 日本語訳（自動翻訳）

> コンピューティング環境の詳細、またはコラボレーションの社会的および経済的側面、共有
> データとコードなど。
> 私たちが提供したワークフロー ステップのリストは長すぎるため、実践に役立つガイドにはなりません。何
> できるでしょうか？ユーザーに 25 項目のチェックリストを提供するのではなく、これらを明確にすることができればと考えています。

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- コンピューティング環境の詳細、またはコラボレーションの社会的および経済的側面、共有 データとコードなど。

## Chunk 0698

### English（抽出4行）

> processes so they can be applied in a structured or even automated framework. Our rough plan is
> as follows:
> • Abstract these principles from our current understanding of best practice, thus producing the
> present article.

### 日本語訳（自動翻訳）

> プロセスを構築して、構造化されたフレームワークや自動化されたフレームワークに適用できるようにします。私たちの大まかな計画は
> 次のように:
> • 現在のベストプラクティスの理解からこれらの原則を抽象化し、
> 現在の記事。

### 熟語・専門語

- **ESS**: 有効サンプルサイズ。自己相関を考慮した独立サンプル相当数。

### 要約

- プロセスを構築して、構造化されたフレームワークや自動化されたフレームワークに適用できるようにします。

## Chunk 0699

### English（抽出4行）

> • Apply this workﬂow to some applied problems and write these up as case studies.
> • Implement as much of the workﬂow as possible in software tools for general application.
> Automating what can be automated should enable the statistician or applied researcher to go beyond
> button pushing and integrate data with domain expertise. The ultimate goal of this project is to

### 日本語訳（自動翻訳）

> • このワークフローをいくつかの応用問題に適用し、ケーススタディとして書き留めます。
> • 可能な限り多くのワークフローを一般的なアプリケーション用のソフトウェア ツールに実装します。
> 自動化できるものは自動化することで、統計学者や応用研究者はそれを超えることができるはずです
> ボタンを押してデータをドメインの専門知識と統合します。このプロジェクトの最終目標は、

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- • このワークフローをいくつかの応用問題に適用し、ケーススタディとして書き留めます。

## Chunk 0700

### English（抽出4行）

> enable ourselves and other data analysts to use statistical modeling more eﬀectively, and to allow
> us to build conﬁdence in the inferences and decisions that we come to.
> This article is a review, a survey of the territory, a reminder of methods we have used, procedures
> we have followed, and ideas we would like to pursue. To be useful to practitioners, we need worked

### 日本語訳（自動翻訳）

> 私たち自身や他のデータ アナリストが統計モデリングをより効果的に使用できるようにし、
> 私たちが導き出した推論と決定に自信を持てるようになります。
> この記事はレビュー、領土の調査、使用した方法、手順の思い出です。
> 私たちが追求してきたアイデア、そして追求したいアイデア。実践者の役に立つためには、努力する必要があります

### 熟語・専門語

- **decision**: 意思決定。予測分布を損失・効用・行動選択へ接続する工程。

### 要約

- 私たち自身や他のデータ アナリストが統計モデリングをより効果的に使用できるようにし、 私たちが導き出した推論と決定に自信を持てるようになります。

## Chunk 0701

### English（抽出4行）

> examples with code. We would also like to provide more structure: if not a checklist, at least a
> some paths to follow in a Bayesian analysis. Some guidance is given in the Stan User’s Guide
> (Stan Development Team, 2020), and we are working on a book on Bayesian workﬂow using Stan
> to provide such a resource to novice and experienced statisticians alike. That said, we believe this

### 日本語訳（自動翻訳）

> コード付きの例。また、より多くの構造を提供したいと考えています。チェックリストではないとしても、少なくとも
> ベイジアン分析で従うべきいくつかのパス。いくつかのガイダンスは Stan ユーザーガイドに記載されています
> (Stan 開発チーム、2020)、私たちは Stan を使用したベイジアン ワークフローに関する書籍の執筆に取り組んでいます。
> 初心者にも経験豊富な統計学者にも同様にそのようなリソースを提供します。つまり、私たちはこれを信じています

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- コード付きの例。

## Chunk 0702

### English（抽出4行）

> paper has value as a ﬁrst step toward putting the many diﬀerent activities of Bayesian workﬂow
> under a single roof.
> References
> Afrabandpey, H., Peltola, T., Piironen, J., Vehtari, A., and Kaski, S. (2020). Making Bayesian

### 日本語訳（自動翻訳）

> この論文は、ベイジアン ワークフローのさまざまなアクティビティを実装するための最初のステップとして価値があります。
> 一つ屋根の下で。
> 参考文献
> Afrabandpey, H.、Peltola, T.、Piironen, J.、Vehtari, A.、および Kaski, S. (2020)。ベイジアンの作成

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- この論文は、ベイジアン ワークフローのさまざまなアクティビティを実装するための最初のステップとして価値があります。

## Chunk 0703

### English（抽出4行）

> predictive models interpretable: A decision theoretic approach. Machine Learning 109, 1855–
> 1876.
> Akaike, H. (1973). Information theory and an extension of the maximum likelihood principle. In
> Proceedings of the Second International Symposium on Information Theory, ed. B. N. Petrov

### 日本語訳（自動翻訳）

> 解釈可能な予測モデル: 決定理論的アプローチ。機械学習 109、1855–
> 1876年。
> 赤池博史（1973）。情報理論と最尤原理の拡張。で
> 第 2 回情報理論国際シンポジウム議事録、編。 B.N.ペトロフ

### 熟語・専門語

- **likelihood**: 尤度。パラメータが与えられたときデータがどれだけ起こりやすいか。
- **decision**: 意思決定。予測分布を損失・効用・行動選択へ接続する工程。

### 要約

- 解釈可能な予測モデル: 決定理論的アプローチ。

## Chunk 0704

### English（抽出4行）

> and F. Csaki, 267–281. Budapest: Akademiai Kiado. Reprinted in Breakthroughs in Statistics,
> ed. S. Kotz, 610–624. New York: Springer (1992).
> Berger, J. O., Bernardo, J. M., and Sun, D. (2009). The formal deﬁnition of reference priors.
> Annals of Statistics 37, 905–938.

### 日本語訳（自動翻訳）

> および F. Csaki、267–281。ブダペスト：アカデミアイ・キアド。 『Breakthroughs in Statistics』に転載
> 編S. コッツ、610–624。ニューヨーク: スプリンガー (1992)。
> Berger, J.O.、Bernardo, J.M.、Sun, D. (2009)。参照事前分布の正式な定義。
> 統計年報 37、905 ～ 938。

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- および F. Csaki、267–281。

## Chunk 0705

### English（抽出4行）

> Berk, R., Brown, L., Buja, A., Zhang, K., and Zhao, L. (2013). Valid post-selection inference.
> Annals of Statistics 41, 802–837.
> Berry, D. (1995). Statistics: A Bayesian Perspective. Duxbury Press.
> Betancourt, M. (2017a). A conceptual introduction to Hamiltonian Monte Carlo. arxiv.org/abs/

### 日本語訳（自動翻訳）

> Berk, R.、Brown, L.、Buja, A.、Zhang, K.、および Zhao, L. (2013)。有効な選択後の推論。
> 統計年報 41、802–837。
> ベリー、D. (1995)。統計: ベイズ主義の視点。ダックスベリープレス。
> ベタンクール、M. (2017a)。ハミルトニアン モンテカルロの概念的な紹介。 arxiv.org/abs/

### 熟語・専門語

- **ESS**: 有効サンプルサイズ。自己相関を考慮した独立サンプル相当数。

### 要約

- Berk, R.、Brown, L.、Buja, A.、Zhang, K.、および Zhao, L. (2013)。

## Chunk 0706

### English（抽出4行）

> 1701.02434
> Betancourt, M. (2017b). Identifying Bayesian mixture models. Stan Case Studies 4. mc-stan.org/
> users/documentation/case-studies/identifying_mixture_models.html
> Betancourt, M. (2018).

### 日本語訳（自動翻訳）

> 1701.02434
> ベタンクール、M. (2017b)。ベイジアン混合モデルの特定。 Stan のケーススタディ 4. mc-stan.org/
> users/documentation/case-studies/identifying_mixture_models.html
> ベタンクール、M. (2018)。

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- 1701.02434 ベタンクール、M. (2017b)。

## Chunk 0707

### English（抽出4行）

> Underdetermined linear regression.
> betanalpha.github.io/assets/case_
> studies/underdetermined_linear_regression.html
> Betancourt, M. (2020a). Towards a principled Bayesian workﬂow. betanalpha.github.io/assets/

### 日本語訳（自動翻訳）

> 過小決定線形回帰。
> betanalpha.github.io/assets/case_
> Studies/underdetermined_linear_regression.html
> ベタンクール、M. (2020a)。原則に基づいたベイジアン ワークフローに向けて。 betanalpha.github.io/assets/

### 熟語・専門語

- **ESS**: 有効サンプルサイズ。自己相関を考慮した独立サンプル相当数。

### 要約

- 過小決定線形回帰。

## Chunk 0708

### English（抽出4行）

> case_studies/principled_bayesian_workﬂow.html
> Betancourt, M. (2020b). Robust Gaussian Process Modeling. github.com/betanalpha/knitr_case_
> studies/tree/master/gaussian_processes
> Betancourt, M., and Girolami, M. (2015). Hamiltonian Monte Carlo for hierarchical models. In

### 日本語訳（自動翻訳）

> case_studies/principled_bayesian_workflow.html
> ベタンクール、M. (2020b)。堅牢なガウス プロセス モデリング。 github.com/betanalpha/knitr_case_
> 研究/ツリー/マスター/gaussian_processes
> Betancourt, M.、Girolami, M. (2015)。階層モデルのハミルトニアン モンテカルロ。で

### 熟語・専門語

- **ESS**: 有効サンプルサイズ。自己相関を考慮した独立サンプル相当数。

### 要約

- case_studies/principled_bayesian_workflow.html ベタンクール、M. (2020b)。

## Chunk 0709

### English（抽出4行）

> Current Trends in Bayesian Methodology with Applications, ed. S. K. Upadhyay, U. Singh, D.
> K. Dey, and A. Loganathan, 79–102.
> Blei, D. M., Kucukelbir, A., and McAuliﬀe, J. D. (2017). Variational inference: A review for
> statisticians. Journal of the American Statistical Association 112, 859–877.

### 日本語訳（自動翻訳）

> 応用を伴うベイジアン方法論の最新動向、編。 S. K. ウパディヤイ、U. シン、D.
> K. デイ、A. ロガナサン、79–102。
> Blei, D.M.、Kucukelbir, A.、および McAuli, J.D. (2017)。変分推論: のレビュー
> 統計学者。米国統計協会ジャーナル 112、859–877。

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- 応用を伴うベイジアン方法論の最新動向、編。

## Chunk 0710

### English（抽出4行）

> Blitzer, J., Dredze, M., and Pereira, F. (2007). Biographies, Bollywood, boom-boxes and blenders:
> Domain adaptation for sentiment classiﬁcation. In Proceedings of the 45th Annual Meeting of
> the Association of Computational Linguistics, 440–447.
> Box, G. E. P. (1980). Sampling and Bayes inference in scientiﬁc modelling and robustness. Journal

### 日本語訳（自動翻訳）

> Blitzer, J.、Dredze, M.、および Pereira, F. (2007)。伝記、ボリウッド、ラジカセとミキサー:
> 感情分類のためのドメイン適応。第45回年次総会議事録にて
> 計算言語学協会、440–447。
> ボックス、G.E.P. (1980)。科学的モデリングとロバスト性におけるサンプリングとベイズ推論。日記

### 熟語・専門語

- **ESS**: 有効サンプルサイズ。自己相関を考慮した独立サンプル相当数。

### 要約

- Blitzer, J.、Dredze, M.、および Pereira, F. (2007)。

## Chunk 0711

### English（抽出4行）

> of the Royal Statistical Society A 143, 383–430.
> Broadie, M. (2018).
> Two simple putting models in golf.
> statmodeling.stat.columbia.edu/

### 日本語訳（自動翻訳）

> 英国王立統計協会 A 143、383–430。
> ブローディ、M. (2018)。
> ゴルフにおける 2 つのシンプルなパッティング モデル。
> statmodeling.stat.columbia.edu/

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- 英国王立統計協会 A 143、383–430。

## Chunk 0712

### English（抽出4行）

> wp-content/uploads/2019/03/putt_models_20181017.pdf
> Bryan, J. (2017). Project-oriented workﬂow. www.tidyverse.org/blog/2017/12/workﬂow-vs-script
> Bürkner, P.-C. (2017). brms: An R Package for Bayesian multilevel models using Stan. Journal of
> Statistical Software 80, 1–28.

### 日本語訳（自動翻訳）

> wp-content/uploads/2019/03/putt_models_20181017.pdf
> ブライアン、J. (2017)。プロジェクト指向のワークフロー。 www.tidyverse.org/blog/2017/12/workflow-vs-script
> ビュルクナー、P.-C. （2017年）。 brms: Stan を使用したベイジアン マルチレベル モデル用の R パッケージ。のジャーナル
> 統計ソフトウェア 80、1 ～ 28。

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- wp-content/uploads/2019/03/putt_models_20181017.pdf ブライアン、J. (2017)。

## Chunk 0713

### English（抽出4行）

> Carpenter, B. (2017). Typical sets and the curse of dimensionality. Stan Case Studies 4. mc-stan.
> org/users/documentation/case-studies/curse-dims.html
> Carpenter, B. (2018). Predator-prey population dynamics: The Lotka-Volterra model in Stan. Stan
> Case Studies 5.

### 日本語訳（自動翻訳）

> カーペンター、B. (2017)。典型的な集合と次元の呪い。 Stan 導入事例 4. mc-stan.
> org/users/documentation/case-studies/curse-dims.html
> カーペンター、B. (2018)。捕食者と被食者の個体群動態: スタンのロトカ・ヴォルテラモデル。スタン
> ケーススタディ 5.

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- カーペンター、B. (2017)。

## Chunk 0714

### English（抽出4行）

> mc-stan.org/users/documentation/case-studies/lotka-volterra-predator-prey.
> html
> Carpenter, B., Gelman, A., Hoﬀman, M., Lee, D., Goodrich, B., Betancourt, M., Brubaker, M.,
> Guo, J., Li, P., and Riddell, A. (2017). Stan: A probabilistic programming language. Journal

### 日本語訳（自動翻訳）

> mc-stan.org/users/documentation/case-studies/lotka-volterra-predator-prey。
> html
> カーペンター、B.、ゲルマン、A.、ホフィマン、M.、リー、D.、グッドリッチ、B.、ベタンコート、M.、ブルベイカー、M.、
> Guo, J.、Li, P.、および Riddell, A. (2017)。 Stan: 確率的プログラミング言語。日記

### 熟語・専門語

- **probabilistic programming**: 確率的プログラミング。Stanなどで確率モデルをコードとして記述し推論する方法。

### 要約

- mc-stan.org/users/documentation/case-studies/lotka-volterra-predator-prey。

## Chunk 0715

### English（抽出4行）

> of Statistical Software 76 (1).
> Chen,
> C.,
> Li,

### 日本語訳（自動翻訳）

> 統計ソフトウェア 76 (1)。
> チェン、
> Cさん、
> 李さん、

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- 統計ソフトウェア 76 (1)。

## Chunk 0716

### English（抽出4行）

> O.,
> Barnett,
> A.,
> Su,

### 日本語訳（自動翻訳）

> お、
> バーネット
> A.、
> すーさん

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- お、 バーネット A.、 すーさん

## Chunk 0717

### English（抽出4行）

> J.,
> and Rudin,
> C. (2019).
> This looks like

### 日本語訳（自動翻訳）

> J.、
> そしてルーディン、
> C. (2019)。
> これは次のようです

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- J.、 そしてルーディン、 C. (2019)。

## Chunk 0718

### English（抽出4行）

> that:
> Deep learning for interpretable image recognition.
> 33rd Conference on Neu-
> ral Information Processing Systems.

### 日本語訳（自動翻訳）

> それは:
> 解釈可能な画像認識のための深層学習。
> 第33回ノイ・カンファレンス
> ラル情報処理システム。

### 熟語・専門語

- **ESS**: 有効サンプルサイズ。自己相関を考慮した独立サンプル相当数。

### 要約

- それは: 解釈可能な画像認識のための深層学習。

## Chunk 0719

### English（抽出4行）

> papers.nips.cc/paper/9095-this-looks-like-that-deep-
> learning-for-interpretable-image-recognition.pdf
> Chiu, W. A., Wright, F. A., and Rusyn, I. (2017). A tiered, Bayesian approach to estimating of
> population variability for regulatory decision-making. ALTEX 34, 377–388.

### 日本語訳（自動翻訳）

> papers.nips.cc/paper/9095-this-looks-like-that-deep-
> 解釈可能な画像認識の学習.pdf
> Chiu, W. A.、Wright, F. A.、および Rusyn, I. (2017)。を推定するための段階的なベイジアン アプローチ
> 規制上の意思決定における母集団の変動。アルテックス 34、377–388。

### 熟語・専門語

- **decision**: 意思決定。予測分布を損失・効用・行動選択へ接続する工程。

### 要約

- papers.nips.cc/paper/9095-this-looks-like-that-deep- 解釈可能な画像認識の学習.pdf Chiu, W. A.、Wright, F. A.、および Rusyn, I. (2017)。

## Chunk 0720

### English（抽出4行）

> Chung, Y., Rabe-Hesketh, S., Gelman, A., Liu, J. C., and Dorie, A. (2013). A non-degenerate
> penalized likelihood estimator for hierarchical variance parameters in multilevel models. Psy-
> chometrika 78, 685–709.
> Chung, Y., Rabe-Hesketh, S., Gelman, A., Liu, J. C., and Dorie, A. (2014). Nonsingular covariance

### 日本語訳（自動翻訳）

> Chung, Y.、Rabe-Hesketh, S.、Gelman, A.、Liu, J.C.、Dorie, A. (2013)。非退化
> マルチレベルモデルの階層分散パラメータに対するペナルティ付き尤度推定器。サイ～
> コメトリカ 78、685–709。
> Chung, Y.、Rabe-Hesketh, S.、Gelman, A.、Liu, J.C.、Dorie, A. (2014)。非特異共分散

### 熟語・専門語

- **likelihood**: 尤度。パラメータが与えられたときデータがどれだけ起こりやすいか。

### 要約

- Chung, Y.、Rabe-Hesketh, S.、Gelman, A.、Liu, J.C.、Dorie, A. (2013)。

## Chunk 0721

### English（抽出4行）

> estimation in linear mixed models through weakly informative priors. Journal of Educational
> and Behavioral Statistics 40, 136–157.
> Clayton, D. G. (1992). Models for the analysis of cohort and case-control studies with inaccurately
> measured exposures. In Statistical Models for Longitudinal Studies of Exposure and Health, ed.

### 日本語訳（自動翻訳）

> 情報量の少ない事前分布を介した線形混合モデルでの推定。教育ジャーナル
> および行動統計 40、136–157。
> クレイトン、D.G. (1992)。不正確なデータを含むコホート研究および症例対照研究の分析モデル
> 測定された露出。暴露と健康の長期的研究のための統計モデル、編。

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- 情報量の少ない事前分布を介した線形混合モデルでの推定。

## Chunk 0722

### English（抽出4行）

> J. H. Dwyer, M. Feinleib, P. Lippert, and H. Hoﬀmeister, 301–331. Oxford University Press.
> Cook, S., Gelman, A., and Rubin, D. B. (2006). Validation of software for Bayesian models using
> posterior quantiles. Journal of Computational and Graphical Statistics 15, 675–692.
> Daumé, H. (2009). Frustratingly easy domain adaptation. arxiv.org/abs/0907.1815

### 日本語訳（自動翻訳）

> J. H. Dwyer、M. Feinleib、P. Lippert、および H. Hoﬀmeister、301–331。オックスフォード大学出版局。
> Cook, S.、Gelman, A.、および Rubin, D.B. (2006)。を使用したベイジアン モデルのソフトウェアの検証
> 後分位数。 Journal of Computational and Graphical Statistics 15、675–692。
> ドーメ、H. (2009)。イライラするほど簡単なドメイン適応。 arxiv.org/abs/0907.1815

### 熟語・専門語

- **ESS**: 有効サンプルサイズ。自己相関を考慮した独立サンプル相当数。
- **validation**: 検証。モデルが目的・データ・外部知識に照らして妥当かを確認すること。

### 要約

- J. H. Dwyer、M. Feinleib、P. Lippert、および H. Hoﬀmeister、301–331。

## Chunk 0723

### English（抽出4行）

> Deming, W. E., and Stephan, F. F. (1940). On a least squares adjustment of a sampled frequency
> table when the expected marginal totals are known. Annals of Mathematical Statistics 11,
> 427–444.
> Devezer, B., Nardin, L. G., Baumgaertner, B., and Buzbas, E. O. (2019). Scientiﬁc discovery in a

### 日本語訳（自動翻訳）

> デミング、W.E.、ステファン、F.F. (1940)。サンプリング周波数の最小二乗調整について
> 予想される限界合計がわかっている場合の表。数学統計年報 11、
> 427–444。
> Devezer, B.、Nardin, L. G.、Baumgaertner, B.、および Buzbas, E. O. (2019)。科学的発見

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- デミング、W.E.、ステファン、F.F. (1940)。

## Chunk 0724

### English（抽出4行）

> model-centric framework: Reproducibility, innovation, and epistemic diversity. PLoS One 14,
> e0216125.
> Devezer, B., Navarro, D. J., Vanderkerckhove, J., and Buzbas, E. O. (2020). The case for formal
> methodology in scientiﬁc reform. doi.org/10.1101/2020.04.26.048306

### 日本語訳（自動翻訳）

> モデル中心のフレームワーク: 再現性、革新性、認識論的多様性。 PLoS ワン 14、
> e0216125。
> Devezer, B.、Navarro, D.J.、Vanderkerckhove, J.、および Buzbas, E.O. (2020)。公式の場合
> 科学改革における方法論。 doi.org/10.1101/2020.04.26.048306

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- モデル中心のフレームワーク: 再現性、革新性、認識論的多様性。

## Chunk 0725

### English（抽出4行）

> Dragicevic, P., Jansen, Y., Sarma, A., Kay, M., and Chevalier, F. (2019). Increasing the trans-
> parency of research papers with explorable multiverse analyses. Proceedings of the 2019 CHI
> Conference on Human Factors in Computing Systems, paper no. 65.
> Efron, B. (2013).

### 日本語訳（自動翻訳）

> ドラギセビッチ、P.、ヤンセン、Y.、サルマ、A.、ケイ、M.、シュバリエ、F. (2019)。トランスの増加
> 探索可能な多元世界分析を含む研究論文の親。 2019 CHI の議事録
> コンピューティング システムにおけるヒューマン ファクターに関する会議、論文 No. 65.
> エフロン、B. (2013)。

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- ドラギセビッチ、P.、ヤンセン、Y.、サルマ、A.、ケイ、M.、シュバリエ、F. (2019)。

## Chunk 0726

### English（抽出4行）

> Estimation and accuracy after model selection.
> Journal of the American
> Statistical Association 109, 991–1007.
> Finkel, J. R., and Manning, C. D. (2009). Hierarchical Bayesian domain adaptation. In Proceedings

### 日本語訳（自動翻訳）

> モデル選択後の推定と精度。
> ジャーナル・オブ・ザ・アメリカン
> 統計協会 109、991–1007。
> フィンケル、J.R.、マニング、C.D. (2009)。階層的ベイジアン ドメイン適応。議事中

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- モデル選択後の推定と精度。

## Chunk 0727

### English（抽出4行）

> of Human Language Technologies: The 2009 Annual Conference of the North American Chapter
> of the Association for Computational Linguistics, 602–610.
> Fithian, W., Taylor, J., Tibshirani, R., and Tibshirani, R. J. (2015). Selective sequential model
> selection. arxiv.org/pdf/1512.02565.pdf

### 日本語訳（自動翻訳）

> 人間の言語技術の研究: 北米支部の 2009 年年次会議
> 計算言語学協会、602–610。
> Fithian, W.、Taylor, J.、Tibshirani, R.、および Tibshirani, R. J. (2015)。選択的逐次モデル
> 選択。 arxiv.org/pdf/1512.02565.pdf

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- 人間の言語技術の研究: 北米支部の 2009 年年次会議 計算言語学協会、602–610。

## Chunk 0728

### English（抽出4行）

> Flaxman, S., Mishra, S., Gandy, A., et al. (2020). Estimating the eﬀects of non-pharmaceutical
> interventions on COVID-19 in Europe. Nature 584, 257–261. Data and code at github.com/
> ImperialCollegeLondon/covid19model
> Fuglstad, G. A., Simpson, D., Lindgren, F., and Rue, H. (2019). Constructing priors that penalize

### 日本語訳（自動翻訳）

> Flaxman, S.、Mishra, S.、Gandy, A. 他（2020年）。非医薬品の影響の推定
> ヨーロッパにおける新型コロナウイルス感染症への介入。自然 584、257–261。データとコードは github.com/ にあります
> インペリアルカレッジロンドン/covid19モデル
> Fuglstad, G. A.、Simpson, D.、Lindgren, F.、および Rue, H. (2019)。ペナルティを与える事前分布の構築

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- Flaxman, S.、Mishra, S.、Gandy, A. 他（2020年）。

## Chunk 0729

### English（抽出4行）

> the complexity of Gaussian random ﬁelds. Journal of the American Statistical Association 114,
> 445–452.
> Gabry, J., et al. (2020a). rstanarm: Bayesian applied regression modeling via Stan, version 2.19.3.
> cran.r-project.org/package=rstanarm

### 日本語訳（自動翻訳）

> ガウスランダム場の複雑さ。米国統計協会ジャーナル 114、
> 445–452。
> ガブリー、J.、他。 (2020a)。 rstanarm: Stan バージョン 2.19.3 によるベイズ適用回帰モデリング。
> cran.r-project.org/package=rstanarm

### 熟語・専門語

- **ESS**: 有効サンプルサイズ。自己相関を考慮した独立サンプル相当数。

### 要約

- ガウスランダム場の複雑さ。

## Chunk 0730

### English（抽出4行）

> Gabry, J., et al. (2020b). bayesplot: Plotting for Bayesian models, version 1.7.2. cran.r-project.
> org/package=bayesplot
> Gabry, J., Simpson, D., Vehtari, A., Betancourt, M., and Gelman, A. (2019). Visualization in
> Bayesian workﬂow (with discussion and rejoinder). Journal of the Royal Statistical Society A

### 日本語訳（自動翻訳）

> ガブリー、J.、他。 (2020b)。 Bayesplot: ベイジアン モデルのプロット、バージョン 1.7.2。 cran.r-プロジェクト。
> org/package=bayesplot
> Gabry, J.、Simpson, D.、Vehtari, A.、Betancourt, M.、Gelman, A. (2019)。視覚化
> ベイジアン ワークフロー (ディスカッションと再参加あり)。王立統計協会ジャーナル A

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- ガブリー、J.、他。

## Chunk 0731

### English（抽出4行）

> 182, 389–441.
> Gelman, A., Bois, F. Y., and Jiang, J. (1996).
> Physiological pharmacokinetic analysis using
> population modeling and informative prior distributions. Journal of the American Statistical

### 日本語訳（自動翻訳）

> 182、389–441。
> Gelman, A.、Bois, F.Y.、および Jiang, J. (1996)。
> を用いた生理学的薬物動態解析
> 人口モデリングと有益な事前分布。アメリカ統計ジャーナル

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

> アソシエーション 91、1400 ～ 1412 年。
> ゲルマン、A. (2003)。
> 探索的データ分析と適合度のベイジアン定式化
> テスト中。国際統計レビュー 71、369–382。

### 熟語・専門語

- **ESS**: 有効サンプルサイズ。自己相関を考慮した独立サンプル相当数。

### 要約

- アソシエーション 91、1400 ～ 1412 年。

## Chunk 0733

### English（抽出4行）

> Gelman, A. (2004). Parameterization and Bayesian modeling. Journal of the American Statistical
> Association 99, 537–545.
> Gelman, A. (2011).
> Expanded graphical models:

### 日本語訳（自動翻訳）

> ゲルマン、A. (2004)。パラメータ化とベイズ モデリング。アメリカ統計ジャーナル
> アソシエーション 99、537–545。
> ゲルマン、A. (2011)。
> 拡張されたグラフィカル モデル:

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- ゲルマン、A. (2004)。

## Chunk 0734

### English（抽出4行）

> Inference, model comparison, model
> checking, fake-data debugging, and model understanding. www.stat.columbia.edu/~gelman/
> presentations/ggr2handout.pdf
> Gelman, A. (2014). How do we choose our default methods? In Past, Present, and Future of

### 日本語訳（自動翻訳）

> 推論、モデル比較、モデル
> チェック、偽データのデバッグ、モデルの理解。 www.stat.columbia.edu/~gelman/
> プレゼンテーション/ggr2handout.pdf
> ゲルマン、A. (2014)。デフォルトのメソッドはどのように選択すればよいでしょうか?過去、現在、そして未来において

### 熟語・専門語

- **model comparison**: モデル比較。LOO-CVなどで複数モデルの予測性能や弱点を比較すること。

### 要約

- 推論、モデル比較、モデル チェック、偽データのデバッグ、モデルの理解。

## Chunk 0735

### English（抽出4行）

> Statistical Science, ed. X. Lin, C. Genest, D. L. Banks, G. Molenberghs, D. W. Scott, and J. L.
> Wang. London: CRC Press.
> Gelman, A. (2019). Model building and expansion for golf putting. Stan Case Studies 6. mc-stan.
> org/users/documentation/case-studies/golf.html

### 日本語訳（自動翻訳）

> 統計科学編X. リン、C. ジェネスト、D. L. バンクス、G. モレンバーグス、D. W. スコット、J. L.
> 王さん。ロンドン：CRCプレス。
> ゲルマン、A. (2019)。ゴルフパッティングのモデル構築と拡張。 Stan 導入事例 6. mc-stan.
> org/users/documentation/case-studies/golf.html

### 熟語・専門語

- **ESS**: 有効サンプルサイズ。自己相関を考慮した独立サンプル相当数。
- **model building**: モデル構築。仮定・データ構造・prior・likelihoodを組み合わせる工程。

### 要約

- 統計科学編X. リン、C. ジェネスト、D. L. バンクス、G. モレンバーグス、D. W. スコット、J. L. 王さん。

## Chunk 0736

### English（抽出4行）

> Gelman, A., et al. (2020).
> Prior choice recommendations.
> github.com/stan-dev/stan/wiki/
> Prior-Choice-Recommendations

### 日本語訳（自動翻訳）

> ゲルマン、A.ら。 （2020年）。
> 事前の選択に関する推奨事項。
> github.com/stan-dev/stan/wiki/
> 事前の選択 - 推奨事項

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- ゲルマン、A.ら。

## Chunk 0737

### English（抽出4行）

> Gelman, A., and Azari, J. (2017). 19 things we learned from the 2016 election (with discussion).
> Statistics and Public Policy 4, 1–10.
> Gelman, A., Carlin, J. B., Stern, H. S., Dunson, D. B., Vehtari, A., and Rubin, D. B. (2013).
> Bayesian Data Analysis, third edition. London: CRC Press.

### 日本語訳（自動翻訳）

> ゲルマン、A.、アザリ、J. (2017)。 2016 年の選挙から学んだ 19 のこと (ディスカッション付き)。
> 統計と公共政策 4、1-10。
> Gelman, A.、Carlin, J.B.、Stern, H.S.、Dunson, D.B.、Vehtari, A.、および Rubin, D.B. (2013)。
> ベイズデータ分析、第 3 版。ロンドン：CRCプレス。

### 熟語・専門語

- **ESS**: 有効サンプルサイズ。自己相関を考慮した独立サンプル相当数。

### 要約

- ゲルマン、A.、アザリ、J. (2017)。

## Chunk 0738

### English（抽出4行）

> Gelman, A., and Hill, J. (2007). Data Analysis Using Regression and Multilevel/Hierarchical
> Models. Cambridge University Press.
> Gelman, A., Hill, J., and Vehtari, A. (2020). Regression and Other Stories. Cambridge University
> Press.

### 日本語訳（自動翻訳）

> ゲルマン、A.、ヒル、J. (2007)。回帰およびマルチレベル/階層を使用したデータ分析
> モデル。ケンブリッジ大学出版局。
> ゲルマン、A.、ヒル、J.、およびヴェフタリ、A. (2020)。回帰とその他の話。ケンブリッジ大学
> を押します。

### 熟語・専門語

- **ESS**: 有効サンプルサイズ。自己相関を考慮した独立サンプル相当数。

### 要約

- ゲルマン、A.、ヒル、J. (2007)。

## Chunk 0739

### English（抽出4行）

> Gelman, A., Hill, J., and Yajima, M. (2012). Why we (usually) don’t have to worry about multiple
> comparisons. Journal of Research on Educational Eﬀectiveness 5, 189–211.
> Gelman, A., Hullman, J., Wlezien, C., and Morris, G. E. (2020). Information, incentives, and goals
> in election forecasts. Judgment and Decision Making 15, 863–880.

### 日本語訳（自動翻訳）

> ゲルマン A.、ヒル J.、矢島 M. (2012)。なぜ（通常は）複数のことを心配する必要がないのか
> 比較。教育効果に関する研究ジャーナル 5、189–211。
> ゲルマン、A.、ハルマン、J.、Wlezien、C.、およびモリス、G. E. (2020)。情報、インセンティブ、目標
> 選挙予想では。判断と意思決定 15、863–880。

### 熟語・専門語

- **ESS**: 有効サンプルサイズ。自己相関を考慮した独立サンプル相当数。
- **decision**: 意思決定。予測分布を損失・効用・行動選択へ接続する工程。

### 要約

- ゲルマン A.、ヒル J.、矢島 M. (2012)。

## Chunk 0740

### English（抽出4行）

> Gelman, A., and Loken, E. (2013). The garden of forking paths: Why multiple comparisons can be a
> problem, even when there is no “ﬁshing expedition” or “p-hacking” and the research hypothesis
> was posited ahead of time. www.stat.columbia.edu/~gelman/research/unpublished/forking.pdf
> Gelman, A., Meng, X. L., and Stern, H. S. (1996). Posterior predictive assessment of model ﬁtness

### 日本語訳（自動翻訳）

> ゲルマン、A.、ローケン、E. (2013)。分岐点の庭: 複数の比較がなぜ重要になるのか
> 「釣り遠征」や「ハッキング」がなく、研究仮説がない場合でも、問題は発生します。
> 事前に設置されていました。 www.stat.columbia.edu/~gelman/research/unpublished/forking.pdf
> ゲルマン、A.、メン、X.L.、およびスターン、H.S. (1996)。モデルの適合性の事後予測評価

### 熟語・専門語

- **posterior predictive**: 事後予測。推定後のモデルが観測データの特徴を再現できるかを見る診断。
- **ESS**: 有効サンプルサイズ。自己相関を考慮した独立サンプル相当数。

### 要約

- ゲルマン、A.、ローケン、E. (2013)。

## Chunk 0741

### English（抽出4行）

> via realized discrepancies (with discussion). Statistica Sinica 6, 733–807.
> Gelman, A., Simpson, D., and Betancourt, M. (2017). The prior can often only be understood in
> the context of the likelihood. Entropy 19, 555.
> Gelman, A., Stevens, M., and Chan, V. (2003). Regression modeling and meta-analysis for decision

### 日本語訳（自動翻訳）

> 認識された矛盾を介して（議論あり）。中国統計 6、733–807。
> ゲルマン、A.、シンプソン、D.、およびベタンコート、M. (2017)。事前計算は多くの場合、次の方法でのみ理解できます。
> 可能性のコンテキスト。エントロピー 19、555。
> ゲルマン、A.、スティーブンス、M.、チャン、V. (2003)。意思決定のための回帰モデリングとメタ分析

### 熟語・専門語

- **likelihood**: 尤度。パラメータが与えられたときデータがどれだけ起こりやすいか。
- **ESS**: 有効サンプルサイズ。自己相関を考慮した独立サンプル相当数。
- **decision**: 意思決定。予測分布を損失・効用・行動選択へ接続する工程。

### 要約

- 認識された矛盾を介して（議論あり）。

## Chunk 0742

### English（抽出4行）

> making: A cost-beneﬁt analysis of a incentives in telephone surveys. Journal of Business and
> Economic Statistics 21, 213–225.
> Gharamani, Z., Steinruecken, C., Smith, E., Janz, E., and Peharz, R. (2019). The Automatic
> Statistician: An artiﬁcial intelligence for data science. www.automaticstatistician.com/index

### 日本語訳（自動翻訳）

> 作成: 電話調査におけるインセンティブの費用便益分析。ビジネスジャーナルと
> 経済統計 21、213–225。
> Gharamani, Z.、Steinruecken, C.、Smith, E.、Janz, E.、および Peharz, R. (2019)。オートマチック
> 統計学者: データサイエンス用の人工知能。 www.automaticstatistician.com/index

### 熟語・専門語

- **ESS**: 有効サンプルサイズ。自己相関を考慮した独立サンプル相当数。

### 要約

- 作成: 電話調査におけるインセンティブの費用便益分析。

## Chunk 0743

### English（抽出4行）

> Ghitza, Y., and Gelman, A. (2020). Voter registration databases and MRP: Toward the use of large
> scale databases in public opinion research. Political Analysis 28, 507–531.
> Giordano, R. (2018). StanSensitivity. github.com/rgiordan/StanSensitivity
> Giordano, R., Broderick, T., and Jordan, M. I. (2018). Covariances, robustness, and variational

### 日本語訳（自動翻訳）

> ギッツァ、Y.、ゲルマン、A. (2020)。有権者登録データベースとMRP：大規模な利用に向けて
> 世論調査におけるデータベースのスケールアップ。政治分析 28、507–531。
> ジョルダーノ、R. (2018)。スタン感度。 github.com/rgiordan/StanSensitivity
> ジョルダーノ、R.、ブロデリック、T.、ジョーダン、M.I. (2018)。共分散、ロバスト性、および変分

### 熟語・専門語

- **ESS**: 有効サンプルサイズ。自己相関を考慮した独立サンプル相当数。

### 要約

- ギッツァ、Y.、ゲルマン、A. (2020)。

## Chunk 0744

### English（抽出4行）

> Bayes. Journal of Machine Learning Research 19, 1981–2029.
> Goel, P. K., and DeGroot, M. H. (1981). Information about hyperparameters in hierarchical models.
> Journal of the American Statistical Association 76, 140–147.
> Grinsztajn, L., Semenova, E., Margossian, C. C., and Riou, J. (2020). Bayesian workﬂow for dis-

### 日本語訳（自動翻訳）

> ベイズ。機械学習研究ジャーナル 19、1981–2029。
> ゴエル、P.K.、デグルート、M.H. (1981)。階層モデルのハイパーパラメータに関する情報。
> 米国統計協会ジャーナル、76、140–147。
> Grinsztajn, L.、Semenova, E.、Margossian, C.C.、および Riou, J. (2020)。分析のためのベイジアン ワークフロー

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

> Stan でのトランスミッション モデリングを容易にします。 mc-stan.org/users/documentation/case-studies/boarding_
> school_case_study.html
> Grolemund、G.、および Wickham、H. (2017)。データサイエンスのR。カリフォルニア州セバストポル：オライリー・メディア。
> ガニング、D. (2017)。説明可能な人工知能 (xai)。米国国防先端研究

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- Stan でのトランスミッション モデリングを容易にします。

## Chunk 0746

### English（抽出4行）

> Projects Agency (DARPA) Program.
> Henderson, C. R. (1950). Estimation of genetic parameters (abstract). Annals of Mathematical
> Statistics 21, 309–310.
> Hill, J. L. (2011). Bayesian nonparametric modeling for causal inference. Journal of Computational

### 日本語訳（自動翻訳）

> プロジェクト庁 (DARPA) プログラム。
> ヘンダーソン、C.R. (1950)。遺伝的パラメーターの推定 (要約)。数学年報
> 統計 21、309–310。
> J.L. ヒル (2011)。因果推論のためのベイズ ノンパラメトリック モデリング。計算ジャーナル

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- プロジェクト庁 (DARPA) プログラム。

## Chunk 0747

### English（抽出4行）

> and Graphical Statistics 20, 217–240.
> Hodges, J. S., and Reich, B. J. (2010). Adding spatially-correlated errors can mess up the ﬁxed
> eﬀect you love. American Statistician 64, 325–334.
> Hoﬀman, M., and Ma, Y. (2020). Black-box variational inference as a parametric approximation

### 日本語訳（自動翻訳）

> およびグラフ統計 20、217–240。
> J. S. ホッジスおよび B. J. ライヒ (2010)。空間相関エラーを追加すると、修正されたエラーが台無しになる可能性があります
> お気に入りのエフェクト。アメリカの統計学者、64、325–334。
> Hoﬀman, M.、および Ma, Y. (2020)。パラメトリック近似としてのブラックボックス変分推論

### 熟語・専門語

- **ESS**: 有効サンプルサイズ。自己相関を考慮した独立サンプル相当数。

### 要約

- およびグラフ統計 20、217–240。

## Chunk 0748

### English（抽出4行）

> to Langevin dynamics. Proceedings of Machine Learning and Systems, in press.
> Hunt, A., and Thomas, D. (1999). The Pragmatic Programmer. Addison-Wesley.
> Hwang, Y., Tong, A. and Choi, J. (2016). The Automatic Statistician: A relational perspective.
> ICML 2016: Proceedings of the 33rd International Conference on Machine Learning.

### 日本語訳（自動翻訳）

> ランジュバン力学へ。機械学習とシステムの論文集、出版中。
> ハント A. およびトーマス D. (1999)。実践的なプログラマー。アディソン・ウェスリー。
> Hwang, Y.、Tong, A.、Choi, J. (2016)。自動統計学者: 関係性の観点。
> ICML 2016: 第 33 回機械学習国際会議の議事録。

### 熟語・専門語

- **ESS**: 有効サンプルサイズ。自己相関を考慮した独立サンプル相当数。

### 要約

- ランジュバン力学へ。

## Chunk 0749

### English（抽出4行）

> Jacquez, J. A. (1972). Compartmental Analysis in Biology and Medicine. Elsevier.
> Kale, A., Kay, M., and Hullman, J. (2019).
> Decision-making under uncertainty in research
> synthesis: Designing for the garden of forking paths. Proceedings of the 2019 CHI Conference

### 日本語訳（自動翻訳）

> ジャック、J.A. (1972)。生物学と医学におけるコンパートメント分析。エルゼビア。
> ケール、A.、ケイ、M.、およびハルマン、J. (2019)。
> 研究における不確実性の下での意思決定
> 合成: 分かれ道の庭のデザイン。 2019 CHI カンファレンスの議事録

### 熟語・専門語

- **uncertainty**: 不確実性。観測・パラメータ・モデル構造・意思決定に残る曖昧さ。
- **decision**: 意思決定。予測分布を損失・効用・行動選択へ接続する工程。

### 要約

- ジャック、J.A. (1972)。

## Chunk 0750

### English（抽出4行）

> on Human Factors in Computing Systems, paper no. 202.
> Kamary, K., Mengersen, K., Robert, C. P., and Rousseau, J. (2019). Testing hypotheses via a
> mixture estimation model. arxiv.org/abs/1412.2044
> Katz,

### 日本語訳（自動翻訳）

> コンピューティング システムにおけるヒューマン ファクターに関する論文 No. 202.
> カマリー、K.、メンガーセン、K.、ロバート、C.P.、およびルソー、J. (2019)。仮説を検証する
> 混合物推定モデル。 arxiv.org/abs/1412.2044
> カッツ、

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- コンピューティング システムにおけるヒューマン ファクターに関する論文 No. 202. カマリー、K.、メンガーセン、K.、ロバート、C.P.、およびルソー、J. (2019)。

## Chunk 0751

### English（抽出4行）

> J. (2016).
> Who will be president?
> www.nytimes.com/interactive/2016/upshot/
> presidential-polls-forecast.html

### 日本語訳（自動翻訳）

> J. (2016)。
> 誰が大統領になるのでしょうか？
> www.nytimes.com/interactive/2016/upshot/
> 大統領-世論調査-予測.html

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- J. (2016)。

## Chunk 0752

### English（抽出4行）

> Kay, M. (2020a). ggdist: Visualizations of distributions and uncertainty. R package version 2.2.0.
> mjskay.github.io/ggdist. doi:10.5281/zenodo.3879620.
> Kay, M. (2020b). tidybayes: Tidy data and geoms for Bayesian models. R package version 2.1.1.
> mjskay.github.io/tidybayes. doi:10.5281/zenodo.1308151.

### 日本語訳（自動翻訳）

> ケイ、M. (2020a)。 ggdist: 分布と不確実性の視覚化。 R パッケージ バージョン 2.2.0。
> mjskay.github.io/ggdist.土井：10.5281/zenodo.3879620。
> ケイ、M. (2020b)。 tinybayes: ベイジアン モデルのデータとジオムを整理します。 R パッケージ バージョン 2.1.1。
> mjskay.github.io/tidybayes.土井:10.5281/zenodo.1308151。

### 熟語・専門語

- **uncertainty**: 不確実性。観測・パラメータ・モデル構造・意思決定に残る曖昧さ。

### 要約

- ケイ、M. (2020a)。

## Chunk 0753

### English（抽出4行）

> Kennedy, L., Simpson, D., and Gelman, A. (2019).
> The experiment is just as important as
> the likelihood in understanding the prior: A cautionary note on robust cognitive modeling.
> Computational Brain and Behavior 2, 210–217.

### 日本語訳（自動翻訳）

> ケネディ、L.、シンプソン、D.、ゲルマン、A. (2019)。
> 実験はそれと同じくらい重要です
> 事前の理解の可能性: 堅牢な認知モデリングに関する注意事項。
> 計算脳と行動 2、210–217。

### 熟語・専門語

- **likelihood**: 尤度。パラメータが与えられたときデータがどれだけ起こりやすいか。

### 要約

- ケネディ、L.、シンプソン、D.、ゲルマン、A. (2019)。

## Chunk 0754

### English（抽出4行）

> Kerman, J., and Gelman, A. (2004). Fully Bayesian computing. www.stat.columbia.edu/~gelman/
> research/unpublished/fullybayesiancomputing-nonblinded.pdf
> Kerman, J., and Gelman, A. (2007). Manipulating and summarizing posterior simulations using
> random variable objects. Statistics and Computing 17, 235–244.

### 日本語訳（自動翻訳）

> Kerman, J. および Gelman, A. (2004)。完全なベイジアン コンピューティング。 www.stat.columbia.edu/~gelman/
> 研究/未公開/完全ベイジアンコンピューティング-非盲検.pdf
> Kerman, J. および Gelman, A. (2007)。を使用した事後シミュレーションの操作と要約
> 確率変数オブジェクト。統計とコンピューティング 17、235–244。

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- Kerman, J. および Gelman, A. (2004)。

## Chunk 0755

### English（抽出4行）

> Kucukelbir, A., Tran, D., Ranganath, R., Gelman, A., and Blei, D. M. (2017). Automatic diﬀeren-
> tiation variational inference. Journal of Machine Learning Research 18, 1–45.
> Kumar, R., Carroll, C., Hartikainen, A., and Martin, O. A. (2019).
> ArviZ a uniﬁed library

### 日本語訳（自動翻訳）

> Kucukelbir, A.、Tran, D.、Ranganath, R.、Gelman, A.、および Blei, D.M. (2017)。自動差動
> 関係変分推論。機械学習研究ジャーナル 18、1–45。
> Kumar, R.、Carroll, C.、Hartikainen, A.、Martin, O. A. (2019)。
> ArviZ 統合ライブラリ

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- Kucukelbir, A.、Tran, D.、Ranganath, R.、Gelman, A.、および Blei, D.M. (2017)。

## Chunk 0756

### English（抽出4行）

> for exploratory analysis of Bayesian models in Python. Journal of Open Source Software,
> doi:10.21105/joss.01143.
> Lambert, B., and Vehtari, A. (2020). R∗: A robust MCMC convergence diagnostic with uncertainty
> using gradient-boosted machines. arxiv.org/abs/2003.07900

### 日本語訳（自動翻訳）

> Python でのベイジアン モデルの探索的分析用。オープンソース ソフトウェアジャーナル、
> 土井:10.21105/joss.01143。
> ランバート、B.、およびヴェタリ、A. (2020)。 R∗: 不確実性のある堅牢な MCMC 収束診断
> 勾配ブーストされたマシンを使用します。 arxiv.org/abs/2003.07900

### 熟語・専門語

- **uncertainty**: 不確実性。観測・パラメータ・モデル構造・意思決定に残る曖昧さ。

### 要約

- Python でのベイジアン モデルの探索的分析用。

## Chunk 0757

### English（抽出4行）

> Lee, M. D., Criss, A. H., Devezer, B., Donkin, C., Etz, A., Leite, F. P., Matzke, D., Rouder, J. N.,
> Trueblood, J. S., White, C. N., and Vandekerckhove, J. (2019). Robust modeling in cognitive
> science. Computational Brain and Behavior 2, 141–153.
> Lin, C. Y., Gelman, A., Price, P. N., and Krantz, D. H. (1999). Analysis of local decisions using

### 日本語訳（自動翻訳）

> Lee, M.D.、Criss, A.H.、Devezer, B.、Donkin, C.、Etz, A.、Leite, F.P.、Matzke, D.、Rouder, J.N.、
> J. S. トゥルーブラッド、C. N. ホワイト、J. ヴァンデケルクホーフ (2019)。コグニティブ分野における堅牢なモデリング
> 科学。計算脳と行動 2、141–153。
> Lin, C.Y.、Gelman, A.、Price, P.N.、および Krantz, D.H. (1999)。を使用したローカル意思決定の分析

### 熟語・専門語

- **decision**: 意思決定。予測分布を損失・効用・行動選択へ接続する工程。

### 要約

- Lee, M.D.、Criss, A.H.、Devezer, B.、Donkin, C.、Etz, A.、Leite, F.P.、Matzke, D.、Rouder, J.N.、 J. S. トゥルーブラッド、C. N. ホワイト、J…

## Chunk 0758

### English（抽出4行）

> hierarchical modeling, applied to home radon measurement and remediation (with discussion).
> Statistical Science 14, 305–337.
> Lindley, D. V. (1956). On a measure of the information provided by an experiment. Annals of
> Mathematical Statistics 27, 986–1005.

### 日本語訳（自動翻訳）

> 階層モデリング、家庭用ラドン測定と修復に適用（ディスカッション付き）。
> 統計科学 14、305–337。
> リンドリー、DV (1956)。実験によって得られる情報の尺度について。の年代記
> 数学統計学 27、986–1005。

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- 階層モデリング、家庭用ラドン測定と修復に適用（ディスカッション付き）。

## Chunk 0759

### English（抽出4行）

> Lins, L., Koop, D., Anderson, E. W., Callahan, S. P., Santos, E., Scheidegger, C. E., Freire, J.,
> and Silva, C. T. (2008). Examining statistics of workﬂow evolution provenance: A ﬁrst study.
> In Scientiﬁc and Statistical Database Management, SSDBM 2008, ed. B. Ludäscher and N.
> Mamoulis, 573–579. Berlin: Springer.

### 日本語訳（自動翻訳）

> リンズ、L.、クープ、D.、アンダーソン、E.W.、カラハン、S.P.、サントス、E.、シャイデッガー、C.E.、フレイレ、J.、
> およびシルバ、C.T. (2008)。ワークフローの進化の起源に関する統計の調査: 最初の調査。
> 『科学的および統計的データベース管理』、SSDBM 2008、編。 B. ルーデッシャーと N.
> マムーリス、573–579。ベルリン：シュプリンガー。

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- リンズ、L.、クープ、D.、アンダーソン、E.W.、カラハン、S.P.、サントス、E.、シャイデッガー、C.E.、フレイレ、J.、 およびシルバ、C.T. (2008)。

## Chunk 0760

### English（抽出4行）

> Linzer, D. A. (2013). Dynamic Bayesian forecasting of presidential elections in the states. Journal
> of the American Statistical Association 108, 124–134.
> Liu, Y., Harding, A., Gilbert, R., and Journel, A. G. (2005).
> A workﬂow for multiple-point

### 日本語訳（自動翻訳）

> D.A. リンザー (2013)。各州の大統領選挙の動的なベイジアン予測。日記
> 米国統計協会の 108、124–134。
> Liu, Y.、Harding, A.、Gilbert, R.、および Journel, A.G. (2005)。
> 複数点のワークフロー

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- D.A. リンザー (2013)。

## Chunk 0761

### English（抽出4行）

> geostatistical simulation. In Geostatistics Banﬀ2004, ed. O. Leuangthong and C. V. Deutsch.
> Dordrecht: Springer.
> Loftus, J. (2015). Selective inference after cross-validation. arxiv.org/pdf/1511.08866.pdf
> Long, J. S. (2009). The Workﬂow of Data Analysis Using Stata. London: CRC Press.

### 日本語訳（自動翻訳）

> 地球統計シミュレーション。 『Geostatistics Banﬀ2004 編』 O. Leuangthong と C. V. Deutsch。
> ドルドレヒト: スプリンガー。
> ロフタス、J. (2015)。相互検証後の選択的推論。 arxiv.org/pdf/1511.08866.pdf
> ロング、J.S. (2009)。 Stata を使用したデータ分析のワークフロー。ロンドン：CRCプレス。

### 熟語・専門語

- **ESS**: 有効サンプルサイズ。自己相関を考慮した独立サンプル相当数。
- **validation**: 検証。モデルが目的・データ・外部知識に照らして妥当かを確認すること。

### 要約

- 地球統計シミュレーション。

## Chunk 0762

### English（抽出4行）

> Mallows, C. L. (1973). Some comments on Cp. Technometrics 15, 661–675.
> Margossian, C. C, and Gelman, A (2020).
> Bayesian Model of Planetary Motion: exploring
> ideas for a modeling workﬂow when dealing with ordinary diﬀerential equations and mul-

### 日本語訳（自動翻訳）

> マローズ、C.L. (1973)。 Cp に関するいくつかのコメント。テクノメトリクス 15、661–675。
> マルゴシアン、C.C、ゲルマン、A (2020)。
> 惑星運動のベイジアン モデル: 探索
> 常微分方程式と乗数を扱う際のモデリング ワークフローのアイデア

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- マローズ、C.L. (1973)。

## Chunk 0763

### English（抽出4行）

> timodality.
> Technical Report, https://github.com/stan-dev/example-models/tree/case-study/
> planet/knitr/planetary_motion
> Margossian, C. C., Vehtari, A., Simpson, D., and Agrawal, R. (2020a). Hamiltonian Monte Carlo

### 日本語訳（自動翻訳）

> 時流性。
> 技術レポート、https://github.com/stan-dev/example-models/tree/case-study/
> 惑星/ニット/planetary_motion
> Margossian, C.C.、Vehtari, A.、Simpson, D.、および Agrawal, R. (2020a)。ハミルトニアン モンテカルロ法

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- 時流性。

## Chunk 0764

### English（抽出4行）

> using an adjoint-diﬀerentiated Laplace approximation: Bayesian inference for latent Gaussian
> models and beyond. Advances in Neural Information Processing Systems 34, page to appear,
> arXiv:2004.12550
> Margossian, C. C., Vehtari, A., Simpson, D., and Agrawal, R. (2020b). Approximate Bayesian

### 日本語訳（自動翻訳）

> 随伴微分ラプラス近似の使用: 潜在ガウスに対するベイズ推論
> モデルとその先へ。神経情報処理システムの進歩 34、表示されるページ、
> arXiv:2004.12550
> Margossian, C.C.、Vehtari, A.、Simpson, D.、および Agrawal, R. (2020b)。近似ベイジアン

### 熟語・専門語

- **Bayesian inference**: ベイズ推論。事前分布と尤度から事後分布を計算する中核処理。
- **ESS**: 有効サンプルサイズ。自己相関を考慮した独立サンプル相当数。
- **approximate**: 近似。速度や扱いやすさのため、正確な推論・モデルを緩めること。

### 要約

- 随伴微分ラプラス近似の使用: 潜在ガウスに対するベイズ推論 モデルとその先へ。

## Chunk 0765

### English（抽出4行）

> inference for latent Gaussian models in Stan. Stan Con 2020, researchgate.net/publication/
> 343690329_Approximate_Bayesian_inference_for_latent_Gaussian_models_in_Stan
> Mayo, D. (2018). Statistical Inference as Severe Testing: How to Get Beyond the Statistics Wars.
> Cambridge University Press.

### 日本語訳（自動翻訳）

> Stan の潜在ガウス モデルの推論。 Stan Con 2020、researchgate.net/publication/
> 343690329_Stan の潜在ガウスモデルの近似ベイジアン推論
> メイヨー、D. (2018)。厳しいテストとしての統計的推論: 統計戦争を乗り越える方法。
> ケンブリッジ大学出版局。

### 熟語・専門語

- **ESS**: 有効サンプルサイズ。自己相関を考慮した独立サンプル相当数。
- **approximate**: 近似。速度や扱いやすさのため、正確な推論・モデルを緩めること。

### 要約

- Stan の潜在ガウス モデルの推論。

## Chunk 0766

### English（抽出4行）

> McConnell, S. (2004). Code Complete, second edition. Microsoft Press.
> Meng, X. L., and van Dyk, D. A. (2001). The art of data augmentation. Journal of Computational
> and Graphical Statistics 10, 1–50.
> Merkle, E. C., Furr, D., and Rabe-Hesketh, S. (2019). Bayesian comparison of latent variable

### 日本語訳（自動翻訳）

> マコーネル、S. (2004)。コードコンプリート、第 2 版。マイクロソフトプレス。
> Meng, X.L.、van Dyk, D.A. (2001)。データ拡張の技術。計算ジャーナル
> およびグラフ統計 10、1 ～ 50。
> Merkle, E.C.、Furr, D.、Rabe-Hesketh, S. (2019)。潜在変数のベイズ比較

### 熟語・専門語

- **ESS**: 有効サンプルサイズ。自己相関を考慮した独立サンプル相当数。

### 要約

- マコーネル、S. (2004)。

## Chunk 0767

### English（抽出4行）

> models: Conditional versus marginal likelihoods. Psychometrika 84, 802–829.
> Millar, R. B. (2018). Conditional vs marginal estimation of the predictive loss of hierarchical
> models using WAIC and cross-validation. Statistics and Computing 28, 375–385.
> Modrák, M. (2018). Reparameterizing the sigmoid model of gene regulation for Bayesian inference.

### 日本語訳（自動翻訳）

> モデル: 条件付き尤度と周辺尤度。サイコメトリカ 84、802–829。
> ミラー、R.B. (2018)。階層的損失の予測の条件付き推定と限界推定
> WAIC と相互検証を使用したモデル。統計とコンピューティング 28、375–385。
> モドラク、M. (2018)。ベイズ推論のための遺伝子制御のシグモイド モデルの再パラメーター化。

### 熟語・専門語

- **Bayesian inference**: ベイズ推論。事前分布と尤度から事後分布を計算する中核処理。
- **likelihood**: 尤度。パラメータが与えられたときデータがどれだけ起こりやすいか。
- **validation**: 検証。モデルが目的・データ・外部知識に照らして妥当かを確認すること。

### 要約

- モデル: 条件付き尤度と周辺尤度。

## Chunk 0768

### English（抽出4行）

> Computational Methods in Systems Biology. CMSB 2018. Lecture Notes in Computer Science,
> vol. 11095, 309–312.
> Montgomery, J. M., and Nyhan, B. (2010). Bayesian model averaging: Theoretical developments
> and practical applications. Political Analysis 18, 245–270.

### 日本語訳（自動翻訳）

> システム生物学における計算手法。 CMSB 2018. コンピューターサイエンスの講義ノート、
> 巻。 11095、309–312。
> モンゴメリー、J.M.、ナイハン、B. (2010)。ベイジアン モデルの平均化: 理論的発展
> そして実用的なアプリケーション。政治分析 18、245–270。

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- システム生物学における計算手法。

## Chunk 0769

### English（抽出4行）

> Morgan, S. L., and Winship, C. (2014). Counterfactuals and Causal Inference: Methods and
> Principles for Social Research, second edition. Cambridge University Press.
> Morris, G. E., Gelman, A., and Heidemanns, M. (2020). How the Economist presidential forecast
> works. projects.economist.com/us-2020-forecast/president/how-this-works

### 日本語訳（自動翻訳）

> モーガン、S.L.、ウィンシップ、C. (2014)。反事実と因果推論: 方法と
> 社会調査の原則、第 2 版。ケンブリッジ大学出版局。
> Morris, G. E.、Gelman, A.、および Heidemanns, M. (2020)。エコノミスト大統領の予想
> 動作します。プロジェクト.economist.com/us-2020-forecast/president/how-this-works

### 熟語・専門語

- **ESS**: 有効サンプルサイズ。自己相関を考慮した独立サンプル相当数。

### 要約

- モーガン、S.L.、ウィンシップ、C. (2014)。

## Chunk 0770

### English（抽出4行）

> Navarro, D. J. (2019). Between the devil and the deep blue sea: Tensions between scientiﬁc
> judgement and statistical model selection. Computational Brain and Behavior 2, 28–34.
> Navarro, D. J. (2020). If mathematical psychology did not exist we might need to invent it: A
> comment on theory building in psychology. Perspectives on Psychological Science. psyarxiv.

### 日本語訳（自動翻訳）

> ナバロ、DJ (2019)。悪魔と紺碧の海の間: 科学と科学の間の緊張
> 判断と統計モデルの選択。計算脳と行動 2、28–34。
> ナバロ、DJ (2020)。数理心理学が存在しなかった場合、それを発明する必要があるかもしれません。
> 心理学における理論構築に関するコメント。心理科学に関する視点。 psyarxiv。

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- ナバロ、DJ (2019)。

## Chunk 0771

### English（抽出4行）

> com/ygbjp
> Neal, R. M. (1993). Probabilistic inference using Markov chain Monte Carlo methods. Technical
> Report CRG-TR-93-1, Department of Computer Science, University of Toronto.
> Neal, R. M. (2011). MCMC using Hamiltonian dynamics. In Handbook of Markov Chain Monte

### 日本語訳（自動翻訳）

> com/ygbjp
> ニール、R.M. (1993)。マルコフ連鎖モンテカルロ法を使用した確率的推論。技術的な
> レポート CRG-TR-93-1、トロント大学コンピューターサイエンス学部。
> ニール、R.M. (2011)。ハミルトン力学を使用する MCMC。マルコフ連鎖モンテのハンドブックに

### 熟語・専門語

- **Markov chain**: マルコフ連鎖。MCMCで事後分布からサンプルを得るための確率過程。

### 要約

- com/ygbjp ニール、R.M. (1993)。

## Chunk 0772

### English（抽出4行）

> Carlo, ed. S. Brooks, A. Gelman, G. L. Jones, and X. L. Meng, 113–162. London: CRC Press.
> Niederlová, V., Modrák, M., Tsyklauri, O., Huranová, M., and Štěpánek, O. (2019). Meta-analysis
> of genotype-phenotype associations in Bardet-Biedl Syndrome uncovers diﬀerences among
> causative genes. Human Mutation 40, 2068–2087.

### 日本語訳（自動翻訳）

> カルロ編S・ブルックス、A・ゲルマン、G・L・ジョーンズ、X・L・メン、113-162。ロンドン：CRCプレス。
> Niederlová, V.、Modrak, M.、Tsyklauri, O.、Huranova, M.、および Štěpánek, O. (2019)。メタアナリシス
> バルデ・ビードル症候群における遺伝子型と表現型の関連性により、次のような違いが明らかになります。
> 原因遺伝子。人類の突然変異 40、2068 ～ 2087 年。

### 熟語・専門語

- **ESS**: 有効サンプルサイズ。自己相関を考慮した独立サンプル相当数。

### 要約

- カルロ編S・ブルックス、A・ゲルマン、G・L・ジョーンズ、X・L・メン、113-162。

## Chunk 0773

### English（抽出4行）

> Nott, D. J., Wang, X., Evans, M., and Englert, B. G. (2020). Checking for prior-data conﬂict using
> prior-to-posterior divergences. Statistical Science 35, 234–253.
> Novick, M. R., Jackson, P. H., Thayer, D. T., and Cole, N. S. (1972).
> Estimating multiple

### 日本語訳（自動翻訳）

> Nott, D.J.、Wang, X.、Evans, M.、および Englert, B. G. (2020)。を使用して以前のデータの競合をチェックする
> 前後の発散。統計科学 35、234–253。
> Novic, M. R.、Jackson, P. H.、Thayer, D.T.、および Cole, N.S. (1972)。
> 複数の見積もり

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- Nott, D.J.、Wang, X.、Evans, M.、および Englert, B. G. (2020)。

## Chunk 0774

### English（抽出4行）

> regressions in m-groups: a cross validation study.
> British Journal of Mathematical and
> Statistical Psychology 25, 33–50.
> O’Hagan, A., Buck, C. E., Daneshkhah, A., Eiser, J. R., Garthwaite, P. H., Jenkinson, D. J., Oakely,

### 日本語訳（自動翻訳）

> m グループの回帰: 相互検証研究。
> 英国数学ジャーナル
> 統計心理学 25、33–50。
> オヘイガン、A.、バック、C.E.、ダーネシュカ、A.、アイザー、JR.、ガースウェイト、P.H.、ジェンキンソン、D.J.、オークリー、

### 熟語・専門語

- **cross validation**: 交差検証。汎化性能を推定するためにデータを分割/近似除外する評価法。
- **ESS**: 有効サンプルサイズ。自己相関を考慮した独立サンプル相当数。
- **validation**: 検証。モデルが目的・データ・外部知識に照らして妥当かを確認すること。

### 要約

- m グループの回帰: 相互検証研究。

## Chunk 0775

### English（抽出4行）

> J. E., and Rakow, T. (2006). Uncertain Judgements: Eliciting Experts’ Probabilities. Wiley.
> Paananen, T., Piironen, J., Bürkner, P.-C., and Vehtari, A. (2020). Implicitly adaptive importance
> sampling. Statistics and Computing, in press.
> Pearl, J., and Bareinboim, E. (2011). Transportability of causal and statistical relations: A formal

### 日本語訳（自動翻訳）

> J. E. および Rakow, T. (2006)。不確実な判断: 専門家の確率を導き出す。ワイリー。
> Paananen, T.、Piironen, J.、Bürkner, P.-C.、Vehtari, A. (2020)。暗黙的な適応重要度
> サンプリング。統計とコンピューティング、出版中。
> パール、J.、およびバレインボイム、E. (2011)。因果関係と統計的関係の可搬性: 形式的

### 熟語・専門語

- **ESS**: 有効サンプルサイズ。自己相関を考慮した独立サンプル相当数。

### 要約

- J. E. および Rakow, T. (2006)。

## Chunk 0776

### English（抽出4行）

> approach. In Data Mining Workshops (ICDMW), 2011 IEEE 11th International Conference,
> 540–547.
> Pearl, J., and Bareinboim, E. (2014). External validity: From do-calculus to transportability across
> populations. Statistical Science 29, 579–595.

### 日本語訳（自動翻訳）

> アプローチする。 2011 年の IEEE 第 11 回国際会議のデータ マイニング ワークショップ (ICDMW) において、
> 540年から547年。
> パール、J.、バレインボイム、E. (2014)。外部妥当性: do-calculus からトランスポータビリティまで
> 人口。統計科学 29、579–595。

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- アプローチする。

## Chunk 0777

### English（抽出4行）

> Piironen, J., and Vehtari, A. (2017). Sparsity information and regularization in the horseshoe and
> other shrinkage priors. Electronic Journal of Statistics 11, 5018–5051.
> Pirš, G., and Štrumbelj, E. (2009). Bayesian combination of probabilistic classiﬁers using multi-
> variate normal mixtures. Journal of Machine Learning Research 20, 1–18.

### 日本語訳（自動翻訳）

> Piironen, J.、Vehtari, A. (2017)。馬蹄形のスパース性情報と正則化
> 他の収縮事前分布。電子統計ジャーナル 11、5018–5051。
> ピルシュ、G.、およびシュトルンベリ、E. (2009)。複数のパラメータを使用した確率的分類器のベイジアン結合
> 通常の混合物を変化させます。機械学習研究ジャーナル 20、1–18。

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- Piironen, J.、Vehtari, A. (2017)。

## Chunk 0778

### English（抽出4行）

> Price, P. N., Nero, A. V., and Gelman, A. (1996). Bayesian prediction of mean indoor radon
> concentrations for Minnesota counties. Health Physics 71, 922–936.
> Rasmussen, C. E., and Williams, C. K. I. (2006). Gaussian Processes for Machine Learning. MIT
> Press.

### 日本語訳（自動翻訳）

> Price, P.N.、Nero, A.V.、Gelman, A. (1996)。平均屋内ラドンのベイズ予測
> ミネソタ州の郡の濃度。健康物理学 71、922–936。
> Rasmussen, C.E. および Williams, C.K.I. (2006)。機械学習のためのガウス プロセス。マサチューセッツ工科大学
> を押します。

### 熟語・専門語

- **ESS**: 有効サンプルサイズ。自己相関を考慮した独立サンプル相当数。
- **prediction**: 予測。未知/将来/除外データに対する分布や点推定。

### 要約

- Price, P.N.、Nero, A.V.、Gelman, A. (1996)。

## Chunk 0779

### English（抽出4行）

> Raudenbush, S. W., and Bryk, A. S. (2002). Hierarchical Linear Models, second edition. Sage
> Publications.
> Richardson, S., and Gilks, W. R. (1993). A Bayesian approach to measurement error problems
> in epidemiology using conditional independence models. American Journal of Epidemiology

### 日本語訳（自動翻訳）

> S. W. Raudenbush および A. S. Bryk (2002)。階層線形モデル、第 2 版。セージ
> 出版物。
> リチャードソン、S.、およびギルクス、W.R. (1993)。測定誤差問題に対するベイジアンアプローチ
> 条件付き独立モデルを使用した疫学。アメリカ疫学ジャーナル

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- S. W. Raudenbush および A. S. Bryk (2002)。

## Chunk 0780

### English（抽出4行）

> 138, 430–442.
> Riebler, A., Sørbye, S. H., Simpson, D., and Rue, H. (2018). An intuitive Bayesian spatial model
> for disease mapping that accounts for scaling. Statistical Methods in Medical Research 25,
> 1145–1165.

### 日本語訳（自動翻訳）

> 138、430–442。
> Riebler, A.、Sørbye, S.H.、Simpson, D.、および Rue, H. (2018)。直感的なベイジアン空間モデル
> スケーリングを考慮した疾患マッピングの場合。医学研究における統計的手法 25、
> 1145 ～ 1165 年。

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- 138、430–442。

## Chunk 0781

### English（抽出4行）

> Robert, C., and Casella, G. (2011). A short history of Markov chain Monte Carlo: Subjective
> recollections from incomplete data. Statistical Science 26, 102–115.
> Rubin, D. B. (1984). Bayesianly justiﬁable and relevant frequency calculations for the applied
> statistician. Annals of Statistics 12, 1151–1172.

### 日本語訳（自動翻訳）

> ロバート、C.、およびカセラ、G. (2011)。マルコフ連鎖モンテカルロの短い歴史: 主観的
> 不完全なデータからの思い出。統計科学 26、102–115。
> ルービン、D.B. (1984)。ベイジアン的に正当化され、適用される関連度数の計算
> 統計学者。統計年報 12、1151 ～ 1172 年。

### 熟語・専門語

- **Markov chain**: マルコフ連鎖。MCMCで事後分布からサンプルを得るための確率過程。

### 要約

- ロバート、C.、およびカセラ、G. (2011)。

## Chunk 0782

### English（抽出4行）

> Rudin, C. (2018). Please stop explaining black box models for high stakes decisions. NeurIPS 2018
> Workshop on Critiquing and Correcting Trends in Machine Learning. arxiv.org/abs/1811.10154
> Rue, H., Martino, S., and Chopin, N. (2009). Approximate Bayesian inference for latent Gaussian
> models by using integrated nested Laplace approximations. Journal of the Royal Statistical

### 日本語訳（自動翻訳）

> ルーディン、C. (2018)。一か八かの意思決定のためにブラックボックスモデルを説明するのはやめてください。 NeurIPS 2018
> 機械学習の傾向の批判と修正に関するワークショップ。 arxiv.org/abs/1811.10154
> ルー、H.、マルティーノ、S.、およびショパン、N. (2009)。潜在ガウスの近似ベイズ推論
> 統合されたネストされたラプラス近似を使用してモデルを作成します。王立統計ジャーナル

### 熟語・専門語

- **Bayesian inference**: ベイズ推論。事前分布と尤度から事後分布を計算する中核処理。
- **approximate**: 近似。速度や扱いやすさのため、正確な推論・モデルを緩めること。
- **decision**: 意思決定。予測分布を損失・効用・行動選択へ接続する工程。

### 要約

- ルーディン、C. (2018)。

## Chunk 0783

### English（抽出4行）

> Society B 71, 319–392.
> Sarma, A., and Kay, M. (2020). Prior setting in practice: Strategies and rationales used in choosing
> prior distributions for Bayesian analysis. Proceedings of the 2020 CHI Conference on Human
> Factors in Computing Systems.

### 日本語訳（自動翻訳）

> ソサエティ B 71、319–392。
> サルマ、A.、ケイ、M. (2020)。実際の事前設定: 選択に使用される戦略と理論的根拠
> ベイズ分析のための事前分布。 2020 CHI 人間会議の議事録
> コンピューティング システムの要素。

### 熟語・専門語

- **prior distribution**: 事前分布。データ観測前の知識・制約を表す分布。

### 要約

- ソサエティ B 71、319–392。

## Chunk 0784

### English（抽出4行）

> Savage, J. (2016). What is modern statistical workﬂow? khakieconomics.github.io/2016/08/29/
> What-is-a-modern-statistical-workﬂow.html
> Shi, X., and Stevens, R. (2008). SWARM: a scientiﬁc workﬂow for supporting bayesian approaches
> to improve metabolic models. CLADE ’08: Proceedings of the 6th International Workshop on

### 日本語訳（自動翻訳）

> サベージ、J. (2016)。最新の統計ワークフローとは何ですか?カーキエコノミクス.github.io/2016/08/29/
> 最新の統計ワークフローとは.html
> Shi、X.、および Stevens, R. (2008)。 SWARM: ベイジアンアプローチをサポートするための科学的ワークフロー
> 代謝モデルを改善します。 CLADE '08: 第 6 回国際ワークショップの議事録

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- サベージ、J. (2016)。

## Chunk 0785

### English（抽出4行）

> Challenges of Large Applications in Distributed Environments, 25–34.
> Shirani-Mehr, H., Rothschild, D., Goel, S., and Gelman, A. (2018). Disentangling bias and variance
> in election polls. Journal of the American Statistical Association 118, 607–614.
> Simmons, J., Nelson, L., and Simonsohn, U. (2011). False-positive psychology: Undisclosed

### 日本語訳（自動翻訳）

> 分散環境における大規模アプリケーションの課題、25 ～ 34。
> シラニ・メア、H.、ロスチャイルド、D.、ゴエル、S.、ゲルマン、A. (2018)。バイアスと分散を解きほぐす
> 選挙世論調査で。米国統計協会ジャーナル 118、607–614。
> シモンズ、J.、ネルソン、L.、およびシモンソン、U. (2011)。偽陽性心理学: 非公開

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- 分散環境における大規模アプリケーションの課題、25 ～ 34。

## Chunk 0786

### English（抽出4行）

> ﬂexibility in data collection and analysis allow presenting anything as signiﬁcant. Psychological
> Science 22, 1359–1366.
> Simpson, D., Rue, H., Riebler, A., Martins, T. G., and Sørbye, S. H. (2017). Penalising model
> component complexity: A principled, practical approach to constructing priors. Statistical

### 日本語訳（自動翻訳）

> データ収集と分析の柔軟性により、あらゆるものを重要なものとして提示できます。心理的
> サイエンス 22、1359–1366。
> Simpson, D.、Rue, H.、Riebler, A.、Martins, T. G.、および Sørbye, S. H. (2017)。ペナルティモデル
> コンポーネントの複雑さ: 事前確率を構築するための原則に基づいた実践的なアプローチ。統計的

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- データ収集と分析の柔軟性により、あらゆるものを重要なものとして提示できます。

## Chunk 0787

### English（抽出4行）

> Science 32, 1–28.
> Singer, E., Van Hoewyk, J., Gebler, N., Raghunathan, T., and McGonagle, K. (1999). The eﬀects
> of incentives on response rates in interviewer-mediated surveys. Journal of Oﬃcial Statistics
> 15, 217–230.

### 日本語訳（自動翻訳）

> サイエンス 32、1–28。
> シンガー、E.、ヴァン・ホーウィク、J.、ゲブラー、N.、ラグナタン、T.、およびマクゴナグル、K. (1999)。効果
> 面接官介在調査における回答率に対するインセンティブの割合。政府統計ジャーナル
> 15、217–230。

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- サイエンス 32、1–28。

## Chunk 0788

### English（抽出4行）

> Sivula, T., Magnusson, M, and Vehtari, A. (2020). Uncertainty in Bayesian leave-one-out cross-
> validation based model comparison. arxiv.org./abs/2008.10296
> Skrondal, A. and Rabe-Hesketh, S. (2004). Generalized Latent Variable Modeling: Multilevel,
> Longitudinal and Structural Equation Models. London: CRC Press.

### 日本語訳（自動翻訳）

> Sivula, T.、Magnusson, M、および Vehtari, A. (2020)。ベイジアン リーブ ワン アウト クロスの不確実性
> 検証ベースのモデル比較。 arxiv.org./abs/2008.10296
> Skrondal, A. および Rabe-Hesketh, S. (2004)。一般化された潜在変数モデリング: マルチレベル、
> 縦断および構造方程式モデル。ロンドン：CRCプレス。

### 熟語・専門語

- **model comparison**: モデル比較。LOO-CVなどで複数モデルの予測性能や弱点を比較すること。
- **leave-one-out**: LOO。一点ずつ除外した予測評価を効率的に近似する交差検証。
- **ESS**: 有効サンプルサイズ。自己相関を考慮した独立サンプル相当数。
- **uncertainty**: 不確実性。観測・パラメータ・モデル構造・意思決定に残る曖昧さ。
- **validation**: 検証。モデルが目的・データ・外部知識に照らして妥当かを確認すること。

### 要約

- Sivula, T.、Magnusson, M、および Vehtari, A. (2020)。

## Chunk 0789

### English（抽出4行）

> Smith, A. (2013). Sequential Monte Carlo Methods in Practice. New York: Springer.
> Stan Development Team (2020). Stan User’s Guide. mc-stan.org
> Steegen, S., Tuerlinckx, F., Gelman, A., and Vanpaemel, W. (2016).
> Increasing transparency

### 日本語訳（自動翻訳）

> スミス、A. (2013)。逐次モンテカルロ法の実践。ニューヨーク：スプリンガー。
> スタン開発チーム (2020)。 Stan ユーザーガイド。 mc-stan.org
> Steegen, S.、Tueerlinckx, F.、Gelman, A.、および Vanpaemel, W. (2016)。
> 透明性の向上

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- スミス、A. (2013)。

## Chunk 0790

### English（抽出4行）

> through a multiverse analysis. Perspectives on Psychological Science 11, 702–712.
> Stone, M. (1974). Cross-validatory choice and assessment of statistical predictions (with discus-
> sion). Journal of the Royal Statistical Society B 36, 111–147.
> Stone, M. (1977). An asymptotic equivalence of choice of model cross-validation and Akaike’s

### 日本語訳（自動翻訳）

> 多元宇宙の分析を通じて。心理科学に関する展望 11、702–712。
> ストーン、M. (1974)。交差検証による選択と統計的予測の評価 (ディスカッションを伴う)
> シオン）。王立統計協会ジャーナル B 36、111–147。
> ストーン、M. (1977)。モデルの相互検証と赤池の選択の漸近的等価性

### 熟語・専門語

- **ESS**: 有効サンプルサイズ。自己相関を考慮した独立サンプル相当数。
- **validation**: 検証。モデルが目的・データ・外部知識に照らして妥当かを確認すること。
- **prediction**: 予測。未知/将来/除外データに対する分布や点推定。

### 要約

- 多元宇宙の分析を通じて。

## Chunk 0791

### English（抽出4行）

> criterion. Journal of the Royal Statistical Society B 36, 44–47.
> Talts, S., Betancourt, M., Simpson, D., Vehtari, A., and Gelman, A. (2020). Validating Bayesian
> inference algorithms with simulation-based calibration.
> www.stat.columbia.edu/~gelman/

### 日本語訳（自動翻訳）

> 基準。王立統計協会ジャーナル B 36、44–47。
> Talts, S.、Betancourt, M.、Simpson, D.、Vehtari, A.、および Gelman, A. (2020)。ベイジアンの検証
> シミュレーションベースのキャリブレーションを備えた推論アルゴリズム。
> www.stat.columbia.edu/~gelman/

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

> 研究/未発表/sbc.pdf
> Taylor, J. および Tibshirani, R.J. (2015)。統計学習と選択的推論。の議事録
> 米国科学アカデミー 112、7629–7634。
> テイラー、S.J.、レセム、B. (2018)。大規模な予測。アメリカの統計学者、72、37–45。

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- 研究/未発表/sbc.pdf Taylor, J. および Tibshirani, R.J. (2015)。

## Chunk 0793

### English（抽出4行）

> Tierney, L., and Kardane, J.B. (1986). Accurate approximations for posterior moments and marginal
> densities. Journal of the American Statistical Association, 81(393):82–86.
> Turner, K. J., and Lambert, P. S. (2015). Workﬂows for quantitative data analysis in the social
> sciences. International Journal on Software Tools for Technology Transfer 17, 321–338.

### 日本語訳（自動翻訳）

> ティアニー、L.、およびカーダン、J.B. (1986)。事後モーメントとマージナルの正確な近似
> 密度。米国統計協会ジャーナル、81(393):82–86。
> ターナー、K.J.、ランバート、PS. (2015)。ソーシャルにおける定量的データ分析のワークフロー
> 科学。技術移転のためのソフトウェアツールに関する国際ジャーナル 17、321–338。

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- ティアニー、L.、およびカーダン、J.B. (1986)。

## Chunk 0794

### English（抽出4行）

> Unwin, A., Volinsky, C., and Winkler, S. (2003). Parallel coordinates for exploratory modelling
> analysis. Computational Statistics and Data Analysis 43, 553–564.
> Vehtari, A. (2019). Cross-validation for hierarchical models. avehtari.github.io/modelselection/
> rats_kcv.html

### 日本語訳（自動翻訳）

> Unwin, A.、Volinsky, C.、および Winkler, S. (2003)。探索的モデリングのための平行座標
> 分析。計算統計とデータ分析 43、553–564。
> ヴェタリ、A. (2019)。階層モデルの相互検証。 avehtari.github.io/modelselection/
> ラッツ_kcv.html

### 熟語・専門語

- **validation**: 検証。モデルが目的・データ・外部知識に照らして妥当かを確認すること。

### 要約

- Unwin, A.、Volinsky, C.、および Winkler, S. (2003)。

## Chunk 0795

### English（抽出4行）

> Vehtari A., Gabry J., Magnusson M., Yao Y., Bürkner P., Paananen T., Gelman A. (2020). loo:
> Eﬃcient leave-one-out cross-validation and WAIC for Bayesian models. R package version
> 2.3.1, mc-stan.org/loo.
> Vehtari, A., and Gabry, J. (2020). Bayesian stacking and pseudo-BMA weights using the loo

### 日本語訳（自動翻訳）

> Vehtari A.、Gabry J.、Magnusson M.、Yao Y.、Bürkner P.、Paananen T.、Gelman A. (2020)。トイレ:
> ベイジアン モデルの効率的なリーブ ワン アウト相互検証と WAIC。 Rパッケージのバージョン
> 2.3.1、mc-stan.org/loo。
> Vehtari、A.、および Gabry、J. (2020)。 loo を使用したベイジアン スタッキングと疑似 BMA 重み

### 熟語・専門語

- **leave-one-out**: LOO。一点ずつ除外した予測評価を効率的に近似する交差検証。
- **validation**: 検証。モデルが目的・データ・外部知識に照らして妥当かを確認すること。

### 要約

- Vehtari A.、Gabry J.、Magnusson M.、Yao Y.、Bürkner P.、Paananen T.、Gelman A. (2020)。

## Chunk 0796

### English（抽出4行）

> package. mc-stan.org/loo/articles/loo2-weights.html
> Vehtari, A., Gelman, A., and Gabry, J. (2017). Practical Bayesian model evaluation using leave-
> one-out cross-validation and WAIC. Statistics and Computing 27, 1413–1432.
> Vehtari, A., Gelman, A., Simpson, D., Carpenter, D., and Bürkner, P.-C. (2020).

### 日本語訳（自動翻訳）

> パッケージ。 mc-stan.org/loo/articles/loo2-weights.html
> Vehtari, A.、Gelman, A.、および Gabry, J. (2017)。 Leave-を使用した実践的なベイジアンモデル評価
> ワンアウト相互検証と WAIC。統計とコンピューティング 27、1413–1432。
> Vehtari, A.、Gelman, A.、Simpson, D.、Carpenter, D.、および Bürkner, P.-C. （2020年）。

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

> ランク-
> 正規化、折り畳み、および位置特定: の収束を評価するための改良された R-hat
> MCMC。ベイズ分析。
> Vehtari、A.、Gelman、A.、Sivula、T.、Jylanki、P.、Tran、D.、Sahai、S.、Blomstedt、P.、カニンガム、

### 熟語・専門語

- **R-hat**: R-hat。複数chainの収束を測る診断量。1から離れるほど問題。
- **ESS**: 有効サンプルサイズ。自己相関を考慮した独立サンプル相当数。

### 要約

- ランク- 正規化、折り畳み、および位置特定: の収束を評価するための改良された R-hat MCMC。

## Chunk 0798

### English（抽出4行）

> J. P., Schiminovich, D., and Robert, C. P. (2020). Expectation propagation as a way of life: A
> framework for Bayesian inference on partitioned data. Journal of Machine Learning Research
> 21, 1–53.
> Vehtari, A., Simpson, D., Gelman, A., Yao, Y., and Gabry, J. (2015). Pareto smoothed importance

### 日本語訳（自動翻訳）

> J. P.、Schiminovich, D.、および Robert, C. P. (2020)。生き方としての期待の伝播: A
> 分割されたデータに対するベイズ推論のフレームワーク。機械学習研究ジャーナル
> 21、1–53。
> Vehtari, A.、Simpson, D.、Gelman, A.、Yao, Y.、および Gabry, J. (2015)。パレート平滑化重要度

### 熟語・専門語

- **Bayesian inference**: ベイズ推論。事前分布と尤度から事後分布を計算する中核処理。
- **Pareto**: Pareto-k診断。PSIS-LOOの信頼性を示す診断量。大きいと再推定やモデル修正が必要。

### 要約

- J. P.、Schiminovich, D.、および Robert, C. P. (2020)。

## Chunk 0799

### English（抽出4行）

> sampling. arxiv.org/abs/1507.02646
> Wang, W., and Gelman, A. (2015). Diﬃculty of selecting among multilevel models using predictive
> accuracy. Statistics and Its Interface 8 (2), 153–160.
> Weber, S., Gelman, A., Lee, D., Betancourt, M., Vehtari, A., and Racine-Poon, A. (2018). Bayesian

### 日本語訳（自動翻訳）

> サンプリング。 arxiv.org/abs/1507.02646
> ワン W. およびゲルマン A. (2015)。予測を使用してマルチレベルモデルから選択することの難しさ
> 精度。統計とそのインターフェイス 8 (2)、153–160。
> Weber, S.、Gelman, A.、Lee, D.、Betancourt, M.、Vehtari, A.、および Racine-Poon, A. (2018)。ベイジアン

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

> 平均データの集約: 医薬品開発への応用。応用統計年報
> 12、1583 ～ 1604 年。
> ウィッカム、H. (2006)。
> R と GGobi を使用した探索的モデル分析。

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- 平均データの集約: 医薬品開発への応用。

## Chunk 0801

### English（抽出4行）

> had.co.nz/model-vis/
> 2007-jsm.pdf
> Wickham, H., Cook, D., and Hofmann, H. (2015). Visualizing statistical models: Removing the
> blindfold. Statistical Analysis and Data Mining: The ASA Data Science Journal 8, 203–225.

### 日本語訳（自動翻訳）

> had.co.nz/model-vis/
> 2007-jsm.pdf
> ウィッカム、H.、クック、D.、およびホフマン、H. (2015)。統計モデルの視覚化:
> 目隠し。統計分析とデータ マイニング: ASA データ サイエンス ジャーナル 8、203–225。

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- had.co.nz/model-vis/ 2007-jsm.pdf ウィッカム、H.、クック、D.、およびホフマン、H. (2015)。

## Chunk 0802

### English（抽出4行）

> Wickham, H., and Groelmund, G. (2017). R for Data Science. Sebastopol, Calif.: O’Reilly.
> Wilson, G., Aruliah, D. A., Brown, C. T., Hong, N. P. C., Davis, M., Guy, R. T., Haddock, S. H. D.,
> Huﬀ, K. D., Mitchell, I. M., Plumbley, M. D., Waugh, B., White, E. P., and Wilson, P. (2014).
> Best practices for scientiﬁc computing. PLoS Biology 12, e1001745.

### 日本語訳（自動翻訳）

> ウィッカム、H.、グロエルムント、G. (2017)。データサイエンスのR。カリフォルニア州セバストポル：オライリー。
> ウィルソン、G.、アルリア、D.A.、ブラウン、C.T.、ホン、N.P.C.、デイビス、M.、ガイ、R.T.、ハドック、S.H.D.、
> Huﬀ, K.D.、Mitchell, I.M.、Plumbley, M.D.、Waugh, B.、White, E.P.、および Wilson, P. (2014)。
> 科学技術コンピューティングのベスト プラクティス。 PLoS 生物学 12、e1001745。

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- ウィッカム、H.、グロエルムント、G. (2017)。

## Chunk 0803

### English（抽出4行）

> Wilson, G., Bryan, J., Cranston, K., Kitzes, J. Nederbragt, L., and Teal, T. K. (2017). Good enough
> practices in scientiﬁc computing. PLoS Computational Biololgy 13, e1005510.
> Yao, Y., Cademartori, C., Vehtari, A., and Gelman, A. (2020). Adaptive path sampling in metastable
> posterior distributions. arxiv.org/abs/2009.00471

### 日本語訳（自動翻訳）

> Wilson, G.、Bryan, J.、Cranston, K.、Kitzes、J. Nederbragt, L.、および Teal, T. K. (2017)。十分です
> 科学技術コンピューティングの実践。 PLoS 計算生物学 13、e1005510。
> Yao, Y.、Cademartori, C.、Vehtari, A.、および Gelman, A. (2020)。メタステーブルでの適応パス サンプリング
> 事後分布。 arxiv.org/abs/2009.00471

### 熟語・専門語

- **posterior distribution**: 事後分布。データ観測後の未知量の不確実性を表す分布。

### 要約

- Wilson, G.、Bryan, J.、Cranston, K.、Kitzes、J. Nederbragt, L.、および Teal, T. K. (2017)。

## Chunk 0804

### English（抽出4行）

> Yao, Y., Vehtari, A., and Gelman, A. (2020). Stacking for non-mixing Bayesian computations: The
> curse and blessing of multimodal posteriors. arxiv.org/abs/2006.12335
> Yao, Y., Vehtari, A., Simpson, D., and Gelman, A. (2018a). Yes, but did it work?: Evaluating
> variational inference. In Proceedings of International Conference on Machine Learning, 5581–

### 日本語訳（自動翻訳）

> Yao, Y.、Vehtari, A.、および Gelman, A. (2020)。非混合ベイジアン計算のためのスタッキング:
> 多峰性事後者の呪いと祝福。 arxiv.org/abs/2006.12335
> Yao, Y.、Vehtari, A.、Simpson, D.、Gelman, A. (2018a)。はい、でもうまくいきましたか?: 評価中
> 変分推論。機械学習に関する国際会議議事録、5581–

### 熟語・専門語

- **ESS**: 有効サンプルサイズ。自己相関を考慮した独立サンプル相当数。

### 要約

- Yao, Y.、Vehtari, A.、および Gelman, A. (2020)。

## Chunk 0805

### English（抽出4行）

> 5590.
> Yao, Y., Vehtari, A., Simpson, D., and Gelman, A. (2018b). Using stacking to average Bayesian
> predictive distributions (with discussion). Bayesian Analysis 13, 917–1003.
> Yu, B., and Kumbier, K. (2020). Veridical data science. Proceedings of the National Academy of

### 日本語訳（自動翻訳）

> 5590。
> Yao, Y.、Vehtari, A.、Simpson, D.、および Gelman, A. (2018b)。スタッキングを使用してベイジアンを平均化する
> 予測分布 (ディスカッション付き)。ベイズ分析 13、917–1003。
> Yu、B.、および Kumbier、K. (2020)。検証的なデータサイエンス。国立アカデミーの議事録

### 熟語・専門語

- （この4行では主要な登録熟語・専門語は少なめ。前後チャンクと合わせて読む。）

### 要約

- 5590。

## Chunk 0806

### English（抽出4行）

> Sciences 117, 3920–3929.
> Zhang, Y. D., Naughton, B. P., Bondell, H. D., and Reich, B. J. (2020). Bayesian regression
> using a prior on the model ﬁt: The R2-D2 shrinkage prior. Journal of the American Statistical
> Association, doi:10.1080/01621459.2020.1825449

### 日本語訳（自動翻訳）

> サイエンス 117、3920–3929。
> Zhang, Y.D.、Naughton, B.P.、Bondell, H.D.、および Reich, B.J. (2020)。ベイジアン回帰
> モデル フィットに事前分布を使用する: R2-D2 収縮事前分布。アメリカ統計ジャーナル
> 協会、土井:10.1080/01621459.2020.1825449

### 熟語・専門語

- **ESS**: 有効サンプルサイズ。自己相関を考慮した独立サンプル相当数。

### 要約

- サイエンス 117、3920–3929。
