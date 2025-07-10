import mysql.connector as connector
from mysql.connector import errorcode
from mysql.connector import(connection)
import os
import platform

if platform.system() == "Windows":
 print(os.system("cls"))



def DeleteStudent():
    try:
     conn = connector.connect(  host="localhost",
     user="root",
     password="1234",
     database="online_exams"
     )
     cursor=conn.cursor()
     Registration_number = input("Enter Registration_number of Student to be deleted : ")
     Qry = ("""DELETE FROM Student WHERE Registration_number = %s""")
     del_rec = (Registration_number,)
     cursor.execute(Qry, del_rec)
     conn.commit()
     cursor.close()
     print(cursor.rowcount, "Record(s) Deleted Successfully.")
    except connector.ERROR as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(err)
        conn.rollback()
    conn.close()



def SearchStudentRec():
    try:
     conn = connector.connect(  host="localhost",
     user="root",
     password="1234",
     database="online_exams"
     )
     cursor=conn.cursor()
     Registration_number = input("Enter Registration_number of Student to be searched : ")
     query = ("SELECT * FROM Student WHERE Registration_number = %s ")
     rec_srch = (Registration_number,)
     cursor.execute(query, rec_srch)
     Rec_count = 0
     for(Registration_number, Name, Email_Address, Phone, Password) in cursor:
         Rec_count += 1
         print("=============================================================")
         print("Registration_number : ", Registration_number)
         print("Name : ", Name)
         print("Email_Address : ", Email_Address)
         print("Phone : ", Phone)
         print("Password :", Password)
         print("=============================================================")
         if Rec_count%2 == 0:
            input("Press any key continue")
            print(Rec_count, "Record(s) found")
     conn.commit()
     cursor.close()
    except:
        print("NOT FOUND")
        conn.rollback()
    conn.close()


def UpdateStudent():
    try:
     conn = connector.connect(  host="localhost",
     user="root",
     password="1234",
     database="online_exams"
     )
     cursor=conn.cursor()
     Registration_number = input("Enter Registration_number of the Student to be Updated : ")
     print("Enter new data")
     NewRegistration_number = input("Enter Registration_number :")
     Name = input("Name : ") 
     Email_Address = input("Enter Email_Address : ")
     Phone = input("Enter Phone_Number : ")
     Password = input("Enter Password : ")
     Qry = ("UPDATE Student SET NewRegistration_number=%s, Name=%s, Email_Address=%s, Phone=%s, Password=%s WHERE Registration_number  = %s")
     data = (NewRegistration_number, Name, Email_Address, Phone, Password, Registration_number)
     cursor.execute(Qry,data)
     conn.commit()
     cursor.close()
     print(cursor.rowcount, "Record(s) Updated Successfully.")
    
    except connector.ERROR as err:
     if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
         print("Something is wrong with your user name or password")
     elif err.errno == errorcode.ER_BAD_DB_ERROR:
         print("Database does not exist")
     else:
         print(err)
 
     conn.rollback()
    conn.close()