class CreditCard:

    def __init__(self, customer, bank, acnt, limit, balance = 0):

        self._customer = customer
        self._bank = bank
        self._account = acnt
        self._limit = limit
        self._balance = balance

    def get_customer(self):
        return self._customer

    def get_bank(self):
        return self._bank

    def get_account(self):
        return self._account

    def get_limit(self):
        return self._limit

    def get_balance(self):
        return self._balance

    def charge(self, price):
        if price + self._balance > self.limit:
            return False
        else:
            self._balance += price
            return True

    def make_payment(self, amount):
        if amount >= 0 and self._balance-amount >= 0:
            self._balance -= amount
            print("Payment successful!")
            print("New balance is", self._balance)
        else:
            raise ValueError('Invalid amount entered')

    def to_string(self):
        str_cc = "Customer:" + self._customer + "\n"
        str_cc += "Bank:" + self._bank + "\n"
        str_cc += "Account Number:" + self._account + "\n"
        str_cc += "Balance:" + str(self._balance) + "\n"
        str_cc += "Account Limit:" + str(self._limit) + "\n"

        return str_cc