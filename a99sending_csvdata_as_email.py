#go over this after going over email module as error in email client ?
#the by syntac has changed from when wathching lectures so its a bit different now .
import csv
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import  encoders
from datetime import *
import time as t

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(5)
driver.get("https://alnafi.com/courses/python")
driver.maximize_window()
t.sleep(5)

driver.execute_script("window.open('https://alnafi.com/courses/sysops','new window')")
wins = driver.window_handles
t.sleep(5)

course=[]
fees = []

driver.switch_to.window(wins[0])
course_name=driver.find_element(by=By.XPATH, value='//*[@id="__nuxt"]/div/div[4]/div[1]/section[1]/div[1]/div/aside[1]/div/h1').text
course_fees= driver.find_element(by=By.XPATH, value='//*[@id="__nuxt"]/div/div[4]/div[1]/section[1]/div[1]/div/aside[2]/section/div[1]/div[2]/div[3]/span').text
course.append(course_name)
fees.append(course_fees)

driver.switch_to.window(wins[1])
t.sleep(8)
course_name=driver.find_element(by=By.XPATH, value='//*[@id="__nuxt"]/div/div[4]/div[1]/section[1]/div[1]/div/aside[1]/div/h1').text
course_fees= driver.find_element(by=By.XPATH, value='//*[@id="__nuxt"]/div/div[4]/div[1]/section[1]/div[1]/div/aside[2]/section/div[1]/div[2]/div[3]/span').text
course.append(course_name)
fees.append(course_fees)
print(course)
print(fees)

data = list(zip(course,fees))
print(data)
file = open('a9datatable_covert.csv','w',newline='')
writer = csv.writer(file)
writer.writerows(data)
file.close()

t.sleep(5)
driver.quit()


day=date.today()
time1=datetime.now()

my_custom=day.strftime("%B %d %Y")
current_time=time1.strftime("%I:%M:%S %p")

filename=r"C:\Users\Dell\PycharmProjects\pythonProject\.cPythSELProj\a9datatable_covert.csv"

msg=MIMEMultipart()

my_mail="shxnzxy@gmail.com"
password="hnooadlxbzuktmxl"
msg['Subject']= f"Alnafi Course fees details :  {my_custom} {current_time}"
msg['From']= my_mail
msg['To'] = my_mail
msg['Cc'] = 'datamas@hotmail.com'


body="""
<html><p> pyth automation testing ,<br>does it work   <br><br><br>Shanzay Khan 
"""
msg.attach(MIMEText(body,'html'))


#ATTACHMENT section
attachment=open(filename,'rb')
part = MIMEBase('application','octet-stream')
part.set_payload((attachment).read())
encoders.encode_base64(part)
part.add_header('Content-Disposition',"attachment; filename=%s" % filename)
msg.attach(part)

connection=smtplib.SMTP('smtp.gmail.com')
connection.starttls()       #TLS transport layer security


connection.login(user=my_mail,password=password)
connection.send_message(msg)
connection.close()