import pathlib
with open(pathlib.Path(__file__).parent / "input.txt") as handle:
    lines = handle.readlines()

safe_reports = 0

for line in lines:
    elements = line.split()
    differences = [int(j)-int(i) for i, j in zip(elements[:-1], elements[1:])] 
    all_same = all([difference>0 for difference in differences]) or all([difference<0 for difference in differences])
    
    if not all_same:
        continue

    differences = [abs(difference) for difference in differences]
    all_within_limit = all(difference < 4 for difference in differences)
    if not all_within_limit:
        continue

    safe_reports += 1

print(safe_reports)