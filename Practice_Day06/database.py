import sqlite3
conn = sqlite3.connect('testdb.sqlite3')
cur = conn.cursor()
# query = '''
# CREATE TABLE Employee2(
# EmpID INTEGER PRIMARY KEY AUTOINCREMENT,
# FIRST_NAME TEXT(20),
# LAST_NAME TEXT(20),
# AGE INTEGER,
# SEX TEXT(1),
# INCOME FLOAT
# )
# '''

# try:
#     cur.execute(query)
#     print("Table created successfully")
# except:
#     print("error in creating table")

# conn.close()

# conn = sqlite3.connect('testdb.sqlite3')
# cur = conn.cursor()
# query = """
# INSERT INTO EMPLOYEE(FIRST_NAME,LAST_NAME,AGE,SEX,INCOME) VALUES
# ("Hello","World",21,"M",300000)
# """
# try: 
#     cur.execute(query)
#     conn.commit()
#     print("Record insert successfully")
# except: 
#     conn.rollback()
# print("error in INSERT successfully")
# conn.close()



conn = sqlite3.connect('testdb.sqlite3')
cur = conn.cursor()
query = """
DELETE FROM EMPLOYEE WHERE INCOME<?
"""


try:
    cur.execute(query,(1000,))
    conn.commit()
    print("Record is deleted")
except Exception as e:
    print('Error: Unable to access data')
conn.close()