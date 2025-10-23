def check_range(a,b,c):
    if b > c:
        print('False, wrong range')
    elif a in range(b,c):
        print('True')
    else:
        print('False')
check_range(5,5,10)
input_list = [1,2,3,3,4,4,4,4,5]
def delete_duplicates(a):
    return list(set(a))

print(delete_duplicates(input_list))

def palindrom(a):
    if a == a[::-1]:
        print('Palinword')
    else:
        print('Not palinword')
palindrom('madam')

def bold(a):
    return f'<b>{a}</b>'
def italic(a):
    return f'<i>{a}</i>'
def underline(a):
    return f'<u>{a}</u>'

print(bold('I am gay'))

def password(a:str):
    has_number = False
    has_letter = False
    has_special = False
    if len(a) < 9:
        return False
    for ch in a:
        if ch.isnumeric():
            has_number = True
        elif ch.isalpha():
            has_letter = True
        elif not ch.isalnum():
            has_special = True
    if has_letter and has_number and has_special:
        return True
    return False

print(password('1111sdfsdfsfsf%#2'))