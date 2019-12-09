def add(x):
	print(x)
	f = open(r'test_io.txt','w',encoding='UTF-8')
	f.write(x)
	f.close()
