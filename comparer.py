import os
import pandas as pd

datapath1 = os.path.join(
    "tests", "data", "no-mismatches", "one2one-A1.csv"
)  # config (dev vs production like with snapshot software)
datapath2 = os.path.join("tests", "data", "no-mismatches", "one2one-A2.csv")  # config

df1 = pd.read_csv(datapath1, parse_dates=["intake_dt", "exit_dt"])  # config parsedates
df2 = pd.read_csv(datapath2, parse_dates=["intake_dt", "exit_dt"])  # config parsedates

match_on = ["last_name", "first_name"]  # config

df1_groups = dict(tuple(df1.groupby(match_on)))
df2_groups = dict(tuple(df2.groupby(match_on)))

handcheck = []

for name, data in df1_groups.items():
    compare = df2_groups.get(name)
    if compare.empty:
        # when a potential match cannot be found
        handcheck.append(data)
        continue

    for obs in data.itertuples():
        # this will need updating to generalize and use configurations
        compare["same_intake"] = compare["intake_dt"] == obs.intake_dt
        compare["same_exit"] = compare["exit_dt"] == obs.exit_dt
        compare["same_reason"] = compare["release_reason"] == obs.release_reason
        compare["match_sum"] = compare[["same_intake", "same_exit", "same_reason"]].sum(
            axis=1
        )
        if 3 in compare["match_sum"].values:  # 3 will have to be dynamic to generalize
            print(f"{name[1]} {name[0]}'s record has match in other dataset")
