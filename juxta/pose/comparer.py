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

        self.handcheck = handcheck

        return self

    def results_to_df(self, **kwargs):
        self.results_df = pd.DataFrame(self.handcheck, **kwargs)
        return self

    def results_to_csv(self, output_path, **kwargs):
        if hasattr(self, "results_df"):
            self.results_df.to_csv(output_path, **kwargs)
        else:
            # using this implementation means cannot add args to the df build part
            pd.DataFrame(self.handcheck).to_csv(output_path, **kwargs)
        return self

    def results_to_excel(self, output_path, **kwargs):
        if hasattr(self, "results_df"):
            self.results_df.to_excel(output_path, **kwargs)
        else:
            # using this implementation means cannot add args to the df build part
            pd.DataFrame(self.handcheck).to_excel(output_path, **kwargs)
        return self


if __name__ == "__main__":

    from pathlib import Path

    print(Path(__file__).resolve().parent.parent)
    data_path = (
        Path(__file__).resolve().parent.parent
        / "tests"
        / "data"
        / "unmatchable"
        / "many-to-many"
    )
    d1_path = data_path / "many_to_many-A1.csv"
    d2_path = data_path / "many_to_many-A2-shuffled.csv"
    comparer = Comparer(path1=d1_path, path2=d2_path)
    comparer.set_dataframes(parse_dates=["intake_dt", "exit_dt"]).compare_dataframes(
        group_on=["last_name", "first_name"],
        compare_on=["intake_dt", "exit_dt", "release_reason"],
    )

    comparer.results_to_excel("test.xlsx", index=False)
    # original index still shows up bc it is useful for referencing the data
    # but the index for the results df is not useful and is not written to the file
