import pandas as pd

# df = pd.DataFrame(
#     {
#         "last_name": ["Williams", "Smith", "Perez"],
#         "first_name": ["John", "Alex", "Samantha"],
#         "id": [11, 22, 33],
#         "SON": ["000-00-0000", "111-11-1111", "222-22-2222"],
#         "program": ["a", "a", "b"],
#         "agency": ["cs", "cs", "cs"],
#         "intake_dt": [
#             pd.Timestamp("2018-12-01"),
#             pd.Timestamp("2018-05-12"),
#             pd.Timestamp("2018-07-31"),
#         ],
#         "exit_dt": [
#             pd.Timestamp("2019-01-25"),
#             pd.Timestamp("2019-04-01"),
#             pd.Timestamp("2019-11-14"),
#         ],
#         "release_reason": ["a" "b", "a"],
#         "DOB": [
#             pd.Timestamp("2000-01-01"),
#             pd.Timestamp("2000-01-01"),
#             pd.Timestamp("2000-01-01"),
#         ],
#     }
# )

data = {
    "last_name": ["Williams", "Smith", "Perez"],
    "first_name": ["John", "Alex", "Samantha"],
    "id": [11, 22, 33],
    "SON": ["000-00-0000", "111-11-1111", "222-22-2222"],
    "program": ["a", "a", "b"],
    "agency": ["cs", "cs", "cs"],
    "intake_dt": [
        pd.Timestamp("2018-12-01"),
        pd.Timestamp("2018-05-12"),
        pd.Timestamp("2018-07-31"),
    ],
    "exit_dt": [
        pd.Timestamp("2019-01-25"),
        pd.Timestamp("2019-04-01"),
        pd.Timestamp("2019-11-14"),
    ],
    "release_reason": ["a", "b", "a"],
    "DOB": [
        pd.Timestamp("2000-01-01"),
        pd.Timestamp("2000-01-01"),
        pd.Timestamp("2000-01-01"),
    ],
}

for key, value in data.items():
    print(f"{key} : {len(value)}")
