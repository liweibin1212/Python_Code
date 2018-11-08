print("how old are you?")
while True:
    age = input()
    if age.isdecimal():
        break
    print("input a correct age")


print("please input your password(letters and number only)")
while True:
    pwd = input()
    if pwd.isalnum():
        break
    print("input a correct password")
    
spam = 'hello python'
print(spam.startswith('hello'))
print(spam.endswith('Python'))
