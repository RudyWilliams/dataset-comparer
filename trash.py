from pathlib import Path
import pandas as pd
from juxta.pose.comparer import Comparer

path1 = (
    Path("juxta") / "tests" / "data" / "mismatches" / "one-to-one" / "one_to_one-A1.csv"
)
path2 = (
    Path("juxta")
    / "tests"
    / "data"
    / "mismatches"
    / "one-to-one"
    / "one_to_one-A2-shuffled.csv"
)


comparer = Comparer(path1, path2)
comparer.set_dataframes(parse_dates=["intake_dt", "exit_dt"]).compare_dataframes(
    group_on=["last_name", "first_name"],
    compare_on=["intake_dt", "exit_dt", "release_reason"],
).results_to_df().results_to_csv("set_intermediate_df_test.csv", index=False)
