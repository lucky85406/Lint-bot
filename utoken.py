import csv
import random
import json

def go(url,x,n):
	with open('user.csv','a+',newline='')as cfile:
			fieldn = ['Utoken','U1','n']

			writer = csv.DictWriter(cfile,fieldnames=fieldn)

			writer.writeheader()

			writer.writerow({'Utoken':url,'U1':x,'n':n})

def inMes(url,x):
	with open('user.csv',newline='') as c:
		rows = csv.DictReader(c)

		for row in rows:
			a = "1"
			if int(a)>0:
				with open('user.csv','a+',newline='')as cfile:
						fieldn = ['Utoken','U1','n']

						writer = csv.DictWriter(cfile,fieldnames=fieldn)

						writer.writeheader()

						writer.writerow({'Utoken':url,'U1':"x",'n':"2"})

	
def showMes(url):
	with open('user.csv',newline='') as csvfile:
		rows = csv.DictReader(csvfile)
		for row in rows:
			print(row)
			if row['Utoken'] == url and row['n'] == '1':
				return "ID:\n{}\nU1: {}\nn: {}".format(row['Utoken'],row['U1'],row['n'])
			elif row['Utoken'] == url and row['n'] == '2':
				return "ID:\n{}\nU1: {}\nn: {}".format(row['Utoken'],row['U1'],row['n'])
				