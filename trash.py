from collections import namedtuple

Pandas = namedtuple(
    "Ps", ["last_name", "first_name", "intake_dt", "exit_dt", "release_reason"]
)

p = Pandas(1, 2, 3, 4, 5)
print(p)
