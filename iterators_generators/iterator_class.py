from sequence_iter import SequenceIterator
from square_iter import SquareIterator

for item in SequenceIterator([3, 4, 5, 6, 7, 8]):
    print(f"The iterator items are {item}")

for square in SquareIterator([3, 4, 5, 6, 7, 8]):
    print(f"The squared values are {square}")

