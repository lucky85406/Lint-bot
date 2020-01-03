import csv
import random

Lcode = ['L1','L2','L3','L4','L5','L6','L7','L8','L9','L10','L11','L12','L13','L14','L15','L16','L17','L18']
def dataList(intxt):
	set1 = {}
	set2 = set()
	set3 = {}
	s = intxt
	with open('cosurl.csv',newline='')as csvfile:
		rows = csv.DictReader(csvfile)
		for row in rows:
			for x in range(0,18):
				if row[Lcode[x]] == s:
					set1[row['url']] = row['酒類']
	a = len(set1)
	if a >=10:
		set2 = random.sample(list(set1),10)
		for x in set2:
			set3[x] = set1[x]
	else:
		return set1	

	return set3

