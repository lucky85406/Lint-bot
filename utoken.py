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
def inData(uid,x):
	with open('user.csv',newline='') as readf:
		rows = csv.DictReader(readf)

		for row in rows:
			if uid == row['Utoken']:
				with open('user.csv', 'w' ,newline='') as wrtf:

					filedn = ['Utoken','U1','U2','U3','U4','U5']

					writer = csv.DictWriter(wrtf,fieldnames=filedn)

					writer.writeheader()
					if x == "a" or x == "b" or x == "c" or x == "d":
						writer.writerow({'U1':x})
					elif x == "e" or x == "f" or x == "g" or x == "h" or x == "i" or x == "j" or x == "k":
						writer.writerow({'U2':x})
					elif x == "l" or x == "m" or x == "n" or x == "o" or x == "p":
						writer.writerow({'U3':x})
					elif x == "q" or x == "r" or x == "s":
						writer.writerow({'U4':x})
					elif x == "t" or x == "u" or x == "v":
						writer.writerow({'U5':x})