import teradata
import pandas as pd

# Connect to Teradata
udaExec = teradata.UdaExec(appName="TeradataExport", version="1.0", logConsole=False)
session = udaExec.connect(method="odbc", system="teradata_system", username="username", password="password")

# Read SQL from first file
with open('query1.sql', 'r') as f:
    query1 = f.read()

# Execute first SQL query
df1 = pd.read_sql(query1, session)

# Export first result to Excel
with pd.ExcelWriter('output1.xlsx') as writer:
    df1.to_excel(writer, sheet_name='Sheet1', index=False)

# Read SQL from second file
with open('query2.sql', 'r') as f:
    query2 = f.read()

# Execute second SQL query
df2 = pd.read_sql(query2, session)

# Export second result to Excel
with pd.ExcelWriter('output2.xlsx') as writer:
    df2.to_excel(writer, sheet_name='Sheet1', index=False)
