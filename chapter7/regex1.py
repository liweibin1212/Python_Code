#! python3
# regex1.py
import re
phoneNymRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
mo = phoneNymRegex.search('my number is 415-121-6666')
print('phone number found ' + mo.group())

print(type(mo))
print(type(phoneNymRegex))