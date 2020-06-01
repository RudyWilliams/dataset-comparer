from collections import namedtuple
from pathlib import Path
import pandas as pd
import pytest
from juxta.pose.comparer import Comparer


Pandas = namedtuple(
    "Pandas",
    ["Index", "last_name", "first_name", "intake_dt", "exit_dt", "release_reason"],
)


@pytest.fixture
def one_to_one_all_match_obj():
    data_path = (
        Path(__file__).resolve().parent
        / "juxta"
        / "tests"
        / "data"
        / "no-mismatches"
        / "one-to-one"
    )
    d1_path = data_path / "one_to_one-A1.csv"
    d2_path = d1_path
    comparer = Comparer(dataset1=d1_path, dataset2=d2_path)
    comparer.set_dataframes(parse_dates=["intake_dt", "exit_dt"])
    return comparer


@pytest.fixture
def shuffled_one_to_one_all_match_obj():
    data_path = (
        Path(__file__).resolve().parent
        / "juxta"
        / "tests"
        / "data"
        / "no-mismatches"
        / "one-to-one"
    )
    d1_path = data_path / "one_to_one-A1.csv"
    d2_path = data_path / "one_to_one-A1-shuffled.csv"
    comparer = Comparer(dataset1=d1_path, dataset2=d2_path)
    comparer.set_dataframes(parse_dates=["intake_dt", "exit_dt"])
    return comparer


@pytest.fixture
def one_to_one_mismatch_obj():
    data_path = (
        Path(__file__).resolve().parent
        / "juxta"
        / "tests"
        / "data"
        / "mismatches"
        / "one-to-one"
    )
    d1_path = data_path / "one_to_one-A1.csv"
    d2_path = data_path / "one_to_one-A2.csv"
    comparer = Comparer(dataset1=d1_path, dataset2=d2_path)
    comparer.set_dataframes(parse_dates=["intake_dt", "exit_dt"])
    return comparer


@pytest.fixture
def shuffled_one_to_one_mismatch_obj():
    data_path = (
        Path(__file__).resolve().parent
        / "juxta"
        / "tests"
        / "data"
        / "mismatches"
        / "one-to-one"
    )
    d1_path = data_path / "one_to_one-A1.csv"
    d2_path = data_path / "one_to_one-A2-shuffled.csv"
    comparer = Comparer(dataset1=d1_path, dataset2=d2_path)
    comparer.set_dataframes(parse_dates=["intake_dt", "exit_dt"])
    return comparer


@pytest.fixture
def pandas_namedtuple():
    return namedtuple(
        "Pandas",
        ["Index", "last_name", "first_name", "intake_dt", "exit_dt", "release_reason"],
    )


@pytest.fixture
def one_to_one_unmatchable_obj():
    data_path = (
        Path(__file__).resolve().parent
        / "juxta"
        / "tests"
        / "data"
        / "unmatchable"
        / "one-to-one"
    )
    d1_path = data_path / "one_to_one-A1.csv"
    d2_path = data_path / "one_to_one-A2.csv"
    comparer = Comparer(dataset1=d1_path, dataset2=d2_path)
    comparer.set_dataframes(parse_dates=["intake_dt", "exit_dt"])
    return comparer


@pytest.fixture
def shuffled_one_to_one_unmatchable_obj():
    data_path = (
        Path(__file__).resolve().parent
        / "juxta"
        / "tests"
        / "data"
        / "unmatchable"
        / "one-to-one"
    )
    d1_path = data_path / "one_to_one-A1.csv"
    d2_path = data_path / "one_to_one-A2-shuffled.csv"
    comparer = Comparer(dataset1=d1_path, dataset2=d2_path)
    comparer.set_dataframes(parse_dates=["intake_dt", "exit_dt"])
    return comparer


@pytest.fixture
def many_to_many_all_match_obj():
    data_path = (
        Path(__file__).resolve().parent
        / "juxta"
        / "tests"
        / "data"
        / "no-mismatches"
        / "many-to-many"
    )
    d1_path = data_path / "many_to_many-A1.csv"
    d2_path = d1_path
    comparer = Comparer(dataset1=d1_path, dataset2=d2_path)
    comparer.set_dataframes(parse_dates=["intake_dt", "exit_dt"])
    return comparer


@pytest.fixture  # can comment out to make sure correct data is set
def shuffled_many_to_many_all_match_obj():
    data_path = (
        Path(__file__).resolve().parent
        / "juxta"
        / "tests"
        / "data"
        / "no-mismatches"
        / "many-to-many"
    )
    d1_path = data_path / "many_to_many-A1.csv"
    d2_path = data_path / "many_to_many-A1-shuffled.csv"
    comparer = Comparer(dataset1=d1_path, dataset2=d2_path)
    comparer.set_dataframes(parse_dates=["intake_dt", "exit_dt"])
    return comparer


@pytest.fixture  # can comment out to make sure correct data is set
def shuffled_many_to_many_mismatch_obj():
    data_path = (
        Path(__file__).resolve().parent
        / "juxta"
        / "tests"
        / "data"
        / "mismatches"
        / "many-to-many"
    )
    d1_path = data_path / "many_to_many-A1.csv"
    d2_path = data_path / "many_to_many-A2-shuffled.csv"
    comparer = Comparer(dataset1=d1_path, dataset2=d2_path)
    comparer.set_dataframes(parse_dates=["intake_dt", "exit_dt"])
    return comparer


