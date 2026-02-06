from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])

def form():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')

        conn = sqlite3.connect('first.db')
        cursor = conn.cursor()

        cursor.execute("INSERT INTO users (name, email) VALUES (?, ?)", (name, email))

        conn.commit()
        conn.close()

        return "Data Inserted Successfully!"

    return render_template('form.html')

if __name__ == '__main__':
    app.run(debug=True)