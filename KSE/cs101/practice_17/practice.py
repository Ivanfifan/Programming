# #Task 1
log_data = [
    500, "user-123", 1.2, {"path": "/login"}, ["critical"], 200, "user-456",
    0.5, {"path": "/home"}, 404, "user-123", 2.1, ["error", "api"],
    "user-789", 0.1, {"path": "/"}, 503, 3.5, ["db", "timeout"],
    "user-456", 0.8, {"path": "/data"}, 200, 201, "user-101",
    1.1, {"path": "/img"}, ["new"], 401, "user-123", 0.3, {"path": "/admin"}
]

def filter_log_data(log_list):
    result = {
        'user_ids': [],
        'error_codes': []
    }

    for i in log_data:
        if type(i) is str:
            result['user_ids'].append(i)
        elif type(i) is int:
            result['error_codes'].append(i)

    return result

print(filter_log_data(log_data))
#Task 2
UNITS_IN_BYTES = {
    "B": 1,
    "KB": 1024,
    "MB": 1024**2,
    "GB": 1024**3,
    "TB": 1024**4
}

def calculate_storage(a,b,c):
    return a, b, a * UNITS_IN_BYTES[b] / UNITS_IN_BYTES[c], c

print(calculate_storage(5120,'MB','GB'))

def format_report(a):
    return f'{a[0]} {a[1]} дорівнює {a[2]} {a[3]}'

print(format_report(calculate_storage(5120,'MB','GB')))

#Task 3,4
import random
from datetime import datetime
import os

log_file = "search_log.csv"
if os.path.exists(log_file):
    os.remove(log_file)

random_numbers = random.sample(range(1,1001),50)
random_numbers.sort()

target = random.choice(random_numbers)

counter = 1

def log_attempt(attempt,value_at_index,hint):
    with open("search_log.csv", "a") as f:
        log_str = f"{datetime.now()},attempt:{attempt},value_at_index:{value_at_index},hint:{hint}\n"
        f.write(log_str)


while counter < 7:
    ur_input = input('Enter index: ')
    try:
        index = int(ur_input)
    except ValueError:
        attempt_result = 'Enter valid number'
        print(attempt_result)
        print(f'Try: {counter}')
        log_attempt(ur_input, None, attempt_result)
        counter +=1
        continue
    try:
        ur_number = random_numbers[index]
    except IndexError:
        attempt_result = "Index out of range"
        print(attempt_result)
        print(f'Try: {counter}')
        log_attempt(index, None, attempt_result)
        counter += 1
        continue
    if target  > ur_number:
        attempt_result = 'Target is bigger'
        print(attempt_result)
        print(f'Try: {counter}')
        log_attempt(index, ur_number, attempt_result)
        counter += 1
    elif target  < ur_number:
        attempt_result = 'Target is smaller'
        print(attempt_result)
        print(f'Try: {counter}')
        log_attempt(index, ur_number, attempt_result)

        counter += 1
    else:
        attempt_result = 'You won'
        print(attempt_result)
        log_attempt(index, ur_number, attempt_result)
        break

def display_summary(file_name):
    with open(file_name, "r") as f:
        all_lines = f.readlines()
        print(f"Attempts count: {len(all_lines)}")

        counter_valid = 0
        for line in all_lines:
            if "Enter valid number" in line:
                counter_valid += 1

        print(f"Total \"Enter valid number errors\": {counter_valid}")


display_summary("search_log.csv")