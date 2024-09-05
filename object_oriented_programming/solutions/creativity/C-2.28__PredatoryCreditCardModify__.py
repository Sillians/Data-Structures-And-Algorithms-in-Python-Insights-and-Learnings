# The PredatoryCreditCard class of Section 2.4.1 provides a process month method that models the completion of a monthly cycle.
# Modify the class so that once a customer has made ten calls to charge in the current month,
# each additional call to that function results in an additional $1 surcharge.


from typing import Any

class CreditCard:
    """A consumer credit card."""

    def __init__(self, customer: str, bank: str, acnt: str, limit: float):
        """Create a new credit card instance

        The initial balance is zero

        customer: the name of the customer (e.g., 'John Kwame')
        bank: the name of the bank (e.g., 'California Savings')
        acnt: the account identifier (e.g., '5391 0375 9387 5309')
        limit: the credit limit (measured in dollars)
        """

        self._customer = customer
        self._bank = bank
        self._account = acnt
        self._limit = limit
        self._balance = 0

    def get_customer(self) -> Any:
        """Return the name of the customer"""
        return self._customer

    def get_bank(self) -> Any:
        """Return the bank's name"""
        return self._bank

    def get_account(self) -> Any:
        """Return the card identifying number (typically stored as a string"""
        return self._account

    def get_limit(self):
        """Return current credit limit"""
        return self._limit

    def get_balance(self):
        """Return current balance"""
        return self._balance

    def charge(self, price: float):
        """Charge given price to the card, assuming sufficient credit limit

        Return True if charge was processed; False if charge was denied.
        """
        if price + self._balance > self._limit:
            return False
        else:
            self._balance += price
            return True

    def make_payment(self, amount: float):
        """Process customer payment that reduces balance"""
        self._balance -= amount


class PredatoryCreditCard(CreditCard):
    MAX_CHARGES = 10
    def __init__(self, customer: str, bank: str, acnt: str, limit: float, apr: float):
        super().__init__(customer, bank, acnt, limit)
        self._apr = apr
        self._count = 0

    def charge(self, price: float):
        success = super().charge(price)
        if success:
            self._count+=1
        else:
            self._balance+=5
        return success

    def process_month(self):
        if self._balance > 0:
            # monthly_factor = (1+self._apr)**(1/12)
            monthly_factor = pow(1 + self._apr, 1/12)
            print("Balance before monthly factor: {}".format(self._balance))
            self._balance *= monthly_factor
            print("Balance after monthly factor: {}".format(self._balance))
            # return self._balance

        if self._count > self.MAX_CHARGES:
            self._balance+=(self._count - self.MAX_CHARGES)
            print("Balance after call count: {}".format(self._balance))


pcc = PredatoryCreditCard("Dorcas Mark", "CitiBankPLC", "8753 9834 65750 2453", 15000, 5)
for i in range(11):
    pcc.charge(1)

pcc.charge(2000)
pcc.process_month()
print(pcc.get_balance())