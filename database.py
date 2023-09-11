import sqlite3

#Create a database in RAM and Connect
connect = sqlite3.connect('database.db', check_same_thread=False)
if connect:
    print("Creating the DB Connection Successful!")
else:
    print("Connection Failed!!!")

#Create a table named users

#createTBL = connect.execute('CREATE TABLE users (name TEXT)')
#if createTBL:
 #   print("Table Created Successfully!")
#else:
 #   print("Table Creation Failed!!!")