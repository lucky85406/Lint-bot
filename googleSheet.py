import sys
import datetime
import gspread
from oauth2client.service_account import ServiceAccountCredentials as SAC

def gmes(txt):
	if txt != "":
		GDriveJSON = 'googleToken.json'
		GSpreadSheet = ' P_UpLoadTest'

		while True:
			try:
				scope = ['https://docs.google.com/spreadsheets/d/1vhiAa6idyIwIkVVZdTXzhAHKclf9lvb5j4PXhsodWXM/edit#gid=0']
				key = SAC.from_json_keyfile_name(GDriveJSON,scope)
				gc = gspread.authorize(key)
				worksheet = gc.open(GSpreadSheet).sheet1
			except Exception as e:
				print('無法連線Google試算表',e)
				sys.exit(1)
			textt = ""
			textt+= text
			if textt != "":
				worksheet.append_row((datatime.datetime.now(),textt))
				print('新增一列資料到試算表',GSpreadSheet)
				return textt
