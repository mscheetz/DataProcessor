from pathlib import Path
from extract import extract_csv_tables, extract_pdf_tables
from query import query_financials
import pandas as pd

DATA_DIR = "data"

def run_extraction():
    dfs = []
    for pdf_file in Path(DATA_DIR).glob("*.pdf"):
        dfs.append(extract_from_pdf(pdf_file))
    
    for csv_file in Path(DATA_DIR).glob("*.csv"):
        dfs.append(extract_from_csv(csv_file))

def extract_from_csv(path: Path):
    dataframe = extract_csv_tables(path)

    query_financials(dataframe);

def extract_from_pdf(path: Path) -> pd.DataFrame:
    dataframe = extract_pdf_tables(path)

    print(f"Extracted from: {path}")

def main():
    print("Hello from dataprocessor!")

    run_extraction()


if __name__ == "__main__":
    main()
