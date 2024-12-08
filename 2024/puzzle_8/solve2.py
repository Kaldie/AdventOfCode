import copy
import pathlib

def find_nodes(i_loc,j_loc,height,width):
    nodes = [i_loc]
    node = copy.copy(i_loc)
    while True:
        a=node[0] + (i_loc[0] - j_loc[0])
        b=node[1] + (i_loc[1] - j_loc[1])
        node = (a,b)
        
        if in_range(node,height,width):
            nodes.append(node)
        else:
            break

    return nodes

def in_range(spot,height,widht):
    if any(x<0 for x in spot):
        return False
    
    if spot[0]>=height:
        return False

    if spot[1]>=widht:
        return False
    
    return True

def clean_lines(lines:list[str]):
    a = []
    for line in lines:
        a.append(line.strip())
    return a

def solve(lines: list[str]):
    lines = clean_lines(lines)
    height = len(lines)
    width = len(lines[0])

    spots = set()
    elements = get_elements(lines)

    for locations in elements.values():
        for i_loc in locations:
            for j_loc in locations:
                if i_loc == j_loc:
                    # Still needed otherwise BOOOM :P
                    # You know why :)
                    continue
                these_spots = find_nodes(i_loc,j_loc,height,width)
                for spot in these_spots:
                    spots.add(spot)

    return spots


def get_elements(lines):
    elements: dict[str, list[tuple[int, int]]] = dict()
    for line_index, line in enumerate(lines):
        for char_index, char in enumerate(line):
            if char == ".":
                continue
            locations = elements.get(char, [])
            locations.append((line_index, char_index))
            elements[char] = locations

    return elements


if __name__ == "__main__":
    with open(pathlib.Path(__file__).parent / "input.txt") as handle:
        lines = handle.readlines()
        print(len(solve(lines)))
