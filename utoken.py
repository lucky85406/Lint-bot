import csv
def outU():
	with open('user.csv',newline='') as csvf:
		rows = csv.DictReader(csvf)

		for row in rows:
			print(row['Utoken'],row['U1'])
def  inU(mes):
	with open('user.csv', 'w' ,newline='') as csvf:

		filedn = ['Utoken','U1']

		writer = csv.DictWriter(csvf,fieldnames=filedn)

		writer.writeheader()
		writer.writerow({'Utoken':mes,'U1':123})