'''
#1
spam = ['a','b','c','d']
print(spam[int(int('3'*2) / 11)]) #spam[3]
print(spam[-1])
print(spam[:2])

#2
bacon = [3.14,'cat',11,'cat',True]
print(bacon.index('cat'))
bacon.append(99)
print(bacon)
bacon.remove('cat')
print(bacon)

#11
list1 = [1,2,3,4,5,6,7,8]
print(list1)
list1.remove(1)
print(list1)

del list1[0]
print(list1)

tuple1=(42,)
print(type(tuple1))
'''
list1 = [1,2,3]
tuple1 = (4,5,6)
list2 = list(tuple1)
tuple2 = tuple(list1)
print(list2)
print(tuple2)