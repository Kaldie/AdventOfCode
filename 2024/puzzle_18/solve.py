import copy
import math
import pathlib


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


def get_score_increase(*args):
    return 1

def get_walls(lines:list[str],number_of_walls=1024):
    walls:set[tuple[int,int]] = set()
    for i in range(number_of_walls):
        walls.add(tuple([int(lines[i].split(",")[j]) for j in [1,0]]))
    return walls

def print_walls(walls, size=7):
    lines=[]
    for i in range(size):
        line=""
        for j in range(size):
            if (i,j) in walls:
                line += "#"
            else:
                line += "."
        lines.append(line)

    for line in lines:
        print(line)    

def solve(lines: list[str], steps=1024,size=7):

    walls = get_walls(lines,steps)
    print_walls(walls,71)

    dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    start = (0,0)
    finish=(size-1,size-1)
    print(finish)
    
    cur_min = math.inf
    front_locations = {start: 0}
    seen_locations = {start:0}
    i=0
    while True:
        i+=1
        new_front = {}
        for location, value in front_locations.items():
            for direction in dirs:
                next_step = (location[0] + direction[0], location[1] + direction[1])
                if next_step[0] < 0 or next_step[1] <0:
                    continue
                if next_step[0]>=size or next_step[1]>=size:
                    continue  

                if next_step == finish:
                    print("found solution: ", value + get_score_increase())
                    cur_min = min(
                        [cur_min, value + get_score_increase()]
                    )
                elif next_step not in walls:
                    new_score = value + get_score_increase()
                    
                    if next_step in seen_locations and seen_locations[next_step] < new_score:
                        continue
               
                    new_front[next_step] = new_score
                    
                    seen_locations[next_step] = new_score

        if len(new_front) == 0:
            break
        
        # if i >= 5:
        front_locations=copy.copy(new_front)
    print(i)

    return cur_min


if __name__ == "__main__":
    with open(pathlib.Path(__file__).parent / "input.txt") as handle:
        lines = [line.strip() for line in handle.readlines()]
        print((solve(lines,steps=1024,size=71)))
