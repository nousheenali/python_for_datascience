import pandas as pd
from pandas import DataFrame


def load(path: str) -> DataFrame:
    """
    Load a dataset from a CSV file
    params:
    path: path to the file
    returns: the dataset
    """
    try:
        data = pd.read_csv(path)
        print("Loading dataset of dimensions {}".format(data.shape))
        return data
    except Exception as e:
        print(type(e).__name__ + ":", e)
        exit(1)
    except KeyboardInterrupt:
        exit(0)
