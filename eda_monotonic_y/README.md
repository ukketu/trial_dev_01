# Yに対する単調関係EDA

大量の数値変数 `X1, X2, ...` から、目的変数 `Y` に対して

- 単調増加（線形候補）
- 単調増加（非線形候補）
- 単調減少
- Spearmanでは弱いがMIが高い非単調な依存候補

をスクリーニングするための最小構成です。

## 役割分担

| 指標 | 見ているもの | 主な用途 |
|---|---|---|
| Pearson | 値そのものの一次直線的な共変動 | 線形関係の強さ |
| Spearman | 順位の単調な共変動 | 単調増加・単調減少の探索 |
| MI (Mutual Information) | Xを知ったときYの不確実性がどれだけ減るか | U字型など相関で拾いにくい依存関係の補完 |

このフォルダでは **Spearmanを単調関係の主指標** とし、Pearsonとの差を使って「線形っぽい / 曲がっていそう」を候補分類します。

> 注意: `|Spearman| - |Pearson|` だけで数学的に線形・非線形を確定することはできません。ここでは大量変数を調べるためのスクリーニング用ヒューリスティックです。候補は散布図、GAM、LOESS、LightGBM/SHAPなどで確認します。

## 基本フロー

```text
全数値変数
   ↓
Pearson / Spearman / MI を一括計算
   ↓
Spearman > 閾値
   ↓
Yに対する単調増加候補
   ├─ Pearsonも高くSpearmanとの差が小さい → 線形候補
   └─ Spearmanが高いがPearsonとの差が大きい → 非線形候補

Spearmanが弱い + MIが上位
   → U字・閾値・その他の非単調依存候補
```

## 実行例

```bash
python eda_monotonic_y/analyze_monotonic.py \
  --input data/sample.csv \
  --y yield \
  --output eda_monotonic_y/result.csv
```

主な引数:

```text
--spearman-threshold 0.30   単調関係候補とするSpearmanの閾値
--nonlinear-gap 0.15       |Spearman|-|Pearson| の差で曲がり候補を分ける目安
--mi-top-quantile 0.90     MI上位何%を強い依存候補とみなすか
--min-n 30                 ペアごとの最低有効サンプル数
```

## 出力カラム

- `feature`: 説明変数名
- `n`: X,Yの両方が欠損していないサンプル数
- `pearson_r`: Pearson相関
- `pearson_p`: Pearson相関のp値
- `spearman_rho`: Spearman順位相関
- `spearman_p`: Spearman相関のp値
- `linear_r2`: 単回帰（切片あり）なら `Pearson^2` と一致するR²
- `mi`: Mutual Information推定値
- `monotonic_direction`: increasing / decreasing / weak
- `shape_candidate`: linear_monotonic / nonlinear_monotonic / weak_monotonic
- `mi_flag`: MI上位候補か
- `screening_label`: 最終的なスクリーニング用ラベル

## 解釈例

### 1. Pearson = 0.82, Spearman = 0.85

直線的かつ単調増加の可能性が高い候補です。

### 2. Pearson = 0.35, Spearman = 0.82

順位はかなり揃っているのに一次直線としては弱いので、`log(x)` や飽和型など **単調非線形候補** と考えます。

### 3. Pearson ≈ 0, Spearman ≈ 0, MIが高い

U字型、逆U字型、閾値型など **非単調な依存関係** の候補です。

## 次の段階

このスクリーニングの後は、目的に応じて次へ進みます。

1. Elastic Net: 他の変数を同時に考慮した主効果・冗長変数整理
2. LightGBM: 閾値、非線形、交互作用の探索
3. SHAP / ALE: どの値域でYに効くかを可視化
4. Tool / Product / Chamberなどで層別・階層モデル化し、交絡を確認
