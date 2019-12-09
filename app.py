 
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
	# 資料源
	drinklist = [["拉圖城堡紅酒","https://i.imgur.com/diorIgW.jpg","afnsv","ajnsv","bfnsv","bjnsv"],
	["Insignia紅酒","https://i.imgur.com/pSZcQg4.jpg","afpsv","ajpsv","afnsv","ajnsv"],
	["葛拉漢年份波特酒","https://i.imgur.com/o6lYsmx.jpg","dfpsv","djpsv","depsv"],
	["那帕鹿躍費園紅酒","https://i.imgur.com/4tTK1St.jpg","afpsv","ajpsv","bfpsv","bjpsv"],
	["鹿躍酒莊月神紅酒","https://i.imgur.com/Bv3rMtT.jpg","afpsv","aepsv","ajpsv"],
	["陳年法國香檳","https://i.imgur.com/7Le5HPb.jpg","cilsv","cinsv"],
	["酩悅Imperial香檳","https://i.imgur.com/EuOJrma.jpg","cglsv","cilsv","celsv"],
	["仙之谷加拿大冰酒","https://i.imgur.com/PRWOdEo.jpg","dimsv","dhmsv","dipsv","dhpsv"],
	["凱歌皇牌香檳","https://i.imgur.com/oCjPUHl.jpg","cipsv","cjpsv","cilsv","cjlsv"],
	["鹿躍酒莊紅酒","https://i.imgur.com/eRT9RKC.jpg","afpsv","ajpsv"],
	["科克蘭白酒","https://i.imgur.com/xCqVEkW.jpg","bgnsu","binsu","bjnsu","bensu","cgnsu","cinsu","cjnsu","censu"],
	["Hess系列夏多內白酒","https://i.imgur.com/4XvUmxE.jpg","bilsv","belsv","bklsv","cilsv","celsv","cklsv"],
	["羅伯蒙岱維夏多內白酒","https://i.imgur.com/hX6ZC7m.jpg","bglsv","bilsv","belsv","bgnsv","binsv","bensv","cglsv","cilsv","celsv","cgnsv","cinsv","censv"],
	["雲霧之灣夏多內白酒","https://i.imgur.com/RGGDCju.jpg","bgosv","biosv","bgnsv","binsv","cgosv","ciosv","cgnsv","cinsv"],
	["雲霧之灣白蘇維翁白酒","https://i.imgur.com/xROza8f.jpg","cilsv","chlsv","cklsv"],
	["拉菲堡智利精選白葡萄酒","https://i.imgur.com/w4BpTlJ.jpg","bgosu","bhosu","bglsu","bhlsu","cgosu","chosu","cglsu","chlsu"],
	["斯卡特選紅酒","https://i.imgur.com/3IpC6Zn.jpg","afnsv","ajnsv","bfnsv","bjnsv"],
	["貓頭鷹晚摘麗絲玲微甜白酒","https://i.imgur.com/7sNA2MF.jpg","bgmsu","bimsu","cgmsu","cimsu","dgmsu","dimsu"],
	["貓頭鷹霜釀葡萄酒","https://i.imgur.com/9oNKIhw.jpg","bgmsu","bimsu","bemsu","bgpsu","bipsu","bepsu","cgmsu","cimsu","cemsu","cgpsu","cipsu","cepsu","dgmsu","dimsu","demsu","dgpsu","dipsu","depsu"],
	["法茲貴族甜白酒","https://i.imgur.com/kztENPK.jpg","demsu","depsu"],
	["科克蘭吉貢達紅酒","https://i.imgur.com/QsQmz7m.jpg","afpsu","akpsu","ajpsu"],
	["10年波特葡萄酒","https://i.imgur.com/3zmDw2T.jpg","dgmsu","dfmsu","dkmsu","dgpsu","dfpsu","dkpsu"],
	["西域微甜紅酒","https://i.imgur.com/8CjsAwR.jpg","afmsu","aemsu","afpsu","aepsu","dfmsu","demsu","dfpsu","depsu"],
	["卡邦精選紅酒","https://i.imgur.com/GG4UJ7o.jpg","afpsu","ajpsu","akpsu"],
	["夏伯帝畢拉奧紅酒","https://i.imgur.com/9YgNSTR.jpg","afpsu","afmsu"],
	["黑羊紅酒","https://i.imgur.com/IQLThHp.jpg","afpsu","aepsu","ajpsu","afnsu","aensu","ajnsu","bfpsu","bepsu","bjpsu","bfnsu","bensu","bjnsu"],
	["庫尼珍藏紅酒","https://i.imgur.com/gERzNU3.jpg","afnsu","aknsu","ajnsu","bfnsu","bknsu","bjnsu"],
	["鑑賞家珍藏級希哈紅酒","https://i.imgur.com/0EXGIxQ.jpg","afnsu","ajnsu"],
	["風行者黑皮諾紅酒","https://i.imgur.com/mMsKVJU.jpg","afnsv","ajnsv","aensv","bfnsv","bjnsv","bensv"],
	["拜倫酒莊黑皮諾紅酒","https://i.imgur.com/9KqAkA8.jpg","afpsv","aepsv","bfpsv","bepsv"],
	["紫十字經典紅酒","https://i.imgur.com/ok5TVbS.jpg","afpsv","aepsv","afnsv","aensv"],
	["科克蘭俄勒岡州紅酒","https://i.imgur.com/USmsc3E.jpg","aflsv","bflsv"],
	["希洛絲頂級紅酒","https://i.imgur.com/fAocgrY.jpg","afnsu","ajnsu","bfnsu","bjnsu"],
	["坎伯莉雅酒莊黑皮諾紅酒","https://i.imgur.com/9FbBaDT.jpg","afpsu","ajpsu","akpsu","bfpsu","bjpsu","bkpsu","cfpsu","cjpsu","ckpsu"],
	["巴利亨廷頓紅酒","https://i.imgur.com/4cLOdhQ.jpg","afnsu","ajnsu","bfnsu","bjnsu","cfnsu","cjnsu"],
	["Meiomi黑皮諾紅酒","https://i.imgur.com/wtBnX5a.jpg","afpsv","ajpsv","akpsv"],
	["亞斯提微甜氣泡酒","https://i.imgur.com/xZ9s7yU.jpg","bimst","bemst","bilst","belst","cimst","cemst","cilst","celst","dimst","demst","dilst","delst"],
	["B&G酒廠精釀紅酒","https://i.imgur.com/llzWcd8.jpg","afnst","bfnst"],
	["索菲亞阿圖索馬爾貝克紅酒","https://i.imgur.com/PzjFfgN.jpg","afmst","akmst","afnst","aknst"],
	["德雷男爵珍藏紅酒","https://i.imgur.com/OHCYIyk.jpg","afnsu","ajnsu","aflsu","ajlsu","bfnsu","bjnsu","bflsu","bjlsu"],
	["金十字卡本內蘇維翁紅酒","https://i.imgur.com/ndSTccD.jpg","afnsu","ajnsu","bfnsu","bjnsu"],
	["侍酒師紅酒","https://i.imgur.com/J7gDA9I.jpg","afnst","ajnst","bfnst","bjnst"],
	["DON DAVID精選蘇維翁紅酒","https://i.imgur.com/kPrA8HI.jpg","afpst","ajpst","akpst","afnst","ajnst","aknst","bfpst","bjpst","bkpst","bfnst","bjnst","bknst"],
	["拉菲堡精選紅酒","https://i.imgur.com/6ROK3Rl.jpg","afnsv","bfnsv"],
	["西恩那維甜紅酒","https://i.imgur.com/h8Zi0Po.jpg","dfmst","dflst"],
	["蒙大維木橋酒莊紅酒","https://i.imgur.com/vCZiMIs.jpg","afnst","ajnst","aknst","bfnst","bjnst","bknst"],
	["老藤金芬黛紅酒","https://i.imgur.com/CHGtYdO.jpg","afnau","ajnau","aknau"],
	["Line 39黑皮諾紅酒","https://i.imgur.com/2vE9WjY.jpg","aflsu","bflsu"],
	["羅浮古堡紅酒","https://i.imgur.com/g13lnOQ.jpg","afpst","aipst","akpst"],
	["Chianti Colli Senesi DOCG","https://i.imgur.com/prSsfwB.jpg","afost","ajost","afpst","ajpst"],
	["威廉寇黑牌陳年紅酒","https://i.imgur.com/AeyFsdi.jpg","afnsu","ajnsu","aknsu"],
	["科克蘭卡本內蘇維翁紅酒","https://i.imgur.com/6RaoRJ0.jpg","afnsv","ajnsv","dfnsv","djnsv"],
	["科克蘭亞歷山大卡本內蘇維翁紅酒","https://i.imgur.com/cxWxtal.jpg","afnsu","aknsu","dfnsu","dknsu"],
	["達拉巴家窖藏極品CS紅酒","https://i.imgur.com/0byM3CD.jpg","afpsv","ajpsv","afnsv","ajnsv","bfpsv","bjpsv","bfnsv","bjnsv","cfpsv","cjpsv","cfnsv","cjnsv"],
	["羅伯蒙岱維卡本內蘇維翁紅酒","https://i.imgur.com/LitjrPC.jpg","ajpsv","aepsv","ajnsv","aensv"],
	["哥倫比亞火鳳凰紅酒","https://i.imgur.com/2BOzSaQ.jpg","afpsv","aepsv","afnsv","aensv"],
	["多利士精選柯羅那紅酒","https://i.imgur.com/DdGpe83.jpg","afpsu","ajpsu","afnsu","ajnsu","bfpsu","bjpsu","bfnsu","bjnsu","cfpsu","cjpsu","cfnsu","cjnsu"],
	["Freakshow卡本內蘇維翁紅酒","https://i.imgur.com/nx6zuxq.jpg","aipsu","akpsu","ainsu","aknsu","bipsu","bkpsu","binsu","bknsu"],
	["豪帝傳承卡本內蘇維翁紅酒","https://i.imgur.com/6jX5iyO.jpg","afpsv"],
	["哥倫比亞峰卡本內紅酒","https://i.imgur.com/k5iSQEv.jpg","ajpsu","afpsu"],
	["拉菲堡特級卡本內紅酒","https://i.imgur.com/LdycM9K.jpg","afnsv","ajnsv"],
	["B&G 1725波爾多典藏紅酒","https://i.imgur.com/FzTlCSc.jpg","afpst"],
	["侯登堡紅酒","https://i.imgur.com/vn81cGW.jpg","afnsu","bfnsu"],
	["達薩堡紅酒","https://i.imgur.com/l34P7gf.jpg","afpsv","ajpsv"],
	["Oveja Negra釀酒師評選紅酒    ","https://i.imgur.com/XuIRJwb.jpg","afnsu"],
	["蒙帝斯精選紅酒","https://i.imgur.com/DVw9Aez.jpg","ajpsu","akpsu","ajnsu","aknsu"],
	["Chateau Cap De Faugeres紅酒","https://i.imgur.com/W6Vt52H.jpg","afmsu","ajmsu","afnsu","ajnsu"],
	["Cenyth Red Blend紅酒","https://i.imgur.com/dwbYcl6.jpg","afnsv","ajnsv","aensv","bfnsv","bjnsv","bensv"],
	["Chateau Castengnes紅酒","https://i.imgur.com/e14hWgX.jpg","afpsu","akpsu","afnsu","aknsu","bfpsu","bkpsu","bfnsu","bknsu"],
	["卡門薩克城堡紅酒","https://i.imgur.com/LVVRtiD.jpg","afpsv","akpsv","afnsv","aknsv","dfpsv","dkpsv","dfnsv","dknsv"],
	["科克蘭簽名哥倫比亞谷卡本內紅酒","https://i.imgur.com/Xy7d3MK.jpg","afnsu","ajnsu"],
	["克曼沙酒堡紅酒","https://i.imgur.com/YVk6nFG.jpg","afnsv","ajnsv"],
	["威士達美經典蘇維翁紅酒","https://i.imgur.com/Az2yX5N.jpg","afnsu","ajnsu"],
	["派克酒莊95 Block紅酒","https://i.imgur.com/bx1VGuy.jpg","afpsv","akpsv"],
	["赫斯阿羅密蘇維翁紅酒","https://i.imgur.com/1Bu5Tkw.jpg","afpsv","afnsv","cfpsv","cfnsv"],
	["銀十字精選紅酒","https://i.imgur.com/BF8mCIN.jpg","afost","ajost","akost","bfost","bjost","bkost"],
	["BANROCK S.夏多內白酒","https://i.imgur.com/JtBHzZ5.jpg","biost","bkost","ciost","ckost"],
	["莎特酒莊密思嘉甜白酒","https://i.imgur.com/uiQALGw.jpg","dimqt","demqt","dipqt","depqt","dimst","demst","dipst","depst"],
	["麥格根黑標紅酒","https://i.imgur.com/xEQfDT6.jpg","afmst","ajmst","bfmst","bjmst"],
	["美麗花園皮諾塔級紅酒","https://i.imgur.com/s6CmRDf.jpg","afpsu","akpsu","ajpsu","bfpsu","bkpsu","bjpsu"],
	["M.A.N. Vintners Shiraz紅酒","https://i.imgur.com/9kVzrSe.jpg","afpst","ajpst","afnst","ajnst","bfpst","bjpst","bfnst","bjnst"],
	["科克蘭灰皮諾白酒","https://i.imgur.com/uOUgi3z.jpg","cgost","ckost","ceost"],
	["聖瑪格麗特灰皮諾白酒","https://i.imgur.com/cieIFt7.jpg","cgosu","ciosu"],
	["科克蘭夏多內白酒","https://i.imgur.com/NpHxSxV.jpg","bimsu","bhmsu","binsu","bhnsu","cimsu","chmsu","cinsu","chnsu"],
	["查理史密斯功夫女孩麗絲玲白酒","https://i.imgur.com/mIrdIZT.jpg","bgmsu","bimsu","bhmsu","bgpsu","bipsu","bhpsu","cgmsu","cimsu","chmsu","cgpsu","cipsu","chpsu"],
	["莫斯蘭麗絲玲晚摘甜白酒","https://i.imgur.com/0PiNDj5.jpg","biost","beost","ciost","ceost"],
	["MAN Vintners Chenin Blanc 白酒","https://i.imgur.com/5e4vJOd.jpg","bgmst","bhmst","bimst","bgnst","bhnst","binst"],
	["三人紅酒","https://i.imgur.com/oddE2xa.jpg","afmqu","ajmqu","afnqu","ajnqu","bfmqu","bjmqu","bfnqu","bjnqu","afmsu","ajmsu","afnsu","ajnsu","bfmsu","bjmsu","bfnsu","bjnsu"],
	["聖塔瑪格麗特梅洛紅酒","https://i.imgur.com/fKCEod9.jpg","afnst","ajnst","afost","ajost"],
	["加州酒莊紅酒","https://i.imgur.com/pS0aIQn.jpg","afnsu","ainsu","aknsu","bfnsu","binsu","bknsu"],
	["JOOSTENBERG卡本內蘇維翁紅酒","https://i.imgur.com/C4uamo6.jpg","afnst","aknst","bfnst","bknst"],
	["聖瑪莉古典奇揚第紅酒","https://i.imgur.com/vSaEAXZ.jpg","ajnsu","aensu","afnsu","bjnsu","bensu","bfnsu"],
	["露飛諾阿西阿諾經典捷安提紅酒","https://i.imgur.com/8HfyMob.jpg","aensu","afnsu","ajnsu","aknsu","bensu","bfnsu","bjnsu","bknsu"],
	["露飛諾蒙提布希亞諾紅酒","https://i.imgur.com/BzCAwlq.jpg","aensv","afnsv","aknsv","bensv","bfnsv","bknsv"],
	["蒙塔奇諾布魯內洛紅酒","https://i.imgur.com/6btHgSL.jpg","afosv","aeosv","afnsv","aensv","bfosv","beosv","bfnsv","bensv"],
	["科克蘭署名托斯卡納紅酒","https://i.imgur.com/0I6l6mm.jpg","afnsu","ajnsu","aknsu","bfnsu","bjnsu","bknsu"],
	["七宗罪金粉黛紅酒","https://i.imgur.com/eVbMryK.jpg","afosu","ajosu","akosu","bfosu","bjosu","bkosu"],
	["哥倫比亞峰特級莊園梅洛紅酒","https://i.imgur.com/5lTDJIq.jpg","aflsu","ajlsu"],
	["克羅伊木桐城堡波爾多紅酒","https://i.imgur.com/52y6R7k.jpg","ajpsu","akpsu","bjpsu","bkpsu"],
	["羅柏蒙岱維梅洛紅酒","https://i.imgur.com/TI3fKDA.jpg","ajpsv","afpsv","ajnsv","afnsv"]]


	# 根據line manager 內設定做判斷
	judge = False
	meetjud = False
	judstr = event.message.text
	if judstr == "選單" or judstr == "？" or judstr == "?":
		judge = True;

	# 根據資料有無符合選項
	for x in range(0,len(drinklist)):
		for y in range(2,len(drinklist[x])):
			if judstr == drinklist[x][y]:
				meetjud = True;

	# 判斷使用者輸入無符合選項時
	if judge == False and meetjud == False:
		line_bot_api.reply_message(	
				event.reply_token,
				TextSendMessage(text= "感謝您的訊息"+chr(0x100008)+"\n"\
									+"很抱歉無法搜尋到符合您輸入的選項！!\n"\
									+chr(0x26A0)+chr(0xFE0F)+"請確認前後是否有空格存在"+chr(0x10002E)))
	# 如果有符合的選項
	if meetjud == True:
		Trans = "https://i.imgur.com/d7DjDmy.png"
		addstr = [""]*10
		addint = 0
		rint =0
		ranlen =0;
		rancon = [0]*10
		# 先找尋所有符合使用者輸入的選項數目
		for x in range(0,len(drinklist)):
			for y in range(0,len(drinklist[x])):
				if judstr == drinklist[x][y]:
					ranlen =ranlen+1;
		# 建立陣列存放所有符合項目
		ranint = [0]*ranlen
		for x in range(0,len(drinklist)):
			for y in range(0,len(drinklist[x])):
				if judstr == drinklist[x][y]:
					ranint[rint] = x
					rint = rint+1;
		# 將符合的選項圖片url顯示圖片的陣列中(如果項目超過10個，隨機產生10個)
		if len(ranint) > 10:
			rancon = random.sample(ranint,10)
			print(rancon)
			for x in range(0,len(rancon)):
				a = rancon[x]
				for y in range(0,len(drinklist[a])):
					if judstr == drinklist[a][y]:
						addstr[addint] = drinklist[a][1]
						addint = addint+1
		else:
			for x in range(0,len(drinklist)):
				for y in range(0,len(drinklist[x])):
					if judstr == drinklist[x][y]:
						addstr[addint] = drinklist[x][1]
						addint = addint+1
		# 如果陣列中出現空的情況放入一張透明圖片									
		for z in range(0,10):
			if addstr[z] == "":
				addstr[z] = Trans
		# 將所有圖片陣列顯示出來										
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
#測試輸出文件
f = open("test.txt","r")
for line in f:
	print(line)
f.close()




		


	


								

#執行
if __name__ == "__main__":
    app.run()
     