import matplotlib.pyplot as plt


def area(p1, p2):
    return (abs(p1[0] - p2[0]) + 1) * (abs(p1[1] - p2[1]) + 1)


def p1(input: str):
    lines = input.splitlines()
    coords = [tuple(map(int, line.split(","))) for line in lines]

    areas = set()
    for i in range(len(coords)):
        for j in range(i + 1, len(coords)):
            # find the area of the rectangle defined by coords[i] and coords[j]
            areas.add(area(coords[i], coords[j]))

    return max(areas)


def is_point_inside(x, y, edges):
    # Ray casting algorithm
    intersections = 0
    for p1, p2 in edges:
        x1, y1 = p1
        x2, y2 = p2

        if (y1 > y) != (y2 > y):
            if x1 == x2:
                if x < x1:
                    intersections += 1

    return intersections % 2 == 1


def check_rect(p1, p2, edges):
    for e1, e2 in edges:
        if e1[0] < p2[0] and e2[0] > p1[0] and e1[1] < p2[1] and e2[1] > p1[1]:
            return False

    # check if the center of the rectangle is inside the shape
    cx = (p1[0] + p2[0]) // 2
    cy = (p1[1] + p2[1]) // 2

    if not is_point_inside(cx, cy, edges):
        return False

    return True


def p2(input: str):
    lines = input.splitlines()
    coords = [tuple(map(int, line.split(","))) for line in lines]
    n = len(coords)

    edges = []
    for i in range(n):
        p1 = coords[i]
        p2 = coords[(i + 1) % n]
        edges.append(
            (
                (min(p1[0], p2[0]), min(p1[1], p2[1])),
                (max(p1[0], p2[0]), max(p1[1], p2[1])),
            )
        )

    rects = []
    for i in range(n):
        for j in range(i + 1, n):
            p1 = coords[i]
            p2 = coords[j]
            rects.append(
                (
                    area(p1, p2),
                    (min(p1[0], p2[0]), min(p1[1], p2[1])),
                    (max(p1[0], p2[0]), max(p1[1], p2[1])),
                )
            )

    # Sort by area descending
    rects.sort(key=lambda x: x[0], reverse=True)

    for idx, (a, p1, p2) in enumerate(rects):
        if check_rect(p1, p2, edges):
            # visualise the largest rectangle found
            # visualise_rectangle(p1, p2, coords)
            return a
    return 0


def visualise_rectangle(p1, p2, coords):
    plt.figure()
    x, y = zip(*coords)
    plt.plot(x + (x[0],), y + (y[0],), "b-")  # Close the polygon

    # Draw rectangle
    rect_x = [p1[0], p2[0], p2[0], p1[0], p1[0]]
    rect_y = [p1[1], p1[1], p2[1], p2[1], p1[1]]
    plt.plot(rect_x, rect_y, "r--", label="Largest Rectangle")

    plt.scatter(x, y, color="red")

    plt.xlabel("X-axis")
    plt.ylabel("Y-axis")
    plt.title("Polygon with Largest Rectangle")
    plt.grid(True)
    plt.axis("equal")
    plt.legend()
    plt.show()


def visualise(input: str):
    lines = input.splitlines()
    coords = [tuple(map(int, line.split(","))) for line in lines]

    plt.figure()
    x, y = zip(*coords)
    plt.plot(x + (x[0],), y + (y[0],), "b-")  # Close the polygon

    plt.scatter(x, y, color="red")

    plt.xlabel("X-axis")
    plt.ylabel("Y-axis")
    plt.title("Polygon Visualization")
    plt.grid(True)
    plt.axis("equal")
    plt.show()


def main():
    with open("09/inp.txt") as f:
        input = f.read()

    with open("09/test.txt") as f:
        test = f.read()

    # visualise(test)
    # visualise(input)

    print(f"Part 1 test: {p1(test)}")
    print(f"Part 2 test: {p2(test)}")

    print(f"Part 1: {p1(input)}")
    print(f"Part 2: {p2(input)}")


if __name__ == "__main__":
    main()
