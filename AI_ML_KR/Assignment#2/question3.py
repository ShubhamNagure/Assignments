# Q.3 Write a python code to plot the pie chart and explore the data on Income.csv file.
# Code
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
df = pd.read_csv(r'csv_data/income.csv')
mydict = dict()
dflist = df['relationship'].to_list()
for i in dflist:

    if i not in mydict:
         mydict[i] = dflist.count(i)
print(mydict)
plt.pie(np.array(list(mydict.values())),labels=list(mydict.keys()),startangle = 40)
plt.show()
