import teradata
import pandas as pd
from openpyxl import Workbook

# Connect to Teradata
udaExec = teradata.UdaExec(appName="test", version="1.0", logConsole=False)
session = udaExec.connect(method="odbc", system="hostname", username="user", password="password")

# Read the SQL files
sql_file1 = open("sql_file1.sql", "r")
sql_file2 = open("sql_file2.sql", "r")
query1 = sql_file1.read()
query2 = sql_file2.read()

# Execute the SQL queries and save the results to dataframes
df1 = pd.read_sql(query1, session)
df2 = pd.read_sql(query2, session)

# Create the workbooks
wb1 = Workbook()
wb2 = Workbook()

# Write the dataframes to the worksheets
with pd.ExcelWriter("output.xlsx") as writer:
    df1.to_excel(writer, sheet_name="Sheet1", index=False)
    df2.to_excel(writer, sheet_name="Sheet2", index=False)

# Save the workbooks
wb1.save("output1.xlsx")
wb2.save("output2.xlsx")
