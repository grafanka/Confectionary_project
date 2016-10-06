from sweets import Sweets


class Cake(Sweets):

    name = ''
    base_price = 0
    fillings = {}
    price = ''

    def __init__(self, cake, fillings):

        self.name = list(cake.keys())[0]

        self.base_price = cake[self.name]

        self.fillings = list(fillings.keys())

        self.price = self.base_price + sum( fillings.values())

        self.class_name = 'Cake'

    def __repr__(self):

        return '# Cake: "{0}". Price: {1}. Fillings: {2}.'.format(self.name, self.price, self.fillings)