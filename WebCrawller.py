import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from tkinter import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import smtplib
from email.message import EmailMessage

def search_result():
    path = "C:\Program Files (x86)\chromedriver.exe"
    driver = webdriver.Chrome(path)

    driver.get("https://www.google.com/")
    print (driver.title)

    search_result = driver.find_element_by_name("q")
    search_result.send_keys(entry1.get())
    search_result.send_keys(Keys.RETURN)
    try:
        main = WebDriverWait(driver, 1).until(
            EC.presence_of_element_located((By.ID, "rcnt"))
     )
        print (main.text)
    finally:
        driver.quit()

    time.sleep(1)
    
def search_re():
    path = "C:\Program Files (x86)\chromedriver.exe"
    driver = webdriver.Chrome(path)

    driver.get("https://haveibeenpwned.com/")
    print (driver.title)

    search_re = driver.find_element_by_name("Account")
    search_re.send_keys(entry1.get())
    search_re.send_keys(Keys.RETURN)
    try:
        main = WebDriverWait(driver, 15).until(
            EC.presence_of_element_located((By.ID, "Canva"))
        )
        print (main.text)
    finally:
        driver.quit()

    time.sleep(5)

def search_res():
    path = "C:\Program Files (x86)\chromedriver.exe"
    driver = webdriver.Chrome(path)

    driver.get("https://www.youtube.com/")

    print (driver.title)
    search_res = driver.find_element_by_name("search_query")
    search_res.send_keys(entry1.get)
    search_res.send_keys(Keys.RETURN)
    try:
        main = WebDriverWait(driver, 15).until(
            EC.presence_of_element_located((By.ID, "contents"))
        )
        print (main.text)
    finally:
        driver.quit()

    time.sleep(5)

def search_resu():

    to = input("Type your e-mail:")

    msg = EmailMessage()
    msg['Subject'] = 'Loin - Resultado'
    msg ['From'] = 'defe2431@gmail.com'
    msg ['To'] = to
    msg.set_content('Segue resultado da busca em anexo')

    files = [r'C:\Users\renan\Downloads\ass2.py']
    for file in files:
        with open(file, 'rb') as f:
            file_data = f.read()
            file_name = 'resultado'

        msg.add_attachment(file_data, maintype='application', subtype='octet-stream', filename=file_name)

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:

        smtp.login('defe2431@gmail.com', 'rxdoveqg')


        smtp.send_message(msg)


windows =Tk()
windows.geometry("600x400")
search=Label(windows,text="Qual informação você procura.....", font= 'times 15')
search.place(x=50,y=10)
entry1 = Entry(windows)
entry1.place (x=350,y=10)

b1=Button(windows,text="Google", command=search_result,width=12,bg='gray')
b1.place(x=200,y=150)

b2=Button(windows,text="haveIbeen", command=search_re,width=12,bg='gray')
b2.place(x=200,y=200)

b3=Button(windows,text="youtube", command=search_res,width=12,bg='gray')
b3.place(x=200,y=250)


b4=Button (windows,text="send email", command=search_resu,width=12,bg='gray')
b4.place(x=200,y=300)

windows.mainloop()

'''
Renan Corrêa Sant'anna

'''