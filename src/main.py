from pathlib import Path
from extract import extract_csv_tables, extract_pdf_tables, extract_excel_tables
from query import query_financials, query_financials_from_excel, expose_schema, expose_schema_from_excel, execute_query, execute_query_select_sheet
import pandas as pd

BASE_DIR = Path(__file__).resolve().parent
DATA_DIR = BASE_DIR.parent / "data"

SQL_QUERY = """
SELECT Month, Revenue
FROM df
ORDER BY Revenue DESC
LIMIT 5
"""

def run_extraction():
    dfs = []    
    for csv_file in Path(DATA_DIR).glob("*.csv"):
        dfs.append(extract_from_csv(csv_file))

    for excel_file in Path(DATA_DIR).glob("*.xlsx"):
        dfs.append(extract_from_excel(excel_file))

    for pdf_file in Path(DATA_DIR).glob("*.pdf"):
        dfs.append(extract_from_pdf(pdf_file))

def extract_from_csv(path: Path):
    df = extract_csv_tables(path)

    print(f"\n Schema for {path} (Columns):")
    print(expose_schema(df))

    query_financials(df);

    execute_query(df, SQL_QUERY)

def extract_from_excel(path: Path):
    dfs = extract_excel_tables(path)

    print(f"\n Schema for {path} (Sheet Name: Columns):")
    print(expose_schema_from_excel(dfs))

    sheet_name = "Finance Monthly"

    query_financials_from_excel(dfs, sheet_name);

    execute_query_select_sheet(dfs, SQL_QUERY, sheet_name)

def extract_from_pdf(path: Path) -> pd.DataFrame:
    df = extract_pdf_tables(path)

    print(f"Extracted from: {path}")

def main():
    print("Hello from dataprocessor!")

    run_extraction()


if __name__ == "__main__":
    main()
