# REF: https://matplotlib.org/stable/tutorials/pyplot.html#sphx-glr-tutorials-pyplot-py

import matplotlib.pyplot as plt
from load_csv import load


def plotCountryLifeExpectancy(path: str) -> None:
    """
    Plot life expectancy for a given country from a CSV file.
    param path: Path to the CSV file containing life expectancy data.
    """
    try:
        df = load(path)
        # print(df.head())
        # print(df.shape)
        # print(df.loc['Morocco'])
        # print(df.loc['Morocco'].isnan().any())
        years = df.columns
        # print(years.isna().any())  # Check if there are any NaN values in the columns
        moroccan_data = df.loc['Morocco'].values
        years = [int(year) for year in years]
        print(years)
        # print(years, moroccan_data)
        plt.plot(years, moroccan_data, linestyle='-')
        plt.title('Morocco Life Expectancy Projections')
        plt.xlabel('Year')
        plt.ylabel('Life Expectancy')
        plt.show()
    except Exception as e:
        print(f'Error: {e}')


if __name__ == "__main__":
    plotCountryLifeExpectancy("life_expectancy_years.csv")
