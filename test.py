from CreditCard import CreditCard

def check_account(cc):
    print()
    print("Account Name:", cc.get_customer())
    print("Bank:", cc.get_bank())
    print("Account Number:", cc.get_account())
    print("Balance:", cc.get_balance())
    print("Account Limit:", cc.get_limit())
    print()

if __name__ == "__main__":

    # Card instance with no initial balance
    card = CreditCard("Chezka", "WF", "1111 2222 3333 4444", 10000)

    # Card instance with initial balance
    card_init_balance = CreditCard("Franchezka", "WF", "1234 1234 1234 1234", 10000, 500)

    # Check account information of both accounts
    check_account(card)
    check_account(card_init_balance)

    # Making valid payment
    card_init_balance.make_payment(135)
    check_account(card_init_balance)

    # Making negative payment. Should throw a ValueError
    card_init_balance.make_payment(-1)