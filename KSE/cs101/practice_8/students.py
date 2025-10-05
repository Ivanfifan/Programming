students_grades = {
    "Andrii": 87,
    "Maria": 93,
    "Serhii": 78,
    "Olena": 85,
    "Dmytro": 91,
    "Kateryna": 76,
    "Yurii": 89,
    "Iryna": 95,
    "Bohdan": 82,
    "Natalia": 88,
    "Oleksandr": 73,
    "Viktoria": 97,
    "Petro": 80,
    "Tetiana": 90,
    "Mykola": 69,
    "Oksana": 92,
    "Vladyslav": 84,
    "Anastasiia": 98,
    "Denys": 77,
    "Sofiia": 94,
    "Illia": 70,
    "Yuliia": 96,
    "Maksym": 83,
    "Valeriia": 79,
    "Roman": 75,
    "Alina": 99,
    "Pavlo": 81,
    "Diana": 88,
    "Anton": 74,
    "Veronika": 91
}
highest_grade = max(students_grades.values())
lowest_grade = min(students_grades.values())
average_grade = round(sum(students_grades.values()) / len(students_grades))
grades_first = []
for name, grades in students_grades.items():
    grades_first.append((grades, name))
grades_first.sort(reverse=True)
top_10 = grades_first[:10]
grades_first.sort()
bottom_10 = grades_first[:10]
print(f'Max grade: {highest_grade}')
print(f'Min grade: {lowest_grade}')
print(f'Avg grade: {average_grade}')
print('Top 10 students:')
for name, grade in top_10:
    print(name, grade)
print('Bottom 10 students:')
for name, grade in bottom_10:
    print(name, grade)