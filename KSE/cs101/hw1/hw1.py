#Task 1
num = input('Enter number: ')
current_num = int(num)
units = current_num % 10
tens = (current_num // 10) % 10
hundreds = current_num // 100
print((units * 100) + (tens * 10) + hundreds)
num_list = list(num)
print(''.join(list(reversed(num_list))))
print(num[::-1])
reversed_num = 0
while current_num > 0:
    digit = current_num % 10
    reversed_num = (reversed_num * 10) + digit
    current_num = current_num // 10
print(reversed_num)

# Task 2
password = input('Enter password: ')
has_numbers = any(i.isdigit() for i in password)
has_uppers = any(i.isupper() for i in password)
long_enough = len(password) >= 9

print(f"Наявність цифр: {has_numbers}")
print(f"Наявність великих літер: {has_uppers}")
print(f"Довжина (>= 9): {long_enough}")

#Task 3
name = str(input("Введіть ім'я: "))
salary = int(input("Введіть зарплату: "))
print(f"Зарплата {name} в рік: {(salary * 12) // 1000} тис. доларів")

#Task4
num_1 = int(input('Введіть перше число: '))
num_2 = int(input('Введіть друге число: '))
def numbers(a, b):
    print(f'Сума is {a + b}')
    print(f'Різниця is {a - b}')
    print(f'Множення is {a * b}')
    print(f'Ділення is {a / b}')
    print(f'Залишок від ділення is {a % b}')
    print(a >= b)
numbers(num_1 , num_2)