<div align="center">
  <h1>Financial Report Analyzer</h1>
</div>

This repo intends to fetch and analyze annual reports in terms of their ESG-related contents.

The annual reports are fetched from the [SEC Edgar database](https://www.sec.gov/edgar). For the analysis, the following pre-trained LLMs are used which can be found on 🤗Hugging Face:

* [ESGBERT/EnvironmentalBERT-environmental](https://huggingface.co/ESGBERT/EnvironmentalBERT-environmental)
* [ESGBERT/SocialBERT-social](https://huggingface.co/ESGBERT/SocialBERT-social)
* [ESGBERT/GovernanceBERT-governance](https://huggingface.co/ESGBERT/GovernanceBERT-governance)

# Installation

### Python Setup

Create virtual environment and activate it.

    python -m venv venv

    source venv/bin/activate

Install the requirements.

    pip install -r requirements.txt

Install this repo as a package locally.

    pip install -e .

Optional: Create a jupyter kernel

    pip install ipykernel

    python -m ipykernel install --user --name financial-report-analyzer


### Database Setup

Pull Postgres image.

    docker pull postgres

Run Postgres Container.

    docker run --name some-postgres -e POSTGRES_PASSWORD=mysecretpassword -p 5432:5432 -d postgres

 Set the database credentials accordingly in the [database connector](financial_report_analyzer/database_connector.py).


# Usage

### Fetch filings URLs
Fetch the report URLs for the annual report 10-K filings of the [default tickers](financial_report_analyzer/defaults/tickery.yaml).

    python scripts/sec_filings_loader.py

### Analyze the filings
Analyze the reports. This feature is currently performed in the [Filing Analyzer Notebook](notebooks/filing_analyzer.ipynb). In the future this will also be an executable.


# Configuration

At the moment, only SEC filings can be analyzed, hence only US stocks. This will be expanded to European stocks in the future.
The tickers can be set in the [default tickers](financial_report_analyzer/defaults/tickery.yaml).

```yaml
A:
  name: AGILENT TECHNOLOGIES INC
  weight: 0.126698730195312
AAL:
  name: AMERICAN AIRLINES GROUP INC
  weight: 0.02926188514229
AAPL:
  name: APPLE INC
  weight: 9.22121612552533
```

The name and weight are currently not required but will be used for further analysis.

