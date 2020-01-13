#!/usr/bin/env python

"""
单例模式
"""


class Obj:
    __instance = None
    __is_first_instance = False

    def __new__(cls, val):
        if not Obj.__instance:
            Obj.__instance = super().__new__(cls)
        return Obj.__instance

    def __init__(self, val):
        if not Obj.__is_first_instance:
            print("创建单例对象")
            self.val = val
            Obj.__is_first_instance = True
        else:
            print("单例对象已存在")

    def get_val(self):
        return self.val


if __name__ == "__main__":
    aa = Obj(123)
    bb = Obj(456)
    cc = Obj(789)

    print(id(aa), "++", id(bb), "++", id(cc))

    print(aa.get_val())
    print(bb.get_val())
    print(cc.get_val())
