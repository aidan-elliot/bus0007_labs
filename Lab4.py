# 1. Import Libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

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

# Part 2 - Visualization using matplotlib

# 3. Use the bar method to display the bar chart (Categories vs Sales)
category_sales = df.groupby('Category')['Sales'].sum()
plt.figure(figsize=(8,6))
category_sales.plot(kind='bar')
plt.title('Total Sales by Category')
plt.xlabel('Category')
plt.ylabel('Sales')
plt.show()

# 4.Use the bar method to display the bar chart in which the x-axis include the sub-categories and the y-axis include Sales.
subcategory_sales = df.groupby('Sub-Category')['Sales'].sum()
plt.figure(figsize=(10,8))
subcategory_sales.plot(kind='bar')
plt.title('Total Sales by Sub-Category')
plt.xlabel('Sub-Category')
plt.ylabel('Sales')
plt.show()

# 5.Repeat step 3 with clustered bar and in each cluster bar for each category show both Sales and Profits.
category_summary = df.groupby('Category')[['Sales', 'Profit']].sum()
category_summary.plot(kind='bar', figsize=(8,6))
plt.title('Sales and Profit by Category')
plt.xlabel('Category')
plt.ylabel('Values')
plt.legend(['Sales', 'Profit'])
plt.show()

# 6.	Repeat step 4 with clustered bar and in each cluster bar for each sub-category show both Sales and Profits.
subcategory_summary = df.groupby('Sub-Category')[['Sales', 'Profit']].sum()
subcategory_summary.plot(kind='bar', figsize=(10,8))
plt.title('Sales and Profit by Sub-Category')
plt.xlabel('Sub-Category')
plt.ylabel('Values')
plt.legend(['Sales', 'Profit'])
plt.show()

# 7.	Use corr() method to show correlation between Sales, Quantity, Discount, and Profit.
correlation_matrix = df[['Sales', 'Quantity', 'Discount', 'Profit']].corr()
print("\nCorrelation matrix:")
print(correlation_matrix)

import seaborn as sns
plt.figure(figsize=(8,6))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', linewidths=0.5)
plt.title('Correlation Matrix')
plt.show()

