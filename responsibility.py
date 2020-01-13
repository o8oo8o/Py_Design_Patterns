#!/usr/bin/env python

"""
职责(责任链)模式
"""


class Handler:
    def set_next_handler(self, next_handler):
        self.next_handler = next_handler


# 流程发起人
class Person(Handler):
    def __init__(self, name, off_day):
        self.name = name
        self.off_day = off_day

    def request(self):
        self.next_handler.handler(self)


# 审批人A
class ManageA(Handler):
    def __init__(self, name):
        self.name = name

    def handler(self, person):
        if 1 <= person.off_day < 3:
            print(f"A={self.name}审批通过权限内")
        else:
            print(f"A={self.name}审批通过,转交下一步")
            self.next_handler.handler(person)


# 审批人B
class ManageB(Handler):
    def __init__(self, name):
        self.name = name

    def handler(self, person):
        if 3 <= person.off_day < 7:
            print(f"B={self.name}审批通过权限内")
        else:
            print(f"B={self.name}审批通过,转交下一步")
            self.next_handler.handler(person)


# 审批人C
class ManageC(Handler):
    def __init__(self, name):
        self.name = name

    def handler(self, person):
        if 7 <= person.off_day < 15:
            print(f"C={self.name}审批通过权限内")
        else:
            print(f"C={self.name}审批拒绝超过15天")


if __name__ == "__main__":
    # 建立3个审批人
    aa = ManageA("主管")
    bb = ManageB("经理")
    cc = ManageC("总监")

    # 设置审批关系
    aa.set_next_handler(bb)
    bb.set_next_handler(cc)

    dog = Person("阿狗", 8)
    dog.set_next_handler(aa)
    dog.request()
