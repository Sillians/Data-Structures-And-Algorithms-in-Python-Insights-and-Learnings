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
            # return self._balance


pcc = PredatoryCreditCard("Dorcas Mark", "CitiBankPLC", "8753 9834 65750 2453", 15000, 5)
pcc.charge(20000)
print(pcc.get_balance())