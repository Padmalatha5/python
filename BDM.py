from flask import Flask, render_template, request, redirect
import mysql.connector

app = Flask(__name__)

# MySQL connection
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="yourpassword",
    database="blood_donor"
)

cursor = db.cursor()

# Home Page
@app.route('/')
def index():
    return render_template('index.html')

# Register Donor
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        name = request.form['name']
        blood_group = request.form['blood_group']
        phone = request.form['phone']
        city = request.form['city']

        query = "INSERT INTO donors (name, blood_group, phone, city) VALUES (%s, %s, %s, %s)"
        values = (name, blood_group, phone, city)

        cursor.execute(query, values)
        db.commit()

        return redirect('/donors')

    return render_template('register.html')

# View Donors
@app.route('/donors')
def donors():
    cursor.execute("SELECT * FROM donors")
    data = cursor.fetchall()
    return render_template('donors.html', donors=data)

# Search Donors
@app.route('/search', methods=['POST'])
def search():
    blood_group = request.form['blood_group']
    cursor.execute("SELECT * FROM donors WHERE blood_group=%s", (blood_group,))
    data = cursor.fetchall()
    return render_template('donors.html', donors=data)

if __name__ == '__main__':
    app.run(debug=True)