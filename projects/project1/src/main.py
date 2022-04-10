from colorama import init, Fore
from sys import platform

if platform == 'win32':
  init()
else:
  pass

with open('users.txt', 'r') as a:
  users = a.readlines()
with open('passwords.txt', 'r') as b:
  pws = b.readlines()


print('Welcome to this Password Manager!')
if users == [] and pws == []:
  print('Let\'s create your account')


password = input()



# Startup