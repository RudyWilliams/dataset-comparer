from collections import namedtuple
import os
from pathlib import Path
import pandas as pd
from juxta.pose.comparer import Comparer


def test_init_both_strings():
    comparer = Comparer(
        dataset1="this/is/a/path/string", dataset2="path/string/to/second/dataset"
    )
    assert isinstance(comparer.path1, str)
    assert isinstance(comparer.path2, str)
    assert not comparer.df1  # None
    assert not comparer.df2  # None


def test_init_one_string_one_df():
    comparer = Comparer(dataset1="this/is/a/path/string", dataset2=pd.DataFrame())
    assert isinstance(comparer.path1, str)
    assert not comparer.path2  # None
    assert not comparer.df1  # None
    isinstance(comparer.df2, pd.DataFrame)


def test_init_both_dfs():
    comparer = Comparer(dataset1=pd.DataFrame(), dataset2=pd.DataFrame())
    assert not comparer.path1  # None
    assert not comparer.path2  # None
    assert isinstance(comparer.df1, pd.DataFrame)
    assert isinstance(comparer.df2, pd.DataFrame)


def test_init_both_paths():
    path1 = Path("home") / "path" / "to" / "data1"
    path2 = Path("home") / "path" / "to" / "data2"
    comparer = Comparer(dataset1=path1, dataset2=path2)
    assert isinstance(comparer.path1, Path)
    assert isinstance(comparer.path2, Path)
    assert not comparer.df1  # None
    assert not comparer.df2  # None


def test_init_one_path_one_df():
    path2 = Path("home") / "path" / "to" / "data2"
    comparer = Comparer(dataset1=pd.DataFrame(), dataset2=path2)
    assert not comparer.path1  # None
    assert isinstance(comparer.path2, Path)
    assert isinstance(comparer.df1, pd.DataFrame)
    assert not comparer.df2  # None


def test_init_both_os_paths():
    path1 = os.path.join("data1/path")
    path2 = os.path.join("data2/path")
    comparer = Comparer(dataset1=path1, dataset2=path2)
    assert isinstance(comparer.path1, str)
    assert isinstance(comparer.path2, str)
    assert not comparer.df1  # None
    assert not comparer.df2  # None


def test_compare_dataframes_1to1_all_match_group_on_one_match_on_rest(
    one_to_one_all_match_obj,
):
    comparer = one_to_one_all_match_obj
    comparer.compare_dataframes(
        group_on=["last_name"],
        compare_on=["first_name", "intake_dt", "exit_dt", "release_reason"],
    )
    result = comparer.handcheck
    assert not result


def test_compare_dataframes_1to1_all_match_group_on_two_match_on_rest(
    one_to_one_all_match_obj,
):
    comparer = one_to_one_all_match_obj
    comparer.compare_dataframes(
        group_on=["last_name", "first_name"],
        compare_on=["intake_dt", "exit_dt", "release_reason"],
    )
    result = comparer.handcheck
    assert not result


def test_compare_dataframes_1to1_all_match_group_on_two_match_on_subset(
    one_to_one_all_match_obj,
):
    comparer = one_to_one_all_match_obj
    comparer.compare_dataframes(
        group_on=["last_name", "first_name"], compare_on=["intake_dt", "release_reason"]
    )
    result = comparer.handcheck
    assert not result


def test_compare_dataframes_1to1_all_match_group_on_two_match_on_subset_shuffled(
    shuffled_one_to_one_all_match_obj,
):
    comparer = shuffled_one_to_one_all_match_obj
    comparer.compare_dataframes(
        group_on=["last_name", "first_name"], compare_on=["intake_dt", "release_reason"]
    )
    result = comparer.handcheck
    assert not result


def test_compare_dataframes_1to1_all_match_group_on_rest_match_on_one(
    one_to_one_all_match_obj,
):
    comparer = one_to_one_all_match_obj
    comparer.compare_dataframes(
        group_on=["first_name", "intake_dt", "exit_dt", "release_reason"],
        compare_on=["last_name"],
    )
    result = comparer.handcheck
    assert not result


def test_compare_dataframes_1to1_mismatch_group_on_two_match_on_rest(
    one_to_one_mismatch_obj, namedtuple_list_1
):
    comparer = one_to_one_mismatch_obj
    comparer.compare_dataframes(
        group_on=["last_name", "first_name"],
        compare_on=["intake_dt", "exit_dt", "release_reason"],
    )
    result = comparer.handcheck
    truth = namedtuple_list_1
    # do not care about order
    assert set(result) == set(truth)


def test_compare_dataframes_1to1_mismatch_group_on_two_match_on_rest_shuffled(
    shuffled_one_to_one_mismatch_obj, namedtuple_list_1
):
    comparer = shuffled_one_to_one_mismatch_obj
    comparer.compare_dataframes(
        group_on=["last_name", "first_name"],
        compare_on=["intake_dt", "exit_dt", "release_reason"],
    )
    result = comparer.handcheck
    truth = namedtuple_list_1
    # do not care about order
    assert set(result) == set(truth)


def test_compare_dataframes_1to1_mismatch_columns_ignored(one_to_one_mismatch_obj):
    """Can ignore columns when considering matches"""
    comparer = one_to_one_mismatch_obj
    comparer.compare_dataframes(
        group_on=["last_name", "first_name"], compare_on=["intake_dt"],
    )
    result = comparer.handcheck
    assert not result


def test_compare_dataframes_1to1_unmatchable_with_mismatch(
    one_to_one_unmatchable_obj, namedtuple_list_2
):
    comparer = one_to_one_unmatchable_obj
    comparer.compare_dataframes(
        group_on=["last_name", "first_name"],
        compare_on=["intake_dt", "exit_dt", "release_reason"],
    )
    result = comparer.handcheck
    truth = namedtuple_list_2
    assert set(result) == set(truth)


