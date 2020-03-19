import sys
from datetime import datetime
import pytz
import gspread
from oauth2client.service_account import ServiceAccountCredentials

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
	time = datetime.now().strftime("%Y/%m/%d-%H:%M:%S")

	utc = pytz.utc
	tpe = pytz.timezone('Asiz/Taipei')
	utcnow = datetime.utcnow()
	print(utcnow)

	#透過insert_row寫入值 第二行塞入時間,abc,123的值
	token().insert_row([time,user,love],2)

def gmes():
	for x in token().col_values(1):
		print("time:",x)
