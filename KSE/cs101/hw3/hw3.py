import random

students = []
for i in range(1, 7):
    student = {
        'id': i,
        'grade': random.randint(50, 100),
        'passed': random.choice([True, False])
    }
    students.append(student)

for s in students:
    if s['passed']:
        status = "Passed"
    else:
        status = "Failed"
    print(f"Student {s['id']}: Grade {s['grade']}, Status: {status}")


passed = [s['grade'] for s in students if s['passed']]
failed = [s['grade'] for s in students if s['passed'] == False]

if not passed or not failed:
    print('Всі здали або всі нездали')
else:
    if min(passed) > max(failed):
        print("Професор Грубл був послідовним.")
        print(f"Поріг складання знаходиться в діапазоні {max(failed) + 1} - {min(passed)} балів.")
    else:
        print("Професор Грубл був не послідовним.")