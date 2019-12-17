import pandas as pd
import os
import csv
import glob

file_list = glob.glob('./price/*.csv')
price = pd.read_csv('./price.csv')
price2 = pd.read_csv('./price.csv')
i=0
for item in file_list:
    print(item[8:-4])
    filedate=item[8:-4] #20191213-11
    day=filedate[6:8]
    hour=item[-6:-4]
    print(item[8:-7])
    # print(day+"Day")
    # print(hour+"hour")
	# date = 20191207

    item=str(item.replace("\\","/"))
    print(str(item))
	# name=item[4:-4] #1_20191205-222700
    data = pd.read_csv(item)
	# data = data[['name','KOR']].rename(columns={'name':'name','KOR':name})
    if file_list[i-1][8:-7] == file_list[i][8:-7] :
       price = pd.merge(price,data, on="name")
    else:
       price = pd.merge(price2,data, on="name")
    filename='./priceperday/'+item[8:-7]+'.csv'
    price.to_csv(filename,mode='w')	
    i=i+1
