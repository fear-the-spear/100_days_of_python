from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///books.db"
db = SQLAlchemy()
db.init_app(app)
# all_books = []


class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    author = db.Column(db.String(250), nullable=False)
    rating = db.Column(db.Float, nullable=False)


with app.app_context():
    db.create_all()


@app.route('/', methods=["GET", "POST"])
def home():

    with app.app_context():
        result = db.session.execute(db.select(Book).order_by(Book.id))
        all_books = result.scalars().fetchall()
        length = len(all_books)
    return render_template("index.html", books=all_books, num_of_books=length)


@app.route('/edit', methods=["GET", "POST"])
def edit_rating():
    if request.method == "POST":
        new_rating = request.form["new rating"]
        book_id = request.args.get('id')
        book_to_update = db.get_or_404(Book, book_id)
        book_to_update.rating = float(new_rating)
        db.session.commit()
        # Use the redirect method from flask to redirect to another route
        # e.g. in this case to the home page after the form has been submitted
        return redirect(url_for('home'))
    book_id = request.args.get('id')
    book = db.get_or_404(Book, book_id)
    title = book.title
    rating = book.rating
    return render_template("edit.html", title=title, rating=rating)


@app.route("/add", methods=["GET", "POST"])
def add():
    if request.method == "POST":
        with app.app_context():
            new_book = Book(
                title=request.form["title"],
                author=request.form["author"],
                rating=request.form["rating"]
            )
        db.session.add(new_book)
        db.session.commit()
        # Use the redirect method from flask to redirect to another route
        # e.g. in this case to the home page after the form has been submitted
        return redirect(url_for('home'))
    return render_template("add.html")


@app.route("/delete")
def delete():
    book_id = request.args.get('id')
    book_to_delete = db.get_or_404(Book, book_id)
    db.session.delete(book_to_delete)
    db.session.commit()
    return redirect(url_for('home'))


if __name__ == "__main__":
    app.run(debug=True)
