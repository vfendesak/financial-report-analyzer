import re

import pandas as pd
from bs4 import BeautifulSoup

SPECIAL_CHARACTERS = ["\xa0", "☒", "☐", "_"]
SENTENCE_PATTERN = r"(?<!\w\.\w.)(?<![A-Z][a-z]\.)(?<=\.|\?)\s"


class TextExtractor:
    def __init__(self, report):
        self.report = report

    def remove_special_characters(self, text):
        for char in SPECIAL_CHARACTERS:
            char = re.escape(char)
            text = re.sub(char, "", text)
        return text

    def reduce_multiple_spaces(self, text):
        return re.sub(r"\s+", " ", text)

    def extract_sentences(self, text):
        return re.split(SENTENCE_PATTERN, text)

    def clean(self, sentence):
        cleaned_sentences = sentence.strip()
        cleaned_sentences = self.remove_special_characters(cleaned_sentences)
        cleaned_sentences = self.reduce_multiple_spaces(cleaned_sentences)
        return cleaned_sentences

    def get_sentences(self):
        soup = BeautifulSoup(self.report.text, "xml")
        text = soup.get_text()
        sentences = self.extract_sentences(text)
        return [self.clean(sentence) for sentence in sentences if sentence.strip()]

    # def load_sentences(report_url: str) -> list:
    #     report = fetch_report(report_url)
    #     sentences = extract_sentences(report)
    #     if len(sentences) == 0:
    #         sentences = extract_sentences(report, parser="html.parser", pattern="p")
    #     return sentences


# class ReportAnalyzer:
#     def __init__(self, sentences):
#         self.sentences = sentences

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
