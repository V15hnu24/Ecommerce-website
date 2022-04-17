from sqlite3 import connect
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

'''
drop table statewise_products;
create table statewise_products(
	state_code	integer not null AUTO_INCREMENT,
    state varchar(125),
    total_products integer
    ,primary key (state_code)
);
'''

#2
mycursor.execute("drop table statewise_products;")
mycursor.execute(" create table statewise_products( state_code integer not null AUTO_INCREMENT,state varchar(125), total_products integer,primary key (state_code));")

temp = "INSERT INTO statewise_products (state,total_products) values"

for i in range(len(result)):
    mycursor.execute(temp + str(result[i])+";")

mydb.commit()

mycursor.execute("Select * from statewise_products")

result2 = mycursor.fetchall()

print(result2)