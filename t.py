import re
import string
a = open('font.txt','r')
b = a.read()
s = input("enter string")
al = string.ascii_lowercase[:26]
for i in s:
	l = (al.find(i))
	print(b[l],end='')

print()
