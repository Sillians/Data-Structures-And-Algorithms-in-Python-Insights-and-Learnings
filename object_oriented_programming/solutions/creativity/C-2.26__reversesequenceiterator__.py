# The SequenceIterator class of Section 2.3.4 provides what is known as a forward iterator.
# Implement a class named ReversedSequenceIterator that serves as a reverse iterator for any Python sequence type.
# The first call to next should return the last element of the sequence,
# the second call to next should return the second-to-last element, and so forth.


class ReversedSequenceIterator:
    """This class serves as a reverse iterator for any Python sequence type"""

    def __init__(self, sequence: list) -> int:
        """Create an iterator for the given sequence"""
        self._seq = sequence
        self._index = 0
        # self._index = len(sequence)

    def __len__(self):
        return len(self._seq)

    def __iter__(self):
        """By convention, an iterator must return itself as an iterator."""
        return self

    def __next__(self):
        """First call returns the last element and second call returns the second-to-last element, and so-forth"""
        self._index += -1
        if len(self._seq) > 1:
            return self._seq[self._index]
        else:
            raise StopIteration()

    # def __next__(self):
    # """First call returns the last element and second call returns the second-to-last element, and so-forth"""
    #     self._index -= 1
    #     if 0 <= self._index < len(self._seq):
    #         return (self._seq[self._index])
    #     else:
    #         raise StopIteration()

# sequence = [4, 2, 3]
sequence = [4, 6, 7, 8, 9, 2, 3]
seq_ = ReversedSequenceIterator(sequence)
print(next(seq_))
print(next(seq_))
print(next(seq_))
print(next(seq_))
print(next(seq_))
print(next(seq_))
print(next(seq_))