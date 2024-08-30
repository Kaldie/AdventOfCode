import string

number_dict = {"one": 1,
"two": 2,
"three":3, 
"four": 4,
"five": 5,
"six": 6,
"seven":7, 
"eight": 8,
"nine": 9}

def get_first_number(text:str, should_reverse:bool=False):
    seen = ""
    if should_reverse:
        text = text[::-1]

    for element in text:
        if element in string.digits:
            return int(element)
        seen += element

        for key in number_dict.keys():
            if key in seen and (should_reverse is False):
                return number_dict[key]
            if key in seen[::-1] and should_reverse:
                return number_dict[key]
            
    raise ValueError("Could not find number")


input = None
with open("input.txt",'r') as handle:
    input = handle.readlines()

total = 0
for line in input:
    total += get_first_number(line) * 10
    total += get_first_number(line,should_reverse=True)

print(total)