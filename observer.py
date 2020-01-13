#!/usr/bin/env python

"""
监听模式
"""

from abc import ABCMeta, abstractmethod


class Mode(metaclass=ABCMeta):
    @abstractmethod
    def update(self, man):
        pass


class Man:
    def __init__(self):
        self.__observers = []
        self.money = 0

    def add_observer(self, mode):
        self.__observers.append(mode)

    def del_observer(self, mode):
        self.__observers.remove(mode)

    def notify_observer(self):
        for obj in self.__observers:
            obj.update(self)

    def set_money(self, money):
        self.money = money
        print(f"我有{money}元钱")
        self.notify_observer()


class ModeA(Mode):

    def update(self, man):
        if 0 <= man.money < 200:
            print("可以滚回家")


class ModeB(Mode):

    def update(self, man):
        if 200 <= man.money < 300:
            print("可以喝啤酒")
            print("可以吹牛逼")


class ModeC(Mode):

    def update(self, man):
        if 300 <= man.money < 500:
            print("可以大保健")
            print("可以找妹子")


if __name__ == "__main__":
    man_a = Man()
    man_a.add_observer(ModeA())
    man_a.add_observer(ModeB())
    man_a.add_observer(ModeC())
    man_a.set_money(422)
