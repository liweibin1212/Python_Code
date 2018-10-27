import random
print('I am thinkinf of a number between 1 to 20')
number = random.randint(1,20)

#while True:
#        print('take a guess')
#        try:
#                guess = int(input())
#        except ValueError:
#                print('must be a number')
#                continue
#        if guess == number:
#                print('you are great! Bingo.')
#                break
#        elif guess < number:
#                print('your guess is too low')
#        else:
#                print('your guess is too high')

for time in range(1,7):
        print('take a guess')
        try:
                guess = int(input())
        except ValueError:
                print('must be a number')
                guess = 0
                continue
        if guess == number:
                break
        elif guess < number:
                print('your guess is too low')
        else:
                print('your guess is too high')

if guess == number:
        print('good job, your take ', str(time), ' times to get that number')
else:
        print('the number in my mind is ', str(number), '. Add oil.')
