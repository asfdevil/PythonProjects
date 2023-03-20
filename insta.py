import os
import re
from instabot import Bot
import wikipedia
from colorama import Fore
print("Enter password")
print(Fore.BLACK)
p =input()
os.system('rm -rf config')
print(Fore.GREEN)
s = wikipedia.summary("sohail",sentences=10)
bot = Bot()
bot.login(username="cosmic__god__",password=p)
bot.send_message(s,['sohail_bagwan_459'])
