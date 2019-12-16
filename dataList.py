import csv
import random
import gspread
import time #待會會取時間
from oauth2client.service_account import ServiceAccountCredentials


Lcode = ['L1','L2','L3','L4','L5','L6','L7','L8','L9','L10','L11','L12','L13','L14','L15','L16','L17','L18']
def dataList(intxt):
	set1 = set()
	set2 = set()
	s = intxt
	with open('cosurl.csv',newline='')as csvfile:
		rows = csv.DictReader(csvfile)
		for row in rows:
			for x in range(0,18):
				if row[Lcode[x]] == s:
					set1.add(row['url'])
	a = len(set1)
	if a >=10:
		set2 = random.sample(set1,10)
	else:
		return set1	

	return set2
def dataOpen(intxt):
	testxt=""
	with open('usertxt.txt','r') as f:
		testxt = f.read()
	with open('usertxt.txt','w') as f:
		f.write(testxt+intxt+"、")
	with open('usertxt.txt','r') as f:
		testxt = f.read()
	if intxt == "show":
		return testxt
	elif intxt == "返回":
		with open('usertxt.txt','w') as f:
			f.write("")
def dataInput(intxt):
	auth_json_path = 'PythonUpload-841c8b986f44.json' #由剛剛建立出的憑證，放置相同目錄以供引入
	gss_scopes = ['https://spreadsheets.google.com/feeds'] #我們想要取用的範圍



	def auth_gss_client(path, scopes):
		credentials = ServiceAccountCredentials.from_json_keyfile_name(path, scopes)
		return gspread.authorize(credentials)

	gss_client = auth_gss_client(auth_json_path, gss_scopes) #呼叫我們的函式


	#從剛剛建立的sheet，把網址中 https://docs.google.com/spreadsheets/d/〔key〕/edit 的 〔key〕的值代入 
	spreadsheet_key_path = '1vhiAa6idyIwIkVVZdTXzhAHKclf9lvb5j4PXhsodWXM'

	#我們透過open_by_key這個method來開啟sheet
	sheet = gss_client.open_by_key(spreadsheet_key_path).sheet1
	#單純取出時間稍後塞入sheet
	#today = time.strftime("%c")
	#透過insert_row寫入值 第二行塞入時間,abc,123的值
	sheet.insert_row([intxt], 2)	
	