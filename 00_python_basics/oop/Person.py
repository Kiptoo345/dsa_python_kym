class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = self.validate_age(age)

    def validate_age(self, age):
        if age > 0 and age < 100:
            self.age = age
        else:
            self.age = 0
        return self.age

    def get_age(self):
        return self.age

p1 = Person("Jason", 10)
print(p1.get_age())

