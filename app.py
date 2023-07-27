from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

#request.args.get() --> .get()
@app.route("/greet")
def greet():
    return render_template("greet.html", name = request.args.get("name", "world"))








if __name__ == "__main__":
    app.run(debug=True)