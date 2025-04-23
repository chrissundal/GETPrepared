from flask import Flask, redirect, url_for, render_template, request, session, flash
import os
from dotenv import load_dotenv
from datetime import timedelta
from flask_sqlalchemy import SQLAlchemy

load_dotenv()

app = Flask(__name__, static_folder='static')
app.secret_key = os.environ.get('SECRET_KEY')
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.permanent_session_lifetime = timedelta(days=7)

db = SQLAlchemy(app)

class users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    firstname = db.Column(db.String(100), nullable=False)
    lastname = db.Column(db.String(100), nullable=False)
    admin = db.Column(db.Boolean, nullable=False, default=False)

    def __init__(self, username, email, password, firstname, lastname, admin):
        self.username = username
        self.email = email
        self.password = password
        self.firstname = firstname
        self.lastname = lastname
        self.admin = admin

test = 'hei på deg'

@app.route('/', methods=['GET', 'POST'])
def home():
    return redirect(url_for("user_object"))

@app.route('/register')
def register():
    return redirect(url_for("home"))

@app.route('/next')
def neste():
    return render_template("neste.html")
@app.route('/old/<name>') # tar verdi og limer inn i user som en slags prop
def old_user(name):
    return render_template("oldindex.html", content=[name, 'chris', 'terje'], text='hvordan går det?', test=test)

@app.route('/admin')
def admin():
    return redirect(url_for("user", name="Admin"))
# @app.route('/admin')
# def admin():
#     return redirect(url_for("home"))

@app.route('/admin/users')
def users_admin():
    return render_template("admin.html", user=session['user'], users=users.query.all())

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        session.permanent = True
        username = request.form['nm']
        password = request.form['pw']
        found_user = users.query.filter_by(username=username, password=password).first()

        if found_user:
            user_dict = {
                'username': found_user.username,
                'email': found_user.email,
                'firstname': found_user.firstname,
                'lastname': found_user.lastname,
                'admin': found_user.admin
            }
            session['user'] = user_dict
        else:
            usr = users(username, "", password, "", "", False)
            db.session.add(usr)
            db.session.commit()

            user_dict = {
                'username': usr.username,
                'email': usr.email,
                'firstname': usr.firstname,
                'lastname': usr.lastname,
                'admin': usr.admin
            }
            session['user'] = user_dict

            flash(f'Bruker {username} ble laget', 'info')
            return redirect(url_for("login"))

        flash(f'Velkommen {username}', 'info')
        return redirect(url_for("user_object"))
    else:
        if 'user' in session:
            flash('Du er allerede logget inn', 'info')
            return redirect(url_for("user_object"))
        return render_template("login.html")


@app.route('/user', methods=['GET', 'POST'])
def user_object():
    user = None
    if 'user' in session:
        user = session['user']
        if request.method == 'POST':
            email = request.form['email']
            firstname = request.form['firstname']
            lastname = request.form['lastname']

            found_user = users.query.filter_by(username=user['username']).first()
            found_user.email = email
            found_user.firstname = firstname
            found_user.lastname = lastname
            db.session.commit()
            full_user = {'username': found_user.username, 'email': found_user.email, 'firstname': found_user.firstname, 'lastname': found_user.lastname, 'admin': found_user.admin}
            session['user'] = full_user
            flash("Bruker er oppdatert", "info")

        user = session['user']
        return render_template("user.html", user=user)
    else:
        flash('Du er ikke logget inn', 'info')
        return redirect(url_for("login"))
@app.route('/logout')
def logout():
    if 'user' in session:
        session.pop('user', None)
        flash('Du har blitt logget ut', 'info')
        return redirect(url_for("login"))
    else:
        flash('Du er ikke logget inn', 'info')
        return redirect(url_for("login"))

if __name__ == '__main__':
    db.create_all()
    app.run()