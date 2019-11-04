 

from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)

import pydata
conn = pymssql.connect(server='localhost', user='DESKTOP-3EGC1SF\陳柏任', password='', database='MyDB')  
cursor = conn.cursor()  
cursor.execute('SELECT id,name,list FROM mychoose')
row = cursor.fetchone()  
while row:  
	print(row)     
	row = cursor.fetchone()
conn.commit()
 



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
	foodlist = [["a","白肉"], ["b","紅肉"],["c","海鮮"],["d","甜點"]]
	aromalist = [["e","花香"], ["f","漿果"],["g","柑橘"],["h","熱帶水果"],["i","淺色水果"],["j","香料"]]
	tastelist = [["k","清香"], ["l","甜"],["m","圓潤"],["n","濃厚"]]
	pacelist = [["o","家樂福"]]
	pricelist = [["p","351~600"],["q","100~350"],["r","600+"]]
	if event.message.text == (foodlist[0][0]+aromalist[4][0]+tastelist[0][0]+pacelist[0][0]+pricelist[1][0]):
			line_bot_api.reply_message(	
        	event.reply_token,
 			TextSendMessage(text="your choose->"+foodlist[0][1]+"--"+aromalist[4][1]+"--"+tastelist[0][1]+"--"+pacelist[0][1]+"--"+pricelist[1][1]+"-- 美國加州庫克斯氣泡酒"))
 			conn.close() 
		


	


								


if __name__ == "__main__":
    app.run()
     