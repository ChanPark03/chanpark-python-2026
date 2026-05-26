class Student:
    def __init__(self, name, korean, math, english, science):
        self.name = name
        self.korean = korean
        self.math = math
        self.english = english
        self.science = science
        
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
    # print(students)
    # print(students[0])
    print("이름\t 국어\t 수학\t 영어\t 과학")
    for student in students:
        print(f"{student.name}\t {student.korean}\t {student.math}\t {student.english}\t {student.science}")
if __name__ == "__main__":
    main()