from typing import Any

class Item:
    def __init__(self, name: str, value: float):
        self.name = name
        self.value = value

    def __eq__(self, other):
        return self.value == other.value

    def __ne__(self, other):
        return self.value != other.value

    def __lt__(self, other):
        return self.value < other.value

    def __le__(self, other):
        return self.value <= other.value

    def __gt__(self, other):
        return self.value > other.value

    def __ge__(self, other):
        return self.value >= other.value

# Creating instances of Item
item1 = Item('Apple', 10)
item2 = Item('Banana', 20)

# Comparing the items
print(item1 == item2)
print(item1 != item2)
print(item1 < item2)
print(item1 <= item2)
print(item1 > item2)
print(item1 >= item2)


