# 半導体製造における製品特定箇所の抵抗予測：QC探索・交絡・交互作用・高次元変数選択の研究調査

- 作成日：2026-10-30
- 対象：半導体量産工程の製品特定箇所の連続値抵抗 R
- 目的：候補QCの網羅的洗い出し → QC間の関係の可視化 → 交絡と交互作用の評価 → 変数削減 → 将来の予測モデル構築
- 位置づけ：先行研究に基づく初期調査とPoC設計案。製品構造・抵抗測定方法・取得できるQCの仕様は未確定であり、QCの優先度は仮説である。
- 関連資料：[半導体製造における大量センサ × 階層データの予測モデリング調査](./semiconductor_hierarchical_modeling_research_report.md)

## 0. 要旨

**推奨する順序は「物理・工程知識に基づく候補QCリスト → 冗長性／条件付き依存／交絡の診断 → 非線形主効果・交互作用の探索 → 安定した変数選択 → 階層・空間構造を含む予測モデルの比較」である。**

主な技術上の落とし穴：

1. 単変量相関が弱い変数でも、交互作用の一方の項として重要な場合がある。最初のPearson相関だけで一括削除しない。
2. Tool、Chamber、Recipe、製品、Lot、Wafer、Shot/Die、測定位置が違えば、QCと抵抗の全体相関がグループ差を反映している可能性がある。
3. 相関する複数QCを個別にランキングすると「代理変数」同士で重要性が分散する。グループ単位の評価も必要。
4. Graphical Lasso／ベイジアンネットワーク／NOTEARS／PCMCIのエッジは、そのまま介入可能な因果効果を意味しない。
5. 予測に使うQCは、予測時点以前に利用できるものに限定する。Lot・Wafer・未来時刻をまたぐ情報漏洩を避ける。
6. 主要な先行研究は膜厚・CD・CMP等のVirtual Metrologyが中心。**抵抗そのものを本データで予測できることが実証されたという意味ではない。**

## 1. 抵抗値と工程知識から候補QCを抽出する

### 1.1 対象構造ごとの第一次QC候補

以下は一般的な物理機構から作った**調査候補**であり、実際の工場で測定可能な項目・有効な因子であると確定したものではない。

| 予測する抵抗の構造 | 先に確認するQC／プロセス指標 | 交互作用・交絡の候補 |
|---|---|---|
| 金属配線・金属膜 | CD/線幅、膜厚、シート抵抗、組成、バリア/ライナー膜厚、粗さ、CMP形状、金属成膜条件 | CD×膜厚、膜厚×材料・成膜条件、Tool×CD |
| コンタクト／Via | 開口CD、エッチング深さ/プロファイル、残渣、前洗浄、下地表面状態、バリア/ライナー、埋め込み・ボイド指標、アライメント | 開口CD×残渣、洗浄×成膜、Recipe×開口CD |
| 拡散層・シート抵抗 | 注入ドーズ／エネルギー、活性化アニール、温度・時間、拡散・接合プロファイル、シート抵抗 | 注入条件×アニール、温度×処理時間 |
| トランジスタの寄生抵抗 | ゲート/アクティブCD、オーバーレイ、拡散層特性、シリサイド、コンタクト抵抗 | CD×ドーピング、コンタクトCD×界面 |
| 全構造共通 | Product/Layer、Lot/Wafer、Tool/Chamber、Recipe、工程順序、測定座標、Shot/Die、PMからの経過、日時 | Tool×QC、PM状態×QC、位置×QC |

金属配線の一次近似は **R = ρ L / (W T)**（抵抗率ρ、長さL、線幅W、膜厚T）。微細構造・界面・粒界・温度などによってρが変わり得るため、単なる1変数比例モデルだけに限定しない。Viaや拡散層などでは別の物理モデルが必要。

### 1.2 QC台帳の必須項目

最低限、QC名、物理量/単位、対象工程、対象レイヤ、採取タイミング、取得可能時点、測定箇所、Tool/Chamber/Recipe、計測頻度、欠損率、測定再現性、想定する作用経路、代理変数候補、除外理由を記録する。

