import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
#1
college_csv_file_path = r"C:\Users\qaism\OneDrive - University of Virginia\Documents\Class Documents\DS 3001\assignment2\data\college_completion.csv"
college_df = pd.read_csv(college_csv_file_path)

#2
dimensions = college_df.shape
observations = dimensions[0]
variables = college_df.columns.tolist()
first_few_rows = college_df.head()
dimensions, observations, variables, first_few_rows

#3
cross_tab = pd.crosstab(college_df['control'], college_df['level'])
cross_tab

#4
#histogram
plt.figure(figsize=(10, 6))
sns.histplot(college_df['grad_100_value'], kde=False, bins=30)
plt.title('Histogram of grad_100_value')
plt.xlabel('grad_100_value')
plt.ylabel('Frequency')
plt.show()
# Kernel Density Plot
plt.figure(figsize=(10, 6))
sns.kdeplot(college_df['grad_100_value'])
plt.title('Kernel Density Plot of grad_100_value')
plt.xlabel('grad_100_value')
plt.ylabel('Density')
plt.show()
# Boxplot
plt.figure(figsize=(10, 6))
sns.boxplot(x=college_df['grad_100_value'])
plt.title('Boxplot of grad_100_value')
plt.xlabel('grad_100_value')
plt.show()

# Statistical Description
stat_description = college_df['grad_100_value'].describe()
print("Statistical Description of grad_100_value:")
print(stat_description)

#5
# Grouped Kernel Density Plot by control
sns.kdeplot(data=college_df, x='grad_100_value', hue='control')
plt.title('Grouped Kernel Density Plot of grad_100_value by Control')
plt.show()

# Grouped Kernel Density Plot by level
sns.kdeplot(data=college_df, x='grad_100_value', hue='level')
plt.title('Grouped Kernel Density Plot of grad_100_value by Level')
plt.show()

# Grouped Statistical Descriptions
grouped_stats_control = college_df.groupby('control')['grad_100_value'].describe()
grouped_stats_level = college_df.groupby('level')['grad_100_value'].describe()
print("Grouped Statistical Descriptions by Control:")
print(grouped_stats_control)
print("Grouped Statistical Descriptions by Level:")
print(grouped_stats_level)

#6
# Create a new variable
college_df['levelXcontrol'] = college_df['level'] + ', ' + college_df['control']

# Grouped Kernel Density Plot
sns.kdeplot(data=college_df, x='grad_100_value', hue='levelXcontrol')
plt.title('Grouped Kernel Density Plot of grad_100_value by levelXcontrol')
plt.show()

#7
plt.figure(figsize=(12, 8))
sns.kdeplot(data=college_df, x='aid_value', hue='levelXcontrol')
plt.title('Grouped Kernel Density Plot of aid_value by Level and Control')
plt.show()

grouped_stats_aid_level = college_df.groupby('level')['aid_value'].describe()
grouped_stats_aid_control = college_df.groupby('control')['aid_value'].describe()
print("Grouped Statistical Descriptions of aid_value by Level:")
print(grouped_stats_aid_level)
print("Grouped Statistical Descriptions of aid_value by Control:")
print(grouped_stats_aid_control)


#8
# Scatterplot of grad_100_value by aid_value
plt.figure(figsize=(12, 8))
sns.scatterplot(data=college_df, x='aid_value', y='grad_100_value')
plt.title('Scatterplot of grad_100_value by aid_value')
plt.show()

# Scatterplot of grad_100_value by aid_value, grouped by level and control
plt.figure(figsize=(12, 8))
sns.scatterplot(data=college_df, x='aid_value', y='grad_100_value', hue='levelXcontrol')
plt.title('Scatterplot of grad_100_value by aid_value Grouped by Level and Control')
plt.show()