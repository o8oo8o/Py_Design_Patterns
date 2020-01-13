#!/usr/bin/env python

"""
构建模式
"""


class Dog:
    def __init__(self, name):
        self.name = name

    def create_head(self):
        print("create_dog_head")

    def create_tail(self):
        print("create_dog_tail")

    def cry(self):
        print("wang")


class Cat:
    def __init__(self, name):
        self.name = name

    def create_head(self):
        print("create_cat_head")

    def create_tail(self):
        print("create_cat_tail")

    def cry(self):
        print("miao")


class Build:
    def __init__(self, animal):
        self.animal = animal

    def create_animal(self):
        self.animal.create_head()
        self.animal.create_tail()
        return self.animal


if __name__ == "__main__":
    dogA = Dog("dog_a")
    catA = Cat("cat_a")

    build = Build(dogA)
    dog = build.create_animal()
    dog.cry()

    build = Build(catA)
    cat = build.create_animal()
    cat.cry()
