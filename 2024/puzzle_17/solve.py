from dataclasses import dataclass, field
import math

import pathlib


@dataclass
class Machine:
    regA: int
    regB: int
    regC: int
    instruction_pointer: int
    program: list[int] = field(default_factory=list)
    output: list[int] = field(default_factory=list)
    program: list[int] = field(default_factory=list)


def div(nom, dennom):
    return nom >> dennom


def get_combo_opperand(machine: Machine, operand: int):
    if operand < 4:
        return operand
    if operand == 4:
        return machine.regA
    if operand == 5:
        return machine.regB
    if operand == 6:
        return machine.regC
    raise ValueError


def adv(machine: Machine, operand):
    machine.regA = div(machine.regA, get_combo_opperand(machine,operand))


def bdv(machine: Machine, operand):
    machine.regB = div(machine.regA, get_combo_opperand(machine,operand))


def cdv(machine: Machine, operand):
    machine.regC = div(machine.regA, get_combo_opperand(machine,operand))


def bxl(machine: Machine, operand):
    machine.regB = machine.regB ^ operand


def bst(machine: Machine, operand):
    machine.regB = get_combo_opperand(machine,operand) % 8


def jnz(machine: Machine, operand):
    if machine.regA == 0:
        return
    machine.instruction_pointer = operand


def bxc(machine: Machine, _):
    machine.regB = machine.regB ^ machine.regC


def out(machine: Machine, operand):
    print("out", get_combo_opperand(machine,operand) % 8)
    machine.output.append(get_combo_opperand(machine,operand) % 8)


def get_func_from_opcode(opcode: int):
    opcodes = [adv, bxl, bst, jnz, bxc, out, bdv, cdv]
    return opcodes[opcode]


def get_machine_from_lines(lines):
    machine = Machine(0, 0, 0, 0)
    for line in lines:
        if "Program" in line:
            machine.program = line.strip().split(": ")[1].split(",")
        elif " A" in line:
            machine.regA = int(line.strip().split(": ")[1])
        elif " B" in line:
            machine.regB = int(line.strip().split(": ")[1])
        elif " C" in line:
            machine.regC = int(line.strip().split(": ")[1])
    return machine


def solve(lines: list[str]):
    machine = get_machine_from_lines(lines)
    machine = _solve(machine)
    return ",".join([str(x) for x in machine.output])

def _solve(machine:Machine):
    while machine.instruction_pointer < len(machine.program):
        opcode = int(machine.program[machine.instruction_pointer])
        operand = int(machine.program[machine.instruction_pointer + 1])
        func = get_func_from_opcode(opcode)
        func(machine, operand)
        if func != jnz or machine.regA==0:
            machine.instruction_pointer+=2

    return machine


if __name__ == "__main__":
    with open(pathlib.Path(__file__).parent / "input.txt") as handle:
        lines = [line.strip() for line in handle.readlines()]
        print((solve(lines)))
