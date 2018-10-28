def collatz(number):
    if number % 2 == 0:
        return number // 2
    else:
        return number * 3 + 1

print('Please input an integer:')
while True:
    try:
        num = int(input())
        break
    except ValueError:
        print('Invalid input, please try again')

while True:
    num = collatz(num)
    print(num)
    if num == 1:
        break
