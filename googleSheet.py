import sys
import csv
import pytz
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from datetime import datetime

def token():

	auth_json_path = 'googleToken.json' #由剛剛建立出的憑證，放置相同目錄以供引入
	gss_scopes = ['https://spreadsheets.google.com/feeds'] #我們想要取用的範圍



	def auth_gss_client(path, scopes):
		credentials = ServiceAccountCredentials.from_json_keyfile_name(path, scopes)
		return gspread.authorize(credentials)

	gss_client = auth_gss_client(auth_json_path, gss_scopes) #呼叫我們的函式


	#從剛剛建立的sheet，把網址中 https://docs.google.com/spreadsheets/d/〔key〕/edit 的 〔key〕的值代入
	spreadsheet_key_path = '1vhiAa6idyIwIkVVZdTXzhAHKclf9lvb5j4PXhsodWXM'

	#我們透過open_by_key這個method來開啟sheet
	sheet = gss_client.open_by_key(spreadsheet_key_path).sheet1
	return sheet

def kmes(user,love):
	utc = pytz.utc
	tpe = pytz.timezone('Asia/Taipei')
	utcnow = datetime.utcnow()
	stime = tpe.fromutc(utcnow).strftime("%Y/%m/%d-%H:%M")

	#透過insert_row寫入值 第二行塞入時間,abc,123的值
	token().insert_row([stime,user,love],2)

def gmes(user):
	dict = {}
	dlist = list()
	for x in range(2,len(token().col_values(1))+1):
		dlist.append(token().row_values(x))
	with open('mylove.csv','w',newline='')as cfile:
			fieldn = ['ID','love']

			writer = csv.DictWriter(cfile,fieldnames=fieldn)

			writer.writeheader()
			for y in dlist:
				writer.writerow({'ID':y[1],'love':y[2]})

def tmes():
	token().clear()
	token().insert_row(["time","user","love"],1)
	with open('mylove.csv',newline='')as csvfile:
		rows = csv.DictReader(csvfile)
		for row in rows:
			token().insert_row(["stime",row['ID'],row['love']],2)
