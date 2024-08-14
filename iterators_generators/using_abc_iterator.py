from collections.abc import Iterator, Iterable
class UsingABCSequenceIterator(Iterator):
    def __init__(self, sequence: Iterable):
        self._sequence = sequence
        self._index = 0

    def __next__(self):
        if self._index < len(self._sequence):
            item = self._sequence[self._index] * 3
            self._index += 1
            return item
        else:
            raise StopIteration

if __name__ == "__main__":
    for number in UsingABCSequenceIterator([1, 2, 3, 4]):
        print(number)
