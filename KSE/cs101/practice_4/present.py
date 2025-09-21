import random

l = ['ps5','vr okulus','iphone 17 pro max orange']
d = random.choice(l)
print('Письмо Святому Миколаю')
name = input('Як тебе звати: ')
age = int(input('Твій вік: '))

print(f'Вітаю Святий Миколай! Я {name} і мені {age} років, хочу попросити на новий рік {d}')
