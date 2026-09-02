# 半導体 Virtual Metrology / Yield Prediction コンペ・公開データセット調査

更新日: 2026-09-02

## 0. Executive Summary

半導体製造での予測タスクを広く、

- **狭義VM (Virtual Metrology)**: FDC / Recipe / 装置センサー → 後工程の膜厚・CD・Etch depth等の実計測値
- **Yield / Predictive Quality**: 工程・装置データ → Pass/Fail、Yield、Defect、Quality excursion
- **Equipment Health**: FDC時系列 → 異常・故障・RUL

まで含めて調査した。

公開データは量産Fabの機密性から非常に少ないが、2025–2026年にかなり良質なデータが公開され始めている。

### 結論: まず触るべき順

|順位|データ / コンペ|タスク|半導体|実データ|VM/Yieldへの近さ|一言|
|---|---|---|---|---|---|---|
|1|Infineon PVD APC/SPC Thickness Dataset|膜厚VM|Yes|Yes|★★★★★|現在もっとも素直な公開VMデータ|
|2|BOSCH Plasma Etching Dataset|Etch depth / Uniformity VM|Yes|Yes|★★★★★|OES＋FDC＋wafer metrologyの高品質データ|
|3|PHM 2016 CMP Data Challenge|MRR VM|Yes|Yes|★★★★★|古いが「VMコンペ」そのもの|
|4|SECOM Defect Detection Challenge|Pass/Fail / Yield|Yes|Yes|★★★★☆|2026年現在Kaggleで参加可能|
|5|Phototransistor VM 2026|Gain VM|Yes|Yes|★★★★★|小標本・階層ベイズに非常に良い|
|6|WM-811K|Wafer yield map / defect pattern|Yes|Yes|★★★☆☆|Yield diagnosis向け、大規模811k wafers|
|7|UCR/UEA Wafer|FDC時系列異常|Yes|Yes|★★★☆☆|センサー波形モデルの練習向け|
|8|PHM 2018 Ion Mill Etch|Fault / RUL|Yes|Yes|★★★☆☆|装置Health/RUL、複数Tool差がある|
|9|Bosch Production Line Performance|Failure prediction|No|Yes|★★★☆☆|100万件超、工程Routeと極端な不均衡|
|10|InduTS-SS|Soft Sensor|No|Yes/benchmark|★★★★☆|VMのモデル比較環境として優秀|

**実際に1つ選ぶなら:**

- 「VMを作りたい」→ **Infineon PVD thickness**
- 「FDC時系列をちゃんと扱いたい」→ **BOSCH Plasma Etching**
- 「コンペ形式でやりたい」→ **SECOM Defect Detection Challenge**
- 「階層ベイズを試したい」→ **Phototransistor VM 2026**
- 「装置劣化まで含めたい」→ **PHM 2016 CMP / PHM 2018 Ion Mill**

---

# 1. Infineon PVD APC/SPC Thickness Dataset — 最優先

**分類:** 狭義VM  
**おすすめ:** ★★★★★  
**公開:** 2025-08-15  
**提供:** University of Sarajevo / Infineon Technologies Austria

Source:
- https://zenodo.org/records/16881338
- DOI: 10.5281/zenodo.16881338

## データ構造

PVD工程における装置内センサー集約値から、成膜後の膜厚を予測する。

```text
X: APC / equipment sensor summaries
   gas flow
   temperature
   voltage
   current
   ...
            ↓
      VM regression
            ↓
Y: post-process thickness at 17 wafer positions
```

2種類の膜が公開されている。

- AlCu
- WTi

Files:

- `X_pvd_AlCu.csv` (9.1 MB)
- `Y_pvd_AlCu.csv` (1.6 MB)
- `X_pvd_WTi.csv` (3.6 MB)
- `Y_pvd_WTi.csv` (560.7 kB)

Yには17点の実膜厚 `RAW_VALUE_t_i` が入る。

## なぜ重要か

これは非常にきれいな

> **FDC/APC features → SPC/metrology values**

の構造を持つ。

つまり半導体現場でいうVMをほぼそのまま再現できる。

さらに出力が17点なので、

- wafer average thickness
- center-edge difference
- non-uniformity
- 17-point structured prediction

