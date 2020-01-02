from linebot.models import (
	BubbleContainer, BoxComponent, TextComponent, ImageComponent, SeparatorComponent, ButtonComponent, MessageAction, FlexSendMessage
)



#測試版型
def testimg():
	mes = BubbleContainer(
			hero =  BoxComponent(
				layout = 'vertical',
				contents = [
					ImageComponent(
						url = 'https://i.imgur.com/YVk6nFG.jpg',
						size = 'full',
						align = 'center',
						aspect_ratio = '13:11',
						aspect_mode = 'fit'
					)
				]
			),
			body = BoxComponent(
				layout = 'vertical',
				contents = [
					SeparatorComponent(
						color = '#0000FF'
					),
					TextComponent(
						margin = 'md',
						text = "敘述:",
						weight = 'bold',
						size = 'md',
						align = 'start'
					),
					TextComponent(
						margin = 'md',
						text = "第一段",
						weight = 'bold',
						size = 'xs',
						align = 'start'
					),
					TextComponent(
						margin = 'md',
						text = "第二段",
						weight = 'bold',
						size = 'xs',
						align = 'start'
					),
					TextComponent(
						margin = 'md',
						text = "第三段",
						weight = 'bold',
						size = 'xs',
						align = 'start'
					),
					SeparatorComponent(
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
	message = FlexSendMessage(alt_text = "hello",contents = mes)
	return message