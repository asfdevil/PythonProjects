import os
import time
a = input("ENTER PHONE NUMBER: ")
c =0
while c<10:
	c=c+1
	b = os.system(f'termux-telephony-call +91{a}')
	time.sleep(10)

