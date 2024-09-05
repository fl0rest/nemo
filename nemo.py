from logparse import Logparse as lp


def countIP(filename):
    ips = []
    counted = []
    with open(filename) as log:
        for line in log:
            ips.append(lp.getIP(line))
    ips.sort(reverse=True)

    for ip in ips:
        times = ips.count(ip)
        counted.append((times, ip))
        ips = [ value for value in ips if value != ip]

    counted_s = sorted(counted, key=lambda x: x[0], reverse=True)

    print(counted_s[1])
    
    # c=0
    # for i in counted_s:
    #     print(counted_s[c])
    #     c += 1



def main():
    countIP("transfer.log")


if __name__ == "__main__":
    main()
    # mystring = '10.10.10.10 10.4.12.6 104.244.79.50 - 356605b0e2c430591ea21759f72bece0 [22/Feb/2024:12:52:09 +0000] "GET /wp-json/wp/v2/users/3 HTTP/1.1" 404 82 "https://jaysipenny.com/" "Mozilla/5.0 (iPhone; CPU iPhone OS 13_1_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.1 Mobile/15E148 Safari/604.1"'
