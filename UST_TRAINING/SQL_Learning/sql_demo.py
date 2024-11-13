import sqlite3

connection = sqlite3.connect(r'C:\Users\Administrator\Desktop\Python_Training\UST_TRAINING\SQL_Learning\Chinook_Sqlite.sqlite')

curr = connection.cursor()

# # print(curr)

# # curr.execute("SELECT name FROM sqlite_master WHERE type = 'table';")
# # tables = curr.fetchall()
# # for table in tables:
# #     print(table)

# curr.execute("SELECT * FROM 'Album' LIMIT 10")
# data = curr.fetchall()
# for row in data:
#     print(row)

# desc = curr.description
# cols = [col[0] for col in desc]
# print(cols)

# Create Operation
# (Customer Id, First NAme, Last Name, Company , Email , Country, Phone)
# new_Customer = ('60','Rajiv','RR','ABC','RajivRR@gmail.com','IND')
# curr.execute(
#     """INSERT INTO Customer(CustomerId,FirstName,LastName,Company,Email,Country) VALUES (?,?,?,?,?,?)""",new_Customer
# )
# connection.commit()
# print('New Customer Added')

# #Read Customer
# curr.execute("SELECT * FROM Customer WHERE CustomerId = 60")
# data = curr.fetchall()
# print(data)

#Update Customer
# new_Email ='RajivRR@ust.com'
# curr.execute(
#     """UPDATE Customer
#     SET Email='RajivRR@ust.com',Company = 'UST'
#     WHERE CustomerId = 60"""
# )
# connection.commit()
# print('Customer Updated')

# #Read Customer
# curr.execute("SELECT * FROM Customer WHERE CustomerId = 60")
# data = curr.fetchall()
# print(data)

#Delete from Customer
curr.execute("""
    DELETE FROM Customer WHERE CustomerId = 60
""")