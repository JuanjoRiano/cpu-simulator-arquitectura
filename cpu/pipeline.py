from instruction import Instruction

IF_ID = {}
ID_EX = {}
EX_MEM = {}
MEM_WB = {}

PC = 0
registers = [0] * 32
instruction_memory = []
memory = [0] * 1024

cycle_count = 0
instruction_count = 0
stalls = 0

forward_EX_MEM = {}
forward_MEM_WB = {}

stall_pipeline = False

def IF():
    global PC, IF_ID, instruction_count, stall_pipeline
    if stall_pipeline:
        IF_ID['instruction'] = Instruction('NOP')
        stall_pipeline = False
        return
    if PC < len(instruction_memory):
        instr = instruction_memory[PC]
        IF_ID['instruction'] = instr
        PC += 1
        instruction_count += 1
    else:
        IF_ID['instruction'] = None

def ID():
    global IF_ID, ID_EX, stall_pipeline
    instr = IF_ID.get('instruction')
    if instr:
        if instr.opcode == 'BEQ':
            stall_pipeline = True
        ID_EX = {
            'instruction': instr,
            'rs_val': registers[instr.rs] if instr.rs is not None else 0,
            'rt_val': registers[instr.rt] if instr.rt is not None else 0,
            'rd': instr.rd,
            'rt': instr.rt,
            'imm': instr.imm
        }
    else:
        ID_EX = {}

def EX():
    global ID_EX, EX_MEM, forward_EX_MEM
    instr = ID_EX.get('instruction')
    if not instr:
        EX_MEM = {}
        return

    rs_val = ID_EX.get('rs_val', 0)
    rt_val = ID_EX.get('rt_val', 0)

    if forward_MEM_WB.get('rd') == instr.rs:
        rs_val = forward_MEM_WB.get('result')
    if forward_MEM_WB.get('rd') == instr.rt:
        rt_val = forward_MEM_WB.get('result')

    result = 0
    if instr.opcode == 'ADD':
        result = rs_val + rt_val
    elif instr.opcode == 'SUB':
        result = rs_val - rt_val
    elif instr.opcode == 'MUL':
        result = rs_val * rt_val
    elif instr.opcode in ['LW', 'SW']:
        result = rs_val + instr.imm
    elif instr.opcode == 'BEQ':
        if rs_val == rt_val:
            global PC
            PC += instr.imm

    EX_MEM = {
        'instruction': instr,
        'result': result,
        'rt_val': rt_val,
        'rd': instr.rd,
        'rt': instr.rt
    }
    forward_EX_MEM.clear()
    forward_EX_MEM.update(EX_MEM)

def MEM():
    global EX_MEM, MEM_WB, forward_MEM_WB
    instr = EX_MEM.get('instruction')
    if not instr:
        MEM_WB = {}
        return

    result = EX_MEM.get('result')

    if instr.opcode == 'LW':
        result = memory[result]
    elif instr.opcode == 'SW':
        memory[result] = EX_MEM.get('rt_val')

    MEM_WB = {
        'instruction': instr,
        'result': result,
        'rd': EX_MEM.get('rd')
    }
    forward_MEM_WB.clear()
    forward_MEM_WB.update(MEM_WB)

def WB():
    global MEM_WB
    instr = MEM_WB.get('instruction')
    if not instr:
        return
    if instr.opcode in ['ADD', 'SUB', 'MUL', 'LW'] and instr.rd is not None:
        registers[instr.rd] = MEM_WB.get('result')

def run_cycle():
    global cycle_count
    WB()
    MEM()
    EX()
    ID()
    IF()
    cycle_count += 1

def load_instructions(instr_list):
    global instruction_memory
    instruction_memory = instr_list.copy()
    reset()

def reset():
    global PC, IF_ID, ID_EX, EX_MEM, MEM_WB, registers, cycle_count, instruction_count, forward_EX_MEM, forward_MEM_WB
    PC = 0
    IF_ID = {}
    ID_EX = {}
    EX_MEM = {}
    MEM_WB = {}
    registers = [0] * 32
    cycle_count = 0
    instruction_count = 0
    forward_EX_MEM.clear()
    forward_MEM_WB.clear()
