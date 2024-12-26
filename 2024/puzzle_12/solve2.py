import math
import pathlib


def get_elements(lines: list[str]):
    elements = set()
    for line in lines:
        for char in line:
            elements.add(char)
    return elements


def find_element(lines: list[str], element: str):
    positions = []
    for i, line in enumerate(lines):
        index = -1
        while True:
            try:
                index = line[index + 1 :].index(element) + index + 1
                positions.append((i, index))
            except:
                break
    return positions


def get_perimeter_vertical(positions: list[tuple[int, int]]):
    min_position = (min([p[0] for p in positions]) - 1, min([p[1] for p in positions]))
    max_position = (max([p[0] for p in positions]) + 1, max([p[1] for p in positions]))
    
    sides = list()
    print("min_pos", min_position, "max_pos", max_position)
    for j in range(min_position[1], max_position[1] + 1, 1):
        for i in range(min_position[0], max_position[0] + 1, 1):
            prev = (i-1,j) in positions
            current = (i,j) in positions
            if prev != current:
                if prev != ((i-1,j-1) in positions) or current != ((i,j-1) in positions):
                    sides.append((i,j))
    print(sides)
    return len(sides)


def get_perimeter_horizontal(positions: list[tuple[int, int]]):
    min_position = (min([p[0] for p in positions]), min([p[1] for p in positions])-1)
    max_position = (max([p[0] for p in positions]), max([p[1] for p in positions])+1)
    positions = set(positions)

    sides = list()

    for i in range(min_position[0], max_position[0] + 1, 1):
        for j in range(min_position[1], max_position[1] + 1, 1):
            prev = (i,j-1) in positions
            current = (i,j) in positions
            if prev != current:
                if prev != ((i-1,j-1) in positions) or current != ((i-1,j) in positions):
                    sides.append((i,j))
    print("horizontal sides: ", sides)
    return len(sides)


def get_number_of_sides(positions: list[tuple[int, int]]):
    return get_perimeter_horizontal(positions=positions) + get_perimeter_vertical(
        positions=positions
    )


def get_clusters(positions: list[tuple[int, int]]):
    options = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    clusters: list[set] = []

    while len(positions) > 0:
        seed = positions.pop()
        cluster = set([seed])
        new_elements = [seed]

        while len(new_elements) > 0:
            new_elements = []

            for element in cluster:
                for option in options:
                    look_at = (element[0] + option[0], element[1] + option[1])
                    if look_at in positions:
                        new_elements.append(look_at)
                        positions.pop(positions.index(look_at))

            [cluster.add(new_position) for new_position in new_elements]

        clusters.append(cluster)

    return clusters


def solve(lines: list[str]):
    elements = get_elements(lines)
    total = 0
    for element in elements:
        positions = find_element(lines, element)
        clusters = get_clusters(positions)

        for positions in clusters:
            area = len(positions)
            perimeter = get_number_of_sides(positions)
            print(element, area, "sides", perimeter, area * perimeter)
            total += area * perimeter

    return total


if __name__ == "__main__":
    with open(pathlib.Path(__file__).parent / "input.txt") as handle:
        lines = [line.strip() for line in handle.readlines()]
        print((solve(lines)))
