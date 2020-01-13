# !/usr/bin/env python


"""
中介模式
"""


class HouseInfo:
    """房产信息"""

    def __init__(self, price, address):
        self.price = price
        self.address = address

    def __str__(self):
        return f"房子价格{self.price},房子地址{self.address}"


class HouseAgent:
    """房屋中介"""

    def __init__(self, name):
        self.name = name
        self.houseInfo = []

    def add_house(self, house):
        self.houseInfo.append(house)

    def price_find(self, price):
        for house in self.houseInfo:
            if house.price == price:
                return house
        return "没有合适的房子"


class HouseOwner:
    """房东"""

    def __init__(self, owner):
        self.owner = owner
        self.houseInfo = None

    def set_house_info(self, price, address):
        self.houseInfo = HouseInfo(price, address)

    def publish_house_info(self, house_agent):
        house_agent.add_house(self.houseInfo)


class Customer:
    """租客"""

    def __init__(self, name):
        self.name = name

    def price_find_house(self, price, house_agent):
        return house_agent.price_find(price)


if __name__ == "__main__":
    # 建立三个房产中介
    agent_a = HouseAgent("链家")
    agent_b = HouseAgent("贝壳")
    # AgentC = HouseAgent("自如")

    # 建立房东A
    house_owner_a = HouseOwner("王老板")
    house_owner_a.set_house_info(1111, "天安门")
    house_owner_a.publish_house_info(agent_a)

    # 建立房东B,把一个房子在两个中介平台发布
    house_owner_b = HouseOwner("黄老板")
    house_owner_b.set_house_info(2222, "东直门")
    house_owner_b.publish_house_info(agent_a)
    house_owner_b.publish_house_info(agent_b)

    # 建立房东C
    house_owner_c = HouseOwner("张老板")
    house_owner_c.set_house_info(3333, "西直门")
    house_owner_c.publish_house_info(agent_b)

    dog = Customer("阿狗")
    house = dog.price_find_house(2222, agent_a)
    print(house)

    cat = Customer("阿猫")
    house = cat.price_find_house(3333, agent_b)
    print(house)
