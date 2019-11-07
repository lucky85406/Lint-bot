 
import random

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
	#line_bot_api.reply_message(event.reply_token,message2)
	foodlist = [["a","白肉"], ["b","紅肉"],["c","海鮮"],["d","甜點"]]
	aromalist = [["e","花香"], ["f","漿果"],["g","柑橘"],["h","熱帶水果"],["i","淺色水果"],["j","香料"]]
	tastelist = [["k","清香"], ["l","甜"],["m","圓潤"],["n","濃厚"]]
	pacelist = [["o","家樂福"]]
	pricelist = [["p","351~600"],["q","100~350"],["r","600+"]]
	drinklist = [["test1","c01.美國加州庫克斯氣泡酒","c02.法國凱芙氣泡甜酒","c03.黃尾袋鼠夏多內白酒","a01.奇蒂雅遲收甜白葡萄酒","a13.冰靈麗絲玲白葡萄酒"]\
				,["test2","c04.冰靈黑皮諾微甜粉紅酒","a03.香奈歪脖子夏多內白葡萄酒","a09.多力士酒廠艾斯瑪瑞達白葡萄酒","a10.南法小豬夏多內白葡萄酒","a11.聖海倫娜酒廠夏多內白葡萄酒"]\
				,["test3","a02.路易菲利普白牌白蘇雅維翁白葡萄酒","a04.黃玉帛金香白葡萄酒","a05.奇蒂雅遲收甜白葡萄酒","a06.囍瑞鳥啼有機白葡萄酒"]\
				,["test4","a07.黃尾袋鼠粉紅慕斯卡多葡萄酒.","a08.黃尾袋鼠慕斯卡多白葡萄酒","a12.小花瑞田麝香白葡萄酒"]]
	urllistc = [["c01","https://i.screenshot.net/yj2k2h5"],["c02","https://i.screenshot.net/p8w2waq"],["c03","https://i.screenshot.net/e5dplf0"],["c04","https://i.screenshot.net/03q81fj"]]
	urllista = [["a01","https://i.screenshot.net/n2k9kud"],["a02","https://i.screenshot.net/wrk2oc9"],["a03","https://i.screenshot.net/r6wzwsk"],["a04","https://i.screenshot.net/569qkae"]\
				,["a05","https://i.screenshot.net/690vda1"],["a06","https://i.screenshot.net/0xn1lar"],["a07","https://i.screenshot.net/pwopeag"],["a08","https://i.screenshot.net/6zjxkhr"]\
				,["a09","https://i.screenshot.net/r04p2cp"],["a10","https://i.screenshot.net/7od49cq"],["a11","https://i.screenshot.net/77r6gi7"],["a12","https://i.screenshot.net/nyzkqbz"]\
				,["a13","https://i.screenshot.net/wrk2oc9"]]
	addstr=''
	urlstr=''
	fistr=''
	randstr=''
	slection_len=0
	for y in range(0,len(drinklist)):
		if event.message.text == (drinklist[y][0]):
			randstr="t"
			rx = [0]*(len(drinklist[y])-1)
			for x in range(0,len(drinklist[y])-1):
				slection_len = len(drinklist[y])
				rx[x] = x+1
	if randstr == "t":
		print(slection_len)
		rx = random.sample(rx,(slection_len)-1)
		print(rx)
	for cl in range(0,len(urllistc)):	
		if event.message.text == urllistc[cl][0]:
			urlstr = urllistc[cl][1]
			fistr = "t"
	for al in range(0,len(urllista)):
		if event.message.text == urllista[al][0]:
			urlstr = urllista[al][1] 	
			fistr = "t"	
	message2 = ImageSendMessage(
    original_content_url=urlstr,
    preview_image_url=urlstr
	)

	for y in range(0,len(drinklist)):
		if event.message.text == (drinklist[y][0]):
			for x in range(1,len(drinklist[y])):	
				addstr += drinklist[y][rx[x-1]]+"\n"
			line_bot_api.reply_message(	
        		event.reply_token,
        		TextSendMessage(text= chr(0x100079)+"your choose->\n"+addstr+chr(0x100091)))

	if fistr == "t":
			line_bot_api.reply_message(event.reply_token,message2)

	if event.message.text == "Image Carousel":
		Image_Carousel = TemplateSendMessage(
			alt_text='目錄 template',
			template=ImageCarouselTemplate(
			columns=[
				ImageCarouselColumn(
					image_url='data:image/png;base64,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',
					action=PostbackTemplateAction(
					label='postback1',
					text='postback text1',
					data='action=buy&itemid=1'
						)
					),
				ImageCarouselColumn(
					image_url='https://i.screenshot.net/p8w2waq',
					action=PostbackTemplateAction(
					label='postback2',
					text='postback text2',
					data='action=buy&itemid=2'
						)
					)
				]
			)
		)
	line_bot_api.reply_message(event.reply_token,Image_Carousel)		





		


	


								


if __name__ == "__main__":
    app.run()
     