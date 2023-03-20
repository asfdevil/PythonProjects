import re 
def main():
  FindWord()
  DEmarcationLine()
  MatchWord()
def FindWord():
try:
  files = open("/data/data/com.termux/files/home/python/file.txt")
  for line in files:
  # you can search any word
    if re.search('lenor|more', line):
      print(line, end=' ')
except FileNotFoundError as e:
  print("Fiel was not found:", e)
def MatchWord():
try:
  files = open("/data/data/com.termux/files/home/python/file.txt")
  for line in files:
  # you can search any pattern that can match this word
    match = re.search('(len|neverm)ore', line)
    if match:
      print(match.group())
except FileNotFoundError as e:
  print("Fiel was not found:", e)
def DEmarcationLine():
  print("*************")
  if __name__ == "__main__":
  main()
