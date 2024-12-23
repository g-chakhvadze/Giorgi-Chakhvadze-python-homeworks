class Person:
    def __init__(self, name, age):
        self._name = name
        self._age = age

    def get_info(self):
        return f"Name: {self._name}, Age: {self._age}"

if __name__ == "__main__":
    person1 = Person("Giorgi", 30)
    person2 = Person("Nino", 25)
    person3 = Person("Sandro", 40)

    print(person1.get_info())
    print(person2.get_info())
    print(person3.get_info())
