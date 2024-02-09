# import re

# from bs4 import BeautifulSoup


# class ReportAnalyzer:
#     def __init__(self, report_url):
#         self.report = load_sentences(report_url)

#     def extract_sentences(self, parser="xml", pattern="span") -> list:
#         soup = BeautifulSoup(self.report.text, parser)
#         sentences = []
#         for span in soup.find_all(pattern):
#             text = span.text
#             if len(text.split(" ")) > 3:
#                 clean_text = text.replace("\n", " ").replace("\xa0", " ")
#                 clean_text = re.sub(r"\s+", " ", clean_text)
#                 clean_text = clean_text.strip()
#                 sentences.append(clean_text)
#         return sentences

#     def load_sentences(report_url: str) -> list:
#         report = fetch_report(report_url)
#         sentences = extract_sentences(report)
#         if len(sentences) == 0:
#             sentences = extract_sentences(report, parser="html.parser", pattern="p")
#         return sentences

#     def analyze_texts(sentences: list, env_pipe, soc_pipe, gov_pipe) -> pd.DataFrame:
#         env = env_pipe(sentences, padding=True, truncation=True)
#         soc = soc_pipe(sentences, padding=True, truncation=True)
#         gov = gov_pipe(sentences, padding=True, truncation=True)

#         env_labels = [x["label"] for x in env]
#         soc_labels = [x["label"] for x in soc]
#         gov_labels = [x["label"] for x in gov]

#         return {
#             "environmental": env_labels,
#             "social": soc_labels,
#             "governance": gov_labels,
#         }

#     def convert_output(x):
#         d = {"none": 0}
#         if x in d:
#             return d[x]
#         return 1
