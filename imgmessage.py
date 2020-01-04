from linebot.models import (
	BubbleContainer, BoxComponent, TextComponent, 
	ImageComponent, SeparatorComponent, ButtonComponent, 
	MessageAction, FlexSendMessage, CarouselContainer
)


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


