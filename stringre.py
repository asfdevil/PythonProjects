import re
a = input("enter string")
for i in a:
	print(re.search('abcd',"####",i),end='')
