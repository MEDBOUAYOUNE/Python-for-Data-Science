#REF: https://matplotlib.org/stable/tutorials/pyplot.html#sphx-glr-tutorials-pyplot-py

import matplotlib.pyplot as plt
from load_csv import load
import pandas as pd

def gg(path: str) -> None:
    try:
        df = load(path)
        print(df.rows)
        # plt.plot(df['country'], df['country'])
        # plt.show()
    except Exception as e:
        print(f'Error: {e}')

if __name__ == "__main__":
    gg("life_expectancy_years.csv")