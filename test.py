from CreditCard import CreditCard
from Flower import Flower


def test_flower_class(name, petals, price):
    # Tests the getters and setters for the Flower class
    new_flower = Flower(name, petals, price)
    print("Current Flower attributes:")
    print(new_flower.to_string())

    print("Getting class attributes using methods...")
    print("Getting name...\n" + new_flower.get_name())
    print("Getting number of petals...\n" + str(new_flower.get_numPetals()))
    print("Getting price...\n" + str(new_flower.get_price()) + "\n")

    print("Setting new attribute values...")
    print("Setting name to Blue Rose...")
    new_flower.set_name("Blue Rose")
    print("Setting number of petals to " + str(petals + 2) + " ...")
    new_flower.set_numPetals(petals + 2)
    print("Setting price to " + str(price + 0.5) + " ...\n")
    new_flower.set_price(price + 0.5)

    print("New Flower attibutes")
    print(new_flower.to_string())


def test_creditcard_class(cc, pay = 0):
    # Tests the CreditCard class

    print("Current CC details:")
    print(cc.to_string())

    print("Getting class attributes using methods...")
    print("Getting customer name...\n" + cc.get_customer())
    print("Getting bank...\n" + cc.get_bank())
    print("Getting accnt number...\n" + cc.get_account())
    print("Getting balance...\n" + str(cc.get_balance()))
    print("Getting limit...\n" + str(cc.get_limit()) + "\n")

    print("Making payment of " + str(pay) + "...")
    cc.make_payment(pay)


if __name__ == "__main__":

    test_flower_class("Rose", 20, 4)

    #Card instance with no initial balance
    card = CreditCard("Chezka", "WF", "1111 2222 3333 4444", 10000)
    test_creditcard_class(card)

    #Card instance with initial balance
    card_init_balance = CreditCard("Franchezka", "WF", "1234 1234 1234 1234", 10000, 500)
    test_creditcard_class(card_init_balance, -15)