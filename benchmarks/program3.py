"""Benchmark Program 3 – Uso intensivo de saltos condicionales
Crea un bucle que se ejecuta 1000 veces usando BEQ/BNE para probar hazards de control.
"""
from cpu.instruction import Instruction

def build_program():
    program = []
    # R0 = 0, R1 = 1000
    program.append(Instruction("ADDI", "R0", None, "R2", 0))      # i = 0
    program.append(Instruction("ADDI", "R0", None, "R3", 1000))   # limit = 1000

    loop_label = 2  # posición del loop
    # loop:
    #   ADDI R2, R2, 1
    #   BNE  R2, R3, loop
    for _ in range(1000):
        program.append(Instruction("ADDI", "R2", None, "R2", 1))
        program.append(Instruction("BNE", "R2", "R3", None, loop_label))
    return program

if __name__ == "__main__":
    from run_pipeline import run_program
    stats = run_program(build_program())
    print(stats)
