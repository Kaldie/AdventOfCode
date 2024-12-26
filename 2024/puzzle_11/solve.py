from functools import cache
import pathlib

@cache
def handle_stone(value:str):
    if int(value)==0:
        return ["1"]
    elif len(value) % 2==0:
        split_index = int(len(value) / 2)
        return [str(int(value[:split_index])), str(int(value[split_index:]))]
    else:
        return [str(int(value) * 2024)]
    
def solve(lines: list[str],number_of_blinks):
    assert len(lines)==1, f"number of lines: {len(lines)}"

    line = lines[0]
    stones = line.strip().split(" ")

    for i in range(number_of_blinks):
        new_stones = []
        for stone in stones:
            new_stones.extend(handle_stone(stone))
        stones = new_stones
    return len(stones)

if __name__ == "__main__":
    with open(pathlib.Path(__file__).parent / "input.txt") as handle:
        lines = handle.readlines()
        print((solve(lines,25)))
