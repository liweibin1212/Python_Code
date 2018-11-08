#! python3
# pwd.py a pwd management tool
import pyperclip
import sys

PASSWORDS = {'163.COM':'abcd@123','tencent':'vito78545','alibaba':'testpwd'}

for a in sys.argv:
    print(a)
if len(sys.argv) < 2:
    print('Usage: python pwd.py [account] - copy accout password')
    sys.exit()
account = sys.argv[1] # first command line arg is the account name

if account in PASSWORDS:
    pyperclip.copy(PASSWORDS[account])
    print('password for ' + account + ' copied to clipboard')
else:
    print('There is no account named ' + account)
    
    
    