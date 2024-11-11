import pandas as pd

print('reading data')
#data=pd.read_csv(r"C:\Users\Administrator\Documents\UST Training\Python-Training\Titanic\titanic.csv")
df = pd.read_csv(r'C:\Users\Administrator\Desktop\Python_Training\UST_TRAINING\Titanic\titanic.csv')
print(df.head())

avg_age_survived = df[df['Survived']==1]['Age'].mean()
avg_age_notsurvived = df[df['Survived']==0]['Age'].mean()

print(avg_age_notsurvived,avg_age_survived)

#print(df.groupby('Sex')['Survived'].mean())

df['family_size']= df['SibSp']+df['Parch']
#print(df[['family_size','SibSp','Parch']].head())

survival_rate_by_family_size = df.groupby('family_size')['Survived'].mean().reset_index()
survival_rate_by_family_size.columns = ['family_size','family_survival_rate']#
#print(survival_rate_by_family_size)

#df = df.merge(survival_rate_by_family_size, on = 'family_size',how='left')


print(df.head())

