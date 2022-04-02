# Q.9 Write a python code to implement classification using logistic regression model (use Income.csv file).
# Code

import pandas as pd 
# To partition the data
from sklearn.model_selection import train_test_split
# Importing library for logistic regression
from sklearn.linear_model import LogisticRegression
# Importing performance metrics - accuracy score & confusion matrix
from sklearn.metrics import accuracy_score,confusion_matrix

import warnings
warnings.filterwarnings("ignore")
data = pd.read_csv(r'C:\Users\Admin\Desktop\income.csv',na_values=[" ?"])
data2 = data.dropna(axis=0)

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

# Make an instance of the Model
logistic = LogisticRegression(solver='lbfgs',max_iter=100)

# Fitting the values for x and y
logistic.fit(train_x,train_y)

# print("Logistic coeff:",logistic.coef_)
print("Logistic intercept:",logistic.intercept_)

# Prediction from test data
prediction = logistic.predict(test_x)
print("\nPrediction:",prediction)

# Confusion matrix
confusion_matrix = confusion_matrix(test_y, prediction)
print("\nConfusion matrix:\n",confusion_matrix)

# Calculating the accuracy
accuracy_score=accuracy_score(test_y, prediction)
print("\nAccuracy score:",accuracy_score)
