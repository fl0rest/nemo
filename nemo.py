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
    parser.add_argument(
        "-l",
        "--limit",
        help="Limit the number of outputs (default: 0)",
        type=int,
        required=False,
        default=0,
    )
    args = parser.parse_args()

    file: str = "access.log"
    if args.file:
        file = args.file

    limit: int = 0
    if args.limit > 0:
        limit = args.limit

    out: list = lp.count(file, args.field, args.search)

    match limit:
        case 0:
            for line in out:
                for item in range(len(line)):
                    print(f"{line[item]}\t", end="")
                print()
        case _:
            c: int = 0
            for line in out:
                if c == limit:
                    break
                for item in range(len(line)):
                    print(f"{line[item]}\t", end="")
                print()
                c += 1


if __name__ == "__main__":
    main()
