def p1(input: str):
    _ranges, _ids = input.split("\n\n")
    ranges = _ranges.splitlines()
    ids = _ids.splitlines()

    count = 0
    for id in ids:
        id_int = int(id)
        for r in ranges:
            start, end = map(int, r.split("-"))
            if start <= id_int <= end:
                count += 1
                break
    return count


def p2(input: str):
    _ranges, _ = input.split("\n\n")
    ranges = _ranges.splitlines()

    # merge intervals
    intervals = []
    for r in ranges:
        start, end = map(int, r.split("-"))
        intervals.append((start, end))
    intervals.sort()

    merged = []
    for start, end in intervals:
        if not merged or merged[-1][1] < start:
            merged.append((start, end))
        else:
            merged[-1] = (merged[-1][0], max(merged[-1][1], end))

    count = 0
    for start, end in merged:
        count += end - start + 1
    return count


def main():
    with open("05/inp.txt") as f:
        input = f.read()

    with open("05/test.txt") as f:
        test = f.read()

    print(f"Part 1 test: {p1(test)}")
    print(f"Part 2 test: {p2(test)}")

    print(f"Part 1: {p1(input)}")
    print(f"Part 2: {p2(input)}")


if __name__ == "__main__":
    main()
