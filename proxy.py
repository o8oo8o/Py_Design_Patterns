#!/usr/bin/env python

"""
代理模式
"""


class Boy:
    def send(self, proxy, money):
        proxy.send(money)


class Girl:
    def recv(self, money):
        print(f"姑娘收到{money}钱")


class Proxy:
    def __init__(self, name, proxy_obj):
        self.name = name
        self.proxy_obj = proxy_obj

    def send(self, money):
        self.proxy_obj.recv(money)


if __name__ == "__main__":
    b = Boy()
    g = Girl()
    p = Proxy("媒婆", g)
    b.send(p, 300)
