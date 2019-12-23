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
    URIAction, MessageAction
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
	elif ukey =="menu":
		Carousel_template = TemplateSendMessage(
		alt_text='Carousel template',
		template=CarouselTemplate(
		columns=[
			CarouselColumn(
				title='食物',				
				text='1',
				thumbnail_image_url='https://i.imgur.com/LmdGm99.png',
				actions=[
					MessageTemplateAction(
						label='紅肉',
						text='a'
					),
					MessageTemplateAction(
						label='白肉',
						text='b'
					)
				]
			),
			CarouselColumn(
				title='食物',				
				text='2',
				thumbnail_image_url='https://i.imgur.com/LmdGm99.png',
				actions=[
					MessageTemplateAction(
						label='海鮮',
						text='c'
					),
					MessageTemplateAction(
						label='甜點',
						text='d'
					)
				]
			)
		]
	)
	)
		line_bot_api.reply_message(event.reply_token,Carousel_template)
	elif ukey =="menu2":
		Carousel_template = TemplateSendMessage(
		alt_text='Carousel template',
		template=CarouselTemplate(
		columns=[
			CarouselColumn(
				thumbnail_image_url='https://i.imgur.com/LmdGm99.png',
				title='香氣',
				text='1',
				actions=[
					MessageTemplateAction(
						label='花香',
						text='e'
					),
					MessageTemplateAction(
						label='漿果',
						text='f'
					),
					MessageTemplateAction(
						label='柑橘',
						text='g'
					)
				]
			),
			CarouselColumn(
				thumbnail_image_url='https://i.imgur.com/LmdGm99.png',
				title='香氣',
				text='2',
				actions=[
					MessageTemplateAction(
						label='熱帶水果',
						text='h'
					),
					MessageTemplateAction(
						label='淺色水果',
						text='i'
					),
					MessageTemplateAction(
						label='X',
						text='null'
					)
				]
			),
			CarouselColumn(
				thumbnail_image_url='https://i.imgur.com/LmdGm99.png',
				title='香氣',
				text='3',
				actions=[
					MessageTemplateAction(
						label='香料',
						text='j'
					),
					MessageTemplateAction(
						label='土木',
						text='k'
					),
					MessageTemplateAction(
						label='X',
						text='null'
					)
				]
			)
		]
	)
	)
		line_bot_api.reply_message(event.reply_token,Carousel_template)
	elif ukey =="menu3":
		Carousel_template = TemplateSendMessage(
		alt_text='Carousel template',
		template=CarouselTemplate(
		columns=[
			CarouselColumn(
				thumbnail_image_url='https://i.imgur.com/LmdGm99.png',
				title='口感',
				text='1',
				actions=[
					MessageTemplateAction(
						label='清香',
						text='l'
					),
					MessageTemplateAction(
						label='甜',
						text='m'
					),
					MessageTemplateAction(
						label='圓潤',
						text='n'
					)
				]
			),
			CarouselColumn(
				thumbnail_image_url='https://i.imgur.com/LmdGm99.png',
				title='口感',
				text='2',
				actions=[
					MessageTemplateAction(
						label='酸',
						text='o'
					),
					MessageTemplateAction(
						label='濃厚',
						text='p'
					),
					MessageTemplateAction(
						label='X',
						text='null'
					)
				]
			)
		]
	)
	)
		line_bot_api.reply_message(event.reply_token,Carousel_template)
	elif ukey =="menu4":
		Carousel_template = TemplateSendMessage(
		alt_text='Carousel template',
		template=CarouselTemplate(
		columns=[
			CarouselColumn(
				thumbnail_image_url='https://i.imgur.com/LmdGm99.png',
				title='通路',
				text='1',
				actions=[
					MessageTemplateAction(
						label='家樂福',
						text='q'
					),
					MessageTemplateAction(
						label='全聯',
						text='r'
					),
					MessageTemplateAction(
						label='Costco',
						text='s'
					)
				]
			)
		]
	)
	)
		line_bot_api.reply_message(event.reply_token,Carousel_template)
	elif ukey =="menu5":
		Carousel_template = TemplateSendMessage(
		alt_text='Carousel template',
		template=CarouselTemplate(
		columns=[
			CarouselColumn(
				thumbnail_image_url='https://i.imgur.com/LmdGm99.png',
				title='價格',
				text='1',
				actions=[
					MessageTemplateAction(
						label='100~350元',
						text='t'
					),
					MessageTemplateAction(
						label='351~600元',
						text='u'
					),
					MessageTemplateAction(
						label='600元以上',
						text='v'
					)
				]
			)
		]
	)
	)
		line_bot_api.reply_message(event.reply_token,Carousel_template)
	else:
		user_id = event.source.user_id
		inMes(user_id,ukey)
