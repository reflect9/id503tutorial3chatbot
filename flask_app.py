# My first AI-infused web app
# Author: Tak Yeon Lee

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def main():
    return render_template("main.html")

@app.route('/about')
def about_page():
    return render_template("about.html")

@app.route('/play')
def play_page():
    return render_template("play.html")
