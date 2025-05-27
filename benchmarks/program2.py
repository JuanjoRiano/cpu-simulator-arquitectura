"""Benchmark Program 2 – Accesos masivos a memoria
Realiza cargas y almacenes para medir la caché.
"""
from cpu.instruction import Instruction

def build_program():
    program = []
    base_addr = 0x1000
    for i in range(1000):
        addr = base_addr + i*4
        # LW R1, [addr]
        program.append(Instruction("LW", None, None, "R1", addr))
        # SW R1, [addr+4096] para ensuciar líneas
        program.append(Instruction("SW", "R1", None, None, addr + 0x1000))
    return program

if __name__ == "__main__":
    from run_pipeline import run_program
    stats = run_program(build_program())
    print(stats)
