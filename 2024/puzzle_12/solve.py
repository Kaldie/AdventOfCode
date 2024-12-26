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


def get_perimeter(positions: list[tuple[int, int]]):
    options = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    number_of_fences = 0
    for position in positions:
        for option in options:
            look_at = (position[0] + option[0], position[1] + option[1])
            if look_at not in positions:
                number_of_fences += 1
    return number_of_fences


def get_clusters(positions: list[tuple[int, int]]):
    options = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    clusters: list[set] = []

    while len(positions) > 0:
        seed = positions.pop()
        cluster = set([seed])
        new_elements=[seed]

        while len(new_elements)>0:
            new_elements=[]

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
            perimeter = get_perimeter(positions)
            print(element, area, perimeter, area * perimeter)
            total += area * perimeter
    
    return total


if __name__ == "__main__":
    with open(pathlib.Path(__file__).parent / "input.txt") as handle:
        lines = [line.strip() for line in handle.readlines()]
        print((solve(lines)))
