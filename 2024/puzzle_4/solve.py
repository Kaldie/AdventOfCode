def search_from_index(lines, needle, index: tuple[int, int]) -> list[tuple[int, int]]:
    if lines[index[0]][index[1]] != needle[0]:
        return 0

    search_rows = [-1, -1, -1, 1, 1, 1, 0, 0]
    search_columns = [-1, 0, 1, -1, 0, 1, -1, 1]
    search_tuples = [(i, j) for i, j in zip(search_rows, search_columns)]
    finds = 0
    print("here2", index)
    for i_dir, j_dir in search_tuples:
        search_index = 0
        i, j = index
        while True:
            # print("here",i,j,len(lines), len(lines[i]),f"'{lines[i]}'")
            if lines[i][j] != needle[search_index]:
                break

            search_index += 1
            if len(needle) <= search_index:
                finds += 1
                break

            i += i_dir
            j += j_dir

            if i < 0 or j < 0:
                break
            if i >= len(lines) or j >= len(lines[i]):
                break

    return finds


def solve(lines: list[str]):
    total = 0
    word = "XMAS"
    for i, line in enumerate(lines):
        for j in range(len(line)):
            total += search_from_index(lines, word, (i, j))
            print(search_from_index(lines, word, (i, j)), i, j)
    return total


if __name__ == "__main__":
    with open("input.txt", "r") as handle:
        lines = handle.readlines()

        print(solve(lines))
