from urllib import request
from flask import Flask, render_template, request, redirect
from flask_mysqldb import MySQL
# import yaml

app = Flask(__name__)

# db=yaml.load(open('db.yaml'))
# app.config['MYSQL_HOST']=db['mysql_host']
# app.config['MYSQL_USER']=db['mysql_user']
# app.config['MYSQL_PASSWORD']=db['mysql_password']
# app.config['MYSQL_DB']=`db['mysql_db']
app.config['MYSQL_HOST']='localhost'
app.config['MYSQL_USER']='root'
app.config['MYSQL_PASSWORD']='7061'
app.config['MYSQL_DB']='olx_final'

mysql=MySQL(app)

@app.route("/", methods=['GET', 'POST'])
def template():
    if request.method=='POST':
        userDetails=request.form
        cur=mysql.connection.cursor()
        cur.execute("select count(*) from user_details")
        result = cur.fetchall()
        userid=result[0][0]+2

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

@app.route('/search')
def search():
    cur=mysql.connection.cursor()
    resultVAlue=cur.execute("SELECT * FROM product_table")
    if resultVAlue>0:
        userDetails=cur.fetchall()
        return render_template('search.html', userDetails=userDetails)

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

@app.route('/sellerSALLTypeProducts')
def sellerSALLTypeProducts():
    cur=mysql.connection.cursor()
    resultVAlue=cur.execute("select DISTINCT(seller_id) from (select seller_id from product_table) AS temp1 where seller_id NOT IN(SELECT seller_id FROM (select* from(select DISTINCT(seller_id)from product_table) AS temp2 cross join (select type_id from type_table) AS temp3)AS temp4 WHERE (seller_id,type_id) NOT IN( select seller_id,type_id from product_table));")
    if resultVAlue>0:
        userDetails=cur.fetchall()
        return render_template('sellerSALLTypeProducts.html', userDetails=userDetails)

@app.route('/AskPandSellPdiff1000')   
def AskPandSellPdiff1000():
    cur=mysql.connection.cursor()
    resultVAlue=cur.execute("select temp1.product_id as ID, temp1.Askprice, temp1.SoldPrice from(select P.product_id,P.price as AskPrice,S.price as SoldPrice from product_table P join sold_product S  on P.product_id = S.product_id where  P.price-S.price<=1000)AS temp1; ")
    if resultVAlue>0:
        userDetails=cur.fetchall()
        return render_template('AskPandSellPdiff1000.html', userDetails=userDetails)

@app.route('/AvgPriOBikeIneveryCities')
def AvgPriOBikeIneveryCities():
    cur=mysql.connection.cursor()
    resultVAlue=cur.execute("select A.city_name,AVG(Price) as AvgPrice, Count(*) as Number from (select product_id,price,city_code from  product_table  where type_id=( select type_id from type_table where name='bike') ) as P join area_table A  on P.city_code=A.area_id Group By A.city_name having  AVG(Price)>1000 Order by A.city_name ")
    if resultVAlue>0:
        userDetails=cur.fetchall()
        return render_template('AvgPriOBikeIneveryCities.html', userDetails=userDetails)

@app.route('/ThoseWhoMEssegedMoreThan1')
def ThoseWhoMEssegedMoreThan1():
    cur=mysql.connection.cursor()
    resultVAlue=cur.execute("select U.user_id, Count(*) as NumberofMsgs from user_details U join chat_table C on U.user_id=C.sender_id Group by  C.sender_id having  Count(distinct receiver_id)>1 order by C.sender_id ")
    if resultVAlue>0:
        userDetails=cur.fetchall()
        return render_template('ThoseWhoMEssegedMoreThan1.html', userDetails=userDetails)

@app.route('/bajajBikeInkarnataka')
def bajajBikeInkarnataka():
    cur=mysql.connection.cursor()
    resultVAlue=cur.execute("select P.product_id,A.city_name as City, P.price as Price, P.seller_id as Seller_id, D.short_description as Description from product_table P join (select area_table.area_id,area_table.city_name from area_table  where area_table.state_name='Karnataka') as A on P.city_code=A.area_id join (select type_table.type_id from type_table where name='bike') as T on T.type_id=P.type_id join (select product_id,short_description from description_table where short_description LIKE 'bajaj%' )as D on D.product_id=P.product_id where NOT EXISTS( 	select product_id     from sold_product     where P.product_id=sold_product.product_id limit 1 ) ")
    if resultVAlue>0:
        userDetails=cur.fetchall()
        return render_template('bajajBikeInkarnataka.html', userDetails=userDetails)