- 抵抗 R が「製品の1箇所・ウエハ1点」か「ウエハ面内の複数点」かを最初に明示する。
- QCと抵抗の測定位置が違う場合、面内補間値や距離・Shot差を考慮する。
- 下流工程QCを使用するかは「いつ予測したいか」によって分ける（未来情報リークを回避）。
- 同一工程の似たQCをグループ化し、グループ単位でも価値を評価する。

## 2. 検証する5つの競合仮説

| 仮説 | 内容 | 主な検証手段 |
|---|---|---|
| H1：少数QCの主効果 | CD・膜厚・シート抵抗などが単独で R を説明 | 散布図、Spearman、GLM/GAM |
| H2：見かけの相関 | Tool/Chamber/Lot/RecipeなどがQCとRに同時に関連 | グループ内/間分解、GLMM、偏回帰 |
| H3：交互作用優位 | QC1だけ・QC2だけでは弱いがQC1×QC2は重要 | EBM/GA2M、glinternet、階層的Lasso、GLMMで検証 |
| H4：空間構造 | Wafer座標、Shot/Die差、外周/中心傾向が R に関連 | 空間GAM、Gaussian Process、Shot効果 |
| H5：QCの冗長性 | 高相関QC群が同じ潜在工程状態を測っている | 相関クラスタ、Graphical Lasso、mRMR、グループ重要性 |

1つだけを前提にしない。5つの仮説を別々に検討して、最終的に統合する。

## 3. 方法の全体マップ（前回回答で挙げた手法を網羅）

### 3.1 QC候補の関係性を確認する手法

| 手法 | 主な用途 | 得意な点 | 注意 |
|---|---|---|---|
| Pearson相関 | 線形の周辺関連 | 簡単・高速 | 非線形、交絡、交互作用に弱い |
| Spearman相関 | 単調な周辺関連 | 外れ値・非線形単調関係に比較的強い | 非単調な関係を見逃す |
| 偏相関/偏回帰 | 共変量調整後の関連 | 交絡の仮説検証の入口 | 調整集合の妥当性が前提、非線形に弱い |
| Graphical Lasso | 高次元QCの疎な条件付き依存ネットワーク | 冗長QCの構造可視化 | ガウス型・線形条件付き依存の解釈に注意 |
| Gaussian Bayesian Network + Markov Blanket | 変数ネットワークと目的変数周辺の候補絞り込み | 工程知識を組み込みやすい | 因果方向は自明でない |
| mRMR | Rへの関連を残しながら冗長QCを削減 | 高次元の初期候補選択 | 弱い主効果・純粋な交互作用を見逃す可能性 |
| NOTEARS | DAG構造の探索 | DAG制約を連続最適化で実装 | 観察データのみから因果が確定するわけではない |
| FCI | 潜在交絡を許す制約ベースの因果探索 | 未観測共通原因の可能性を表現 | 大規模・測定誤差・仮定違反で不安定 |
| PCMCI | 多変量時系列の遅延付き関連探索 | 時系列依存を条件付き検定 | 同期誤差、時系列分解能、非定常に注意 |

### 3.2 交絡・階層性を扱う手法

| 手法 | 主な用途 | 注意 |
|---|---|---|
| GLM/多変量線形回帰 | 交絡候補を固定効果として調整 | 高次元多重共線性、関数形の誤指定 |
| GAM | QC主効果を非線形の滑らかな関数で表現 | 自由度、過学習、共曲線性 |
| GLMM / Linear Mixed Model（連続RならLMM） | Lot・Tool・Chamber・Waferの群間変動を反映 | クロス分類・ネストを実データに合わせる |
| Random slopeモデル | ToolごとのQC感度の違い | 群ごとに十分なサンプルが必要 |
| Within-Between / Mundlak分解 | 同一Tool/Chamber内のQC変化と群平均差を分離 | 群内変動が乏しい場合は識別しにくい |
| 階層ベイズ | 部分プーリング・不確実性を明示 | 計算コスト、事前分布、識別性 |
| Double / Debiased Machine Learning | 明示した因果効果パラメータを高次元共変量で調整 | 因果識別仮定が不可欠。探索的因果発見ツールではない |

### 3.3 交互作用検出・解釈の手法

