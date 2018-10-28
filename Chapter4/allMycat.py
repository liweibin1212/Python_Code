'''
print('Input the name of cat 1:')
cat1 = input()
print('Input the name of cat 2:')
cat2 = input()
print('Input the name of cat 3:')
cat3 = input()
print('Input the name of cat 4:')
cat4 = input()
print('Input the name of cat 5:')
cat5 = input()

print('the name of cat1 is ' + cat1)
print('the name of cat2 is ' + cat2)
print('the name of cat3 is ' + cat3)
print('the name of cat4 is ' + cat4)
print('the name of cat5 is ' + cat5)
'''
catNames = []
while True:
    print('Input the name of cat ',len(catNames)+1, 'or input nothing to stop')
    name = input()
    if name == '':
        break
    else:
        catNames.append(name)

print('the cat names are ',end='')
#for i in range(len(catNames)):
#    print(catNames[i] + ' ',end='')
for name in catNames:
    print(name + ' ', end='')
    
