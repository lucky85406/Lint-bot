import csv
import random
import json
def outU():
	with open('user.csv',newline='') as csvf:
		rows = csv.DictReader(csvf)
		for row in rows:
			print(row['Utoken'],row['U1'],row['U2'],row['U3'],row['U4'],row['U5'])
		return json.loads(rows)
		
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
					writer.writerow({'Utoken':uid,'U1':x,'U2':row['U2'],'U3':row['U3'],'U4':row['U4'],'U5':row['U5']})
def ine(uid,x):
	with open('user.csv',newline='') as csvf:
		rows = csv.DictReader(csvf)
		for row in rows:
			if row['Utoken'] == uid:
				with open('user.csv', 'w' ,newline='') as csvf:

					filedn = ['Utoken','U1','U2','U3','U4','U5']

					writer = csv.DictWriter(csvf,fieldnames=filedn)

					writer.writeheader()
					writer.writerow({'Utoken':uid,'U1':row['U1'],'U2':x,'U3':row['U3'],'U4':row['U4'],'U5':row['U5']})
def inl(uid,x):
	with open('user.csv',newline='') as csvf:
		rows = csv.DictReader(csvf)
		for row in rows:
			if row['Utoken'] == uid:
				with open('user.csv', 'w' ,newline='') as csvf:

					filedn = ['Utoken','U1','U2','U3','U4','U5']

					writer = csv.DictWriter(csvf,fieldnames=filedn)

					writer.writeheader()
					writer.writerow({'Utoken':uid,'U1':row['U1'],'U2':row['U2'],'U3':x,'U4':row['U4'],'U5':row['U5']})
def inq(uid,x):
	with open('user.csv',newline='') as csvf:
		rows = csv.DictReader(csvf)
		for row in rows:
			if row['Utoken'] == uid:
				with open('user.csv', 'w' ,newline='') as csvf:

					filedn = ['Utoken','U1','U2','U3','U4','U5']

					writer = csv.DictWriter(csvf,fieldnames=filedn)

					writer.writeheader()
					writer.writerow({'Utoken':uid,'U1':row['U1'],'U2':row['U2'],'U3':row['U3'],'U4':x,'U5':row['U5']})
def inu(uid,x):
	with open('user.csv',newline='') as csvf:
		rows = csv.DictReader(csvf)
		for row in rows:
			if row['Utoken'] == uid:
				with open('user.csv', 'w' ,newline='') as csvf:

					filedn = ['Utoken','U1','U2','U3','U4','U5']

					writer = csv.DictWriter(csvf,fieldnames=filedn)

					writer.writeheader()
					writer.writerow({'Utoken':uid,'U1':row['U1'],'U2':row['U2'],'U3':row['U3'],'U4':row['U4'],'U5':x})

