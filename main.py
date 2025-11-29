from headline_analyzer import HeadlineAnalyzer

def main():
    query = input("クエリを入力：").strip()
    
    if not query:
        print("クエリが空です。終了します。")
        return
    if "　 "  in query:
        query = query.replace("　", " ")

    analyzer = HeadlineAnalyzer(query)
    summary = analyzer.analyze(use_ai_analysis=True)
    print(summary)
    analyzer.save_to_file()

main()