from flask import Flask, render_template, request
from api import *
app = Flask(__name__)

@app.route('/',methods=["GET"])
def index():
    return render_template("index.html")

@app.route('/',methods=["POST"])
def hi():
    barcode = request.form.get("barcode")
    html_barcode_info = barcode_info(barcode)
    print(html_barcode_info)
    return render_template("index.html",html_barcode_info=html_barcode_info)
if __name__ == '__main__':
    app.run(debug=True)

# barcode_info(8076800195033)
