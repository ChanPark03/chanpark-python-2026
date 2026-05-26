class Student:
    count = int()
    students = list()
    def __init__(self, name, korean, math, english, science):
        self.name = name
        self.korean = korean
        self.math = math
        self.english = english
        self.science = science
        Student.count += 1
        Student.students.append(self)
        self.__aa = "secret key"

    def get_sum(self):
        return self.korean + self.math + self.english + self.science

    def get_average(self):
        return self.get_sum() / 4

    def to_string(self):
        return f"{self.name}\t {self.korean}\t {self.math}\t {self.english}\t {self.science}"

    def __repr__(self):
        return f"{self.name}\t {self.korean}\t {self.math}\t {self.english}\t {self.science}\
            {self.get_sum()}\t {self.get_average()}"

    def __str__(self) -> str:
        return f"{self.name}\t {self.korean}\t {self.math}\t {self.english}\t {self.science}\
            {self.get_sum()}\t {self.get_average()} str"

    # 사칙연산 + - * /
    def __add__(self, other):
        return self.get_sum() + other.get_sum()

    def __sub__(self, other):
        return self.get_sum() - other.get_sum()

    def __mul__(self, other):
        return self.get_sum() * other.get_sum()

    def __truediv__(self, other):
        return self.get_sum() / other.get_sum()

    # 관계 연산자 greater than -> gt , less than -> lt, equal -> eq, nagative ->ne
    # grather than equal -> ge, less than equal ->le
    def __gt__(self, value):
        if isinstance(value, Student):
            return self.get_sum() > value.get_sum()
        else:
            # raise
            return "error"

    @classmethod
    def print(cls):
        print(f"등록된 학생 수는 {Student.count}")
        print("이름\t 국어\t 수학\t 영어\t 과학\t 총점\t 평균")
        print()
        print("--------------------학생 목록------------------")
        for student in Student.students:
            print(student)
        print("----------------------------------------------")

def main():
    students = [
        Student("abc", 90, 63, 14, 13),
        Student("adf", 31, 44, 75, 32),
        Student("erf", 37, 55, 85, 78),
        Student("xdf", 35, 77, 67, 65),
        Student("weqe", 21, 98, 34, 94),
        Student("rewr", 23, 21, 73, 95),
        Student("qqe", 100, 35, 18, 75),
        Student("sso", 89, 65, 88, 64)
    ]
  
    print(f"등록된 학생 수는 {Student.count}")
    Student.print()
    
if __name__ == "__main__":
    main()