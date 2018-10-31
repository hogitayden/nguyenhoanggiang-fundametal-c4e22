from flask import Flask, render_template,  request
apple = Flask(__name__)

@apple.route('/')
def home():
    return('homie')

@apple.route('/bike_rental', methods=['GET', 'POST'])
def bike_rental():
    if request.method == 'GET':
        return render_template('bike_rental.html')
    elif request.method == 'POST':
        form = request.form
        print(form)
        return "YOu GOd"


if __name__ == "__main__":
    apple.run(debug = True)