# 半導体製造における大量センサ × 階層データの予測モデリング調査

## 1. 結論

半導体製造のように、**装置センサ → 工程内寸法・膜厚などのメトロロジー → 電気特性 → 歩留まり**という多段階の因果・情報構造があり、さらに装置・チャンバ・レシピ・製品・Lot・Waferなどの階層を持つ問題では、全変数を1枚の巨大な表にして単一モデルへ投入する構成は、精度・解釈性・運用安定性のいずれでも不利になりやすい。

推奨は次の3点である。

1. **工程ごとにセンサ情報を圧縮する**
   - 手作り統計量、PLS、Sparse PCA、Elastic Net、1D-CNN/TCNなどを工程特性に応じて使い分ける。
2. **装置・チャンバ・レシピ・製品などの階層を明示的にモデル化する**
   - Mixed Effects、階層ベイズ、Multi-task Learning、あるいはGBDT + 階層残差補正を使う。
3. **予測値だけでなく不確実性・ドリフト・OODを出す**
   - 物理メトロロジーの追加測定対象選択や再学習トリガーに利用する。

実務上は、まず **PLS/Elastic Net + LightGBM/CatBoost + 階層効果** の強いベースラインを作り、その後に時系列深層学習やGNNを追加し、Tool holdout・Time holdoutで本当に改善するか確認するのがよい。

---

## 2. 半導体製造データで難しい理由

### 2.1 高次元・少数サンプル

装置1台あたり数百〜数千センサを持ち、各センサが時系列になると、1 wafer/runあたりの候補特徴量は数万〜数十万次元に達する。一方で、実際に品質ラベルが付くwaferはメトロロジーのサンプリング率が低く、特に新規製品・新規装置では `p >> n` になりやすい。

また、同一Lot内waferや同一Toolで連続処理されたwaferは相関が強いため、見かけ上のサンプル数より**有効サンプルサイズは小さい**と考えるべきである。

### 2.2 データが階層構造を持つ

典型的には以下の階層が存在する。

- Fab
- Process / Layer / Operation
- Tool
- Chamber / Module
- Recipe
- Product / Device / Technology node
- Lot
- Wafer
- Site / Die

同じセンサ値でもToolやRecipeが違えば意味が変わることがある。単純なOne-hotや全カテゴリ別モデルでは、データが少ない群で過学習しやすい。

### 2.3 分布が時間とともに変わる

半導体製造では以下により分布が動く。

- PM前後
- Consumable交換
- Chamber clean
- Tool matching調整
- Recipe改版
- 装置経時変化
- センサ交換・校正
- 製品mix変化

そのため、ランダム分割だけで高精度でも、実運用では急激に崩れることがある。

### 2.4 工程間で情報が伝播する

歩留まりは1工程だけで決まらない。上流工程で生じた微小な偏差が、後工程の寸法・電気特性を介して最終歩留まりへ効くため、**工程単体モデル + 工程間統合**の2段構成が自然である。

---

## 3. 推奨データ設計

中心となるキーは **1 wafer × 1 process step/run** とする。

### 3.1 工程内情報

- 生センサ時系列
- Setpoint
- Recipe parameters
- Alarm / Event
- 処理時間
- Step/Phase区間

### 3.2 階層情報

- Tool ID
- Chamber ID
- Recipe ID
- Product ID
- Layer / Process ID
- Lot ID
- PM state
- Run count since PM

### 3.3 上流履歴

- 上流工程の実測メトロロジー
- 上流工程のVirtual Metrology
- 上流工程の異常スコア
- Tool/Chamber履歴

### 3.4 教師ラベル

- 寸法/CD/膜厚
- WAT/電気特性
- Defect count
- Bin/yield
- 最終歩留まり

重要なのは、生時系列をすべて横持ちにするのではなく、**工程別Feature Store / Embedding Store**として管理することである。

---

## 4. センサ時系列の表現方法

### 4.1 まず作るべき手作り特徴

各工程Phaseごとに以下を抽出する。

