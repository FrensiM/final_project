from flask import Flask, url_for, render_template, request, redirect
from database import get_database
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('home.html')

@app.route("/login")
def login():
    return render_template('login.html')

@app.route("/register", methods=["POST", "GET"])
def register():
    if request.method == 'POST':
        name = request.form['name']
        password = request.form['password']
        hashed_password = generate_password_hash(password)

        db = get_database()
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
    
