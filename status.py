#!/usr/bin/env python

"""
状态模式
"""


class State:
    def __init__(self):
        pass

    def get_msg(self, w):
        pass


class Work:

    def __init__(self, status=None):
        if status is None:
            status = []
        self.hour = 9
        self.curr = StateA()
        self.status = status

    def set_state(self, s):
        self.curr = s

    def speak(self):
        for stat in self.status:
            stat.get_msg(self)


class StateA(State):
    def get_msg(self, w):
        if 0 <= w.hour < 7:
            print(f"当前时间:{w.hour},在半夜")


class StateB(State):
    def get_msg(self, w):
        if 7 <= w.hour < 12:
            print(f"当前时间:{w.hour},在上午")


class StateC(State):
    def get_msg(self, w):
        if 12 <= w.hour < 19:
            print(f"当前时间:{w.hour},在下午")


class StateD(State):
    def get_msg(self, w):
        if 19 <= w.hour < 24:
            print(f"当前时间:{w.hour},在晚上")


if __name__ == "__main__":
    work = Work(status=[StateA(), StateB(), StateC(), StateD()])
    work.hour = 5
    work.speak()
    work.hour = 11
    work.speak()
    work.hour = 15
    work.speak()
    work.hour = 21
    work.speak()
