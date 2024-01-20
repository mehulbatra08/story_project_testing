from flask import Flask,render_template
import random

app = Flask(__name__)


@app.route('/')
def helloworld():
    when = ["Yesterday","Last Month","Last Year","Few Days Ago","Few Months Ago"]
    whom = ["Two Friends","Two People","A Couple","A group of Friends"]
    why = ["Navratri","Diwali","Holi"]
    randomwhom = random.choice(when) + " "+ random.choice(whom)  + " " + "were  dancing on" + " " +random.choice(why)
    return render_template("index.html",randomwhom=randomwhom)

if __name__ == ("__main__"):
    app.run(debug = True)

