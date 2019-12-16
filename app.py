 
from flask import Flask, request, abort
from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage, TemplateSendMessage, ButtonsTemplate, PostbackTemplateAction, MessageTemplateAction, URITemplateAction, ImageCarouselColumn, ImageCarouselTemplate, ImageSendMessage, URIImagemapAction, MessageImagemapAction
    )
from oauth2client.service_account import ServiceAccountCredentials 

from dataList import (dataList)
import random
import gspread
import time #待會會取時間



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
today = time.strftime("%c")


app = Flask(__name__)

line_bot_api = LineBotApi('+xnEz6H8r8/SZr2w0WRZxzuYUfJ98uPnZmkwybxctShP3J7j2H9P7Wub9o4/m7Cwb3jgsXNBFxBxOQ+NFvIsSM4HEccnDapK8x8rI2lRCGggqRGtwdlacsdtDalahZmiEI5K/GI1T6XqjkQf41CqNAdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('c8d07de2da7598c580b0979f0c96978d')


@app.route("/")
def home():
    return 'home OK'

# 監聽所有來自 /callback 的 Post Request
@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        print("Invalid signature. Please check your channel access token/channel secret.")
        abort(400)

    return 'OK'




# 處理訊息
@handler.add(MessageEvent, message=TextMessage)
def function(event):
	tStart = time.time()
	# 根據line manager 內設定做判斷
	judge = False
	meetjud = False
	judstr = event.message.text
	data = dataList(judstr)
	dlen = len(data)
	dlist = list(data)

	if judstr == "選單" or judstr == "？" or judstr == "?":
		judge = True
	elif dlen==0:
		line_bot_api.reply_message(	
				event.reply_token,
				TextSendMessage(text= "感謝您的訊息"+chr(0x100008)+"\n"\
									+"很抱歉無法搜尋到符合您輸入的選項！!\n"\
									+chr(0x26A0)+chr(0xFE0F)+"請確認前後是否有空格存在"+chr(0x10002E)))
	elif dlen>0:
		# 將所有圖片陣列顯示出來										
		Image_Carousel = TemplateSendMessage(
			alt_text='目錄 template',
			template=ImageCarouselTemplate(
			columns=[
				ImageCarouselColumn(
					image_url=dlist[0],
					action=PostbackTemplateAction(
					label=' ',
					text=' ',
					data='action=buy&itemid=1'
						)
					),
				ImageCarouselColumn(
					image_url=dlist[1],
					action=PostbackTemplateAction(
					label=' ',
					text=' ',
					data='action=buy&itemid=2'
						)
					),
				ImageCarouselColumn(
					image_url=dlist[2],
					action=PostbackTemplateAction(
					label=' ',
					text=' ',
					data='action=buy&itemid=3'
						)
					),
				ImageCarouselColumn(
					image_url=dlist[3],
					action=PostbackTemplateAction(
					label=' ',
					text=' ',
					data='action=buy&itemid=4'
						)
					),
				ImageCarouselColumn(
					image_url=dlist[4],
					action=PostbackTemplateAction(
					label=' ',
					text=' ',
					data='action=buy&itemid=5'
						)
					),
				ImageCarouselColumn(
					image_url=dlist[5],
					action=PostbackTemplateAction(
					label=' ',
					text=' ',
					data='action=buy&itemid=6'
						)
					),
				ImageCarouselColumn(
					image_url=dlist[6],
					action=PostbackTemplateAction(
					label=' ',
					text=' ',
					data='action=buy&itemid=7'
						)
					),
				ImageCarouselColumn(
					image_url=dlist[7],
					action=PostbackTemplateAction(
					label=' ',
					text=' ',
					data='action=buy&itemid=8'
						)
					),
				ImageCarouselColumn(
					image_url=dlist[8],
					action=PostbackTemplateAction(
					label=' ',
					text=' ',
					data='action=buy&itemid=9'
						)
					),
				ImageCarouselColumn(
					image_url=dlist[9],
					action=PostbackTemplateAction(
					label=' ',
					text=' ',
					data='action=buy&itemid=10'
						)
					)
				]
			)
		)
		tEnd = time.time()
		print ("It cost %f sec" % (tEnd - tStart))
		line_bot_api.reply_message(event.reply_token,Image_Carousel)		



		


	


								

#執行
if __name__ == "__main__":
    app.run()
     