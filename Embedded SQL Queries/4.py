import re
from sqlite3 import connect
from unicodedata import category
from unittest import result
import mysql.connector

mydb = mysql.connector.connect(host="localhost",user="root",passwd="vishnu7879",auth_plugin ='mysql_native_password',database="online_selling")

mycursor = mydb.cursor()

'''
select customer_name, customer_mobile, count(*) as count
from user_details
where user_id in (select buyer_id
				from sold_product)
group by customer_name
having count > 0
order by count desc
'''

mycursor.execute("select customer_name, customer_mobile, count(*) as count from user_details where user_id in (select buyer_id from sold_product) group by customer_name having count > 0 order by count desc;")

result4 = mycursor.fetchall()

print(result4)
