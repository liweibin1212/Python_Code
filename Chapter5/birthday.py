from test.datetimetester import DAY
birthday = {'alice':'1Apr','bob':'25Jan','Catty':'12Dec','David':'8Aug'}

while True:
    print('Input a name: (blank to quit)')
    name = input()
    if name == '':
        break
    if name in birthday:
        print(birthday[name] + ' is ' + name + ' birthday!')
    else:
        print('I do not have birthday information for ' + name)
        print('what is their birthday?')
        day = input()
        birthday[name]=day
        print('birthday updated. You can try now')
for key in birthday.keys():
    print(key)
for val in birthday.values():
    print(val)
for i in birthday.items():
    print(i)
print('Vito''s birthday is ' + str(birthday.get('Vito', 'not found')))