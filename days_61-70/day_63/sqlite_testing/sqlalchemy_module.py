from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import sqlalchemy as sa

# create the app
app = Flask(__name__)

# CREATE DATABASE
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///new-books-collection.db"

# create the extension
db = SQLAlchemy()
# Initialize the app with the extension
db.init_app(app)


# CREATE TABLE
class Book(db.Model):
    id = sa.Column(sa.Integer, primary_key=True)
    title = sa.Column(sa.String(250), unique=True, nullable=False)
    author = sa.Column(sa.String(250), nullable=False)
    rating = sa.Column(sa.Float, nullable=False)

    # OPTIONAL: this will allow each book object to be identified by its
    # when printed
    def __repr__(self):
        return f'<Book {self.title}>'


# Create table schema in the database. Requires application context.
with app.app_context():
    db.create_all()

# CREATE RECORD
with app.app_context():
    new_book = Book(id=1, title="Harry Potter and the Chamber of Secrets",
                    author="J.K. Rowling", rating=9.3)
    db.session.add(new_book)
    db.session.commit()
