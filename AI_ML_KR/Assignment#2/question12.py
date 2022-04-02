# Q.12 Write a python program to implement k-Nearest Neighbor (KNN) algorithm to classify the Income.csv dataset.
# Code
import pandas as pd 
# To perform numerical operations
import numpy as np
# To visualize data
import seaborn as sns
# To partition the data
from sklearn.model_selection import train_test_split
# importing the library of KNN
from sklearn.neighbors import KNeighborsClassifier  
# Importing performance metrics - accuracy score & confusion matrix
from sklearn.metrics import accuracy_score,confusion_matrix
data = pd.read_csv(r'csv_data/income.csv',na_values=[" ?"]) 

missing = data[data.isnull().any(axis=1)]
data2 = data.dropna(axis=0)

# Reindexing the salary status names to 0,1
data2['SalStat']=data2['SalStat'].map({' less than or equal to 50,000':0,' greater than 50,000':1})
# print(data2['SalStat'])

new_data=pd.get_dummies(data2, drop_first=True)

# Storing the column names 
columns_list=list(new_data.columns)
# print(columns_list)

# Separating the input names from data
features=list(set(columns_list)-set(['SalStat']))
# print(features)

# Storing the output values in y
y=new_data['SalStat'].values
# print(y)

# Storing the values from input features
x = new_data[features].values
# print(x)

# Splitting the data into train and test
train_x,test_x,train_y,test_y = train_test_split(x,y,test_size=0.3, random_state=0)


# Storing the K nearest neighbors classifier
KNN_classifier = KNeighborsClassifier(n_neighbors = 5)  

# Fitting the values for X and Y
KNN_classifier.fit(train_x, train_y) 

# Predicting the test values with model
prediction = KNN_classifier.predict(test_x)
print("\nPrediction:",prediction)
# Performance metric check
confusionMmatrix = confusion_matrix(test_y, prediction)
print("\nConfusion matrix:\n",confusionMmatrix)

# Calculating the accuracy
accuracy_score=accuracy_score(test_y, prediction)

print("\nAccuracy Score:\n",accuracy_score)

print('\nMisclassified samples: %d\n' % (test_y != prediction).sum())

Misclassified_sample = []
# Calculating error for K values between 1 and 20
for i in range(1, 20):  
    knn = KNeighborsClassifier(n_neighbors=i)
    knn.fit(train_x, train_y)
    pred_i = knn.predict(test_x)
    Misclassified_sample.append((test_y != pred_i).sum())

print(Misclassified_sample)
