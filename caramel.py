import numpy

from sweets import Sweets


class Caramel(Sweets):

    kind = ''
    kind_list = ['strawberry', 'vanilla', 'chocolate']
    price = 0

    def __init__(self, price):

        self.kind = numpy.random.choice(self.kind_list)

        self.price = price

    def __repr__(self):

        return 'Name: Caramel. Kind: {0}. Price: {1}.'.format(self.kind, self.price)