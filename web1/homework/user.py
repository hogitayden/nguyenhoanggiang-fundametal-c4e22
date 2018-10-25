from flask import Flask, render_template

app = Flask(__name__)


@app.route("/user/<username>")
def user(username):
    user = {
    "giang":{
        "name": "Nguyen Hoang Giang",
        "age": 23
    },
    "hanh":{
        "name": "Luong Thi Hanh",
        "age": 23
    },
    "van":{
        "name": "Dinh Thi Van",
        "age": 43
    }
    }
    if username in user.keys():
        return render_template("user.html", profile = user[username])
    else:
        return "User not found"
    
if __name__ == "__main__":
    app.run(debug = True)