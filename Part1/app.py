from flask import Flask

app = Flask(__name__)

@app.route("/")
@app.route("/home")
def home():
    return "<h1>welcome to the home page !!!</h1>"

@app.route("/welcome/<name>")
def welcome(name):
    return f"<h1>hi {name.title()}, you're welcome to the page!!!</h1>"

@app.route("/addition/<int:num>")
def addition(num):
    return f"<h1>Input is {num}, Output is {num+10}</h1>"

@app.route("/addition_two/<int:num1>/<int:num2>")
def addition_two(num1, num2):
    return f"<h1>{num1} + {num2} is {num1+num2}</h1>"

@app.route("/about")
def about():
    return "<h1>welcome to the about page !!!</h1>"

if __name__ == "__main__":
    app.run(debug=True)