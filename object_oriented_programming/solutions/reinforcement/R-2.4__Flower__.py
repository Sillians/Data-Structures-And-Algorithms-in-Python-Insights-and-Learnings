# Write a Python class, Flower, that has three instance variables of type str, int, and float,
# that respectively represent the name of the flower, its number of petals, and its price.
# Your class must include a constructor method that initializes each variable to an
# appropriate value, and your class should include methods for setting the value of each type,
# and retrieving the value of each type.

# Note: Both methods for getters and setters must be the same, and the order of declaration matters.
# i.e, the getter must be defined before the setter in the file or else a NameError output.


class Flower:

    def __init__(self, name: str, number_of_petals: int, price: float):
        self._name = name
        self._number_of_petals = number_of_petals
        self._price = price

    @property
    def set_name(self):
        return self._name

    @set_name.setter
    def set_name(self, value: str):
        try:
            assert type(value) == str, f"name has to be string, not {type(value)}"
            self._name = value
        except Exception as err:
            print(err)

    @property
    def number_of_petals(self):
        return self._number_of_petals

    @number_of_petals.setter
    def number_of_petals(self, number_of_petals: int):
        try:
            assert type(number_of_petals) == int, f"Number of petals has to be an integer, not {type(number_of_petals)}"
            self._number_of_petals = number_of_petals
        except Exception as err:
            print(err)

    @property
    def flower_price(self):
        return self._price

    @flower_price.setter
    def flower_price(self, price: float):
        try:
            assert type(price) == float or type(price) == int, f"Price of flower has be float or integer, not {type(price)}"
            self._price = price
        except Exception as err:
            print(err)



rose = Flower("Rose", 6, 50)
iris = Flower("Iris", 15, 12.5)

print(rose.flower_price)
print(rose.number_of_petals)
print(rose.set_name)
rose.flower_price = 30
print(rose.flower_price)

print(iris.set_name)
print(iris.number_of_petals)
iris.number_of_petals = 8
print(iris.number_of_petals)
print(iris.flower_price)
