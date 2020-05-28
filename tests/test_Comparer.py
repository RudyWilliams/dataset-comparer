def test_1to1_no_mismatch_group_on_one_match_on_rest(one_to_one_perfect_match_obj):
    comparer = one_to_one_perfect_match_obj
    result = comparer.compare_dataframes(
        group_on=["last_name"],
        compare_on=["first_name", "intake_dt", "exit_dt", "release_reason"],
    )
    assert not result


def test_1to1_no_mismatch_group_on_two_match_on_rest(one_to_one_perfect_match_obj):
    comparer = one_to_one_perfect_match_obj
    result = comparer.compare_dataframes(
        group_on=["last_name", "first_name"],
        compare_on=["intake_dt", "exit_dt", "release_reason"],
    )
    assert not result


def test_1to1_no_mismatch_group_on_two_match_on_subset(one_to_one_perfect_match_obj):
    comparer = one_to_one_perfect_match_obj
    result = comparer.compare_dataframes(
        group_on=["last_name", "first_name"], compare_on=["intake_dt", "release_reason"]
    )
    assert not result


def test_1to1_no_mismatch_group_on_rest_match_on_one(one_to_one_perfect_match_obj):
    comparer = one_to_one_perfect_match_obj
    result = comparer.compare_dataframes(
        group_on=["first_name", "intake_dt", "exit_dt", "release_reason"],
        compare_on=["last_name"],
    )
    assert not result
