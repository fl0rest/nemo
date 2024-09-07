from logparse import Logparse as lp
import argparse


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("field", help="Field to parse [ip|ua|ref|code|size]",\
                        choices=['ip','ua','ref','code','size'], nargs='+')
    parser.add_argument("-f", "--file", help="path to file, default ./access.log")
    parser.parse_args()
    args = parser.parse_args()

    file = "access.log"
    if args.file:
        file = args.file

    if len(args.field) == 1:
        out: list = lp.count_single(file, args.field[0])
    else:
        out: list = lp.count_more(file, args.field)

    for i in out:
        print(i[0], f"\t{i[1]}")

if __name__ == "__main__":
    main()
    # mystring = '10.10.10.10 10.4.12.6 104.244.79.50 - 356605b0e2c430591ea21759f72bece0 [22/Feb/2024:12:52:09 +0000] "GET /wp-json/wp/v2/users/3 HTTP/1.1" 404 82 "https://jaysipenny.com/" "Mozilla/5.0 (iPhone; CPU iPhone OS 13_1_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.1 Mobile/15E148 Safari/604.1"'
