from abc import ABC, abstractmethod

class Shop(ABC):
    @abstractmethod
    def add_item(self, section, item, price):
        return None

    @abstractmethod
    def remove_item(self, section, item):
        return None


class Cart(Shop):
    def __init__(self, username):
        self.username = username
        self.itemsDict = {}

    def add_to_cart(self, category, item, price):
        if category in self.itemsDict:
            value = self.itemsDict.get(category)
            value.append([item, price])
        else:
            self.itemsDict.update({category: [[item, price]]})

    def remove_from_cart(self, section, item):
        value = self.itemsDict.get(section)
        for i in value:
            if item in i:
                value.remove(i)


l = [1,2,3,4,5,6,7,8]
print(l[:-4])
