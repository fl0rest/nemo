import re


class LogparseGet:

    @staticmethod
    def getIP(input: str) -> str:
        addrs = input.split("-")[0].strip()
        addrs = addrs.split()
        try:
            if len(addrs) > 1:
                origin = len(addrs) - 1
                return f"{addrs[origin]}-X"
            else:
                return addrs[0]
        except IndexError:
            return "There is no IP"

    @staticmethod
    def getUA(input: str) -> str:
        rev = input[::-1].strip()
        ua = rev.split('"')[1][::-1]
        return ua

    @staticmethod
    def getHTTP(input: str) -> str:
        code = input.split('"')[2].strip()
        code = code.split()[0]
        return int(code)

    @staticmethod
    def getRef(input: str) -> str:
        rev = input[::-1].strip()
        ref = rev.split('"')[3][::-1]
        return ref

    @staticmethod
    def getSize(input: str) -> int:
        size = input.split('"')[2].strip()
        size = size.split()[1]
        if size == "-":
            return int(0)
        else:
            return int(size)

    @staticmethod
    def getURL(input: str) -> str:
        url = input.split('"')[1].strip()
        url = url.split(" ")[1]
        return url

    @staticmethod
    def getMethod(input: str) -> str:
        method = input.split('"')[1]
        method = method.split(" ")[0]
        return method

    @staticmethod
    def getSearch(search: str, line: str) -> str:
        search_r = re.compile(search)
        if type(re.search(search_r, line)) != type(None):
            return line
