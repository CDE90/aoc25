from collections import defaultdict


def p1(input: str, test: bool = False):
    lines = input.splitlines()

    coords = [tuple(map(int, line.split(","))) for line in lines]

    # Generate all pairs with squared Euclidean distance
    edges = []
    for i in range(len(coords)):
        for j in range(i + 1, len(coords)):
            d2 = (
                (coords[i][0] - coords[j][0]) ** 2
                + (coords[i][1] - coords[j][1]) ** 2
                + (coords[i][2] - coords[j][2]) ** 2
            )
            edges.append((d2, i, j))

    edges.sort(key=lambda x: x[0])

    # Select top N edges
    n_limit = 10 if test else 1000
    selected_edges = edges[:n_limit]

    # Union-Find
    parent = list(range(len(coords)))

    def find(i):
        if parent[i] != i:
            parent[i] = find(parent[i])
        return parent[i]

    def union(i, j):
        root_i = find(i)
        root_j = find(j)
        if root_i != root_j:
            parent[root_j] = root_i

    for _, i, j in selected_edges:
        union(i, j)

    groups_map = defaultdict(set)
    for i in range(len(coords)):
        groups_map[find(i)].add(i)
    groups = list(groups_map.values())

    groups.sort(key=len, reverse=True)
    group_sizes = [len(group) for group in groups]

    if len(group_sizes) >= 3:
        return group_sizes[0] * group_sizes[1] * group_sizes[2]
    return 0


def p2(input: str, test: bool = False):
    lines = input.splitlines()

    coords = [tuple(map(int, line.split(","))) for line in lines]

    # Generate all pairs with squared Euclidean distance
    edges = []
    for i in range(len(coords)):
        for j in range(i + 1, len(coords)):
            d2 = (
                (coords[i][0] - coords[j][0]) ** 2
                + (coords[i][1] - coords[j][1]) ** 2
                + (coords[i][2] - coords[j][2]) ** 2
            )
            edges.append((d2, i, j))

    # Sort by distance
    edges.sort(key=lambda x: x[0])

    # Union-Find
    parent = list(range(len(coords)))
    num_components = len(coords)

    def find(i):
        if parent[i] != i:
            parent[i] = find(parent[i])
        return parent[i]

    def union(i, j):
        root_i = find(i)
        root_j = find(j)
        if root_i != root_j:
            parent[root_j] = root_i
            return True
        return False

    for _, i, j in edges:
        if union(i, j):
            num_components -= 1
            if num_components == 1:
                # This is the last edge needed to connect everything
                return coords[i][0] * coords[j][0]

    return 0


def main():
    with open("08/inp.txt") as f:
        input = f.read()

    with open("08/test.txt") as f:
        test = f.read()

    print(f"Part 1 test: {p1(test, True)}")
    print(f"Part 2 test: {p2(test, True)}")

    print(f"Part 1: {p1(input)}")
    print(f"Part 2: {p2(input)}")


if __name__ == "__main__":
    main()
