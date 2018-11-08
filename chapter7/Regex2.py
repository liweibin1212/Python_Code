#! python3
# regex2.py
import re
phoneNymRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
mo = phoneNymRegex.search('my number is 415-121-6666')
print('phone number found ' + mo.group())
tuple1 = mo.groups()
for i in range(len(tuple1)):
    print(tuple1[i])
    
phoneNymRegex2 = re.compile(r'(\(\d\d\d\))(\d\d\d-\d\d\d\d)')
mo2 = phoneNymRegex2.search('my number is (415)121-6666')
print('phone number found ' + mo2.group())
tuple2 = mo2.groups()
for i in range(len(tuple2)):
    print(tuple2[i])