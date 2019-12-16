import csv
import random
Lcode = ['L1','L2','L3','L4','L5','L6','L7','L8','L9','L10','L11','L12','L13','L14','L15','L16','L17','L18']
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
		return set1	

	return set2
def dataOpen(intxt):
	testxt=""
	with open('usertxt.txt','r') as f:
		testxt = f.read()
	with open('usertxt.txt','w') as f:
		f.write(testxt+intxt)
	with open('usertxt.txt','r') as f:
		testxt = f.read()
	if intxt == "測試":
		return testxt
	elif intxt == "返回":
		with open('usertxt.txt','w') as f:
			f.write("")
	