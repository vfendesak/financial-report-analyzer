import json
import time
from pathlib import Path

from tqdm import tqdm

from financial_report_analyzer.scraping import SECScraper
from financial_report_analyzer.utils import load_filings, load_tickers


def main():
    tickers = load_tickers()
    existing_filings = load_filings()
    sec_scraper = SECScraper()

    filings = {}

    for ticker in tqdm(tickers, ncols=60):
        try:
            filings[ticker] = sec_scraper.get_10k_filings(ticker)
            time.sleep(1)
        except Exception:
            filings[ticker] = {}
            continue

    existing_filings.update(filings)

    with open("filings.json", "w") as f:
        json.dump(existing_filings, f)


if __name__ == "__main__":
    main()
