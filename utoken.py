import csv
import random

def rantoken():
	a = random.random()
	return("a{}".format(a))

def outU(tok):
	with open('user.csv',newline='') as csvf:
		rows = csv.DictReader(csvf)

		for row in rows:
			if tok == row['Utoken']:
				print(row['Utoken'],row['U1'])
def  inU(mes):
	with open('user.csv', 'w' ,newline='') as csvf:

		filedn = ['Utoken','U1']

		writer = csv.DictWriter(csvf,fieldnames=filedn)

		writer.writeheader()
		writer.writerow({'Utoken':mes,'U1':123})