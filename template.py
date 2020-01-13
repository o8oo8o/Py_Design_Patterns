#!/usr/bin/env python

"""
模板模式
"""

from abc import ABCMeta, abstractmethod


class Template(metaclass=ABCMeta):

    @abstractmethod
    def step_a(self):
        pass

    def step_b(self):
        pass

    def exe(self):
        self.step_a()
        self.step_b()


class TemplateImpA(Template):

    def step_a(self):
        print("a_step_a")

    def step_b(self):
        print("a_step_b")


class TemplateImpB(Template):

    def step_a(self):
        print("b_step_a")

    def step_b(self):
        print("b_step_b")


if __name__ == "__main__":
    ta = TemplateImpA()
    ta.exe()

    tb = TemplateImpB()
    tb.exe()
