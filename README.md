<div align="center">
  <h1>Financial Report Analyzer (FRA)</h1>
</div>

This repo intends to fetch and analyze annual reports in terms of their ESG-related contents.

The annual reports are fetched from the [SEC Edgar database](https://www.sec.gov/edgar). For the analysis, the following pre-trained LLMs are used which can be found on 🤗Hugging Face:

* [ESGBERT/EnvironmentalBERT-environmental](https://huggingface.co/ESGBERT/EnvironmentalBERT-environmental)
* [ESGBERT/SocialBERT-social](https://huggingface.co/ESGBERT/SocialBERT-social)
* [ESGBERT/GovernanceBERT-governance](https://huggingface.co/ESGBERT/GovernanceBERT-governance)

## Usage

### Pull Postgres image

    docker pull postgres


### Start Postgres Container

    docker run --name some-postgres -e POSTGRES_PASSWORD=mysecretpassword -p 5432:5432 -d postgres
