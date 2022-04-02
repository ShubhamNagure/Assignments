# Write a python program to load the dataset and understand the input data
# Dataset: Diabetes Dataset
# Library : Scipy
# a) Load data, describe the given data and identify missing, outlier data items
# b) Find correlation among all attributes
# c) Visualize correlation matrix

import pandas as pd
from tabulate import tabulate
df = pd.read_csv(r'csv_data/diabetes.csv')
print("\n\nSum of missing data:\n\n",df.isnull().sum())
from scipy import stats
import numpy as np
z = np.abs(stats.zscore(df['Glucose']))
print("\n\n",z,end="\n\n")
threshold = 3
 # Position of the outlier
print("\n\nPosition of the outlier:\n",np.where(z > 3))

corr_matrix = df.corr()
corr_matrix.style.background_gradient(cmap='coolwarm')
print(corr_matrix)
