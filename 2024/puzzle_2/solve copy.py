import copy
import pathlib
with open(pathlib.Path(__file__).parent / "input.txt") as handle:
    lines = handle.readlines()

def check_line(elements):
    differences = [j-i for i, j in zip(elements[:-1], elements[1:])] 
    all_same = all([difference>0 for difference in differences]) or all([difference<0 for difference in differences])
    
    if not all_same:
        return False

    differences = [abs(difference) for difference in differences]
    all_within_limit = all(difference < 4 for difference in differences)
    if not all_within_limit:
        return False

    return True


safe_reports = 0

for line in lines:
    elements = [int(a) for a in line.split()]
    if check_line(elements):
      safe_reports+=1
      continue  
    for i in range(len(elements)):        
        new_elements = copy.deepcopy(elements)
        new_elements.pop(i)
        if check_line(new_elements):
            safe_reports+=1
            break

print(safe_reports)