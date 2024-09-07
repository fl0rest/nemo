from logparse_get import LogparseGet as lpg


class Logparse:

    @staticmethod
    def count_sort(input: list) -> list:
        counted: list = []
        for v in input:
            times: int = input.count(v)
            counted.append((times, v))
            input = [value for value in input if value != v]

        counted_s: list = sorted(counted, key=lambda x: x[0], reverse=True)
        counted_s = filter(lambda x: x[0] != 0, counted_s)

        return counted_s

    @staticmethod
    def count_single(filename: str, field: str) -> list:
        values: list = []
        try:
            with open(filename) as log:
                match field:
                    case "ip":
                        for line in log:
                            values.append(lpg.getIP(line))
                    case "ua":
                        for line in log:
                            values.append(lpg.getUA(line))
                    case "ref":
                        for line in log:
                            values.append(lpg.getRef(line))
                    case "code":
                        for line in log:
                            values.append(lpg.getHTTP(line))
                    case "size":
                        for line in log:
                            values.append(lpg.getSize(line))
        except FileNotFoundError:
            print("File not found")

        counted_s: list = Logparse.count_sort(values)

        # for i in counted_s:
        #     print(i[0], f"{i[1]}")

        return counted_s
