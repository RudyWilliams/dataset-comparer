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
