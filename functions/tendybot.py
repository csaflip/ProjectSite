import ssl
import time
import smtplib
from datetime import date
import random
import requests
import json
from bs4 import BeautifulSoup

def load_config(config_file_path):
    data = {}
    with open(config_file_path, "r") as file:
        data=json.load(file)
    return data

def send_message():

    data = load_config('static/config.json')
    port = data['port']
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", port=port, context=context) as loggerserver:
        loggerserver.login(data['email'], data['pass'])
        time.sleep(1)
        print("YEET")
        loggerserver.sendmail(data['email'], data['phonenum'], 'Chicken Tender subs are on SALE MOTHERFUCKER!!!!')
        time.sleep(1)


        
def check_tendy():
    r = requests.get('http://arepublixchickentendersubsonsale.com/')
    soup = BeautifulSoup(r.text, features='html5lib')

    tender_question= soup.find(text='YES THEY ARE!')

    print(tender_question)

    if tender_question != None:
        send_message()
        return 'Chicken tender subs are on sale!!!'
    else:
        return 'No tender subs on sale rn :('
