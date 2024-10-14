from flask import Flask, render_template, request
from api import *
app = Flask(__name__)

@app.route('/',methods=["GET"])
def hi():
    return render_template("index.html")

@app.route('/',methods)

if __name__ == '__main__':
    app.run(debug=True)