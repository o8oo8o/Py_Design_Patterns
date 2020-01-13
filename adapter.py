#!/usr/bin/env python

"""
适配模式
"""


class ClassB(object):

    def need_method(self):
        print("class_A")


class ClassA(object):

    def need_method_other_name(self):
        print("class_B")


class Adapter(object):
    def __init__(self, cls):
        self.instance = cls()

    def need_method(self):
        self.instance.need_method_other_name()


if __name__ == "__main__":
    aa = Adapter(ClassA)
    bb = ClassB()

    aa.need_method()
    bb.need_method()
