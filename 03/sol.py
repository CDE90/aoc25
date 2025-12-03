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
            left = nums[: len(nums) - (11 - i)]
            fm = max(left)
            fi = left.index(fm)
            right = nums[fi + 1 :]
            s += max(left) * (10 ** (12 - i - 1))
            nums = right

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
