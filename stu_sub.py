import mysql.connector as connector
from mysql.connector import errorcode

def sub():
 try:
    conn = connector.connect(  host="localhost",
    user="root",
    password="1234",
    database="online_exams"
    )
    cursor=conn.cursor()
    Registration_number = input("Enter Registration_number : ")
    Subject_ID  = input("Enter Subject_ID  : ")
    Qry = ("INSERT INTO STU_SUB VALUES(%s,%s)")
    data=(Registration_number,Subject_ID)
    cursor.execute(Qry,data)
    conn.commit()
    cursor.close()
 except connector.ERROR as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Something is wrong with your user name or password")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("Database does not exist")
    else:
        print(err)
    conn.rollback()
 conn.close()

sub()