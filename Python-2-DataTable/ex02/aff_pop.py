
from load_csv import load
import matplotlib.pyplot as plt
import pandas as pd


def plotPop(path: str) ->None:
    """
    Plot population data from a CSV file.
    param path: Path to the CSV file containing population data.
    """
    try:
        df = load(path)
        # print(df)
        # print(df.head())
        # print(df.shape)
        years = df.columns
        years = [int(year) for year in years]

        moroccan_data = df.loc['Belgium'].values
        canadian_data = df.loc['France'].values

        plt.plot(years, moroccan_data, label='USA')
        plt.plot(years, canadian_data, label='Japan')
        # plt.xlim(years.min() - 1, years.max() + 1)
        plt.tight_layout()
        plt.title('Population Projections')
        plt.xlabel('Year')
        plt.ylabel('Population')
        plt.show()

        # print(years, moroccan_data, canada_data)
    except Exception as e:
        print(f'Unexcpected error: {e}')



if __name__ == "__main__":
    plotPop("population_total.csv")

        