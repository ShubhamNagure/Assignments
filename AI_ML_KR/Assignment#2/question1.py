# Q.1 Write a python code to plot the histogram and explore the data on Income.csv file
# Code
import matplotlib.pyplot as plt
import pandas as pd
df = pd.read_csv(r'csv_data/income.csv')
age_group=[x for x in range(10,100,10)]
plt.hist(df['age'],age_group, rwidth=0.8)
plt.xlabel("Range of ages")
plt.ylabel("Count")
plt.xticks(age_group)
plt.show()
