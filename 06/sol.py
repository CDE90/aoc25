import itertools

import numpy as np

F = {"+": sum, "*": np.prod}


def get_chunks(input: str):
    return [
        ["".join(chars) for chars in zip(*group)]
        for is_sep, group in itertools.groupby(
            zip(*input.splitlines()), lambda c: all(char == " " for char in c)
        )
        if not is_sep
    ]


def p1(input: str):
    return sum(
        F[chunk[-1].strip()]([int(line.strip()) for line in chunk[:-1]])
        for chunk in get_chunks(input)
    )


def p2(input: str):
    return sum(
        F[chunk[-1].strip()]([int("".join(col).strip()) for col in zip(*chunk[:-1])])
        for chunk in get_chunks(input)
    )


def main():
    with open("06/inp.txt") as f:
        input = f.read()

    with open("06/test.txt") as f:
        test = f.read()

    print(f"Part 1 test: {p1(test)}")
    print(f"Part 2 test: {p2(test)}")

    print(f"Part 1: {p1(input)}")
    print(f"Part 2: {p2(input)}")


if __name__ == "__main__":
    main()
