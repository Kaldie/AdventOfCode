def find_needle_with_default(line:str,needle:str,default=99999999999999999999):
    try:
        # check for do and donts
        nearest = line.index(needle)
        return nearest 
    except ValueError:
        return default

def solve(lines:list[str]):
    total = 0
    should_do=True
    for line in lines:
        current_index=0
        while True:
            try:
                mul_index = line[current_index:].index("mul(") + current_index
                close_brace_index = line[mul_index:].index(")") + mul_index
            except ValueError:
                break
            
            do_index = current_index
            while do_index <= mul_index:
                nearest_dont = find_needle_with_default(line[do_index:],"don't()")+do_index
                nearest_do = find_needle_with_default(line[do_index:],"do()")+do_index   
                
                closest_index = min(nearest_dont,nearest_do)
                
                if closest_index < mul_index:
                    if closest_index == nearest_dont:
                        should_do=False
                        do_index=closest_index+7
                    else:
                        should_do=True
                        do_index=closest_index+4
                else:
                    do_index=closest_index
          

            numbers_and_comma=line[mul_index+4:close_brace_index]
            numbers_and_comma=numbers_and_comma.split(",")
                
            if len(numbers_and_comma) == 2:
                try: 
                    if all( [str(int(x))==x for x in numbers_and_comma]): 
                        if should_do:
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

