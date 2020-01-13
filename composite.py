#!/usr/bin/env python

"""
组合模式
"""

from abc import ABCMeta


class BaseClass(metaclass=ABCMeta):
    def __init__(self, name):
        self.name = name
        self.sub = []

    def show(self):
        for item in self.sub:
            print(item.name)


class Root(BaseClass):
    def __init__(self, name):
        super().__init__(name)
        self.sub = []

    def add(self, branch):
        self.sub.append(branch)


class Branch(BaseClass):
    def __init__(self, name):
        super().__init__(name)
        self.sub = []

    def add(self, leaf):
        self.sub.append(leaf)


class Leaf(BaseClass):
    def __init__(self, name):
        super().__init__(name)


if __name__ == "__main__":
    root = Root("tree")
    bra = Branch("bra")
    brb = Branch("brb")
    lea = Leaf("lea")
    leb = Leaf("leb")
    lec = Leaf("lec")
    led = Leaf("led")

    bra.add(lea)
    bra.add(leb)
    brb.add(lec)
    brb.add(led)

    root.add(bra)
    root.add(brb)

    root.show()
    bra.show()
