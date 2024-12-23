class Student:
    def __init__(self, name):
        self._name = name
        self._scores = []

    def add_score(self, score):
        if 0 <= score <= 100:
            self._scores.append(score)
        else:
            print("Invalid score")

    def get_average(self):
        if self._scores:
            return sum(self._scores) / len(self._scores)
        else:
            return 0

    def get_scores(self):
        return self._scores

if __name__ == "__main__":
    students = [
        Student("Giorgi"),
        Student("Nino"),
        Student("Sandros")
    ]

    students[0].add_score(85)
    students[0].add_score(90)
    students[1].add_score(78)
    students[1].add_score(82)
    students[2].add_score(95)
    students[2].add_score(88)

    for student in students:
        print(f"{student._name}'s average score: {student.get_average()}")

    new_student = Student("Ana")
    new_student.add_score(92)
    print(f"{new_student._name}'s average score: {new_student.get_average()}")

