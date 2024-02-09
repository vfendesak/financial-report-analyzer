import json
import time
from pathlib import Path

from tqdm import tqdm

from analyzer.scraping import Scraper
from analyzer.utils import load_tickers


def main():
    tickers = load_tickers()
    scraper = Scraper(tickers)

    def load_filings():
        with open(Path(__file__).parent.parent / "filings.json", "r") as f:
            filings = json.load(f)
        return filings

    existing_filings = load_filings()

    filings = {}

    for ticker in tqdm(tickers[69:], ncols=60):
        try:
            filings[ticker] = scraper.get_10k_filings(ticker)
            time.sleep(1)
        except Exception:
            filings[ticker] = {}
            continue

    existing_filings.update(filings)

    with open("filings.json", "w") as f:
        json.dump(existing_filings, f)


if __name__ == "__main__":
    main()
