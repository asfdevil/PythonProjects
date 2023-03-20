import json
file = open('contacts.json',)
data = json.load(file)
for i in data['contacts']:
	l = list(i.values())
	print(l[0],l[1])
