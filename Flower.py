class Flower:

    def __init__(self, name, numPetals, price):

        self._name = name
        self._numPetals = numPetals
        self._price = price

        def get_name(self):
            return self._name

        def get_numPetals(self):
            return self._numPetals

        def get_price(self):
            return self._price

        def set_name(self, new_name):
            self._name = new_name

        def set_numPetals(self, new_petals):
            self._numPetals = new_petals

        def set_price(self, new_price):
            self._price = new_price