import random
import string
from string import punctuation
passwords = []

while True:
    print('Welcome to the menu!')
    print('1. Register')
    print('2. Find')
    print('3. Check')
    print('4. Random')
    print('0. Exit')
    result = int(input('Enter the number of the action you want to perform: '))
    if result == 1:
        name = str(input('Enter your name of program: '))
        while name == '':
            print('Name must not be empty.')
            name = str(input('Enter your name of program again: '))
        login = str(input('Enter your login: '))
        while login == '' or len(login) < 3:
            print('Login must be at least 3 characters long and not empty.')
            login = str(input('Enter your login again: '))
        password = str(input('Enter your password: '))
        while password == '' or len(password) < 9:
            print('Password must be at least 9 characters long and not empty.')
            password = str(input('Enter your password again: '))
        passwords.append((name, login, password))
        print('You have successfully registered!')
    elif result == 2:
        search_name = str(input('Enter the name of the program you want to find: '))
        for ch in passwords:
            if search_name in ch:
                print(f'Name: {ch[0]}\nLogin: {ch[1]}\nPassword: {ch[2]}')
            else:
                print('No password')
    elif result == 3:
        check_password = str(input('Enter the password you want to check: '))

        for ch in check_password:
            if ch.isnumeric():
                print('Password has number')
                break
        else:
            print('Password has no number')
        for ch in check_password:
            if ch.isupper():
                print('Password has uppercase letter')
                break
        else:
            print('Password has no uppercase letter')
        for ch in check_password:
            if ch.islower():
                print('Password has lowercase letter')
                break
        else:
            print('Password has no lowercase letter')
        for ch in check_password:
            if not ch.isalnum():
                print('Password has special character')
                break
        else:
            print('Password has no special character')
    elif result == 4:
        long_of_password = int(input('How long password do you want?: '))
        n = 0
        generated_password = ''
        while long_of_password > n:
            random_choice = random.randint(1,4)
            if random_choice == 1:
                generated_password = generated_password + random.choice(string.ascii_lowercase)
            elif random_choice == 2:
                generated_password = generated_password + random.choice(string.ascii_uppercase)
            elif random_choice == 3:
                generated_password = generated_password + str(random.randint(0, 9))
            else:
                generated_password = generated_password + random.choice(punctuation)
            n += 1
        print(generated_password)
        print('Want to add password to list?\n1.Yes\n2.No')
        add_password = int(input('Your choice: '))
        if add_password == 1:
            name = str(input('Enter your name of program: '))
            while name == '':
                print('Name must not be empty.')
                name = str(input('Enter your name of program again: '))
            login = str(input('Enter your login: '))
            while login == '' or len(login) < 3:
                print('Login must be at least 3 characters long and not empty.')
                login = str(input('Enter your login again: '))
            passwords.append((name, login, generated_password))
            print('You have successfully registered!')
    elif result == 0:
        print('Goodbye!')
        break