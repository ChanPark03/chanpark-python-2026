from dataclasses import dataclass

@dataclass
class Student:
    name: str
    korean: int
    math: int
    english: int
    science: int

    def get_sum(self):
        return self.korean + self.math + self.english + self.science



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

    print(students[0])
    print(students[0].get_sum())
    
if __name__ == "__main__":
    main()