import mysql.connector as connector

def elink():
  conn=connector.connect(host="localhost",user="root",password="1234",database="online_exams")
  cursor=conn.cursor(buffered=True)
  Subject_ID=input("Enter Subject ID : ")
  Exam_Date=input("Enter Exam Date : ")
  query=("SELECT Exam_Link FROM exam WHERE Subject_ID=%s AND Exam_Date=%s")
  data=(Subject_ID,Exam_Date)
  cursor.execute(query,data)
  b=cursor.fetchall()
  conn.commit()
  cursor.close()
  conn.close()
  return b[0][0]



def smail():
  conn=connector.connect(host="localhost",user="root",password="1234",database="online_exams")
  cursor=conn.cursor()
  Subject_ID=input("Enter Subject ID : ")
  qry=("SELECT student.Email_Address FROM student INNER JOIN stu_sub ON student.Registration_number=stu_sub.Registration_number WHERE Subject_ID=%s ")
  data=(Subject_ID)
  cursor.execute(qry,(data,))
  a=cursor.fetchall()
  conn.commit()
  cursor.close()
  conn.close()
  return[a[i] for i in range(len(a))]


