from collections import namedtuple
from pathlib import Path
import pytest
from juxta.pose.comparer import Comparer


@pytest.fixture
def one_to_one_all_match_obj():
    data_path = (
        Path(__file__).resolve().parent
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
def one_to_one_mismatch_obj():
    data_path = (
        Path(__file__).resolve().parent / "tests" / "data" / "mismatches" / "one-to-one"
    )
    d1_path = data_path / "one_to_one-A1.csv"
    d2_path = data_path / "one_to_one-A2.csv"
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
