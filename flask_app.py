# My first AI-infused web app
# Author: Tak Yeon Lee

from flask import Flask, render_template, request
from PlayTennisClassifier import createClassifier
import json

app = Flask(__name__)
features = {
    "outlook": ["Sunny","Overcast","Rain"],
    "temp": ["Cool","Mild","Hot"],
    "humidity": ["High","Normal"],
    "wind": ["Weak","Strong"],
    "play": ["No","Yes"]
}
def feature2int(f):
    # Converting feature text into int
    for column, flist in features.items():
        if f in flist:
            return flist.index(f)  #  1

@app.route('/')
def main():
    return render_template("main.html")

@app.route('/about')
def about_page():
    return render_template("about.html")

@app.route('/play')
def play_page():
    return render_template("play.html")

@app.route('/classifyUI')
def classifyUI_page():
    return render_template("classifyUI.html", features=features)


@app.route('/classify')
def classify():
    # Read parameter of the request
    featuresToPredict = request.args.get("features")  #
    rf_dict = json.loads(featuresToPredict)   # {"outlook":"Overcast","temp":"Mild","humidity":"Normal","wind":"Strong"}
    rf_list = [rf_dict["outlook"], rf_dict["temp"], rf_dict["humidity"], rf_dict["wind"]]  # ["Overcast", "Mild", "Normal", "Strong"]
    print(rf_list) #  ['Overcast', 'Mild', 'Normal', 'Strong']
    rf_list_int = []      # [1,1,1,1]
    for f in rf_list:
        rf_list_int.append(feature2int(f))
    print(rf_list_int)  # [1,1,1,1]

    # Create a Classifier
    playTennisClassifier = createClassifier(feature2int)
    predictionResult = playTennisClassifier.predict([rf_list_int])  # [[1,1,1,1]]  result: [1]

    return json.dumps(predictionResult.tolist())

@app.route('/chatbot')
def chatbot():
    return render_template("chatbot.html")

def call_openweather_api(city):
    import requests
    openweather_api_key= "069839f84604112570cb8cb4a20b9048"
    openweather_url = "http://api.openweathermap.org/data/2.5/weather?q="+city+"&appid="+openweather_api_key
    response = requests.get(openweather_url).json()
    if response.get('cod') != 200:
        message = response.get('message', '')
        return f'Could not get the current weather at {city}. Error message = {message}'

    current_weather = response['weather'][0]['description']
    if current_weather:
        return f'Current weather at {city} is {current_weather}.'
    else:
        return f'Error getting weather for {city}'

@app.route('/webhook_weather', methods=['POST'])
def webhook_weather():
    data = request.get_json()
    location_city = data["queryResult"]["parameters"]["geo-city"]
    weather = call_openweather_api(location_city)
    return {
        "fulfillmentText": weather,
        "fulfillmentMessages": [
            {
            "text": {
                "text": [
                    weather
                    ]
                }
            }
        ]
    }

@app.route('/dialogflow', methods=['POST'])
def dialogflow():
    from DialogflowIntentDetector import detect_intent_texts

    data = request.get_json()
    queryText = data["queryText"]
    session_id = "123456789";
    project_id = "firstbot-nbnd";
    responses = detect_intent_texts(project_id, session_id, [queryText], "en")
    return json.dumps(responses)
