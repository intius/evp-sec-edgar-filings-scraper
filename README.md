# SEC EDGAR Filings Scraper & Unofficial API (Python, Node.js, MCP)

[Run SEC EDGAR Filings Scraper - Full-Text Search & Company Filings on Apify](https://apify.com/evpp/sec-edgar-filings) to export SEC EDGAR Filings data as clean JSON, CSV, Excel, or an API feed. This repository is a developer quick-start kit with working Python and Node.js clients, an MCP configuration, a real sample dataset, and an n8n automation template.

[![Run on Apify](https://img.shields.io/badge/Run%20on-Apify-orange)](https://apify.com/evpp/sec-edgar-filings)

[Open the documentation and crawlable sample explorer](https://intius.github.io/evp-labs-data-extractors/actors/sec-edgar-filings/) for quick inputs, integration links, real sample rows, and ready-made task examples.

## Why use this SEC EDGAR Filings scraper?

- Export SEC EDGAR Filings data without building or maintaining a custom scraper
- Get flat, schema documented JSON ready for analytics, lead generation, market research, and AI agents
- Run manually, on a schedule, through the Apify API, or through MCP compatible AI tools
- Use the included 25+ row sample dataset to prototype before running the live Actor

Built for Investors/analysts, compliance teams, lawyers monitoring disclosures, journalists, AI-agent builders.

## Quick start on Apify

Open [https://apify.com/evpp/sec-edgar-filings](https://apify.com/evpp/sec-edgar-filings) and use this input:

```json
{
  "ticker": "AAPL",
  "forms": "10-K,10-Q,8-K",
  "startDate": "2025-01-01",
  "maxItems": 10
}
```

## Python

```bash
pip install -r requirements.txt
export APIFY_TOKEN=your_apify_token
python python/run.py
```

On Windows PowerShell, use `$env:APIFY_TOKEN="your_apify_token"` instead of `export`.

## Node.js

```bash
npm install
export APIFY_TOKEN=your_apify_token
node node/run.mjs
```

## MCP and AI agents

Add the hosted Apify MCP server from `mcp-config.json` to your MCP client:

```json
{
  "mcpServers": {
    "apify": {
      "type": "http",
      "url": "https://mcp.apify.com/?tools=evpp/sec-edgar-filings"
    }
  }
}
```

Then ask your agent to run `evpp/sec-edgar-filings`, inspect the output schema, or export the latest dataset. The direct MCP URL is `https://mcp.apify.com/?tools=evpp/sec-edgar-filings`.

## n8n automation

Import `n8n-workflow.json` into n8n, select your Apify credential, replace the webhook placeholder, and activate the schedule. The workflow runs the Actor every morning and posts fresh dataset items to your webhook.

## Output schema

| Field | Type | Description |
|---|---|---|
| `accessionNumber` | string | SEC accession number uniquely identifying the filing |
| `form` | string | SEC form type of the filing |
| `filingDate` | string | Date the filing was submitted to EDGAR (YYYY-MM-DD) |
| `reportDate` | string | Period of report / period ending date (YYYY-MM-DD) |
| `cik` | string[] | CIK(s) of the filing entity or entities (10-digit zero-padded) |
| `companyNames` | string[] | Display names of the filing entities |
| `fileNum` | string | SEC file number of the filing |
| `primaryDocument` | string | Filename of the primary document within the filing (company mode) |
| `url` | string | Direct EDGAR URL: primary document in company mode, filing index page in search mode |
| `entityName` | string | Registered entity name (company mode) |
| `ticker` | string | Stock ticker of the filing company (company mode) |
| `sic` | string | SIC industry code or description of the filer |
| `items` | string[] | Item numbers reported in the filing (mainly for 8-K forms) |
| `matchedQuery` | string | Full-text query that produced this item (search mode only) |

## Real sample output

The first sanitized row from the included sample dataset:

```json
{
  "accessionNumber": "0000320193-26-000026",
  "form": "10-K",
  "filingDate": "2026-11-03",
  "reportDate": "2026-09-26",
  "cik": [
    "0000320193"
  ],
  "companyNames": [
    "Apple Inc. (AAPL)"
  ],
  "fileNum": "001-36743",
  "url": "https://www.sec.gov/Archives/edgar/data/320193/000032019326000026/0000320193-26-000026-index.htm",
  "sic": "3571",
  "matchedQuery": "\"artificial intelligence\""
}
```

## Files in this kit

| File | Purpose |
|---|---|
| `python/run.py` | Working Python Apify API example |
| `node/run.mjs` | Working Node.js Apify API example |
| `mcp-config.json` | MCP server configuration for AI agents |
| `sample-output.json` | First five sanitized sample rows |
| `dataset-snapshot.csv` | 25+ row evaluation snapshot |
| `DATASET_CARD.md` | Dataset documentation and provenance |
| `n8n-workflow.json` | Scheduled n8n automation template |

## Fresh data

This repository contains a static evaluation sample. For current data, run the live Actor: https://apify.com/evpp/sec-edgar-filings

## Responsible use

The Actor reads public data from `sec.gov`. Review the source site's terms and applicable privacy rules before production use.
