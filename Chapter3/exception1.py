def div(num):
        try:
                return 42 / num
        except ZeroDivisionError:
                print('Error: Zero Division')

print(div(3))
print(div(5))
print(div(0))
print(div(10))
