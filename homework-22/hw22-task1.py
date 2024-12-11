class Inset:
    def __init__(self):
        self.elements = []

    def insert(self, element):
        if element not in self.elements:
            self.elements.append(element)

    def member(self, element):
        return element in self.elements

    def remove(self, element):
        if element in self.elements:
            self.elements.remove(element)
        else:
            raise ValueError("ვერ ვიპოვნე")

    def __str__(self):
        return str(sorted(self.elements))

inset = Inset()
inset.insert(3)
inset.insert(1)
inset.insert(2)
print(inset)
print(inset.member(2))
print(inset.member(4))
print(inset)
