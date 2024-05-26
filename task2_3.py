import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

file_path = '/Users/vardanvij/Downloads/bigBasket.csv'
df = pd.read_csv(file_path)
df['Created On'] = pd.to_datetime(df['Created On'], errors='coerce')
df = df.dropna(subset=['Created On'])
df['Day'] = df['Created On'].dt.day
df['Month'] = df['Created On'].dt.month
df['Year'] = df['Created On'].dt.year
df['Hour'] = df['Created On'].dt.hour

print(df[['Created On', 'Day', 'Month', 'Year', 'Hour']].head())

# 1. Total number of customers
total_customers = df['Member'].nunique()
print(f"Total number of customers: {total_customers}")

# 2. Customer with the highest order
customer_orders = df.groupby('Member')['Order'].count().reset_index()
customer_with_highest_order = customer_orders.loc[customer_orders['Order'].idxmax()]
print(f"Customer with the highest order: {customer_with_highest_order['Member']} with {customer_with_highest_order['Order']} orders")

# Plot: Customer with the highest order
plt.figure(figsize=(10, 6))
sns.barplot(data=customer_orders.sort_values(by='Order', ascending=False).head(10), x='Member', y='Order')
plt.title('Top 10 Customers by Number of Orders')
plt.xticks(rotation=45)
plt.xlabel('Customer')
plt.ylabel('Number of Orders')
plt.show()

# 3. Days, month, and year with highest sales order
day_with_highest_sales = df['Day'].value_counts().idxmax()
month_with_highest_sales = df['Month'].value_counts().idxmax()
year_with_highest_sales = df['Year'].value_counts().idxmax()
print(f"Day with highest sales order: {day_with_highest_sales}")
print(f"Month with highest sales order: {month_with_highest_sales}")
print(f"Year with highest sales order: {year_with_highest_sales}")

# Plot: Days with highest sales order
plt.figure(figsize=(10, 6))
sns.countplot(x='Day', data=df)
plt.title('Sales Orders by Day')
plt.xlabel('Day of the Month')
plt.ylabel('Number of Orders')
plt.show()

# Plot: Months with highest sales order
plt.figure(figsize=(10, 6))
sns.countplot(x='Month', data=df)
plt.title('Sales Orders by Month')
plt.xlabel('Month')
plt.ylabel('Number of Orders')
plt.show()

# Plot: Years with highest sales order
plt.figure(figsize=(10, 6))
sns.countplot(x='Year', data=df)
plt.title('Sales Orders by Year')
plt.xlabel('Year')
plt.ylabel('Number of Orders')
plt.show()

# 4. Top 10 Most sought after products by customers
top_10_products = df['SKU'].value_counts().head(10)
print(f"Top 10 Most sought after products:\n{top_10_products}")

# Plot: Top 10 Most sought after products
plt.figure(figsize=(10, 6))
sns.barplot(x=top_10_products.index, y=top_10_products.values)
plt.title('Top 10 Most Sought After Products')
plt.xlabel('Product SKU')
plt.ylabel('Number of Orders')
plt.xticks(rotation=45)
plt.show()

# 5. Top 10 Least sought after products by customers
least_10_products = df['SKU'].value_counts().tail(10)
print(f"Top 10 Least sought after products:\n{least_10_products}")

# Plot: Top 10 Least sought after products
plt.figure(figsize=(10, 6))
sns.barplot(x=least_10_products.index, y=least_10_products.values)
plt.title('Top 10 Least Sought After Products')
plt.xlabel('Product SKU')
plt.ylabel('Number of Orders')
plt.xticks(rotation=45)
plt.show()

# 6. Period of day with high sales order
period_of_day_with_high_sales = df['Hour'].value_counts().idxmax()
print(f"Period of day with highest sales order: {period_of_day_with_high_sales}:00 hours")

# Plot: Sales orders by hour of the day
plt.figure(figsize=(10, 6))
sns.countplot(x='Hour', data=df)
plt.title('Sales Orders by Hour of the Day')
plt.xlabel('Hour of the Day')
plt.ylabel('Number of Orders')
plt.show()

# 7. Total number of unique items
total_unique_items = df['SKU'].nunique()
print(f"Total number of unique items: {total_unique_items}")

# Save the transformed DataFrame to a new CSV file
transformed_file_path = '/Users/vardanvij/Downloads/bigBasket_transformed.csv'
df.to_csv(transformed_file_path, index=False)

print(f"\nTransformed DataFrame saved to {transformed_file_path}")
