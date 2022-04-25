import re
from sqlite3 import connect
from unicodedata import category
from unittest import result
import mysql.connector

mydb = mysql.connector.connect(host="localhost",user="root",passwd="vishnu7879",auth_plugin ='mysql_native_password',database="online_selling")

mycursor = mydb.cursor()

''' 
SET FOREIGN_KEY_CHECKS = 0;
delete from product_table
where product_id = 3 and type_id = (select type_id
				from type_table
                where name = 'bike');
'''
mycursor.execute("SET FOREIGN_KEY_CHECKS = 0;")
category = 'bike'
num = '2'
mycursor.execute(" delete from product_table where product_id = "+num+" and type_id = (select type_id from type_table where name = 'bike');")
mycursor.execute("SET FOREIGN_KEY_CHECKS = 1;")

mycursor.execute("select product_id from product_table; where product_id = 3")

result5 = mycursor.fetchall()

print(result5)
