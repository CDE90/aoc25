inp = [x.split("-") for x in open("02/inp.txt").read().strip().split(",")]


def isinvalid(num: int) -> bool:
    s = str(num)
    first, second = s[: len(s) // 2], s[len(s) // 2 :]
    return first == second


c = 0

for start, end in inp:
    for num in range(int(start), int(end) + 1):
        # c += not isvalid(num)
        if isinvalid(num):
            c += num

print(c)


def isinvalid2(num: int) -> bool:
    # now the repeated part can be repeated any number of times
    s = str(num)

    for partlen in range(1, len(s) // 2 + 1):
        # split s into parts of length partlen
        parts = [s[i : i + partlen] for i in range(0, len(s), partlen)]
        # check if all parts are the same
        if all(part == parts[0] for part in parts):
            return True
    return False


c2 = 0

for start, end in inp:
    for num in range(int(start), int(end) + 1):
        if isinvalid2(num):
            c2 += num

print(c2)
