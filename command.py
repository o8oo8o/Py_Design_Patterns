#!/usr/bin/env python

"""
命令模式
"""
from abc import ABCMeta, abstractmethod


class Receiver:

    def run(self):
        print("run...")

    def eat(self):
        print("eat...")


class Command:
    __metaclass__ = ABCMeta

    @abstractmethod
    def execute(self):
        pass


# 跑命令
class RunCommand(Command):
    def __init__(self, receiver):
        self.__receiver = receiver

    def execute(self):
        self.__receiver.run()


# 吃命令
class EatCommand(Command):
    def __init__(self, receiver):
        self.__receiver = receiver

    def execute(self):
        self.__receiver.eat()


class Client:
    def __init__(self, command):
        self.command = command

    def exe_cmd(self):
        self.command.execute()


if __name__ == "__main__":
    recv = Receiver()
    run_cmd = RunCommand(recv)
    eat_cmd = EatCommand(recv)
    ca = Client(run_cmd)
    # ca = Client(eat_cmd)
    ca.exe_cmd()
