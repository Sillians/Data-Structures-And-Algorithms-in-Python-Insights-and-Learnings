from progression import Progression

class FibonacciProgression(Progression):
    
    def __init__(self, current_value=0, next_value=1):
        super().__init__(current_value)
        self._prev = next_value - current_value

    def _advance(self):
        self._prev, self._current = self._current, self._prev + self._current

FibonacciProgression(4, 6).make_progression(10)