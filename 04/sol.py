def p1(input: str):
    lines = input.splitlines()

    s = 0
    for i, line in enumerate(lines):
        for j, char in enumerate(line):
            if char != "@":
                continue

            # Check the 8 adjacent positions
            adjacent = [
                lines[i - 1][j - 1] if i > 0 and j > 0 else None,
                lines[i - 1][j] if i > 0 else None,
                lines[i - 1][j + 1] if i > 0 and j < len(line) - 1 else None,
                lines[i][j - 1] if j > 0 else None,
                lines[i][j + 1] if j < len(line) - 1 else None,
                lines[i + 1][j - 1] if i < len(lines) - 1 and j > 0 else None,
                lines[i + 1][j] if i < len(lines) - 1 else None,
                lines[i + 1][j + 1]
                if i < len(lines) - 1 and j < len(line) - 1
                else None,
            ]
            # Count the number of adjacent "@" characters
            count = sum(1 for c in adjacent if c == "@")

            if count < 4:
                s += 1

    return s


def p2(input: str):
    lines = input.splitlines()

    s = 0
    while True:
        to_change = []

        for i, line in enumerate(lines):
            for j, char in enumerate(line):
                if char != "@":
                    continue

                # Check the 8 adjacent positions
                adjacent = [
                    lines[i - 1][j - 1] if i > 0 and j > 0 else None,
                    lines[i - 1][j] if i > 0 else None,
                    lines[i - 1][j + 1] if i > 0 and j < len(line) - 1 else None,
                    lines[i][j - 1] if j > 0 else None,
                    lines[i][j + 1] if j < len(line) - 1 else None,
                    lines[i + 1][j - 1] if i < len(lines) - 1 and j > 0 else None,
                    lines[i + 1][j] if i < len(lines) - 1 else None,
                    lines[i + 1][j + 1]
                    if i < len(lines) - 1 and j < len(line) - 1
                    else None,
                ]
                # Count the number of adjacent "@" characters
                count = sum(1 for c in adjacent if c == "@")

                if count < 4:
                    to_change.append((i, j))

        if not to_change:
            break

        for i, j in to_change:
            lines[i] = lines[i][:j] + "#" + lines[i][j + 1 :]

        s += len(to_change)

    return s


def main():
    with open("04/inp.txt") as f:
        input = f.read()

    with open("04/test.txt") as f:
        test = f.read()

    print(f"Part 1 test: {p1(test)}")
    print(f"Part 2 test: {p2(test)}")

    print(f"Part 1: {p1(input)}")
    print(f"Part 2: {p2(input)}")


if __name__ == "__main__":
    main()
