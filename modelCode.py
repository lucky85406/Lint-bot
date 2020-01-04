from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage, TemplateSendMessage, 
    ButtonsTemplate, PostbackTemplateAction, MessageTemplateAction, 
    URITemplateAction, ImageCarouselColumn, ImageCarouselTemplate, 
    ImageSendMessage, URIImagemapAction, MessageImagemapAction, CarouselTemplate ,
    CarouselColumn, MessageImagemapAction, ImagemapArea, ImagemapSendMessage, BaseSize,
    BubbleContainer, BoxComponent, TextComponent, FlexSendMessage, ImageComponent, ButtonComponent,
    URIAction, MessageAction, CarouselContainer, SeparatorComponent, IconComponent
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

#我的最愛
def mylove(n,ulist):
	a = ulist
	b=0
	alen = len(ulist)
	contents = [SeparatorComponent(
				color = '#0000FF'
				),
			BoxComponent(
				margin = 'md',
				layout = 'vertical',
				spacing = 'xs',
				contents = [
					BoxComponent(
						margin = 'md',
						layout = 'horizontal',
						spacing = 'xs',
						contents = [
							ButtonComponent(
								style='link',
								color='#84C1FF',
								flex = 3,
								height='sm',
								action=MessageAction(label=a[0],text='showImg')
							),
							ButtonComponent(
								style='secondary',
								color='#ECFFFF',
								flex = 1,
								height='sm',
								action=MessageAction(label='-',text='-')
							)
						]
					)

				]
			)
		]
	for x in range(1,alen):
		contents.append(BoxComponent(
				margin = 'md',
				layout = 'vertical',
				spacing = 'xs',
				contents = [
					BoxComponent(
						margin = 'md',
						layout = 'horizontal',
						spacing = 'xs',
						contents = [
							ButtonComponent(
								style='secondary',
								color='#84C1FF',
								flex = 3,
								height='sm',
								action=MessageAction(label=a[x],text='showImg')
							),
							ButtonComponent(
								style='secondary',
								color='#84C1FF',
								flex = 1,
								height='sm',
								action=MessageAction(label='-',text='-')
							)
						]
					)
				]
			))
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

#10
def tenMod(img,dset):
	d = dset
	imglist = img
	contents = []
	dlen = len(imglist)
	for x in range(0,dlen):
		contents.append(BubbleContainer(
				hero = ImageComponent(
							url = imglist[x],
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
									text = d[imglist[x]],
									weight = 'bold',
									size = 'md',
									align = 'center'
								),
								TextComponent(
									margin = 'md',
									text = "第一段",
									weight = 'bold',
									size = 'xs',
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
											action=MessageAction(label="加入最愛",text='MyLove:'+d[imglist[x]])
										),
										ButtonComponent(
											margin = 'xxl',
											style='link',
											color='#84C1FF',
											flex = 1,
											height='sm',
											action=MessageAction(label="還沒想到",text='還沒想到')
										)
									]
								)
							]
				)			
			))
	Carousel = CarouselContainer(
		contents = contents		
	)
	message = FlexSendMessage(alt_text = "hello",contents= Carousel)
	return message