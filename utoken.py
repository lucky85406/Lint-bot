import csv
import random

def outU():
	with open('user.csv',newline='') as csvf:
		rows = csv.DictReader(csvf)
		for row in rows:
			print(row['Utoken'],row['U1'],row['U2'],row['U3'],row['U4'],row['U5'])
		print(rows)
def  inID(uid):
	with open('user.csv', 'w' ,newline='') as csvf:

		filedn = ['Utoken','U1','U2','U3','U4','U5']

		writer = csv.DictWriter(csvf,fieldnames=filedn)

		writer.writeheader()
		writer.writerow({'Utoken':uid,'U1':"",'U2':"",'U3':"",'U4':"",'U5':""})
def ina(uid,x):
	with open('user.csv',newline='') as csvf:
		rows = csv.DictReader(csvf)
		for row in rows:
			if row['Utoken'] == uid:
				with open('user.csv', 'w' ,newline='') as csvf:

					filedn = ['Utoken','U1','U2','U3','U4','U5']

					writer = csv.DictWriter(csvf,fieldnames=filedn)

					writer.writeheader()
					if row['U1'] != '' and row['U2'] != '' and row['U3'] != '' and row['U4'] != '' and row['U5'] != '':
						writer.writerow({'Utoken':uid,'U1':x,'U2':row['U2'],'U3':row['U3'],'U4':row['U4'],'U5':row['U5']})				
				print(row['Utoken'],row['U1'],row['U2'],row['U3'],row['U4'],row['U5'])

