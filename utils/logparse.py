from .logparse_get import LogparseGet as lpg


class DataRaw:
    """
    Object containing the key values for investigating traffic from apache logs
    """

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
        DataRaw.totalSize += self.size

    def __str__(self):
        return f"\tIP: {self.ip}\n\
        UA: {self.ua}\n\
        Response Code: {self.code}\n\
        Referrer: {self.ref}\n\
        Size(b): {self.size}\n\
        REST Method: {self.method}\n\
        Requested URL: {self.url}"

    def populate(filename: str, search: str = None) -> list:
        """
        Populates a list with DataRaw objects
        :param str filename: Name of the file to look from
        :param str search: A pattern to search for
        :raises: :class:`FileNotFoundError`: File not found
        :returns: A list of lines from `filename` containing `search` if specified
        :rtype: list
        """
        try:
            with open(filename, "r") as log_raw:
                log: list = []
                if search != None:
                    for line in log_raw:
                        src = lpg.getSearch(search, line)
                        if type(src) != type(None):
                            log.append(src)
                else:
                    log = log_raw.readlines()

            entry: list = []
            for line in log:
                entry.append(DataRaw(line))
            return entry

        except FileNotFoundError:
            return f"File {filename} was not found"

    @staticmethod
    def sort(list: list):
        """
        Method to sort a list of DataRaw objects based on IP
        :param list: A list of DataRaw objects
        :type list: list
        :returns: A sorted list of DataRaw objects
        :rtype: list
        """
        list.sort(key=lambda data: data.ip, reverse=True)
        pass
