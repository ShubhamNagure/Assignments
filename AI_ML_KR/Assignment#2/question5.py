# Q.5 Write a python code to find the data distributions using scatter plot for Income.csv file.
# Code
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
df = pd.read_csv(r'csv_data/income.csv')
mydict = df['maritalstatus'].value_counts().to_dict()
plt.scatter(list(mydict.values()),mydict.keys())
plt.show()
