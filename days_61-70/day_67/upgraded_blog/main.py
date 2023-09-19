from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, URL
from flask_ckeditor import CKEditor, CKEditorField
from datetime import datetime as dt


app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
ckeditor = CKEditor(app)
bootstrap5 = Bootstrap5(app)


# CONNECT TO DB
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///posts.db'
db = SQLAlchemy()
db.init_app(app)

# CREATE NEW POST FORM


class NewPost(FlaskForm):
    title = StringField(
        label="Blog Post Title",
        validators=[DataRequired()]
    )
    subtitle = StringField(
        label="Blog Post Subtitle",
        validators=[DataRequired()]
    )
    author = StringField(
        label="Author",
        validators=[DataRequired()]
    )
    bg_img = StringField(
        label="Background Image URL",
        validators=[DataRequired(), URL()]
    )
    body = CKEditorField(
        label="Blog Content",
        validators=[DataRequired()]
    )
    submit = SubmitField(label="Post")

# CONFIGURE TABLE


class BlogPost(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    subtitle = db.Column(db.String(250), nullable=False)
    date = db.Column(db.String(250), nullable=False)
    body = db.Column(db.Text, nullable=False)
    author = db.Column(db.String(250), nullable=False)
    img_url = db.Column(db.String(250), nullable=False)


with app.app_context():
    db.create_all()


@app.route('/')
def get_all_posts():
    # TODO: Query the database for all the posts. Convert the data to a python list.
    # DONE DONE DONE DONE DONE DONE DONE DONE DONE DONE DONE DONE DONE DONE DONE
    result = db.session.execute(db.select(BlogPost).order_by(BlogPost.title))
    all_posts = result.scalars()
    posts = [post for post in all_posts]
    return render_template("index.html", all_posts=posts)

# TODO: Add a route so that you can click on individual posts.
# DONE DONE DONE DONE DONE DONE DONE DONE DONE DONE DONE DONE DONE DONE DONE


@app.route('/post/<int:post_id>')
def show_post(post_id):
    # TODO: Retrieve a BlogPost from the database based on the post_id
    # DONE DONE DONE DONE DONE DONE DONE DONE DONE DONE DONE DONE DONE DONE DONE
    post = db.session.execute(
        db.select(BlogPost).where(BlogPost.id == post_id))
    requested_post = post.scalar()
    return render_template("post.html", post=requested_post)


# TODO: add_new_post() to create a new blog post
@app.route('/new-post', methods=["GET", "POST"])
def add_new_post():
    h1_tag = "New Post"
    heading = "Create a new and meaningful blog post today."
    form = NewPost()
    if request.method == "POST":
        date = dt.now().strftime("%B %d, %Y")
        # add time to database at a later date
        #   code below looks like this: 10:45 PM
        # time = dt.now().strftime("%I:%M %p")
        new_post = BlogPost(
            title=form.title.data,
            subtitle=form.subtitle.data,
            author=form.author.data,
            img_url=form.bg_img.data,
            body=form.body.data,
            date=date
        )
        db.session.add(new_post)
        db.session.commit()
        return redirect(url_for('get_all_posts'))
    return render_template("make-post.html", form=form, h1_tag=h1_tag, heading=heading)

# TODO: edit_post() to change an existing blog post


@app.route("/post/<int:post_id>/edit", methods=["GET", "POST"])
def edit_post(post_id):
    h1_tag = "Edit Post"
    heading = "Change the details of your existing post."
    post = db.session.execute(db.select(BlogPost).where(
        BlogPost.id == post_id)).scalar()
    edit_form = NewPost(
        title=post.title,
        subtitle=post.subtitle,
        author=post.author,
        bg_img=post.img_url,
        body=post.body
    )
    if edit_form.validate_on_submit():
        post.title = edit_form.title.data
        post.subtitle = edit_form.subtitle.data
        post.author = edit_form.author.data
        post.img_url = edit_form.bg_img.data
        post.body = edit_form.body.data
        db.session.commit()
        return redirect(url_for('show_post', post_id=post.id))
    return render_template('make-post.html', form=edit_form, h1_tag=h1_tag, heading=heading)

# TODO: delete_post() to remove a blog post from the database


@app.route("/delete/<post_id>")
def delete_post(post_id):
    post_to_delete = db.session.execute(
        db.select(BlogPost).where(BlogPost.id == post_id)).scalar()
    db.session.delete(post_to_delete)
    db.session.commit()
    return redirect(url_for('get_all_posts'))

# Below is the code from previous lessons. No changes needed.


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


if __name__ == "__main__":
    app.run(debug=True, port=5003)
