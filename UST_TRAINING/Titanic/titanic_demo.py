import pandas as pd

data=pd.read_csv(r"C:\Users\Administrator\Desktop\Python_Training\UST_TRAINING\Titanic\titanic.csv")
# print(data.head())
# print(data['Age'].head())

# df=data[['Age','Sex']]
# print(df.head())

# df=data[data['Age']<25]
# print(df)

#print(len(data.index))

#print(data['Age'].mean())

df=data[(data["Sex"]=='male') & (data['Age']<25)]
print(df['Fare'].mean())

df.to_csv("filtered_titanic.csv",index=False)

#print(len(data[data['Survived']==1].index)/len(data.index) * 100)