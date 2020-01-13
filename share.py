#!/usr/bin/env python

"""
享元模式
"""


class Water:

    def __init__(self, taste):
        print("water_init")
        self.taste = taste

    def set_user(self, user):
        self.user = user

    def show_info(self):
        print(f"{self.user} 喝 {self.taste}水")


class WaterFactory:
    def __init__(self):
        self.__water = {}

    def get_water(self, taste):
        water = self.__water.get(taste)
        if water is None:
            water = Water(taste)
            # self.__water.setdefault(taste,water)
        return water


if __name__ == "__main__":
    factory = WaterFactory()

    wa = factory.get_water("糖")
    wa.set_user("张三")
    wa.show_info()

    wb = factory.get_water("酸")
    wb.set_user("李四")
    wb.show_info()

    wc = factory.get_water("酸")
    wc.set_user("王五")
    wc.show_info()
