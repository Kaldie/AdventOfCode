lines = []
with open("input.txt") as handle:
    lines = handle.readlines()

def solve_line(line:str):
    input, consecutives = line.split(" ")
    consecutives=[int(x) for x in consecutives.split(',')]

    number_of_groups=len(consecutives)

    known_splitted_groups = [a for a in input.split(".") if len(a) >0]

    # too many, kill some based on order of the numbers
    if len(known_splitted_groups) > number_of_groups:
        "no clue yet"
        raise ValueError()
    
    if len(known_splitted_groups) < number_of_groups:
        """
        we need to do at least part of the calculations on 2 
        consecutives
        """
        "no clue yet"

    if len(known_splitted_groups) == number_of_groups:
        for splitted_group, consecutive in zip(known_splitted_groups, consecutives):
            shabba = calculate_number_of_options(splitted_group, consecutive)          


def calculate_number_of_options(group_string:str, consecutive):
    if len(group_string) == consecutive:
        return 1

    if "#" not in group_string: 
        return 1 + (len(group_string) - consecutive)

    known_indexes = [index for index, c in enumerate(group_string) if c == "#"]
    
    return min()