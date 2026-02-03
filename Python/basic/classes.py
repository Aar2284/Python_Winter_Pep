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