import csv
def outU():
	with open('user.csv',newline='') as csvf:
		rows = csv.DictReader(csvf)

		for row in rows:
			print(row['Utoken'],row['U1'])
def  inU(mes):
	with open('user.csv',newline='') as csvf:
		writer = csv.writer(csvf)

		writer.writerow([mes,111])