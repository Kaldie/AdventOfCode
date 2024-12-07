

def solve(lines:list[str]):
    total = 0
    for line in lines:
        current_index=0
        while True:
            try:
                mul_index = line[current_index:].index("mul(") + current_index
                close_brace_index = line[mul_index:].index(")") + mul_index
            except ValueError:
                break

            numbers_and_comma=line[mul_index+4:close_brace_index]
            numbers_and_comma=numbers_and_comma.split(",")
                
            if len(numbers_and_comma) == 2:
                try: 
                    if all( [str(int(x))==x for x in numbers_and_comma]): 
                        print(int(numbers_and_comma[0]), int(numbers_and_comma[1]))
                        total += int(numbers_and_comma[0]) * int(numbers_and_comma[1])
                    current_index=close_brace_index+1
                except ValueError:
                    current_index=mul_index+4
                    continue
            else:
                current_index=mul_index+4

    return total

if __name__ == "__main__":
    with open("input.txt",'r') as handle:
        lines = handle.readlines()

        print(solve(lines))

