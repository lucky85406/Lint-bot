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
from datalist import(dataList)
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

# 食物清單
def food():
	mes = BubbleContainer(
			header = BoxComponent(
				layout = 'baseline',
				contents = [
					TextComponent(
						text = 'Q1:搭配食物',
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
	message = FlexSendMessage(alt_text = "hello",contents = mes)
	return message

# 香氣清單
def aroma():
	mes = BubbleContainer(
			header = BoxComponent(
				layout = 'baseline',
				contents = [
					TextComponent(
						text = 'Q2:喜歡的香氣',
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
						action=MessageAction(label='花香',text='花香')
					),
					ButtonComponent(
						margin = 'xl',
						style='secondary',
						color='#FFEE99',
						height='sm',
						action=MessageAction(label='漿果',text='漿果')
					),
					ButtonComponent(
						margin = 'xl',
						style='secondary',
						color='#FFEE99',
						height='sm',
						action=MessageAction(label='柑橘',text='柑橘')
					),
					ButtonComponent(
						margin = 'xl',
						style='secondary',
						color='#FFEE99',
						height='sm',
						action=MessageAction(label='熱帶水果',text='熱帶水果')
					),
					ButtonComponent(
						margin = 'xl',
						style='secondary',
						color='#FFEE99',
						height='sm',
						action=MessageAction(label='淺色水果',text='淺色水果')
					),
					ButtonComponent(
						margin = 'xl',
						style='secondary',
						color='#FFEE99',
						height='sm',
						action=MessageAction(label='香料',text='香料')
					),
					ButtonComponent(
						margin = 'xl',
						style='secondary',
						color='#FFEE99',
						height='sm',
						action=MessageAction(label='土木',text='土木')
					)																	
				]
			)		
		)
	message = FlexSendMessage(alt_text = "hello",contents = mes)
	return message

# 口感清單
def taste():
	mes = BubbleContainer(
			header = BoxComponent(
				layout = 'baseline',
				contents = [
					TextComponent(
						text = 'Q3:想要的口感',
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
						action=MessageAction(label='清香',text='清香')
					),
					ButtonComponent(
						margin = 'xl',
						style='secondary',
						color='#FFEE99',
						height='sm',
						action=MessageAction(label='甜',text='甜')
					),
					ButtonComponent(
						margin = 'xl',
						style='secondary',
						color='#FFEE99',
						height='sm',
						action=MessageAction(label='圓潤',text='圓潤')
					),
					ButtonComponent(
						margin = 'xl',
						style='secondary',
						color='#FFEE99',
						height='sm',
						action=MessageAction(label='酸',text='酸')
					),
					ButtonComponent(
						margin = 'xl',
						style='secondary',
						color='#FFEE99',
						height='sm',
						action=MessageAction(label='濃厚',text='濃厚')
					)																	
				]
			)		
		)
	message = FlexSendMessage(alt_text = "hello",contents = mes)
	return message
#通路
def chain():
	mes = BubbleContainer(
			header = BoxComponent(
				layout = 'baseline',
				contents = [
					TextComponent(
						text = 'Q4:想購買的通路',
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
						action=MessageAction(label='家樂福',text='家樂福')
					),
					ButtonComponent(
						margin = 'xl',
						style='secondary',
						color='#FFEE99',
						height='sm',
						action=MessageAction(label='全聯',text='全聯')
					),
					ButtonComponent(
						margin = 'xl',
						style='secondary',
						color='#FFEE99',
						height='sm',
						action=MessageAction(label='Costco',text='Costco')
					)																	
				]
			)		
		)
	message = FlexSendMessage(alt_text = "hello",contents = mes)
	return message

#價格清單
def price():
	mes = BubbleContainer(
			header = BoxComponent(
				layout = 'baseline',
				contents = [
					TextComponent(
						text = 'Q5:價格預算',
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
						action=MessageAction(label='100~350元',text='100~350元')
					),
					ButtonComponent(
						margin = 'xl',
						style='secondary',
						color='#FFEE99',
						height='sm',
						action=MessageAction(label='351~600元',text='351~600元')
					),
					ButtonComponent(
						margin = 'xl',
						style='secondary',
						color='#FFEE99',
						height='sm',
						action=MessageAction(label='600元以上',text='600元以上')
					)																	
				]
			)		
		)
	message = FlexSendMessage(alt_text = "hello",contents = mes)
	return message

#顯示圖片
def showimg():
	mes = BubbleContainer(
			body = BoxComponent(
				layout = 'vertical',
				spacing = 'xs',
				contents = [
					ButtonComponent(
						style='secondary',
						color='#FFEE99',
						height='sm',
						action=MessageAction(label='ShowImg',text='showImg')
					)																	
				]
			)		
		)
	message = FlexSendMessage(alt_text = "hello",contents = mes)
	return message

#測試版型
def testimg():
	mes = BubbleContainer(
			header = BoxComponent(
				layout = 'baseline',
				contents = [
					TextComponent(
						text = 'Q5:價格預算',
						weight = 'bold',
						size = 'xxl',
						flex =2,
						align = 'center'
					)
				]
			),
			hero = ImageComponent(
				url = 'https://i.imgur.com/A5TeDg0.png',
				size = 'full',
				align = 'center',
				aspect_ratio = '792:555',
				aspect_mode = 'cover'
			),
			body = BoxComponent(
				layout = 'vertical',
				spacing = 'xs',
				contents = [
					SeparatorComponent(
						margin = 'lg',
						color = '#0000FF'
					),
					TextComponent(
						text = '敘述:故事敘述法，就是像講故事一樣,',
						weight = 'bold',
						size = 'xs',	
						align = 'start',
						color = '#FF00FF'
					),
					TextComponent(
						text = '	把事情的前因後果、來龍去脈、出場人物、',
						weight = 'bold',
						size = 'xs',	
						align = 'start',
						color = '#FF00FF'
					),
					TextComponent(
						text = '	發展過程、結局和解決方案都說明白的一種方法。',
						weight = 'bold',
						size = 'xs',	
						align = 'start',
						color = '#FF00FF'
					)
				]
			)
		)
	message = FlexSendMessage(alt_text = "hello",contents = mes)
	return message

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
	#!!!!!!!!!!!!!!!!!這裡有ID
	user_id = event.source.user_id
	
	

	if event.message.text == "showshow":
		line_bot_api.reply_message(event.reply_token,showimg())
	elif ukey == "紅肉" or ukey =="白肉" or ukey =="海鮮" or ukey =="甜點":
		user_id = event.source.user_id
		inMes(user_id,conversionCode(ukey))
		line_bot_api.reply_message(event.reply_token,aroma())
	elif ukey == "花香" or ukey =="漿果" or ukey =="柑橘" or ukey =="熱帶水果" or ukey =="淺色水果" or ukey =="香料" or ukey =="土木":
		user_id = event.source.user_id
		inMes(user_id,conversionCode(ukey))
		line_bot_api.reply_message(event.reply_token,taste())
	elif ukey == "清香" or ukey =="甜" or ukey =="圓潤" or ukey =="酸" or ukey =="濃厚":
		user_id = event.source.user_id
		inMes(user_id,conversionCode(ukey))
		line_bot_api.reply_message(event.reply_token,chain())
	elif ukey == "家樂福" or ukey =="全聯" or ukey =="Costco":
		user_id = event.source.user_id
		inMes(user_id,conversionCode(ukey))
		line_bot_api.reply_message(event.reply_token,price())
	elif ukey =="100~350元" or ukey =="351~600元" or ukey =="600元以上":
		user_id = event.source.user_id
		inMes(user_id,conversionCode(ukey))
	else:
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
			line_bot_api.reply_message(event.reply_token,food())
		elif ukey =="showImg":
			user_id = event.source.user_id
			data = dataList(showMes(user_id))
			dlist = list(data)
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
			line_bot_api.reply_message(event.reply_token,Image_Carousel)
		elif ukey =="testimg":
			line_bot_api.reply_message(event.reply_token,testimg())



# 執行
if __name__ == "__main__":
    app.run()
