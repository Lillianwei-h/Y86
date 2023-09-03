from const import *
from general_funcs import *


class ConditionCode:
    def __init__(self):
        self.ZF = True
        self.SF = False
        self.OF = False

    def getCC(self):
        cc = {
            'ZF': int(self.ZF),
            'SF': int(self.SF),
            'OF': int(self.OF)
        }
        return cc