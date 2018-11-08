def printPicnic(itemDict,leftwidth,rightwidth):
    print('PICNIC ITEM'.center(leftwidth+rightwidth, '*'))
    for i,n in itemDict.items():
        print(i.ljust(leftwidth,'.') + str(n).rjust(rightwidth))

picniclist = {"apple":5,"chicken":3,"egg":10,"bread":20}
printPicnic(picniclist, 20,5)
printPicnic(picniclist, 25,5)