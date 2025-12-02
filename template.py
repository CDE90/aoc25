def p1(input: str):
    return


def p2(input: str):
    return


def main():
    with open("{{day}}/inp.txt") as f:
        input = f.read()

    with open("{{day}}/test.txt") as f:
        test = f.read()

    print(f"Part 1 test: {p1(test)}")
    print(f"Part 2 test: {p2(test)}")

    print(f"Part 1: {p1(input)}")
    print(f"Part 2: {p2(input)}")


if __name__ == "__main__":
    main()