def test_compare_dataframes_1to1_unmatchable_with_mismatch_shuffled(
    shuffled_one_to_one_unmatchable_obj, namedtuple_list_2
):
    comparer = shuffled_one_to_one_unmatchable_obj
    comparer.compare_dataframes(
        group_on=["last_name", "first_name"],
        compare_on=["intake_dt", "exit_dt", "release_reason"],
    )
    result = comparer.handcheck
    truth = namedtuple_list_2
    assert set(result) == set(truth)


def test_compare_dataframes_1to1_unmatchable_only(
    one_to_one_unmatchable_obj, namedtuple_list_3
):
    # using the feature that we can ignore columns
    comparer = one_to_one_unmatchable_obj
    comparer.compare_dataframes(
        group_on=["last_name", "first_name"], compare_on=["exit_dt", "release_reason"],
    )
    result = comparer.handcheck
    truth = namedtuple_list_3
    assert set(result) == set(truth)


def test_compare_dataframes_MtoM_all_match_group_on_one_match_on_rest(
    many_to_many_all_match_obj,
):
    comparer = many_to_many_all_match_obj
    comparer.compare_dataframes(
        group_on=["last_name"],
        compare_on=["first_name", "intake_dt", "exit_dt", "release_reason"],
    )
    result = comparer.handcheck
    assert not result


def test_compare_dataframes_MtoM_all_match_group_on_two_match_on_rest(
    many_to_many_all_match_obj,
):
    comparer = many_to_many_all_match_obj
    comparer.compare_dataframes(
        group_on=["last_name", "first_name"],
        compare_on=["intake_dt", "exit_dt", "release_reason"],
    )
    result = comparer.handcheck
    assert not result


def test_compare_dataframes_MtoM_all_match_group_on_two_match_on_subset(
    many_to_many_all_match_obj,
):
    comparer = many_to_many_all_match_obj
    comparer.compare_dataframes(
        group_on=["last_name", "first_name"], compare_on=["intake_dt", "exit_dt"],
    )
    result = comparer.handcheck
    assert not result


def test_compare_dataframes_MtoM_all_match_group_on_two_match_on_rest_shuffled(
    shuffled_many_to_many_all_match_obj,
):
    comparer = shuffled_many_to_many_all_match_obj
    comparer.compare_dataframes(
        group_on=["last_name", "first_name"],
        compare_on=["intake_dt", "exit_dt", "release_reason"],
    )
    result = comparer.handcheck
    assert not result


def test_compare_dataframes_MtoM_mismatch_with_MtoM_all_good_MtoM_all_bad_shuffled(
    shuffled_many_to_many_mismatch_obj, namedtuple_list_4
):
    comparer = shuffled_many_to_many_mismatch_obj
    comparer.compare_dataframes(
        group_on=["last_name", "first_name"],
        compare_on=["intake_dt", "exit_dt", "release_reason"],
    )
    result = comparer.handcheck
    truth = namedtuple_list_4
    assert set(result) == set(truth)


def test_compare_dataframes_MtoM_mismatch_with_MtoM_some_bad_shuffled(
    shuffled_many_to_many_mismatch_obj, namedtuple_list_5
):
    comparer = shuffled_many_to_many_mismatch_obj
    comparer.compare_dataframes(
        group_on=["last_name", "first_name"],
        compare_on=["intake_dt", "release_reason"],
    )
    result = comparer.handcheck
    truth = namedtuple_list_5
    assert set(result) == set(truth)


def test_compare_dataframes_1to1_and_MtoM_unmatchable_shuffled(
    shuffled_many_to_many_unmatchable_obj, namedtuple_list_6
):
    comparer = shuffled_many_to_many_unmatchable_obj
    comparer.compare_dataframes(
        group_on=["last_name", "first_name"],
        compare_on=["intake_dt", "exit_dt", "release_reason"],
    )
    result = comparer.handcheck
    truth = namedtuple_list_6
    assert set(result) == set(truth)


def test_to_df_empty_handcheck(shuffled_one_to_one_all_match_obj):
    comparer = shuffled_one_to_one_all_match_obj
    comparer.compare_dataframes(
        group_on=["last_name", "first_name"], compare_on=["intake_dt", "release_reason"]
    ).results_to_df()
    results_df = comparer.results_df
    truth_df = pd.DataFrame()
    assert results_df.equals(truth_df)


def test_to_df_no_kwargs(one_to_one_mismatch_obj, truth_df_1):
    comparer = one_to_one_mismatch_obj
    comparer.compare_dataframes(
        group_on=["last_name", "first_name"],
        compare_on=["intake_dt", "exit_dt", "release_reason"],
    ).results_to_df()
    results_df = comparer.results_df.sort_values(by="Index").reset_index(drop=True)
    truth_df = truth_df_1.sort_values(by="Index").reset_index(drop=True)
    assert results_df.equals(truth_df)


def test_to_df_with_kwargs(one_to_one_mismatch_obj, truth_df_1):
    comparer = one_to_one_mismatch_obj
    comparer.compare_dataframes(
        group_on=["last_name", "first_name"],
        compare_on=["intake_dt", "exit_dt", "release_reason"],
    ).results_to_df(columns=["c1", "c2", "c3", "c4", "c5", "c6"])
    results_df = comparer.results_df.sort_values(by="c1").reset_index(drop=True)
    truth_df = truth_df_1.sort_values(by="Index").reset_index(drop=True)
    truth_df.columns = ["c1", "c2", "c3", "c4", "c5", "c6"]
    assert results_df.equals(truth_df)
