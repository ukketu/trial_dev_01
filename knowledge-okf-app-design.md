# ナレッジ抽出・精査・OKF化アプリ 設計書(実装AI向けワンファイル仕様)

- 版: v1.1 / 2026-07-18(v1.0→v1.1: ①活用デモモード §10.9/§11 ②大分類/小分類の階層カテゴリと相対パス管理 §10.8 を追加)
- 想定読者: 本アプリを実装するAIコーディングエージェント(ZOOCODE)
- 前提: 実装AIは **Web検索・MCP・外部スキル一切不可**。本書のみを正とし、本書に無い外部仕様を推測で参照しないこと。不明点は §17 の手順で処理する。

---

## 0. 実装AIへの指示(最初に読むこと)

1. 本書を通読し、§15 のマイルストーン順に実装する。マイルストーンを飛ばさない。各マイルストーン完了時点で `start.bat` から起動してデモ可能な状態を保つこと。
2. 作業開始時にリポジトリ直下へ `PROGRESS.md` と `QUESTIONS.md` を作成し、以後維持する。
   - `PROGRESS.md`: マイルストーンごとの要件チェックリスト(本書から転記)、完了状況、自己レビュー結果。
   - `QUESTIONS.md`: 人間に確認したい事項。**回答を待たずに** §18 のデフォルト値で実装を続行し、該当箇所のコードコメントとPROGRESS.mdに `[ASSUME]` と明記する。
3. テストは LLM モックモード(§9.6)で完結させる。実APIキーが無くても `uv run pytest -q` が全て緑になること。
4. 禁止事項:
   - Web検索、MCP、外部CDN参照(JS/CSS/フォント含む。全アセットはリポジトリ内に同梱)
   - Docker、外部DBサーバ、Node.js/npm、常駐サービスの追加
   - 本書に列挙されていない依存パッケージの追加(必要なら QUESTIONS.md に理由を書き、代替手段が無い場合のみ追加し `[ASSUME]` を付す)
   - LLM API 以外への外部ネットワーク通信をランタイムに行うコード
5. 各マイルストーン完了時の自己レビュー観点: §16.2 のチェックリストを PROGRESS.md 上で消し込むこと。

---

## 1. 背景と目的

社内のベテランエンジニアが持つ暗黙知が、過去のPowerPoint資料・Outlookメール・Excel・Word/PDF文書に分散している。これらには誤りや古い情報も混在する。本アプリは:

1. 大量の社内文書からナレッジ(原子的な知識クレーム)を出典付きで抽出し、
2. 横断的に統合・矛盾検出して**精査**し、
3. 資料に書かれていない判断根拠(暗黙知)を**質問としてベテランに提示**し、
4. 回答を反映した検証済みナレッジを **OKF(Open Knowledge Format)準拠の Markdown バンドル**として出力する。

利用者は2種類:
- **管理者**(技術者): 初期セットアップ、ファイル投入、取り込み実行。
- **ベテラン**(非技術者): `start.bat` をダブルクリックしてブラウザで質問に答えるだけ。Python や bat の中身は理解しない前提。

## 2. スコープ / 非スコープ

**スコープ**
- ローカル単一マシン(Windows)で動作する uv 管理の Python アプリ
- 入力: .pptx / .ppt(COM経由) / .msg / .eml / .xlsx / .xlsm / .docx / .pdf / .txt / .md
- GPT系 API(社内承認済み、OpenAI互換エンドポイント)による抽出・統合・質問生成
- ローカルWebUI(取り込み・進捗・質問回答・ナレッジ閲覧・OKF出力)
- OKFバンドル出力(zip ダウンロード含む。大分類/小分類の2階層+相対パス管理 §10.8)
- **活用デモモード**: 出力済みOKFバンドルを索引から必要な分だけ読み取り、質問に回答するチャットUI(§10.9, §11)

**非スコープ(v1では実装しない)**
- Outlook サーバ/Exchange への直接接続(メールは .msg/.eml ファイルとして投入)
- マルチユーザー同時編集、認証、ネットワーク公開(バインドは 127.0.0.1 固定)
- 画像内の図面の自動ベクトル化、音声文字起こし
- ナレッジグラフ可視化

## 3. 用語

| 用語 | 定義 |
|---|---|
| Claim | 出典付きの原子的な知識1件(1〜3文)。抽出の最小単位 |
| Concept | 同一トピックの Claim 群を統合した知識単位。OKF の1ファイルに対応 |
| Bundle | Concept 群をディレクトリにまとめた OKF 出力一式 |
| Gap質問 | 資料に書かれていない判断根拠・閾値理由・例外条件を問う質問 |
| Conflict質問 | 資料間で矛盾する記述のどちらが正しいかを問う質問 |
| 精査 | 出典追跡+信頼度重み付け+矛盾検出+人間裁定による誤り訂正プロセス(§10.7) |

## 4. 全体アーキテクチャ

```
input/ (管理者がファイルを置く)
   │
   ▼
[S1 取り込み]──── COM(PowerPoint) / extract-msg / openpyxl / python-docx / PyMuPDF
   │  documents, chunks (SQLite + JSONL)
   ▼
[S2 クレーム抽出]── LLM (テキスト+スライド画像, structured output)
   │  claims
   ▼
[S3 統合・矛盾検出]── rapidfuzz + LLM
   │  concepts(draft), conflicts
   ▼
[S4 質問生成]── LLM (Gap / Conflict)
   │  questions(open)
   ▼
[S5 人間レビュー]── WebUI: ベテランが回答 → 回答は最上位信頼度の Claim として再統合
   │  concepts(verified/disputed)
   ▼
[S6 OKF出力]── output/okf_bundle/ (+zip、大分類/小分類 階層)
   │
   ▼
[活用デモモード]── WebUI チャット: 索引読解 → 必要ファイル選択 → 回答生成(§10.9)
```

