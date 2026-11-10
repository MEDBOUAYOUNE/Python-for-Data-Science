# REF: https://matplotlib.org/stable/tutorials/pyplot.html#sphx-glr-tutorials-pyplot-py

from load_csv import load
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator


def plotCountryLifeExpectancy(path: str) -> None:
    """
    Plot life expectancy for a given country from a CSV file.
    param path: Path to the CSV file containing life expectancy data.
    """
    try:
        df = load(path)
        years = df.columns.astype(int)
        moroccan_data = df.loc['Morocco'].copy()
        ax = plt.gca()
        plt.plot(years, moroccan_data, linestyle='-')
        ax.xaxis.set_major_locator(MultipleLocator(40))
        plt.title('Morocco Life Expectancy Projections')
        plt.xlabel('Year')
        plt.ylabel('Life Expectancy')
        plt.show()
    except Exception as e:
        print(f'Error: {e}')


if __name__ == "__main__":
    plotCountryLifeExpectancy("life_expectancy_years.csv")
