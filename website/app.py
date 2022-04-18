from urllib import request
from flask import Flask, render_template, request, redirect
from flask_mysqldb import MySQL
# import yaml

app = Flask(__name__)

# db=yaml.load(open('db.yaml'))
# app.config['MYSQL_HOST']=db['mysql_host']
# app.config['MYSQL_USER']=db['mysql_user']
# app.config['MYSQL_PASSWORD']=db['mysql_password']
# app.config['MYSQL_DB']=db['mysql_db']
app.config['MYSQL_HOST']='localhost'
app.config['MYSQL_USER']='root'
app.config['MYSQL_PASSWORD']='7061'
app.config['MYSQL_DB']='olx'

mysql=MySQL(app)

@app.route("/", methods=['GET', 'POST'])
def template():
    if request.method=='POST':
        userDetails=request.form
        userid=userDetails['userid']
        customer_name=userDetails["customer_name"]
        customer_mobile=userDetails["customer_mobile"]
        customer_email=userDetails['customer_email']
        gender=userDetails['gender']
        city_name=userDetails['city_name']
        state_name=userDetails['state_name']
        age=userDetails['age']
        cur=mysql.connection.cursor()
        cur.execute("INSERT INTO user_details(user_id,customer_name,customer_mobile,customer_email,gender,city_name,state_name,age) VALUES(%s,%s,%s,%s,%s,%s,%s,%s)",(userid,customer_name,customer_mobile,customer_email,gender,city_name,state_name,age))
        mysql.connection.commit()
        cur.close()
        return redirect('/homepage')
    return render_template('index.html')
@app.route('/users')
def users():
    cur=mysql.connection.cursor()
    resultVAlue=cur.execute("select DISTINCT(seller_id) from (select seller_id from product_table) AS temp1 where seller_id NOT IN(SELECT seller_id FROM (select* from(select DISTINCT(seller_id)from product_table) AS temp2 cross join (select type_id from type_table) AS temp3)AS temp4 WHERE (seller_id,type_id) NOT IN( select seller_id,type_id from product_table));")
    if resultVAlue>0:
        userDetails=cur.fetchall()
        return render_template('users.html', userDetails=userDetails)

@app.route('/homepage')
def Homepage():
    cur=mysql.connection.cursor()
    resultVAlue=cur.execute("select DISTINCT(seller_id) from (select seller_id from product_table) AS temp1 where seller_id NOT IN(SELECT seller_id FROM (select* from(select DISTINCT(seller_id)from product_table) AS temp2 cross join (select type_id from type_table) AS temp3)AS temp4 WHERE (seller_id,type_id) NOT IN( select seller_id,type_id from product_table));")
    if resultVAlue>0:
        userDetails=cur.fetchall()
        return render_template('homepage.html', userDetails=userDetails)
if __name__=='__main__':
    app.run(debug=True)
