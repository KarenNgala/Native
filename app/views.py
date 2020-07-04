from app import app
from flask import render_template

@app.route('/')
def homepage():
    print(app.config)
    return render_template("index.html")

@app.route('/articles/<name>')
def articles(name):
    return render_template("articles.html")
