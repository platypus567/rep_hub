from flask import Flask, render_template, redirect, url_for
import requests
from flask_wtf import FlaskForm
from flask_bootstrap import Bootstrap
from wtforms import StringField, SubmitField, IntegerField
from wtforms.validators import DataRequired, URL
from wtforms.widgets import html5

#INSTALL THESE PACKAGES OR IT WON'T WORK

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap(app)

#setting vars for the app to work above

class SearchForm(FlaskForm):
    user_search = StringField("Search:", validators=[DataRequired()])
    submit = SubmitField("Search")

# form class, only two fields because it's a search bar, DO NOT CHANGE


@app.route("/")
def home():
    form = SearchForm()
    return render_template("index.html", form=form)
#home route, self explanatory


@app.route("/search", methods=['POST'])
def find_user():
    form = SearchForm()
    if form.validate_on_submit():
     print("True")
     name_searched = form.user_search.data
     response = requests.get(f"https://api.github.com/users/{name_searched}")
     data = response.json()
     print(data)
     key = "message"
     if key in data:
         return render_template('error.html')
     else:
        return render_template("search-result.html",form=form, username=name_searched, data=data)
    
#API call should be made, return response as JSON and we handle data on the front end side


@app.errorhandler(404)
def page_not_found(e):
    return render_template('error.html'), 404
#error page 404


if __name__ == "__main__":
    app.run(debug=True)