# Load Libraries
import numpy as np
import pandas as pd
from sklearn import metrics, preprocessing
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import classification_report, confusion_matrix
import os

def createClassifier():
    # Let's train a decision tree
    current_path = os.path.dirname(os.path.abspath(__file__))
    df = pd.read_csv(current_path+"/play_tennis.csv")
    string_to_int = preprocessing.LabelEncoder()
    df = df.apply(string_to_int.fit_transform)

    feature_cols = ['outlook', 'temp', 'humidity', 'wind']
    X = df[feature_cols]
    y = df.play

    classifier = DecisionTreeClassifier(criterion="entropy", random_state=100)
    classifier.fit(X,y)
    return classifier

# Let's predict a new feature
# x_new = [[2,1,1,0]]
# print (classifier.predict(x_new))


