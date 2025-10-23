students = [
    {'id': 1,'grade': 78,'passed': False},
    {'id': 2,'grade': 82,'passed': True},
    {'id': 3,'grade': 97,'passed': True},
    {'id': 4,'grade': 86,'passed': True},
    {'id': 5,'grade': 67,'passed': True},
    {'id': 6,'grade': 75,'passed': True}
]
min_passed = min(passed['grade'] for passed in students if passed['passed'])
max_passed = max(passed['grade'] for passed in students if passed['passed'])
max_failed = max(passed['grade'] for passed in students if passed['passed'] == False)
if min_passed > max_failed:
    print("Професор Грубл був послідовним")
    print(f"Поріг складання знаходиться між {min_passed} і {max_passed}")
else:
    print("Професор Грубл був не послідовним")