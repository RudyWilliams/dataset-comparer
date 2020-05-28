from collections import namedtuple
import pandas as pd


def test_compare_dataframes_1to1_all_match_group_on_one_match_on_rest(
    one_to_one_all_match_obj,
):
    comparer = one_to_one_all_match_obj
    result = comparer.compare_dataframes(
        group_on=["last_name"],
        compare_on=["first_name", "intake_dt", "exit_dt", "release_reason"],
    )
    assert not result


def test_compare_dataframes_1to1_all_match_group_on_two_match_on_rest(
    one_to_one_all_match_obj,
):
    comparer = one_to_one_all_match_obj
    result = comparer.compare_dataframes(
        group_on=["last_name", "first_name"],
        compare_on=["intake_dt", "exit_dt", "release_reason"],
    )
    assert not result


def test_compare_dataframes_1to1_all_match_group_on_two_match_on_subset(
    one_to_one_all_match_obj,
):
    comparer = one_to_one_all_match_obj
    result = comparer.compare_dataframes(
        group_on=["last_name", "first_name"], compare_on=["intake_dt", "release_reason"]
    )
    assert not result


def test_compare_dataframes_1to1_all_match_group_on_rest_match_on_one(
    one_to_one_all_match_obj,
):
    comparer = one_to_one_all_match_obj
    result = comparer.compare_dataframes(
        group_on=["first_name", "intake_dt", "exit_dt", "release_reason"],
        compare_on=["last_name"],
    )
    assert not result


def test_compare_dataframes_1to1_mismatch_group_on_two_match_on_rest(
    one_to_one_mismatch_obj, pandas_namedtuple
):
    comparer = one_to_one_mismatch_obj
    result = comparer.compare_dataframes(
        group_on=["last_name", "first_name"],
        compare_on=["intake_dt", "exit_dt", "release_reason"],
    )
    truth = {
        pandas_namedtuple(
            Index=3,
            last_name="Smith",
            first_name="Jonathan",
            intake_dt=pd.Timestamp("2018-01-08"),
            exit_dt=pd.Timestamp("2019-10-24"),
            release_reason="c",
        ),
        pandas_namedtuple(
            Index=7,
            last_name="Landry",
            first_name="Kristina",
            intake_dt=pd.Timestamp("2018-06-18"),
            exit_dt=pd.Timestamp("2019-04-01"),
            release_reason="a",
        ),
    }
    # do not care about order
    assert set(result) == truth


def test_compare_dataframes_1to1_mismatch_columns_ignored(one_to_one_mismatch_obj):
    """Can ignore columns when considering matches"""
    comparer = one_to_one_mismatch_obj
    result = comparer.compare_dataframes(
        group_on=["last_name", "first_name"], compare_on=["intake_dt"],
    )
    assert not result
