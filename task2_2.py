#2 Pre-processing and data-cleaning
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler, OneHotEncoder

file_path = '/Users/vardanvij/Downloads/bigBasket_new.csv'
df = pd.read_csv(file_path)
print("Original DataFrame:")
print(df.head())

df['Order'] = df['Order'].fillna(df['Order'].mean())
df['SKU'] = df['SKU'].fillna(df['SKU'].mean())
df['Member'] = df['Member'].fillna(df['Member'].mode()[0])
df['Description'] = df['Description'].fillna(df['Description'].mode()[0])
df['Created On'] = df['Created On'].fillna(df['Created On'].mode()[0])

df['Order'] = df['Order'].astype(int)
df['SKU'] = df['SKU'].astype(int)
df['Created On'] = pd.to_numeric(df['Created On'], errors='coerce')
df['Created On'] = pd.to_datetime(df['Created On'], unit='d', origin='1899-12-30')
df['Year'] = df['Created On'].dt.year
df['Month'] = df['Created On'].dt.month
encoder = OneHotEncoder(drop='first', sparse_output=False)
encoded_members = encoder.fit_transform(df[['Member']])

# Create DataFrame from the encoded features
encoded_members_df = pd.DataFrame(encoded_members, columns=encoder.get_feature_names_out(['Member']))
df = pd.concat([df, encoded_members_df], axis=1)
df = df.drop(['Member'], axis=1)
scaler = StandardScaler()
df[['Order', 'SKU']] = scaler.fit_transform(df[['Order', 'SKU']])
print("\nCleaned and Preprocessed DataFrame:")
print(df.head())
preprocessed_file_path = '/Users/vardanvij/Downloads/bigBasket_preprocessed.csv'
df.to_csv(preprocessed_file_path, index=False)

print(f"\nPreprocessed DataFrame saved to {preprocessed_file_path}")
