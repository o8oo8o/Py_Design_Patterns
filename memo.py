#!/usr/bin/env python

"""
备忘录模式
"""


class MemoManage:
    def __init__(self):
        self.memo = None

    def save_memo(self, memo):
        self.memo = memo

    def get_memo(self):
        return self.memo


class Person:

    def __init__(self, name):
        self.name = name
        self.workList = []

    def add_work_content(self, txt):
        self.workList.append(txt)

    def get_work_list(self):
        return self.workList

    def recover_work_list(self, workList):
        self.workList = workList

    def show_work(self):
        for work in self.workList:
            print(work)

    def forget(self):
        self.workList = []


if __name__ == "__main__":
    pa = Person("dog")
    pa.add_work_content("写程序")
    pa.add_work_content("写PPT")

    # 建立一个备忘管理
    mm = MemoManage()
    mm.save_memo(pa.get_work_list())

    pa.forget()
    pa.show_work()
    print("=====(恢复备忘)=====")
    pa.recover_work_list(mm.get_memo())

    pa.show_work()
