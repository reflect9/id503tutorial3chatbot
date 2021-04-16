# My first AI-infused web app
# Author: Tak Yeon Lee

from flask import Flask, render_template, request
from PlayTennisClassifier import createClassifier
import json

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

@app.route('/classify')
def classify():
    # Read parameter of the request
    featuresToPredict = request.args.get("features")  # http://reflect9.pythonanywhere.com/classify?features=[[2,0,1,1],[2,0,1,0]]
    fArr = json.loads(featuresToPredict)

    # Create a Classifier
    playTennisClassifier = createClassifier()
    predictionResult = playTennisClassifier.predict(fArr)

    return "Input Feature: " + featuresToPredict + ", Prediction Result: " + str(predictionResult)