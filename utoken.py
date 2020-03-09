import csv
import random
import json

def go(url):

	c = []
	d = []

	with open('user.csv',newline='') as csvfile:
		rows = csv.DictReader(csvfile)
		for row in rows:
			c.append(row)

	if len(c):
		for x in c:
			if x['ID'] == url:
				d.append(x)
		for x in d:
			c.remove(x)
		with open('user.csv','w',newline='')as cfile:
			fieldn = ['ID','D1','D2','D3','D4','D5']

			writer = csv.DictWriter(cfile,fieldnames=fieldn)

			writer.writeheader()
			for x in c:
				writer.writerow({'ID':x['ID'],'D1':x['D1'],'D2':x['D2'],'D3':x['D3'],'D4':x['D4'],'D5':x['D5']})
			writer.writerow({'ID':url,'D1':"",'D2':"",'D3':"",'D4':"",'D5':""})
	else:
		with open('user.csv','w',newline='')as cfile:
			fieldn = ['ID','D1','D2','D3','D4','D5']

			writer = csv.DictWriter(cfile,fieldnames=fieldn)

			writer.writeheader()

			writer.writerow({'ID':url,'D1':"",'D2':"",'D3':"",'D4':"",'D5':""})

def level(x):
	l1 = ["a","b","c","d"]
	l2 = ["e","f","g","h","i","j","k"]
	l3 = ["l","m","n","o","p"]
	l4 = ["q","r","s"]
	l5 = ["t","u","v"]

	lev = "0"

	for x in l1:
		lev = "1"
	for x in l2:
		lev = "2"
	for x in l3:
		lev = "3"
	for x in l4:
		lev ="4"
	for x in l5:
		lev = "5"
	return lev

def inMes(url,x):
	con = url
	Dlist = [""]*5
	lev = level(x)
	a = 0
	with open('user.csv',newline='') as csvfile:
		rows = csv.DictReader(csvfile)
		for row in rows:
			print(a)
			a =a+1
			if row['ID'] == url and lev == "1":
				Dlist[0] = x
				Dlist[1] = row['D2']
				Dlist[2] = row['D3']
				Dlist[3] = row['D4']
				Dlist[4] = row['D5']
				lev = ""
			elif row['ID'] == url and lev == "2":
				Dlist[0] = row['D1']
				Dlist[1] = x
				Dlist[2] = row['D3']
				Dlist[3] = row['D4']
				Dlist[4] = row['D5']
				lev = ""
			elif row['ID'] == url and lev == "3":
				Dlist[0] = row['D1']
				Dlist[1] = row['D2']
				Dlist[2] = x
				Dlist[3] = row['D4']
				Dlist[4] = row['D5']
				lev = ""
			elif row['ID'] == url and lev == "4":
				Dlist[0] = row['D1']
				Dlist[1] = row['D2']
				Dlist[2] = row['D3']
				Dlist[3] = x
				Dlist[4] = row['D5']
				lev = ""
			elif row['ID'] == url and lev == "5":
				Dlist[0] = row['D1']
				Dlist[1] = row['D2']
				Dlist[2] = row['D3']
				Dlist[3] = row['D4']
				Dlist[4] = x
				lev = ""

	with open('user.csv','a',newline='')as cfile:
			fieldn = ['ID','D1','D2','D3','D4','D5']

			writer = csv.DictWriter(cfile,fieldnames=fieldn)
			print(con)
			print("------")
			print(Dlist)
			writer.writerow({'ID':url,'D1':Dlist[0],'D2':Dlist[1],'D3':Dlist[2],'D4':Dlist[3],'D5':Dlist[4]})

def showMes(url):
	a = "1"
	with open('user.csv',newline='') as csvfile:
		rows = csv.DictReader(csvfile)
		for row in rows:
			if row['ID'] == url:
				return "{}{}{}{}{}".format(row['D1'],row['D2'],row['D3'],row['D4'],row['D5'])
	return a
