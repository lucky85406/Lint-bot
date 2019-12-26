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
from utoken import(go,inMes,showMes)
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
	'''
	ukey = event.message.text
	#!!!!!!!!!!!!!!!!!這裡有ID
	user_id = event.source.user_id
	
	if ukey == "show":
		user_id = event.source.user_id
		a = showMes(user_id)
		if a == "1":
			line_bot_api.reply_message(	
				event.reply_token,
				TextSendMessage(text= "null"))
		else:
			line_bot_api.reply_message(	
				event.reply_token,
				TextSendMessage(text= showMes(user_id)))
	elif ukey =="go":
		user_id = event.source.user_id
		go(user_id)
	else:
		user_id = event.source.user_id
		inMes(user_id,ukey)
'''
	if event.message.text == "我要測試":
		ISM = CarouselContainer(
			contents = [
				BubbleContainer(
					header = BoxComponent(
						layout = 'baseline',
						contents = [
							TextComponent(
								text = 'Q1:搭配食物?',
								weight = 'bold',
								size = 'xxl',
								flex =2,
								align = 'center'
							)
						]
					),
					body = BoxComponent(
						layout = 'vertical',
						spacing = 'xs',
						contents = [
							ButtonComponent(
								style='secondary',
								color='#FFEE99',
								height='sm',
								action=MessageAction(label='紅肉',text='紅肉')
							),
							ButtonComponent(
								margin = 'xl',
								style='secondary',
								color='#FFEE99',
								height='sm',
								action=MessageAction(label='白肉',text='白肉')
							),
							ButtonComponent(
								margin = 'xl',
								style='secondary',
								color='#FFEE99',
								height='sm',
								action=MessageAction(label='海鮮',text='海鮮')
							),
							ButtonComponent(
								margin = 'xl',
								style='secondary',
								color='#FFEE99',
								height='sm',
								action=MessageAction(label='甜點',text='甜點')
							)																	
						]
					)		
				)
			]
		)
		message = FlexSendMessage(alt_text = "hello",contents=ISM)
		line_bot_api.reply_message(event.reply_token,message)


# 執行
if __name__ == "__main__":
    app.run()
