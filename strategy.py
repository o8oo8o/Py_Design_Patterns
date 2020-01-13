#!/usr/bin/env python

"""
策略模式
"""


class Cash3:
    def set_discount(self, price):
        print("3折价格:", price * 0.3)


class Cash5:
    def set_discount(self, price):
        print("5折价格:", price * 0.5)


class Cash8:
    def set_discount(self, price):
        print("8折价格:", price * 0.8)


class Commodity:
    def __init__(self, name, discount):
        self.name = name
        self.discount = discount

    def pay(self, price):
        self.discount.set_discount(price)


if __name__ == "__main__":
    dd = Commodity("杜杜", Cash3())
    dd.pay(20)

    dd = Commodity("冈本", Cash5())
    dd.pay(20)
