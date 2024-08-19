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


if __name__ == "__main__":
    card = CreditCard('Jordan Clarkson', 'CitiBank', '6383 9846 2534 4942', 2000)
    # card.charge(5000)


    # wallet = []
    # wallet.append(CreditCard('Rubin Richard', 'CitiBank', '6477 2537 9484 2927', 1500))
    # wallet.append(CreditCard('John Hopkins', 'Access bank', '7575 3839 2453 2964', 2500))
    # wallet.append(CreditCard('Luke Mick', 'Bank of America', '7554 2839 8293 2948', 3500))
    #
    # for val in range(1, 20):
    #     wallet[0].charge(val)
    #     wallet[1].charge(2*val)
    #     wallet[2].charge(3*val)
    #
    # for c in range(3):
    #     print('Customer =', wallet[c].get_customer())
    #     print('Bank =', wallet[c].get_bank())
    #     print('Account Number =', wallet[c].get_account())
    #     print('Limit =', wallet[c].get_limit())
    #     print('Balance =', wallet[c].get_balance())
    #     while wallet[c].get_balance() > 100:
    #         wallet[c].make_payment(100)
    #         print('New balance =', wallet[c].get_balance())
    #     print()



# cc = CreditCard('Rubin Richard', 'CitiBank', '6477 2537 9484 2927', 1500)
# print(cc.get_limit())
