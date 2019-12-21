import csv
import random
import json

def goMes(url):
	with open('user.csv','a+',newline='')as cfile:
		fieldn = ['Utoken','U1','U2','U3','U4','U5']

		writer = csv.DictWriter(cfile,fieldnames=fieldn)

		writer.writeheader()

		writer.writerow({'Utoken':url,'U1':'2','U2':'x','U3':'x','U4':'x','U5':'x'})

def inMes(url,x):
	with open('user.csv','a+',newline='')as cfile:
		fieldn = ['Utoken','U1','U2','U3','U4','U5']

		writer = csv.DictWriter(cfile,fieldnames=fieldn)

		writer.writeheader()

		writer.writerow({'Utoken':url,'U1':"2",'U2':"x",'U3':x,'U4':"x",'U5':"x"})
def showMes(url):
	with open('user.csv',newline='') as csvfile:
		rows = csv.DictReader(csvfile)
		a =0
		for row in rows:
			b =str(a)
			if row['Utoken'] == url and row['U1'] == b:
				return "ID:\n{}\nU1: {}\nU2: {}\nU3: {}\nU4: {}\nU5: {}\n".format(row['Utoken'],row['U1'],row['U2'],row['U3'],row['U4'],row['U5'])
			else:
				a = a+1	
				return "1"
				