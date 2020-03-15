import pygsheets



def mesin():
	gc = pygsheets.authorize(service_account_file='googleToken.json')
	survey_url = 'https://docs.google.com/spreadsheets/d/1vhiAa6idyIwIkVVZdTXzhAHKclf9lvb5j4PXhsodWXM/'
	sh = gc.open_by_url(survey_url)
	ws = sh.worksheet_by_title(' P_UpLoadTest')
	ws.update_value('A1','test')

	df1 = pd.DataFrame({'a':[1,2],'b':[3,4]})
	ws.set_dataframe(df1,'A2',copy_index=True,nan='')
