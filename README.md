# Stock Data ETL Pipeline

This project is an Extract-Transform-Load (ETL) pipeline for stock price data. It extracts data from an external stock API, transforms it into a structured format, and loads it into a PostgreSQL data warehouse.

## Project Structure

```bash
STOCKS_ETL/
├── data/
│   ├── raw/
│   │   └── stock_data.json         # Raw data from API
│   └── processed/
│       └── stock_data_processed.json  # Transformed data
├── src/
│   ├── extract.py                  # Contains logic for data extraction
│   ├── transform.py                # Contains logic for data transformation
│   ├── load.py                     # Loads processed data into PostgreSQL
│   ├── orchestrator.py             # Orchestrates the ETL pipeline
│   └── utils.py                    # Utility functions (e.g., logging)
├── tests/
│   ├── test_extract.py             # Unit tests for data extraction
│   ├── test_transform.py           # Unit tests for data transformation
│   └── test_load.py                # Unit tests for data loading
├── requirements.txt                # Required Python libraries
└── README.md                       # Project documentation
