# classes

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

print("--------------- Class Example -----------------")
student1.student_detials()
student2.student_detials()

# classes using encapsulation in bank account data

class Bank:
    def __init__(self, acc_num, cash, interest):
        self.acc_num = acc_num      # Public: Accessible from anywhere
        self._cash = cash           # Protected: Convention says "don't touch outside class"
        self.__interest = interest  # Private: Python hides this from easy access

    def deposit(self, amount):
        self._cash += amount
        print(f"Deposited {amount}. New balance is {self._cash}")

    def withdraw(self, amount):
        
        if amount > self._cash:
            print("Insufficient funds")
        else:
            self._cash -= amount
            print(f"Withdrew {amount}. New balance is {self._cash}")

    def add_interest(self):
        
        interest_amt = (self._cash * self.__interest / 100) 
        self._cash += interest_amt
        print(f"Interest added. New balance is {self._cash}")

# --- Testing ---
#instance
account1 = Bank('123456790', 1000, 5)
account2 = Bank('234567887', 65000, 8)
account3 = Bank('456789444', 45000, 4)

print("------------------------ Bank Account Operations -----------------")
account1.deposit(500)
account2.withdraw(35000)
account3.add_interest()

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

print("--------------- Inheritance Example -----------------")
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

print("--------------- Teacher Inheritance Example -----------------")
teacher1.teacher_details()
teacher1.teacher_mode()
teacher2.teacher_details()
teacher2.teacher_mode()
teacher3.teacher_details()
teacher3.teacher_mode()
teacher4.teacher_details()
teacher4.teacher_mode()