# Q.4 Write a python code to find the data distributions using box plot for Income.csv file
# Code
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

dataframe = pd.read_csv("csv_data/income.csv")
print(dataframe.head())
print(dataframe.isnull().values.any())

age = dataframe["age"]
JobType = dataframe["JobType"]
SalStat = dataframe["SalStat"]

dataframe.head()  
sns.boxplot(x=age)
plt.show()

age = dataframe["age"]
sns.boxplot(x=age, y=SalStat)
plt.show()

dataframe = pd.DataFrame(data=dataframe, columns=["age", "JobType", "SalStat"])
boxplot = sns.boxplot(x="age", y="SalStat",data=pd.melt(dataframe))
boxplot.axes.set_title("Distribution of Income", fontsize=16)
boxplot.set_xlabel("Conditions", fontsize=14)
boxplot.set_ylabel("Values", fontsize=14)
plt.show()