| 手法 | 主な用途 | 注意 |
|---|---|---|
| QC1×QC2の積項を含むGLM/LMM/GLMM | 特定の2変数交互作用の効果量と検定 | 積項のみのモデルでは非線形主効果との混同に注意 |
| hierNet（階層的Lasso） | 主効果＋交互作用の疎な選択 | 階層性制約の種類を確認 |
| glinternet（hierarchical group lasso） | 連続・カテゴリ混在のペア交互作用選択 | 大量ペアは事前スクリーニング推奨 |
| GA2M / Explainable Boosting Machine (EBM) | 非線形主効果＋少数の2変数交互作用を可視化 | モデル内寄与と統計的有意性は別 |
| LightGBM / CatBoost | 高精度の非線形・交互作用学習 | 説明・因果解釈を別途検討 |
| CatBoost Feature Interaction | 学習済みモデルでの特徴ペアの相互利用度 | データの統計的交互作用検定ではない |
| SHAP / SHAP Interaction Values | Tree modelにおける特徴寄与とペア寄与 | 特徴間依存・背景分布に影響される |
| PDP (Partial Dependence Plot) | 特徴別予測曲線 | 強相関QCだと観測されない組合せを評価しやすい |
| ALE / 2D ALE | 条件付きの局所変化の積算による可視化 | 強依存・疎な領域では解釈と精度に注意 |

### 3.4 変数選択・予測・評価の手法

| 手法 | 主な用途 | 注意 |
|---|---|---|
| Lasso | 疎な線形主効果の選択 | 相関QCから恣意的に1つ選びやすい |
| Elastic Net | 相関QCを含む正則化 | 交互作用を明示的に用意しないと拾えない |
| Stability Selection | 再抽出による変数選択頻度 | 群相関・分割単位・選択アルゴリズム依存 |
| Group/Block Conditional Permutation Importance | 相関QCのグループ重要性 | グループ定義と条件付き分布推定に依存 |
| Random Forest / Decision Tree / XGBoost | 非線形予測、変数候補のスクリーニング | 不純度・Gain重要度はバイアスを持つことがある |
| ProjSe（projective selection） | 特に複数出力の高速変数選択 | この案件が1出力なら優先度は低い |
| Gaussian Process / Online GP | 空間変動、不確実性、ドリフト・動的測定 | 大規模データで計算負担 |
| 時系列分割、Lot単位分割、Tool holdout | 実運用に近い汎化検証 | 学習・選択・前処理を各fold内で完結させる |
| MAE / RMSE / R²、Tool別・位置別誤差 | 精度・ばらつきの多面的評価 | 全体平均だけで劣悪なToolを隠さない |

## 4. 交絡の例とモデル式

例：ChamberによってQC-Aと抵抗Rが両方変化する場合、「QC-AとRの全体相関」が生じてもQC-A自体の効果だとは限らない。

比較する解析：
- 全データでの R と QC-A の周辺関連
- Tool/Chamber/Recipe内の R と QC-A の関連
- Tool/Chamber/Recipe間の平均QCと平均Rの関連
- 必要な交絡共変量を入れた LMM/GLMM の係数と不確実性

連続抵抗の例：

    R_ijk = β0 + β1 QC1_ijk + β2 QC2_ijk
            + β12 (QC1×QC2)_ijk
            + u_Tool(i) + u_Lot(j) + ε_ijk

実データではLotとToolの交差分類、Chamberの所属、Wafer内多点などの構造を再設計する。ランダム切片が「すべての交絡」を除くわけではない。

Within-Between分解の概念：

    QC_ig = (QC_ig - mean(QC)_g) + mean(QC)_g
    R_ig  = βw [QC_ig - mean(QC)_g] + βb mean(QC)_g + other terms

これにより、群内変動と群平均差が同じ傾向かを確認できる。

**注意**：予測目的の補助変数と因果効果推定で調整すべき変数は同一ではない。媒介変数、コライダー、未来情報を無批判に調整しない。

## 5. 交互作用の探索から確認まで

