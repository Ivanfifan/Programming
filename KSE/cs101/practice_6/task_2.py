import random
r = random.randint(0,100)

while True:
    a = int(input('Enter number: '))
    if a < r:
        print('Your number is less. Try again')
    if a > r:
        print('Your number is more. Try again')
    if a == r:
        print('Win')
        break