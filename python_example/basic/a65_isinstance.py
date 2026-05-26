class Student(object):
    def study(self):
        print("studying")
        
class Teacher:
    def teach(self):
        print("teaching")
        
def main():
    student = Student()
    classroom = [Student(), Student(), Teacher(), Teacher(), Student(), Student()]
    
    print(isinstance(student, Student))
    print(isinstance(student, int))
    print(isinstance(student, object))
    
    print(isinstance(1, object))
    print(isinstance([1,2,3, student], object))
    
    for person in classroom:
        if isinstance(person, Student):
            person.study()
        if isinstance(person, Teacher):
            person.teach()
            
if __name__ == "__main__":
    main()