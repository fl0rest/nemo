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
    # mystring = '10.10.10.10 10.4.12.6 104.244.79.50 - 356605b0e2c430591ea21759f72bece0 [22/Feb/2024:12:52:09 +0000] "GET /wp-json/wp/v2/users/3 HTTP/1.1" 404 82 "https://jaysipenny.com/" "Mozilla/5.0 (iPhone; CPU iPhone OS 13_1_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.1 Mobile/15E148 Safari/604.1"'