- S1〜S4 は WebUI の「取り込み・分析を実行」ボタンで一括実行(バックグラウンドジョブ、進捗ポーリング)。
- S5 はベテランのペースで随時。回答が入るたび、影響 Concept のみ再統合(S3')。
- S6 は「OKF出力」ボタンで実行。何度でも再出力可(冪等)。
- 増分処理: ファイルは SHA-256 で管理し、既処理ファイルはスキップ(§10.1)。

## 5. 動作環境・制約

| 項目 | 内容 |
|---|---|
| OS | Windows 10/11(日本語環境。パスに日本語・空白を含み得る) |
| Office | Microsoft Office インストール済み(PowerPoint COM を利用。無い場合はテキストのみのフォールバック §7.1) |
| Python | 3.12(uv 管理。`requires-python = ">=3.12"`) |
| パッケージ取得 | 社内 PyPI ミラー経由で `uv sync` が可能な前提 |
| ネットワーク | ランタイムの外部通信は LLM API エンドポイントのみ |
| LLM API | OpenAI 互換 `/v1/chat/completions`。モデル名・base_url・APIキーは `config.toml` で設定(§9.1) |
| 起動 | `start.bat` ダブルクリック → ブラウザ自動起動(§12) |
| バインド | `127.0.0.1:8765` 固定(§18 で変更可) |

## 6. ディレクトリ構成

```
repo/
├── start.bat                # ベテランが唯一触るファイル
├── pyproject.toml
├── uv.lock
├── config.toml.example      # 初回に config.toml へコピーして管理者が編集
├── app/
│   ├── __init__.py
│   ├── server.py            # FastAPI 起動エントリ (python -m app.server)
│   ├── config.py            # config.toml 読み込み (pydantic)
│   ├── db.py                # SQLite 接続・スキーマ作成
│   ├── models.py            # pydantic モデル(§8)
│   ├── llm.py               # LLMクライアント(実物/モック切替 §9)
│   ├── jobs.py              # バックグラウンドジョブ管理(threading)
│   ├── demo_qa.py           # 活用デモモード Q&Aエンジン(§10.9)
│   ├── pipeline/
│   │   ├── s1_ingest.py
│   │   ├── extractors/      # pptx.py, msg.py, eml.py, xlsx.py, docx.py, pdf.py, text.py
│   │   ├── s2_claims.py
│   │   ├── s3_consolidate.py
│   │   ├── s4_questions.py
│   │   ├── s5_answers.py    # 回答反映・再統合
│   │   └── s6_publish.py    # OKF出力 + validator
│   ├── prompts/             # プロンプト本文(.txt, §10 に全文掲載)
│   ├── web/
│   │   ├── templates/       # Jinja2 (base.html, dashboard.html, ingest.html,
│   │   │                    #  questions.html, concepts.html, publish.html, chat.html)
│   │   └── static/          # app.css, app.js (CDN禁止・同梱)
│   └── util/                # hashing, chunking, textnorm, winpath
├── tests/
│   ├── fixtures/
│   │   ├── llm/             # モック応答 JSON(§9.6)
│   │   └── docs/            # ダミー入力(生成スクリプト含む §14.2)
│   └── test_*.py
├── samples/                 # 受け入れデモ用ダミー文書一式(§16.1)
└── (実行時生成 / .gitignore)
    workspace/
    ├── db.sqlite3
    ├── documents/<doc_id>/  # 抽出テキスト, スライドPNG, 添付
    ├── artifacts/           # ステージ別JSONLダンプ(デバッグ用)
    ├── logs/app.log         # RotatingFileHandler
    └── output/okf_bundle/   # S6 出力(+ okf_bundle.zip)。§10.8 の階層構造
    input/                   # 管理者がファイルを置く(サブフォルダ可・再帰走査)
```

## 7. 入力仕様

共通: 走査対象は `input/` 以下再帰。1ファイル上限 200MB(超過はスキップし警告ログ+UI表示)。ファイル名・パスは日本語対応(常に `pathlib.Path`、内部文字列は UTF-8)。Zip等アーカイブは非対応(スキップ+警告)。

### 7.1 PowerPoint (.pptx / .ppt)

2系統を併用する:

**(a) テキスト系(必須)** — `python-pptx`(.pptx のみ)
- 各スライドの図形テキスト、表、**スピーカーノート**を抽出。ノートは `notes` として本文と区別して保持(暗黙知密度が高いため S2 で明示的に扱う)。
- グループ図形は再帰展開。SmartArt はテキスト取得できない場合があるため、取得不能でもエラーにしない。

```python
from pptx import Presentation
prs = Presentation(path)
for i, slide in enumerate(prs.slides, 1):
    texts = []
    def walk(shapes):
        for sh in shapes:
            if sh.shape_type == 6:  # GROUP
                walk(sh.shapes)
            elif sh.has_text_frame:
                texts.append(sh.text_frame.text)
            elif getattr(sh, "has_table", False) and sh.has_table:
                for row in sh.table.rows:
                    texts.append(" | ".join(c.text for c in row.cells))
    walk(slide.shapes)
    notes = ""
    if slide.has_notes_slide and slide.notes_slide.notes_text_frame:
        notes = slide.notes_slide.notes_text_frame.text
```

**(b) 画像系(Office がある場合)** — PowerPoint COM でスライドPNG書き出し。図解・矢印・配置に乗った情報を Vision で読むために使う。

```python
import pythoncom, win32com.client
def export_slides_png(pptx_path, out_dir):
    pythoncom.CoInitialize()
    try:
        app = win32com.client.Dispatch("PowerPoint.Application")
        pres = app.Presentations.Open(str(pptx_path), ReadOnly=True,
                                      Untitled=False, WithWindow=False)
        pres.Export(str(out_dir), "PNG", 1280, 720)  # スライド1.PNG.. または Slide1.PNG.. が生成される
        pres.Close()
        app.Quit()
    finally:
        pythoncom.CoUninitialize()
```

- COM 呼び出しはジョブスレッド内で直列実行(同時1件)。失敗時(Office無し/破損ファイル)はログに残しテキスト系のみで続行(document に `images_available: false` を記録)。
- 出力ファイル名は環境言語で変わる(日本語Officeでは `スライド1.PNG`)。**ディレクトリ内の PNG を数値抽出ソートで列挙**して割り当てること(名前を決め打ちしない)。
- .ppt(旧形式)は COM で開けるが python-pptx 不可 → COM 経由で一時 .pptx に `SaveAs` してから (a) を適用。SaveAs の FileFormat は 24 (ppSaveAsOpenXMLPresentation)。COM 不可環境の .ppt はスキップ+警告。

### 7.2 Outlook メール (.msg / .eml)

- 前提運用: 管理者が Outlook から対象メールをフォルダへ**ドラッグ&ドロップ**すると .msg が生成される。それを `input/` に置く。Exchange 直接接続は行わない。
- .msg: `extract-msg` を使用。

```python
import extract_msg
m = extract_msg.Message(str(path))
subject, sender, to, date, body = m.subject, m.sender, m.to, m.date, m.body
for att in m.attachments:
    # att.longFilename / att.data。添付が .msg の場合は再帰処理(深さ最大3)
    ...
m.close()
```

- .eml: 標準ライブラリ `email` + `email.policy.default` でパース。text/plain 優先、無ければ text/html を `html.parser` ベースの簡易タグ除去でテキスト化。
- 添付のうち対応形式(§7の一覧)は子 document として取り込み、`parent_doc_id` で親メールに紐付ける。
- 引用返信の連鎖(`>` 行、`-----Original Message-----` 以降)は残すが、S2 プロンプト側で「引用部の重複抽出をしない」よう指示(§10.2)。
- 送信日時・差出人は provenance と信頼度(§10.7)に使うため必ず保持。

### 7.3 Excel (.xlsx / .xlsm)

- `openpyxl`(`read_only=True, data_only=True`)。data_only は保存時キャッシュ値を返すため、一度も再計算保存されていないファイルでは None になり得る。その場合は数式文字列を代替表示(`load_workbook(..., data_only=False)` を該当シートのみ再読込)。
- シートごとに使用範囲を Markdown 表へ変換。上限: 200行 × 30列 / シート。超過時は先頭50行+末尾10行のサンプル+「n行×m列、省略」注記。
- セルコメント(`cell.comment`)は `[コメント B4: ...]` として表に併記(暗黙知が入りやすい)。
- 結合セルは左上値を採用、他は空欄。マクロ(.xlsm の VBA)は読まない。
- シート名を locator に使う: `sheet:シート名!A1:D50`。

### 7.4 Word (.docx) / PDF / テキスト

- .docx: `python-docx`。段落+表を順に連結。見出しスタイル(`paragraph.style.name` が `Heading` で始まる)は `## ` 付与で構造を残す。.doc(旧形式)は COM があれば SaveAs(FileFormat=16: wdFormatXMLDocument) 経由、無ければスキップ+警告。
- PDF: `PyMuPDF`(import 名 `fitz`)。`page.get_text("text")` をページ単位で。テキストが取れない画像PDFはページを `page.get_pixmap(dpi=150)` でPNG化し Vision に回す(document に `images_available: true`)。
- .txt/.md: エンコーディング判定は UTF-8 → CP932 の順に try。両方失敗なら `errors="replace"` で UTF-8。

## 8. データモデル

保存先: SQLite(`workspace/db.sqlite3`、WALモード)。加えて各ステージ完了時に `workspace/artifacts/` へ JSONL をダンプ(デバッグ・再実行用。正はSQLite)。以下は pydantic モデル定義(app/models.py)。DBカラムは同名。

```python
class Provenance(BaseModel):
    doc_id: str
    locator: str        # 例 "slide:12" "sheet:工程表!A1:D50" "page:3" "mail_body" "para:45"
    quote: str          # 根拠となる原文抜粋(最大200字)

class Document(BaseModel):
    doc_id: str         # "doc_" + sha256先頭12桁
    path: str
    kind: str           # pptx|ppt|msg|eml|xlsx|docx|pdf|txt|md
    title: str
    created_at: str | None   # ファイル更新日時 or メール送信日時 (ISO8601)
    sender: str | None
    parent_doc_id: str | None
    images_available: bool
    status: str         # ingested|extracted|error
    error: str | None

class Chunk(BaseModel):
    chunk_id: str
    doc_id: str
    locator: str
    text: str           # 目安 1500〜3000字。スライドは1枚=1chunk(notes含む)、メールは1通=1chunk(長文は分割)
    image_path: str | None   # スライド/ページPNG

class Claim(BaseModel):
    claim_id: str       # "clm_" + uuid4先頭12桁
    text: str           # 1〜3文の日本語
    kind: str           # fact|procedure|criterion|cause_effect|tip
    topic_tags: list[str]    # 3〜6個、日本語名詞句
    entities: list[str]      # 装置名・工程名・材料名など
    provenance: list[Provenance]
    trust: float        # §10.7 の初期重み
    status: str         # extracted|merged|disputed|verified|rejected
    origin: str         # source|answer   (answer=ベテラン回答由来)

class Concept(BaseModel):
    concept_id: str     # "cpt_" + uuid4先頭12桁
    slug: str           # OKFパス用 ascii スラッグ(§10.8)
    title: str
    summary: str
    claim_ids: list[str]
    status: str         # draft|disputed|verified
    confidence: float
    tags: list[str]
    category_major_slug: str   # ascii ケバブ(例 "press-process")。未分類は "misc"
    category_major_title: str  # 日本語表示名(例 "プレス工程")。未分類は "その他"
    category_minor_slug: str   # 例 "temp-control"。未分類は "general"
    category_minor_title: str  # 例 "温度管理"。未分類は "一般"

class Question(BaseModel):
    question_id: str
    qtype: str          # gap|conflict
    concept_id: str
    text: str           # ベテランに見せる質問文
    options: list[str]  # conflict は必ず ["Aが正しい","Bが正しい","状況による(補足に記入)"]
                        # gap は選択肢化できる場合のみ、できなければ []
    context: str        # 出典抜粋など判断材料(UI表示用)
    claim_ids: list[str]
    priority: int       # 1(高)〜3
    status: str         # open|answered|skipped
    answer_choice: str | None
    answer_text: str | None
    answered_at: str | None

class Job(BaseModel):
    job_id: str
    kind: str           # ingest_analyze|publish|reconsolidate
    status: str         # running|done|error
    progress: int       # 0-100
    message: str        # 現在処理中の内容(UI表示)
    started_at: str
    finished_at: str | None
```

DBには他に `settings(key,value)` テーブル(最終実行日時など)。トークン使用量ログは `llm_calls(ts, stage, model, prompt_tokens, completion_tokens)` に記録。活用デモの「ナレッジ化候補」は `demo_feedback(ts, question, note)` に記録。確定したカテゴリ体系は settings キー `taxonomy_json` に保存(§10.8.1)。

## 9. LLM 連携

### 9.1 設定 (config.toml)

```toml
[llm]
base_url = "https://api.example.co.jp/v1"   # 社内ゲートウェイ
api_key_env = "KNOWLEDGE_APP_API_KEY"        # 環境変数名。直接キーを書く場合は api_key を使用
# api_key = "sk-..."
model = "gpt-5.6"
vision = true                # 画像入力を使うか
structured_output = "auto"   # auto|on|off  (§9.4)
max_concurrency = 2          # 並列リクエスト数
timeout_s = 120

[app]
port = 8765
input_dir = "input"
workspace_dir = "workspace"
old_doc_years = 5            # これより古い資料は信頼度を減衰(§10.7)
demo_max_files = 8           # 活用デモ: 1質問あたり読み込む最大ファイル数
demo_max_rounds = 2          # 活用デモ: 選択→回答 の最大周回数(§10.9)
```

`config.toml` が無い場合、起動時に `config.toml.example` からコピー生成し、UI ダッシュボードに「APIキー未設定(モックモードで動作中)」と表示する。

### 9.2 クライアント

`openai` SDK を使用。`app/llm.py` に薄いラッパ `LLMClient` を実装し、全ステージはこれ経由でのみ呼ぶ。

```python
from openai import OpenAI
client = OpenAI(base_url=cfg.base_url, api_key=key, timeout=cfg.timeout_s)
resp = client.chat.completions.create(
    model=cfg.model,
    messages=messages,
    response_format=schema_or_none,   # §9.4
    temperature=0.2,
)
```

- リトライ: 429/5xx/timeout に対し指数バックオフ(2,4,8,16秒、最大4回)。それでも失敗したチャンクは `status=error` で記録し、ジョブは続行(全滅させない)。
- 並列: `ThreadPoolExecutor(max_workers=cfg.max_concurrency)`。

### 9.3 画像入力(Vision)

```python
import base64
def image_part(png_path):
    b64 = base64.b64encode(Path(png_path).read_bytes()).decode()
    return {"type": "image_url",
            "image_url": {"url": f"data:image/png;base64,{b64}"}}
messages = [{"role": "user", "content": [
    {"type": "text", "text": prompt_text},
    image_part(chunk.image_path),
]}]
```

`vision=false` の場合、または画像が無いチャンクはテキストのみ。1リクエスト1画像まで(スライド単位なので十分)。

### 9.4 構造化出力

- `structured_output="on"`: `response_format={"type":"json_schema","json_schema":{"name":..., "schema":..., "strict":True}}` を付与。
- `"off"`: response_format を付けず、プロンプト末尾で「JSONのみを出力。コードフェンス禁止」と指示。
- `"auto"`(既定): まず on で試行し、API がエラー(400等)を返したら以後そのプロセス内は off に自動フォールバック(結果を settings に記録)。
- 受信側は常に防御的にパース: 先頭末尾の ```json フェンス除去 → `json.loads` → 失敗時は最初の `{` から最後の `}` を切り出して再試行 → それでも失敗なら1回だけ「有効なJSONのみで再出力」と自動再依頼 → 失敗はチャンク単位で error 記録。

### 9.5 コンテキスト予算

- 1リクエストの入力テキストは最大 12,000 字を目安にチャンク側で保証(§8 Chunk)。
- S3 の統合は Claim 群をトピックごとに束ね、1回の入力 Claim は最大 40 件。超える場合は分割統合→再統合の2段。

### 9.6 モックモード(テストの要)

- 環境変数 `LLM_MOCK=1`、または APIキー未設定時に自動で有効。
- `MockLLMClient` は「ステージ名 + 入力の SHA-256 先頭8桁」でキーを作り、`tests/fixtures/llm/<stage>/<key>.json` があればそれを返す。無ければ**ステージごとの決定的な合成応答**を生成する(乱数不使用):
  - s2: 入力チャンクの各文から先頭2文を claim 化(kind=fact, tags=["モック"])。ただし入力に `【モック指示:...】` という埋め込みがあればその指示どおりの claim を返す(fixture文書側で矛盾ペア等を意図的に作るための仕掛け。§14.2)。
  - s3: 同一 topic_tags の claim を1 concept に束ね、`【モック指示:conflict】` 由来の claim ペアを conflicts として返す。
  - s4: concept ごとに gap 質問1件、conflicts から conflict 質問を生成。
  - s6本文生成: claims を箇条書き整形したテンプレ本文。
  - demo(選択/回答): §10.9 のとおり(rapidfuzz による決定的選択+summary引用のテンプレ回答)。
- これにより E2E 受け入れシナリオ(§16.1)が完全オフライン・決定的に再現できる。

## 10. パイプライン詳細

### 10.1 S1 取り込み

1. `input/` を再帰走査、対応拡張子を列挙。SHA-256 を計算し、既存 doc_id と一致すればスキップ(増分)。
2. 形式別 extractor でテキスト/画像抽出 → `workspace/documents/<doc_id>/` に保存(`text.json`: chunk配列、`slide_001.png` 等)。
3. Document / Chunk を DB 登録。失敗ファイルは `status=error` と理由を記録し続行。
4. ジョブ進捗はファイル数ベースで更新。

### 10.2 S2 クレーム抽出

チャンクごとに LLM 呼び出し。**プロンプト全文**(`app/prompts/s2_claims.txt`。`{...}` は Python format で埋める):

```
あなたは製造・エンジニアリング分野のナレッジ抽出の専門家です。
以下の社内文書の断片から、再利用価値のある知識を「クレーム」として抽出してください。

# 文書情報
種別: {kind} / タイトル: {title} / 作成日: {created_at} / 位置: {locator}
{sender_line}

# ルール
- 1クレーム = 1つの独立した知識。1〜3文の日本語。文書を読んでいない人にも通じる自己完結の文にする(「これ」「上記」等の指示語禁止)。
- 書かれていないことを推測で補わない。数値・条件・固有名詞は原文どおり。
- kind の分類: fact(事実・仕様) / procedure(手順) / criterion(判断基準・閾値) / cause_effect(原因と結果・トラブル事例) / tip(コツ・注意点)。
- スピーカーノート由来の内容は特に重視して抽出する。
- メールの場合、引用部(>で始まる行や Original Message 以降)から同じ内容を重複抽出しない。
- 単なる挨拶、日程調整、目次、ページ番号などナレッジでないものは抽出しない。該当なしなら空配列。
- 各クレームに quote として根拠原文(最大200字)を付ける。
- 添付画像がある場合、図中の矢印・配置・強調が示す関係性(順序、対比、因果)も読み取って抽出する。

# 出力(JSONのみ)
{{"claims": [{{"text": "...", "kind": "fact", "topic_tags": ["...","..."],
  "entities": ["..."], "quote": "..."}}]}}

# 文書断片
{chunk_text}
```

JSONスキーマ(structured_output 用)は上記出力形に対応する strict スキーマを `app/llm.py` に定数定義。claim には trust 初期値(§10.7)と provenance(doc_id, locator, quote)を付与して保存。

### 10.3 S3 統合・矛盾検出

1. **候補ペアリング(LLM不使用)**: 全 claim を topic_tags の正規化(全半角統一・小文字化)でグルーピング。タグ一致が無い claim 同士でも `rapidfuzz.fuzz.token_set_ratio(text) >= 70` ならブリッジ結合。連結成分をトピック群とする。1群40件超は作成日順に分割。
2. **LLM 統合**(`app/prompts/s3_consolidate.txt`):

```
以下は社内文書から抽出した知識クレームの一覧です(同じ話題の可能性が高いもの)。
これらを整理してください。

# タスク
1. 実質的に同じ内容のクレームをまとめ、1つ以上の「コンセプト」を作る。
   コンセプトには title(20字以内)、summary(3文以内)、含まれる claim_id を付ける。
2. 内容が「矛盾」しているペアを挙げる。矛盾とは、同じ対象について両立しない
   数値・手順・判断を述べている場合。単なる詳細度の違いや補完関係は矛盾ではない。
3. 矛盾には reason(何がどう食い違うか、50字以内)を付ける。

# 出力(JSONのみ)
{{"concepts": [{{"title":"...","summary":"...","claim_ids":["clm_..."],
   "tags":["..."]}}],
  "conflicts": [{{"claim_id_a":"clm_...","claim_id_b":"clm_...","reason":"..."}}]}}

# クレーム一覧
{claims_block}    ← 各行: [clm_xxx] (kind/作成日/出典種別) text
```

3. 矛盾ペアの裁定(§10.7): trust 差が 0.25 以上なら高い方を採用し、低い方を `status=rejected`(ただし Concept 本文の「過去の記述との差異」節に残す)。差が 0.25 未満なら両方 `disputed` とし S4 で Conflict 質問化。
4. Concept を保存(status=draft、disputed claim を含むものは status=disputed)。confidence は所属 claim の trust 加重平均。

### 10.4 S4 質問生成

Concept ごとに LLM 呼び出し(`app/prompts/s4_questions.txt`):

```
あなたは熟練エンジニアへのインタビュアーです。以下のコンセプト(整理済みナレッジ)を読み、
資料に書かれていない暗黙知を引き出す質問を作ってください。

# 質問の観点(この観点に該当するものだけ。無理に作らない)
- なぜその閾値・条件なのか(根拠)
- 手順を省略・変更するとどうなるか(失敗モード)
- 例外条件・適用できないケース
- 前提となる環境・機材・スキル
- 現在も有効か、古くなっていないか

# ルール
- 最大3問。ベテランが1問5分以内で答えられる具体的な質問にする。
- 選択肢で答えられる質問は options を付ける(2〜4択+「その他(補足に記入)」)。
  自由記述が適切なら options は空配列。
- priority: 1=このコンセプトの信頼性を左右する / 2=有用 / 3=あれば良い

# 出力(JSONのみ)
{{"questions":[{{"text":"...","options":["..."],"priority":1}}]}}

# コンセプト
タイトル: {title}
要約: {summary}
クレーム:
{claims_block}
```

Conflict 質問は LLM を使わずテンプレ生成:

```
text  = f"「{title}」について、資料間で記述が食い違っています。どちらが正しいですか?"
context = f"A: {claim_a.text}\n  (出典: {a出典} {a.locator}, {a作成日})\n" \
          f"B: {claim_b.text}\n  (出典: {b出典} {b.locator}, {b作成日})\n" \
          f"食い違い: {reason}"
options = ["Aが正しい", "Bが正しい", "状況による(補足に記入)"]
priority = 1
```

### 10.5 S5 回答反映

- 回答受信時: `answer_text`(補足)+選択結果を1つの Claim に変換(`origin=answer, trust=1.0, provenance=[{doc_id:"answer:"+question_id, locator:"webui", quote:answer全文}]`)。
- Conflict 回答: 「Aが正しい」→ B claim を rejected、A を verified。「状況による」→ 両 claim を保持し、回答 claim(条件の説明)を追加、Concept に「条件分岐」として記載。
- 影響 Concept のみ S3 の LLM 統合を再実行(reconsolidate ジョブ)。open な conflict が無くなり、priority=1 の gap 質問が answered/skipped になった Concept は `status=verified`。
- スキップは status=skipped(いつでも再オープン可)。

### 10.6 S6 OKF 出力

手順: (0) カテゴリ付与(§10.8.1) → (1) §10.8 のプロファイルに従い `workspace/output/okf_bundle/` に生成 → (2) zip 化。生成後にバリデータを必ず実行:
- 全 .md の frontmatter が必須キーを持つ / YAML としてパース可能
- ルート index.md → 大分類 index.md → 小分類 index.md → concept の相対リンクが全て実在し、逆に全 concept がこの経路で到達可能
- バンドル内のリンク・frontmatter・本文に絶対パス(ドライブレター等)やバックスラッシュ区切りが無い(区切りは `/` のみ)
- slug 重複なし(concept・カテゴリとも)
バリデータ失敗は publish ジョブを error にし、UI に理由表示。

Concept 本文の整形は LLM に依頼(`s6_body.txt`): 「以下の verified/merged claims と回答を、指定の節構成で日本語Markdown本文にせよ。**新しい事実を追加しない**。各記述の末尾に出典番号 [1] を付けよ」。出典番号は本文下部の「根拠と出典」節と対応。

### 10.7 精査(信頼度)モデル

Claim の初期 trust:

| 出典 | trust |
|---|---|
| ベテラン回答(origin=answer) | 1.00 |
| 文書(pptx/docx/pdf/xlsx) | 0.60 |
| メール本文 | 0.50 |
| 補正: 作成日が `old_doc_years` より古い | ×0.7 |
| 補正: 同内容の claim が別文書にも存在(統合時) | +0.1(上限0.9、answer除く) |

- 矛盾裁定は §10.3-3。trust と status のこの仕組み+人間裁定が本アプリの「精査」の実体であり、**誤り資料は rejected として痕跡を残したまま最終ナレッジから除外**される。
- rejected claim は OKF 本文の「過去の記述との差異(注意)」節に「旧資料では X とされていたが、確認の結果 Y が正」と明記する(同じ誤りの再流通を防ぐため)。

### 10.8 OKF 出力プロファイル(本プロジェクトの確定仕様)

OKF(Open Knowledge Format, Google提唱 v0.1)の基本原則—「YAML frontmatter 付き plain Markdown」「1概念=1ファイル」「ファイルパス=概念ID」「ディレクトリ=Bundle、index.md で束ね、通常のMarkdownリンクで相互参照」—に準拠する。**実装AIは外部仕様を参照できないため、以下を本プロジェクトにおける完全な確定仕様として扱うこと。**

```
okf_bundle/
├── index.md                       # Bundle ルート: 大分類一覧+_meta へのリンク
├── <大分類slug>/                   # 例 press-process/
│   ├── index.md                   # 大分類の説明+小分類一覧
│   └── <小分類slug>/               # 例 temp-control/
│       ├── index.md               # 小分類の説明+concept 一覧(タイトル+1行説明+status)
│       └── <concept-slug>.md      # Concept 本体
└── _meta/
    ├── provenance.md              # doc_id → 元ファイル相対パス(input/ 起点)の対応表
    └── open-questions.md          # 未回答質問一覧(status=open/skipped)
```

**相対パス管理(共有可搬性の必須要件)**
- concept の ID はバンドルルートからの相対パス(拡張子なし)。例 `press-process/temp-control/press-temp-control`。
- バンドル内の全リンク・全パス表記はバンドルルート基準の相対パスとし、区切りは `/` 固定。絶対パス・ドライブレター・バックスラッシュは禁止(バリデータで検査)。フォルダごとコピー/zip/Git 共有してもリンクが壊れないことを保証する。
- ディレクトリ名(カテゴリslug)は **ascii ケバブケース**とする。日本語フォルダ名は Windows ローカルでは動作するが、zip 共有時の文字コード差(CP932/UTF-8)により他環境で文字化けする事故が定番のため採用しない。日本語の分類名は各 index.md の見出しと concept frontmatter の `category` で表示する(人間は index.md 経由で日本語名のまま辿れる)。

- slug: タイトルを LLM 生成時に ascii ケバブケース(例 `press-temp-control`)で併せて出力させる。重複時は `-2` 付与。パスが概念IDとなる(例 `press-process/temp-control/press-temp-control`)。
- Concept ファイル雛形:

```markdown
---
type: concept            # concept|procedure|criterion|faq のいずれか(主要claimのkindから決定)
id: press-process/temp-control/press-temp-control
title: プレス温度管理の基準
summary: プレス加工時の金型温度は120度を基準に管理する。   # 1行要約。§10.9 の索引で使用
category: [プレス工程, 温度管理]      # [大分類, 小分類] の日本語表示名
status: verified          # verified|draft|disputed
confidence: 0.85
tags: [プレス, 温度管理]
sources:
  - file: 資料/2019_プレス工程改善.pptx   # input/ 起点の相対パス
    locator: slide:12
  - file: RE_温度条件の件.msg
    locator: mail_body
verified_by: WebUI回答 (2026-07-20)   # 回答が無い場合は省略
updated: 2026-07-20
---

# プレス温度管理の基準

## 概要
(summary)

## 詳細
(本文。各記述末尾に [1] 形式の出典番号)

## 判断基準・例外
(criterion / 回答由来の条件分岐)

## 過去の記述との差異(注意)
(rejected claim がある場合のみ)

## 根拠と出典
1. 資料/2019_プレス工程改善.pptx slide:12 「...quote...」
2. ...

## 未解決の論点
(open/skipped 質問がある場合のみ、質問文を列挙)
```

- 各階層の index.md は手書き風のシンプルな一覧とし、**同階層/直下への相対リンク**のみで書く:
  - ルート index: `- [プレス工程](press-process/index.md) — 説明1行`
  - 大分類 index: `- [温度管理](temp-control/index.md) — 説明1行`
  - 小分類 index: `- [プレス温度管理の基準](press-temp-control.md) — summary (verified)`

### 10.8.1 カテゴリ付与(S6 ステップ0)

- 初回 publish 時: 全 concept の title/tags/summary を1回の LLM 呼び出しに渡し、2階層の分類体系(大分類 最大7 × 各小分類 最大7)と全 concept の割当を同時に決めさせる。concept が 80 件を超える場合は、まず体系のみ決定 → 割当をバッチ分割。
- 決定した体系は settings `taxonomy_json` に保存し、concept レコードに category_* を書き込む。
- 2回目以降の publish: 既存体系を維持し、新規/変更 concept のみ既存体系へ割当(収まらない場合のみ小分類の追加を許可)。**再出力のたびにカテゴリが揺れないこと(冪等性)。**
- 割当不能・LLM失敗時のフォールバック: 大分類 misc(その他)/ 小分類 general(一般)。

`app/prompts/s6_categorize.txt`(全文):

```
以下は社内ナレッジ(コンセプト)の一覧です。共有フォルダで整理するための2階層の分類体系を作り、
全コンセプトを割り当ててください。

# ルール
- 大分類は最大7個、各大分類の小分類は最大7個。実務者が探しやすい業務軸で分ける。
- 各分類に title(日本語、10字以内)と slug(ascii小文字ケバブケース)を付ける。
- 全コンセプトを必ずどこか1つの小分類に割り当てる。
{existing_taxonomy_block}   ← 既存体系がある場合「既存の分類体系を変更せず、以下に割り当てること: ...」を挿入

# 出力(JSONのみ)
{{"taxonomy": [{{"slug":"press-process","title":"プレス工程",
    "children":[{{"slug":"temp-control","title":"温度管理"}}]}}],
  "assign": [{{"concept_id":"cpt_...","major":"press-process","minor":"temp-control"}}]}}

# コンセプト一覧
{concepts_block}    ← 各行: [cpt_xxx] title / tags / summary
```

### 10.9 活用デモモード Q&A エンジン(app/demo_qa.py)

出力済み OKF バンドル(mdファイル群)**のみ**を知識源として質問に回答し、「AIが索引から必要な分だけ読んで活用する」様子を見せるエンジン。DB の concept ではなく**バンドル内の実ファイルを読む**こと(可搬な md ファイルがそのまま AI に使えると示すのがデモの主旨)。

前提: `output/okf_bundle/` が存在すること。無ければ API はその旨のエラーを返し、UI は「先に[出力]タブで OKF を出力してください」と案内。

処理フロー(1質問あたり):
1. **索引(manifest)構築**: バンドルを走査し、全 concept の frontmatter から (id, title, summary, tags, status) を取得、大分類/小分類でグループ化したテキスト索引を作る。バンドルの最終更新時刻をキーにメモリキャッシュ。manifest が 8,000 字を超える場合は2段選択(まず大分類を選ばせ、選ばれた分類の manifest のみ提示)。
2. **選択(Phase A)**: 質問+直近会話+manifest を LLM に渡し、読むべきファイルを最大 `demo_max_files` 件選ばせる。
3. **読込**: 選ばれた相対パスのファイルを読む(本文合計 60,000 字上限。超過分は frontmatter の confidence 降順で切り詰め)。**パス検証必須**: `Path.resolve()` 後の実パスがバンドルディレクトリ配下であることを `is_relative_to` で確認。範囲外・不存在パスは無視して警告ログ。
4. **回答(Phase B)**: 質問+会話+選択ファイル本文で回答生成。応答が `insufficient=true` の場合、そのヒントを添えて Phase A からもう1周(合計 `demo_max_rounds` 周まで)。
5. 応答: answer_md / 参照ファイル一覧(path, title, status)/ 選択理由 / not_found。llm_calls に stage="demo" で記録。

`app/prompts/demo_select.txt`(全文):

```
あなたは社内ナレッジベースを使って質問に答えるアシスタントです。
まず、以下の索引から「質問に答えるために読むべきファイル」を選んでください。

# ルール
- 必要最小限だけ選ぶ(最大{max_files}件)。関係ないものは選ばない。
- 索引に該当がなければ paths を空配列にする。
{hint_block}   ← 2周目のみ「前回の回答で不足した点: ...」を挿入

# 出力(JSONのみ)
{{"paths": ["press-process/temp-control/press-temp-control.md"], "reason": "選定理由を1文"}}

# 会話の文脈
{history_block}

# 質問
{question}

# ナレッジ索引
{manifest_block}
```

`app/prompts/demo_answer.txt`(全文):

```
あなたは社内ナレッジベースを使って質問に答えるアシスタントです。
以下のナレッジファイルの内容【のみ】に基づいて回答してください。

# ルール
- ナレッジに書かれていないことを推測や一般知識で補わない。
- 回答中の各記述の末尾に、根拠ファイルの id を [press-process/temp-control/press-temp-control] の形式で付ける。
- status が draft / disputed のナレッジを使う場合は「(未確定情報)」と明示する。
- ナレッジだけでは答えられない場合: insufficient を true にし、more_hint に追加で読みたい内容を書く。
  すでに{max_rounds}周目の場合は insufficient を使わず、「この件はまだナレッジ化されていません」と
  正直に答え、not_found を true にする。
- 回答は日本語 Markdown で簡潔に。

# 出力(JSONのみ)
{{"answer_md": "...", "used_ids": ["..."], "insufficient": false,
  "more_hint": "", "not_found": false}}

# 会話の文脈
{history_block}

# 質問
{question}

# ナレッジファイル
{files_block}    ← 各ファイルを「===== id =====」区切りで連結(frontmatter含む)
```

- 会話履歴: クライアントから直近6往復を受け取り、両プロンプトの {history_block} に「ユーザー: .../ AI: ...(要約)」形式で挿入。サーバは会話状態を持たない。
- モックモード: Phase A は rapidfuzz で質問と title+tags を照合し上位3件を決定的に選択。Phase B は選択ファイルの summary を [id] 付きで整形するテンプレ回答。一致0件なら not_found=true の定型応答。

## 11. WebUI 設計

構成: FastAPI + Jinja2 テンプレート + 素の JS(fetch でポーリング)。CSS/JS は `app/web/static/` に同梱、外部CDN禁止。日本語UI。対象ユーザーは非技術者のため、**専門用語(claim, concept 等)を画面に出さない**。文言は下記を使用: Claim→「抜き出した知識」、Concept→「ナレッジ」、Gap質問→「教えてほしいこと」、Conflict質問→「食い違いの確認」。

### 11.1 画面とモード切替

ヘッダ右端に**モード切替ボタン**を常設し、2つのモードを切り替える(サーバ側の状態は持たず、単なる画面遷移で実現):

- **整備モード**(既定): タブ `[ホーム] [取り込み] [質問に答える] [ナレッジを見る] [出力]`
- **活用デモモード**: タブを隠し、チャット画面(chat.html)のみを表示

ボタン表記: 整備モード時「▶ 活用デモを試す」/ デモモード時「◀ 整備モードに戻る」。

**ホーム(dashboard.html)**
- 件数カード: 取り込んだファイル / 抜き出した知識 / ナレッジ / 未回答の質問
- 実行中ジョブがあれば進捗バー+現在の処理内容(2秒ポーリング)
- APIキー未設定時は黄色の帯で「モックモードで動作中(お試し用)」

**取り込み(ingest.html)** ※管理者向け
- input フォルダのパス表示+「フォルダを開く」ボタン(`os.startfile`)
- 「取り込み・分析を実行」ボタン → ingest_analyze ジョブ開始(S1→S4)。実行中は無効化。
- 直近ジョブのログ要約(スキップ/エラーになったファイル一覧)

**質問に答える(questions.html)** ← ベテランの主画面。最重要。
- 未回答質問を priority 順に**1問ずつ**カード表示(一覧で圧迫しない)。「残り n 問」を表示。
- カード構成: 質問文(大きめ18px)、判断材料(context: 出典と抜粋を出典名付きで表示)、選択肢ボタン(縦並び・大きめ)、補足自由記述(textarea、任意)、[回答する] [あとで(スキップ)]
- 回答送信 → 次の質問へ自動遷移。全問完了時「ありがとうございました。回答はナレッジに反映されます」
- スキップ済みを再表示するリンクを下部に小さく設置

**ナレッジを見る(concepts.html)**
- ナレッジ一覧(タイトル/status バッジ/confidence)。status フィルタ。
- 詳細画面: OKF 本文プレビュー(markdown → HTML はサーバ側で最小変換: 見出し・リスト・太字のみの自前簡易変換で可。外部ライブラリ追加不要)+含まれる知識と出典の一覧+この ナレッジに紐づく質問へのリンク

**出力(publish.html)**
- 「OKFファイルを出力」ボタン → publish ジョブ → 完了後「okf_bundle.zip をダウンロード」リンク+出力先フォルダを開くボタン
- バリデータ結果表示(エラー時は赤で理由)

**活用デモ(chat.html)** ← デモモードの唯一の画面
- チャット形式: 上に会話ログ、下に入力欄+[質問する]。応答待ちはスピナー+「ナレッジを探しています…」(同期API、タイムアウトは LLM 設定準拠)。
- AI の各回答の下に「参照したナレッジ」チップを表示(タイトル+statusバッジ)。クリックで該当 md をモーダル表示(GET /api/demo/file)。回答本文中の [id] 表記はこのチップに対応。
- 選択理由(reason)を折りたたみで小さく表示 — 「AIが索引からどのファイルを選んだか」を見せるのがデモの見せ場。
- not_found の場合: 「この件はまだナレッジ化されていません」+[ナレッジ化候補として記録する]ボタン(POST /api/demo/feedback)。記録された候補は[取り込み]タブ下部に一覧表示(管理者が次の資料収集・ヒアリングの参考にする)。
- バンドル未出力時: 入力欄を無効化し「先に[出力]タブで OKF を出力してください」を表示。
- 会話履歴はページ内(クライアント側)保持のみ。直近6往復を API に送る。リロードで消える旨を小さく表示。

### 11.2 API(全て JSON、prefix /api)

| Method/Path | 内容 |
|---|---|
| GET /api/summary | ダッシュボード件数 |
| POST /api/jobs/ingest_analyze | S1〜S4 実行(既に running なら 409) |
| POST /api/jobs/publish | S6 実行 |
| GET /api/jobs/current | 実行中ジョブ progress/message(無ければ null) |
| GET /api/questions?status=open | priority, 作成順ソート |
| POST /api/questions/{id}/answer | body: {choice?, text?} → S5 反映(+必要なら reconsolidate ジョブ) |
| POST /api/questions/{id}/skip | |
| GET /api/concepts / GET /api/concepts/{id} | |
| GET /api/publish/download | zip 返却(FileResponse) |
| POST /api/open_folder | body: {target: "input"|"output"} → os.startfile |
| GET /api/demo/status | バンドル有無・concept件数・最終出力日時 |
| POST /api/demo/ask | body: {question, history:[{role,text}]} → {answer_md, used:[{path,title,status}], reason, not_found}。同期実行 |
| GET /api/demo/file?path=... | バンドル内 md の本文。§10.9-3 のパス検証必須(違反は 400) |
| POST /api/demo/feedback | body: {question, note?} → demo_feedback へ記録 |

ジョブは同時1件のみ(グローバルロック)。/api/demo/ask は読み取り専用のためジョブロックの対象外(LLM 並列数 max_concurrency は共有)。サーバは `uvicorn` を `app/server.py` の `main()` から起動(`uvicorn.run(app, host="127.0.0.1", port=cfg.port)`)。

### 11.3 挙動の細部

- ポーリングは実行中ジョブがある時のみ 2 秒間隔、無ければ停止(ページ遷移不要のためのミニマム実装。WebSocket 不使用)。
- 例外時はトースト表示(赤)+ `workspace/logs/app.log` へスタックトレース。ベテランには「管理者にご連絡ください」と表示。
- ブラウザは既定ブラウザ。IE 非考慮、Edge/Chrome 前提の素直な JS(fetch, async/await 可)。

## 12. 起動・配布

### 12.1 start.bat(この内容をそのまま作成)

```bat
@echo off
chcp 65001 >nul
cd /d "%~dp0"
set PYTHONUTF8=1

where uv >nul 2>nul
if errorlevel 1 (
  echo [エラー] uv が見つかりません。管理者にご連絡ください。
  pause
  exit /b 1
)

uv sync --frozen >nul 2>workspace_setup_error.log
if errorlevel 1 (
  echo [エラー] セットアップに失敗しました。workspace_setup_error.log を管理者に送ってください。
  pause
  exit /b 1
)

uv run python -m app.server
if errorlevel 1 pause
```

- ブラウザ起動は Python 側で行う: サーバ起動直後に `webbrowser.open("http://127.0.0.1:8765/")`(uvicorn 起動前に `threading.Timer(1.5, ...)` で予約)。
- ポート使用中(既に起動済み)の場合: bind 失敗を捕捉し、「既に起動しています。ブラウザを開きます」と表示してブラウザだけ開いて正常終了する。
- 初回セットアップ(uv インストール、config.toml 編集、社内ミラー設定)は管理者作業とし、`README.md` に管理者向け手順を書く(実装AIが作成)。ベテランの操作は start.bat ダブルクリックのみ。

### 12.2 pyproject.toml 依存(これ以外を追加する場合は §0-4 に従う)

```toml
[project]
name = "knowledge-okf-app"
version = "0.1.0"
requires-python = ">=3.12"
dependencies = [
  "fastapi>=0.115",
  "uvicorn>=0.30",
  "jinja2>=3.1",
  "openai>=1.40",
  "pydantic>=2.7",
  "extract-msg>=0.48",
  "python-pptx>=1.0",
  "openpyxl>=3.1",
  "python-docx>=1.1",
  "pymupdf>=1.24",
  "rapidfuzz>=3.9",
  "pyyaml>=6.0",
  "pywin32>=306; sys_platform == 'win32'",
]
[dependency-groups]
dev = ["pytest>=8.2", "httpx>=0.27"]
```

## 13. 非機能・運用

- **機密**: 全データはローカル保存。外部送信は LLM API への抽出テキスト/画像のみ(社内承認済みAPI前提)。この旨を README に明記。
- **規模想定**: ファイル 2,000 件 / 合計 5GB / メール 10,000 通まで(§18)。増分処理により2回目以降は差分のみ。
- **中断耐性**: 各ステージはチャンク/クレーム単位で DB コミット。ジョブ再実行時は未処理分から再開(status で判定)。アプリ強制終了→再起動で壊れない(SQLite WAL)。
- **ログ**: `logging` + RotatingFileHandler(5MB×3)。LLM 呼び出しはトークン数を llm_calls に記録し、ダッシュボードに累計表示。
- **Windows 注意点**: コンソール CP932 対策に `PYTHONUTF8=1`(bat で設定済み)。パスは常に Path。COM はジョブスレッドで CoInitialize/CoUninitialize。OneDrive 配下の input はファイルロックに注意(読み取り失敗はリトライ1回→エラー記録)。

## 14. テスト計画

### 14.1 方針

- 全テストは **LLM_MOCK=1 で決定的に**動く。実APIを叩くテストは作らない。
- COM 依存テストは `@pytest.mark.skipif(not _office_available(), ...)` でスキップ可能にする(CI は Office 無し前提)。COM 無し環境でもパイプライン全体はテキスト経路で通ること。

### 14.2 フィクスチャ(tests/fixtures/docs/ — 生成スクリプト `make_fixtures.py` を同梱し、生成物もコミット)

- `sample.pptx`: python-pptx で生成。3スライド+ノート。ノートに `【モック指示:claim=プレス温度は120度に設定する】` を仕込む。
- `sample_conflict.eml`: 本文に `【モック指示:conflict=プレス温度は135度に設定する】` を含む .eml(テキストで直接作成)。→ モックS3で 120度 vs 135度 の conflict が必ず生成される。
- `sample.xlsx`: openpyxl で生成。2シート、結合セル、セルコメント入り。
- `sample.docx`: python-docx で生成。見出し+表。
- `sample.pdf`: pymupdf で生成(テキスト1ページ)。
- `sample.msg` は実物生成が困難なため、msg extractor は extract_msg を monkeypatch した単体テストで検証(subject/body/添付再帰の呼び出し)。
- `samples/`(§16.1 デモ用)には上記と同等の内容をコピー。

### 14.3 テスト一覧(最低限)

| テスト | 内容 |
|---|---|
| test_extractors_* | 各形式のテキスト/locator/notes/コメント抽出、上限・エンコーディング処理 |
| test_ingest_incremental | 同一ファイル再実行でスキップされる |
| test_s2_mock | モックで claim が生成され provenance が付く |
| test_s3_conflict | 120度/135度が conflict になり、trust差裁定と disputed 分岐が仕様どおり |
| test_s4_questions | gap/conflict 質問生成、conflict の options 固定文言 |
| test_s5_answer_flow | 回答→rejected/verified 遷移、再統合、skipped 再オープン |
| test_s6_okf | バンドル生成+バリデータ緑(frontmatter必須キー、リンク整合、slug重複なし)、rejected が「過去の記述との差異」に載る |
| test_api_* | FastAPI TestClient で全エンドポイント(409含む) |
| test_llm_parse | フェンス付き/前後ノイズ付きJSONのパース、フォールバック再依頼 |
| test_okf_hierarchy | ルート→大→小→concept のリンク到達性、ascii slug、絶対パス/バックスラッシュ検出でバリデータが赤になる |
| test_categorize | taxonomy 生成(モック)、再 publish での冪等性(既存体系維持)、misc/general フォールバック |
| test_demo_manifest | frontmatter からの索引生成、カテゴリグループ化、バンドル更新でのキャッシュ無効化 |
| test_demo_ask_mock | 選択→回答、[id] 引用、not_found 経路、insufficient→2周目、履歴の受け渡し |
| test_demo_path_guard | `..` や絶対パスを指定した /api/demo/file が 400 |
| test_e2e_mock | §16.1 シナリオを API 経由で通す(受け入れテスト) |

## 15. マイルストーン(この順で実装)

| M | 内容 | Done の定義 |
|---|---|---|
| M0 | リポジトリ骨格、pyproject、config、DB、start.bat、FastAPI+全タブの空画面、モックLLM、`pytest` 動作 | start.bat でブラウザが開き5タブが表示される。テスト緑 |
| M1 | S1 全形式 extractor+増分+取り込みUI(ジョブ/進捗) | samples/ を取り込みホームに件数が出る。エラーファイルが一覧表示される |
| M2 | S2 クレーム抽出(モック+実API両対応)+Vision 経路 | 取り込み後に claim が DB に入り、artifacts/ に JSONL が出る |
| M3 | S3 統合・矛盾+S4 質問生成 | conflict サンプルから「食い違いの確認」質問が UI に出る |
| M4 | S5 回答フロー+再統合+status 遷移 | 回答するとナレッジが verified になり、質問が消化される |
| M5 | S6 カテゴリ付与+階層OKF出力+バリデータ+zip | samples/ から §10.8 準拠の階層バンドルが出力されバリデータ緑 |
| M6 | 活用デモモード(モード切替UI+Q&Aエンジン)+E2E 受け入れテスト | §16.1 が全て通る。`test_e2e_mock` 緑 |

## 16. 受け入れ基準

### 16.1 E2E シナリオ(モックモードで再現可能であること)

1. `samples/` の全ファイルを `input/` にコピー
2. `start.bat` 実行 → ブラウザが開く(モックモード表示)
3. [取り込み] → 実行 → 進捗が動き完了。ホームにファイル数・知識数・ナレッジ数が表示される
4. [質問に答える] に「教えてほしいこと」1件以上と「食い違いの確認」(120度 vs 135度)1件以上が出る
5. 食い違いに「Aが正しい」+補足を入力して回答 → 該当ナレッジが verified になり、135度側は除外される
6. [出力] → OKF出力 → zip ダウンロード可。バンドル内で: ルート index → 大分類 → 小分類 → concept と相対リンクで到達できる/verified concept の frontmatter が §10.8 準拠(summary, category 含む)/「過去の記述との差異」に 135度の旧記述が注意として残る/_meta/open-questions.md に未回答分が載る
7. 「▶ 活用デモを試す」→ チャットで「プレスの温度は何度に設定する?」と質問 → 回答に 120度 が [id] 引用付きで表示され、「参照したナレッジ」チップから該当 md がモーダルで開く
8. ナレッジに無い質問(例「塗装の乾燥時間は?」)→ not_found 応答+[ナレッジ化候補として記録]が動作し、[取り込み]タブ下部に候補が表示される
9. 「◀ 整備モードに戻る」で元のタブ群に戻る

### 16.2 自己レビューチェックリスト(各マイルストーンで消し込み)

- [ ] 日本語パス・空白入りパスで動作(fixtureに `テスト 資料` フォルダを含めて確認)
- [ ] 外部通信は LLM API のみ(grep で http クライアント使用箇所を確認)
- [ ] CDN 参照が無い(templates/static を grep)
- [ ] ベテラン向け画面に専門用語・英語エラーが出ない
- [ ] ジョブ中の例外がアプリを落とさず、UI とログに残る
- [ ] `uv run pytest -q` 緑 / `start.bat` からのスモーク手順を PROGRESS.md に記録
- [ ] /api/demo/file のパストラバーサル対策をテストで確認済み
- [ ] バンドル内に絶対パス・バックスラッシュ区切り・日本語ディレクトリ名が無い(バリデータ+grep)
- [ ] 新規 `[ASSUME]` を QUESTIONS.md に転記済み

## 17. 実装AIの作業ループ規約

1. マイルストーン開始時: 本書の該当節を PROGRESS.md にチェックリスト化(要件の再確認に相当)。曖昧点は QUESTIONS.md へ記載し、§18 のデフォルトで続行。
2. 実装 → テスト作成/更新 → `uv run pytest -q` 緑 → §16.2 消し込み → PROGRESS.md 更新、の順を厳守。テストを後回しにしない。
3. リファクタは動くテストを保ったまま小さく行う。マイルストーンをまたぐ大規模書き換えをしない。
4. 本書と矛盾する実装判断が必要になった場合: 本書を書き換えず、QUESTIONS.md に「提案」として差分を記載し、暫定実装には `[ASSUME]` を付す。

## 18. デフォルト値・確認事項(人間が後で調整する想定)

| 項目 | デフォルト | 備考 |
|---|---|---|
| model | "gpt-5.6" | config.toml で変更 |
| base_url | ダミー(example) | 管理者が実URLを設定 |
| structured_output | auto | ゲートウェイ非対応なら自動 off |
| ポート | 8765 | |
| 1ファイル上限 | 200MB | |
| Excel 表上限 | 200行×30列/シート | |
| old_doc_years | 5年 | 信頼度減衰の閾値 |
| trust 重み | §10.7 の表 | 精査の感度調整ポイント |
| 質問数上限 | 3問/Concept | |
| 規模想定 | 2,000ファイル/5GB/メール1万通 | 超過時は分割投入を README に記載 |
| demo_max_files | 8 | 活用デモ: 1質問あたりの読込上限 |
| demo_max_rounds | 2 | 活用デモ: 選択→回答の最大周回 |
| 索引2段化の閾値 | manifest 8,000字 | 超過時は大分類の先行選択 |
| taxonomy 上限 | 大分類7×小分類7 | |
| カテゴリdir命名 | ascii ケバブケース | zip共有時の文字化け回避(§10.8)。日本語名は index.md 側 |
| デモ会話履歴 | 直近6往復 | クライアント側保持のみ |

---
以上。実装AIは §0 に戻り、M0 から着手すること。
