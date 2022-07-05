from flask import Flask, render_template, redirect, url_for
from flask_wtf import FlaskForm
from flask_bootstrap import Bootstrap
from wtforms import StringField, SubmitField, IntegerField
from wtforms.validators import DataRequired, URL
from wtforms.widgets import html5
app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap(app)

class SearchForm(FlaskForm):
    user_search = StringField("Search:", validators=[DataRequired()])
    submit = SubmitField("Search")



@app.route("/")
def home():
    form = SearchForm()
    return render_template("index.html", form=form)

@app.route("/search", methods=['POST'])
def find_user():
    form = SearchForm()
    if form.validate_on_submit():
     print("True")
     name_searched = form.user_search.data
     return render_template("search-result.html",form=form, name=name_searched)
    

@app.errorhandler(404)
def page_not_found(e):
    return render_template('error.html'), 404




if __name__ == "__main__":
    app.run(debug=True)