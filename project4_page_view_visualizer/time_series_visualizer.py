#!/usr/bin/env python
# coding: utf-8

# # Data Import and Cleaning

# In[1]:


import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()


# In[2]:


# Clean the data
# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv("fcc-forum-pageviews.csv", index_col="date")
df.index = pd.to_datetime(df.index)
df


# In[3]:


# Calculate the 2.5th & 97.5th percentiles of the 'value' column
bottom_percentile = df['value'].quantile(0.025)
top_percentile = df['value'].quantile(0.975)


# In[4]:


# Filter DF to keep only rows where 'value' is >=2.5th percentile
df = df[(df['value'] >= bottom_percentile)]
# Filter DF to keep only rows where 'value' is <=97.5th percentile
df = df[(df['value'] <= top_percentile)]
df


# # Line Plot

# In[5]:


# Draw the line plot
fig, ax = plt.subplots(figsize=(12, 6))  # Create figure and axis
ax.plot(df.index, df['value'], color='pink')  # Plot data

# Set labels
ax.set_title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019')
ax.set_xlabel('Date')
ax.set_ylabel('Page Views')

# Save image and return fig (don't change this part)
#fig.savefig('line_plot.png')
#return fig


# # Bar Plot
# 
# Draws a bar chart showing the average daily page views for each month grouped by year.
# 
# This function takes no args and returns a Matplotlib figure. The chart displays
# the average daily page views on the y-axis and the years on the x-axis. Each month
# is represented by a different coloured bar in the chart. The plot is saved as 'bar_plot.png'.

# In[6]:


# Copy the data and add columns for year and month
df_bar = df.copy()
df_bar['year'] = df_bar.index.year
df_bar['month'] = df_bar.index.strftime('%B')
df_bar


# ### Bar Plot: Grouping and Stacking
# 
# Group / stack the data by year and month using groupby() to obtain a GroupBy (stacked) object
# Aggregate this grouped data by taking the mean of the 'value' column
# Apply unstack() to the grouped data to create a pivot table

# In[7]:


# Original data is ordered by date (year, month, day) and value
# Want to group by year, month and value (where value is the average of all values in that month)
df_bar_grouped = df_bar.groupby(['year', 'month'])['value'].mean()
df_bar_grouped


# In[8]:


# Unstack the grouped data to create a pivot table (with months as columns and years as rows)
df_bar = df_bar_grouped.unstack()
df_bar


# In[9]:


# Order columns by month
months_of_year = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
months_of_year


# In[10]:


# reindex() will order the columns by the order of "the_months"
df_bar = df_bar.reindex(columns=months_of_year)
df_bar


# In[11]:


# Draw bar plot
fig, ax = plt.subplots(figsize=(15, 5))
df_bar.plot(kind='bar', ax=ax)
ax.set(xlabel="Years", ylabel="Average Page Views")
ax.legend(title='Months')

# Save image and return fig (don't change this part)
#fig.savefig('bar_plot.png')
#return fig


# ### Box Plot
# 
# Draws two box plots to visualize the distribution of page views over time. 
# One plot shows year-wise trends, and the other shows month-wise seasonality.

# In[12]:


# Copy the data and add columns for year and month
df_box = df.copy()
df_box['year'] = df_box.index.year
df_box['month'] = df_box.index.strftime('%b')
df_box


# ## Box Plot: Draw using Seaborn

# In[13]:


# Add a new (month number) column to DF (Jan=1, Feb=2, Mar=3, etc)
df_box['month_num'] = df.index.month
df_box


# In[14]:


# Sort DF based on 'month_num'
df_box = df_box.sort_values('month_num')
df_box


# In[15]:


# Create a figure with 2 subplots (1 row, 2 columns)
fig, ax = plt.subplots(1, 2, figsize=(15,5))

# Box plot in 1st subplot (ax[0])
sns.boxplot(data = df_box, x = "year", y = "value", ax = ax[0]) 
(ax[0]).set_xlabel("Year")
(ax[0]).set_ylabel("Page Views")
(ax[0]).set_title("Year-wise Box Plot (Trend)")

# Box plot in 2nd subplot (ax[1])
sns.boxplot(data = df_box, x = "month", y = "value", ax = ax[1])
(ax[1]).set_xlabel("Month")
(ax[1]).set_ylabel("Page Views")
(ax[1]).set_title("Month-wise Box Plot (Seasonality)")

# Save image and return fig (don't change this part)
#fig.savefig('box_plot.png')
#return fig

