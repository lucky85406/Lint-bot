import sys
from datetime import datetime
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from apiclient import discovery
from oauth2client import client
from oauth2client import tools
from oauth2client.file import Storage

def gmes(txt):

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
	#單純取出時間稍後塞入sheet
	now = datetime.now()
	time = now.strftime("%Y/%m/%d-%H:%M:%S")
	#透過insert_row寫入值 第二行塞入時間,abc,123的值
	sheet.insert_row([time,txt],2)
	print(getSheetValue(spreadsheet_key_path,'sheet1!A1:B'))


def getSheetValue(spreadsheetId, rangeName):
 
    # 建立 Google Sheet API 連線
    credentials = getCredentials()
    http = credentials.authorize(httplib2.Http())
    discoveryUrl = ('https://sheets.googleapis.com/$discovery/rest?'
                    'version=v4')
    service = discovery.build('sheets', 'v4', http=http, discoveryServiceUrl=discoveryUrl)
 
    # 取的 Sheet 資料
    result = service.spreadsheets().values().get(spreadsheetId=spreadsheetId, range=rangeName).execute()
    values = result.get('values', [])
 
    return values
