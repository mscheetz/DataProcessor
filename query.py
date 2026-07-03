import pandas as pd

def query_financials(df: pd.DataFrame):
    hightest_mo = df.loc[df["Revenue"].idxmax()]

    print(f"\n{hightest_mo["Month"]} had the highest revenu of {hightest_mo["Revenue"]}")

    top_five = df.nlargest(5, "Revenue")[["Month", "Revenue"]]

    print(f"\nTop 5 Months (Revenue):")
    print(top_five)