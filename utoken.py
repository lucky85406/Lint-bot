import csv
import random
import json

def go(url):
	with open('user.csv','w',newline='')as cfile:
			fieldn = ['ID','D1','D2','D3','D4','D5','Ver']

			writer = csv.DictWriter(cfile,fieldnames=fieldn)

			writer.writeheader()

			writer.writerow({'ID':url,'D1':"",'D2':"",'D3':"",'D4':"",'D5':"",'Ver':"0"})

def inMes(url,x):
	a=0
	b=""
	with open('user.csv',newline='') as csvfile:
		rows = csv.DictReader(csvfile)
		for row in rows:
			b = row['Ver']
			if row['ID'] == url and int(b)<=5:
				if  x == "a" or x == "b" or x == "c" or x == "d":
					with open('user.csv','a',newline='')as cfile:
							fieldn = ['ID','D1','D2','D3','D4','D5','Ver']

							writer = csv.DictWriter(cfile,fieldnames=fieldn)

							writer.writerow({'ID':url,'D1':x,'D2':row['D2'],'D3':row['D3'],'D4':row['D4'],'D5':row['D5'],'Ver':int(b)+1})

				elif x == "e" or x == "f" or x == "g" or x == "h" or x == "i" or x =="j" or x =="k":
					with open('user.csv','a',newline='')as cfile:
							fieldn = ['ID','D1','D2','D3','D4','D5','Ver']

							writer = csv.DictWriter(cfile,fieldnames=fieldn)


							writer.writerow({'ID':url,'D1':row['D1'],'D2':x,'D3':row['D3'],'D4':row['D4'],'D5':row['D5'],'Ver':int(b)+1})

				elif x == "l" or x == "m" or x == "n" or x == "o" or x == "p":
					with open('user.csv','a',newline='')as cfile:
							fieldn = ['ID','D1','D2','D3','D4','D5','Ver']

							writer = csv.DictWriter(cfile,fieldnames=fieldn)


							writer.writerow({'ID':url,'D1':row['D1'],'D2':row['D2'],'D3':x,'D4':row['D4'],'D5':row['D5'],'Ver':int(b)+1})

				elif x == "q" or x == "r" or x == "s":
					with open('user.csv','a',newline='')as cfile:
							fieldn = ['ID','D1','D2','D3','D4','D5','Ver']

							writer = csv.DictWriter(cfile,fieldnames=fieldn)


							writer.writerow({'ID':url,'D1':row['D1'],'D2':row['D2'],'D3':row['D3'],'D4':x,'D5':row['D5'],'Ver':int(b)+1})

				elif x == "t" or x == "u" or x == "v":
					with open('user.csv','a',newline='')as cfile:
							fieldn = ['ID','D1','D2','D3','D4','D5','Ver']

							writer = csv.DictWriter(cfile,fieldnames=fieldn)


							writer.writerow({'ID':url,'D1':row['D1'],'D2':row['D2'],'D3':row['D3'],'D4':row['D4'],'D5':x,'Ver':int(b)+1})

	

def showMes(url):
	with open('user.csv',newline='') as csvfile:
		rows = csv.DictReader(csvfile)
		for row in rows:
			if row['n'] == '0':
				print('--------------\n')
				print('ID:{} U1:{} N:{}'.format(row['Utoken'],row['U1'],row['n']))
				print('\n--------------')
			elif row['n'] == '1':
				print('--------------\n')
				print('ID:{} U1:{} N:{}'.format(row['Utoken'],row['U1'],row['n']))
				print('\n--------------')
			elif row['n'] == '2':
				print('--------------\n')
				print('ID:{} U1:{} N:{}'.format(row['Utoken'],row['U1'],row['n']))
				print('\n--------------')
			else:
				print('--------------\n')
				print(row)
				print('\n--------------')		
				