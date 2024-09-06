from logparse_get import LogparseGet as lpg


class Logparse:

    @staticmethod
    def count_single(filename, field):
        values = []
        counted = []
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
                    

        values.sort(reverse=True)

        for v in values:
            times = values.count(v)
            counted.append((times, v))
            values = [value for value in values if value != v]

        counted_s = sorted(counted, key=lambda x: x[0], reverse=True)
        counted_s = filter(lambda x: x[0] != 0, counted_s)

        for i in counted_s:
            print(i[0], f"{i[1]}")
