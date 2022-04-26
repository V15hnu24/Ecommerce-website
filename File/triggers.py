import mysql.connector
mydb=mysql.connector.connect(host="localhost",user="root",passwd="7061" ,database = "olx_final")


def Seetriggers():
    mycursor = mydb.cursor()
    query="show triggers;"
    mycursor.execute(query)
    myresult = mycursor.fetchall()
    print('Views are as follow:')
    for x in myresult:
        print(x)
    print()
Seetriggers()