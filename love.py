import csv

def love(uid,text):
	keyin = text.split(":")
	c = False
	with open('mylove.csv',newline='')as cfile:
		rows = csv.DictReader(cfile)
		for row in rows:
			if row['ID'] == uid and row['love'] == keyin[1]:
				c = True
				return c
	return c
def love2(uid):
	set1 = set()
	with open('mylove.csv',newline='')as csvfile:
		rows = csv.DictReader(csvfile)
		for row in rows:
			if row['ID'] == uid:
				set1.add(row['love'])
	return set1

def relove(uid,text):
	mes = set()
	a = list()
	if text != 'x':
		with open('mylove.csv',newline='')as csvfile:
			rows = csv.DictReader(csvfile)
			for row in rows:
				if len(row):
					a.append([row['time'],row['ID'],row['love']])
	for x in a:
		if x[1] == uid and x[2] == text:
			a.remove(x)
	with open('mylove.csv','w',newline='')as cfile:
			fieldn = ['time','ID','love']

			writer = csv.DictWriter(cfile,fieldnames=fieldn)

			writer.writeheader()
			for y in a:
				writer.writerow({'time':y[0],'ID':y[1],'love':y[2]})
	with open('mylove.csv',newline='')as csvfile:
		rows = csv.DictReader(csvfile)
		for row in rows:
			if uid == row['ID']:
				mes.add(row['love'])
	return mes
