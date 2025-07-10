from errno import errorcode
import tkinter as tk
from tokenize import Name
import mysql.connector as connector
from tkinter import *

def entry():
    global Registration_number
    global Name
    global Email_Address
    global Phone
    global Password

    Registration_number=Registration_number.get()
    Name=Name.get()
    Email_Address=Email_Address.get()
    Phone=Phone.get()
    Password=Password.get()

    try:
        conn = connector.connect(  host="localhost",
        user="root",
        password="1234",
        database="online_exams"
        )
        cursor=conn.cursor()
        qry=("INSERT INTO Student VALUES (%s, %s, %s, %s, %s)")
        data = (Registration_number, Name, Email_Address, Phone, Password)
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
lblfrstrow = tk.Label(root, text ="Registration Number", )
lblfrstrow.place(x = 50, y = 20)
Registration_number = tk.Entry(root, width = 35)
Registration_number.place(x = 250, y = 20, width = 100)
  
lblsecrow = tk.Label(root, text ="Name ")
lblsecrow.place(x = 50, y = 40)
Name = tk.Entry(root, width = 35)
Name.place(x = 250, y = 40, width = 100)

lblfrstrow = tk.Label(root, text ="Email Address", )
lblfrstrow.place(x = 50, y = 60)
Email_Address = tk.Entry(root, width = 35)
Email_Address.place(x = 250, y = 60, width = 100)

lblfrstrow = tk.Label(root, text ="Phone Number", )
lblfrstrow.place(x = 50, y = 80)
Phone = tk.Entry(root, width = 35)
Phone.place(x = 250, y = 80, width = 100)

lblfrstrow = tk.Label(root, text ="Password", )
lblfrstrow.place(x = 50, y = 100)
Password = tk.Entry(root, width = 35)
Password.place(x = 250, y = 100, width = 100)
 

submitbtn = tk.Button(root, text ="Save",
                      bg ='blue', command = entry)
submitbtn.place(x = 150, y = 135, width = 55)

exit_button = Button(root, text="Exit",
                      bg='blue', command=close)
exit_button.place(x=150,y=165, width=35)
root.mainloop()
