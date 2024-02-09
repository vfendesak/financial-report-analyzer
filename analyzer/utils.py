from pathlib import Path

import pandas as pd
import yaml
from sqlalchemy import create_engine

DEFAULTS_PATH = Path(__file__).parent / "defaults"
DB_PATH = "postgresql://postgres:test@localhost:5432/esg"


def load_ticker_data():
    with open(DEFAULTS_PATH / "tickers.yaml", "r") as f:
        ticker_data = yaml.load(f, Loader=yaml.FullLoader)
    return ticker_data


def load_tickers():
    ticker_data = load_ticker_data()
    return list(ticker_data.keys())


def create_filings_table(filings):
    rows = []
    for ticker, years in filings.items():
        for year, report_url in years.items():
            row = {"ticker": ticker, "year": year}
            row.update({"filing_url": report_url})
            rows.append(row)

    return pd.DataFrame(rows)


class Connector:
    def __init__(self):
        self.engine = create_engine(DB_PATH)

    def fetch_data(self, table="scores") -> pd.DataFrame:
        return pd.read_sql_table(table, self.engine, index_col="id")

    def store_scores(self, df, table="sec") -> None:
        df.to_sql("sec", self.engine, if_exists="append", index=False)
        return None
