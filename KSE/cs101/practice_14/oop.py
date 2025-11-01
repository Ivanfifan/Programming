class Person:
    def __init__(self, name, age, iq):
        self.name = name
        self.age = age
        self.iq = iq
    def walk(self):
        print("I'm walking")
    def tell_my_age(self):
        print(f'My age is {self.age}')

person = Person('Serafym',19,120)

person.walk()
person.tell_my_age()