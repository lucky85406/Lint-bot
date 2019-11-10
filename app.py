 
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
	drinklist = [["南法小豬格納希粉紅酒","https://i.imgur.com/Rk9AEb3.jpg","bflqu","bilqu","bhlqu","cflqu","cilqu","chlqu"],\
		["阿爾薩斯斐得萊格烏茲塔明娜","https://i.imgur.com/qWt8bca.jpg","bipqu","bhpqu","cipqu","chpqu"],\
		["邁坡酒莊花樣微甜白酒","https://i.imgur.com/JNKuGvw.jpg","dgmqu","demqu","dglqu","delqu"],\
		["邁坡莊園花樣微甜粉紅酒","https://i.imgur.com/jMrI5b3.jpg","bimqu","bgmqu","bfmqu","bilqu","bglqu","bflqu","cimqu","cgmqu","cfmqu","cilqu","cglqu","cflqu","dimqu","dgmqu","dfmqu","dilqu","dglqu","dflqu"],\
		["愛瑜珈慕斯甜白酒","https://i.imgur.com/5XKzEnl.jpg","bimqt","bhmqt","dimqt","dhmqt"],\
		["三風酒之舞白蘇維翁白酒","https://i.imgur.com/VO7cNqz.jpg","cglqu","celqu"],\
		["愛慕拉慕斯卡多甜白酒","https://i.imgur.com/QCZe8BI.jpg","bimqu","bemqu","bilqu","belqu","cimqu","cemqu","cilqu","celqu","dimqu","demqu","dilqu","delqu"],\
		["巴富酒莊慕斯卡白葡萄酒","https://i.imgur.com/mNeE89w.jpg","bilqt","bglqt","dilqt","dglqt"],\
		["巴富酒莊慕斯卡粉紅酒","https://i.imgur.com/x1zn4dv.jpg","bgnqt","benqt","bfnqt","dgnqt","denqt","dfnqt"],\
		["真我系列慕斯卡白酒","https://i.imgur.com/2uwcB1j.jpg","dgmqu","dimqu","demqu","dglqu","dilqu","delqu"],\
		["3人黃金夏多內白酒","https://i.imgur.com/oJzL0ny.jpg","chpqu","cjpqu","cepqu"],\
		["布隆嘉谷莊園蘇維翁白酒","https://i.imgur.com/oHIOiBu.jpg","cgnqt","chnqt","cjnqt"],\
		["貝林格金芬黛粉紅酒","https://i.imgur.com/onL3ap0.jpg","bgnqu","bfnqu","binqu","dgnqu","dfnqu","dinqu"],\
		["地中海波曼桐粉紅酒","https://i.imgur.com/uUjT7di.jpg","dfnqt","dgnqt","denqt"],\
		["JC氣泡酒","https://i.imgur.com/hysqVzu.jpg","bhlqt","chlqt"],\
		["JC粉紅氣泡酒","https://i.imgur.com/qTf8zWF.jpg","dhmqt","dfmqt","dimqt","dhlqt","dflqt","dilqt"],\
		["情盼多倫特粉紅微甜氣泡酒","https://i.imgur.com/5Vtpaid.jpg","dfmqv","demqv"],\
		["克萊喜水蜜桃氣泡酒","https://i.imgur.com/HvSYPWI.jpg","cilqt","dilqt"],\
		["卡迪威氣泡酒","https://i.imgur.com/a3Xf4Sg.jpg","bglqu","bilqu","belqu","cglqu","cilqu","celqu"],\
		["鴕鳥氣泡白酒","https://i.imgur.com/DJAhiAb.jpg","bhnqt","benqt","chnqt","cenqt","dhnqt","denqt"],\
		["蒙多羅氣泡酒","https://i.imgur.com/qzhRDMC.jpg","bhlqu","bilqu","chlqu","cilqu"],\
		["巴塔希慕斯卡多微甜氣泡酒","https://i.imgur.com/m32hSMd.jpg","cimqu"],\
		["威廉水蜜桃氣泡酒","https://i.imgur.com/lfFieF8.jpg","dilqt"],\
		["巴洛亞荔枝氣泡酒","https://i.imgur.com/G1H6PAv.jpg","dhlqt","dglqt"],\
		["巴洛亞雨果氣泡酒","https://i.imgur.com/43DWNQI.jpg","dglqt","delqt"],\
		["米娜多特雷維索氣泡酒","https://i.imgur.com/sT64juU.jpg","cinqv","cenqv"],\
		["坎帕羅拉酒莊氣泡酒","https://i.imgur.com/n4c0uwu.jpg","chmqu","cimqu"],\
		["坎培氣泡白酒","https://i.imgur.com/UBBKTOm.jpg","ailqt","aglqt","cilqt","cglqt","bilqt","bglqt"],\
		["坎培氣泡甜白酒","https://i.imgur.com/bST52xR.jpg","cgnqt","cinqt","cenqt","cjnqt","bgnqt","binqt","benqt","bjnqt","dgnqt","dinqt","denqt","djnqt"],\
		["黃尾袋鼠粉紅氣泡酒","https://i.imgur.com/bJz4dbB.jpg","aflqu","aglqu","ahlqu","cflqu","cglqu","chlqu","bflqu","bglqu","bhlqu"],\
		["康蒂雅不甜氣泡酒","https://i.imgur.com/FeF6rbS.jpg","bilqt","bglqt","cilqt","cglqt"],\
		["慕斯卡朵粉紅氣泡酒","https://i.imgur.com/k0jdEIK.jpg","dfmqu","dfnqu"],\
		["慕斯卡多白氣泡酒","https://i.imgur.com/tGBUoUk.jpg","dhmqv","dgmqv","dhlqv","dglqv"],\
		["蘿朵莊園精選花季氣泡酒","https://i.imgur.com/5TKBPsr.jpg","dinqv","denqv"],\
		["寶蘭美蜜桃氣泡酒","https://i.imgur.com/dPN5yjd.jpg","dilqu","dglqu"],\
		["丹赫氣泡酒","https://i.imgur.com/R0mda2B.jpg","dilqu","dhlqu","dglqu"],\
		["聖塔瑪格莉特氣泡酒","https://i.imgur.com/m3odXh2.jpg","bipqt","cipqt"],\
		["閨蜜粉紅氣泡酒","https://i.imgur.com/KdQp515.jpg","cilqu"],\
		["迴音金芬黛粉紅酒","https://i.imgur.com/2ReNkff.jpg","bflqt","aflqt"],\
		["托斯堤慕斯卡多粉紅微甜氣泡酒","https://i.imgur.com/lGzdAwn.jpg","dilqv","dflqv"],\
		["加泰隆氣泡酒","https://i.imgur.com/IH1RSXg.jpg","binqu","benqu","cinqu","cenqu","dinqu","denqu"],\
		["雀拉微氣泡白酒","https://i.imgur.com/0Hv1Tqa.jpg","bilqt","cilqt"],\
		["露飛諾氣泡酒","https://i.imgur.com/dsUDhJP.jpg","bilqv","bglqv","cilqv","cglqv","dilqv","dglqv"],\
		["托斯堤阿斯堤微甜氣泡酒","https://i.imgur.com/p7QpRVl.jpg","dimqv","dhmqv","demqv"],\
		["托斯堤慕斯卡多微甜白酒","https://i.imgur.com/tF4o01j.jpg","demqv","dhmqv"],\
		["韓可氣泡酒","https://i.imgur.com/d4n1jGi.jpg","cipqu","cepqu"],\
		["康緹氣泡酒","https://i.imgur.com/69OjlaP.jpg","demqu","dhmqu"],\
		["禾富鷹牌氣泡酒","https://i.imgur.com/8WBSaVU.jpg","cilqu","cglqu"],\
		["安德烈氣泡酒","https://i.imgur.com/84PtiGC.jpg","bilqt","bglqt","cilqt","cglqt"],\
		["藍多克凱利蘭仙梭粉紅酒","https://i.imgur.com/x3brhqi.jpg","cenqt","denqt"],\
		["艾思綺幻普羅旺斯粉紅酒","https://i.imgur.com/c471R2W.jpg","cfnqv","cgnqv","cenqv"],\
		["莎特金芬黛粉紅酒","https://i.imgur.com/n6BzIyg.jpg","bfmqt","bgmqt","bemqt","cfmqt","cgmqt","cemqt"],\
		["寶帝加浪漫紅分子氣泡酒(櫻桃)","https://i.imgur.com/v8baLLX.jpg","bfnqv","bhnqv","cfnqv","chnqv"],\
		["寶帝加浪漫金分子氣泡酒(柑橘)","https://i.imgur.com/CW8paiJ.jpg","bgnqv","bhnqv","cgnqv","chnqv","",""],\
		["寶帝加浪漫粉分子氣泡酒(草莓)","https://i.imgur.com/Fx5Lw3z.jpg","bfnqv","benqv","cfnqv","cenqv"],\
		["庫倫斯玫瑰香檳","https://i.imgur.com/hHUCVt3.jpg","bilqv","bglqv","cilqv","cglqv"],\
		["庫倫斯香檳","https://i.imgur.com/kFc17Od.jpg","bilqv","bglqv","cilqv","cglqv","",""],\
		["庫克斯氣泡酒","https://i.imgur.com/DjmE3x3.jpg","bilqt","bglqt","cilqt","cglqt"],\
		["凱芙氣泡甜酒","https://i.imgur.com/KmvsCGa.jpg","dimqu","demqu","dilqu","delqu"],\
		["奇蒂雅遲收甜白葡萄酒","https://i.imgur.com/qQD5OQw.jpg","dimru","demru"],\
		["路易菲利普白牌白蘇微翁白葡萄酒","https://i.imgur.com/nx5dcE6.jpg","cgnru","chnru"],\
		["路易菲利普晚摘白葡萄酒","https://i.imgur.com/CMonCf9.jpg","dgmru","dimru","demru"],\
		["香奈歪脖子夏多內白葡萄酒","https://i.imgur.com/5px7cyk.jpg","bgnru","bhnru"],\
		["玉泉金香白葡萄酒","https://i.imgur.com/VOAD1E9.jpg","bglrt","bilrt","bklrt","cglrt","cilrt","cklrt"],\
		["嘉露金牌慕斯卡白葡萄酒","https://i.imgur.com/mgyVkO5.jpg","dglrt","dilrt"],\
		["囍瑞鳥啼有機白葡萄酒","https://i.imgur.com/fYIz9HJ.jpg","chnru","dhnru","chlru","dhlru"],\
		["黃尾袋鼠夏多內白酒","https://i.imgur.com/w9lDPYm.jpg","bimqu","bjmqu","cimqu","cjmqu"],\
		["黃尾袋鼠粉紅慕斯卡多葡萄酒","https://i.imgur.com/LewcbeI.jpg","cflrt","dflrt","cflqt","dflqt"],\
		["黃尾袋鼠慕斯卡多白葡萄酒","https://i.imgur.com/YqU7kDD.jpg","chlrt","celrt","cflrt","dhlrt","delrt","dflrt","chlqt","celqt","cflqt","dhlqt","delqt","dflqt"],\
		["多利士酒廠艾斯瑪瑞達白葡萄酒","https://i.imgur.com/Y5TRp33.jpg","belrt","bglrt","celrt","cglrt","delrt","dglrt"],\
		["南法小豬夏多內白葡萄酒","https://i.imgur.com/3FD99FT.jpg","bgpru","cgpru"],\
		["聖海倫娜酒廠夏多內白葡萄酒","https://i.imgur.com/PyhIZJV.jpg","chlru","celru","cilru"],\
		["小花微甜麝香白葡萄酒","https://i.imgur.com/mYrcuR2.jpg","demru","dgmru","demqu","dgmqu"],\
		["冰靈黑皮諾微甜粉紅酒","https://i.imgur.com/RUIF55d.jpg","belqu","bflqu","celqu","cflqu"]]

	titletxt = ""
	if event.message.text == "選單":
		line_bot_api.reply_message(	
        		event.reply_token,
        		TextSendMessage(text= chr(0x1F4CC)+"食物\n"+"a.紅 肉 "+chr(0x1F969)+" b.白 肉"+chr(0x1F416)+" c.海 鮮"+chr(0x1F990)+" d.甜 點"+chr(0x1F370)+"\n"+"\n"\
        			+chr(0x1F4CC)+"香氣\n"+"e.花 香"+chr(0x1000B9)+" f.漿 果"+chr(0x1F347)+" g.柑 橘"+chr(0x1F34A)+" h.熱 帶 水 果"+chr(0x1F34D)+" I.淺 色 水 果"+chr(0x1F34E)+" j.香 料"+chr(0x1F343)+" k.土 木 味"+chr(0x1F332)+"\n"+"\n"\
					+chr(0x1F4CC)+"口感\n"+"l.清 香"+chr(0x100039)+" m.甜"+chr(0x1F36C)+" n.圓 潤"+chr(0x1F353)+" o.酸"+chr(0x100098)+" p.濃 厚"+chr(0x100065)+"\n"+"\n"\
					+chr(0x1F4CC)+"通路\n"+"q.家樂福"+" r. 全聯"+" s. Costco"+"\n"+"\n"\
					+chr(0x1F4CC)+"價格\n"+"t.100-350元"+" u.351-600 元"+" v.600 以上"))

	Trans = "https://i.imgur.com/d7DjDmy.png"
	addstr = [""]*10
	addint = 0

	for x in range(0,len(drinklist)):
		for y in range(0,len(drinklist[x])):
			if event.message.text == drinklist[x][y]:
				addstr[addint] = drinklist[x][1]
				addint = addint+1
	for z in range(0,10):
		if addstr[z] == "":
			addstr[z] = Trans										
	for x in range(0,len(drinklist)):
		for y in range(0,len(drinklist[x])):
			if event.message.text == drinklist[x][y]:
				print(len(drinklist))
				Image_Carousel = TemplateSendMessage(
					alt_text='目錄 template',
					template=ImageCarouselTemplate(
					columns=[
						ImageCarouselColumn(
							image_url=addstr[0],
							action=PostbackTemplateAction(
							label=' ',
							text=' ',
							data='action=buy&itemid=1'
								)
							),
						ImageCarouselColumn(
							image_url=addstr[1],
							action=PostbackTemplateAction(
							label=' ',
							text=' ',
							data='action=buy&itemid=2'
								)
							),
						ImageCarouselColumn(
							image_url=addstr[2],
							action=PostbackTemplateAction(
							label=' ',
							text=' ',
							data='action=buy&itemid=3'
								)
							),
						ImageCarouselColumn(
							image_url=addstr[3],
							action=PostbackTemplateAction(
							label=' ',
							text=' ',
							data='action=buy&itemid=4'
								)
							),
						ImageCarouselColumn(
							image_url=addstr[4],
							action=PostbackTemplateAction(
							label=' ',
							text=' ',
							data='action=buy&itemid=5'
								)
							),
						ImageCarouselColumn(
							image_url=addstr[5],
							action=PostbackTemplateAction(
							label=' ',
							text=' ',
							data='action=buy&itemid=6'
								)
							),
						ImageCarouselColumn(
							image_url=addstr[6],
							action=PostbackTemplateAction(
							label=' ',
							text=' ',
							data='action=buy&itemid=7'
								)
							),
						ImageCarouselColumn(
							image_url=addstr[7],
							action=PostbackTemplateAction(
							label=' ',
							text=' ',
							data='action=buy&itemid=8'
								)
							),
						ImageCarouselColumn(
							image_url=addstr[8],
							action=PostbackTemplateAction(
							label=' ',
							text=' ',
							data='action=buy&itemid=9'
								)
							),
						ImageCarouselColumn(
							image_url=addstr[9],
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





		


	


								


if __name__ == "__main__":
    app.run()
     