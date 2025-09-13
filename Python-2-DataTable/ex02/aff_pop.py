
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

        # Restrict to years 1800–2050
        years = df.loc[:, "1800":"2050"].columns.astype(int)

        # Extract population data
        moroccan_data = df.loc["Morocco", "1800":"2050"].values 
        france_data = df.loc["France", "1800":"2050"].values

        # Plot data
        plt.plot(years, moroccan_data, label="Morocco")
        plt.plot(years, france_data, label="France")

        # Add labels and title
        plt.title("Population Projections")
        plt.xlabel("Year")
        plt.ylabel("Population (total)")
        plt.legend()
        plt.tight_layout()
        plt.show()

    except Exception as e:
        print(f"Unexpected error: {e}")



if __name__ == "__main__":
    plotPop("population_total.csv")

        