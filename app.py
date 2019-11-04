 

from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
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
	line_bot_api.reply_message(event.reply_token, message)
	message=TemplateSendMessage(
	alt_text='Buttons template',
	template=ButtonsTemplate(
		thumbnail_image_url='https://example.com/image.jpg',
		title='Menu',
		text='Please select',
		actions=[
		PostbackTemplateAction(
			label='postback',
			text='postback text',
			data='action=buy&itemid=1'
			),
		MessageTemplateAction(
			label='message',
			text='message text'
			),
		URITemplateAction(
			label='uri',
			uri='http://example.com/'
			)
		]
		)
	)


		


	


								


if __name__ == "__main__":
    app.run()
     