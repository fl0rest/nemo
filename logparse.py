from logparse_get import LogparseGet as lpg


class Logparse:

    total: float = 0

    @staticmethod
    def count_sort(input: list) -> list:
        counted: list = []
        for item in input:
            times: int = input.count(item)
            if type(item) == list:
                counted.append((times, *item))
            else:
                counted.append((times, item))
            input = [value for value in input if value != item]

        counted_s: list = sorted(counted, key=lambda x: x[0], reverse=True)
        counted_s = list(filter(lambda x: x[0] != 0, counted_s))

        return counted_s

    @staticmethod
    def count(filename: str, fields: list, search: str = None) -> list:
        values: list = []
        some: int = 0
        try:
            with open(filename) as log_raw:
                log: list = []
                if search != None:
                    for line in log_raw:
                        src = lpg.getSearch(search, line)
                        if type(src) != type(None):
                            log.append(src)
                    if len(log) == 0:
                        print(f"No match for search: {search}")
                else:
                    log = log_raw

                for line in log:
                    temp: list = []
                    if "ip" in fields:
                        temp.append(lpg.getIP(line))
                    if "method" in fields:
                        temp.append(lpg.getMethod(line))
                    if "code" in fields:
                        temp.append(lpg.getHTTP(line))
                    if "url" in fields:
                        temp.append(lpg.getURL(line))
                    if "ua" in fields:
                        temp.append(lpg.getUA(line))
                    if "ref" in fields:
                        temp.append(lpg.getRef(line))
                    if "size" in fields:
                        temp.append(lpg.getSize(line))
                    if "totalSize" in fields:
                        Logparse.totalSize(lpg.getSize(line))
                    values.append(temp)
        except FileNotFoundError:
            print("File", filename, "not found")

        counted_s: list = Logparse.count_sort(values)
        return counted_s

    @staticmethod
    def totalSize(size:int) -> None:
        Logparse.total += size
