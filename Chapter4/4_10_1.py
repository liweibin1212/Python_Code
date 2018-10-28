def connect(list):
    str = ''
    for i in range(len(list)):
        if i == len(list)-1:
            str = str + 'and '+list[i]
        else:
            str = str + list[i] + ','
    return str

print("please input the list for test:")
list1 = []
i = 1
while True:
    print('input element ' + str(i) + ' or nothing to stop')
    element = input()
    if element == '':
        break
    list1.append(element)
    i += 1

print(list1)
print(connect(list1))    

