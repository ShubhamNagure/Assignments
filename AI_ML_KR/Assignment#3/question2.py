import pandas as pd
import matplotlib.pyplot as plt
data = pd.read_csv('csv_data/Iris.csv')
data.head()
data.sample(11)
data.columns
data.shape
print(data)
for col in data.columns[:-1]:
    print("Mean of ",col,":\t",data[col].mean())  
data['Species'] = data['Species'].astype('category') 
print(end="\n\n========================\n")
print(data.groupby(data['Species']).mean().reset_index())
data.plot(kind ="scatter",
          x ='SepalLengthCm',
          y ='PetalLengthCm')
plt.grid()
