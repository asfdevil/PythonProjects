import os
a = input("enter")
if a:

	b=os.system(f'termux-open https://google.com/search?q={a}')
	print(b)
else:

	print("no")

