# Ref : https://pandas.pydata.org/docs/
import pandas as pd


def load(path: str) -> pd.DataFrame:
    """
        Loading a file.csv and print it is dimensions
        Arguments:
            str: a path of the file csv
        Return:
            pd.DataFrame: a Pandas DataFrame of the dataset in the file passed
        Raises:
            FileNotFoundError: If the CSV file does not exist.
            ValueError: If the CSV file cannot be read or parsed.
            AssertionError: If the path is not a string, is empty, or has an unsupported
            format (only .csv is supported).
    """
    try:
        assert isinstance(path, str), "Path must be a string"
        assert path.endswith('.csv'), "Unsupported file format, only .csv is supported"
        assert len(path) > 0, "Path cannot be empty"
        df = pd.read_csv(path, index_col=0)
        print(f'File  : {path} | Loading dataset of dimensions ({df.shape[0]}X{df.shape[1]})')
        return df
    except FileNotFoundError:
        print(f"File not found: {path}")
    except ValueError as error:
        print(f"Value error: {error}")
    except AssertionError as error:
        print(f"Assertion error: {error}")
    except Exception as error:
        print(f"An unexpected error occurred: {error}")
