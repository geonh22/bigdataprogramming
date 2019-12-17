import pandas as pd
import os
import csv
import glob

file_list = glob.glob('./priceperday/*.csv')
price = pd.read_csv('./price.csv')
price2 = pd.read_csv('./price.csv')
i=0
for item in file_list:
    print(item)
    print(item[:-3])
    print(item[14:-6])

    item=str(item.replace("\\","/"))
    print(str(item))
	# name=item[4:-4] #1_20191205-222700
    data = pd.read_csv(item)
	# data = data[['name','KOR']].rename(columns={'name':'name','KOR':name})
    # if file_list[i-1][8:-7] == file_list[i][8:-7] :
    price = pd.merge(price,data, on="name")
    # else:
    #    price = pd.merge(price2,data, on="name")
    filename='./'+item[14:-6]+'.csv'
    price.to_csv(filename,mode='w')	
    i=i+1
