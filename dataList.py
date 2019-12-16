import csv
import random
Lcode = ['L1','L2','L3','L4','L5','L6','L7','L8','L9','L10','L11','L12','L13','L14','L15','L16','L17','L18']
a=0
set1 = set()
def dataList(intxt):
	with open('cosurl.csv',newline='',encoding='gbk')as csvfile:
		rows = csv.DictReader(csvfile)
		for row in rows:
			for x in range(0,18):
				if row[Lcode[x]] == intxt:
					set1.add(row['url'])
	set1 = random.sample(set1,10)
	return set1