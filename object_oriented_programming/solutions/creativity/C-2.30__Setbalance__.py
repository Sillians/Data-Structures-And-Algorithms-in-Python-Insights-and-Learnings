# At the close of Section 2.4.1, we suggest a model in which the CreditCard class supports a nonpublic method,
# _set_balance(b), that could be used by subclasses to affect a change to the balance, without directly accessing
# the balance data member. Implement such a model, revising both the CreditCard and PredatoryCreditCard classes accordingly.

from creditcard import CreditCard

class PredatoryCreditCard(CreditCard):

    def __init__(self, customer: str, bank: str, acnt: str, limit: float, apr: float):
        super().__init__(customer, bank, acnt, limit)
        self._apr = apr

    def charge(self, price: float):
        success = super().charge(price)
        if not success:
            super()._set_balance(super().get_balance() + 5)
        return success

    def process_month(self):
        if self._balance > 0:
            monthly_factor = pow(1 + self._apr, 1/12)
            # monthly_factor = (1+self._apr)**(1/12)
            self._balance *= monthly_factor
            return self._balance


pcc = PredatoryCreditCard("Dorcas Markson", "CitiBank PLC", "8753 9334 6575 2453", 15000, 5)
pcc.charge(20000)
print(pcc.get_balance())
print(pcc.process_month())

# pcc.charge(20)
# print(pcc.get_balance())