from flask import Flask, request, render_template

app = Flask(__name__)
@app.route('/', methods=['POST', 'GET'])

def login():
    error = None

    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        if not username or not password:
            error = 'Both fields are required. Please fill them out.'
        elif username != 'admin' or password != 'password123':
            error = 'Invalid credentials. Please try again.'
        else:
            return "Login successful! Welcome, admin."
    return render_template('login.html', error=error)

if __name__ == '__main__':
    app.run(debug=True)