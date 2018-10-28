'''
suppliers = ['AAA','Microsoft','Facebook','Whatsapp']
for i in range(len(suppliers)):
    print('the index '+ str(i)+' suppliers name is '+suppliers[i])

print('please input the suppliers name:')
name = input()
if name in suppliers:
    print(name + ' is one of our suppliers')
else:
    print(name + ' is not our suppliers')
    

if name not in suppliers:
    print(name + ' nonono')
else:
    print(name + ' yesyesyes')

factor = [168,50,'36D']

tall = factor[0]
weight = factor[1]
boob = factor[2]

tall,weight,boob=factor

print('tall is '+str(tall))
print('weight is '+str(weight))
print('the boob is '+boob)


num = 1
num += 1
print('num += 1: '+ str(num))
num *= 2
print('num *= 2: '+ str(num))

spam = ['Alice','Bob','Catty','David','Elean']
print(spam)
print('please input a name')
name = input()
try:
    idx = spam.index(name)
    print('Yes,' + name + ' is our staff'+str(idx+1))
except ValueError:
    print('sorry, '+name+' is not in the list') 
'''    
import sys
spam = ['alice','bob','catty','david','elean']
print(spam)
print('please input the new name you want to add')
spam.append(input())
print('spam now becomes to:')
print(spam)

print('please input the new name you want to add')
name=input()
print('please input the new sequence you want to add')
while True:
    try:
        idx=int(input())
        break
    except ValueError:
        print('invalid input, please give a integer')

if idx < 0 or idx >= len(spam):
    print('wrong sequence')
    #sys.exit()
spam.insert(idx, name)
print(spam)

print('Input a name you want to remove:')
name = input()
if name in spam:
    spam.remove(name)
    print('current spam')
    print(spam)
else:
    print(name + ' is not in the list!')
    
print('after sort')
spam.sort()
print(spam)

num = [-15,3,8,555,58526]
num.sort(reverse=True)
print(num)