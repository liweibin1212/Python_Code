print('please input Exit')
str = input()
while True:
    if str == 'Exit':
        break
    if str == 'pwd':
        str = input()
        continue
    print('wrong input')
    str = input()
    
