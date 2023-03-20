import os
def cycle(vo):
#	b = os.system('termux-speech-to-text > q.txt')
#	d = open("q.txt",'r')
	f = vo.readline()
	g = (len(f))
	y = g-1
	vo.seek(0)
	h = vo.readline(y)
	print(h)

b = os.system('termux-speech-to-text > q.txt')
d = open("q.txt",'r')
cycle(d)
