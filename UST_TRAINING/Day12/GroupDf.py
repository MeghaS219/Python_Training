import pandas as pd
import numpy as np


df = pd.DataFrame({
    'Store': ['Store1','Store1','Store2','Store2','Store3','Store3'],
    'Region': ['North','North','South','South','West','West'],
    'Sales': [450,502,505,450,500,600]
})
print(df)
df1 = df.groupby(['Region']).agg({'Sales':np.mean}).reset_index()
print(df1)