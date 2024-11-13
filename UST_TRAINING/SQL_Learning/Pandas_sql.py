import pandas as pd
import sqlite3

connection = sqlite3.connect(r'C:\Users\Administrator\Desktop\Python_Training\UST_TRAINING\SQL_Learning\Chinook_Sqlite.sqlite')

query1 = """
    SELECT * FROM Customer LIMIT 10
"""

query2 = """
    SELECT BillingCountry, SUM(Total) AS Sales_Total  
    FROM Invoice 
    GROUP BY BillingCountry
"""
query = "SELECT * FROM Invoice"

df_customers = pd.read_sql_query(query,connection)
df_customers
print(df_customers)
connection.close()