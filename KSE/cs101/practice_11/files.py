#f = open('file.txt','a')
#content = f.write(input('Type: '))
with open('file.txt', 'a') as file:
    file.write(input('Type: '))