import sqlite3
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder, MinMaxScaler
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.metrics import classification_report
import joblib
from utils import *
import argparse

# Create the parser
parser = argparse.ArgumentParser()
# Add an argument
parser.add_argument('--model', type=str, required=True)
# Parse the argument
args = parser.parse_args()


model_select=args.model

model = {
    "LogisticRegression":   LogisticRegression(),
    "SVC":  SVC(),
    "KNeighbors":  KNeighborsClassifier(n_neighbors=3),
    "DecisionTree":   DecisionTreeClassifier(),
    "RandomForest":   RandomForestClassifier(),
    "GradientBoost":   GradientBoostingClassifier()
}


con = sqlite3.connect("./data/failure.db")
df = pd.read_sql_query("SELECT * from failure", con)
con.close()

# Data cleaning
df = dataclean(df)

# Data preparation
# Transform ordinal features into numerical features
df= encode(df)

# Split the data into 20% test and 80% train
X = df.drop("Failure",axis=1)
y = df['Failure']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=123)


# print('X_Train Shape :', end=' ')
# print(X_train.shape)
# print('y_Train Shape :', end=' ')
# print(y_train.shape)
# print('X_test Shape :', end=' ')
# print(X_test.shape)
# print('Y_test Shape :', end=' ')
# print(y_test.shape)

# List of numerical columns and categorical columns  
num_cols = ["Temperature", "RPM", "Usage", "Fuel consumption", "Membership"]
cat_cols = ["Model", "Factory"]


# Define transformer for numerical and catagorical feature
num_transformer = Pipeline(steps=[
    ('impute', SimpleImputer(strategy='mean')),
    ('scale',MinMaxScaler())
])

cat_transformer = Pipeline(steps=[
    ('impute', SimpleImputer(strategy='most_frequent')),
    ('one-hot',OneHotEncoder(handle_unknown='ignore', sparse_output=False))
])

# Use Column transformer as preprocessor the numerical and categorical features are transformed seperately and combined
preprocessor = ColumnTransformer(
   transformers=[
    ('numeric', num_transformer, num_cols)
   ,('categorical', cat_transformer, cat_cols)
]) 


pipeline = Pipeline(steps = [
               ('preprocessor', preprocessor)
              ,('clf',model[model_select])
           ])


pipeline.fit(X_train, y_train)

# Save the pipeline for future to be called without fitting
joblib.dump(pipeline,"pipe.joblib")

preds = pipeline.predict(X_test)

# print('Prediction Shape :', end=' ')
print(preds.shape)
print('---------------------------------')
print(model_select)
print('-----------------------------------')
print(classification_report(y_test, preds))