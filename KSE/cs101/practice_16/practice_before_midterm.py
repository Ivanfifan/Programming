#Task 1
# num = int(input('Enter number: '))
# reversed_num = 0
# while num > 0:
#     digit = num % 10
#     reversed_num = (reversed_num * 10) + digit
#     num = num // 10
# print(reversed_num)

#Task 2
# string = input('Write string: ')
#
# count = [['Letters', 0],['Digits', 0],['Others', 0]]
# for i in string:
#     if i.isalpha():
#         count[0][1] += 1
#     elif i.isnumeric():
#         count[1][1] += 1
#     elif not i.isalnum():
#         count[2][1] += 1
# print(count)

#Task 3
number_height = int(input('Enter height: '))
for i in range(1, number_height + 1):
    spaces = number_height - i
    stars = 2 * i - 1
    print(' ' * spaces + '*' * stars)