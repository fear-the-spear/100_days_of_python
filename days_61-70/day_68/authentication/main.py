from flask import Flask, render_template, request, url_for, redirect, flash, send_from_directory
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin, login_user, LoginManager, login_required, current_user, logout_user

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret-key-goes-here'
app.config['UPLOAD_FOLDER'] = 'static/files'

# USER AUTH MANAGEMENT
login_manager = LoginManager()
login_manager.init_app(app)

# CONNECT TO DB
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
db = SQLAlchemy()
db.init_app(app)


# CREATE TABLE IN DB
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))


with app.app_context():
    db.create_all()


@login_manager.user_loader
def load_user(user_id):
    return db.get_or_404(User, user_id)


@app.route('/')
def home():
    return render_template("index.html", logged_in=current_user.is_authenticated)


@app.route('/register', methods=["GET", "POST"])
def register():
    if request.method == "POST":
        email = request.form['email']
        result = db.session.execute(db.select(User).where(User.email == email))
        # NOTE: email in database is unique so will only have one result
        user = result.scalar()
        if user:
            # user already exists
            flash("You've already signed up with that email - log in instead!")
            return redirect(url_for('login'))

        # hashing and salting the password entered by the user
        hash_and_salted_password = generate_password_hash(
            password=request.form['password'],
            method='pbkdf2',
            salt_length=8
        )
        # storing the hashed password in the database
        new_user = User(
            name=request.form['name'],
            email=request.form['email'],
            password=hash_and_salted_password
        )

        db.session.add(new_user)
        db.session.commit()

        # log in and authenticate user after adding details to database
        login_user(new_user)

        return redirect('secrets')
    return render_template("register.html", logged_in=current_user.is_authenticated)


@app.route('/login', methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form['email']
        password = request.form['password']

        # find user by email entered
        result = db.session.execute(db.select(User).where(User.email == email))
        user = result.scalar()

        # email doesn't exist or password incorrect
        if not user:
            flash("That email does not exist - please try again.")
            return redirect(url_for('login'))
        elif not check_password_hash(user.password, password):
            flash("Password incorrect - please try again.")
            return redirect(url_for('login'))
        else:
            login_user(user)
            return redirect(url_for('secrets'))

    return render_template("login.html", logged_in=current_user.is_authenticated)


# only logged in users can access the route
@app.route('/secrets')
@login_required
def secrets():
    print(current_user.name)
    # passing the name from the current_user
    return render_template("secrets.html", name=current_user.name, logged_in=True)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('home'))


# only logged in users can download the pdf
@app.route('/download')
@login_required
def download():
    return send_from_directory(
        app.config["UPLOAD_FOLDER"], "cheat_sheet.pdf"
    )


if __name__ == "__main__":
    app.run(debug=True)
