from enum import Enum, IntEnum, Flag, auto

# class syntax
class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 5

print(Color.RED.name)
print(Color.GREEN.value)

# functional syntax
Color = Enum('Color', ['RED', 'GREEN', 'BLUE'])

class Number(IntEnum):
    ONE = 1
    TWO = 2
    THREE = 3

print(Number.THREE + Number.TWO)
print(Number.THREE == 3)


class NewColor(Flag):
    RED = auto()
    GREEN = auto()
    BLUE = auto()

purple = NewColor.RED | NewColor.BLUE
white = NewColor.RED | NewColor.BLUE | NewColor.GREEN

print(purple in white)
print(white in purple)


















