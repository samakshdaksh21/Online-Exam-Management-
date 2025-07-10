from errno import errorcode
import tkinter as tk
from tokenize import Name
import mysql.connector as connector
from tkinter import *

def entry():
    global Exam_ID
    global Subject_ID
    global Exam_Date
    global Exam_Link

    Exam_ID=Exam_ID.get()
    Subject_ID=Subject_ID.get()
    Exam_Date=Exam_Date.get()
    Exam_Link=Exam_Link.get()

    try:
        conn = connector.connect(  host="localhost",
        user="root",
        password="1234",
        database="online_exams"
        )
        cursor=conn.cursor()
        qry=("INSERT INTO exam VALUES (%s, %s, %s, %s)")
        data = (Exam_ID,Subject_ID,Exam_Date,Exam_Link)
        cursor.execute(qry,data)
        conn.commit()
        cursor.close()
        print("Entry Successfull")
    
    except connector.ERROR as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(err)
        conn.rollback()
    conn.close()

def close():
    root.destroy()

root = tk.Tk()
root.geometry("400x300")
root.title("Student Details")
  
 
# Defining the first row
lblsecrow = tk.Label(root, text ="EXAM  ID ")
lblsecrow.place(x = 50, y = 20)
Exam_ID= tk.Entry(root, width = 35)
Exam_ID.place(x = 250, y = 20, width = 100)

lblfrstrow = tk.Label(root, text ="SUBJECT  ID", )
lblfrstrow.place(x = 50, y = 40)
Subject_ID = tk.Entry(root, width = 35)
Subject_ID.place(x = 250, y = 40, width = 100)
  
lblfrstrow = tk.Label(root, text ="EXAM  DATE", )
lblfrstrow.place(x = 50, y = 60)
Exam_Date = tk.Entry(root, width = 35)
Exam_Date.place(x = 250, y = 60, width = 100)

lblfrstrow = tk.Label(root, text ="EXAM  LINK", )
lblfrstrow.place(x = 50, y = 80)
Exam_Link = tk.Entry(root, width = 35)
Exam_Link.place(x = 250, y = 80, width = 100)

 

submitbtn = tk.Button(root, text ="Save",
                      bg ='blue', command = entry)
submitbtn.place(x = 150, y = 135, width = 55)

exit_button = Button(root, text="Exit",
                      bg='blue', command=close)
exit_button.place(x=150,y=165, width=35)
root.mainloop()
