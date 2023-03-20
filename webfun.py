import os
import wikipedia
import re
def asif():
	os.system('termux-tts-speak ok devil what question you wanna ask')
	print("hearing")
	os.system('termux-speech-to-text > q.txt')
	d = open("q.txt",'r')
	f = d.readline()
	g = (len(f))
	y = g-1
	d.seek(0)
	h = d.readline(y)
	print(h)
	l = wikipedia.summary(h,sentences=1)
	if l:
		print(l)
		os.system(f'termux-tts-speak {l}')
	else:
		print("NOT FOUND")
		os.system('termux-tts-speak sorry not found')

asif()

