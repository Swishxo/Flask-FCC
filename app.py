from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])#this url route now takes both "GET" and "POST"
def index():
    if request.method == "GET":
        return render_template("index.html")
    elif request.method == "POST":
        #when using "POST" on flask you must use request.form.get() to get data  
        return render_template("greet.html", name=request.form.get("name", "world"))










if __name__ == "__main__":
    app.run(debug=True)