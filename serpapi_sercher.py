import requests
import dotenv
import os

dotenv.load_dotenv()

class SerpApiSearch:
    def __init__(self):
        self.api_key = os.environ.get("SERP_API_KEY1")
        self.urls = []
        self.related_keywords = []  # 関連キーワードを保持するためのリスト

    def search(self, query):
        params = {
            "engine": "google",
            "q": query,
            "api_key": self.api_key,
            "location": "Japan"
        }

        response = requests.get("https://serpapi.com/search", params=params)
        data = response.json()

        # 検索結果からURLを抽出してリストに追加
        self.urls = [result.get("link") for result in data.get("organic_results", [])]

        # 関連キーワードを抽出してリストに追加
        self.related_keywords = [keyword.get("query") for keyword in data.get("related_searches", [])]

    def get_urls(self):
        return self.urls

    def get_related_keywords(self):
        return self.related_keywords
