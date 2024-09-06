class Base:

    def publ(self):
        print("This is a public method")

    def __priv(self):
        print("This is a private method")

class DerivedClass(Base):
    def __init__(self):
        Base().__init__()

    def cal_pub(self):
        print("\nInside the derived class")
        self.publ()

    def cal_priv(self):
        self.__priv()


out = Base()
out.publ()
out.__priv()

driv = DerivedClass()
driv.cal_pub()
driv.__priv()


# To call the private method outside the class we have a way that is by using the public method.

class NewBase:

    def pub(self):
        print("This is a new public method")

    def __priv(self):
        print("This is a new private method")

    def calling_priv(self):
        self.pub()
        self.__priv()

nb = NewBase()
nb.pub()
nb.calling_priv()
















