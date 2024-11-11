import pandas as pd
import re
def ReadContent(file_path):
    try:
        file_handle = open(file_path)
        #Count =0
        WordsCount = {}
        for line in file_handle:
            #Count+=1    
            #print('*** Line ',Count,'***')
            #print(line)
            line=line[:-1:]
            if line.strip() !="":
                #print('*** Line ',Count,'***')
                #print(line)
                cleand_line = re.sub(r'[^a-zA-Z1-9\s\']','',line.lower())
                #print(cleand_line)
                line_list = cleand_line.split(' ')
                #print(line_list)
                for word in line_list:
                    if word not in WordsCount:
                        WordsCount[word] = 1
                    else:
                        WordsCount[word]+=1
        #print('****Output****')
        #print(WordsCount) 
        df_wordCount = pd.DataFrame(WordsCount.items(),columns=['Words','Frequency']) 
        #print(df_wordCount)
        return df_wordCount
    except Exception as e:
        print(f'Error Occurred: {e}')
        return {}


csv_file_path = r'C:\Users\Administrator\Desktop\Python_Training\PythonAssessments\Assessment_01\PrideAndPrjudice.csv'
df_wordfrequency = ReadContent(csv_file_path)
print(df_wordfrequency.head())