# Headline Analyzer

## 概要
Headline Analyzerは、ニュースや記事の見出しを自動で抽出・分析し、OpenAIやSerpAPIなどの外部サービスと連携して、見出しの要約や関連情報の取得を行うPythonプログラムです。

## 主な機能
- ニュースや記事の見出し抽出
- OpenAI APIを利用した見出しの要約や分析
- SerpAPIを利用した検索・情報取得
- コマンドラインからの簡単な実行

## ファイル構成
- `main.py` : メイン実行ファイル
- `head_line_extractor.py` : 見出し抽出ロジック
- `headline_analyzer.py` : 見出しの分析・要約ロジック
- `openai_adapter.py` : OpenAI API連携
- `serpapi_sercher.py` : SerpAPI連携
- `system_prompt.md` : システムプロンプト定義
- `summary/` : 出力結果やサマリーの保存先

## 必要な環境
- Python 3.8以上
- 必要なパッケージは`requirements.txt`に記載（未作成の場合は`openai`, `requests`などをインストールしてください）

## 使い方
1. 必要なPythonパッケージをインストールします。
   ```pwsh
   pip install openai requests
   ```
2. APIキー（OpenAI, SerpAPI）を環境変数または設定ファイルで設定します。
3. `main.py`を実行します。
   ```pwsh
   python main.py
   ```
