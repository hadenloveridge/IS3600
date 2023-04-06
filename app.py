from flask import Flask, render_template
from datetime import date


app = Flask(__name__)

@app.route("/")
def home_page():
    return render_template("index.html")
    
@app.route("/conact")
def contact():
    return render_template("contact.html")
    
@app.route("/gallery")
def gallery():
    return render_template("gallery.html")
    
def todays_date():
    today = date.today()
    str_date = today.strftime('%B %d %Y')
    return "Todays date is " + str_date
