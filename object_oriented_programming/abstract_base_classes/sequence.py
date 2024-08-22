from abc import ABC, ABCMeta, abstractmethod

class Sequence(metaclass=ABCMeta):
    """Our own version of collections.Sequence abstract base class."""

    @abstractmethod
    def __len__(self):
        """Return the length of the sequence."""

    @abstractmethod
    def __getitem__(self, item):
        """Return the element at index item of the sequence."""

    def __contains__(self, item):
        """Return True if item found in the sequence; False otherwise."""
        for j in range(len(self)):
            if self[j] == item:
                return True
        return False

    def index(self, item):
        """Return leftmost index at which item is found (or raise ValueError)."""
        for j in range(len(self)):
            if self[j] == item:
                return j
        raise ValueError("value not in Sequence")

    def count(self, item):
        """Return the number of elements equal to given value"""
        k = 0
        for j in range(len(self)):
            if self[j] == item:
                k += 1
        return k


# class Range(Sequence):
#     pass