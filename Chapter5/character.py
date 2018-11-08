import pprint
message = 'It was a bright cold day in April, and the clocks were striking thirteen.'

count = {}

for character in message:
    count.setdefault(character, 0)
    count[character] = count[character] + 1

print(count)
#for i in count.items():
#    print(i)
    
pprint.pprint(count)
print(pprint.pformat(count))
