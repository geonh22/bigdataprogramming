import requests
import pandas as pd
import csv
import time
import threading

def getapi1():
    timestr = time.strftime("%Y%m%d-%H%M%S")
    print(timestr)
    filename='./1/1_'+timestr+'.csv'

    file=open('./coinlist.txt','r')
    lines=file.readlines()
    file.close()
    coins=lines[0].split(',') 
    payload_coin=str(coins).replace("'","").replace(" ","")
    payload_coin1=payload_coin[1:297]

    apiKey = "d1f3b83ef8ee58c09c5e7640f3e271c633c8a12489e880a9691ab0324d639bed"

    url = "https://min-api.cryptocompare.com/data/pricemulti"

    payload = {
        "fsyms": {payload_coin1},
        "tsyms": {"USD","KRW"}
    }

    headers = {
        "authorization": "Apikey " + apiKey
    }

    result1 = requests.get(url, headers=headers, params=payload).json()
    csv_file = open(filename,'w', encoding='utf-8')

    for c in coins[:67]:

        money = result1[c]
        KRW = money["KRW"]
        USD = money["USD"]
        price_list=[c,KRW,USD]
        writer = csv.writer(csv_file)
        writer.writerow(price_list)

    csv_file.close

    threading.Timer(2,getapi1).start()

getapi1()
