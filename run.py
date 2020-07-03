from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return "Native Homepage"

@app.route('/sources')
def sources():
    return "Source articles"


if __name__ == "__main__":
    app.run(debug=True)