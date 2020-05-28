from pathlib import Path
import pytest
import juxta.pose as jp


@pytest.fixture
def one_to_one_perfect_match_obj():
    data_path = (
        Path(__file__).resolve().parent
        / "tests"
        / "data"
        / "no-mismatches"
        / "one-to-one"
    )
    d1_path = data_path / "one_to_one-A1.csv"
    d2_path = d1_path
    comparer = jp.Comparer(path1=d1_path, path2=d2_path)
    comparer.set_dataframes(parse_dates=["intake_dt", "exit_dt"])
    return comparer
