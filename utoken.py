import csv
import random


def outU():
	with open('user.csv',newline='') as csvf:
		rows = csv.DictReader(csvf)

		for row in rows:
			if tok == row['Utoken']:
				print(row['Utoken'],row['U1'])
def  inID(uid):
	with open('user.csv', 'w' ,newline='') as csvf:

		filedn = ['Utoken','U1']

		writer = csv.DictWriter(csvf,fieldnames=filedn)

		writer.writeheader()
		writer.writerow({'Utoken':uid,'U1':""})
def inData(uid,x):
	with open('user.csv',newline='') as readf:
		rows = csv.DictReader(readf)

		for row in rows:
			if uid == row['Utoken']:
				with open('user.csv', 'w' ,newline='') as wrtf:

					filedn = ['Utoken','U1']

					writer = csv.DictWriter(wrtf,fieldnames=filedn)

					writer.writeheader()
					writer.writerow({'Utoken':uid,'U1':x})