まで試せる。

## 最初に試すモデル

Baseline:

- Ridge / ElasticNet
- PLS
- Random Forest
- LightGBM / XGBoost / CatBoost

Advanced:

- Multi-output regression
- PCA + Gaussian Process
- MLP
- Deep structured output
- Multi-task learning (17 points simultaneous)
- Conformal Prediction

## おすすめ評価

単純な17点平均RMSEだけでなく、

1. 17-point RMSE
2. Wafer mean thickness MAE
3. Wafer non-uniformity error
4. Edge/center error
5. Prediction interval coverage

を見る。

**このデータを最初のPoCにするのが一番おすすめ。**

---

# 2. BOSCH Plasma Etching Multi-Modal Dataset

**分類:** 狭義VM / FDC / Plasma modeling  
**おすすめ:** ★★★★★  
**公開:** 2025-09-15  
**提供:** Chemnitz University of Technology / Fraunhofer ENAS

Source:
- https://zenodo.org/records/17122442
- DOI: 10.5281/zenodo.17122442

## 内容

BOSCH深掘りEtch工程の実験データ。

Inputs:

- **OES: 3648波長 channel, 185–884 nm, 25 Hz**
- **31 machine/process parameters, 5 Hz**

Outputs:

- pre/post oxide thickness
- step height
- 9-point / 89-point wafer measurements
- etch depth
- uniformity
- selectivity を導出可能

データ総量は約7.9 GB。

## VMとしてのタスク

```text
OES time series + FDC/process variables
                    ↓
               representation
                    ↓
                VM model
                    ↓
etch depth / spatial uniformity / selectivity
```

これは公開データとしてはかなり珍しい、**in-situ high-frequency sensor + ex-situ wafer metrology**のセット。

## 特に研究価値が高いテーマ

- OESのみ vs FDCのみ vs OES+FDC
- PCA / NMF / AutoencoderによるOES圧縮
- TCN / Transformer / LSTM
- Multi-modal fusion
- chamber conditioning / drift
- wafer sequence effect
- spatially structured VM (89-point prediction)
- uncertainty-aware VM

## 注意

実験データであり、量産Fabの大量データではない。

しかし、公開VM研究用としてはかなり高品質。

---

# 3. PHM 2016 Data Challenge — CMP Material Removal Rate

**分類:** 狭義VM + Equipment degradation  
**おすすめ:** ★★★★★  
**Competition:** Closed（データと正解は公開）

Official:
- https://phmsociety.org/conference/annual-conference-of-the-phm-society/annual-conference-of-the-prognostics-and-health-management-society-2016/phm-data-challenge-4/

## 問題

CMP装置のRecipe・時系列センサーデータから、ウェハごとのAverage Material Removal Rateを予測。

```text
CMP recipe + sensor time series + tool state
                    ↓
                  model
                    ↓
       AVG_REMOVAL_RATE / wafer
```

Official pageにはTraining/Test/Validationだけでなく、Test/Validation answerも公開されている。

CMPでは、

- polishing pad
- dresser
- slurry
- carrier

などが使用とともに劣化するため、**Concept Drift / tool degradationを含むVM**になっている点が非常に良い。

## おすすめ研究課題

- handcrafted time-series features + LightGBM
- PLS / GP
- TCN / LSTM
- pad/dresser health latent state
- Just-in-Time VM
- time-aware CV
- drift-aware updating
- hierarchical / state-space models

## Validation

Random splitより、時間順holdoutを推奨。

VMの本質である

> 「過去の装置状態から未来の製品を予測できるか」

を見る。

---

# 4. SECOM Defect Detection Challenge — 2026年現在参加可能

**分類:** Yield / Pass-Fail prediction  
**おすすめ:** ★★★★★（コンペ形式）

Kaggle:
- https://www.kaggle.com/competitions/secom-defect-detection-challenge

Original UCI:
- https://archive.ics.uci.edu/dataset/179/secom

## 状況

2026-09-02調査時点でKaggleに `Join Competition` と表示されているCommunity Prediction Competition。

Metric:
- ROC-AUC

Prizes:
- Kudos only
- Kaggle points / medalsなし

## Original SECOM data

