from abc import ABC, ABCMeta, abstractmethod

class AbstractClassExample(ABC):

    def __init__(self, value):
        self.value = value
        super().__init__()

    @abstractmethod
    def do_something(self):
        pass


class DoAdd42(AbstractClassExample):

    def do_something(self):
        return self.value + 48

class DoMul42(AbstractClassExample):

    def do_something(self):
        return self.value * 50




x = DoAdd42(4)
y = DoMul42(5)

print(x.do_something())
print(y.do_something())