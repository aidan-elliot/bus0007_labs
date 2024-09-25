# 1. Import Libraries
import numpy as np
import pandas as pd

# 2. Import the SampleSuperstore dataset as a pandas DataFrame, and call it 'df'
df = pd.read_excel('SampleSuperstore.xls')

# 3. View the DataFrame (Implicitly view the dataset)
print(df.head())  # This will show the first 5 rows of the DataFrame

# 4. View the shape of the dataset and display the names of the columns
print("Shape of the dataset:", df.shape)  # (rows, columns)
print("Column names:", df.columns)

# 5. View information about the dataset including range index, datatypes, and number of non-null entries
print("\nInformation about the dataset:")
df.info()  # Displays data types, non-null values, and memory usage

# 6. View unique categories in the 'Category' column
unique_categories = df['Category'].unique()
print("\nUnique categories:", unique_categories)

# 7. View the unique list of states
unique_states = df['State'].unique()
print("\nUnique states:", unique_states)

# 8. View the unique categories and subcategories
unique_subcategories = df['Sub-Category'].unique()
print("\nUnique subcategories:", unique_subcategories)

# 9. View the statistical description of the DataFrame
print("\nStatistical description of the dataset:")
print(df.describe())  # This will give a summary of numerical columns like sales, profit, etc.

# 10. Create a new DataFrame where the profit is negative, i.e., loss, and call it loss_df
loss_df = df[df['Profit'] < 0]
print("\nLoss DataFrame (first 5 rows):")
print(loss_df.head())  # View the loss data

# 11. In the loss_df, group by "Segment" and calculate the sum of profits
segment_loss = loss_df.groupby('Segment')['Profit'].sum()
print("\nLoss by Segment:")
print(segment_loss)

# 12. Group by 'Sub-Category' and sum the profits in the loss_df
subcategory_loss = loss_df.groupby('Sub-Category')['Profit'].sum()
print("\nLoss by Sub-Category:")
print(subcategory_loss)

# 13. Rank the Sub-Categories by the number of records in the loss_df using value_counts
subcategory_counts = loss_df['Sub-Category'].value_counts()
print("\nRank of Sub-Categories by number of records:")
print(subcategory_counts)

# 14. In the loss_df, group by "City" and sort values by profit
city_loss_sorted = loss_df.groupby('City')[['Profit']].sum().sort_values(by='Profit')
print("\nCities with losses, sorted by Profit:")
print(city_loss_sorted)

# 15. In the original DataFrame (df), group by "Region" and display Sales, Quantity, Discount, and Profit
region_summary = df.groupby('Region')[['Sales', 'Quantity', 'Discount', 'Profit']].sum()
print("\nSales, Quantity, Discount, and Profit by Region:")
print(region_summary)
