# DataProcessor

Extract, clean, and query financial data from PDF, CSV, and Excel files.

## Features

- **PDF table extraction** — parse tabular data from PDFs using `pdfplumber`
- **CSV ingestion** — load and normalize CSV files
- **Excel ingestion** — load all sheets from `.xlsx`/`.xls` workbooks
- **Multi-sheet queries** — query a named sheet from an Excel workbook
- **Numeric cleaning** — auto-convert currency (`$`), comma-separated, and percentage columns to numeric types
- **Date formatting** — convert datetime months to readable `"Mon YYYY"` format
- **Schema inspection** — expose column names per sheet or dataframe
- **SQL queries via DuckDB** — run ad-hoc SQL against in-memory DataFrames
- **Sheet-targeted SQL** — query a named Excel sheet with SQL
- **Financial queries** — identify highest-revenue month and top 5 months

## Usage

```bash
uv run python src/main.py
```

Place input files in `data/` (PDF, CSV, XLSX). Outputs extracted results and queries to stdout.

## Project Structure

```
src/
  main.py     — entrypoint, orchestrates extraction
  extract.py  — PDF/CSV/Excel parsing + numeric column normalization
  query.py    — financial analysis + DuckDB SQL queries + schema inspection
data/         — input data files
```

## Requirements

- Python >= 3.12
- duckdb >= 1.5.4
- openpyxl >= 3.1.5
- pandas >= 3.0.3
- pdfplumber >= 0.11.10