- 1,567 samples
- 約590 process/sensor features
- Missing values多数
- timestampあり
- Target: Pass / Fail
- Failは少数（強いclass imbalance）

## なぜ良いか

対象が連続Metrology値ではないので狭義VMではないが、実際の半導体予測で重要な

- 高次元
- n << p
- 欠損
- 不均衡
- feature selection
- Yield / quality prediction
- RCA候補抽出

を全部含む。

## 試すモデル

- Logistic + L1/L2
- PLS-DA
- Random Forest
- XGBoost / LightGBM
- CatBoost
- TabPFN系（小標本なので比較価値あり）

### 評価時の注意

ROC-AUCだけでなく、現場用途では

- PR-AUC
- Recall at fixed false-positive rate
- Cost-weighted threshold
- calibration

も見るべき。

---

# 5. Phototransistor Virtual Metrology 2026

**分類:** 狭義VM / hierarchical manufacturing data  
**おすすめ:** ★★★★★（階層ベイズ）

Paper:
- https://arxiv.org/abs/2608.11868

GitHub:
- https://github.com/mahshid-amirabgir/phototransistor-virtual-metrology

Zenodo:
- https://doi.org/10.5281/zenodo.21379925

## データ

実シリコン・バイポーラ・フォトトランジスタ製造履歴。

- Arm A: 260 wafers / 13 process runs
- Arm B: 285 wafers / 14 process runs
- Target: phototransistor GAIN
- Process recipe
- emitter sheet resistivity
- screen oxide thickness
- wafer position within run

元のdie-levelデータは約930万measurementsだが、公開データはwafer-levelに集約・normalize済み。

## 一番面白い点

製造階層が明確。

```text
Run
 └ Wafer
    └ Die
```

論文ではGain varianceのおよそ半分がrun間に存在する。

これは、

> 同じRecipeでもRun/Tool stateで品質が変わる

というVMの本質的問題。

## 最適な研究テーマ

- Mixed Effects
- Hierarchical Bayesian Regression
- Partial Pooling
- Gaussian Process
- Leave-One-Run-Out CV
- uncertainty-aware VM
- forward VM + inverse recipe search

Deep Learningより、階層ベイズを試す教材として価値が高い。

---

# 6. WM-811K Wafer Maps

**分類:** Yield diagnosis / failure pattern  
**おすすめ:** ★★★★☆

Kaggle:
- https://www.kaggle.com/datasets/qingyi/wm811k-wafer-map

## データ

- **811,457 wafer maps**
- 約172,950 wafer mapsに専門家ラベル
- 9 classes
  - Center
  - Donut
  - Edge-Loc
  - Edge-Ring
  - Loc
  - Near-Full
  - Random
  - Scratch
  - None
- CC0

wafer mapはdie単位Pass/Failの2D分布。

## 何に使えるか

これは「工程センサー→Yield予測」ではない。

代わりに、

- Yield map diagnosis
- Failure pattern classification
- Failure mode discovery
- Semi-supervised learning
- representation learning
- defect spatial clustering

に非常に良い。

「なぜYieldが落ちたか」を空間Patternから分類する研究向け。

---

# 7. UCR/UEA Wafer Time-Series Dataset

**分類:** Semiconductor FDC anomaly  
**おすすめ:** ★★★☆☆

Zenodo:
- https://zenodo.org/records/11198387

Multivariate conversion:
- https://zenodo.org/records/10839966

## 内容

半導体製造中にセンサーから取得されたinline process control measurement。

Task:
- Normal / Abnormal classification

元データはunivariate time-series benchmarkとして有名。

多変量版も公開されている。

## 使い道

- TCN / Transformer / 1D-CNN
- Time-series anomaly classification
- FDC representation learning
- pretrained TS modelsの比較

Yield predictionではないが、「波形をどう表現するか」の検証に使いやすい。

---

# 8. PHM 2018 Data Challenge — Ion Mill Etching

**分類:** Equipment Health / RUL  
**おすすめ:** ★★★★☆

Official:
- https://phmsociety.org/conference/annual-conference-of-the-phm-society/annual-conference-of-the-prognostics-and-health-management-society-2018-b/phm-data-challenge-6/

## Task

