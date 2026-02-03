import mysql.connector as connector
print("MySQL connector imported successfully")

class Databass:
    def __init__(self):
        self.con = connector.connect(
            host="localhost",
            user="root",
            password="1234",
            database="new_db"
        )

        self.cur = self.con.cursor()

        
        query = """
        CREATE TABLE IF NOT EXISTS students(
            student_id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(50),
            email VARCHAR(50),
            phone VARCHAR(15),
            city VARCHAR(30)
        )
        """
        self.cur.execute(query)

        
        query = """
        CREATE TABLE IF NOT EXISTS applications(
            app_id INT AUTO_INCREMENT PRIMARY KEY,
            student_id INT,
            course VARCHAR(50),
            marks INT,
            status VARCHAR(15) DEFAULT 'Pending',
            FOREIGN KEY(student_id) REFERENCES students(student_id)
        )
        """
        self.cur.execute(query)

        self.con.commit()
        print("Tables ready")

    
    def add_student(self, name, email, phone, city):
        query = f"""
        INSERT INTO students(name, email, phone, city)
        VALUES('{name}', '{email}', '{phone}', '{city}')
        """
        self.cur.execute(query)
        self.con.commit()
        print("Student added successfully")

    def apply_admission(self, sid, course, marks):
        query = f"""
        INSERT INTO applications(student_id, course, marks)
        VALUES({sid}, '{course}', {marks})
        """
        self.cur.execute(query)
        self.con.commit()
        print("Admission applied successfully")

    def view_applications(self):
        self.cur.execute("""
        SELECT a.app_id, s.name, a.course, a.marks, a.status
        FROM applications a
        JOIN students s ON a.student_id = s.student_id
        """)
        for row in self.cur.fetchall():
            print(row)

    def update_status(self, app_id, status):
        self.cur.execute(
            f"UPDATE applications SET status='{status}' WHERE app_id={app_id}"
        )
        self.con.commit()
        print("Application status updated")
