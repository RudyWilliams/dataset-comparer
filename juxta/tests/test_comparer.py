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


def test_compare_dataframes_1to1_all_match_group_on_two_match_on_subset_shuffled(
    shuffled_one_to_one_all_match_obj,
):
    comparer = shuffled_one_to_one_all_match_obj
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


def test_compare_dataframes_1to1_mismatch_group_on_two_match_on_rest_shuffled(
    shuffled_one_to_one_mismatch_obj, pandas_namedtuple
):
    comparer = shuffled_one_to_one_mismatch_obj
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


def test_compare_dataframes_1to1_unmatchable_with_mismatch(
    one_to_one_unmatchable_obj, pandas_namedtuple
):
    comparer = one_to_one_unmatchable_obj
    result = comparer.compare_dataframes(
        group_on=["last_name", "first_name"],
        compare_on=["intake_dt", "exit_dt", "release_reason"],
    )
    truth = {
        pandas_namedtuple(
            Index=0,
            last_name="Houston",
            first_name="Dennis",
            intake_dt=pd.Timestamp("2018-01-20"),
            exit_dt=pd.Timestamp("2019-01-12"),
            release_reason="c",
        ),
        pandas_namedtuple(
            Index=6,
            last_name="Perez",
            first_name="Denise",
            intake_dt=pd.Timestamp("2019-06-18"),
            exit_dt=pd.Timestamp("2019-08-03"),
            release_reason="c",
        ),
        pandas_namedtuple(
            Index=9,
            last_name="Johnson",
            first_name="Anthony",
            intake_dt=pd.Timestamp("2019-07-18"),
            exit_dt=pd.Timestamp("2019-03-31"),
            release_reason="c",
        ),
    }
    assert set(result) == truth


def test_compare_dataframes_1to1_unmatchable_with_mismatch_shuffled(
    shuffled_one_to_one_unmatchable_obj, pandas_namedtuple
):
    comparer = shuffled_one_to_one_unmatchable_obj
    result = comparer.compare_dataframes(
        group_on=["last_name", "first_name"],
        compare_on=["intake_dt", "exit_dt", "release_reason"],
    )
    truth = {
        pandas_namedtuple(
            Index=0,
            last_name="Houston",
            first_name="Dennis",
            intake_dt=pd.Timestamp("2018-01-20"),
            exit_dt=pd.Timestamp("2019-01-12"),
            release_reason="c",
        ),
        pandas_namedtuple(
            Index=6,
            last_name="Perez",
            first_name="Denise",
            intake_dt=pd.Timestamp("2019-06-18"),
            exit_dt=pd.Timestamp("2019-08-03"),
            release_reason="c",
        ),
        pandas_namedtuple(
            Index=9,
            last_name="Johnson",
            first_name="Anthony",
            intake_dt=pd.Timestamp("2019-07-18"),
            exit_dt=pd.Timestamp("2019-03-31"),
            release_reason="c",
        ),
    }
    assert set(result) == truth


def test_compare_dataframes_1to1_unmatchable_only(
    one_to_one_unmatchable_obj, pandas_namedtuple
):
    # using the feature that we can ignore columns
    comparer = one_to_one_unmatchable_obj
    result = comparer.compare_dataframes(
        group_on=["last_name", "first_name"], compare_on=["exit_dt", "release_reason"],
    )
    truth = {
        pandas_namedtuple(
            Index=0,
            last_name="Houston",
            first_name="Dennis",
            intake_dt=pd.Timestamp("2018-01-20"),
            exit_dt=pd.Timestamp("2019-01-12"),
            release_reason="c",
        ),
        pandas_namedtuple(
            Index=6,
            last_name="Perez",
            first_name="Denise",
            intake_dt=pd.Timestamp("2019-06-18"),
            exit_dt=pd.Timestamp("2019-08-03"),
            release_reason="c",
        ),
    }
    assert set(result) == truth


def test_compare_dataframes_MtoM_all_match_group_on_one_match_on_rest(
    many_to_many_all_match_obj,
):
    comparer = many_to_many_all_match_obj
    result = comparer.compare_dataframes(
        group_on=["last_name"],
        compare_on=["first_name", "intake_dt", "exit_dt", "release_reason"],
    )
    assert not result


