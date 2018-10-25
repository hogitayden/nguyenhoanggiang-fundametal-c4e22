from flask import Flask, redirect
app = Flask(__name__)

@app.route("/")
def homepage():
    return "Welcome to dis homepage"

@app.route("/about_me")
def about_me():
    return "My name is Hogi. I just travel to dis world to meet my lover."

@app.route("/school")
def school():
    return redirect("http://techkids.vn")

if __name__ == "__main__":
    app.run(debug=True)


