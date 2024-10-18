#!/usr/bin/env python
# coding: utf-8

# # Sea Level Predictor

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress


# ## Use Pandas to import the data from epa-sea-level.csv

# In[2]:


df = pd.read_csv('epa-sea-level.csv')
df


# ## Use matplotlib to create a scatter plot using the Year column as the x-axis and the CSIRO Adjusted Sea Level column as the y-axis

# In[7]:


plt.figure(figsize=(15, 7))
plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'])


# ## Use the linregress function from scipy.stats to get the slope and y-intercept of the line of best fit

# In[13]:


slope, intercept, _, _, _ = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
print(f"Slope: {slope:.2f}")
print(f"Intercept: {intercept:.2f}")


# ## Plot the line of best fit over the top of the scatter plot - make the line go through the year 2050 to predict the sea level rise in 2050

# ### Create x values for line of best fit

# In[18]:


years = range(df['Year'].min(), 2051)
years


# ### Calc y values for line of best fit

# In[32]:


y = [slope * year + intercept for year in years]
y[0:10]


# In[31]:


y[-11:-1]


# ### Plot line of best fit on scatter plot

# In[34]:


# Scatter plot
plt.figure(figsize=(15, 7))
plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'])

# Line of best fit
plt.plot(years, y, 'g')

# Labels
plt.xlabel('Year')
plt.ylabel('CSIRO Adjusted Sea Level (inches)')
plt.title('Rise in Sea Level')
plt.show()


# ## Plot a new line of best fit just using the data from year 2000 through the most recent year in the dataset - make the line also go through the year 2050 to predict the sea level rise in 2050 if the rate of rise continues as it has since the year 2000.

# ### Filter data to include only years >= 2000

# In[36]:


df_filt = df[df['Year'] >= 2000]
df_filt


# ### Calculate slope and y intercept of line of best fit for filtered data

# In[38]:


slope_filtered, intercept_filtered, _, _, _= linregress(df_filt['Year'], df_filt['CSIRO Adjusted Sea Level'])
print(f"Slope filtered: {slope_filtered:.2f}")
print(f"Intercept filtered: {intercept_filtered:.2f}")


# ### Plot line of best fit on scatter plot

# In[42]:


# Create scatter plot
plt.figure(figsize=(15, 7))
plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'])

# Plot line of best fit for the filtered data
x_filt = range(df_filt['Year'].min(), 2051)
y_filt = slope_filtered * x_filt + intercept_filtered
plt.plot(x_filt, y_filt, 'r')

# Labels
plt.title('Rise in Sea Level')
plt.xlabel('Year')
plt.ylabel('Sea Level (inches)')

# Show plot
plt.show()

