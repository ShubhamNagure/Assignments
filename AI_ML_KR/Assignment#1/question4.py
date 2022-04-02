# Q.4 Plot the correlation plot on dataset and visualize giving an overview of relationships among data on iris data.
# Code
import matplotlib.pyplot as plt
import pandas as pd
data = pd.read_csv(r'csv_data/iris.csv')
correlations=data.corr(method='pearson')
print(correlations)

x1=data["SepalLengthCm"]
x2=data["SepalWidthCm"]

plt.hist(x1,bins=20,color="green",rwidth=0.6)
plt.title("Sepal length in cm")
plt.xlabel("sepal Length in cm")
plt.ylabel("count")
plt.show()

plt.hist(x2,bins=20,color="pink",rwidth=0.6)
plt.title("Sepal width in cm")
plt.xlabel("sepal width in cm")
plt.ylabel("count")
plt.show()
