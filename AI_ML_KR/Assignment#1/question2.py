# Q.2 Find the correlation matrix of dataset attributes with the help of corr() function on Pandas DataFrame.
# Code
# Making data frame from the csv file
import pandas as pd
df = pd.read_csv(r'/Users/shubham/Desktop/Projects/AIMLKR/clone/Assignments/AI_ML_KR/csv_data/stats.csv')
df[:6]
df.corr(method ='pearson')
print(df.corr())
