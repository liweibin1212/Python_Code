import copy
from builtins import list
name = 'Alice'
for i in range(0,len(name)):
    print('***'+name[i]+'***')
for i in name:
    print('###'+i+'###')
#name[1]='X' TypeError: 'str' object does not support item assignment
print(name)
print(name[0:2]+'xxxx')

suppliers =('microsft','ibm','oracle','dasd','google')
print(suppliers)
for name in suppliers:
    print(name)
print(suppliers[1])
#suppliers[0]='facebook' TypeError: 'tuple' object does not support item assignment
spam = ('hello')
print(type(spam))
spam1 = ('hello',)
print(type(spam1))
print(spam1)

spam_tuple = suppliers
spam_list = list(suppliers)
print(spam_list)
print(spam_tuple)
print(list(name))

list1 = [1,2,3,4,5]
list2 = list1
print(list1)
print(list2)

def addElement(list,num):
    list.append(num)

addElement(list1, 6)  # by reference
print(list1)
print(list2)

list3=copy.copy(list1) #by value

print(list1)
print(list2)
print(list3)

addElement(list3, 10)
print(list1)
print(list2)
print(list3)



