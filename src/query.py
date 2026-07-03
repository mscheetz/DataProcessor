import pandas as pd
import duckdb

def expose_schema_from_excel(dfs: dict[str, pd.DataFrame]) -> dict[str, list[str]]:
    return {
        sheet_name: df.columns.tolist()
        for sheet_name, df in dfs.items()
    }

def expose_schema(df: pd.DataFrame) -> list[str]:
    return df.columns.tolist()

def query_financials_from_excel(dfs: dict[str, pd.DataFrame], sheet_name: str):
    if sheet_name not in dfs:
        raise Exception(f"Sheet: '{sheet_name}' does not exist")

    query_financials(dfs[sheet_name])

def query_financials(df: pd.DataFrame):
    if pd.api.types.is_datetime64_any_dtype(df["Month"]):
        df["Month"] = df["Month"].dt.strftime("%b %Y")

    hightest_mo = df.loc[df["Revenue"].idxmax()]

    print(f"\n{hightest_mo["Month"]} had the highest revenu of {hightest_mo["Revenue"]}")

    top_five = df.nlargest(5, "Revenue")[["Month", "Revenue"]]

    print(f"\nTop 5 Months (Revenue):")
    print(top_five)

def execute_query_select_sheet(dfs: dict[str, pd.DataFrame], sql: str, sheet_name: str):
    if sheet_name not in dfs:
        raise Exception(f"Sheet: '{sheet_name}' does not exist")

    print(f"\nQuerying on sheet {sheet_name}")

    execute_query(dfs[sheet_name], sql)

def execute_query(df: pd.DataFrame, sql: str):
    result = duckdb.query(sql).df()

    print(f"\nExecuting query {sql.replace("\n", " ").strip()}:")
    print(result)
