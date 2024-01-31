import time
from scraping import Scraper
import json
from tqdm import tqdm

def load_tickers():
    return ["abt", "aapl"]

def main():

    tickers = load_tickers()
    scraper = Scraper(tickers)

    filings = {}

    for ticker in tqdm(tickers, ncols=60):
        filings[ticker] = scraper.get_10k_filings(ticker)
        time.sleep(1)

    with open("filings.json", "w") as f:
        json.dump(filings, f)


if __name__ == "__main__":
    main()