import smtplib
import qry

try:
    smtp=smtplib.SMTP('smtp.gmail.com',587)
    smtp.starttls()
    smtp.login("samakshdaksh2106@gmail.com","djoeguaofzengxtv")
    smtp.sendmail("samakshdaksh2106@gmail.com",qry.smail(),"EXAM LINK {}".format(qry.elink()))
    smtp.quit()
    print("Email sent successfully")
    
except Exception as err:
    print("Something went wrong...",err)

