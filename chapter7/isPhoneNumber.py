#! python3
# isPhoneNumber: check a str is phone number or not format 123-456-7890
def isPhoneNumber(str):
    if len(str) != 12:
        return False
    if str[3] != '-' or str[7] != '-':
        return False
    '''
    for i in range(3):
        if not str[i].isdecimal():
            return False
    for i in range(4,7):
        if not str[i].isdecimal():
            return False   
    for i in range(8,12):
        if not str[i].isdecimal():
            return False   '''
    if not (str[0:3]+str[4:7]+str[8:12]).isdecimal():
        print(str[0:3]+str[4:7]+str[8:12])
        return False
    return True

print(isPhoneNumber('sdf'))  
print(isPhoneNumber('123-000-7890'))  
print(isPhoneNumber('123-x00-7890')) 
print(isPhoneNumber('123910007890')) 

message = 'call me at 415-555-4242 tomorrow. 415-555-9999 is my office.'
for i in range(len(message)):
    text = message[i:i+12]
    if isPhoneNumber(text):
        print('phone number found: ' + text)
print('done')
    