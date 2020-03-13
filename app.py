from flask import Flask, request, abort
from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage
)
from modelCode import(
	food, aroma, taste, chain, price, showimg, mylove, tenMod, single,ckey,model)
from utoken import(go,inMes,showMes)
from datalist import(dataList,singleList)
from love import(love,love2,relove)
import random
import time  # 待會會取時間


app = Flask(__name__)

line_bot_api = LineBotApi('OmKfxVvx9CsNGTdlkwgVkSfSAmP0zxVz/IXB9ET1/Twtxc2FCUuOCqeYQFl3tBu5ggPiLBQK0XZ87QtMp3bVn4MDTDGBRktZO10RvV+s8CPq6Ei/tg8qilsfwlWGrFsRi451gCVrj/f4nX6qhR7F4wdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('c7342786e81022d70ef05e4757461fd7')


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


def conversionCode(k):
	code = {'紅肉':'a','白肉':'b','海鮮':'c','甜點':'d','花香':'e'
			,'漿果':'f','柑橘':'g','熱帶水果':'h','淺色水果':'i','香料':'j'
			,'土木':'k','清香':'l','甜':'m','圓潤':'n'
			,'酸':'o','濃厚':'p','家樂福':'q','全聯':'r','Costco':'s'
			,'100~350元':'t','351~600元':'u','600元以上':'v'}
	return code[k]



# 處理訊息
@handler.add(MessageEvent, message=TextMessage)
def function(event):
	tStart = time.time()#計時開始

	#取得使用者輸入訊息
	def Ukey():
		return event.message.text

	#取得使用者ID
	def Uid():
		return event.source.user_id

	#將使用者選擇寫進user.csv
	def InMes():
		return inMes(Uid(),conversionCode(Ukey()))

	#取得使用者姓名
	def Name():
		return line_bot_api.get_profile(Uid()).display_name

	if Ukey() == "go":
		go(Uid())
		line_bot_api.reply_message(event.reply_token,model(Ukey()))

	elif ckey(Ukey()):
		InMes()
		line_bot_api.reply_message(event.reply_token,model(Ukey()))

	elif ckey(Ukey()):
		InMes()
		data = dataList(showMes(Uid()))
		line_bot_api.reply_message(event.reply_token,tenMod(data))

	elif Ukey().split(':')[0] == 'MyLove':
		if love(Name(),Ukey()):
			line_bot_api.reply_message(event.reply_token,TextSendMessage(text='我的最愛:已存在'))

	elif Ukey().split(':')[0] == 're':
		relove(Name(),Ukey().split(':')[1])
		dlist = list(love2(Name()))
		line_bot_api.reply_message(event.reply_token,mylove(Name(),dlist))

	elif Ukey() == 'seemylove':
		dlist = list(love2(Name()))
		line_bot_api.reply_message(event.reply_token,mylove(Name(),dlist))

	elif Ukey().split(':')[0] == 'see':
		data = singleList(Ukey().split(':')[1])
		line_bot_api.reply_message(event.reply_token,single(data))
	tEnd = time.time()#計時結束
	print('-------------------')
	print( "It cost %f sec" % (tEnd - tStart))






# 執行
if __name__ == "__main__":
    app.run()
