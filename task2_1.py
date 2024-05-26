#create a dataset(data_set): some NULL values must be there in dataset, else create it thru numpy.nan 
#1 data preprocessing  DATA: bigbasket
#2 data cleaning
#3 data transformation using aggregation functions, groupby, merge, joins 
#4 data visualization , expiring soon will be bigger in scatter plot and price will be lower as comparison to when it was fresh
#5 advertisements - 2 types of advertisements - for the products which are expiring soon(lower prices) 

import pandas as pd
import numpy as np

file_path = '/Users/vardanvij/Downloads/bigBasket.csv'
df = pd.read_csv(file_path)
print("Original DataFrame:")
print(df.head())
np.random.seed(42)
nan_fraction = 0.1
mask = np.random.rand(*df.shape) < nan_fraction
df[mask] = np.nan
output_file_path = '/Users/vardanvij/Downloads/bigBasket_new.csv'
df.to_csv(output_file_path, index=False)

print(f"\nModified DataFrame saved to {output_file_path}")