@pytest.fixture  # can comment out to make sure correct data is set
def shuffled_many_to_many_unmatchable_obj():
    data_path = (
        Path(__file__).resolve().parent
        / "juxta"
        / "tests"
        / "data"
        / "unmatchable"
        / "many-to-many"
    )
    d1_path = data_path / "many_to_many-A1.csv"
    d2_path = data_path / "many_to_many-A2-shuffled.csv"
    comparer = Comparer(dataset1=d1_path, dataset2=d2_path)
    comparer.set_dataframes(parse_dates=["intake_dt", "exit_dt"])
    return comparer


@pytest.fixture
def namedtuple_list_1():
    return [
        Pandas(
            Index=3,
            last_name="Smith",
            first_name="Jonathan",
            intake_dt=pd.Timestamp("2018-01-08"),
            exit_dt=pd.Timestamp("2019-10-24"),
            release_reason="c",
        ),
        Pandas(
            Index=7,
            last_name="Landry",
            first_name="Kristina",
            intake_dt=pd.Timestamp("2018-06-18"),
            exit_dt=pd.Timestamp("2019-04-01"),
            release_reason="a",
        ),
    ]


@pytest.fixture
def namedtuple_list_2():
    return [
        Pandas(
            Index=0,
            last_name="Houston",
            first_name="Dennis",
            intake_dt=pd.Timestamp("2018-01-20"),
            exit_dt=pd.Timestamp("2019-01-12"),
            release_reason="c",
        ),
        Pandas(
            Index=6,
            last_name="Perez",
            first_name="Denise",
            intake_dt=pd.Timestamp("2019-06-18"),
            exit_dt=pd.Timestamp("2019-08-03"),
            release_reason="c",
        ),
        Pandas(
            Index=9,
            last_name="Johnson",
            first_name="Anthony",
            intake_dt=pd.Timestamp("2019-07-18"),
            exit_dt=pd.Timestamp("2019-03-31"),
            release_reason="c",
        ),
    ]


@pytest.fixture
def namedtuple_list_3():
    return [
        Pandas(
            Index=0,
            last_name="Houston",
            first_name="Dennis",
            intake_dt=pd.Timestamp("2018-01-20"),
            exit_dt=pd.Timestamp("2019-01-12"),
            release_reason="c",
        ),
        Pandas(
            Index=6,
            last_name="Perez",
            first_name="Denise",
            intake_dt=pd.Timestamp("2019-06-18"),
            exit_dt=pd.Timestamp("2019-08-03"),
            release_reason="c",
        ),
    ]


@pytest.fixture
def namedtuple_list_4():
    return [
        Pandas(
            Index=3,
            last_name="Smith",
            first_name="Jonathan",
            intake_dt=pd.Timestamp("2018-01-08"),
            exit_dt=pd.Timestamp("2019-10-24"),
            release_reason="c",
        ),
        Pandas(
            Index=10,
            last_name="Smith",
            first_name="Jonathan",
            intake_dt=pd.Timestamp("2018-08-19"),
            exit_dt=pd.Timestamp("2019-05-10"),
            release_reason="b",
        ),
        Pandas(
            Index=11,
            last_name="Smith",
            first_name="Jonathan",
            intake_dt=pd.Timestamp("2018-04-04"),
            exit_dt=pd.Timestamp("2019-12-14"),
            release_reason="b",
        ),
        Pandas(
            Index=7,
            last_name="Landry",
            first_name="Kristina",
            intake_dt=pd.Timestamp("2018-06-18"),
            exit_dt=pd.Timestamp("2019-04-01"),
            release_reason="a",
        ),
    ]


@pytest.fixture
def namedtuple_list_5():
    return [
        Pandas(
            Index=3,
            last_name="Smith",
            first_name="Jonathan",
            intake_dt=pd.Timestamp("2018-01-08"),
            exit_dt=pd.Timestamp("2019-10-24"),
            release_reason="c",
        ),
        Pandas(
            Index=10,
            last_name="Smith",
            first_name="Jonathan",
            intake_dt=pd.Timestamp("2018-08-19"),
            exit_dt=pd.Timestamp("2019-05-10"),
            release_reason="b",
        ),
    ]


@pytest.fixture
def namedtuple_list_6():
    return [
        Pandas(
            Index=0,
            last_name="Houston",
            first_name="Dennis",
            intake_dt=pd.Timestamp("2018-01-20"),
            exit_dt=pd.Timestamp("2019-01-12"),
            release_reason="c",
        ),
        Pandas(
            Index=8,
            last_name="Valenzuela",
            first_name="Clifford",
            intake_dt=pd.Timestamp("2018-11-24"),
            exit_dt=pd.Timestamp("2019-05-15"),
            release_reason="b",
        ),
        Pandas(
            Index=10,
            last_name="Valenzuela",
            first_name="Clifford",
            intake_dt=pd.Timestamp("2018-08-19"),
            exit_dt=pd.Timestamp("2019-10-16"),
            release_reason="b",
        ),
        Pandas(
            Index=11,
            last_name="Valenzuela",
            first_name="Clifford",
            intake_dt=pd.Timestamp("2018-04-04"),
            exit_dt=pd.Timestamp("2019-05-10"),
            release_reason="b",
        ),
    ]


@pytest.fixture
def truth_df_1():
    return pd.DataFrame(
        {
            "Index": [3, 7],
            "last_name": ["Smith", "Landry"],
            "first_name": ["Jonathan", "Kristina"],
            "intake_dt": [pd.Timestamp("2018-01-08"), pd.Timestamp("2018-06-18")],
            "exit_dt": [pd.Timestamp("2019-10-24"), pd.Timestamp("2019-04-01")],
            "release_reason": ["c", "a"],
        }
    )


if __name__ == "__main__":
    comparer = shuffled_many_to_many_unmatchable_obj()
    print(comparer.df1)
    print("------------------")
    print(comparer.df2)
