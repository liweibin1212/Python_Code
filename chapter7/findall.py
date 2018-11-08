import re
from unicodedata import numeric
phoneNumReg = re.compile(r'\d{3}-\d{3}-\d{4}')
mo = phoneNumReg.search('office number: 415-444-1234 home number: 415-666-9876')
print(mo.group())
result = phoneNumReg.findall('office number: 415-444-1234 home number: 415-666-9876')
for i in range(len(result)):
    print(result[i])

phoneNumReg1 = re.compile(r'(\d{3})-(\d{3})-(\d{4})')

result1 = phoneNumReg1.findall('office number: 415-444-1234 home number: 415-666-9876')
for i in range(len(result1)):
    print(result1[i])
    
'''
    \d  0-9 numeric
    \D  except \d
    \w  letter + numeric + _
    \W  except \w
    \s  space + tab + \n
    \S  except \s
'''
    
xMasRegex = re.compile(r'\d+\s\w+')
print(xMasRegex.findall('12 drummers, 11 pipers, 10 lords, 9 ladies'))