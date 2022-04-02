# Q.7 Write a python code for handling missing data using “Ignore the tuple” method on income.csv file
# Code
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
df = pd.read_csv(r'csv_data/income.csv')
null_mask = df["capitalgain"].isnull()
df[null_mask]
df.isnull().sum()
print(df.drop(labels = ["capitalgain"], axis=1).head())
