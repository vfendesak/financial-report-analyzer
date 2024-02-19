import numpy as np
import pandas as pd
from transformers import AutoModelForSequenceClassification, AutoTokenizer, pipeline

MODEL_TYPES = {
    "env": "ESGBERT/EnvironmentalBERT-environmental",
    "soc": "ESGBERT/SocialBERT-social",
    "gov": "ESGBERT/GovernanceBERT-governance",
}


class ScoringModel:
    def __init__(self):
        env_pipe = self.load_pipe("env")
        soc_pipe = self.load_pipe("soc")
        gov_pipe = self.load_pipe("gov")
        self.pipes = {"env": env_pipe, "soc": soc_pipe, "gov": gov_pipe}

    def load_pipe(self, type):
        name = MODEL_TYPES[type]
        tokenizer = AutoTokenizer.from_pretrained(name)
        model = AutoModelForSequenceClassification.from_pretrained(name)
        return pipeline("text-classification", model=model, tokenizer=tokenizer)

    def calculate_report_scores(self, sentences: list) -> dict:
        pd.set_option("future.no_silent_downcasting", True)

        env = self.pipes["env"](sentences, padding=True, truncation=True)
        soc = self.pipes["soc"](sentences, padding=True, truncation=True)
        gov = self.pipes["gov"](sentences, padding=True, truncation=True)
        labels = pd.DataFrame(
            {
                "environmental": pd.DataFrame(env)["label"],
                "social": pd.DataFrame(soc)["label"],
                "governance": pd.DataFrame(gov)["label"],
            }
        ).replace("none", np.nan)
        return (~labels.isna()).astype(int).mean().to_dict()
