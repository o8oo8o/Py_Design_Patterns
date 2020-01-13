#!/usr/bin/env python

"""
迭代模式
"""


class Iter:

    def __init__(self, data):
        self.__index = 0
        self.data = data

    def begin(self):
        self.__index = 0

    def end(self):
        self.__index = len(self.data)

    def prev(self):
        self.__index -= 1

    def next(self):
        if len(self.data) > self.__index:
            self.__index += 1
            return True
        else:
            return False

    def get_current_data(self):
        return self.data[self.__index - 1]


if __name__ == "__main__":
    obj = Iter(data=list(range(10)))
    while (obj.next()):
        print(obj.get_current_data())
    print(obj.get_current_data())
    obj.prev()
    obj.prev()
    obj.prev()
    obj.prev()
    print(obj.get_current_data())