- mean / median
- std / MAD
- min / max / range
- start / end value
- slope
- integral / area
- time above threshold
- overshoot
- settling time
- peak location
- FFT band power
- Phase間差分

これは単純だが非常に強い。工程知識を直接反映でき、特徴量重要度も説明しやすい。

### 4.2 PLS / Sparse PLS

PLSは、説明変数が高次元・多重共線で、教師ラベルが少ないVirtual Metrologyに非常に相性がよい。

利点:

- センサ間の強い相関を圧縮
- 目的変数を意識した低次元化
- 小規模データでも比較的安定
- Loadingsから解釈できる

最初の強いベースラインとして推奨する。

### 4.3 PCA / Sparse PCA / MPCA

ラベルが少ない場合は、まず教師なしでセンサを圧縮する方法も有効である。

特にSparse PCA系は、重要センサを少数へ絞りながら低次元化できるため、Virtual MetrologyやFDCで実務価値が高い。

時系列プロセスでは、バッチ工程用のMPCAやDynamic Sparse PCAも候補になる。

### 4.4 LASSO / Elastic Net / Fused Lasso

`p >> n` かつ説明性を重視する場合に有効。

特に時間順序を持つ分光・波形データではFused Lassoが有効で、隣接時刻の係数をまとめて選択できる。

### 4.5 1D-CNN / TCN

波形形状自体が重要な場合は、Transformerより先に1D-CNN/TCNを試す価値が高い。

理由:

- 局所パターンの抽出が得意
- Transformerより少ないデータでも学習しやすい
- 推論負荷が比較的小さい
- 工程Phaseに対応した特徴を学習しやすい

### 4.6 Transformer

長距離依存や多変量時系列の複雑な関係を扱えるが、ラベル数が少ない半導体VMでは必ずしも第一選択ではない。

使うなら、Self-supervised pretrainingやMasked reconstructionなどで大量のラベルなしセンサログを事前学習し、そのEmbeddingを下流モデルへ渡す構成が現実的である。

---

## 5. 階層構造の扱い

### 5.1 Mixed Effects / 階層ベイズ

最も自然な基本形は次である。

\[
y_i = f(x_i) + \alpha_{tool[t_i]} + \alpha_{chamber[c_i]} + \alpha_{recipe[r_i]} + \alpha_{product[p_i]} + \epsilon_i
\]

各群効果に

\[
\alpha_g \sim \mathcal{N}(0, \sigma_g^2)
\]

のような事前分布を置く。

これにより、データが少ないToolやRecipeは全体平均へShrinkし、データが多い群だけ個別性を強く持つ。これは**partial pooling**の効果であり、単純One-hotより新規群・少数群へ強い。

### 5.2 Random slope

Toolごとにセンサ感度が異なる場合は、切片だけでなく傾きも階層化する。

例:

\[
y = \beta x + b_{0,tool} + b_{1,tool}x + \epsilon
\]

これにより「同じセンサ変化でもTool AとTool Bで品質への影響が違う」を表現できる。

### 5.3 GBDT + 階層残差補正

実務では、LightGBM/CatBoostで非線形を取りつつ、残差へMixed Effectsを追加する構成も扱いやすい。

1. GBDTで `f(x)` を学習
2. 残差にTool/Chamber/RecipeのRandom Effectsを推定
3. 合算して最終予測

精度と解釈性のバランスがよい。

### 5.4 Multi-task Learning

Tool別・製品別に予測タスクを分けつつ、Encoderを共有する。

- Shared encoder
- Tool-specific head
- Product-specific head

のような形にすれば、データの多い群から少ない群へ表現を共有できる。

---

## 6. 工程間の統合

推奨アーキテクチャは以下。

```text
Raw sensor traces
      ↓
Stage Encoder Bank
  - Phase statistics
  - PLS / Sparse PCA
  - 1D-CNN / TCN
      ↓
Stage Embedding (20–200D程度)
      ↓
Hierarchical Fusion
  - Tool / Chamber
  - Recipe / Product
  - Lot / Layer
  - PM / Time state
      ↓
Multi-head Prediction
  ├─ Virtual Metrology
  ├─ WAT / electrical
  ├─ Yield
  └─ FDC / anomaly
      ↓
Uncertainty / OOD / Drift score
```

