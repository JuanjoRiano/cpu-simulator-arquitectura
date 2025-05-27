from instruction import Instruction
from pipeline import load_instructions, run_cycle, cycle_count, instruction_count

def main():
    instructions = [
        Instruction('ADD', rs=1, rt=2, rd=3),
        Instruction('SUB', rs=3, rt=4, rd=5),
        Instruction('MUL', rs=5, rt=6, rd=7)
    ]

    load_instructions(instructions)

    while cycle_count < len(instructions) + 4:
        run_cycle()

    print(f"Ciclos totales: {cycle_count}")
    print(f"Instrucciones ejecutadas: {instruction_count}")

if __name__ == "__main__":
    main()
