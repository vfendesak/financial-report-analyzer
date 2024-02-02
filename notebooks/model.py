from transformers import AutoModelForSequenceClassification, AutoTokenizer, pipeline

TYPES = {
    "env": "ESGBERT/EnvironmentalBERT-environmental",
    "soc": "ESGBERT/SocialBERT-social",
    "gov": "ESGBERT/GovernanceBERT-governance",
}


class Model:
    def __init__(self):
        self = self

    def load_pipe(self, type):
        name = TYPES[type]
        tokenizer = AutoTokenizer.from_pretrained(name)
        model = AutoModelForSequenceClassification.from_pretrained(name)
        return pipeline("text-classification", model=model, tokenizer=tokenizer)
