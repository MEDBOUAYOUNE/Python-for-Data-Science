from load_csv import load
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter, MultipleLocator


def projection_lifeexp_grossnproduct(path1: str, path2: str) -> None:
    """
    Scatter plot of life expectancy against gross domestic product (1900).
    param path1: Path to the GDP per person CSV file.
    param path2: Path to the life expectancy CSV file.
    """
    try:
        gdp = load(path1)
        life = load(path2)

        _, ax = plt.subplots()
        ax.scatter(gdp["1900"], life["1900"])

        ax.set_xscale("log")
        ax.set_xlim(300, 10000)
        ax.set_xticks([300, 1000, 10000])
        ax.xaxis.set_major_formatter(FuncFormatter(
            lambda x, _: f"{x / 1000:g}k" if x >= 1000 else f"{int(x)}"))
        # ax.xaxis.set_minor_formatter(NullFormatter())

        ax.yaxis.set_major_locator(MultipleLocator(5))

        ax.set_title("1900")
        ax.set_xlabel("Gross domestic product")
        ax.set_ylabel("Life Expectancy")
        plt.tight_layout()
        plt.show()

    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    projection_lifeexp_grossnproduct(
        "income_per_person_gdppercapita_ppp_inflation_adjusted.csv",
        "life_expectancy_years.csv")
