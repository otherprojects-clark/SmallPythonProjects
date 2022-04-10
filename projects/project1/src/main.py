from colorama import init, Fore
from platform import system

if system() == 'Windows':
  init()
else:
  pass

print('Welcome to this Password Manager!')
password = input()

# Startup