from flask import Flask

app = Flask(__name__)

@app.route("/")
def homepage():
    return "Welcome to dis homepage"

@app.route("/bmi/<int:weight>/<int:height>")
def bmi(weight, height):
    bmi = weight/((height/100)**2)
    if bmi < 16:
        return "Serverly underweight"
    elif 16 <= bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 25:
        return "Normal"
    elif 25 <= bmi < 30:
        return "Overweight"
    elif 30 <= bmi:
        return "Obese"


if __name__ == "__main__":
    app.run(debug = True)