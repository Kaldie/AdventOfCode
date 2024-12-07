def search_from_index(lines, needle, index: tuple[int, int]) -> list[tuple[int, int]]:
    if lines[index[0]][index[1]] != needle[0]:
        return []

    search_rows = [
        -1,
        -1,
        1,
        1,
    ]
    search_columns = [-1, 1, -1, 1]
    search_tuples = [(i, j) for i, j in zip(search_rows, search_columns)]
    finds = []

    for i_dir, j_dir in search_tuples:
        search_index = 0
        i, j = index
        while True:
            if lines[i][j] != needle[search_index]:
                break

            search_index += 1
            if len(needle) <= search_index:
                finds.append((index, (i, j)))
                break

            i += i_dir
            j += j_dir

            if i < 0 or j < 0:
                break
            if i >= len(lines) or j >= len(lines[i]):
                break

    return finds


def solve(lines: list[str]):
    finds = []
    word = "MAS"
    total = 0
    for i, line in enumerate(lines):
        for j in range(len(line)):
            finds.extend(search_from_index(lines, word, (i, j)))

    sorted_finds = []
    for find in finds:
        sorted_finds.append(
            (
                (min([x[0] for x in find]), min([x[1] for x in find])),
                (max([x[0] for x in find]), max([x[1] for x in find])),
            )
        )

    
    for find in sorted_finds:
        print(find, finds.count(find))
        if sorted_finds.count(find) > 1:
            total += 0.5

    return total


if __name__ == "__main__":
    with open("input.txt", "r") as handle:
        lines = handle.readlines()

        print(solve(lines))
