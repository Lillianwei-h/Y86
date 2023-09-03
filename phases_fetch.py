from const import *
from general_funcs import *


#################################################################################
# 六大阶段的第一阶段: 取指
# 六大阶段皆按照CSAPP 'Y-86的顺序实现' 一节进行编写
# icode ifun 两个字段以标识指令类型和操作类型（若有）
# imem_error 标志变量表示是否有内存读取错误
# instr_valid 标志变量表示指令是否合法
# need_regids 标志变量表示该指令是否需要读/写内存
# need_valC 标志变量表示该指令是否包含后续常数
# 根据 need_regids need_valC计算valP（下一个PC值）
#################################################################################
def fetch(cpu):
    cpu.operation = []
    imem_error = False
    try:    # 取icode和ifun
        icf = split(cpu.Mem.read(cpu.PC, 1), 1)
        cpu.icode = hex2int(icf[0])
        cpu.ifun = hex2int(icf[1])
    except:
        cpu.imem_error = True
        cpu.icode = INOP
        cpu.ifun = FNONE

    instr_valid = cpu.icode not in [INOP, IHALT, IRRMOVQ, IIRMOVQ, IRMMOVQ, IMRMOVQ, IOPQ, IJXX, ICALL, IRET, IPOPQ, IPUSHQ]
    cpu.need_regids = cpu.icode in [IRMMOVQ, IOPQ, IPUSHQ, IPOPQ, IRRMOVQ, IIRMOVQ, IMRMOVQ]
    cpu.need_valC = cpu.icode in [IRMMOVQ, IIRMOVQ, IMRMOVQ, IJXX, ICALL]
    valp = cpu.PC + 1 + int(cpu.need_regids) + 8 * int(cpu.need_valC)
    # print(valp)
    # valp = str(valp)
    cpu.valP = valp
    # print(cpu.valP)

    cpu.valC = ZERO
    if cpu.need_valC:
        try:
            cpu.valC = cpu.Mem.read(cpu.PC + 1 + int(cpu.need_regids), 8)
            # print(cpu.valC)
        except:
            print("Fetch: read valC fail")
            cpu.imem_error = True

    if cpu.need_regids:
        try:
            cpu.rA, cpu.rB = split(cpu.Mem.read(cpu.PC + 1, 1), 1)
            cpu.rA = hex2int(cpu.rA)
            cpu.rB = hex2int(cpu.rB)
        except:
            print("Fetch: read rA, rB fail")
            cpu.imem_error = True

    if cpu.imem_error:
        cpu.changeSTAT(SADR)
    elif instr_valid:
        cpu.changeSTAT(SINS)
    elif cpu.icode == IHALT:
        cpu.changeSTAT(SHLT)
    else:
        cpu.changeSTAT(SAOK)
