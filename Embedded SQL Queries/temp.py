import re
from sqlite3 import connect
from unicodedata import category
from unittest import result
import mysql.connector

mydb=mysql.connector.connect(host="localhost",user="root",passwd="7061" ,database = "olx_final")
mycursor = mydb.cursor()

mycursor.execute("select count(*) from user_details")

result = mycursor.fetchall()

print(result[0][0])