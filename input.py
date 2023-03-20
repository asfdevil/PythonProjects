import sys


for line in sys.stdin:

    if 'q' == line.rstrip():

        break

    print(f'Input : {line}')
print("Exit")

#another code
txt = input("enter")
#first write printing string
x = txt.rstrip(",.asf")

print(x)
