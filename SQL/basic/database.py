import mysql.connector as connector
print("Mysql connector imported seuccessfully")

class DatabaseConnection:
    def __init__(self):
        
        self.con=connector.connect(
            host="localhost",
            user="root",
            password="Aaryan1234",
            database="prep"
        )
        query="CREATE TABLE IF NOT EXISTS student(id INT PRIMARY KEY,name VARCHAR(20), age INT)"

        cur= self.con.cursor()
        cur.execute(query)
        print("Student table created")

    def insert_student(self, id, name, age):
        query=f"INSERT INTO student(id, name, age) VALUES({id}, '{name}', {age})"
        cur= self.con.cursor()
        cur.execute(query)
        self.con.commit()
        print("Student data inserted successfully")

    def fetch_students(self):
        query="SELECT * FROM student"
        cur= self.con.cursor()
        cur.execute(query)
        for row in cur.fetchall():
            print(row)

    def update_student(self, id, name, age):
        query=f"UPDATE student SET name='{name}', age={age} WHERE id={id}"
        cur= self.con.cursor()
        cur.execute(query)
        self.con.commit()
        print("Student data updated successfully")

    def delete_student(self, id):
        query=f"DELETE FROM student WHERE id={id}"
        cur= self.con.cursor()
        cur.execute(query)
        self.con.commit()
        print("Student data deleted successfully") 


dbc=DatabaseConnection()
dbc.fetch_students()
print("Done")
