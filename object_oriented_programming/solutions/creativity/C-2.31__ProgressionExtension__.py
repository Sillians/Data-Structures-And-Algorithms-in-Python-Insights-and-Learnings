# Write a Python class that extends the Progression class so that each value in the progression
# is the absolute value of the difference between the previous two values. You should include
# a constructor that accepts a pair of numbers as the first two values, using 2 and 200 as the defaults.


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


class ProgressionExtension(Progression):

    def __init__(self, first_num=2, second_num=200):
        super().__init__(start=0)
        self._current = first_num
        self._prev = second_num + first_num


    def __next__(self):
        answer = self._current
        self._current, self._prev = abs(self._prev - self._current), self._current
        return answer



if __name__ == "__main__":
    Progression(2).make_progression(10)
    prog = ProgressionExtension()
    prog.make_progression(10)