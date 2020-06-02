import pandas as pd

from juxta.pose.base import Base


class Prepper(Base):
    def __init__(self, dataset1, dataset2):
        super().__init__(dataset1, dataset2)

    def keep_relevant_columns(self, ds1_columns, ds2_columns=None):
        # not specifying the second dataset's columns will mean that they
        # are the same as the first dataset's columns
        if not ds2_columns:
            ds2_columns = ds1_columns

        df1 = self.df1
        df2 = self.df2

        df1 = df1.loc[:, ds1_columns].copy()
        df2 = df1.loc[:, ds2_columns].copy()

        self.df1 = df1
        self.df2 = df2

        return self

    def map_to_ds1_column_names(self, mapper):
        """just map the second dataset to the first dataset's column names"""
        df2 = self.df2
        df2 = df2.rename(mapper=mapper, axis="columns")
        self.df2 = df2
        return self
