from collections import defaultdict


def debug(lines: list[str], beams: set[tuple[int, int]]):
    output = []
    for y in range(len(lines)):
        row = []
        for x in range(len(lines[0])):
            if (x, y) in beams:
                row.append("|")
            else:
                row.append(lines[y][x])
        output.append("".join(row))

    print("\n".join(output))
    print()


def p1(input: str):
    lines = input.splitlines()

    # Find the index of "S" in the first line
    start = lines[0].index("S")

    # beams: set[tuple[int, int]] = {(start, 1)}
    beams: set[tuple[int, int]] = set()
    queue: list[tuple[int, int]] = [(start, 1)]

    splits = 0

    while queue:
        x, y = queue.pop(0)
        if (x, y) in beams:
            continue

        beams.add((x, y))
        if y + 1 >= len(lines):
            continue

        # always look down
        if lines[y + 1][x] == "^":
            # add the positions on either side to the queue
            queue.append((x - 1, y + 1))
            queue.append((x + 1, y + 1))
            splits += 1
        elif lines[y + 1][x] == ".":  # continue down
            queue.append((x, y + 1))

        # debug(lines, beams)

    # output a visualization of the beams
    # debug(lines, beams)

    return splits


def p2(input: str):
    lines = input.splitlines()

    start = lines[0].index("S")

    beams: dict[tuple[int, int], int] = defaultdict(int)
    beams[(start, 1)] = 1
    active_xs: set[int] = {start}

    t = 0

    for y in range(1, len(lines)):
        next_active_xs = set()

        for x in active_xs:
            count = beams[(x, y)]
            if y + 1 >= len(lines):
                t += count
                continue

            next_positions = []

            if lines[y + 1][x] == "^":
                next_positions.append(x - 1)
                next_positions.append(x + 1)
            elif lines[y + 1][x] == ".":
                next_positions.append(x)

            for next_x in next_positions:
                beams[(next_x, y + 1)] += count
                next_active_xs.add(next_x)

        active_xs = next_active_xs

    return t


def main():
    with open("07/inp.txt") as f:
        input = f.read()

    with open("07/test.txt") as f:
        test = f.read()

    print(f"Part 1 test: {p1(test)}")
    print(f"Part 2 test: {p2(test)}")

    print(f"Part 1: {p1(input)}")
    print(f"Part 2: {p2(input)}")


if __name__ == "__main__":
    main()