'''
	if event.message.text == "我要測試":
		message = FlexSendMessage(
			alt_text = "hello",
			template = CarouselTemplate(
			contents = [
					CarouselColumn(
						BubbleContainer(
							header = BoxComponent(
								layout = 'baseline',
								contents = [
									TextComponent(
										text = '示範',
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
										action=MessageAction(label='設定起始數字',text='測試')
									),
									ButtonComponent(
										style='secondary',
										color='#FFEE99',
										height='sm',
										action=MessageAction(label='設定起始數字',text='測試')
									),
									ButtonComponent(
										style='secondary',
										color='#FFEE99',
										height='sm',
										action=MessageAction(label='設定起始數字',text='測試')
									),
									ButtonComponent(
										style='secondary',
										color='#FFEE99',
										height='sm',
										action=MessageAction(label='設定起始數字',text='測試')
									),
									ButtonComponent(
										style='secondary',
										color='#FFEE99',
										height='sm',
										action=MessageAction(label='設定起始數字',text='測試')
									),
									ButtonComponent(
										style='secondary',
										color='#FFEE99',
										height='sm',
										action=MessageAction(label='設定起始數字',text='測試')
									),
									ButtonComponent(
										style='secondary',
										color='#FFEE99',
										height='sm',
										action=MessageAction(label='設定起始數字',text='測試')
									)										
								]
							),
							footer = BoxComponent(
								layout = 'baseline',
								contents = [
									TextComponent(
										text = '示範',
										weight = 'bold',
										size = 'xxl',
										flex =2,
										align = 'center'
									)
								]
							)		
						)

					),
					CarouselColumn(
						BubbleContainer(
							header = BoxComponent(
								layout = 'baseline',
								contents = [
									TextComponent(
										text = '示範',
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
										action=MessageAction(label='設定起始數字',text='測試')
									),
									ButtonComponent(
										style='secondary',
										color='#FFEE99',
										height='sm',
										action=MessageAction(label='設定起始數字',text='測試')
									),
									ButtonComponent(
										style='secondary',
										color='#FFEE99',
										height='sm',
										action=MessageAction(label='設定起始數字',text='測試')
									),
									ButtonComponent(
										style='secondary',
										color='#FFEE99',
										height='sm',
										action=MessageAction(label='設定起始數字',text='測試')
									),
									ButtonComponent(
										style='secondary',
										color='#FFEE99',
										height='sm',
										action=MessageAction(label='設定起始數字',text='測試')
									),
									ButtonComponent(
										style='secondary',
										color='#FFEE99',
										height='sm',
										action=MessageAction(label='設定起始數字',text='測試')
									),
									ButtonComponent(
										style='secondary',
										color='#FFEE99',
										height='sm',
										action=MessageAction(label='設定起始數字',text='測試')
									)										
								]
							),
							footer = BoxComponent(
								layout = 'baseline',
								contents = [
									TextComponent(
										text = '示範',
										weight = 'bold',
										size = 'xxl',
										flex =2,
										align = 'center'
									)
								]
							)		
						)
					)
				]
			)
			)
		line_bot_api.reply_message(event.reply_token,message)


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
