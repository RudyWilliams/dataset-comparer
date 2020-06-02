from pathlib import Path
import pandas as pd


class Base:
    def __init__(self, dataset1, dataset2):
        if isinstance(dataset1, (str, Path)):
            self.path1 = dataset1
            self.df1 = None
        elif isinstance(dataset1, pd.DataFrame):
            self.path1 = None
            self.df1 = dataset1
        else:
            raise ValueError("dataset1 may only be a path, string, or dataframe")

        if isinstance(dataset2, (str, Path)):
            self.path2 = dataset2
            self.df2 = None
        elif isinstance(dataset2, pd.DataFrame):
            self.path2 = None
            self.df2 = dataset2
        else:
            raise ValueError("dataset2 may only be a path, string, or dataframe")

    def set_dataframes(self, **kwargs):
        # this is fine bc the dataframes are required to be converted to the same
        # column names before hand
        if self.path1:
            self.df1 = pd.read_csv(self.path1, **kwargs)
        if self.path2:
            self.df2 = pd.read_csv(self.path2, **kwargs)
        return self
