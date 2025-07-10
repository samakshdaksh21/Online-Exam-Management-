import mysql.connector as connector


def DatabaseCreate():
  conn = connector.connect(
  host="localhost",
  user="root",
  password="1234"
  )

  cursor = conn.cursor()
  cursor.execute("CREATE DATABASE online_exams")
  cursor.close()
  conn.close()

def connection():
  conn = connector.connect(  host="localhost",
  user="root",
  password="1234",
  database="online_exams"
  )
  cursor = conn.cursor()
  cursor.execute("SELECT DATABASE()")
  data = cursor.fetchone()
  print("Connection established to: ",data)
  conn.close()


def TablesCreate():
  conn = connector.connect(
  host="localhost",
  user="root",
  password="1234",
  database="online_exams"
  )
  cursor = conn.cursor()
  cursor.execute("CREATE TABLE STUDENT(Registration_number varchar(10) PRIMARY KEY,Name text(40), Email_Address varchar(40),  Phone varchar(10), Password varchar(20))")
  cursor.execute("CREATE TABLE SUBJECT(Subject_ID varchar(10) PRIMARY KEY, Subject_name text(20), Credits int(2), Teacher text(40))")
  cursor.execute("CREATE TABLE EXAM(Exam_ID varchar(10) PRIMARY KEY, Subject_ID varchar(10),Exam_Date varchar(20), Exam_Link varchar(200))")
  cursor.execute("CREATE TABLE STU_SUB(Registration_number varchar(10),Subject_ID varchar(10) )")
  cursor.close()
  conn.close()