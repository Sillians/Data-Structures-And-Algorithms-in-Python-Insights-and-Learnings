
class Progression:

    def __init__(self, start=0) -> None:
        self._current = start

    def _advance(self):
        self._current += 1

    def __next__(self):
        if self._current is None:
            raise StopIteration("Out nof bounds!")
        else:
            answer = self._current
            self._advance()
            return answer

    def __iter__(self):
        return self

    def make_progression(self, n):
        print(' '.join(str(next(self)) for j in range(n)))


# Write a Python class that extends the Progression class so that each
# value in the progression is the square root of the previous value.
# (Note that you can no longer represent each value with an integer.)
# Your constructor should accept an optional parameter specifying the start value, using 65,536 as a default.


class SquareProgressionExtension(Progression):

    def __init__(self, start_value=65536):
        super().__init__()
        self._current = start_value

    def __next__(self):
        answer = self._current
        self._current =  self._current ** (1/2)
        return answer

    def __getitem__(self, item):
        return self._current**(1/(2**item))


if __name__ == "__main__":
    Progression(2).make_progression(10)
    prog = SquareProgressionExtension()

    for i in range(10):
        print("The value at {} is {}".format(i+1, prog[i]))

    prog.make_progression(10)