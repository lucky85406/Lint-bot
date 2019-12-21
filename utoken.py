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
			if row['ID'] == url:
				if  x == "a" or x == "b" or x == "c" or x == "d":
					if row['Ver']=="1":
						with open('user.csv','a',newline='')as cfile:
								fieldn = ['ID','D1','D2','D3','D4','D5','Ver']

								writer = csv.DictWriter(cfile,fieldnames=fieldn)

								writer.writerow({'ID':url,'D1':x,'D2':row['D2'],'D3':row['D3'],'D4':row['D4'],'D5':row['D5'],'Ver':int(b)+1})

				elif x == "e" or x == "f" or x == "g" or x == "h" or x == "i" or x =="j" or x =="k":
					if row['Ver']=="2":
						with open('user.csv','a',newline='')as cfile:
								fieldn = ['ID','D1','D2','D3','D4','D5','Ver']

								writer = csv.DictWriter(cfile,fieldnames=fieldn)


								writer.writerow({'ID':url,'D1':row['D1'],'D2':x,'D3':row['D3'],'D4':row['D4'],'D5':row['D5'],'Ver':int(b)+1})

				elif x == "l" or x == "m" or x == "n" or x == "o" or x == "p":
					if row['Ver']=="3":
						with open('user.csv','a',newline='')as cfile:
								fieldn = ['ID','D1','D2','D3','D4','D5','Ver']

								writer = csv.DictWriter(cfile,fieldnames=fieldn)


								writer.writerow({'ID':url,'D1':row['D1'],'D2':row['D2'],'D3':x,'D4':row['D4'],'D5':row['D5'],'Ver':int(b)+1})

				elif x == "q" or x == "r" or x == "s":
					if row['Ver']=="4":
						with open('user.csv','a',newline='')as cfile:
								fieldn = ['ID','D1','D2','D3','D4','D5','Ver']

								writer = csv.DictWriter(cfile,fieldnames=fieldn)


								writer.writerow({'ID':url,'D1':row['D1'],'D2':row['D2'],'D3':row['D3'],'D4':x,'D5':row['D5'],'Ver':int(b)+1})

				elif x == "t" or x == "u" or x == "v":
					if row['Ver']=="5":
						with open('user.csv','a',newline='')as cfile:
								fieldn = ['ID','D1','D2','D3','D4','D5','Ver']

								writer = csv.DictWriter(cfile,fieldnames=fieldn)


								writer.writerow({'ID':url,'D1':row['D1'],'D2':row['D2'],'D3':row['D3'],'D4':row['D4'],'D5':x,'Ver':int(b)+1})

	

def showMes(url):
	with open('user.csv',newline='') as csvfile:
		rows = csv.DictReader(csvfile)
		for row in rows:
			if row['Ver'] == '0':
				print('--------------\n')
				print('ID:{} D1:{} D2:{} D3:{} D4:{} D5:{} Ver:{}'.format(row['ID'],row['D1'],row['D2'],row['D3'],row['D4'],row['D5'],row['Ver']))
				print('\n--------------')
			elif row['Ver'] == '1':
				print('--------------\n')
				print('ID:{} D1:{} D2:{} D3:{} D4:{} D5:{} Ver:{}'.format(row['ID'],row['D1'],row['D2'],row['D3'],row['D4'],row['D5'],row['Ver']))
				print('\n--------------')
			elif row['Ver'] == '2':
				print('--------------\n')
				print('ID:{} D1:{} D2:{} D3:{} D4:{} D5:{} Ver:{}'.format(row['ID'],row['D1'],row['D2'],row['D3'],row['D4'],row['D5'],row['Ver']))
				print('\n--------------')
			elif row['Ver'] == '3':
				print('--------------\n')
				print('ID:{} D1:{} D2:{} D3:{} D4:{} D5:{} Ver:{}'.format(row['ID'],row['D1'],row['D2'],row['D3'],row['D4'],row['D5'],row['Ver']))
				print('\n--------------')	
			elif row['Ver'] == '4':
				print('--------------\n')
				print('ID:{} D1:{} D2:{} D3:{} D4:{} D5:{} Ver:{}'.format(row['ID'],row['D1'],row['D2'],row['D3'],row['D4'],row['D5'],row['Ver']))
				print('\n--------------')
			elif row['Ver'] == '5':
				print('--------------\n')
				print('ID:{} D1:{} D2:{} D3:{} D4:{} D5:{} Ver:{}'.format(row['ID'],row['D1'],row['D2'],row['D3'],row['D4'],row['D5'],row['Ver']))
				print('\n--------------')