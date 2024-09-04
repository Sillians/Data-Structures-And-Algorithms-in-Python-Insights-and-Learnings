# In Section 2.3.5, we note that our version of the Range class has implicit support for iteration,
# due to its explicit support of both __len__ and __getitem__.
# The class also receives implicit support of the Boolean test, “k in r” for Range r.
# This test is evaluated based on a forward iteration through the range,
# as evidenced by the relative quickness of the test 2 in Range(10000000) versus 9999999 in Range(10000000).
# Provide a more efficient implementation of the __contains__ method to
# determine whether a particular value lies within a given range.
# The running time of your method should be independent of the length of the range.


class Range:
    """A class that mimic s the built-in range class."""

    def __init__(self, start: int, stop=None, step=1) -> None:
        """Initialize a Range instance.

        Semantics is similar to built-in range class.
        """
        if step == 0:
            raise ValueError('step cannot be zero')

        if stop is None: # special case of range(n
            start, stop = 0, start # should be treated as if range(0, n

        # calculate the effective length once
        self._length = max(0, (stop - start + step - 1) // step)

        self._start = start
        self._stop = stop
        self._step = step

    def __len__(self):
        """Return number of entries in the range."""
        return self._length

    def __getitem__(self, item):
        """Return entry at index k (using standard interpretation if negative)."""
        if item < 0:
            item += len(self)   # # attempt to convert negative index

        if not 0 <= item < self._length:
            raise IndexError('index out of range')

        return self._start + item * self._step

    def __contains__(self, item):
        if item < 0:
            item += len(self)

        if self._start <= item < self._stop and (item - self._start) % self._step == 0:
            return True
        return False


range_ = Range(1, 5)
for i in range_:
    print(i)

print(range_[-3])
print(8 in Range(8))

print(2 in Range(10000000))
print(9999999 in Range(10000000))