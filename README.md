# Headline Analyzer

## 概要
Headline Analyzerは、キーワードをGoogle検索し、検索結果のウェブサイトから見出しを自動抽出し、OpenAI APIを使用してSEOコンテンツ制作のための競合分析を行うPythonプログラムです。

## 主な機能
- **Google検索**: SerpAPI経由で指定キーワードのGoogle検索を実行
- **見出し抽出**: 検索結果のURLからタイトルと見出し(H2, H3, H4)を自動抽出
- **インデント付き表示**: 見出しレベルに応じたインデント付きで見出し階層を表示
- **AI分析**: OpenAI APIを利用してSEOコンテンツ制作に必要な競合分析を実施
  - 複数サイト共通の見出し要素を抽出
  - サイト固有の見出し要素を分析
  - SEO対策の観点から見出し構成を評価
- **結果ファイル保存**: 分析結果を`summary/`ディレクトリに自動保存

## ファイル構成
| ファイル | 説明 |
|---------|------|
| `main.py` | メイン実行ファイル（ユーザー入力を受け取り処理実行） |
| `headline_analyzer.py` | 検索・抽出・分析を統括するメインロジック |
| `head_line_extractor.py` | URLから見出しを抽出するクラス |
| `google_searcher.py` | SerpAPIを使用したGoogle検索機能 |
| `openai_adapter.py` | OpenAI ChatGPT APIの統括クラス |
| `system_prompt.md` | AI分析用のシステムプロンプト定義 |
| `summary/` | 分析結果出力ディレクトリ |
| `.env` | API キーの設定ファイル（git管理外） |

## 必要な環境
- Python 3.8以上

## インストール

1. 必要なPythonパッケージをインストール:
   ```pwsh
   pip install -r requirements.txt
   ```

2. 環境変数を設定（`.env`ファイルを作成）:
   ```
   OPENAI_API_KEY=your_openai_api_key
   SERP_API_KEY=your_serpapi_key
   ```

## 使い方

```pwsh
python main.py
```

実行後、クエリ（キーワード）を入力するとプログラムが以下の処理を実行します:

1. Google検索（最大10件のURL取得）
2. 各URLから見出しを抽出
3. OpenAI APIを使用してSEO観点から競合分析
4. 関連キーワードの表示
5. 結果を`summary/{query}.txt`に保存

## 例
```
クエリを入力：システム開発 詳細設計
```

上記を入力すると、「システム開発 詳細設計」に関するGoogle検索結果から複数サイトの見出しを抽出し、AIが競合分析を行います。
