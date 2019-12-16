import csv
import random
Lcode = ['L1','L2','L3','L4','L5','L6','L7','L8','L9','L10','L11','L12','L13','L14','L15','L16','L17','L18']
pngurl="https://stickersofast.com/images/transparent_500.jpg?3"
def dataList(intxt):
	set1 = set()
	set2 = set()
	s = intxt
	with open('cosurl.csv',newline='')as csvfile:
		rows = csv.DictReader(csvfile)
		for row in rows:
			for x in range(0,18):
				if row[Lcode[x]] == s:
					set1.add(row['url'])
	a = len(set1)
	if a >=10:
		set2 = random.sample(set1,10)
	else:
		li = list(set2)
		for x in range(0,10):
			if li[x] == "":
				li[x] = pngurl
		set2 = set(li)		

	return set2