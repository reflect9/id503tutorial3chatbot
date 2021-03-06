import numpy as np  # library for data analysis
import pandas as pd  # library for data analysis
import os   # file and directory structure
from sklearn import metrics, preprocessing  # Python's most popular ML library
from sklearn.tree import DecisionTreeClassifier

def createClassifier(feature2int):
    # Step 1. Loading a dataset(play_tennis.csv) for training model
    current_path = os.path.dirname(os.path.abspath(__file__)) # absolute path to the current file
    df = pd.read_csv(current_path + "/play_tennis.csv")  # df: dataframe

    # Step 2. Cleaning dataset > Preparing X(features), and y(labels)
    df_int = df.applymap(feature2int)
    print("Converted Play Tennis")
    print(df_int)

    feature_cols = ["outlook", "temp", "humidity", "wind"]
    X = df_int[feature_cols]  # X is features. Extracted from df, containing columns that are in feature_cols
    y = df_int.play  # y is the label

    # Step 3. Training
    classifier = DecisionTreeClassifier(criterion="entropy")
    classifier.fit(X,y)  # training the model using given X and y

    return classifier