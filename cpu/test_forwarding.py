import pytest
from instruction import Instruction
from pipeline import load_instructions, run_cycle, registers, reset

def test_forwarding_add_sequence():
    reset()
    registers[1] = 10
    registers[2] = 20

    instructions = [
        Instruction('ADD', rs=1, rt=2, rd=3),
        Instruction('SUB', rs=3, rt=2, rd=4)
    ]

    load_instructions(instructions)
    for _ in range(8):
        run_cycle()

    assert registers[4] == 10, "Error en forwarding: R4 debería ser 10"
