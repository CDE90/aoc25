def p1(input: str):
    lines = input.splitlines()

    s = 0
    for line in lines:
        nums = [int(x) for x in line]
        first = nums[:-1]
        fm = max(first)
        fi = first.index(fm)
        last = nums[fi + 1 :]
        s += fm * 10 + max(last)

    return s


def p2(input: str):
    lines = input.splitlines()

    s = 0

    for line in lines:
        nums = [int(x) for x in line]

        for i in range(12):
            r = 11 - i
            left = nums[: len(nums) - r]
            fm = max(left)
            fi = left.index(fm)
            s += fm * (10**r)
            nums = nums[fi + 1 :]

    return s


def main():
    with open("03/inp.txt") as f:
        input = f.read()

    with open("03/test.txt") as f:
        test = f.read()

    print(f"Part 1 test: {p1(test)}")
    print(f"Part 2 test: {p2(test)}")

    print(f"Part 1: {p1(input)}")
    print(f"Part 2: {p2(input)}")


if __name__ == "__main__":
    main()
