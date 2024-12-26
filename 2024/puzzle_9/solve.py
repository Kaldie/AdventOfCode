import pathlib

def get_number_of_mem_blocks(line):
    return (len(line)-1)/2

def solve(lines: list[str]):
    assert len(lines)==1
    line = lines[0]

    total = 0
    start_index=0
    mem_index=0
    end_index=len(line)-1 # current index at the end of the line
    remainder_to_write=0 #number of blocks still need to be written for the current index
    remainder_to_place=0 #number of blocks that can be written consectivly
    end_mem_value=get_number_of_mem_blocks(line)+1 #current value of the block
    start_mem_value=-1
    # curren
    while True:
        
        if remainder_to_place == 0:
            if start_index % 2==0: #we are in a block size
                # write all the mem from the left side
                start_mem_value+=1

                for _ in range(int(line[start_index])):
                    # print(f"{start_mem_value} * {mem_index}={start_mem_value*mem_index}")
                    total+=start_mem_value*mem_index
                    mem_index+=1
                # we done with this value, next
                start_index+=1
                continue

            else:
                remainder_to_place=int(line[start_index])
                start_index+=1

        for _ in range(remainder_to_place):
            if remainder_to_write<=0:
                remainder_to_write=int(line[end_index])
                end_index-=2
                end_mem_value-=1
            
                if end_index <= start_index:
                    break

            # print(f"{end_mem_value} * {mem_index}={end_mem_value*mem_index}")
            total+=end_mem_value*mem_index
            remainder_to_write-=1
            remainder_to_place-=1
            mem_index+=1



        if end_index <= start_index:
            # write the last bits
            # start_mem_value+=1
            # for _ in range(int(line[start_index])):
            #     print(f"start_index: {start_index}")
            #     print(f"{start_mem_value} * {mem_index}={start_mem_value*mem_index}")
            #     total+=start_mem_value*mem_index
            #     mem_index+=1
        
            for _ in range(remainder_to_write):
                print(f"end_index: {end_index}")
                print(f"{end_mem_value} * {mem_index}={end_mem_value*mem_index}")
                total+=end_mem_value*mem_index
                mem_index+=1

        
            break


        
    return total



if __name__ == "__main__":
    with open(pathlib.Path(__file__).parent / "input.txt") as handle:
        lines = handle.readlines()
        line = lines[0]
        current = 0
        length_tot=0
        while current <= len(line):
            length_tot+= int(line[current])
            current+=2
        print(length_tot)


        print((solve(lines)))
