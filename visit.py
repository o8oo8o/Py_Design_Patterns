#!/usr/bin/env python

"""
访问者模式
"""


class Book:
    def __init__(self, name):
        self.name = name


class Student:

    def read(self, book):
        print(f"{book.name}这本书,学生看不懂")


class Teacher:

    def read(self, book):
        print(f"{book.name}这本书,老师看不懂")


if __name__ == "__main__":
    book = Book("金瓶梅")

    objs = [Student(), Teacher()]
    for obj in objs:
        obj.read(book)
