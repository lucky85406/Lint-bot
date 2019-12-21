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
	con = ""
	Dlist = [""]*5
	ver = ""
	with open('user.csv',newline='') as csvfile:
		rows = csv.DictReader(csvfile)
		for row in rows:
			if row['ID'] != url:
				con = "tr"
			if row['ID'] == url and row['Ver'] == "0" and row['D1'] == "":
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

			if con == "tr":
				con = "fa"
				writer.writerow({'ID':url,'D1':"",'D2':"",'D3':"",'D4':"",'D5':"",'Ver':"0"})
				
			elif con == "fa":
				writer.writerow({'ID':url,'D1':Dlist[0],'D2':Dlist[1],'D3':Dlist[2],'D4':Dlist[3],'D5':Dlist[4],'Ver':ver})			
	

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