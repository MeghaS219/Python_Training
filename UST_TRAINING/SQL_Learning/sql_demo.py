import sqlite3

connection = sqlite3.connect(r'C:\Users\Administrator\Desktop\Python_Training\UST_TRAINING\SQL_Learning\Chinook_Sqlite.sqlite')

cursor = connection.cursor()

print(cursor)
