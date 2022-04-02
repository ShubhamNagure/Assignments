# Q.4 Write a python program to impute missing values with various techniques on given dataset. (Diabetes Dataset)
# a) Remove rows/ attributes
# b) Replace with mean or mode
# c) Write a python program to perform transformation of data using Discretization (Binning)/normalization
# Code
# example of removing rows that contain missing values
from numpy import nan
from pandas import read_csv
# load the dataset
dataset = read_csv(r'csv_data/diabetes.csv')
print(dataset.shape,end="\n\n===================\n\n")
# replace '0' values with 'nan'
dataset['Outcome'] = dataset['Outcome'].replace(0, nan)
# drop rows with missing values\
dataset = dataset.head(5)
print(dataset,end="\n\n=======================\n\n")
# dataset.dropna(inplace=True)
# print(dataset['Outcome'].mean())
dataset['Outcome'].fillna(dataset['Outcome'].mean(),inplace=True)
# summarize the shape of the data with missing rows removed
print(dataset)
import warnings
warnings.filterwarnings("ignore")
# c)
# demonstration of the discretization transform
from sklearn.preprocessing import KBinsDiscretizer
from matplotlib import pyplot
# generate gaussian data sample
# histogram of the raw data
pyplot.hist(dataset, bins=25)
pyplot.show()
# discretization transform the raw data
kbins = KBinsDiscretizer(n_bins=10, encode='ordinal', strategy='uniform')
data_trans = kbins.fit_transform(dataset)
# summarize first few rows
print(data_trans[:10, :])
# histogram of the transformed data
pyplot.hist(data_trans, bins=10)
pyplot.show()
