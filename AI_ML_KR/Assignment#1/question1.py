# Q.1 Find the below statistical properties of each & every data attribute on income.csv file
# a. Count
# b. Mean
# c. Standard Deviation
# d. Minimum Value
# e. Maximum value
# f. mode
# Ans = Code
import pandas as pd
df = pd.read_csv (r'csv_data/stats.csv') 
mean1 = df['Salary'].mean()
max1 = df['Salary'].max()
min1 = df['Salary'].min()
count1 = df['Salary'].count()
std1 = df['Salary'].std() 
std2 =df['Salary'].mode()
print('Mode of Salary:'+str(std2))
print('Mean salary: ' +str(mean1))
print('Max salary: ' +str(max1))
print('Min salary: ' + str(min1))
print('Count of salaries: ' +str(count1))
print('Standard Deviation of salaries: ' +str(std1))
