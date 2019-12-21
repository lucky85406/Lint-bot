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
	a=0
	b=""
	with open('user.csv',newline='') as csvfile:
		rows = csv.DictReader(csvfile)
		for row in rows:
			b = row['n']
			if int(b)>0:
				a = a+1

	with open('user.csv','a',newline='')as cfile:
			fieldn = ['Utoken','U1','n']

			writer = csv.DictWriter(cfile,fieldnames=fieldn)


			writer.writerow({'Utoken':url,'U1':x,'n':a})

	
def showMes(url):
	with open('user.csv',newline='') as csvfile:
		rows = csv.DictReader(csvfile)
		for row in rows:
			if row['n'] == '0':
				print('--------------\n')
				print(row)
				print('\n--------------')
			elif row['n'] == '1':
				print('--------------\n')
				print('ID:{} U1:{} N:{}'.format(row['Utoken'],row['U1'],row['n']))
				print('\n--------------')
			elif row['n'] == '2':
				print('--------------\n')
				print('ID:{} U1:{} N:{}'.format(row['Utoken'],row['U1'],row['n']))
				print('\n--------------')			
				