import requests
import pandas as pd
import csv
def selectcoin():
    coinname = input("코인을 입력하세요")
    price = pd.read_csv('./price/20191205-17.csv')
    file=open('./coinlist.txt','r')
    lines=file.readlines()
    file.close()
    coins=lines[0].split(',') 
    b=0
    i=0
    print(len(coins))
    for i in range(0,len(coins)):
        if coinname == coins[i]:
            b = i
        i = i+1

    selectedcoin = price.loc[b]
    selectedcoin.to_csv('./selectedprice/selectedcoin.csv',mode='w')	

    print(selectedcoin)
    
selectcoin()
