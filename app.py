 

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
	message[0] = ImageSendMessage(
    original_content_url='https://i.screenshot.net/eqdppak',
    preview_image_url='https://i.screenshot.net/eqdppak'
	)
	line_bot_api.reply_message(event.reply_token,message[0])


	#foodlist = [["a","白肉"], ["b","紅肉"],["c","海鮮"],["d","甜點"]]
	#aromalist = [["e","花香"], ["f","漿果"],["g","柑橘"],["h","熱帶水果"],["i","淺色水果"],["j","香料"]]
	#tastelist = [["k","清香"], ["l","甜"],["m","圓潤"],["n","濃厚"]]
	#pacelist = [["o","家樂福"]]
	#pricelist = [["p","351~600"],["q","100~350"],["r","600+"]]

	#drinklist = [["aekop","冰靈麗絲玲黑皮諾微甜粉紅酒","義大利愛茉拉慕斯卡多甜白酒","南法小豬格納希粉紅酒","義大利若林慕斯卡微氣泡白酒","隆河紫羅蘭風土科倫坡白酒","德國丹赫1794慕斯卡白酒"]\
	#			,["afkop","冰靈麗絲玲黑皮諾微甜粉紅酒","黃尾袋鼠粉紅氣泡酒","邁坡莊園花漾微甜粉紅酒","南法小豬格納希粉紅酒"]]
	#addstr=''
	#for y in range(0,2):
		#if event.message.text == (drinklist[y][0]):
			#for x in range(1,len(drinklist[y])):
				#addstr += drinklist[y][x]+"\n"
			#line_bot_api.reply_message(	
        		#event.reply_token,
        		#TextSendMessage(text="your choose->\n"+addstr))



		


	


								


if __name__ == "__main__":
    app.run()
     