1. 物理的にありそうな候補ペア（例：CD×膜厚、CD×Tool、注入条件×アニール、開口CD×残渣）を事前登録する。
2. 主効果をGAM/EBM等で十分にモデル化し、単なる曲率が交互作用に見えていないか確認する。
3. EBMの交互作用ランキング、CatBoost Interaction、SHAP Interactionで広めに候補探索。
4. 2D EBM関数/2D ALEを描く。**観測データが存在するQC組合せ領域**とサンプル密度を重ねる。
5. 上位ペアをglinternet/hierNetで安定的に選択し、適切な階層（Tool/Lotなど）を調整したGLMMで係数・不確実性を評価。
6. 候補探索と仮説検定を同じデータで実施すると選択バイアスが生じる。独立した検証用期間、サンプル分割、または多重検定補正を検討する。
7. 予測性能が実際に改善するかを外部テストで確認する。交互作用が「見える」ことと「使える」ことを分ける。

### 優先度の高い比較

A: 工程知識QC + Elastic Net / LMM（説明性の基準線）  
B: A + 明示的なQC×QCとQC×Tool（交互作用の寄与）  
C: EBM（非線形な主効果＋交互作用）  
D: LightGBM/CatBoost（予測精度の対照）  
E: C/D + 必要に応じた階層残差・空間成分

## 6. 大量のQCを削減する具体策

### 6.1 一次フィルタ

- 定数/ほぼ定数、重複、物理的に無意味な値、明確な未来情報を整理する。
- 欠損率・測定再現性・センサ交換などのメタデータを記録する。
- 欠損率が高いだけで一括削除せず、測定欠損自体が設備状態に依存する可能性を確認する。
- Spearman/Pearsonのランキングは**参考情報**として残し、単変量相関が低いだけで有望QCを全削除しない。

### 6.2 グループ評価

- 工程・物理量・計測器・時間帯でQCを束ねる。
- QC群内の相関クラスタやGraphical Lassoのネットワークを可視化。
- mRMRで低冗長な候補集合を作る。純粋な交互作用向けの候補は別ルートで保護する。
- Group/Block conditional permutation importanceで「このQC群が持つ予測情報」を評価する。
- 個別変数選択だけでなく、同じ物理群の選択頻度を集計する。

### 6.3 選択の安定性

Lot/時系列ブロックを単位に再抽出し、Elastic Net / glinternet等を繰り返して各QC・QCペアの選択率を出す。例えば「100回中90回選択」は安定性を示唆するが、交絡不存在や因果性を証明しない。

## 7. 空間特性をどう使うか

- 1 Waferにつき抵抗1測定点：Wafer/位置を説明変数または群効果として扱う。
- Wafer内で多数点：x,y座標の滑らかな成分、Shot単位の不連続効果、必要なら残差の空間相関をモデル化。
- QCがウェハ平均のみなのかSite単位なのかで情報粒度が異なるため、位置を揃えないまま擬似的に多サンプルへ展開しない。
- 空間情報が試験条件・測定順序による影響を含む場合、それらも確認する。

## 8. Virtual Metrologyを踏まえた実証研究：何が確認されているか

| 番号 | 研究 | 本件への示唆 | 限界 |
|---|---|---|---|
| P1 | Mević et al., 2026 / ECAI 2025 | InfineonのPVD、複数位置の膜厚、XGB・ProjSe・木モデルの変数選択比較。AlCu 4,848 Wafer/97変数/17出力、WTi 1,740 Wafer/108変数/17出力。AlCuのXGB R²は全変数0.71、XGB選択後0.75 | 目的は主に膜厚であり、抵抗直接予測の結果ではない |
| P2 | Susto et al., 2015 | 複数工程にまたがるVM。高次元の正則化＋多段工程の説明変数構造 | 抵抗特定箇所への転用は別途検証 |
| P3 | Yang et al., 2019 | Gaussian Bayesian Network→Markov Blanket→予測。QC間の関係と候補選択に極めて近い | ネットワークのエッジを因果と即断しない |
| P4 | Han et al., 2025 | CMP、Online Gaussian Process、ドリフト、予測不確実性を用いた動的サンプリング | 主眼はオンライン運用・追加測定 |
| P5 | Wafer-Level Characteristic Variation Modeling..., 2024 | ウエハ面内の滑らかな変動＋Shotの不連続系統変動。産業データで誤差36%以上低減 | 対象の電気抵抗と空間構造が同一とは限らない |

