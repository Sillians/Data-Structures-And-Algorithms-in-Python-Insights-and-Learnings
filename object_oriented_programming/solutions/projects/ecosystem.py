# Write a Python program to simulate an ecosystem containing two types of creatures, bears and fish.
# The ecosystem consists of a river, which is modeled as a relatively large list.
# Each element of the list should be a Bear object, a Fish object, or None. In each time step,
# based on a random process, each animal either attempts to move into an adjacent list location or stay where it is.
# If two animals of the same type are about to collide in the same cell,
# then they stay where they are, but they create a new instance of that type of animal,
# which is placed in a random empty (i.e., previously None) location in the list.
# If a bear and a fish collide, however, then the fish dies (i.e., it disappears).


- Ecosystem
- Creatures
    - Bears
        - Move into an adjacent list location or stay where it is
    - Fish
        - Move into an adjacent list location or stay where it is

- River
    - Large List
        - Bear object
        - Fish object
        - None

- If a bear and a fish collide, then the fish dies (disappears)


class Bears:
    def __init__(self):
        pass



class Fish:
    def __init__(self):
        pass

