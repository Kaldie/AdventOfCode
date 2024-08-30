input = ""
with open("input.txt") as handle:
    input = handle.read()

buffer_size = 14



def add_to_buffer(element: str, buffer):
    buffer += element
    if len(buffer) > buffer_size:
        buffer = buffer[1:buffer_size+1]
    return buffer


def buffer_is_all_unique(buffer):
    print(len(set(buffer)) )
    return len(set(buffer)) == buffer_size 

def solve():
    buffer = []
    for index, element in enumerate(input):
        buffer = add_to_buffer(element=element, buffer=buffer)
        print(buffer, len(buffer))
        if buffer_is_all_unique(buffer=buffer) and len(buffer) == buffer_size:
            return index + 1

print(solve())