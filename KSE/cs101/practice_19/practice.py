passwords = {

}
def add_change_password(name,login,password):
    passwords[name] = {"login" : login, 'password': password}
    print(passwords)

add_change_password('facebook','ivf',1234)
add_change_password('youtube','ivf2',1235)

def delete_password(name):
    passwords.pop(name)

def get_password(name):
    if name in passwords:
        print(f'Name: {name}, Login: {passwords[name]['login']}, Password: {passwords[name]['password']}')

get_password('facebook')

def write_password(name):
    with open('file.txt', 'a') as file:

        file.write(f'Name: {name}, Login: {passwords[name]['login']}, Password: {passwords[name]['password']}\n')

write_password('facebook')
write_password('youtube')

def read_password(name):
    with open('file.txt', 'r') as file:
        for i in file:
            if name in i:
                print(i)

read_password('youtube')