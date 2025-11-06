# #Task 1
# log_data = [
#     500, "user-123", 1.2, {"path": "/login"}, ["critical"], 200, "user-456",
#     0.5, {"path": "/home"}, 404, "user-123", 2.1, ["error", "api"],
#     "user-789", 0.1, {"path": "/"}, 503, 3.5, ["db", "timeout"],
#     "user-456", 0.8, {"path": "/data"}, 200, 201, "user-101",
#     1.1, {"path": "/img"}, ["new"], 401, "user-123", 0.3, {"path": "/admin"}
# ]
# result = {
#     'user_ids': [],
#     'error_codes': []
# }
#
# for i in log_data:
#     if str(i).isnumeric():
#         if i >= 100:
#             result['error_codes'].append(i)
#     elif isinstance(i, str) and i.startswith('user-'):
#         result['user_ids'].append(i)
#
# print(result)
#
#Task 2
# UNITS_IN_BYTES = {
#     "B": 1,
#     "KB": 1024,
#     "MB": 1024**2,
#     "GB": 1024**3,
#     "TB": 1024**4
# }
#
# def calculate_storage(a,b,c):
#     return a, b, a * UNITS_IN_BYTES[b] / UNITS_IN_BYTES[c], c
#
# print(calculate_storage(5120,'MB','GB'))
#
# def format_report(a):
#     return f'{a[0]} {a[1]} дорівнює {a[2]} {a[3]}'
#
# print(format_report(calculate_storage(5120,'MB','GB')))

#Task 3
import random
random_numbers = random.sample(range(1,1001),50)

random_numbers.sort()

target = random.choice(random_numbers)

while attempts < 6:
