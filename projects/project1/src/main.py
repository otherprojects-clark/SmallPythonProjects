from colorama import init, Fore
from sys import platform
from re import compile
from hashlib import sha1
from getpass import getpass

if platform == 'win32':
  init()
else:
  pass

with open('passwords.txt', 'r') as b:
  passwords_list = []
  pws = b.readlines()
  for x in pws:
    passwords_list.append(x[:40].strip())

password_pattern = compile('^[\w]{8,200}$')
r = Fore.RESET

# functions






# main

print('Welcome to this Password Manager!')
if pws == []:
  print(Fore.GREEN+'Let\'s wanna create a password? (ok/no)'+r)
  confirm_create = input().lower()
  if confirm_create == 'ok':
    pass
  else:
    exit()
  while True:
    print(Fore.YELLOW+'Your password should have equal or more than 8 characters, and contain small & capital letters, numeric characters, and underscores.'+r)
    password = getpass('Enter your password: ')
    if password_pattern.match(password) == None:
      print(Fore.RED+'Try again.'+r)
    else:
      confirmation = getpass('Repeat for confirmation: ')
      if confirmation != password:
        print(Fore.RED+'Try again.'+r)
      else:
        with open('passwords.txt') as pw:
          pw.write(password)
        break
else:
  print('Login')
  
  passwordLogin = getpass('Enter your password')

# password creation or else login