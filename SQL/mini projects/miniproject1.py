from miniproject import Databass

def main():
    db = Databass()

    while True:
        print("\n ### College Admission Portal ###")
        print("1. Add Student")
        print("2. Apply for Applications")
        print("3. View Applications")
        print("4. Approve Applications")
        print("5. Reject Applications")
        print("6. Exit")

        try:
            choice = int(input("Enter your choice based on the above instructions: "))
        except:
            print("please enter a number from 1 to 6.")
            continue

        if choice == 1:
            name = input("Enter name: ")
            email = input("Enter email: ")
            phone = input("Enter phone: ")
            city = input("Enter city: ")
            db.add_student(name, email, phone, city)

        elif choice == 2:
            student_id = int(input("Student ID: "))
            course = input("Course: ")
            marks = int(input("Marks: "))
            db.apply_for_admission(student_id, course, marks)

        elif choice == 3:
            apps = db.view_all_applications()
            print("This is the retrieval data:")
            for a in apps:
                print(a)

        elif choice == 4:
            ap_id = int(input("Application ID: "))
            db.update_status(ap_id, "Approved")

        elif choice == 5:
            ap_id = int(input("Application ID: "))
            db.update_status(ap_id, "Rejected")

        elif choice == 6:
            db.close()
            print("Bye 👋")
            break

        else:
            print("Invalid choice, Try picking from 1 to 6.")

if __name__ == "__main__":
    main()
