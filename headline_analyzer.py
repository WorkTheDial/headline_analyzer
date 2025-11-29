from head_line_extractor import HeadlineExtractor
from openai_adapter import OpenAIAdapter
from google_searcher import GoogleSearcher

class HeadlineAnalyzer:

    def __init__(self, query):
        self.query = query
        self.google_searcher = GoogleSearcher()
        self.elements_texts_combined = ""

    def analyze(self, use_ai_analysis=False):
        urls, related_keywords = self.google_searcher.get_search_result(self.query)

        extractor = HeadlineExtractor(urls)
        self.elements_texts = extractor.extract_elements_text()

        # URLテキストを変数にまとめる
        for i, text in enumerate(self.elements_texts, start=1):
            self.elements_texts_combined += f"--- URL {i} ---\n{text}\n\n"
        
        if use_ai_analysis:
            ai_analysis = self._ai_analysis()
            self.elements_texts_combined += f"\n--- AI Analysis ---\n{ai_analysis}\n"

        self.elements_texts_combined += "\n--- 関連キーワード ---\n" + "\n".join(related_keywords)    
        
        return self.elements_texts_combined

    ## AIによる分析
    def _ai_analysis(self):
        with open("system_prompt.md", "r", encoding="utf-8") as f:
            system_prompt = f.read()
        adapter = OpenAIAdapter(system_prompt)
        return adapter.create_chat(self.elements_texts_combined, model="gpt-4o")
        
        
    ## 結果をファイルに保存
    def save_to_file(self):
        with open(f"summary/{self.query}.txt", "w", encoding="utf-8") as file:
            file.write(self.elements_texts_combined)