論文P1に関して、先の回答にある「2026年発表」はオンライン公開日のこと。論文は **ECAI 2025のプロシーディングに属し、Web公開は2026-08-25**。混同に注意。P1のR²改善は**AlCuの膜厚マルチ出力実験**であり、抵抗で同じ改善幅を期待する根拠ではない。

## 9. 実装・検証の推奨ロードマップ

### Step 1: 抵抗の定義とデータ辞書
- Rの単位・対象構造・Site・測定工程・規格・測定の繰り返し精度を明示。
- QC台帳から、取得可能時点・物理グループ・Lot/Wafer/Tool/Chamber/Recipe/座標を揃える。

### Step 2: QC関係性の可視化
- 分布、測定単位ごとの欠損、散布図、Pearson/Spearman、相関クラスタ、Graphical Lasso。
- 同じTool等の群内・群間差を比較し、QCネットワークを描く。

### Step 3: 交絡診断
- DAG（工程常識に基づく仮説）を作り、共通原因・媒介・コライダーを分類。
- LMM/GLMM・Within-BetweenでQC-R関係を比較。
- 時間・Recipe・装置状態により符号が反転していないか確認。

### Step 4: 交互作用探索
- 事前候補ペア＋EBM/GA2M＋CatBoost Interactionで上位ペア。
- 疎な領域を明示した2D可視化。
- glinternet/hierNetで変数選択→別データで交互作用の再検証。

### Step 5: 安定性評価・モデル化
- Stability Selection、group importance、mRMR/Elastic Netで候補圧縮。
- LMM/GAM/EBM/LightGBMの性能比較。
- Lot group split + 時間方向holdout、必要ならTool holdout。
- MAE/RMSE/R²、Tool別・Chamber別・Wafer/Shot別誤差、時間ドリフトを記録。

### Step 6: 量産での使用判断
- 高誤差条件の特定、PM・Recipe改定時の再評価。
- 因果的な工程改善が目的なら、現場で実施可能なDOE・限定介入で検証。

### 出力テーブル（推奨スキーマ）

| QC | 工程/物理群 | 単変量関連 | 交絡調整後の関連 | 主要交互作用 | 選択頻度 | 期間外テストの貢献 | 物理仮説 |
|---|---|---|---|---|---|---|---|
| QC-A | 例：CD | Spearman など | β, CI, p 等 | QC-C | 0–1 | ΔMAE | 作用経路メモ |

注：数値はデータ取得後に計算。関連係数の「有意」と予測性能向上の「実用性」は別判断。

## 10. 文献一覧：前回挙げた論文および各手法の主要原著

### A. 半導体VM・実製造・空間構造

**[P1]** Mević, A., Laber, A., & Krivić, S. (ECAI 2025 proceedings; online 2026-08-25). *Application of Multi-Output Regression and Feature Selection Methods in Semiconductor Manufacturing*. DOI: https://doi.org/10.3233/FAIA251482  
→ PVD（AlCu/WTi）・多出力膜厚予測・ProjSe/DT/RF/XGBによる変数選択、安定性・実行時間。

**[P2]** Susto, G. A., Pampuri, S., Schirru, A., Beghi, A., & De Nicolao, G. (2015). *Multi-step virtual metrology for semiconductor manufacturing: A multilevel and regularization methods-based approach*. Computers & Operations Research. DOI: https://doi.org/10.1016/j.cor.2014.05.008  
→ 過去工程情報と高次元正則化、マルチレベル構成。

**[P3]** Yang, W.-T., et al. (2019). *A Structure Data-Driven Framework for Virtual Metrology Modeling*. IEEE Transactions on Automation Science and Engineering. DOI: https://doi.org/10.1109/TASE.2019.2941047  
→ Gaussian Bayesian Network、Markov Blanket、CMP実データの物理的解釈。

