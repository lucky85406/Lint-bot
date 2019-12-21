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
	ver = ""

	if x == "a" or x =="b" or x =="c" or x =="d":
		ver = "1"
	elif x == "e" or x =="f" or x =="g" or x =="h" or x =="i" or x =="j" or x =="k":
		ver ="2"
	elif x == "l" or x =="m" or x =="n" or x =="o" or x =="p":
		ver ="3"
	elif x == "q" or x =="r" or x =="s":
		ver ="4"
	elif x == "y" or x =="u" or x =="v":
		ver ="5"

	with open('user.csv',newline='')as cfile:
		rows = csv.DictReader(cfile)
		for row in rows:
			with open('user.csv','a',newline='')as cfile:
					fieldn = ['ID','D1','D2','D3','D4','D5','Ver']

					writer = csv.DictWriter(cfile,fieldnames=fieldn)
					if row['ID'] == url and row['Ver'] == '0':
						writer.writerow({'ID':url,'D1':x,'D2':row['D2'],'D3':row['D3'],'D4':row['D4'],'D5':row['D5'],'Ver':ver})
					elif row['ID'] == url and row['Ver'] == '1':
						writer.writerow({'ID':url,'D1':row['D1'],'D2':x,'D3':row['D3'],'D4':row['D4'],'D5':row['D5'],'Ver':ver})
					elif row['ID'] == url and row['Ver'] == '2':
						writer.writerow({'ID':url,'D1':row['D1'],'D2':row['D2'],'D3':x,'D4':row['D4'],'D5':row['D5'],'Ver':ver})
					elif row['ID'] == url and row['Ver'] == '3':
						writer.writerow({'ID':url,'D1':row['D1'],'D2':row['D2'],'D3':row['D3'],'D4':x,'D5':row['D5'],'Ver':ver})
					elif row['ID'] == url and row['Ver'] == '4':
						writer.writerow({'ID':url,'D1':row['D1'],'D2':row['D2'],'D3':row['D3'],'D4':row['D4'],'D5':x,'Ver':ver})					
			
	

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