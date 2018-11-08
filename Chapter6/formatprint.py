spam = ['alice','bob','cathy','david']
print('_'.join(spam))
spam1 = '''this is a test sentence
another line

the third line'''
test = spam1.split('\n')
print(test)

print('hello'.rjust(20))
print('hello'.ljust(12, '*'))
print('hello'.center(21, '-'))