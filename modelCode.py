from linebot.models import (
    TextSendMessage, CarouselTemplate , BubbleContainer,
    BoxComponent, TextComponent, FlexSendMessage, ImageComponent,
    ButtonComponent, MessageAction, CarouselContainer, SeparatorComponent, IconComponent
)

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
						action=MessageAction(label='花香 (ex:玫瑰花...)',text='花香')
					),
					ButtonComponent(
						margin = 'xl',
						style='secondary',
						color='#FFEE99',
						height='sm',
						action=MessageAction(label='漿果 (ex:櫻桃...)',text='漿果')
					),
					ButtonComponent(
						margin = 'xl',
						style='secondary',
						color='#FFEE99',
						height='sm',
						action=MessageAction(label='柑橘 (ex:檸檬...)',text='柑橘')
					),
					ButtonComponent(
						margin = 'xl',
						style='secondary',
						color='#FFEE99',
						height='sm',
						action=MessageAction(label='熱帶水果 (ex:鳳梨...)',text='熱帶水果')
					),
					ButtonComponent(
						margin = 'xl',
						style='secondary',
						color='#FFEE99',
						height='sm',
						action=MessageAction(label='淺色水果 (ex:杏桃...)',text='淺色水果')
					),
					ButtonComponent(
						margin = 'xl',
						style='secondary',
						color='#FFEE99',
						height='sm',
						action=MessageAction(label='香料 (ex:胡椒...)',text='香料')
					),
					ButtonComponent(
						margin = 'xl',
						style='secondary',
						color='#FFEE99',
						height='sm',
						action=MessageAction(label='土木 (ex:橡木桶...)',text='土木')
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

#選擇清單:
def model(mes):
	fkey = ['紅肉','白肉','海鮮','甜點']
	akey = ['花香','漿果','柑橘','熱帶水果','淺色水果','香料','土木']
	tkey = ['清香','甜','圓潤','酸','濃厚']
	chkey = ['家樂福','全聯','Costco']
	if mes == "Go":
		return food()
	elif mes in fkey:
		return aroma()
	elif mes in akey:
		return taste()
	elif mes in tkey:
		return chain()
	elif mes in chkey:
		return price()
	return TextSendMessage(text="None img")

#圖片按鈕
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

#我的最愛
def mylove(n,ulist):
	a = ulist
	s = []
	alen = len(ulist)
	if alen == 0:
		a.append('None')
		s.append('x')
	else:
		s.append(a[0])
	contents = [BoxComponent(
				margin = 'md',
				layout = 'vertical',
				spacing = 'xs',
				contents = [
					BoxComponent(
						margin = 'xs',
						layout = 'horizontal',
						spacing = 'xs',
						contents = [
							ButtonComponent(
								style='secondary',
								color='#84C1FF',
								flex = 8,
								height='sm',
								action=MessageAction(label=a[0],text='See:'+a[0])
							),
							ButtonComponent(
								style='secondary',
								color='#ECFFFF',
								flex = 4,
								height='sm',
								action=MessageAction(label="刪除",text='re:'+s[0])
							)
						]
					)
				]
			)]
	for x in range(1,alen):
		contents.append(BoxComponent(
				margin = 'md',
				layout = 'vertical',
				spacing = 'xs',
				contents = [
					BoxComponent(
						margin = 'xs',
						layout = 'horizontal',
						spacing = 'xs',
						contents = [
							ButtonComponent(
								style='secondary',
								color='#84C1FF',
								flex = 8,
								height='sm',
								action=MessageAction(label=a[x],text='See:'+a[x])
							),
							ButtonComponent(
								style='secondary',
								color='#ECFFFF',
								flex = 4,
								height='sm',
								action=MessageAction(label='刪除',text='re:'+a[x])
							)
						]
					)
				]
			)
		)
	Carousel = CarouselContainer(
			contents = [
				BubbleContainer(
				header = BoxComponent(
					layout = 'baseline',
					contents = [
						TextComponent(
							text = n +"的最愛",
							weight = 'bold',
							size = 'xl',
							align = 'center'
						)
					]
				),
				body = BoxComponent(
					layout = 'vertical',
					contents = contents
				)
			)
		]
	)

	message = FlexSendMessage(alt_text = "hello",contents = Carousel)
	return message

#顯示圖片
def tenMod(dset):
	contents = []
	if len(dset):
		for x in dset:
			contents.append(BubbleContainer(
					hero = ImageComponent(
								url = x,
								size = 'full',
								align = 'center',
								aspect_ratio = '13:13',
								aspect_mode = 'cover'
					),
					body = BoxComponent(
								layout = 'vertical',
								contents = [
									TextComponent(
										margin = 'md',
										text = dset[x],
										weight = 'bold',
										size = 'md',
										align = 'center'
									),
									SeparatorComponent(
										margin = 'xl',
										color = '#0000FF'
									),
									BoxComponent(
										margin = 'md',
										layout = 'horizontal',
										spacing = 'xs',
										contents = [
											ButtonComponent(
												style='link',
												color='#84C1FF',
												flex = 1,
												height='sm',
												action=MessageAction(label="加入最愛",text='MyLove:'+dset[x])
											)
										]
									)
								]
					)
				)
			)
		Carousel = CarouselContainer(
			contents = contents
		)
		message = FlexSendMessage(alt_text = "hello",contents= Carousel)
	else:
		message = TextSendMessage(text='無符合您輸入的葡萄酒'+chr(0x100010)+"\n"\
										+"請重新選擇"+chr(0x10008D))
	return message

#顯示單張圖片
def single(set1):
	for x in set1:
		mes = BubbleContainer(
					hero = ImageComponent(
						url = set1[x],
						size = 'full',
						align = 'center',
						aspect_ratio = '13:13',
						aspect_mode = 'cover'
					),
					body = BoxComponent(
						layout = 'vertical',
						contents = [
							TextComponent(
								margin = 'md',
								text = x,
								weight = 'bold',
								size = 'md',
								align = 'center'
							),
							SeparatorComponent(
								margin = 'xl',
								color = '#0000FF'
							),
							BoxComponent(
								margin = 'md',
								layout = 'horizontal',
								spacing = 'xs',
								contents = [
									ButtonComponent(
										style='link',
										color='#84C1FF',
										flex = 1,
										height='sm',
										action=MessageAction(label="我的最愛",text='SeeMyLove')
									)
								]
							)
						]
					)
				)
		return FlexSendMessage(alt_text = "hello",contents= mes)
	else:
		return TextSendMessage(text="None img")

#Ukey 選項確認
def ckey(mes):
	fkey = ['紅肉','白肉','海鮮','甜點']
	akey = ['花香','漿果','柑橘','熱帶水果','淺色水果','香料','土木']
	tkey = ['清香','甜','圓潤','酸','濃厚']
	chkey = ['家樂福','全聯','Costco']
	pkey = ['100~350元','351~600元','600元以上']
	if mes in fkey:
		return "ck"
	elif mes in akey:
		return "ck"
	elif mes in tkey:
		return "ck"
	elif mes in chkey:
		return "ck"
	elif mes in pkey:
		return "pk"

	return "none"
