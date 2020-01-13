#!/usr/bin/env python

"""
桥接模式
"""
from abc import ABCMeta, abstractmethod


class Shape(metaclass=ABCMeta):

    def __init__(self, color):
        self.__color = color

    @abstractmethod
    def get_shape_type(self):
        pass

    def shape_info(self):
        print(f"{self.get_shape_type()}是{self.__color.get_color()}色")


class Rectangle(Shape):

    def __init__(self, color):
        super().__init__(color)

    def get_shape_type(self):
        return "矩形"


class Ellipse(Shape):
    def __init__(self, color):
        super().__init__(color)

    def get_shape_type(self):
        return "椭圆"


class Color(metaclass=ABCMeta):

    @abstractmethod
    def get_color(self):
        pass


class Red(Color):
    def get_color(self):
        return "红"


class Green(Color):
    def get_color(self):
        return "绿"


if __name__ == "__main__":
    ra = Rectangle(Red())
    ra.shape_info()

    ea = Ellipse(Green())
    ea.shape_info()
