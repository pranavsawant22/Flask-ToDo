import sqlite3

# makes a new database or connect to already existing databaase
conn = sqlite3.connect('Customer.db')

# create a table
# 1)create a cursor-tells the db what to do

c = conn.cursor()

# 2)
"""
c.execute('''CREATE TABLE customers(
first text,
last text,
email text
)''')"""
# DATATYPES
# int,null,real,blob,text
c.execute('SELECT rowid,* FROM customers ORDER BY first')
items = c.fetchall()

for item in items:
    print(item)

#commit the table
conn.commit()

#close the connection
conn.close()