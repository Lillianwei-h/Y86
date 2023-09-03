from const import *
from general_funcs import *



#################################################################################
# 六大阶段第五阶段: 写回
# 根据 dstE 和 dstM 写回寄存器
#################################################################################
def writeback(cpu):
    if cpu.dstE != RNONE:
        cpu.Reg.write(cpu.dstE, cpu.valE)
    if cpu.dstM != RNONE:
        cpu.Reg.write(cpu.dstM, cpu.valM)
