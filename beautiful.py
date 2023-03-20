from bs4 import BeautifulSoup
file = open("index.html",'r').read()
soup = BeautifulSoup(file)
print(soup.
