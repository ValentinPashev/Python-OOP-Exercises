class Person:
    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age


class Child(Person):
    pass


person = Person("Peter", 25)
child = Child("Peter Junior", 5)
print(child.name)
print(child.age)
print(child.__class__.__bases__[0].__name__)