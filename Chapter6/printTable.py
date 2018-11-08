#! python3
# printTable: for exercise
from audioop import findmax
tableData = [['apples','oranges','cherries','banana'],['Alice','Bob','Carol','David'],
              ['dogs','cats','moose','goose']]

def findMax(list):
    max = 0
    for i in range(len(list)):
        if max < len(list[i]):
            max = len(list[i])
    return max

#print(findMax(tableData[0]))

def printTable(list):
    k = len(list)
    v = len(list[0])
    for i in range(v):
        for j in range(k):
            print(list[j][i].rjust(findMax(list[j])), end=' ')
        print()

printTable(tableData)