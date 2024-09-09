from logparse import Logparse as lp
from logparse_get import LogparseGet as lpg
import argparse


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "field",
        help="Field to parse [ip|ua|ref|code|size|url|method]",
        choices=["ip", "ua", "ref", "code", "size", "url", "method"],
        nargs="*",
    )
    parser.add_argument("-f", "--file", help="Path to file, default ./access.log")
    parser.add_argument("-s", "--search", help="String to search for", type=str)
    parser.add_argument("-l", "--limit", help="Limit the number of outputs", type=int, required=False)
    parser.parse_args()
    args = parser.parse_args()

    file = "access.log"
    if args.file:
        file = args.file

    if len(args.field) == 1:
        out: list = lp.count_single(file, args.field[0], args.search)
        for i in out:
            print(i[0], f"\t{i[1]}")
    else:
        out: list = lp.count_more(file, args.field, args.search)

        for line in out:
            for item in range(len(line)):
                print(f"{line[item]}\t", end="")
            print()


if __name__ == "__main__":
    main()
