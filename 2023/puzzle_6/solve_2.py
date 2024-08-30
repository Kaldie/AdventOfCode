# distance = (gametime - starttime) * speed

# with open("input.txt") as handle:
#     lines = handle.readlines()
#     time = int(lines[0].split(":")[1].strip().replace(" ",""))
#     distance = int(lines[1].split(":")[1].strip().replace(" ",""))

# mul_way_to_beat = 1
# ways_to_beat = 0
# for start_time in range(time):
#     this_distance = (time - start_time) * start_time
#     if this_distance > distance:
#         ways_to_beat +=1
# mul_way_to_beat *= ways_to_beat 

# print(mul_way_to_beat)


"""
function is :
distance = (61677571 - x) * x
fill in some more

430103613071150 = (61677571 - x) * x
x^2 - 61677571x + 430103613071150 = 0
"""

import cmath
import math

# Coefficients
a = 1
b = -71530
c = 940200

# Calculate the discriminant
discriminant = cmath.sqrt(b**2 - 4*a*c)

# Calculate the two solutions
root1 = (-b + discriminant) / (2 * a)
root2 = (-b - discriminant) / (2 * a)

print("Root 1:", root1)
print("Root 2:", root2)

result = math.floor(root1.real) - math.ceil(root2.real)
print(result,math.floor(root1.real), math.ceil(root2.real))
print(53662612-8014959)