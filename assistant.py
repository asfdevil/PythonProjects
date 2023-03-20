import os
import time
import wikipedia
os.system('clear')
print("   hearing   ")
b = os.system('termux-speech-to-text > q.txt')
d = open("q.txt",'r')
f = d.readline()
g = (len(f))
y = g-1
d.seek(0)
h = d.readline(y)
print(h)
def movie():
  os.system('termux-tts-speak which movie you want to download')
  print("hearing")
  os.system('termux-speech-to-text > q.txt')
  if True:
    br = os.system(f'termux-open https://google.com/search?q={h}')
    print(h)
  else:
    print("no")

if (h == "hello") | (h == "hi"):
	os.system('termux-tts-speak hi i am your assistant ask me anything you want')
	os.system('python assistance.py')
elif (h == "what is my sister name") | (h == "who is my sister"):
	os.system('termux-tts-speak misba')
elif h == "what is my another sister name":
	os.system('termux-tts-speak anji')
elif h == "how are you":
	os.system('termux-tts-speak fine')
elif h == "f*** you":
	os.system('termux-tts-speak fuck you too')
elif h == "turn on flash":
	os.system('termux-torch on')
	time.sleep(10)
	os.system('termux-torch off')
elif h == "play music":
        os.system('play /sdcard/Download/*.mp3')
elif h == "what is my name":
	os.system('termux-tts-speak devil the king of hell')
elif h == "exit":
	os.system('termux-tts-speak ok, have a great day')
	exit
elif h == "what is your name":
	os.system('termux-tts-speak devil, still not gave me the name')
elif h == "my friend's name":
	os.system('termux-tts-speak parthmesh and sourabh')
elif h == "help me to find this answer":
	os.system('python webfun.py')
elif h == "what is my brother name":
	os.system('termux-tts-speak sajid bagwan')
elif h == "call Sohail":
	os.system('termux-telephony-call +918618029235')
elif h == "f*** off":
	os.system('termux-tts-speak ok')
elif (h == "who made you") | (h == "who created you"):
	os.system('termux-tts-speak asif')
elif (h == "download movie"):
	movie()
elif h == "open WhatsApp":
	os.system('am start -n com.whatsapp/com.whatsapp.HomeActivity')
else:

	os.system('termux-tts-speak sorry, say correctly')
	os.system('python assistant.py')

