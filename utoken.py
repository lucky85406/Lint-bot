import csv
import random

def outU():
	with open('user.csv',newline='') as csvf:
		rows = csv.DictReader(csvf)
		for row in rows:
			print(row['Utoken'],row['U1'],row['U2'],row['U3'],row['U4'],row['U5'])
def  inID(uid):
	with open('user.csv', 'w' ,newline='') as csvf:

		filedn = ['Utoken','U1','U2','U3','U4','U5']

		writer = csv.DictWriter(csvf,fieldnames=filedn)

		writer.writeheader()
		writer.writerow({'Utoken':uid,'U1':"",'U2':"",'U3':"",'U4':"",'U5':""})
def ina(uid,x):
	with open('user.csv',newline='') as readf:
		rows = csv.DictReader(readf)

		for row in rows:
			if uid == row['Utoken']:
				with open('user.csv', 'w' ,newline='') as wrtf:

					filedn = ['Utoken','U1']

					writer = csv.DictWriter(wrtf,fieldnames=filedn)

					writer.writeheader()
					writer.writerow({'Utoken':uid,'U1':x})
def inb(uid,x):
	with open('user.csv',newline='') as readf:
		rows = csv.DictReader(readf)

		for row in rows:
			if uid == row['Utoken']:
				with open('user.csv', 'w' ,newline='') as wrtf:

					filedn = ['Utoken','U2']

					writer = csv.DictWriter(wrtf,fieldnames=filedn)

					writer.writeheader()
					writer.writerow({'U2':x})
def inc(uid,x):
	with open('user.csv',newline='') as readf:
		rows = csv.DictReader(readf)

		for row in rows:
			if uid == row['Utoken']:
				with open('user.csv', 'w' ,newline='') as wrtf:

					filedn = ['Utoken','U3']

					writer = csv.DictWriter(wrtf,fieldnames=filedn)

					writer.writeheader()
					writer.writerow({'U3':x})
def ind(uid,x):
	with open('user.csv',newline='') as readf:
		rows = csv.DictReader(readf)

		for row in rows:
			if uid == row['Utoken']:
				with open('user.csv', 'w' ,newline='') as wrtf:

					filedn = ['Utoken','U4']

					writer = csv.DictWriter(wrtf,fieldnames=filedn)

					writer.writeheader()
					writer.writerow({'U4':x})
def ine(uid,x):
	with open('user.csv',newline='') as readf:
		rows = csv.DictReader(readf)

		for row in rows:
			if uid == row['Utoken']:
				with open('user.csv', 'w' ,newline='') as wrtf:

					filedn = ['Utoken','U5']

					writer = csv.DictWriter(wrtf,fieldnames=filedn)

					writer.writeheader()
					writer.writerow({'U5':x})

