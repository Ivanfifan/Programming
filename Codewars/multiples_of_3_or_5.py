# First solution
# def solution(number):
#     start = 3
#     sum = 0
#     while start < number:
#         if start % 3 == 0 or start % 5 == 0:
#             sum += start
#             print(start)
#         start += 1
#     return sum
# Second solution
def solution(number):
    sum = 0
    for i in range(number):
        if i % 3 == 0 or i % 5== 0:
            sum+=i
    return sum
print(solution(16))