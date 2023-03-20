import time
from colorama import Fore
a = [1,0,1,0,0,1]
b = [0,1,1,0,1,1]
while a:
#	time.sleep(3)
	for i in a:
		print(Fore.GREEN + str(i),end='   ')