「各工程を数十〜数百次元の意味ある表現へ圧縮し、その後に工程間情報を統合する」という考え方が重要である。

---

## 7. 高次元問題でのモデル選択指針

### nが数百〜数千程度

- 工程知識でSensor groupを限定
- Phase統計
- PLS / Elastic Net
- Sparse PCA
- 少数のRandom Effects

深層学習は後回し。

### nが数千〜数万

- Screening
- LightGBM / CatBoost
- 階層効果
- 限定した交互作用
- Multi-task learning

### 波形形状が本当に重要

- 1D-CNN / TCN
- 必要ならTransformer
- Encoder出力は低次元Embeddingとして下流へ渡す

### 新規Tool / Recipeへ展開したい

- Partial pooling
- Domain adaptation
- Active learning
- Uncertainty-aware sampling

---

## 8. ドメインシフトと新規装置対応

新規ToolやPM後は、既存モデルをそのまま使うと性能が落ちることがある。

有効な手法は以下。

### 8.1 Moving window / Recursive update

古いデータを徐々に忘れ、最新のプロセス状態へ追従する。Recursive PLSなどは古典的だが、半導体VMで実績がある。

### 8.2 Domain adaptation

既存Toolで学習した特徴表現を、新規Toolへ合わせる。

- CORAL
- MMD
- adversarial domain adaptation
- feature normalization

などが候補。

### 8.3 Active learning

不確実性が高いwaferだけ実測メトロロジーへ回す。

全waferを測る必要がなくなり、ラベル取得コストを抑えながらモデルを更新できる。

### 8.4 Uncertainty-aware VM

Gaussian Process、Deep Ensemble、Conformal Predictionなどで予測区間を出し、信頼できない予測を自動的に除外する。

---

## 9. 検証方法

### 9.1 Random splitは原則禁止

隣接wafer・同一Lot・同一ToolがTrain/Testへ混ざると、実運用よりかなり楽な問題になる。

推奨:

- Time-block CV
- Grouped Lot CV
- Tool/Chamber holdout
- Product/Recipe holdout

### 9.2 評価指標

単なるRMSE/R²だけでは不足する。

- Overall RMSE / MAE / R²
- Worst Tool error
- Worst Product error
- Time bucket error
- PM前後error
- Calibration
- OOD rejection performance
- Improvement reproducibility

### 9.3 Leakageチェック

特に以下は危険。

- 目的変数測定後に得られる特徴
- 未来データを含むRolling statistics
- 同一Lotの別waferの正解値
- 全データでfitしたPCA / scaler / imputer
- Test側のtarget encoding
- 下流工程の情報を上流予測へ使用
- 重複・ほぼ重複したtraceがTrain/Testへ分離

---

## 10. 解釈性

半導体製造ではモデル精度だけでなく、原因究明へつなげる必要がある。

推奨する解釈階層:

1. Sensor importance
2. Phase × Sensor importance
3. Interaction
4. Tool-specific sensitivity
5. Process / physics interpretation
6. DOE / A-B testで検証

SHAPやPDPは「予測上の寄与」を示すだけで、因果効果を保証しない。改善施策へ落とす場合は、最終的にDOE・工程知識・物理モデルで検証する必要がある。

---

## 11. 実務PoCの進め方

### Model A: 説明性ベースライン

- Phase statistics
- Group-wise screening
- PLS / Elastic Net
- Tool/Chamber hierarchy

### Model B: 精度ベースライン

- Model A特徴
- LightGBM / CatBoost
- Tool / Product / Recipe interaction
- Grouped SHAP

### Model C: 時系列表現学習

- Raw traces / Phase sequences
- 1D-CNN / TCN
- 32–128D embedding
- Model Bへ追加

比較解釈:

- A ≈ B → 強い非線形は不要
- B ≫ A → 非線形・交互作用が重要
- C ≫ B → 波形形状が重要
- Tool holdoutだけ崩壊 → 階層化 / Domain adaptationが最優先

