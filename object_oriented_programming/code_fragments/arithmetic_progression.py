from progression import Progression

class ArithmeticProgression(Progression):      # inherit from Progression

    def __init__(self, increment=1, start=0):
        super().__init__(start)      # base class
        self._increment = increment

    def _advance(self):   # override inherited version
        self._current += self._increment

if __name__ == "__main__":
    ap = ArithmeticProgression(4, 2)
    ap.make_progression(10)
