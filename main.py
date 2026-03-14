import pandas as pd
import sqlite3
import os

if os.path.exists("company.db"):
    os.remove("company.db")

conn = sqlite3.connect("./company.db")


PO = pd.read_excel("/Users/sanyamtiwari/Desktop/excel_ai_project/PO_REGISTER.xlsx")
PURCHASE = pd.read_excel("/Users/sanyamtiwari/Desktop/excel_ai_project/PURCHSE_REGISTER (2).xlsx")


PO.to_sql("PO_TABLE", conn, if_exists="replace", index=False)
PURCHASE.to_sql("PURCHASE_TABLE", conn, if_exists="replace", index=False)

print("Excel files dumped successfully in SQLite")

conn.close()
#verify
# cursor=conn.cursor()
# cursor.execute("SELECT * FROM PO_table")
# rows=cursor.fetchall()
# print(rows)
