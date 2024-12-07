import pathlib
with open(pathlib.Path(__file__).parent / "input.txt") as handle:
    lines = handle.readlines()

list_1=[]
list_2=[]
for line in lines:
    a,b = line.split("  ")
    list_1.append(int(a))
    list_2.append(int(b))

list_1=sorted(list_1)
list_2=sorted(list_2)

distance=0
for a,b in zip(list_1, list_2):
    
    distance+= abs(a-b)

print(distance)