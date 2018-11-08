theStuff = {'rope':1,'torch':6,'gold coin':42,'dagger':3,'arrow':12}

def displayInventory(stuff):
    print('Inventory:')
    total = 0
    for item, num in stuff.items():
        total += num
        print( item+':'+str(num))
    print("total: "+str(total))
    
displayInventory(theStuff)
print('==============================')

dragonLoot = ['gold coin','dagger','gold coin','gold coin','ruby','torch','rope']
def addtoInventory(stuff,item):
    stuff.setdefault(item,0)
    stuff[item] += 1
    
for item in dragonLoot:
    addtoInventory(theStuff, item)
    
displayInventory(theStuff)
    