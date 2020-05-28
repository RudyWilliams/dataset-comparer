import os
import pandas as pd


class Comparer:
    def __init__(self, path1, path2):
        self.path1 = path1
        self.path2 = path2
        self.df1 = None
        self.df2 = None
        # self.handcheck = None

    def set_dataframes(self, **kwargs):
        # this is fine bc the dataframes are required to be converted to the same
        # column names before hand
        self.df1 = pd.read_csv(self.path1, **kwargs)
        self.df2 = pd.read_csv(self.path2, **kwargs)
        return self

    def compare_dataframes(self, group_on, compare_on):
        n_compare_columns = len(compare_on)
        same_columns = [f"_same_{c}" for c in compare_on]
        df1_groups = tuple(self.df1.groupby(group_on))
        df2_groups_dict = dict(tuple(self.df2.groupby(group_on)))

        handcheck = []

        for identifier, data in df1_groups:
            # only need to check a subset of df2
            compare = df2_groups_dict.get(identifier, None)
            if compare is None:
                print(f"{identifier} could not be found in other data set.")
                handcheck.extend(list(data.itertuples()))
                continue

            for obs in data.itertuples():

                obs_dict = obs._asdict()
                for column, same_column in zip(compare_on, same_columns):
                    compare[same_column] = compare[column] == obs_dict[column]
                compare["_match_sum"] = compare[same_columns].sum(axis=1)

                if n_compare_columns in compare["_match_sum"].values:
                    print(f"{identifier} has matching records in data sets.")
                else:
                    print(f"{identifier} did NOT have matching record in data sets.")
                    handcheck.append(obs)

        return handcheck


if __name__ == "__main__":

    datapath1 = os.path.join(
        "tests", "data", "unmatchable", "one2one-A1.csv"
    )  # config (dev vs production like with snapshot software)
    datapath2 = os.path.join("tests", "data", "unmatchable", "one2one-A2.csv")  # config
    c = Comparer(datapath1, datapath2)
    c.set_dataframes(parse_dates=["intake_dt", "exit_dt"])
    handcheck = c.compare_dataframes(
        group_on=["last_name", "first_name"],
        compare_on=["intake_dt", "exit_dt", "release_reason"],
    )

    print(pd.DataFrame(handcheck))
