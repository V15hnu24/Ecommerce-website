
import mysql.connector
mydb=mysql.connector.connect(host="localhost",user="root",passwd="7061" ,database = "olx_final")

def forUSer_Details():
    mycursor = mydb.cursor()
    query="SHOW INDEX FROM olx_final.user_details;"
    mycursor.execute(query)
    myresult = mycursor.fetchall()
    print('Indexes for USerDetails: ')
    for x in myresult:
        print(x)
    print()

def product_table():
    mycursor = mydb.cursor()
    query="SHOW INDEX FROM olx_final.product_table;"
    mycursor.execute(query)
    myresult = mycursor.fetchall()
    print('Indexes for product table: ')
    for x in myresult:
        print(x)
    print()

def area_table():
    mycursor = mydb.cursor()
    query="SHOW INDEX FROM olx_final.area_table;"
    mycursor.execute(query)
    myresult = mycursor.fetchall()
    print('Indexes for area table: ')
    for x in myresult:
        print(x)
    print()

def chat_table():
    mycursor = mydb.cursor()
    query="SHOW INDEX FROM olx_final.chat_table;"
    mycursor.execute(query)
    myresult = mycursor.fetchall()
    print('Indexes for chat table: ')
    for x in myresult:
        print(x)
    print()
def sold_product():
    mycursor = mydb.cursor()
    query="SHOW INDEX FROM olx_final.sold_product;"
    mycursor.execute(query)
    myresult = mycursor.fetchall()
    print('Indexes for sold product: ')
    for x in myresult:
        print(x)
    print()

def type_table():
    mycursor = mydb.cursor()
    query="SHOW INDEX FROM olx_final.type_table;"
    mycursor.execute(query)
    myresult = mycursor.fetchall()
    print('Indexes for type table: ')
    for x in myresult:
        print(x)
    print()

def description_table():
    mycursor = mydb.cursor()
    query="SHOW INDEX FROM olx_final.description_table;"
    mycursor.execute(query)
    myresult = mycursor.fetchall()
    print('Indexes for description table: ')
    for x in myresult:
        print(x)
    print()

forUSer_Details()
sold_product()
product_table()
chat_table()
area_table()
type_table()
description_table()
