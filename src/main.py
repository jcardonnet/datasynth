import pandas as pd
from pandas import DataFrame
from pathlib import Path



def hello() -> None:
    print("Hello World")

def load_data(path: Path) -> DataFrame: 
    return pd.read_csv(path)