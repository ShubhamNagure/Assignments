# Q.8 Write a python code for handling missing data using “Normalization (min-max approach)” method on income.csv file.
# Code

import pandas as pd
df = pd.read_csv(r'csv_data/income.csv')
df = df.select_dtypes(include=['int64'])
# apply the min-max scaling in Pandas using the .min() and .max() methods
def min_max_scaling(df):
    # copy the dataframe
    df_norm = df.copy()
    # apply min-max scaling
    for column in df_norm.columns:
        df_norm[column] = (df_norm[column] - df_norm[column].min()) / (df_norm[column].max() - df_norm[column].min())

    return df_norm

# call the min_max_scaling function
df_cars_normalized = min_max_scaling(df)

print(df_cars_normalized.head(7))
