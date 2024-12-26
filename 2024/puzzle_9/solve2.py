import pathlib


def get_number_of_mem_blocks(line):
    return (len(line) - 1) / 2


def process_line(line: str) -> dict[int, list[int]]:
    free_space_list = []
    file_lists = []
    current_position = 0
    for i in range(len(line)):
        value = int(line[i])
        if i % 2 != 0:
            free_space_list.append([current_position, value])
        else:
            file_lists.append([current_position, value, int(i / 2)])
        current_position += value
    return free_space_list, file_lists


def solve(lines: list[str]):
    assert len(lines) == 1
    line = lines[0]

    # create list of free spots with index, size as values
    # ordered from left to right
    free_space_list, file_list = process_line(line)

    processed_files = []
    for file_entry in file_list[::-1]:
        has_placed=False
        for free_space in free_space_list:
            # no space found
            if file_entry[0] <= free_space[0]:
                break
            # Found a spot where the file fits
            if file_entry[1] <= free_space[1]:
                has_placed=True
                # update the index of the file entry
                file_entry[0] = free_space[0]
                processed_files.append(file_entry)

                # reduce the free space by file size
                free_space[1] -= file_entry[1]
                # move the index to the right by file size
                free_space[0] += file_entry[1]
                break  # out of this loop

        if not has_placed:
            processed_files.append(file_entry)

    total = 0
    for processed_file in processed_files:
        for i in range(processed_file[0], processed_file[0] + processed_file[1]):
            total += i * processed_file[2]

    return total


if __name__ == "__main__":
    with open(pathlib.Path(__file__).parent / "input.txt") as handle:
        lines = handle.readlines()
        line = lines[0]
        current = 0
        length_tot = 0
        while current <= len(line):
            length_tot += int(line[current])
            current += 2
        print(length_tot)

        print((solve(lines)))
