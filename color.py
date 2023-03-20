from colorama import Fore
import pyfiglet
k = input("enter color")
a = input("enter name")
c = pyfiglet.figlet_format(a)
d = (f'Fore.{k}' + c)
print(d)