Ion Mill Etching Toolの多変量時系列から、

1. failure diagnosis
2. remaining useful life

を予測。

複数のtool・operating condition・failure modeが含まれる。

VMではないが、装置FDCにおける

- Tool差
- operating-mode差
- degradation onset
- RUL
- online prediction

の教材として良い。

PHM 2016 CMPと組み合わせると、

```text
PHM 2016: process → product quality
PHM 2018: process → equipment health
```

の両側を学べる。

---

# 9. Bosch Production Line Performance

**分類:** Manufacturing Predictive Quality  
**半導体:** No  
**おすすめ:** ★★★★☆

Kaggle:
- https://www.kaggle.com/competitions/bosch-production-line-performance

## 規模

- Train: 1,183,747 parts
- Positive failure: 6,879 (~0.58%)
- Numeric / categorical / date features
- Station / Line構造あり
- Metric: Matthews Correlation Coefficient

2026年現在Late Submission可能。

## 半導体への転用価値

非常に大規模で、

- 部品ごとに通る工程が違う
- missing pattern自体が工程Routeを表す
- station structure
- severe imbalance
- time proximity

があり、Fabのprocess-route × yield predictionにかなり近い。

ただし半導体ではない。

---

# 10. InduTS-SS — VMモデル選定の練習基盤

**分類:** Industrial Soft Sensor benchmark  
**おすすめ:** ★★★★☆

GitHub:
- https://github.com/YuAn-06/Industrial-Time-Series-Soft-Sensor

2026-05に初版公開、2026-07まで活発に更新。

## 対応データ例

- Debutanizer Column
- Sulfur Recovery Unit
- Ironmaking
- Mining Process
- Power Plant Gas Turbine
- Tennessee Eastman

Task:

- Soft Sensor Regression
- Soft Sensor Forecasting

Soft Sensorは数理的にはVMとほぼ同じ。

```text
cheap/on-line process sensors
            ↓
          model
            ↓
expensive/delayed quality measurement
```

## 利点

dataset split、scaling、training、metricsが統一されているため、モデル比較を素早くできる。

VM候補モデルをInduTS-SSでbenchmarkしてから半導体データへ持ち込む使い方がおすすめ。

---

# 11. 注意: 出所不明・合成半導体Yield Dataset

Kaggleには2026年現在、

- Semiconductor Yield
- Semiconductor Sensor Data for Predictive Quality
- Fab Yield Prediction

等の名前で複数のデータが存在する。

しかし、説明には「semiconductor fabrication environment」と書かれていても、

- 元論文なし
- 企業/装置不明
- License unknown
- simulated dataと明記
- 物理的に不自然な列構造

のものがある。

したがって本レポートでは、**実Fabデータとして根拠を確認できないものを主推薦から除外**した。

学習用のsynthetic benchmarkとして使うのは問題ないが、

> 「この精度なら実Fabでも使える」

という評価には使用しない方がよい。

---

# 12. ﾓﾁｭ向けおすすめ実験ロードマップ

## Stage 1 — 一番VMらしいデータでBaseline

**Infineon PVD thickness**

目的:

```text
APC/FDC features → 17-point thickness
```

比較:

1. PLS
2. Ridge
3. LightGBM
4. CatBoost
5. MLP

まずDeep Learningは不要。

### Metrics

- 17-point mean MAE/RMSE
- wafer average thickness MAE
- non-uniformity MAE
- R²

---

## Stage 2 — 不確実性を付ける

同データで、

- Quantile LightGBM
- NGBoost
- Gaussian Process
- Conformal Prediction

を比較。

「平均精度」だけではなく、

> **Prediction intervalがSpecを跨ぐwaferを追加測定へ回す**

というVMらしい意思決定まで作る。

---

## Stage 3 — 高次元FDC / 時系列

**BOSCH Plasma Etch**

比較:

```text
Summary statistics + LightGBM
vs
PCA/NMF + ML
vs
TCN
vs
Transformer
```

OESは3648 channelなので、まずrepresentation learningの方が重要。

---

## Stage 4 — Tool / Run階層を入れる

**Phototransistor VM**

比較:

```text
pooled regression
vs
run dummy
vs
mixed effects
vs
hierarchical Bayes
```

