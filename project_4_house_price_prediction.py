# -*- coding: utf-8 -*-
"""Project 4 : House Price Prediction.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1BvTOfj5ZJEBXXPetNCvOdx6TiK0Vob-x

importing the dependencies
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import sklearn.datasets
import seaborn as sns
from sklearn.model_selection import train_test_split
from xgboost import XGBRegressor
from sklearn import metrics

"""impporting the boston House Price Dataset"""

house_price_dataset =sklearn.datasets.load_boston()

print(house_price_dataset)

# Loading the dataset to a pandas datsframe
house_price_dataframe=pd.DataFrame(house_price_dataset.data,columns=house_price_dataset.feature_names)

#print First 5 rows of our Dataframe
house_price_dataframe.head()

# add the target column to the dataframe
house_price_dataframe["price"]=house_price_dataset.target

house_price_dataframe.head()

# checking the number of rows and columns in the Datafrme
house_price_dataframe.shape

# check for missing values
house_price_dataframe.isnull().sum()

# statical measures of the dataset
house_price_dataframe.describe()

"""understanding the correlation batween various features in the dataset

1.positive correlation

2.negative Correlation
"""

correlation= house_price_dataframe.corr()

# constructing a heatmap to understand the correlation
plt.figure(figsize=(10,10))
sns.heatmap(correlation,cbar=True,square=True,annot=True,fmt='.1f',annot_kws={'size':8},cmap='Blues');

"""splitting the data and target"""

X=house_price_dataframe.drop(['price'],axis=1)
Y=house_price_dataframe['price']

print(X)
print(Y)

"""splitting the data into training data and test data"""

X_train, X_test, Y_train, Y_test= train_test_split(X,Y, test_size=0.2,random_state=2)

print(X.shape,X_train.shape,X_test.shape)

"""Model Training 

XGBoost Regressor
"""

# laoading the model 
model=XGBRegressor()

# training the model with X_train
model.fit(X_train, Y_train);

"""Evaluation

Prediction on training data
"""

# accuracy for prediction on training data
training_data_prediction=model.predict(X_train)

print(training_data_prediction)

# R squared error
score_1 = metrics.r2_score(Y_train,training_data_prediction)

# Mean Absoluate error
score_2=metrics.mean_absolute_error(Y_train,training_data_prediction)

print("R squared error : ",score_1)
print("Mean absolute error :",score_2)

"""Visualizating the actual and predicted prices"""

plt.scatter(Y_train,training_data_prediction)
plt.xlabel("Actual price")
plt.ylabel("Pridected prices")
plt.title("Actual Prices vs Predicted Prices")
plt.show()

"""predication on test data"""

# accuracy for prediction on test data
test_data_prediction=model.predict(X_test)

# R squared error
score_1 = metrics.r2_score(Y_test,test_data_prediction)

# Mean Absoluate error
score_2=metrics.mean_absolute_error(Y_test,test_data_prediction)

print("R squared error : ",score_1)
print("Mean absolute error :",score_2)

