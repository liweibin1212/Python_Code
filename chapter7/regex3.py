import re
heroRegex = re.compile(r'Batman|Tina Fey')
mo1 = heroRegex.search('Batman and Tina Fey')
print(mo1.group())

mo2 = heroRegex.search('Tina Fey and Batman')
print(mo2.group())

batRegex = re.compile(r'Bat(man|mobile|copter|bat)')
mo = batRegex.search('Batmobile lost a wheel')
print(mo.group(0)+'|'+mo.group(1))

'?'
batRegex1 = re.compile(r'Bat(wo)?man')
print(batRegex1.search('The adventure of Batwoman').group())
print(batRegex1.search('The adventure of Batman').group())


phoneReg = re.compile(r'(\d\d\d-)?\d\d\d\d-\d\d\d')
print(phoneReg.search('my phone is 415-5555-666').group())
print(phoneReg.search('my phone is 5555-666').group())

'*'
batRegex2 = re.compile(r'Bat(wo)*man')
print(batRegex2.search('The adventure of Batwowowoman').group())
print(batRegex2.search('The adventure of Batman').group())

'+'
batRegex3 = re.compile(r'Bat(wo)+man')
print(batRegex3.search('The adventure of Batwowoman').group())
print(batRegex3.search('The adventure of Batman'))

'{}'
phoneReg1 = re.compile(r'(\d{3}-)?\d{4}-\d{3}')
print(phoneReg1.search('my phone is 415-5555-666').group())
print(phoneReg1.search('my phone is 5555-666').group())

'{n,m}'
cardNoReg1 = re.compile(r'\d{16,18}')
print(cardNoReg1.search('622588024152145 is 62258805090943431266').group())

cardNoReg2 = re.compile(r'\d{16,18}?')
print(cardNoReg2.search('622588024152145 is 62258805090943431266').group())