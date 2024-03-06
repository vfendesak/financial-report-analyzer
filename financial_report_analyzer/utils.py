import json
from pathlib import Path

import pandas as pd
import yaml

DEFAULTS_PATH = Path(__file__).parent / "defaults"


def load_ticker_data(tickers_name):
    with open(DEFAULTS_PATH / f"{tickers_name}.yaml", "r") as f:
        ticker_data = yaml.load(f, Loader=yaml.FullLoader)
    return ticker_data


def load_tickers(tickers_name):
    ticker_data = load_ticker_data(tickers_name)
    return list(ticker_data.keys())


def load_filings(tickers_name):
    with open(Path(__file__).parent.parent / f"{tickers_name}.yaml", "r") as f:
        filings = json.load(f)
    return filings


def create_filings_table(filings):
    rows = []
    for ticker, years in filings.items():
        for year, report_url in years.items():
            row = {"ticker": ticker, "year": year}
            row.update({"filing_url": report_url})
            rows.append(row)

    return pd.DataFrame(rows)
