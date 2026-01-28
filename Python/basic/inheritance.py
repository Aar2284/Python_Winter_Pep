# inheritance in classes

class Student:
    def __init__(self, name, grade, percentage):
        self.name = name # attributes
        self.grade = grade # grade is public, __grade will make it private 
        self.percentage = percentage 

    def student_detials(self):
        print(f"{self.name} is in grade {self.grade}, with {self.percentage+2}%")

#instance of class
student1 = Student('Madhav',11, 96)
student2 = Student('Rahul',10, 86)

print("\n--------------- Inheritance Example -----------------\n")
student1.student_detials()
student2.student_detials()

class SchoolStudent(Student):
    def __init__(self, name, grade, percentage, stream):
        super().__init__(name, grade, percentage) # calling parent class constructor
        self.stream = stream

Stud1 = SchoolStudent('Aaryan',12, 89, 'Science')
Stud1.student_detials()

# Inheritance example2

class Teacher:
    def __init__(self, name, subject):
        self.name = name
        self.subject = subject

    def teacher_details(self):
        print(f"{self.name} teaches {self.subject}")

class SchoolTeacher(Teacher):
    def __init__(self, name, subject, mode):
        super().__init__(name, subject)
        self.mode = mode

    def teacher_mode(self):
        print(f"{self.name} teaches in {self.mode} mode")

teacher1 = SchoolTeacher("Mr. Sharma", "Mathematics", "Online")
teacher2 = SchoolTeacher("Ms. Gupta", "Science", "Offline")
teacher3 = SchoolTeacher("Mrs. Verma", "English", "Online")
teacher4 = SchoolTeacher("Mr. Singh", "History", "Offline")

print("\n--------------- Teacher Inheritance Example -----------------\n")
teacher1.teacher_details()
teacher1.teacher_mode()
teacher2.teacher_details()
teacher2.teacher_mode()
teacher3.teacher_details()
teacher3.teacher_mode()
teacher4.teacher_details()
teacher4.teacher_mode()