import smtplib
import datetime as dt
from random import randint
cur_dt=dt.datetime.now()
with open("quotes.txt", "r") as f:
    quotes = f.readlines()
    quote = quotes[randint(0, 102)]
#emails=["aroradivyam3@gmail.com","piya051714@gmail.com","aileenvarghese02@gmail.com","vanshita993@gmail.com","akshayskumar23@gmail.com","annemaryfrancis25@gmail.com"]
emails=["refuel2006@yahoo.co.in"]
#emails=[
if cur_dt.weekday() in [0,1,2,3,4]:
    for email in emails:
        my_email="divyamautomated@gmail.com"
        password="" #add password
        connection=smtplib.SMTP("smtp.gmail.com",port=587)
        connection.starttls()
        connection.login(user=my_email,password=password)
        connection.sendmail(from_addr=my_email,to_addrs=email,msg=f"subject: Daily Motivation\n\n{quote}\n\nYour Best friend\n\nDivyam")
        connection.close()
