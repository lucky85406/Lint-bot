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


from dataList import (dataList, dataOpen, dataInput)
import random
import time  # 待會會取時間


app = Flask(__name__)

line_bot_api = LineBotApi(
    'SE2ze7zRWntpaA+vp22pDMAm/BI93Pti5qNo3wZ0NOOHO11HSm+ffoSdWxKXw7cEggPiLBQK0XZ87QtMp3bVn4MDTDGBRktZO10RvV+s8CMLyL33aonQyn8dUBSDjZ2vbsulJmZdnykXosjs9dhoSAdB04t89/1O/w1cDnyilFU=')
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
    tStart = time.time()
    # 根據line manager 內設定做判斷
    judge = False
    meetjud = False
    judstr = event.message.text
    pngurl = "https://gss0.baidu.com/-vo3dSag_xI4khGko9WTAnF6hhy/zhidao/wh%3D600%2C800/sign=be7b6ffbd462853592b5da27a0df5afe/0b46f21fbe096b63d30f4b590d338744ebf8aca0.jpg"
    data = dataList(judstr)
    dlen = len(data)
    dlist = list(data)

    if dlen < 10:
        for x in range(dlen, 10):
            dlist.append(pngurl)
    # 打印資料
    '''
	dataOpen(judstr)
	if judstr == "show":
		line_bot_api.reply_message(	
						event.reply_token,
						TextSendMessage(text= dataOpen(judstr)))
	'''

    if judstr == "選單" or judstr == "？" or judstr == "?":
        judge = True
    elif dlen == 0:
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text="感謝您的訊息" + chr(0x100008) + "\n"
                            + "很抱歉無法搜尋到符合您輸入的選項！!\n"
                            + chr(0x26A0) + chr(0xFE0F) + "請確認前後是否有空格存在" + chr(0x10002E)))
    elif dlen > 0:
        # 將所有圖片陣列顯示出來
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
        tEnd = time.time()
        print("It cost %f sec" % (tEnd - tStart))
        line_bot_api.reply_message(event.reply_token, Image_Carousel)



# 執行
if __name__ == "__main__":
    app.run()
