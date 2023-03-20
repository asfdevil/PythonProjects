import os
import time
import morse
a = input("enter code")
z = morse.morsecode(a)
for i in z:
	if i == ".":
		os.system('termux-torch on')
		time.sleep(0.01)
		os.system('termux-torch off')
	elif i == "_":
		os.system('termux-torch on')
		time.sleep(1)
		os.system('termux-torch off')
	else:
		print("rewrite the code")


