import argparse
from pathlib import Path
import sys

from juxta.pose.comparer import Comparer
from juxta.pose.prepper import Prepper


def main():
    parser = argparse.ArgumentParser(
        description="Compare two datasets by passing paths to their CSV files"
    )
    parser.add_argument(
        "path1", type=lambda x: Path(x), help="path/to/dataset1.csv file"
    )
    parser.add_argument(
        "path2", type=lambda x: Path(x), help="path/to/dataset2.csv file"
    )
    parser.add_argument(
        "--use-config",
        action="store_true",
        help="setting this flag will use the config file for setting the other optional args",
    )
    parser.add_argument(
        "--save-as-excel",
        action="store_true",
        help="Set this to save result as excel. Otherwise, will save as CSV file.",
    )
    parser.add_argument("--ds1-keep-columns", nargs="+")
    parser.add_argument("--ds2-keep-columns", nargs="+")
    parser.add_argument("--mapper", nargs="+")
    parser.add_argument("--group-on", nargs="+")
    parser.add_argument("--compare-on", nargs="+")

    args = parser.parse_args()

    if args.use_config:
        from juxta import config

        print(" ---> filling out optional args with config file")
        ds1_columns = config.DS1_KEEP_COLUMNS
        ds2_columns = config.DS2_KEEP_COLUMNS
        mapper = config.MAPPER
        group_on = config.GROUP_ON
        compare_on = config.COMPARE_ON

    else:
        ds1_columns = args.ds1_keep_columns
        ds2_columns = args.ds2_keep_columns
        mapper = args.mapper
        group_on = args.group_on
        compare_on = args.compare_on

        if not ds1_columns:  # if they are None
            print(
                "COULD NOT RUN: at least --ds1-keep-columns must be set if not using config file"
            )
            sys.exit()

        if (not mapper) or (not group_on) or (not compare_on):
            print(
                "COULD NOT RUN: --mapper, --group-on, and --compare-on must all be set if not using config file"
            )
            sys.exit()

    prepper = Prepper(dataset1=args.path1, dataset2=args.path2)
    prepper.set_dataframes().keep_relevant_columns(
        ds1_columns=ds1_columns, ds2_columns=ds2_columns
    ).map_to_ds1_column_names(mapper=mapper)

    comparer = Comparer(dataset1=prepper.df1, dataset2=prepper.df2)
    comparer.compare_dataframes(group_on=group_on, compare_on=compare_on)

    if args.save_as_excel:
        output_path = args.path1.parent / "results.xlsx"
        comparer.results_to_excel(output_path)
        sys.exit()

    output_path = args.path1.parent / "result.csv"
    comparer.results_to_csv(output_path)


if __name__ == "__main__":
    main()
