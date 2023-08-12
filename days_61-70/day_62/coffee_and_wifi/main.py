from flask import Flask, render_template
from flask_bootstrap import Bootstrap5
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired, URL, Length
from wtforms.fields import URLField
import csv

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
bootstrap = Bootstrap5(app)

# Exercise:
# add: Location URL, open time, closing time, coffee rating, wifi rating, power outlet rating fields
# make coffee/wifi/power a select element with choice of 0 to 5.
# e.g. You could use emojis ☕️/💪/✘/🔌🛜
# make all fields required except submit
# use a validator to check that the URL field has a URL entered.
# ---------------------------------------------------------------------------


class CafeForm(FlaskForm):
    cafe = StringField('Cafe name', validators=[
        DataRequired(message="TEST: WRONG")])
    location = URLField(
        'Location URL', validators=[URL(message="TEST: WRONG")])
    open_time = StringField('Open', validators=[DataRequired(), Length(5)])
    close_time = StringField('Close', validators=[DataRequired(), Length(5)])
    coffee_rating = SelectField('Coffee Rating', validators=[DataRequired(), Length(1)], choices=[
                                '', '☕️', '☕️☕️', '☕️☕️☕️', '☕️☕️☕️☕️', '☕️☕️☕️☕️☕️'])
    wifi_rating = SelectField('Wifi Rating', validators=[DataRequired(), Length(1)], choices=[
                              '', '🛜', '🛜🛜', '🛜🛜🛜', '🛜🛜🛜🛜', '🛜🛜🛜🛜🛜'])
    outlet_rating = SelectField('Outlet Rating', validators=[DataRequired(), Length(1)], choices=[
                                '', '🔌', '🔌🔌', '🔌🔌🔌', '🔌🔌🔌🔌', '🔌🔌🔌🔌🔌'])
    submit = SubmitField('Submit')

# all Flask routes below


@app.route("/")
def home():
    return render_template("index.html")


@app.route('/add', methods=["GET", "POST"])
def add_cafe():
    form = CafeForm()
    if form.validate_on_submit():
        cafe = form.cafe.data
        url = form.location.data
        open_time = form.open_time.data
        close_time = form.close_time.data
        coffee_rtg = form.coffee_rating.data
        wifi_rtg = form.wifi_rating.data
        outlet_rtg = form.outlet_rating.data
        new_place = [cafe, url, open_time, close_time,
                     coffee_rtg, wifi_rtg, outlet_rtg]
        with open('cafe-data.csv', 'a') as csv_file:
            write_obj = csv.writer(csv_file)
            write_obj.writerow(new_place)
        return render_template("cafes.html")
    # Exercise:
    # Make the form write a new row into cafe-data.csv
    # with   if form.validate_on_submit()
    return render_template('add.html', form=form)


@app.route('/cafes', methods=["GET"])
def cafes():
    with open('cafe-data.csv', newline='', encoding='utf-8') as csv_file:
        csv_data = csv.reader(csv_file, delimiter=',')
        row_data = [row for row in csv_data]
        print(row_data)
    return render_template('cafes.html', cafes=row_data)


if __name__ == '__main__':
    app.run(debug=True)
