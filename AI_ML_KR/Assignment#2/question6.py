# Q.6 Write a python code for handling missing data using “fill the null value” method on income.csv file
# Code
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
df = pd.read_csv(r'csv_data/income.csv')
print(df.isnull().sum())
df.fillna(value=0,inplace=True)
print(df.isnull().sum())
