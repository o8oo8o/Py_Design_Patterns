#!/usr/bin/env python

"""
抽象工厂模式
"""


class PetShop:

    def __init__(self, animal_factory=None):
        self.pet_factory = animal_factory

    def show_pet(self):
        pet = self.pet_factory.get_pet()
        print("动物类型:", str(pet))
        print("动物叫声:", pet.speak())
        print("吃的东西:", self.pet_factory.get_food())


class Dog:
    def speak(self):
        return "wang"

    def __str__(self):
        return "Dog"


class Cat:
    def speak(self):
        return "miao"

    def __str__(self):
        return "Cat"


# Factory class
class DogFactory:
    def get_pet(self):
        return Dog()

    def get_food(self):
        return "dog food"


class CatFactory:
    def get_pet(self):
        return Cat()

    def get_food(self):
        return "cat food"


if __name__ == "__main__":
    shop = PetShop(DogFactory())
    shop.show_pet()
