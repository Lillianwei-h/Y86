from const import *


# 把const中0-f的数值转为十六进制字符, 返回字符
def id2strHex(d):
    return "0123456789abcdef"[int(d)]


# 把字符串s按l位分割，返回值是分割后的数组块
def split(s, l):
    res = [s[i: i + l] for i in range(0, len(s), l)]
    return res


# X86（Y86）结构是小端模式，需要转换储存模式
# 转换存储模式
def swichEndian(s):
    if s.startswith("0x") or s.startswith("0X"):
        s = s[2:]  # 去除开头的'0x'字段
    return ''.join(reversed(split(s, 2)))  # s按两位两位分隔, 进行倒序


# 十六进制字符串换成十进制整数
def hex2int(i):
    res = int(i, 16)    # 读取16进制字符串
    max_int_str = "7fffffffffffffff"
    MAXINT = int(max_int_str, 16)   # 计算32可表示的最大正数
    # print("MAXINT:")
    # print(MAXINT)
    if res > MAXINT:        # 针对溢出情况的处理: 用32位二进制数能表示的最大正数减去得出的结果并+1
        j = i[0:1]
        i_firbit = int(j, 16)
        i_firbit -= 8       # 十六进制最高位 -8
        i_f = id2strHex(i_firbit)
        j = i_f + i[1:]
        res = int(j, 16)
        ret_val = '-' + str(MAXINT - res + 1)   # 加上负号
        return int(ret_val)     # 返回int类型
    else:
        return res      # 没有发生溢出, 直接返回


# 十六进制小端存储字符串形式转为十进制整数: 转换存储形式并且按16进制进行读取、计算
def strHex2int(i):
    return int(swichEndian(i), 16)


# 十进制整数转化为十六进制形式的字符串
def int2strHex(i):
    if i >= 0:
        s = hex(i)
        s = s[2:]       # hex() 返回'0xXXXXXXXX'模式串, 将开头的'0x'字段去除
        # if len(s) > 8:
        #     s = s[-8:]
        # s = "0" * (8 - len(s)) + s
    else:
        i = ~i + 1
        s = hex(i)
    return s

