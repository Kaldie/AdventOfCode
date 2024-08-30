# distance = (gametime - starttime) * speed

with open("input.txt") as handle:
    lines = handle.readlines()
    times = [int(x) for x in lines[0].split(":")[1].strip().split(" ")]
    distances = [int(x) for x in lines[1].split(":")[1].strip().split(" ")]

mul_way_to_beat = 1
for index, time in enumerate(times):
    ways_to_beat = 0
    for start_time in range(time):
        distance = (time - start_time) * start_time
        if distance > distances[index]:
            ways_to_beat +=1
    mul_way_to_beat *= ways_to_beat 

print(mul_way_to_beat)
