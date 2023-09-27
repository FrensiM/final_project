from flask import Flask, url_for, render_template, request, redirect, session
from database import get_database
from werkzeug.security import generate_password_hash, check_password_hash
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(24)

@app.route("/")
def index():
    return render_template('home.html')

@app.route("/login")
def login():

    error = None

    if request.method == 'POST':
        name = request.form['name']
        password = request.form['password']
        db = get_database()
        user_cursor = db.execute('select * from users where name = ?', [name])
        user = user_cursor.fetchone()

        if user:
            if check_password_hash(user['password'], password):
                session['user'] = user['name']
                return redirect(url_for('dashboard'))
            else:
                error = "Password did not match"
    return render_template('login.html', loginerror = error)

@app.route("/register", methods=["POST", "GET"])
def register():
    if request.method == 'POST':
        db = get_database()
        name = request.form['name']
        password = request.form['password']
        hashed_password = generate_password_hash(password)

        dbuser_cur = db.execute('select * from users where name = ?', [name])
        existing_username = dbuser_cur.fetchone()
        if existing_username:
            return render_template('register.html', registererror = ', User already taken try new username/email')
        
        db.execute('INSERT INTO users( name, password) values (?, ?)',[name, hashed_password])
        db.commit()
        return redirect(url_for('index'))
    return render_template('register.html')

@app.route("/addneweuser")
def add_new():
    return render_template('addnewuser.html')

@app.route("/update")
def update_user():
    return render_template('updateuser.html')

@app.route("/dashboard")
def dashboard():
    return render_template('dashboard.html')

@app.route("/singleuser")
def singleuser():
    return render_template('singleuser.html')

def logout():
    render_template('homepage.html')

if __name__ == '__main__':
    app.run(debug = True)
    
