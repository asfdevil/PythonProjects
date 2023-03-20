a = (open('q.txt','r'))
c = a.read()
g = (len(c))
y = g-1
a.seek(0)
h = a.readline(y)
print(h)
if h == "hello boys":
	print("yes")
else:
	print("no")
