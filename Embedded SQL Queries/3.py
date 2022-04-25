import re
from sqlite3 import connect
from unicodedata import category
from unittest import result
import mysql.connector

mydb = mysql.connector.connect(host="localhost",user="root",passwd="vishnu7879",auth_plugin ='mysql_native_password',database="online_selling")

mycursor = mydb.cursor()

#3
'''
select customer_name, customer_mobile, count(*)
from user_details
where user_id in (select seller_id
				from product_table
				where product_id in ( select product_id
									  from sold_product)
				)
group by customer_name
having count(*) > 0
order by customer_name
'''

mycursor.execute("select customer_name, customer_mobile, count(*) from user_details where user_id in (select seller_id	from product_table where product_id in ( select product_id  from sold_product)) group by customer_name having count(*) > 0 order by customer_name")

result3 = mycursor.fetchall()

print(result3)

