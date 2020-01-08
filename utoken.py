import csv
import random
import json

def go(url):
	c = []
	d = []
	with open('user.csv',newline='')as csvfile:
		rows = csv.DictReader(csvfile)
		for row in rows:
			if row['Ver'] == '5':
				c.append(row['ID']+'-'+row['D1']+'-'+row['D2']+'-'+row['D3']+'-'+row['D4']+'-'+row['D5']+'-'+row['Ver'])
			else:
				d.append(row['ID']+'-'+row['D1']+'-'+row['D2']+'-'+row['D3']+'-'+row['D4']+'-'+row['D5']+'-'+row['Ver'])

	for x in c:
		if x.split('-')[6] == '5':
			c.remove(x)
	if c:
	else:
		with open('user.csv','w',newline='')as cfile:
			fieldn = ['ID','D1','D2','D3','D4','D5','Ver']

			writer = csv.DictWriter(cfile,fieldnames=fieldn)
			for x in d:
				title = x.split('-')[0]
				d1 = x.split('-')[1]
				d2 = x.split('-')[2]
				d3 = x.split('-')[3]
				d4 = x.split('-')[4]
				d5 = x.split('-')[5]
				ver = x.split('-')[6]
				writer.writerow({'ID':title,'D1':d1,'D2':d2,'D3':d3,'D4':d4,'D5':d5,'Ver':ver})

	with open('user.csv','a',newline='')as cfile:
			fieldn = ['ID','D1','D2','D3','D4','D5','Ver']

			writer = csv.DictWriter(cfile,fieldnames=fieldn)

			writer.writerow({'ID':url,'D1':"",'D2':"",'D3':"",'D4':"",'D5':"",'Ver':"0"})

def inMes(url,x):
	test = "1"
	con = ""
	Dlist = [""]*5
	ver = ""
	with open('user.csv',newline='') as csvfile:
		rows = csv.DictReader(csvfile)
		for row in rows:
			if row['ID'] == url and row['Ver'] == "0" and row['D1'] == "":
				con = row['ID']
				Dlist[0] = x
				Dlist[1] = row['D2']
				Dlist[2] = row['D3']
				Dlist[3] = row['D4']
				Dlist[4] = row['D5']
				ver = "1"
			elif row['ID'] == url and row['Ver'] == "1" and row['D2'] == "":
				Dlist[0] = row['D1']
				Dlist[1] = x
				Dlist[2] = row['D3']
				Dlist[3] = row['D4']
				Dlist[4] = row['D5']
				ver = "2"
			elif row['ID'] == url and row['Ver'] == "2" and row['D3'] == "":
				Dlist[0] = row['D1']
				Dlist[1] = row['D2']
				Dlist[2] = x
				Dlist[3] = row['D4']
				Dlist[4] = row['D5']
				ver = "3"
			elif row['ID'] == url and row['Ver'] == "3" and row['D4'] == "":
				Dlist[0] = row['D1']
				Dlist[1] = row['D2']
				Dlist[2] = row['D3']
				Dlist[3] = x
				Dlist[4] = row['D5']
				ver = "4"
			elif row['ID'] == url and row['Ver'] == "4" and row['D5'] == "":
				Dlist[0] = row['D1']
				Dlist[1] = row['D2']
				Dlist[2] = row['D3']
				Dlist[3] = row['D4']
				Dlist[4] = x
				ver = "5"		

	with open('user.csv','a',newline='')as cfile:
			fieldn = ['ID','D1','D2','D3','D4','D5','Ver']

			writer = csv.DictWriter(cfile,fieldnames=fieldn)

			if con != url:
				writer.writerow({'ID':url,'D1':"",'D2':"",'D3':"",'D4':"",'D5':"",'Ver':"0"})	
			else:
				writer.writerow({'ID':url,'D1':Dlist[0],'D2':Dlist[1],'D3':Dlist[2],'D4':Dlist[3],'D5':Dlist[4],'Ver':ver})		

def showMes(url):
	a = "1"
	with open('user.csv',newline='') as csvfile:
		rows = csv.DictReader(csvfile)
		for row in rows:
			if row['ID'] == url and row['Ver'] == '5':
				return "{}{}{}{}{}".format(row['D1'],row['D2'],row['D3'],row['D4'],row['D5'])
	return a

