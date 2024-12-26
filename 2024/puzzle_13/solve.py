from dataclasses import dataclass
import pathlib

def is_whole(f, eps=0.00001):
    return abs(f - round(f)) < abs(eps)

@dataclass
class Machine:
    X: int | None = None
    Y: int | None = None
    AX: int | None = None
    AY: int | None = None
    BX: int | None = None
    BY: int | None = None

def solve_machine(machine:Machine):
    
    a=(machine.Y-machine.BY/machine.BX*machine.X)/(machine.AY-machine.AX*machine.BY/machine.BX)
    b=(machine.X-a*machine.AX)/machine.BX

    if is_whole(a) and is_whole(b):
        return 3*a + b
    
    return 0




def yield_machine(lines: list[str]):
    machine = Machine()
    for line in lines:
        if len(line.strip()) == 0:
            yield machine
            machine = Machine()

        if "Button A:" in line:
            machine.AX, machine.AY = [
                int(part.split("+")[1])
                for part in line.strip().split(":")[1].strip().split(", ")
            ]

        if "Button B:" in line:
            machine.BX, machine.BY = [
                int(part.split("+")[1])
                for part in line.strip().split(":")[1].strip().split(", ")
            ]

        if "Prize:" in line:
            machine.X, machine.Y = [
                int(part.split("=")[1])
                for part in line.strip().split(":")[1].strip().split(", ")
            ]
    yield machine

def solve(lines: list[str]):
    """
    This are the equetions we need to do
    a=(Y-BY/BX*X)/(AY-AX*BY/BX)
    b=(X-a*AX)/BX
    """

    total = 0
    for x in yield_machine(lines):
        total+= solve_machine(x)

    return total


if __name__ == "__main__":
    with open(pathlib.Path(__file__).parent / "input.txt") as handle:
        lines = [line.strip() for line in handle.readlines()]
        print((solve(lines)))
