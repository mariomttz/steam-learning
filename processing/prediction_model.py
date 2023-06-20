#!/usr/bin/env python
# -*- coding: utf-8 -*-


# 1. Libraries

import pandas as pd
from sklearn.tree import DecisionTreeClassifier


# 2. Load training data

PATH = './data/'
data = pd.read_csv(PATH + 'steam_data.csv')


# 3. We do the cleaning for the training data

df = data.copy()

# We eliminate attributes that the user does not enter
df.drop('fecha', axis = 1, inplace = True)
df.drop('appid', axis = 1, inplace = True)


# 4. We divide the column to be predicted  from the rest of the data
y = df['review_range']
X = df.drop(['review_range'], axis=1)


# 5. Select the model and adjust it
modelo =  DecisionTreeClassifier(criterion = 'entropy')
modelo.fit(X, y)


# 6. We load the data to predict

X_pred = pd.read_csv(PATH + 'predict_data.csv')
y_pred = str(modelo.predict(X_pred)[0])

# In predict_data.csv only the last "query" that was made is saved, 
#so it has 1 row and 96 columns that are the attributes that are 
#considered when predicting (predicts from 1 to 5 )


# 7. Save prediction

with open(PATH + 'rating.txt', 'w') as f:
    f.write(y_pred)


