def spam():
    eggs = 314
    bacon()
    print(eggs)

def bacon():
    eggs = 0
    ham = 101

spam()

def spam1():
    print(bacon)

bacon = 100
spam1()
print(bacon())
