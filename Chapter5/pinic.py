
allGuests = {'Alice':{'apples':5,'pretzels':12},
             'Bob':{'ham sandwiches':3,'apples':2},
             'Carol':{'cups':3,'apple pies':1,'ham sandwiches':10}}

def totalBrought(guests,item):
    numBrought = 0
    for k, v in guests.items():
        numBrought = numBrought + v.get(item,0)
    return numBrought

print('apples: ' + str(totalBrought(allGuests, 'apples')))
print('pretzels: ' + str(totalBrought(allGuests, 'pretzels')))
print('ham sandwiches: ' + str(totalBrought(allGuests, 'ham sandwiches')))
print('cups: ' + str(totalBrought(allGuests, 'cups')))
print('apple pies: ' + str(totalBrought(allGuests, 'apple pies')))