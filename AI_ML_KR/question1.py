import matplotlib.pyplot as plt
import pandas as pd
df = pd.read_csv(r'csv_data/Iris.csv')
print(df['Species'].value_counts())
fig, ax = plt.subplots()
# plot histogram
ax.hist(df['SepalLengthCm'])
# set title and labels
ax.set_title('sepal_length')
ax.set_xlabel('Points')
ax.set_ylabel('Frequency')
plt.show()
