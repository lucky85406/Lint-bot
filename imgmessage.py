from linebot.models import (
	BubbleContainer, BoxComponent, TextComponent, 
	ImageComponent, SeparatorComponent, ButtonComponent, 
	MessageAction, FlexSendMessage, CarouselContainer
)

def test():
	a = {BubbleContainer(
				hero = ImageComponent(
							url = 'https://i.imgur.com/diorIgW.jpg',
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
									text = '拉圖城堡紅酒',
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
											action=MessageAction(label="加入最愛",text='MyLove:'+'拉圖城堡紅酒')
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
			)}
	return list(a)[0]

#10
def tenMod(img,dset):
	d = dset
	imglist = img
	Carousel = CarouselContainer(
		contents = [
			#1
			test(),
			#2
			BubbleContainer(
				hero = ImageComponent(
							url = imglist[1],
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
									text = d[imglist[1]],
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
											action=MessageAction(label="加入最愛",text='MyLove:'+d[imglist[1]])
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
			),#3
			BubbleContainer(
				hero = ImageComponent(
							url = imglist[2],
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
									text = d[imglist[2]],
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
											action=MessageAction(label="加入最愛",text='MyLove:'+d[imglist[2]])
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
			),#4
			BubbleContainer(
				hero = ImageComponent(
							url = imglist[3],
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
									text = d[imglist[3]],
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
											action=MessageAction(label="加入最愛",text='MyLove:'+d[imglist[3]])
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
			),#5
			BubbleContainer(
				hero = ImageComponent(
							url = imglist[4],
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
									text = d[imglist[4]],
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
											action=MessageAction(label="加入最愛",text='MyLove:'+d[imglist[4]])
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
			),#6
			BubbleContainer(
				hero = ImageComponent(
							url = imglist[5],
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
									text = d[imglist[5]],
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
											action=MessageAction(label="加入最愛",text='MyLove:'+d[imglist[5]])
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
			),#7
			BubbleContainer(
				hero = ImageComponent(
							url = imglist[6],
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
									text = d[imglist[6]],
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
											action=MessageAction(label="加入最愛",text='MyLove:'+d[imglist[6]])
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
			),#8
			BubbleContainer(
				hero = ImageComponent(
							url = imglist[7],
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
									text = d[imglist[7]],
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
											action=MessageAction(label="加入最愛",text='MyLove:'+d[imglist[7]])
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
			),#9
			BubbleContainer(
				hero = ImageComponent(
							url = imglist[8],
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
									text = d[imglist[8]],
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
											action=MessageAction(label="加入最愛",text='MyLove:'+d[imglist[8]])
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
			),#10
			BubbleContainer(
				hero = ImageComponent(
							url = imglist[9],
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
									text = d[imglist[9]],
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
											action=MessageAction(label="加入最愛",text='MyLove:'+d[imglist[9]])
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
#9
def ninMod():
	Carousel = CarouselContainer(
		contents = [
			  #1
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
			),#2
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
			),#3
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
			),#4
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
			),#5
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
			),#6
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
			),#7
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
			),#8
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
			),#9
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
#8
def eigMod():
	Carousel = CarouselContainer(
		contents = [
			  #1
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
			),#2
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
			),#3
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
			),#4
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
			),#5
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
			),#6
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
			),#7
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
			),#8
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
#7
def sevMod():
	Carousel = CarouselContainer(
		contents = [
			  #1
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
			),#2
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
			),#3
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
			),#4
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
			),#5
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
			),#6
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
			),#7
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
#6
def sixMod():
	Carousel = CarouselContainer(
		contents = [
			  #1
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
			),#2
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
			),#3
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
			),#4
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
			),#5
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
			),#6
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
#5
def fivMod():
	Carousel = CarouselContainer(
		contents = [
			  #1
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
			),#2
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
			),#3
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
			),#4
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
			),#5
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
#4
def fouMod():
	Carousel = CarouselContainer(
		contents = [
			  #1
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
			),#2
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
			),#3
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
			),#4
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
#3
def thrMod():
	Carousel = CarouselContainer(
		contents = [
			  #1
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
			),#2
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
			),#3
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
#2
def twoMod():
	Carousel = CarouselContainer(
		contents = [
			  #1
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
			),#2
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
#1
def oneMod():
	Carousel = CarouselContainer(
		contents = [
			  #1
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

