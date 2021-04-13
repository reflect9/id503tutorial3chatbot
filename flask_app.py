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
def classifyAPI():
    featuresToPredictString = request.args.get("features")
    featuresToPredict = json.loads(featuresToPredictString)
    # print(featuresToPredict)
    # return "Feature Length: " + str(len(featuresToPredict))

    classifier = createClassifier()
    predictionResult = classifier.predict(featuresToPredict)
    return "Feature: "+str(featuresToPredict) + "\nPrediction: " + str(list(predictionResult))