from flask import Flask, render_template, url_for
# from employees import employees_data

# create the flask app
app = Flask(__name__)

# home page
@app.route("/")
@app.route("/home")
def home():
	return "<h1>Welcome to Home page</h1>"

# about page
@app.route("/about")
def about():
	return "<h1>Welcome to about page</h1>"

# start the app
if __name__ == "__main__":
	app.run(debug=True)