from flask import Flask, request, abort
from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage, TemplateSendMessage, 
    ButtonsTemplate, PostbackTemplateAction, MessageTemplateAction, 
    URITemplateAction, ImageCarouselColumn, ImageCarouselTemplate, 
    ImageSendMessage, URIImagemapAction, MessageImagemapAction, CarouselTemplate ,
    CarouselColumn, MessageImagemapAction, ImagemapArea, ImagemapSendMessage, BaseSize,
    BubbleContainer, BoxComponent, TextComponent, FlexSendMessage, ImageComponent, ButtonComponent,
    URIAction, MessageAction, CarouselContainer, SeparatorComponent, IconComponent
)
from modelCode import(food, aroma, taste, chain, price, showimg, mylove, tenMod, single)
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
	
	ukey = event.message.text
	mod = []
	if ukey == "紅肉" or ukey =="白肉" or ukey =="海鮮" or ukey =="甜點":
		user_id = event.source.user_id
		inMes(user_id,conversionCode(ukey))
		mod[0] = aroma()

	elif ukey == "花香" or ukey =="漿果" or ukey =="柑橘" or ukey =="熱帶水果" or ukey =="淺色水果" or ukey =="香料" or ukey =="土木":
		user_id = event.source.user_id
		inMes(user_id,conversionCode(ukey))
		mod[0] = taste()
	elif ukey == "清香" or ukey =="甜" or ukey =="圓潤" or ukey =="酸" or ukey =="濃厚":
		user_id = event.source.user_id
		inMes(user_id,conversionCode(ukey))
		mod[0] = chain()
	elif ukey == "家樂福" or ukey =="全聯" or ukey =="Costco":
		user_id = event.source.user_id
		inMes(user_id,conversionCode(ukey))
		mod[0] = price()
	elif ukey =="100~350元" or ukey =="351~600元" or ukey =="600元以上":
		user_id = event.source.user_id
		inMes(user_id,conversionCode(ukey))
		mod[0] = showimg()
	else:
		if ukey == "go":
			user_id = event.source.user_id
			go(user_id)
			mod[0] = food()

		elif ukey == "showImg":
			user_id = event.source.user_id
			data = dataList(showMes(user_id))
			dlist = list(data)
			mod[0] = tenMod(dlist,data)

		elif ukey.split(':')[0] == 'MyLove':
			user_id = event.source.user_id
			profile = line_bot_api.get_profile(user_id)
			name = profile.display_name
			love(name,ukey)

		elif ukey.split(':')[0] == 're':
			user_id = event.source.user_id
			profile = line_bot_api.get_profile(user_id)
			name = profile.display_name
			relove(name,ukey.split(':')[1])
			dlist = list(love2(name))
			mod[0] = mylove(name,dlist)

		elif ukey == 'seemylove':
			user_id = event.source.user_id
			profile = line_bot_api.get_profile(user_id)
			name = profile.display_name		
			dlist = list(love2(name))
			mod[0] = mylove(name,dlist)

		elif ukey.split(':')[0] == 'see':
			data = singleList(ukey.split(':')[1])
			mod[0] = single(data)

	line_bot_api.reply_message(event.reply_token,aroma())







# 執行
if __name__ == "__main__":
    app.run()
