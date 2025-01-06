
import pathlib

def find_walls(lines:list[str]):
    return find_chars(lines,"#")

def find_boxes(lines:list[str]):
    return find_chars(lines,"O")

def find_robot(lines:list[str]):
    robots = find_chars(lines,"@")
    assert len(robots)==1
    return robots[0]

def find_chars(lines:list[str],char:str):
    elements:list[tuple[int,int]]=[]
    for i,line in enumerate(lines):
        for j,v in enumerate(line):
            if v == char:
                elements.append((i,j))

    return elements

def print_state(robot, boxes,walls):
    max_cor=max([wall[0] for wall in walls]),max([wall[1] for wall in walls])

    for i in range(max_cor[0]+1):
        line=""
        for j in range(max_cor[0]+1):
            if (i,j)==robot:
                line+="@"
            elif (i,j) in walls:
                line+="#"
            elif (i,j) in boxes:
                line+="O"
            else:
                line+="."
        print(line)
    print()

def move_robot(char:str,robot:tuple[int,int],boxes:list[tuple[int,int]],walls:list[tuple[int,int]]):
    if char == "^":
        dir=[-1,0]
    if char == ">":
        dir=[0,1]
    if char == "v":
        dir=[1,0]
    if char == "<":
        dir=[0,-1]
    
    position_to_check = robot
    boxes_to_move=[]
    run_into_wall=False

    while True:
        # untill we find a wall or an open spot
        position_to_check=(position_to_check[0] + dir[0], position_to_check[1] + dir[1])

        if position_to_check in walls:
            run_into_wall=True
            break
        elif position_to_check in boxes:
            boxes_to_move.append(boxes.index(position_to_check))
        else:
            break

    if not run_into_wall:
        robot=(robot[0] + dir[0], robot[1] + dir[1])
        for box_index in boxes_to_move:
            box = boxes[box_index]
            boxes[box_index]=(box[0] + dir[0], box[1] + dir[1])
    
    return robot
        

def solve(lines: list[str]):
    for index,line in enumerate(lines):
        if len(line.strip())==0:
            split=index   
            break

    walls = find_walls(lines[:split])
    boxes=find_boxes(lines[:split])
    robot = find_robot(lines[:split])

    for line in lines[split:]:
        for char in line:
            robot=move_robot(char,robot,boxes,walls)
            # print_state(robot,boxes,walls)

    total=0
    for box in boxes:
        total+= 100 * box[0] + box[1]

    return total


if __name__ == "__main__":
    with open(pathlib.Path(__file__).parent / "input.txt") as handle:
        lines = [line.strip() for line in handle.readlines()]
        print((solve(lines)))
