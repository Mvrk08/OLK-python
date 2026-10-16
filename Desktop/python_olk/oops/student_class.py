class Student:
    def __init__(self, name: str, age: int, marks: list[int]) -> None:
        self.name = name
        self.age = age
        self.marks = marks

    def total(self) -> int:
        return sum(self.marks)

    def average(self) -> float:
        return sum(self.marks) / len(self.marks)

    def grade(self):
        avg = self.average()

        if avg >= 90:
            print("A")
        elif avg >= 50:
            print("B")
        else:
            print("C")


student1 = Student("naman", 67, [93, 89, 66, 78])

total = student1.total()
print(total)

avg = student1.average()
print(avg)

student1.grade()