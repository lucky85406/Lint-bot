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
			if row['ID'] == "U7a3fa520f67563a2429f22e86b798981":
				print(row['ID']+":"+row['love'])	