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
from utoken import(inID,outU,ina,ine,inl,inq,inu)
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


# 處理訊息
@handler.add(MessageEvent, message=TextMessage)
def function(event):

	ukey = event.message.text
	#!!!!!!!!!!!!!!!!!這裡有ID
	user_id = event.source.user_id
	if ukey == "go":	
		inID(user_id)
		line_bot_api.reply_message(	
				event.reply_token,
				TextSendMessage(text= "儲存成功"))
	elif ukey == "show":
		line_bot_api.reply_message(	
				event.reply_token,
				TextSendMessage(text= outU(user_id)))		
	else:
		if ukey == "a" or ukey == "b" or ukey == "c" or ukey == "d":
			ina(user_id,ukey)
		elif ukey == "e" or ukey == "f" or ukey == "g" or ukey == "h" or ukey == "i" or ukey == "j" or ukey == "k":
			ine(user_id,ukey)
		elif ukey == "l" or ukey == "m" or ukey == "n" or ukey == "o" or ukey == "p" :
			inl(user_id,ukey)
		elif ukey == "q" or ukey == "r" or ukey == "s":
			inq(user_id,ukey)
		elif ukey == "t" or ukey == "u" or ukey == "v":
			inu(user_id,ukey) 



	if event.message.text == "食物":
		with open("usertxt.txt","w") as f:
				mes = f.write("")
		Image_Carousel = TemplateSendMessage(
			alt_text='目錄 template',
			template=ImageCarouselTemplate(
			columns=[
				ImageCarouselColumn(
					image_url="https://i.imgur.com/6btHgSL.jpg",
					action=PostbackTemplateAction(
					label='a',
					text='a',
					data='action=buy&itemid=1'
						)
					),
				ImageCarouselColumn(
					image_url="https://i.imgur.com/0I6l6mm.jpg",
					action=PostbackTemplateAction(
					label='b',
					text='b',
					data='action=buy&itemid=2'
						)
					),
				ImageCarouselColumn(
					image_url="https://i.imgur.com/eVbMryK.jpg",
					action=PostbackTemplateAction(
					label='c',
					text='c',
					data='action=buy&itemid=3'
						)
					),
				ImageCarouselColumn(
					image_url="https://i.imgur.com/5lTDJIq.jpg",
					action=PostbackTemplateAction(
					label='d',
					text='d',
					data='action=buy&itemid=4'
						)
					),
				ImageCarouselColumn(
					image_url="https://i.imgur.com/52y6R7k.jpg",
					action=PostbackTemplateAction(
					label='e',
					text='e',
					data='action=buy&itemid=5'
						)
					)
				]
			)
		)
		line_bot_api.reply_message(event.reply_token,Image_Carousel)




# 執行
if __name__ == "__main__":
    app.run()
