import string
def morsecode(st):
	a = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.-"]
	b = string.ascii_lowercase[:26]
#	st = input("enter string")
	for i in st:
		l = b.find(i)
		g = a[l]
		print(g,end=' ')
		for j in g:
			return j
#text=input("enter text")
#morsecode(text)
