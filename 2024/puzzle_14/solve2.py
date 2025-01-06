from dataclasses import dataclass
import pathlib


@dataclass
class Machine:
    x: int | None = None
    y: int | None = None
    vx: int | None = None
    vy: int | None = None


def iterate_machine(machine: Machine, size: tuple[int, int]):
    
    # perform tick
    # move
    machine.x += machine.vx 
    machine.y += machine.vy

    # wrap
    machine.x = machine.x % size[0]
    machine.y = machine.y % size[1]
    return machine


def yield_machine(lines: list[str]):
    for line in lines:
        machine = Machine()
        p, v = line.strip().split(" ")
        machine.x, machine.y = [int(a) for a in p.split("=")[1].split(",")]
        machine.vx, machine.vy = [int(a) for a in v.split("=")[1].split(",")]
        yield machine

def print_machines(machines:list[Machine],size):
    positions = set([(machine.x,machine.y) for machine in machines])
    robots_in_row={}
    for position in positions:
        number = robots_in_row.get(position[1],0) + 1
        robots_in_row[position[1]]=number
    
    should_print=False
    for k,v in robots_in_row.items():
        if v >30:
            print(k,v)
            should_print=True
            break

    if should_print:
        for y in range(size[1]):
            line=""
            for x in range(size[0]):
                if (x,y) in positions:
                    line+="x"
                else:
                    line+="."
            print(line)
        input()


def solve(lines: list[str], size):
    """
    This are the equetions we need to do
    a=(Y-BY/BX*X)/(AY-AX*BY/BX)
    b=(X-a*AX)/BX
    """
    index=0
    machines = list(yield_machine(lines))
    while True:
        for machine in machines:
            iterate_machine(machine, size)
        
        
        print(index)
        print_machines(machines,size)
        index+=1
      



if __name__ == "__main__":
    SIZE = (101, 103)
    with open(pathlib.Path(__file__).parent / "input.txt") as handle:
        lines = [line.strip() for line in handle.readlines()]
        print((solve(lines, SIZE)))
