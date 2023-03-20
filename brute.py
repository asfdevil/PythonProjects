import time
a = open("text.txt",'r')
x = a.readlines()
for i in x:
	d = i.strip()
	time.sleep(1)
	print(d[0:])
