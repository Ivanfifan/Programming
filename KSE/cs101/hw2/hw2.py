# Task 1
input_num = int(input('Enter number: '))
if input_num % 5 == 0 and input_num % 3 == 0 :
    print('Ham')
elif input_num % 3 == 0:
    print('Foo')
elif input_num % 5 == 0:
    print('Bar')

# Task 2
def plus_minus(a,b):
    if a > b:
        print(f'Більше число {a}, менше {b}')
    elif a == b:
        print('Error')
    else:
        print(f'Більше число {b}, менше {a}')

# Task 3
def tri_churky(a,b,c):
    list_num = [a,b,c]
    if a == b or b == c or a == c:
        print('Error')
        return
    print(f'Найбільше число: {max(list_num)}, середнє: {sum(list_num) -max(list_num) - min(list_num)}, найменше: {min(list_num)}')

#Task 6
value_of_number = 20.79
zakupka_input = int(input('Введіть кількість квартири: '))
numbers = {
    '0': 0,
    '1': 0,
    '2': 0,
    '3': 0,
    '4': 0,
    '5': 0,
    '6': 0,
    '7': 0,
    '8': 0,
    '9': 0,
}
for i in range(1, zakupka_input + 1):
    hata = str(i)
    for number in hata:
        numbers[number] +=1

sum_of_hata = sum(numbers.values()) * value_of_number
print(numbers)
print(sum_of_hata)

#Task 7
def login_check():
    passwords = {
        'user1': 'passwordexample1234',
        'user2': 'passwordexample4321'
    }

    login_input = input('Enter login: ')

    if login_input not in passwords:
        print('There is not your login, you need to registrate')
        return

    attempts = 0

    while attempts < 3:

        password_input = input('Enter password: ')
        if password_input == passwords[login_input]:
            print('You entered password right')
            break
        else:
            print('Password is incorect')
            attempts += 1
    if attempts == 3:
        print('There is too many attempts')
