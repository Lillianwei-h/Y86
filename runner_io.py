import io
import os
import json
import pprint
import fileinput
from CPU import *
from phases_fetch import *
from phases_decode import *
from phases_memory import *
from phases_execute import *
from phases_writeback import *
from phases_updatePC import *

def run(cpu):
    log_list = []
    first_open = True
    while cpu.getSTAT() not in ['SHLT', 'SINS', 'SADR']:
        fetch(cpu)
        decode(cpu)
        execute(cpu)
        memory(cpu)
        writeback(cpu)
        updatePC(cpu)
        log = cpu.getCPUlog()
        log_list.append(log)
    res = json.dumps(log_list, sort_keys=False, indent=4, separators=(',', ': '))       # 改为json格式
    generate_answer(log_list, first_open)        # 输出到文件


# 生成答案输出文件
def generate_answer(res, flag):
    current_path = os.path.abspath(".")     # 获取当前绝对路径
    father_file_loc = current_path.rfind('\\')       # 答案文件夹在当前路径的的父文件夹下，是一个新的文件夹，故需要找到父文件夹字串
    path1 = current_path[0: father_file_loc]
    # 生成答案文件所在文件名（绝对路径）
    father_file = current_path + "\\web-design\\"+"answer.json"       # 输出文件 web-design/answer.json
    file = open(father_file, 'w')       # 打开只写文件，若无则新建
    json.dump(res,file)
    file.close()

if __name__ == "__main__":
    # 重定向输入
    test = io.StringIO(open(input(), "r").read())
    myCPU = CPU()
    myCPU.init(test)
    run(myCPU)
