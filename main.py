from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html") # This is the path to the html file. flask knows the folder for html documents

@app.route("/", methods=["POST"])
def home_post():
    # print(request.form)
    dim1 = request.form["first_dim"]
    dim2 = request.form["second_dim"]
    dim3 = request.form["third_dim"]
    volume =  dim1 * dim2 * dim3

    print("Get post request")
    return render_template("index.html")

app.run(host="0.0.0.0")

