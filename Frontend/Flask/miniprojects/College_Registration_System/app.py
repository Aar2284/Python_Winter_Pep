from flask import Flask, render_template, request, redirect

app = Flask(__name__)

students = []

courses_list = [
    "Computer Science",
    "Information Technology",
    "Mechanical Engineering",
    "Civil Engineering",
    "Electrical Engineering",
    "Business Administration",
    "Graphic Design"
]

@app.route('/')

def home():
    return redirect('/register')

@app.route('/register', methods=['GET', 'POST'])

def register():
    error = None
    
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        course = request.form.get('course')

        if not name or not email or not course:
            error = "Error: All fields are required!"

        elif '@gmail.com' not in email:
            error = "Error: Only @gmail.com addresses are accepted!"

        else:
            new_student = {
                "name": name,
                "email": email,
                "course": course
            }
            students.append(new_student)
            return redirect('/students')

    return render_template('register.html', error=error, courses=courses_list)

@app.route('/students')

def show_students():
    return render_template('students.html', students=students)

if __name__ == '__main__':
    app.run(debug=True)