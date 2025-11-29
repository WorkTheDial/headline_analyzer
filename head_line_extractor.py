import requests
from bs4 import BeautifulSoup

class HeadlineExtractor:
    def __init__(self, urls):
        self.urls = urls

    def fetch_elements_with_indentation(self, url):
        """指定されたURLからタイトルと見出しを抽出し、見出しレベルに応じたインデントを付与"""
        result = [f"URL: {url}"]  # 最初にURLを追加
        try:
            response = requests.get(url)
            response.raise_for_status()  # エラー時に例外を発生させる
            soup = BeautifulSoup(response.content, 'html.parser')

            # ページタイトルを取得
            title_tag = soup.find('title')
            if title_tag:
                result.append(f"[TITLE] {title_tag.text.strip()}")

            # H2, H3, H4タグを取得して、インデント付きでリストに追加
            for heading in soup.find_all(['h2', 'h3', 'h4']):
                tag_name = heading.name.upper()  # タグ名を大文字で表示
                indent_level = " " * (2 * (int(tag_name[1]) - 2))  # インデントの計算
                result.append(f"{indent_level}[{tag_name}] {heading.text.strip()}")

        except requests.exceptions.RequestException as e:
            result.append(f"Error fetching {url}: {e}")

        return result

    def extract_elements_text(self):
        """URLリストからタイトルと見出しを抽出してリストを返す"""
        all_elements_text = []
        for url in self.urls:
            elements_with_indentation = self.fetch_elements_with_indentation(url)
            all_elements_text.append("\n".join(elements_with_indentation))
        return all_elements_text

if __name__ == "__main__":
    # テスト用のURLリスト
    urls = ["https://products.sint.co.jp/ober/blog/detailed-design-deliverable",
            "https://system-kanji.com/posts/system-detailed-design"]

    extractor = HeadlineExtractor(urls)
    elements_texts = extractor.extract_elements_text()
    for i, text in enumerate(elements_texts, start=1):
        print(f"--- URL {i} ---")
        print(text)
