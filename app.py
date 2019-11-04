 

from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage, TemplateSendMessage, ButtonsTemplate, PostbackTemplateAction, MessageTemplateAction, URITemplateAction, ImageCarouselColumn, ImageCarouselTemplate
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
	message = TemplateSendMessage(
    alt_text='ImageCarousel template',
    template=ImageCarouselTemplate(
        columns=[
            ImageCarouselColumn(
                image_url='https://comps.canstockphoto.com.tw/abc-%E6%B6%B2%E4%BD%93-%E7%B3%BB%E5%88%97-%E6%95%B8%E5%AD%97-%E6%B0%B4-8-%E7%BE%8E%E5%B7%A5%E5%90%91%E9%87%8F_csp7832476.jpg',
                action=PostbackTemplateAction(
                    label='postback1',
                    text='postback text1',
                    data='action=buy&itemid=1'
                )
            ),
            ImageCarouselColumn(
                image_url='https://www.redhat.com/cms/managed-files/img-rhel-8-hero-mobile.png',
                action=PostbackTemplateAction(
                    label='postback2',
                    text='postback text2',
                    data='action=buy&itemid=2'
                )
            ),
            ImageCarouselColumn(
                image_url='https://blognumbers.files.wordpress.com/2010/09/81.jpg',
                action=PostbackTemplateAction(
                    label='postback3',
                    text='postback text3',
                    data='action=buy&itemid=3'
                )
            ),
            ImageCarouselColumn(
                image_url='data:image/jpeg;base64,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',
                action=PostbackTemplateAction(
                    label='postback4',
                    text='postback text4',
                    data='action=buy&itemid=4'
                )
            )
        ]
    )
)
	line_bot_api.reply_message(event.reply_token, message)

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
     