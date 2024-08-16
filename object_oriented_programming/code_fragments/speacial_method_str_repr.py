class Product:
    def __init__(self, name: str, price: float) -> str:
        self._name = name
        self._price = price

    def __str__(self):
        return f"Product: name: {self._name} and price: {self._price}" # <-- user friendly

    def __repr__(self):
        return f"Product: {self._name}, {self._price}" # <-- developers friendly

# create an instance of the product
prod = Product('Apple MackBook M3', 3599.99)

# Using print() or str() calls __str__()
print(prod)

# Using repr() or printing in the console calls __repr__()
print(repr(prod))