from collections import namedtuple
from pathlib import Path
import pytest
from juxta.pose.comparer import Comparer


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
    comparer = Comparer(path1=d1_path, path2=d2_path)
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
    comparer = Comparer(path1=d1_path, path2=d2_path)
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
    comparer = Comparer(path1=d1_path, path2=d2_path)
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
    comparer = Comparer(path1=d1_path, path2=d2_path)
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
    comparer = Comparer(path1=d1_path, path2=d2_path)
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
    comparer = Comparer(path1=d1_path, path2=d2_path)
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
    comparer = Comparer(path1=d1_path, path2=d2_path)
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
    comparer = Comparer(path1=d1_path, path2=d2_path)
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
    comparer = Comparer(path1=d1_path, path2=d2_path)
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
    comparer = Comparer(path1=d1_path, path2=d2_path)
    comparer.set_dataframes(parse_dates=["intake_dt", "exit_dt"])
    return comparer


if __name__ == "__main__":
    comparer = shuffled_many_to_many_unmatchable_obj()
    print(comparer.df1)
    print("------------------")
    print(comparer.df2)
