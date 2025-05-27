class Instruction:
    def __init__(self, opcode, rs=None, rt=None, rd=None, imm=None):
        self.opcode = opcode.upper()
        self.rs = rs
        self.rt = rt
        self.rd = rd
        self.imm = imm

    def __str__(self):
        if self.opcode in ['ADD', 'SUB', 'MUL']:
            return f"{self.opcode} R{self.rd}, R{self.rs}, R{self.rt}"
        elif self.opcode in ['LW', 'SW']:
            return f"{self.opcode} R{self.rt}, {self.imm}(R{self.rs})"
        elif self.opcode in ['BEQ']:
            return f"{self.opcode} R{self.rs}, R{self.rt}, {self.imm}"
        else:
            return f"{self.opcode} (formato desconocido)"
