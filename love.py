import csv

def love(uid,text):
	keyin = text.split(":")
	c = False
	with open('mylove.csv',newline='')as cfile:
		rows = csv.DictReader(cfile)
		for row in rows:
			if row['ID'] == uid and row['love'] == keyin[1]:
				c = True
				break
	if c:
		return c
	else:
		with open('mylove.csv','a',newline='')as cfile:
				fieldn = ['ID','love']

				writer = csv.DictWriter(cfile,fieldnames=fieldn)

				writer.writerow({'ID':uid,'love':keyin[1]})
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
	print("uname:",uid)
	print("text:",text)
	n = 0
	mes = set()
	c = []
	e = []
	a = []
	f = []
	g = []

	if text != 'x':
		with open('mylove.csv',newline='')as csvfile:
			rows = csv.DictReader(csvfile)
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
		n = c.count(uid)
		for y in range(1,n):
			c.remove(uid)
		c.extend(a)
		g.extend(f)
		with open('mylove.csv','w',newline='')as cfile:
				fieldn = ['ID','love']

				writer = csv.DictWriter(cfile,fieldnames=fieldn)

				writer.writeheader()
				for x in range(0,len(c)-1):
					writer.writerow({'ID':c[x],'love':g[x]})
		with open('mylove.csv',newline='')as csvfile:
			rows = csv.DictReader(csvfile)

			for row in rows:
				if uid == row['ID']:
					mes.add(row['love'])
		return mes
