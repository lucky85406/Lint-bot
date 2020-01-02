from linebot.models import (
	BubbleContainer, BoxComponent, TextComponent, 
	ImageComponent, SeparatorComponent, ButtonComponent, 
	MessageAction, FlexSendMessage, CarouselContainer
)



#測試版型
def testimg():
	Carousel = CarouselContainer(
		contents = [
			BubbleContainer(
				hero = ImageComponent(
							url = 'https://i.imgur.com/YVk6nFG.jpg',
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
									text = "敘述:",
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
											action=MessageAction(label="加入最愛",text='加入最愛')
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
				)
			]		
	)
	message = FlexSendMessage(alt_text = "hello",contents= Carousel)
	return message