**[P4]** Han, X., Miller, M., Moyne, J., Vogl, G. W., Penkova, A., & Jia, X. (2025). *A Comparative Study of Semiconductor Virtual Metrology Methods and Novel Algorithmic Framework for Dynamic Sampling*. IEEE Transactions on Semiconductor Manufacturing, 38(2). DOI: https://doi.org/10.1109/TSM.2025.3531920  
→ Online Gaussian Process、データドリフト、不確実性・動的サンプリング。NIST: https://www.nist.gov/publications/comparative-study-semiconductor-virtual-metrology-methods-and-novel-algorithmic

**[P5]** (2024). *Wafer-Level Characteristic Variation Modeling Considering Systematic Discontinuous Effects*. IEICE Transactions on Fundamentals, E107-A(1). https://www.jstage.jst.go.jp/article/transfun/E107.A/1/E107.A_2023KEP0010/_article  
→ Gaussian Process＋Shot依存の不連続な系統変動。位置データに有用。

### B. QCの関係・変数選択・安定性

**[M1]** Friedman, J., Hastie, T., & Tibshirani, R. (2008). *Sparse inverse covariance estimation with the graphical lasso*. Biostatistics, 9(3), 432–441. DOI: https://doi.org/10.1093/biostatistics/kxm045  
→ Graphical Lasso。

**[M2]** Peng, H., Long, F., & Ding, C. (2005). *Feature selection based on mutual information: criteria of max-dependency, max-relevance, and min-redundancy*. IEEE TPAMI, 27(8), 1226–1238. DOI: https://doi.org/10.1109/TPAMI.2005.159  
→ mRMR。

**[M3]** Meinshausen, N., & Bühlmann, P. (2010). *Stability selection*. JRSS Series B, 72(4), 417–473. DOI: https://doi.org/10.1111/j.1467-9868.2010.00740.x  
→ 再標本化に基づく安定変数選択。

**[M4]** Chamma, A., Thirion, B., & Engemann, D. (2024). *Variable Importance in High-Dimensional Settings Requires Grouping*. AAAI 2024, 38(10), 11195–11203. DOI: https://doi.org/10.1609/aaai.v38i10.28997  
→ BCPI: Block-Based Conditional Permutation Importance。

### C. 交互作用検出・解釈

**[I1]** Bien, J., Taylor, J., & Tibshirani, R. (2013). *A Lasso for Hierarchical Interactions*. Annals of Statistics, 41(3), 1111–1141. DOI: https://doi.org/10.1214/13-AOS1096  
→ hierNet、階層制約のある交互作用選択。

**[I2]** Lim, M., & Hastie, T. (2015). *Learning Interactions via Hierarchical Group-Lasso Regularization*. Journal of Computational and Graphical Statistics, 24(3), 627–654. DOI: https://doi.org/10.1080/10618600.2014.938812  
→ glinternet、カテゴリ×連続も扱える強階層。

**[I3]** Lou, Y., Caruana, R., Hooker, G., & Gehrke, J. (2013). *Accurate Intelligible Models with Pairwise Interactions*. KDD 2013. https://www.microsoft.com/en-us/research/publication/accurate-intelligible-models-pairwise-interactions/  
→ GA2M、FASTで候補ペアをランキング。

**[I4]** Nori, H., Caruana, R., Bu, Z., Shen, J. H., & Kulkarni, J. (2021). *Accuracy, Interpretability, and Differential Privacy via Explainable Boosting*. ICML/PMLR 139, 8227–8237. https://proceedings.mlr.press/v139/nori21a.html  
→ EBM関連研究。実装ドキュメント: https://interpret.ml/docs/ebm.html

**[I5]** Lundberg, S. M., Erion, G. G., & Lee, S.-I. (2018). *Consistent Individualized Feature Attribution for Tree Ensembles*. arXiv:1802.03888. https://arxiv.org/abs/1802.03888  
→ TreeSHAP・SHAP Interaction Values。

**[I6]** Apley, D. W., & Zhu, J. (2020). *Visualizing the Effects of Predictor Variables in Black Box Supervised Learning Models*. JRSS Series B, 82(4), 1059–1086. DOI: https://doi.org/10.1111/rssb.12377  
→ ALE、PDPの問題点を補う可視化。

