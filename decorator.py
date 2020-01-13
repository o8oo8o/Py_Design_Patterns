#!/usr/bin/env python

"""
装饰模式
"""

from abc import ABCMeta, abstractmethod


class BaseClass(metaclass=ABCMeta):
    @abstractmethod
    def run(self):
        pass


class People(BaseClass):

    def run(self):
        print("人在跑步")


class DogDecorator(BaseClass):

    def __init__(self, cls):
        self._people = cls()

    def run(self):
        print(f"人模狗样的")
        self._people.run()


class CatDecorator(BaseClass):

    def __init__(self, cls):
        self._people = cls()

    def run(self):
        print(f"人模猫样的")
        self._people.run()


if __name__ == "__main__":
    peopleA = People()
    peopleA.run()
    print("===========")
    peopleB = DogDecorator(People)
    peopleB.run()
    print("===========")
    peopleC = CatDecorator(People)
    peopleC.run()
