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

    make setup

#### Optional: Create a Jupyter Kernel

    make kernel

### Database Setup

    POSTGRES_PASSWORD=mysecretpassword make database

 Set the database password accordingly in the [database connector](financial_report_analyzer/database_connector.py) DB PATH constant:

 ```python
DB_PASSWORD = "mysecretpassword"
```

# Usage

### Fetch Filings URLs
Fetch the report URLs for the annual report 10-K filings of the [default tickers](financial_report_analyzer/defaults/tickery.yaml).

    make filings

### Analyze the Filings
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
