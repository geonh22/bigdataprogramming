import pandas as pd
import os
import csv
import glob

file_list = glob.glob('./1/*.csv')
price = pd.read_csv('./price.csv')
price2 = pd.read_csv('./price.csv')
i=0
for item in file_list:
	filedate = item[6:14] #20191205
	day = filedate[-2:]
	hour = item[15:17]
	date = 20191207

	item=str(item.replace("\\","/"))
	print(str(item))
	name=item[4:-4] #1_20191205-222700
	data = pd.read_csv(item,names=['name', 'USD','KOR'])
	data = data[['name','KOR']].rename(columns={'name':'name','KOR':name})
	if file_list[i-1][15:17] == file_list[i][15:17] :
		price = pd.merge(price,data, on="name")
	else:
		price = pd.merge(price2,data, on="name")
	filename='./price/'+filedate+'-'+str(hour)+'.csv'
	price.to_csv(filename,mode='w')	
	i=i+1
