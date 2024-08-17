from typing import List

class SquareIterator:
    """An iterator that prints the square of given numbers"""

    def __init__(self, stop: int, start: int) -> int:
        self._stop = stop
        self._start = start

    def __iter__(self):
        return self

    def __next__(self):
        if self._start <= self._stop:
            result = self._start **2
            self._start += 1
            return result
        else:
            raise StopIteration


class SequenceIterator:
    """An iterator for any of Python's sequence types"""

    def __init__(self, sequence: list) -> int:
        """Create an iterator for the given sequence"""
        self._seq = sequence
        self._index = -1

    def __len__(self):
        return len(self._seq)

    def __iter__(self):
        """By convention, an iterator must return itself as an iterator."""
        return self

    def __next__(self):
        result = []
        for j in range(0, len(self._seq)):
            result.append(self._seq[self._index] ** 3)
            self._index -= 1
        return result





si = SquareIterator(8, 2)
for i in si:
    print(i)

sequence = [4, 6, 7, 8, 9, 2, 3]
seq = SequenceIterator(sequence)
print(next(seq))