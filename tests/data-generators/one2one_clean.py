import datetime
from faker import Faker
import pandas as pd

fake = Faker()
Faker.seed(1)

data_len = 10
intake_range = [
    datetime.date(year=2018, month=1, day=1),
    datetime.date(year=2019, month=12, day=31),
]
exit_range = [
    datetime.date(year=2019, month=1, day=1),
    datetime.date(year=2019, month=12, day=31),
]  # for this purpose, we don't care if the exit date is before the intake date

first_names = [fake.first_name() for _ in range(data_len)]
last_names = [fake.last_name() for _ in range(data_len)]
intake_dts = [
    fake.date_between_dates(intake_range[0], intake_range[1]) for _ in range(data_len)
]
exit_dts = [
    fake.date_between_dates(exit_range[0], exit_range[1]) for _ in range(data_len)
]
release_reasons = [fake.random_element() for _ in range(data_len)]


df1 = pd.DataFrame(
    {
        "last_name": last_names,
        "first_name": first_names,
        "intake_dt": intake_dts,
        "exit_dt": exit_dts,
        "release_reason": release_reasons,
    }
)

df2 = df1.copy()


classification = "no-mismatches"
df1.to_csv(f"tests/data/{classification}/one2one-A1.csv", index=False)
df2.to_csv(f"tests/data/{classification}/one2one-A2.csv", index=False)
