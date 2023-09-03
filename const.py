regName = {
    0: 'RAX',
    1: 'RCX',
    2: 'RDX',
    3: 'RBX',
    4: 'RSP',
    5: 'RBP',
    6: 'RSI',
    7: 'RDI',
    8: 'R8',
    9: 'R9',
    0xa: 'R10',
    0xb: 'R11',
    0xc: 'R12',
    0xd: 'R13',
    0xe: 'R14',
    0xf: 'null',
    '0': 'RAX',
    '1': 'RCX',
    '2': 'RDX',
    '3': 'RBX',
    '4': 'RSP',
    '5': 'RBP',
    '6': 'RSI',
    '7': 'RDI',
    '8': 'R8',
    '9': 'R9',
    'a': 'R10',
    'b': 'R11',
    'c': 'R12',
    'd': 'R13',
    'e': 'R14',
    'f': 'null',
    'F': 'null'
}

instrName = {
    "00": "halt",
    "10": "nop",
    "20": "rrmovq",
    "21": "cmovle",
    "22": "cmovl",
    "23": "cmove",
    "24": "cmovne",
    "25": "cmovge",
    "26": "cmovg",
    "30": "irmovq",
    "40": "rmmovq",
    "50": "mrmovq",
    "60": "addq",
    "61": "subq",
    "62": "andq",
    "63": "xorq",
    "70": "jmp",
    "71": "jle",
    "72": "jl",
    "73": "je",
    "74": "jne",
    "75": "jge",
    "76": "jg",
    "80": "call",
    "90": "ret",
    "a0": "pushq",
    "b0": "popq"
}

IHALT = 0x0   # halt
INOP = 0x1    # nop
IRRMOVQ = 0x2  # rrmovl
IIRMOVQ = 0x3  # irmovl
IRMMOVQ = 0x4  # rmmovl
IMRMOVQ = 0x5  # mrmovl
IOPQ = 0x6    # integer operation
IJXX = 0x7    # jump
ICALL = 0x8   # call
IRET = 0x9    # ret
IPUSHQ = 0xA  # pushl
IPOPQ = 0xB   # popl

CJMP = 0x0
CMOVLE = 0x1
CMOVL = 0x2
CMOVE = 0x3
CMOVNE = 0x4
CMOVGE = 0x5
CMOVG = 0x6

FNONE = 0x0   # Default function code(默认功能码)

# Register IDs:
RRAX = 0x0
RRCX = 0x1
RRDX = 0x2
RRBX = 0x3
RRSP = 0x4
RRBP = 0x5
RRSI = 0x6
RRDI = 0x7
RR8 = 0x8
RR9 = 0x9
RR10 = 0xa
RR11 = 0xb
RR12 = 0xc
RR13 = 0xd
RR14 = 0xe
RNONE = 0xf

ALUADD = 0x0

SAOK = 0x1  # Status Code for normal operation(正常状态操作码)
SADR = 0x2  # Status Code for address exception(地址异常状态码)
SINS = 0x3  # Status Code for illegal instruction exception(非法指令异常状态码)
SHLT = 0x4  # Status Code for halt(halt状态码)

ZERO = "0000000000000000"
EIGHT = "0800000000000000"
NEGEIGHT = "F8FFFFFFFFFFFFFF"
AADD = 0x0
ASUB = 0x1
AAND = 0x2
AXOR = 0x4
VNONE = '0000000000000000'

MEMSIZE = 1 << 12
