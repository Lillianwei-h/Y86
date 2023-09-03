from const import *
from general_funcs import *


#################################################################################
# 六大阶段第六阶段: 更新PC
# 根据 icode 用不同的值更新 PC
#################################################################################
def updatePC(cpu):
    if cpu.icode in [ICALL]:
        cpu.PC = strHex2int(cpu.valC)
    elif cpu.icode in [IJXX] and cpu.Cnd:
        cpu.PC = strHex2int(cpu.valC)
    elif cpu.icode in [IRET]:
        cpu.PC = hex2int(swichEndian(cpu.valM))
    elif cpu.STAT in [SHLT]:
        cpu.PC = cpu.PC
    else:
        cpu.PC = cpu.valP
