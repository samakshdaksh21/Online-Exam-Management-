import mysql.connector as connector
from mysql.connector import errorcode
from datetime import date, datetime, timedelta
from mysql.connector import(connection)
import os
import platform
from turtle import clearscreen


def DeleteSubject():
  try:
    conn= connector.connect(  host="localhost",
    user="root",
    password="1234",
    database="online_exams"
    )
    cursor = conn.cursor()
    Subject_ID = input("Enter Subject_ID to be deleted : ")
    Qry =("""DELETE FROM Subject WHERE Subject_ID = %s""")
    del_rec = (Subject_ID,)
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


def SearchSubject():
  try:
    conn= connector.connect(  host="localhost",
    user="root",
    password="1234",
    database="online_exams"
    )
    cursor = conn.cursor()
    Subject_ID = input("Enter Subject_ID to be Searched : ")
    query = ("SELECT * FROM Subject where Subject_ID = %s")
    rec_srch = (Subject_ID,)
    cursor.execute(query, rec_srch)
    Rec_count = 0
    for(Subject_ID,Subject_name, Credits,Teacher) in cursor:
      Rec_count += 1
      print("=============================================================")
      print("Subject_ID : ", Subject_ID)
      print("Subject_name : ", Subject_name)
      print("Credits : ", Credits)
      print("Teacher : ", Teacher)
      print("=============================================================")
    if Rec_count%2 == 0:
      input("Press any key to continue: ")
      clearscreen()
    print(Rec_count, "Record(s) found")
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


def UpdateSubject():
  try:
    conn= connector.connect(  host="localhost",
    user="root",
    password="1234",
    database="online_exams"
    )
    cursor = conn.cursor()
    Subject_ID = input("Enter Subject_ID of Subject to be Updated : ")
    print("Enter new data")
    New_Subject_ID  = input("Enter Subject_ID  : ")
    Subject_name = input("Enter Subject Name : ")
    Credits = int(input("Enter Credits : "))
    Teacher = input("Enter Teacher Name : ")
    Qry = ("UPDATE Subject SET Subject_ID=%s, Subject_name=%s, Credits=%s, Teacher=%s WHERE Subject_ID=%s")
    data = (New_Subject_ID,Subject_name, Credits,Teacher, Subject_ID)
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