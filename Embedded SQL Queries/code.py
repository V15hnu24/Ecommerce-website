import re
from sqlite3 import connect
from unicodedata import category
from unittest import result
import mysql.connector

mydb = mysql.connector.connect(host="localhost",user="root",passwd="vishnu7879",auth_plugin ='mysql_native_password',database="online_selling")

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

#2
'''
drop table statewise_products;
create table statewise_products(
	state_code	integer not null AUTO_INCREMENT,
    state varchar(125),
    total_products integer
    ,primary key (state_code)
);
'''
#Inserting the data for the table created

mycursor.execute("drop table statewise_products;")
mycursor.execute(" create table statewise_products( state_code integer not null AUTO_INCREMENT,state varchar(125), total_products integer,primary key (state_code));")

temp = "INSERT INTO statewise_products (state,total_products) values"

for i in range(len(result)):
    mycursor.execute(temp + str(result[i])+";")



mycursor.execute("Select * from statewise_products")

result2 = mycursor.fetchall()

print(result2)

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


#4

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

#5

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

mycursor.execute("select * from product_table;")

result5 = mycursor.fetchall()

print(result5)