from load_csv import load
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter, MultipleLocator


def to_number(value: str) -> float:
    """Convert '29M', '2.5M', '350k', '1.2B' to a float."""
    value = str(value).strip()
    factors = {"k": 1e3, "M": 1e6, "B": 1e9}
    if value[-1] in factors:
        return float(value[:-1]) * factors[value[-1]]
    return float(value)


def plotPop(path: str) -> None:
    """
    Plot population data from a CSV file.
    param path: Path to the CSV file containing population data.
    """
    try:
        df = load(path)
        # print(df.info())

        years = df.loc[:, "1800":"2050"].columns.astype(int)

        moroccan_data = df.loc["Morocco", "1800":"2050"].map(to_number)
        france_data = df.loc["France", "1800":"2050"].map(to_number)

        plt.plot(years, moroccan_data, label="Morocco")
        plt.plot(years, france_data, label="France")

        ax = plt.gca()
        ax.xaxis.set_major_locator(MultipleLocator(40))
        ax.yaxis.set_major_locator(MultipleLocator(20e6))
        ax.yaxis.set_major_formatter(
            FuncFormatter(lambda y, _: f"{int(y / 1e6)}M"))

        plt.title("Population Projections")
        plt.xlabel("Year")
        plt.ylabel("Population")
        plt.legend()
        plt.tight_layout()
        plt.show()

    except Exception as e:
        print(f"Unexpected error: {e}")


if __name__ == "__main__":
    plotPop("population_total.csv")
