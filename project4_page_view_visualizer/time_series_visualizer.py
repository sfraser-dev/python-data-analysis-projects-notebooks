import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# 1
# Import data (Make sure to parse dates. Consider setting index column to 'date'.)

file_path_to_csv = "fcc-forum-pageviews.csv"
df = pd.read_csv(file_path_to_csv) 
print("\n------- df:")
print(df.head())
# Set 'date' col as the index of the DataFrame
df.set_index('date', inplace=True)
print("\n------- df (date as idx):")
print(df.head())

# 2
# Clean data

# Calc the 2.5th and 97.5th percentiles of 'value' col
lower_threshold = df['value'].quantile(0.025)
upper_threshold = df['value'].quantile(0.975)

# Filter the DataFrame to keep only rows within the desired range
df_cleaned = df[df['value'] >= lower_threshold]
df_cleaned = df_cleaned[df_cleaned['value'] <= upper_threshold]
print("\n------- df (cleaned):")
print(df_cleaned.head())


#USED NOTEBOOK TO SEE WHAT'S HAPPENING MORE CLEARLY!!

# 3
def draw_line_plot():
  # Create the line plot using the cleaned data
  fig, ax = plt.subplots(figsize=(15, 5))  # Adjust figure size as needed
  ax.plot(df_cleaned.index, df_cleaned['value'], color='red', linewidth=1)

  # Set the title and labels
  ax.set_title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019')
  ax.set_xlabel('Date')
  ax.set_ylabel('Page Views')

  # Show the plot
  plt.show()

"""

def draw_line_plot():
    # Draw line plot





    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    df_bar = None

    # Draw bar plot





    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig

def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]

    # Draw box plots (using Seaborn)





    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig
"""