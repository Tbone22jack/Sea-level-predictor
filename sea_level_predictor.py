import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')
    
    x = list(range(171))
    for j in x:
      x[j] =  x[j] + 1880
    x = pd.Series(x)
    x = x.to_numpy()
    


    # Create scatter plot
    fig , ax = plt.subplots(figsize = (8,8))
    ax.scatter(x=df['Year'],y=df['CSIRO Adjusted Sea Level'])

    # Create first line of best fit
    line = linregress(df['Year'].iloc[0:133],df['CSIRO Adjusted Sea Level'].iloc[0:133])
    ax.plot(x, line.intercept + line.slope*x, 'r', label='fitted line')

    # Create second line of best fit
    line2 = linregress(df['Year'].iloc[120:133],df['CSIRO Adjusted Sea Level'].iloc[120:133])
    ax.plot(x[120:-1], line2.intercept + line2.slope*x[120:-1], 'g', label='fitted line')

    # Add labels and title
    ax.set_xlabel('Year')
    ax.set_ylabel('Sea Level (inches)')
    ax.set_title('Rise in Sea Level')
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()