from pathlib import Path
from extract import extract_csv_tables, extract_pdf_tables, extract_excel_tables
from query import query_financials, query_financials_from_excel, expose_schema, expose_schema_from_excel
import pandas as pd

BASE_DIR = Path(__file__).resolve().parent
DATA_DIR = BASE_DIR.parent / "data"

def run_extraction():
    dfs = []
    for pdf_file in Path(DATA_DIR).glob("*.pdf"):
        dfs.append(extract_from_pdf(pdf_file))
    
    for csv_file in Path(DATA_DIR).glob("*.csv"):
        dfs.append(extract_from_csv(csv_file))

    for csv_file in Path(DATA_DIR).glob("*.xlsx"):
        dfs.append(extract_from_excel(csv_file))

def extract_from_csv(path: Path):
    df = extract_csv_tables(path)

    print(f"\n Schema for {path} (Columns):")
    print(expose_schema(df))

    query_financials(df);

def extract_from_excel(path: Path):
    df = extract_excel_tables(path)

    print(f"\n Schema for {path} (Sheet Name: Columns):")
    print(expose_schema_from_excel(df))

    query_financials_from_excel(df, "Finance Monthly");

def extract_from_pdf(path: Path) -> pd.DataFrame:
    df = extract_pdf_tables(path)

    print(f"Extracted from: {path}")

def main():
    print("Hello from dataprocessor!")

    run_extraction()


if __name__ == "__main__":
    main()