def test_compare_dataframes_MtoM_all_match_group_on_two_match_on_rest(
    many_to_many_all_match_obj,
):
    comparer = many_to_many_all_match_obj
    result = comparer.compare_dataframes(
        group_on=["last_name", "first_name"],
        compare_on=["intake_dt", "exit_dt", "release_reason"],
    )
    assert not result


def test_compare_dataframes_MtoM_all_match_group_on_two_match_on_subset(
    many_to_many_all_match_obj,
):
    comparer = many_to_many_all_match_obj
    result = comparer.compare_dataframes(
        group_on=["last_name", "first_name"], compare_on=["intake_dt", "exit_dt"],
    )
    assert not result


def test_compare_dataframes_MtoM_all_match_group_on_two_match_on_rest_shuffled(
    shuffled_many_to_many_all_match_obj,
):
    comparer = shuffled_many_to_many_all_match_obj
    result = comparer.compare_dataframes(
        group_on=["last_name", "first_name"],
        compare_on=["intake_dt", "exit_dt", "release_reason"],
    )
    assert not result


def test_compare_dataframes_MtoM_mismatch_with_MtoM_all_good_MtoM_all_bad_shuffled(
    shuffled_many_to_many_mismatch_obj, pandas_namedtuple
):
    comparer = shuffled_many_to_many_mismatch_obj
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
            Index=10,
            last_name="Smith",
            first_name="Jonathan",
            intake_dt=pd.Timestamp("2018-08-19"),
            exit_dt=pd.Timestamp("2019-05-10"),
            release_reason="b",
        ),
        pandas_namedtuple(
            Index=11,
            last_name="Smith",
            first_name="Jonathan",
            intake_dt=pd.Timestamp("2018-04-04"),
            exit_dt=pd.Timestamp("2019-12-14"),
            release_reason="b",
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
    assert set(result) == truth


def test_compare_dataframes_MtoM_mismatch_with_MtoM_some_bad_shuffled(
    shuffled_many_to_many_mismatch_obj, pandas_namedtuple
):
    comparer = shuffled_many_to_many_mismatch_obj
    result = comparer.compare_dataframes(
        group_on=["last_name", "first_name"],
        compare_on=["intake_dt", "release_reason"],
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
            Index=10,
            last_name="Smith",
            first_name="Jonathan",
            intake_dt=pd.Timestamp("2018-08-19"),
            exit_dt=pd.Timestamp("2019-05-10"),
            release_reason="b",
        ),
    }
    assert set(result) == truth


def test_compare_dataframes_1to1_and_MtoM_unmatchable_shuffled(
    shuffled_many_to_many_unmatchable_obj, pandas_namedtuple
):
    comparer = shuffled_many_to_many_unmatchable_obj
    result = comparer.compare_dataframes(
        group_on=["last_name", "first_name"],
        compare_on=["intake_dt", "exit_dt", "release_reason"],
    )
    truth = {
        pandas_namedtuple(
            Index=0,
            last_name="Houston",
            first_name="Dennis",
            intake_dt=pd.Timestamp("2018-01-20"),
            exit_dt=pd.Timestamp("2019-01-12"),
            release_reason="c",
        ),
        pandas_namedtuple(
            Index=8,
            last_name="Valenzuela",
            first_name="Clifford",
            intake_dt=pd.Timestamp("2018-11-24"),
            exit_dt=pd.Timestamp("2019-05-15"),
            release_reason="b",
        ),
        pandas_namedtuple(
            Index=10,
            last_name="Valenzuela",
            first_name="Clifford",
            intake_dt=pd.Timestamp("2018-08-19"),
            exit_dt=pd.Timestamp("2019-10-16"),
            release_reason="b",
        ),
        pandas_namedtuple(
            Index=11,
            last_name="Valenzuela",
            first_name="Clifford",
            intake_dt=pd.Timestamp("2018-04-04"),
            exit_dt=pd.Timestamp("2019-05-10"),
            release_reason="b",
        ),
    }
    assert set(result) == truth
