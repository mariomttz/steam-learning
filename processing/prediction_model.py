#!/usr/bin/python3
# -*- coding: utf-8 -*-

# Libraries
from sklearn.tree import DecisionTreeClassifier
import pandas as pd

# Load training data
PATH = './dataset/'
data = pd.read_csv(PATH + 'steam_data.csv')

# We do the cleaning for the training data
df = data.copy()
df.drop('fecha', axis = 1, inplace = True)
df.drop('appid', axis = 1, inplace = True)

# We divide the column to be predicted 
# from the rest of the data
y = df['review_range']
X = df.drop(['review_range'], axis=1)

# Select the model and adjust it
model = DecisionTreeClassifier(criterion = 'entropy')
model.fit(X, y)

# We load the data to predict
X_pred = pd.read_csv(PATH + 'predict_data.csv')

# We predict the qualification
y_pred = model.predict(X_pred)[0]

# We write the rating in a file
with open(PATH + 'rating.txt', 'w') as f:
    f.write(y_pred)