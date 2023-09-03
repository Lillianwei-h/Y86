from const import *
from general_funcs import *



#################################################################################
# 六大阶段第四阶段: 访存
# 根据 icode 判断要对内存进行的操作（读or写），确定操作的目标地址
# 读取出的数据为 valM
#################################################################################
def memory(cpu):
    cpu.valM = VNONE

    if cpu.icode in [IPOPQ, IRET]:
        mem_addr = cpu.valB
    elif cpu.icode in [IRMMOVQ, IPUSHQ, IMRMOVQ, ICALL]:
        mem_addr = cpu.valE
    else:
        mem_addr = None

    if cpu.icode in [IRMMOVQ, IPUSHQ]:
        mem_data = cpu.valA
    elif cpu.icode in [ICALL]:
        mem_data = int2strHex(cpu.valP)
    else:
        mem_data = VNONE

    if cpu.icode in [IMRMOVQ, IPOPQ, IRET]:
        read_flag = True
    else:
        read_flag = False
    if cpu.icode in [IRMMOVQ, IPUSHQ, ICALL]:
        write_flag = True
    else:
        write_flag = False

    if read_flag:
        try:
            if isinstance(mem_addr, str):
                cpu.valM = cpu.Mem.read(strHex2int(mem_addr), 8)
            elif isinstance(mem_addr, int):
                cpu.valM = cpu.Mem.read(mem_addr, 8)
        except:
            cpu.STAT = SADR

    if write_flag:
        try:
            cpu.Mem.write(strHex2int(mem_addr), mem_data)
        except:
            cpu.STAT = SADR
