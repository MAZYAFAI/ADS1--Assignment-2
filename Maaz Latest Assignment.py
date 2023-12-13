# -*- coding: utf-8 -*-
"""
Created on Wed Dec 13 17:43:54 2023

@author: MAZ YAFAI
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# File path of Xlsx file
file_path = 'C:\\Users\\MAZ YAFAI\\OneDrive\\Desktop\\Climate.xlsx' 
data = pd.read_excel(file_path)


print(data.describe())

print(data.columns)
print(data.head())
precipitation_data = data[data['Variable'] == 'Precipitation']

plt.figure(figsize=(22, 8))
sns.boxplot(x='County/Country', y='Annual', data=precipitation_data)
plt.title('Distribution of Annual Precipitation')
plt.xlabel('County/Country')
plt.ylabel('Annual Precipitation')
plt.xticks(rotation=45)
plt.show()


monthly_columns = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

# Calculate correlation matrix
correlation_matrix = precipitation_data[monthly_columns].corr()

# Plot heatmap for correlation
plt.figure(figsize=(10, 8))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt='.2f')
plt.title('Correlation Heatmap for Monthly Precipitation')
plt.show()

months = precipitation_data.columns[4:]
monthly_precipitation = precipitation_data.groupby('County/Country')[months].sum().T

plt.figure(figsize=(10, 6))
for country in monthly_precipitation.columns:
    plt.plot(monthly_precipitation.index, monthly_precipitation[country], marker='o', label=country)

plt.title('Monthly Precipitation Comparison')
plt.xlabel('Month')
plt.ylabel('Precipitation')
plt.legend()
plt.xticks(rotation=45)
plt.show()



