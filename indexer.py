# from llama_index.core import SQLDatabase
# from sqlalchemy import create_engine
# engine = create_engine("sqlite:///company.db")
# sql_database=SQLDatabase(engine)
# print("Database Indexed successfully")
import pandas as pd
import sqlite3

conn = sqlite3.connect("./company.db")

def clean_excel(file, table):

    df = pd.read_excel(file, header=None)

    # detect header
    header_row = None
    for i in range(10):
        row = df.iloc[i].astype(str).str.lower()

        if "item name" in row.values or "pur no" in row.values:
            header_row = i
            break

    df = pd.read_excel(file, header=header_row)

    # clean columns
    df.columns = (
        df.columns
        .str.strip()
        .str.replace(" ", "_")
        .str.replace(".", "")
        .str.replace("/", "_")
        .str.upper()
    )

    df = df.dropna(how="all")
    df = df.dropna(axis=1, how="all")

    df.to_sql(table, conn, if_exists="replace", index=False)

    print(table, "loaded")


clean_excel("PURCHASE_UPDATED.xlsx","PURCHASE_table")
clean_excel("PO_UPDATED.xlsx","PO_table")

conn.close()