#!/usr/bin/env python

from copy import copy, deepcopy

"""
克隆(原型)模式
"""


class Dog:
    def __init__(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def clone(self):
        return copy(self)

    def deep_clone(self):
        return deepcopy(self)


if __name__ == "__main__":
    dog_a = Dog("阿黄")
    dog_b = dog_a.clone()

    print(dog_b.get_name())
