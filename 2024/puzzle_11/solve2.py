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


def iterate_stones(stones:list[tuple[str,int]]):
    new_stones=[]
    for value, iteration in stones:
        if len(value) > 1:
            new_stones.extend([(stone,0) for stone in handle_stone(value)])
        else:
            new_stones.append((value, iteration+1))
    return new_stones

@cache
def get_length_stone(origin_stone:tuple[str,int]):
    print(origin_stone)
    if origin_stone[1]==0:
        return 1
    
    total = 0
    # print(origin_stone)
    stones= [(origin_stone[0],0)]
    for _ in range(origin_stone[1]):
        stones = iterate_stones(stones)
    
    print(origin_stone, stones)
    for stone in stones:
        if stone[1]==0:
            total+=1
            print("xx", stone)
            continue

        iteration = stone[1] -1
        stone=handle_stone(stone[0])[0]
        # print("xx",(stone,iteration), get_length_stone((stone, iteration-1))) 
        total += get_length_stone((stone,iteration))

    return total


    
def solve(lines: list[str],number_of_blinks):
    assert len(lines)==1, f"number of lines: {len(lines)}"

    line = lines[0]
    stones = [(value,0) for value in line.strip().split(" ")]

    for i in range(number_of_blinks):
        print(f"blink: {i}")
        stones=iterate_stones(stones)
    
    total = 0
    for stone in stones:
        total += get_length_stone(stone)

    return total

if __name__ == "__main__":
    with open(pathlib.Path(__file__).parent / "input.txt") as handle:
        lines = handle.readlines()
        print((solve(lines,75)))
