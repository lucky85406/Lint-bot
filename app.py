 
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

def random_int_list(start, stop, length):
	start, stop = (int(start), int(stop)) if start <= stop else (int(stop), int(start))
	length = int(abs(length)) if length else 0
	random_list = []
	for i in range(length):
		random_list.append(random.randint(start, stop))
	return random_list


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
	rx=[]
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

	for tx in range(0,9):
		rx = random_int_list(1,10,1)

	for y in range(0,len(drinklist)):
		if event.message.text == (drinklist[y][0]):
			for x in range(1,len(drinklist[y])):	
				addstr += drinklist[y][x]+"\n"
				print(rx[x-1])
			line_bot_api.reply_message(	
        		event.reply_token,
        		TextSendMessage(text= chr(0x100079)+"your choose->\n"+addstr+"\n"+chr(0x100091)))
	if fistr == "t":
			line_bot_api.reply_message(event.reply_token,message2)





		


	


								


if __name__ == "__main__":
    app.run()
     