

import pandas as pd
import numpy as np
"""merge 2 DF"""
df1 = pd.DataFrame({
    'Name' : ['A','B','C','D'],
    'Age' : [20,30,40,50],
    'Place' : ['AB','BC','CD','DE']
})
df2 = pd.DataFrame({
    'Name' : ['A','B','C'],
    'Salary' : [2000,3000,4000],
    'Place' : ['abc','bcd','cde']
})
df3 = pd.merge(df1,df2, on='Name', how='left',suffixes=["_df1","_df2"])

print(df3)