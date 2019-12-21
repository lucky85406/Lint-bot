import csv
import random
import json

def go(url,x,n):
	with open('user.csv','w',newline='')as cfile:
			fieldn = ['Utoken','U1','n']

			writer = csv.DictWriter(cfile,fieldnames=fieldn)

			writer.writeheader()

			writer.writerow({'Utoken':url,'U1':x,'n':n})

def inMes(url,x):
	with open('user.csv','a',newline='')as cfile:
			fieldn = ['Utoken','U1','n']

			writer = csv.DictWriter(cfile,fieldnames=fieldn)

			writer.writeheader()

			writer.writerow({'Utoken':url,'U1':"z",'n':"2"})

	
def showMes(url):
	with open('user.csv',newline='') as csvfile:
		rows = csv.DictReader(csvfile)
		for row in rows:
			print('--------------\n')
			print(row)
			print('\n--------------')
				