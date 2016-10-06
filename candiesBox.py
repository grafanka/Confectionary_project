from counterStr import CounterStr
from food import Food


class CandiesBox(Food):

    name = 'Candie Box'
    price = 0
    list = []
    disc_mark = False

    def __init__(self, box, price):
        # Create CandiesBox object with total coast (in field price)

        self.list = box
        self.price = price
        self.class_name = 'Candies box'

    def __repr__(self):

        kind_list = [x.kind for x in self.list]

        s = '# Name: Candies Box. Price: {0}.\nContains {1} caramels: {2}.' \
        .format(self.price, len(self.list), repr(CounterStr(kind_list)))

        return s
