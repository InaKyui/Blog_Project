from app import app
from flask import render_template, url_for

@app.route("/")
@app.route("/index")
def index():
    user = { "username": "InaKyui" }
    return render_template("welcome.html", title="InaKyui", user=user)

@app.route("/home")
def home():
    return render_template("base.html", title="Home")