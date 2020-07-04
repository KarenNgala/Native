from app import app
from flask import render_template

@app.route('/')
def index():
    print(app.config)
    return render_template("index.html")

@app.route('/sources/<name>')
def sources(name):
    return render_template("sources.html")
