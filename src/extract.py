from pathlib import Path
import pdfplumber
import pandas as pd

def extract_excel_tables(path: Path) -> dict[str, pd.DataFrame]:
    if path.suffix.lower() not in [".xlsx", ".xls"]:
        raise Exception("File is not an Excel file")

    if path.exists() == False:
        raise FileNotFoundError(f"No file found at '{path}'")
    
    dfs = pd.read_excel(path, sheet_name=None)

    return dfs

def extract_pdf_tables(path: Path) -> pd.DataFrame:
    if path.suffix.lower() != ".pdf":
        raise Exception("File is not of type pdf")

    if path.exists() == False:
        raise FileNotFoundError(f"No file found at '{path}'")

    all_tables = [];

    with pdfplumber.open(path) as pdf:
        for page in pdf.pages:
            for table in page.extract_tables():
                if not table or len(table) < 2:
                    continue

                header = table[0]
                rows = table[1:]

                df = pd.DataFrame(rows, columns=header)

                df.dropna(how="all")
                
                all_tables.append(df)

    if not all_tables:
        print("No tables found in file")
        return None

    combined_df = pd.concat(all_tables, ignore_index=True)

    return dataframe_numeric_columns(combined_df)

def extract_csv_tables(path: Path) -> pd.DataFrame:
    if path.suffix.lower() != ".csv":
        raise Exception("File is not of type csv")

    if path.exists() == False:
        raise FileNotFoundError(f"No file found at '{path}'")

    df = pd.read_csv(path)
    
    return dataframe_numeric_columns(df)

def dataframe_numeric_columns(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()

    for col in df.columns:
        if (df[col].dtype == "object" 
            or 
            df[col].dtype == "string"):
            cleaned = (
                df[col]
                    .astype(str)
                    .str.replace("$", "", regex=False)
                    .str.replace(",", "", regex=False)
                    .str.replace("%", "", regex=False)
                    .str.strip()
            )

            converted = pd.to_numeric(cleaned, errors="coerce")

            if converted.notna().sum() == df[col].notna().sum():
                df[col] = converted

    return df