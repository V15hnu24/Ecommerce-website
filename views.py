import mysql.connector
mydb=mysql.connector.connect(host="localhost",user="root",passwd="7061" ,database = "olx_final")


def SeeViews():
    mycursor = mydb.cursor()
    query="SHOW FULL TABLES IN olx_final WHERE TABLE_TYPE LIKE 'VIEW';"
    mycursor.execute(query)
    myresult = mycursor.fetchall()
    print('Views are as follow:')
    for x in myresult:
        print(x)
    print()
SeeViews()