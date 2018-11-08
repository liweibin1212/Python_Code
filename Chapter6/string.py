str1 = 'that is alice\'s cat'
str2 = "that is alice's cat"
print(str1)
print(str2)
print("hello there?\nHow are you?\nI\'m doing fine")
print(r'that is what I want\'')
print('that is what I want\'')
#multiple lines use 

print('''dear alice,
Eve's cat was arrested.
Don't worry.
Your Bob''')

spam = 'Hello World!'
print(len(spam))
print(spam[:2])
print(type(spam))

spam = spam.lower()
spam = spam.upper()
print(spam)
print(spam.isupper())
if 'hello' in spam:
    print(True)
else:
    print(False)
    
print('that'.istitle())

text='Hello World!'
print(text.upper().islower())

text1='remember,remember,the fifth of November'
print(text1.split())
print('-'.join('There can be only one'.split()))
print('hello'.ljust(20, '*'))
print('hello'.rjust(20, '*'))
print('hello'.center(20, '*'))
print(' hello world '.strip())
print(' hello world '.rstrip())