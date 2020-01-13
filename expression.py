#!/usr/bin/env python

"""
解释器模式
"""
from abc import ABCMeta, abstractmethod


class AbsExpression(metaclass=ABCMeta):
    @abstractmethod
    def interpreter(self, context):
        pass


class ExpressionA(AbsExpression):
    def interpreter(self, context):
        print("A", context.name)


class ExpressionB(AbsExpression):
    def interpreter(self, context):
        print("B", context.name)


class Context:
    def __init__(self):
        self.name = ""


if __name__ == "__main__":
    con_text = Context()
    con_text.name = "huang"
    add = [ExpressionA(), ExpressionB()]
    for item in add:
        item.interpreter(con_text)
