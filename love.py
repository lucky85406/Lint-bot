import csv

def love(uid,text):
	keyin = text.split(":")
	with open('mylove.csv','a',newline='')as cfile:
			fieldn = ['ID','love']

			writer = csv.DictWriter(cfile,fieldnames=fieldn)

			writer.writerow({'ID':uid,'love':keyin[1]})
	with open('mylove.csv',newline='')as csvfile:
		rows = csv.DictReader(csvfile)
		for row in rows:
			if row['ID'] == "Chen William":
				print(row['ID']+":"+row['love'])
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
	a = []
	c = []	
	e = []	
	f = []
	g = []
	d=0

	with open('mylove.csv',newline='')as csvfile:
		rows = csv.DictReader(csvfile)
		print(type(rows))
		for row in rows:
			c.append(row['ID'])
			e.append(row['love'])



	for x in range(0,len(c)):
		if c[x] == uid:
			a.append(c[x])
			f.append(e[x])
		else:
			g.append(e[x])		

	a.remove(uid)
	f.remove(text)
	for x in c:
		if x == uid:
			c.remove(uid)

	c.extend(a)
	g.extend(f)

	with open('mylove.csv','w',newline='')as cfile:
			fieldn = ['ID','love']

			writer = csv.DictWriter(cfile,fieldnames=fieldn)

			writer.writeheader()
			for x in range(0,len(c)):
				if c[x] is None and g[x] is None:
					writer.writerow({'ID':c[x],'love':g[x]})
	with open('mylove.csv',newline='')as csvfile:
		rows = csv.DictReader(csvfile)
		
		for row in rows:
			if uid == row['ID']:
				mes.add(row['love'])
	return mes
