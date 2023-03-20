import wikipedia
import os
e = input("enter question")
a = wikipedia.summary(e,sentences=1)
if e == "devil":
	a = open('q.txt','r').readline()
	print(a)
	b = os.system(f'termux-tts-speak {a}')
else:
	print("no")

