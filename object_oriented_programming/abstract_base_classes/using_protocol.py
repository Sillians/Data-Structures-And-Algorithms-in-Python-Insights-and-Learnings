from typing_extensions import Protocol

class AbstractClassExample(Protocol):

    def do_something(self):
        print("Here is a sample implementaion!")

    def do_another_thing(self):
        ...

class AnotherSubClass(AbstractClassExample):

    def do_something(self):
        super().do_something()
        print("Here is another implementation in Production.")

x = AnotherSubClass()
x.do_something()