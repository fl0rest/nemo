from logparse_get import LogparseGet as lpg


class Data:
    totalSize: float = 0

    def __init__(self, raw: str):
        self.raw: str = raw
        self.ip: str = lpg.getIP(raw)
        self.ua: str = lpg.getUA(raw)
        self.code: int = lpg.getHTTP(raw)
        self.ref: str = lpg.getRef(raw)
        self.size: int = lpg.getSize(raw)
        self.method: str = lpg.getMethod(raw)
        self.url: str = lpg.getURL(raw)
        Data.totalSize += self.size

    def __str__(self):
        return f"\tIP: {self.ip}\n\
        UA: {self.ua}\n\
        Response Code: {self.code}\n\
        Referrer: {self.ref}\n\
        Size(b): {self.size}\n\
        REST Method: {self.method}\n\
        Requested URL: {self.url}"

    @staticmethod
    def populate(filename: str, search: str = None) -> list:
        try:
            with open(filename, "r") as log_raw:
                log: list = []
                if search != None:
                    for line in log_raw:
                        src = lpg.getSearch(search, line)
                        if type(src) != type(None):
                            log.append(src)
                        if len(log) == 0:
                            return f"No match for search: {search}"
                else:
                    log = log_raw.readlines()

                entry: list = []
                for line in log:
                    entry.append(Data(line))
                return entry

        except FileNotFoundError:
            return f"File {filename} was not found"

    @staticmethod
    def sort(list: list):
        list.sort(key=lambda data: data.ip)
        pass


class Logparse:
    """
    A class with functions for parsing log entries
    """

    totalSize: float = 0

    @staticmethod
    def count_sort(input: list) -> list:
        """
        Counts and sorts a list
        :param input: A unsorted and uncouinted list
        :type input: list
        :return: A counted and sorted list
        :rtype: list
        """
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
    def grab(filename: str, fields: list, search: str = None) -> list:
        """
            Grabs the specified field from all log entries in a file, counts and sorts them

            :param filename: name of the file
            :type filename: str
            :param fields: the field(s) to look for
            :type fields: list
            :param search: a pattern to RegEX for in the log entries
            :type search: str
            :return: A counted and sorted list
            :rtype: list
        """
        values: list = []
        try:
            log: list = []
            with open(filename) as log_raw:
                if search != None:
                    for line in log_raw:
                        src = lpg.getSearch(search, line)
                        if type(src) != type(None):
                            log.append(src)
                else:
                    log = log_raw

                values = []
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
    def totalSize(size: float) -> None:
        """
        :param size:
        :type size: float
        """
        Logparse.total += size
