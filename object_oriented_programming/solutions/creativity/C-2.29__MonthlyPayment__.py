# Modify the PredatoryCreditCard class from Section 2.4.1 so that a customer is assigned a minimum monthly payment,
# as a percentage of the balance, and so that a late fee is assessed if the customer
# does not subsequently pay that minimum amount before the next monthly cycle.

from creditcard import CreditCard

class PredatoryCreditCard(CreditCard):

    def __init__(self, customer: str, bank: str, acnt: str, limit: float, apr: float):
        super().__init__(customer, bank, acnt, limit)
        self._apr = apr

    def charge(self, price: float):
        success = super().charge(price)
        if not success:
            self._balance += 5
        return success

    def process_month(self):
        if self._balance > 0:
            monthly_factor = pow(1 + self._apr, 1/12)
            # monthly_factor = (1+self._apr)**(1/12)
            self._balance *= monthly_factor
            return self._balance


class PCCMonthlyPayment(PredatoryCreditCard):
    LATE_FEE = 15
    MINIMUM_PCT = 0.05

    def __init__(self, customer: str, bank: str, acnt: str, limit: float, apr: float):
        super().__init__(customer, bank, acnt, limit, apr)
        self._minimum_payment = 0

    def process_month(self):
        super().process_month()
        if self._minimum_payment > 0:
            self._balance += self.LATE_FEE
        if self._balance > 0:
            self._minimum_payment = self._balance * self.MINIMUM_PCT

    def make_payment(self, amount: int):
        super().make_payment(amount)
        self._minimum_payment = max(0, self._minimum_payment - amount)


pccm = PCCMonthlyPayment("Elekan Imolaniki", "TrustBank PLC", "3738 3038 2937 4520", 5000, 1.25)
pccm.charge(3000)
# pccm.charge(300)
pccm.process_month()
print(pccm.get_balance(), pccm._minimum_payment)

# pccm.process_month()
# print(pccm.get_balance(), pccm._minimum_payment)