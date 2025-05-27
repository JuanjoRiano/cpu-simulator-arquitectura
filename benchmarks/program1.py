"""Benchmark Program 1 – Aritmética intensiva
Este script genera 1000 instrucciones de suma y resta para estresar la ALU.
"""
from cpu.instruction import Instruction

def build_program():
    program = []
    # 500 ADD y 500 SUB intercaladas
    for i in range(500):
        program.append(Instruction("ADD", f"R{i%8}", f"R{(i+1)%8}", f"R{(i+2)%8}", 0))
        program.append(Instruction("SUB", f"R{i%8}", f"R{(i+1)%8}", f"R{(i+3)%8}", 0))
    return program

if __name__ == "__main__":
    from run_pipeline import run_program   # asume un helper que ejecuta la lista
    stats = run_program(build_program())
    # stats = {'ciclos':..., 'stalls':..., 'hits':..., 'misses':...}
    print(stats)
