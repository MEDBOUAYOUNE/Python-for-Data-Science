#Ref : https://pandas.pydata.org/docs/

import pandas as pd

def load(path: str) -> pd.DataFrame:
    """ 
        Loading a file.csv and print it is dimensions
        Arguments:
            str: a path of the file csv 
        
        Return:
            pd.DataFrame: a Pandas DataFrame of the dataset in the file passed

    """
    try:

        df = pd.read_csv(path)
        print(f'File  : {path} | Loading dataset of dimensions ({df.shape[0]}X{df.shape[1]})')
        return  df

    except FileNotFoundError:
        return None
