from juxta.pose.prepper import Prepper


# tests for keeping relevant columns
def test_keep_relevant_columns_same_naming_infer(input_df_1, input_df_2):
    prepper = Prepper(dataset1=input_df_1, dataset2=input_df_2)
    keep_columns = ["last_name", "first_name", "intake_dt", "exit_dt", "release_reason"]
    prepper.keep_relevant_columns(ds1_columns=keep_columns)
    print(prepper.df1.columns)
    print(prepper.df2.columns)
    assert (prepper.df1.columns == keep_columns).all()
    assert (prepper.df2.columns == keep_columns).all()


def test_keep_relevant_columns_same_naming_explicit(input_df_1, input_df_2):
    prepper = Prepper(dataset1=input_df_1, dataset2=input_df_2)
    keep_columns = ["last_name", "first_name", "intake_dt", "exit_dt", "release_reason"]
    prepper.keep_relevant_columns(ds1_columns=keep_columns, ds2_columns=keep_columns)
    print(prepper.df1.columns)
    print(prepper.df2.columns)
    assert (prepper.df1.columns == keep_columns).all()
    assert (prepper.df2.columns == keep_columns).all()


def test_keep_relevant_columns_diff_naming_explicit(input_df_1, input_df_3):
    prepper = Prepper(dataset1=input_df_1, dataset2=input_df_3)
    keep_columns1 = [
        "last_name",
        "first_name",
        "intake_dt",
        "exit_dt",
        "release_reason",
    ]
    print(prepper.df2.columns)
    keep_columns2 = ["lastname", "firstname", "intake_date", "exit_date", "discharge"]
    prepper.keep_relevant_columns(ds1_columns=keep_columns1, ds2_columns=keep_columns2)
    print(prepper.df1.columns)
    print(prepper.df2.columns)
    assert (prepper.df1.columns == keep_columns1).all()
    assert (prepper.df2.columns == keep_columns2).all()


# tests for making column names consistent
