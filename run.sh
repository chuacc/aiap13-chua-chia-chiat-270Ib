#!/bin/sh

mkdir data
wget https://techassessment.blob.core.windows.net/aiap13-assessment-data/failure.db -O ./data/failure.db
python ./src/main.py --model RandomForest
python ./src/main.py --model LogisticRegression
python ./src/main.py --model SVC
python ./src/main.py --model DecisionTree
python ./src/main.py --model GradientBoost