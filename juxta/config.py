DS1_KEEP_COLUMNS = ["last_name", "first_name", "intake_dt", "exit_dt", "release_reason"]
DS2_KEEP_COLUMNS = None

MAPPER = None

GROUP_ON = ["last_name", "first_name"]
COMPARE_ON = ["intake_dt", "exit_dt", "release_reason"]
