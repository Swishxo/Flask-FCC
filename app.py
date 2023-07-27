#imports needed for flask
from flask import Flask, render_template, request

#passed the name of the module or package of the application
app = Flask(__name__)

#decerator used to map function to a particular part of url
@app.route("/")
def index():
    if "name" in request.args:#if there is a name in request.args
        name = request.args["name"]#get name from HTTP and store in var (name)
    else:
        name = "World" #if no HTTP (name) provided. 
        #'render_template()' also takes named args of your choice to pass to template dir files
    return render_template("index.html", placeholder=name)#finds the html given and displays to user








if __name__ == "__main__":
    app.run(debug=True) #stops the need to close server