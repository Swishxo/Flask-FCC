#imports needed for flask
from flask import Flask, render_template, request

#passed the name of the module or package of the application
app = Flask(__name__)

#decerator used to map function to a particular part of url
@app.route("/")
def index():
    return "Hello, World"

if __name__ == "__main__":
    app.run(debug=True) #stops the need to close server