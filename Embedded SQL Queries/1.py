import re
from sqlite3 import connect
from unicodedata import category
from unittest import result
import mysql.connector

mydb=mysql.connector.connect(host="localhost",user="root",passwd="7061" ,database = "olx_final")
mycursor = mydb.cursor()

#1
''' 
select state_name, count(*) as count
from area_table
where area_id in (select city_code
	from product_table)
GROUP BY state_name
order by count(*) DESC
'''

mycursor.execute("select state_name, count(*) as count from area_table where area_id in (select city_code	from product_table) GROUP BY state_name order by count(*) DESC;")

result = mycursor.fetchall()
print(result)