@app.route('/soldAmountAndBoughtAmount')
def soldAmountAndBoughtAmount():
    cur=mysql.connection.cursor()
    resultVAlue=cur.execute("select temp.user_id,temp.Selling_amount,IFNULL(Bought_amount, 0 ) as Bought_amount FROM ( select P.seller_id as user_id, SUM(P.price) as Selling_Amount, SUM(S.price) as Bought_amount from product_table P left join sold_product S on P.product_id=S.product_id Group by  P.seller_id Order by P.seller_id ) as temp ")
    if resultVAlue>0:
        userDetails=cur.fetchall()
        return render_template('soldAmountAndBoughtAmount.html', userDetails=userDetails)

@app.route('/ChatOfUSer9And1ondate')
def ChatOfUSer9And1ondate():
    cur=mysql.connection.cursor()
    resultVAlue=cur.execute("select sender,receiver,chat,time from( select U.customer_name as sender, U1.customer_name as receiver, C.chat, C.time from user_details U join (select sender_id,chat,time,receiver_id,date from chat_table where sender_id=1 and receiver_id=9 and date='2020-05-03') as C on U.user_id = C.sender_id join user_details U1 on U1.user_id = C.receiver_id union all select U.customer_name as sender, U1.customer_name as receiver, C.chat, C.time from user_details U join (select sender_id,chat,time,receiver_id,date from chat_table where sender_id=9 and receiver_id=1 and date='2020-05-03') as C on U.user_id = C.sender_id join user_details U1 on U1.user_id = C.receiver_id ) as Temp Order by Temp.time ")
    if resultVAlue>0:
        userDetails=cur.fetchall()
        return render_template('ChatOfUSer9And1ondate.html', userDetails=userDetails)  

@app.route('/groupingUSerByage')
def groupingUSerByage():
    cur=mysql.connection.cursor()
    resultVAlue=cur.execute("select U.age,count(*) as Number from user_details U group by U.age order by U.age ")
    if resultVAlue>0:
        userDetails=cur.fetchall()
        return render_template('groupingUSerByage.html', userDetails=userDetails)

@app.route('/groupbyMessageSize')
def groupbyMessageSize():
    cur=mysql.connection.cursor()
    resultVAlue=cur.execute("select length(chat),count(*) as length  from chat_table group by length(chat) order by length(chat) ")
    if resultVAlue>0:
        userDetails=cur.fetchall()
        return render_template('groupbyMessageSize.html', userDetails=userDetails)

@app.route('/ThoseWhoAreSellerAndBuyer')
def ThoseWhoAreSellerAndBuyer():
    cur=mysql.connection.cursor()
    resultVAlue=cur.execute("select U.user_id, U.customer_name, U.age from user_details U  where EXISTS( 	select P.seller_id     from product_table P     where U.user_id=P.seller_id limit 1)  and EXISTS(  select S.bought_id  from sold_product S  where S.bought_id=U.user_id limit 1 	) order by user_id ")
    if resultVAlue>0:
        userDetails=cur.fetchall()
        return render_template('ThoseWhoAreSellerAndBuyer.html', userDetails=userDetails)

@app.route('/bike')
def bike():
    cur=mysql.connection.cursor()
    resultVAlue=cur.execute("SELECT * FROM product_table where type_id=1")
    if resultVAlue>0:
        userDetails=cur.fetchall()
        return render_template('bike.html', userDetails=userDetails)

@app.route('/car')
def car():
    cur=mysql.connection.cursor()
    resultVAlue=cur.execute("SELECT * FROM product_table where type_id=2")
    if resultVAlue>0:
        userDetails=cur.fetchall()
        return render_template('bike.html', userDetails=userDetails)

@app.route('/electronics')
def electronics():
    cur=mysql.connection.cursor()
    resultVAlue=cur.execute("SELECT * FROM product_table where type_id=4")
    if resultVAlue>0:
        userDetails=cur.fetchall()
        return render_template('bike.html', userDetails=userDetails)

@app.route('/books')
def books():
    cur=mysql.connection.cursor()
    resultVAlue=cur.execute("SELECT * FROM product_table where type_id=5")
    if resultVAlue>0:
        userDetails=cur.fetchall()
        return render_template('bike.html', userDetails=userDetails)

@app.route('/others')
def others():
    cur=mysql.connection.cursor()
    resultVAlue=cur.execute("SELECT * FROM product_table where type_id=3")
    if resultVAlue>0:
        userDetails=cur.fetchall()
        return render_template('bike.html', userDetails=userDetails)
@app.route('/kolkata')
def kolkata():
    cur=mysql.connection.cursor()
    resultVAlue=cur.execute("SELECT * FROM product_table where type_id=3")
    if resultVAlue>0:
        userDetails=cur.fetchall()
        return render_template('kolkata.html', userDetails=userDetails)

if __name__=='__main__':
    app.run(debug=True)