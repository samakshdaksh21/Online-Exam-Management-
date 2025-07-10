from errno import errorcode
import tkinter as tk
from tokenize import Name
import mysql.connector as connector
from tkinter import *

def entry():
    global Subject_ID
    global Subject_name
    global Credits
    global Teacher

    Subject_ID=Subject_ID.get()
    Subject_name=Subject_name.get()
    Credits=Credits.get()
    Teacher=Teacher.get()

    try:
        conn = connector.connect(  host="localhost",
        user="root",
        password="1234",
        database="online_exams"
        )
        cursor=conn.cursor()
        qry=("INSERT INTO subject VALUES (%s, %s, %s, %s)")
        data = (Subject_ID, Subject_name, Credits, Teacher)
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
lblfrstrow = tk.Label(root, text ="SUBJECT ID", )
lblfrstrow.place(x = 50, y = 20)
Subject_ID = tk.Entry(root, width = 35)
Subject_ID.place(x = 250, y = 20, width = 100)
  
lblsecrow = tk.Label(root, text ="SUBJECT NAME ")
lblsecrow.place(x = 50, y = 40)
Subject_name = tk.Entry(root, width = 35)
Subject_name.place(x = 250, y = 40, width = 100)

lblfrstrow = tk.Label(root, text ="CREDITS", )
lblfrstrow.place(x = 50, y = 60)
Credits = tk.Entry(root, width = 35)
Credits.place(x = 250, y = 60, width = 100)

lblfrstrow = tk.Label(root, text ="TEACHER NAME", )
lblfrstrow.place(x = 50, y = 80)
Teacher = tk.Entry(root, width = 35)
Teacher.place(x = 250, y = 80, width = 100)

 

submitbtn = tk.Button(root, text ="Save",
                      bg ='blue', command = entry)
submitbtn.place(x = 150, y = 135, width = 55)

exit_button = Button(root, text="Exit",
                      bg='blue', command=close)
exit_button.place(x=150,y=165, width=35)
root.mainloop()