ここでPartial Poolingの価値を確認する。

---

## Stage 5 — Yield prediction

**SECOM Kaggle**へ参加。

目的:

```text
590 sensors → Pass/Fail
```

精度だけでなく、

- PR-AUC
- calibration
- SHAP / permutation importance
- model disagreement

まで作る。

最終的には、

> VM値予測 + Yield prediction + uncertainty

を同じpipelineで扱える設計にする。

---

# 13. 個人的な研究テーマ候補

公開データを使うなら以下が面白い。

## A. Hierarchical Virtual Metrology

```text
Global model
 + Tool effect
 + Chamber effect
 + Recipe effect
 + Run effect
```

を階層ベイズで学習。

少数データのToolでもpartial poolingする。

## B. Uncertainty-aware VM / Selective Metrology

VMを「測定値の代替」にするだけでなく、

```text
VM prediction
+ uncertainty
→ skip / sample / full metrology
```

まで最適化。

## C. Drift-aware VM

PM前後、Chamber age、材料Lot変化でVMが劣化する問題を扱う。

- ADWIN / CUSUM
- coverage monitoring
- rolling retraining
- conformal recalibration

## D. Multi-task VM

17点膜厚を別々に予測せず、wafer spatial profileを一括予測。

## E. VM + Yield joint modeling

```text
FDC
 ├→ metrology VM
 └→ Yield
```

または

```text
FDC → VM → Yield
```

とし、VM predictionをYield modelの中間表現に使う。

## F. RCAまでつなぐ

```text
FDC → VM error / Yield risk
             ↓
      feature attribution
             ↓
   Process / Tool候補
```

単なる予測モデルではなく、原因候補のランキングまで作る。

---

# 14. 最終推奨

今すぐ1つ始めるなら、**Infineon PVD APC/SPC Thickness Dataset**が最も良い。

理由:

1. 半導体実データ
2. Xが装置センサー/FDC相当
3. Yが実膜厚
4. 17-pointでspatial VMまでできる
5. CSVで扱いやすい
6. データ量も約15 MBと軽い
7. 学習モデルから不確実性、Selective Metrologyまで発展できる

次にBOSCH Plasma Etchを使い、時系列・OES・driftを追加する。

歩留まり予測をやりたい場合は、現在参加可能な **SECOM Defect Detection Challenge** を並行して使うのが良い。

最終的には、

```text
Infineon PVD        → 狭義VM
BOSCH Plasma Etch   → 時系列 / multimodal VM
Phototransistor     → hierarchical VM
SECOM               → Yield prediction
PHM 2018            → Equipment health
```

を1つの製造AI benchmark suiteとして扱うと、かなり面白いポートフォリオ/研究になる。

---

# Sources

- Infineon PVD APC/SPC Thickness Dataset: https://zenodo.org/records/16881338
- BOSCH Plasma Etching Dataset: https://zenodo.org/records/17122442
- PHM 2016 CMP Data Challenge: https://phmsociety.org/conference/annual-conference-of-the-phm-society/annual-conference-of-the-prognostics-and-health-management-society-2016/phm-data-challenge-4/
- SECOM Kaggle Challenge: https://www.kaggle.com/competitions/secom-defect-detection-challenge
- UCI SECOM: https://archive.ics.uci.edu/dataset/179/secom
- Phototransistor VM paper: https://arxiv.org/abs/2608.11868
- Phototransistor VM GitHub: https://github.com/mahshid-amirabgir/phototransistor-virtual-metrology
- Phototransistor VM Zenodo: https://doi.org/10.5281/zenodo.21379925
- WM-811K: https://www.kaggle.com/datasets/qingyi/wm811k-wafer-map
- UCR Wafer Zenodo: https://zenodo.org/records/11198387
- PHM 2018 Ion Mill Etch Challenge: https://phmsociety.org/conference/annual-conference-of-the-phm-society/annual-conference-of-the-prognostics-and-health-management-society-2018-b/phm-data-challenge-6/
- Bosch Production Line Performance: https://www.kaggle.com/competitions/bosch-production-line-performance
- InduTS-SS: https://github.com/YuAn-06/Industrial-Time-Series-Soft-Sensor
