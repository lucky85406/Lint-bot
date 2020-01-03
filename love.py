import csv

def love(uid,text):
	keyin = text.split(":")
	with open('mylove.csv','a',newline='')as cfile:
			fieldn = ['ID','love']

			writer = csv.DictWriter(cfile,fieldnames=fieldn)

			writer.writerow({'ID':uid,'love':keyin[1]})
	with open('mylove.csv',newline='')as csvfile:
		rows = csv.DictReader(csvfile)
		for row in rows:
			if row != "":
				print(row['ID']+":"+row['love'])	