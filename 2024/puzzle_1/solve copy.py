import pathlib
with open(pathlib.Path(__file__).parent / "input.txt") as handle:
    lines = handle.readlines()

list_1=[]
list_2={}
for line in lines:
    a,b = line.split("  ")
    b=int(b)
    list_1.append(int(a))
    number = list_2.get(b,0)
    list_2[b] = number+1
    
distance=0
for a in list_1:
    distance += a * list_2.get(a,0)
print(distance)