from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html") # This is the path to the html file. flask knows the folder for html documents

@app.route("/", methods=["POST"])
def home():
    print("Get post request")
    return render_template("index.html")

app.run(host="0.0.0.0")

