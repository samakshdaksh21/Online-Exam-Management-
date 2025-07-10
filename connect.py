import mysql.connector as connector
from urllib import request
from flask import Flask 
from flaskext.mysql import MySQL 
mysql = MySQL() 
app=Flask(__name__) 
app.config['MYSQL_DATABASE_USER'] ="root" 
app.config['MYSQL_DATABASE_PASSWORD'] = "1234"
app.config['MYSQL_DATABASE_DB'] ="online_exams" 
app.config['MYSQL_DATABASE_HOST'] = "localhost" 
mysql.init_app(app) 
conn=mysql.connect() 
cursor=conn.cursor() 
@app.route('/register',methods=['POST']) 
def register(): 
    registration_number=request.form['reg-num']
    name=request.form['full-name']
    email=request.form['email']
    number=request.form['number']
    pas=request.form['password']
    cursor.execute("insert into student values (%s,%s,%s,%s,%s)",(registration_number,name,email,number,pas)) 
    conn.commit() 
    return "successfully registered"