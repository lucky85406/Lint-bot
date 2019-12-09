def add(x):
	print(x)
	f = open(r'test_io.txt','w')
	f.write(x)
	f.close()
