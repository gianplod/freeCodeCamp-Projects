import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress


def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv', float_precision='legacy')
    s_years = df['Year'].append(pd.Series([year for year in range(2014, 2050)])).reset_index(
        drop=True)  # not including 2050 as the tests only include till 2049

    # Create scatter plot
    fig, ax = plt.subplots(1, 1, figsize=(10, 5))
    plt.scatter(x='Year', y='CSIRO Adjusted Sea Level', data=df)
    ax.set_title('Rise in Sea Level')
    ax.set_xlabel('Year')
    ax.set_ylabel('Sea Level (inches)')
    ax.set_xlim(None, 2060)
    ax.set_ylim(-2.5, 17.5)

    # Create first line of best fit
    slope, intercept, rvalue, pvalue, stderr = linregress(
        x=df['Year'], y=df['CSIRO Adjusted Sea Level'])
    plt.plot(s_years, intercept + slope*s_years)  # first line of fit

    # Create second line of best fit
    slope2, intercept2, rvalue2, pvalue2, stderr2 = linregress(
        x=df['Year'].iloc[120:134], y=df['CSIRO Adjusted Sea Level'].iloc[120:134])
    # second line of fit (from 2000 to 2049)
    plt.plot(s_years[120:], intercept2 + slope2*s_years[120:])

    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()
