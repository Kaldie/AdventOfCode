from io import TextIOWrapper





def is_input(line: str):
    return line.startswith("$")


def is_change_dir(line: str):
    return line.startswith("$ cd")


def get_dir_from_change_dir(line: str):
    return line.split(" ")[-1]


def starts_ls(line: str):
    return line.startswith("$ ls")


def handle_ls(handle: TextIOWrapper, current_path: list[str], dir_dict:dict):
    for line in handle.readline():
        if is_input(line):
            return dir_dict, line

        if line.startswith("dir"):
            continue

        size = line.split(" ")[0]
        current_dict = dir_dict
        for directory_name in current_path:
            if directory_name:
                current_dict=current_dict["children"].get(directory_name, {"size": 0, "children": {}})
            current_dict["size"] = current_dict["size"] + size

    raise ValueError("thois shouldt happen")

def handle_line(handle, line:str, current_dir:list[str], current_dict_dir:dict):
    if is_input(line): 
        
        if starts_ls(line):
            current_dict_dir, line = handle_ls(handle,current_dir, current_dict_dir)
        
        if is_change_dir(line):
            new_dir = get_dir_from_change_dir(line)
            if new_dir == "..":
                current_dir = current_dir[:-1]
            else:
                current_dir.append(get_dir_from_change_dir(line))


with open("input.txt") as handle:
    input = handle.readline()
    current_dir = []
    current_dict_dir={"size": 0, "children": {}}
    for line in input:
        handle_line(line, current_dir, current_dict_dir)

print(current_dir)
print(current_dict_dir)
