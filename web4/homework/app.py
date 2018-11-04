from flask import Flask, render_template, request
import mlab
from river import River

app = Flask(__name__)
mlab.connect()


@app.route("/river/<continent>")
def river_continent(continent):
    river_list = River.objects(continent = continent)
    return render_template("river_continent.html", Africa_river = river_list)

@app.route("/river/<int:length>")
def river_length(length):
    river_list = River.objects(continent = "S. America", length__lt = length)
    return render_template("river_length.html", river_short = river_list)

if __name__ == "__main__":
    app.run(debug=True)