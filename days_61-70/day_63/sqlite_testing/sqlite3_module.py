import sqlite3

# create database (if there isn't one already)
# this will put a file in the root project directory
db = sqlite3.connect(database="books-collection.db")

# create cursor to control database
cursor = db.cursor()
# cursor.execute("CREATE TABLE books (id INTEGER PRIMARY KEY, title varchar(250) NOT NULL UNIQUE, author varchar(250) NOT NULL, rating FLOAT NOT NULL)")

cursor.execute(
    "INSERT INTO books VALUES (1, 'Harry Potter', 'J.K. Rowling', '9.3')")
db.commit()
