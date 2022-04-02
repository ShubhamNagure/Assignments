# Q.2 Write a python code to plot bar chart and explore the data on Income.csv file
# Code
import matplotlib.pyplot as plt
import pandas as pd
df = pd.read_csv(r'csv_data/income.csv')
mydict = df['maritalstatus'].value_counts().to_dict()
plt.barh(list(mydict.keys()),list(mydict.values()), color ='maroon')
plt.xlabel("Marital Status")
plt.ylabel("Count")
plt.show()
