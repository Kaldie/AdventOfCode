import pathlib


def find_heads(lines: list[str]):
    heads = []
    for i, line in enumerate(lines):
        index = -1
        while True:
            try:
                index = line[index + 1 :].index("0") + index + 1
                heads.append((i, index))
            except:
                break
    return heads


def find_nexts(lines: list[str], pos: tuple[int, int], cur_val: str):
    nexts = []
    options = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    needle = str(int(cur_val) + 1)

    for option in options:
        look_at = (pos[0] + option[0], pos[1] + option[1])

        if look_at[0] < 0 or look_at[1] < 0:
            continue

        if (len(lines) <= look_at[0]) or (len(lines[look_at[0]]) <= look_at[1]):
            continue

        if lines[look_at[0]][look_at[1]] == needle:
            nexts.append(look_at)
            # print("find_nexts", look_at, lines[look_at[0]][look_at[1]], needle, nexts)
    return nexts, needle


def find_ends_for_pos(lines, pos: tuple[int, int]):
    cur_val = "0"
    nexts = [pos]
    finds = 0
    found_nines=set()
    while len(nexts) > 0:
        next_nexts = []
        for next in nexts:
            # print("find_ends", cur_val, next)
            these_nexts, next_val = find_nexts(lines, pos=next, cur_val=cur_val)
            print(cur_val)
            if int(next_val) < 9:
                next_nexts.extend(these_nexts)
            else:
                print("add to total:", len(these_nexts), these_nexts, nexts)
                for nine in these_nexts:
                    found_nines.add(nine)

        nexts = next_nexts
        cur_val=next_val
        # print("after loop nexts:", nexts)

    return len(found_nines)


def solve(lines: list[str]):
    total = 0
    print("asd")
    for head in find_heads(lines=lines):
        total += find_ends_for_pos(lines, head)
    return total


if __name__ == "__main__":
    with open(pathlib.Path(__file__).parent / "input.txt") as handle:
        lines = handle.readlines()
        print((solve(lines)))