---

## 12. 推奨する最終構成

最終的には以下のようなシステムが実務に適する。

```text
[Raw Trace / Recipe / Context]
            ↓
[Process-specific Encoder]
            ↓
[Compact Stage Representation]
            ↓
[Hierarchical + Cross-stage Fusion]
            ↓
[VM / Electrical / Yield / FDC Heads]
            ↓
[Uncertainty + Drift + OOD]
            ↓
[Physical Metrology / Engineer Review / APC]
```

巨大なEnd-to-Endモデル1本ではなく、**工程ごとの局所モデルと、全工程をつなぐ統合モデルを分ける**ことで、再学習・説明・デバッグ・工程展開が容易になる。

---

## 13. 参考文献・関連研究

1. Maitra, Su, Shi. *Virtual metrology in semiconductor manufacturing: Current status and future prospects.* Expert Systems with Applications, 247, 123559, 2024. DOI: `10.1016/j.eswa.2024.123559`
2. Chen, Qin, Xu. *A multimodal hierarchical learning approach for virtual metrology in semiconductor manufacturing.* Journal of Manufacturing Systems, 80, 194–205, 2025. DOI: `10.1016/j.jmsy.2025.02.010`
3. Wang et al. *Dynamic sparse PCA: a dimensional reduction method for sensor data in virtual metrology.* Expert Systems with Applications, 251, 123995, 2024. DOI: `10.1016/j.eswa.2024.123995`
4. *True sparse PCA for reducing the number of essential sensors in virtual metrology.* International Journal of Production Research, 62(6), 2142–2157, 2024. DOI: `10.1080/00207543.2023.2217282`
5. Khan, Moyne, Tilbury. *Virtual metrology and feedback control for semiconductor manufacturing processes using recursive partial least squares.* Journal of Process Control, 18(10), 961–974, 2008. DOI: `10.1016/j.jprocont.2008.04.014`
6. *Virtual metrology modeling of time-dependent spectroscopic signals by a fused lasso algorithm.* 2016.
7. *Multilevel Kernel Methods for Virtual Metrology in Semiconductor Manufacturing.* IFAC, 2011. DOI: `10.3182/20110828-6-IT-1002.01339`
8. *A hierarchical model-based method for wafer level virtual metrology under process information deficiency.* Quality Engineering, 36(3), 2024. DOI: `10.1080/08982112.2023.2252891`
9. Shim, Kang. *Domain-adaptive active learning for cost-effective virtual metrology modeling.* Computers in Industry, 135, 103572, 2022. DOI: `10.1016/j.compind.2021.103572`
10. NIST. *A Comparative Study of Semiconductor Virtual Metrology Methods and Novel Algorithmic Framework for Dynamic Sampling.* 2025.
11. Fan, Chang. *An integrated advanced process control framework using run-to-run control, virtual metrology and fault detection.* Journal of Process Control, 23(7), 933–942, 2013. DOI: `10.1016/j.jprocont.2013.03.013`
12. Arpitha, Pani. *Machine Learning Approaches for Fault Detection in Semiconductor Manufacturing Process: A Critical Review.* Chemical and Biochemical Engineering Quarterly, 36(1), 1–16, 2022. DOI: `10.15255/CABEQ.2021.1973`

---

## 14. 次に実データへ落とす場合の確認項目

実データで設計する際は、少なくとも以下を整理するとモデル構成をかなり具体化できる。

- 目的変数: 寸法 / WAT / Yield / defect など
- 1目的変数あたりのラベル件数
- Sensor数とサンプリング周期
- 工程数
- Tool / Chamber数
- Recipe / Product数
- Lot/Wafer相関
- PM周期
- Metrology sampling rate
- 新規Tool / 新製品への展開要否
- モデル更新周期
- 推論速度制約

この情報が揃えば、**どの工程にPLSを使い、どこをLightGBMにし、どこだけ時系列Encoderを使うか**まで具体的に設計できる。
