from dotenv import load_dotenv
import os
import serpapi

class GoogleSearcher():

    def __init__(self):
        load_dotenv()
        self.client = serpapi.Client(api_key=os.environ.get('SERP_API_KEY'))

    def get_search_result(self, query: str):
        query = query.strip()
        if not query:
            return None

        ## 30件URL取得のため num=30 に変更
        result = self.client.search({
            "q": query,
            "num": "10",      ## ← 最大30件要求
            "engine": "google",
            "location": "Japan"
        })

        organic_results = result.get("organic_results", [])
        if not organic_results:
            return None

        ## URL
        urls = [res.get("link") for res in organic_results if "link" in res]
        
        ## 関連キーワード
        related_keywords = [res.get("query") for res in result.get("related_searches", []) if res.get("query")]

        return urls, related_keywords