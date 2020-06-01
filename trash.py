from pathlib import Path
import pandas as pd

path = (
    Path("juxta")
    / "tests"
    / "data"
    / "no-mismatches"
    / "one-to-one"
    / "one_to_one-A1.csv"
)
df = pd.read_csv(path)
print(df)