**[I7]** Prokhorenkova, L., Gusev, G., Vorobev, A., Dorogush, A. V., & Gulin, A. (2018). *CatBoost: unbiased boosting with categorical features*. NeurIPS 31. https://proceedings.neurips.cc/paper_files/paper/2018/hash/14491b756b3a51daac41c24863285549-Abstract.html  
→ CatBoostの原著。Feature Interactionの仕様: https://catboost.ai/docs/en/concepts/feature-interaction

### D. 因果構造・階層交絡

**[C1]** Zheng, X., Aragam, B., Ravikumar, P., & Xing, E. P. (2018). *DAGs with NO TEARS: Continuous Optimization for Structure Learning*. NeurIPS 31. https://papers.neurips.cc/paper_files/paper/2018/hash/e347c51419ffb23ca3fd5050202f9c3d-Abstract.html  
→ NOTEARSによるDAG探索。

**[C2]** Runge, J., Nowack, P., Kretschmer, M., Flaxman, S., & Sejdinovic, D. (2019). *Detecting and quantifying causal associations in large nonlinear time series datasets*. Science Advances, 5(11), eaau4996. DOI: https://doi.org/10.1126/sciadv.aau4996  
→ PCMCI。工程ごとの時系列の時間整列がある場合に候補。

**[C3]** Bell, A., & Jones, K. (2015). *Explaining Fixed Effects: Random Effects Modeling of Time-Series Cross-Sectional and Panel Data*. Political Science Research and Methods, 3(1), 133–153. DOI: https://doi.org/10.1017/psrm.2014.7  
→ Within-Betweenと相関した群効果を考える出発点。

**[C4]** Chernozhukov, V., Chetverikov, D., Demirer, M., Duflo, E., Hansen, C., Newey, W., & Robins, J. (2018). *Double/debiased machine learning for treatment and structural parameters*. The Econometrics Journal, 21(1), C1–C68. DOI: https://doi.org/10.1111/ectj.12097  
→ DMLによる高次元交絡調整（因果識別仮定が必要）。

### E. 追加の実装資料（論文ではなく公式ドキュメント）

- InterpretML / ExplainableBoostingRegressor: https://interpret.ml/docs/python/api/ExplainableBoostingRegressor.html
- CatBoost Pairwise Feature Interaction: https://catboost.ai/docs/en/concepts/feature-interaction
- CatBoost Feature Importance API: https://catboost.ai/docs/en/features/feature-importances-calculation
- 関連する先行調査（大規模センサ・階層データ・PLS・多段工程・ドリフトなど）：[既存リポジトリ内レポート](./semiconductor_hierarchical_modeling_research_report.md)

## 11. 実装候補のライブラリ（概念案）

- Python: pandas, scipy, statsmodels, scikit-learn, pygam（GAM）, interpret（EBM）, catboost, lightgbm, shap, PyMC, Tigramite（PCMCI）等
- R: lme4, mgcv, hierNet, glinternet、必要ならbnlearnなど
- Graphical Lasso: scikit-learn の GraphicalLasso系
- 選択安定性: Lot/時期をブロック化して自前で再標本化を実装してもよい
- P1のProjSeは多出力を要する時に優先検討

## 12. 解決すべき未確定情報

1. 抵抗の構造：金属配線／Via／コンタクト／拡散層／TEG／複合構造のどれか。
2. 教師データ粒度：製品×Wafer×Siteのどれか、目的変数のサンプル件数、測定誤差。
3. QC：どの工程まであるか、候補数、欠損、時間・座標、QCがロット/ウエハ/サイトのどの粒度か。
4. Tool/Chamber/Recipe/PMなどの紐付け可能性。
5. 最終用途：未測定抵抗の予測か、改善可能な因子の同定か（予測・因果の評価設計が変わる）。

---

**重要な読み方**：このレポートは「確認された原著」と「実務向け提案・仮説」を分けて記した。解析手法によって得られるのは、相関、条件付き依存、モデルの利用した交互作用、または仮定付きの因果推定であり、それぞれ同一ではない。報告中のデータ数とR²は引用研究の膜厚実験の値で、ユーザーの製品抵抗データに対する予測実績ではない。
