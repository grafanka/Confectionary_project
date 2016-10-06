class Discount:

    def __init__(self, order):

        self.order = order

        self.big_summ = 2000
        self.big_summ_percent = 5

        self.same_numbers = 10              # discount <same_numbers_percent> % at more than <same_numbers> same goods
        self.same_numbers_percent = 10

        self.regular_percent = 5            # discount <regular_percent> % for regular customer

        discount = self.do_discount()

        self.order_sum = discount[0]
        self.name = discount[1]



    @staticmethod

    def to_all(order, percent):
        # Returns sum of <order> with discount <percent> %

        new_summ = (100 - percent) / 100 * order.summ

        return new_summ

    def to_regular(self, order, percent):
            # Returns list [,] : [sum of <order> with discount for regular costumer, 'name of discount']
        if order.reg_cust is True:

            new_summ = Discount.to_all(order, percent)

            return [new_summ, 'discount {0}% for regular customer'.format(self.regular_percent)]
        else:
            return [90000000, '']

    def to_big_sum(self, order, percent):
        # Returns list [,] : [sum of <order> with discount for big order, 'name of discount']

        if order.summ >= self.big_summ:

            new_summ = Discount.to_all(order, percent)

            return [new_summ, 'discount  {0}% at more than {1} order'.format(self.big_summ_percent, self.big_summ)]
        else:
            return [900000000, '']

    def to_same(self, order, numbers, percent):
        # Returns list [,] : [sum of <order> with discount for <numbers> same goods, 'name of discount']

        new_summ = 0

        for x in order.list:

            if len(x) >= numbers:
                new_summ += (100 - percent) / 100 * sum([y.price for y in x])
            else:
                new_summ += sum([y.price for y in x])

        return [new_summ, 'discount {0} % at more than {1} same goods'.format(self.same_numbers_percent, \
                                                                              self.same_numbers)]

    def no_discount(self, order):

        return [order.summ, 'order without discount']

    def do_discount(self):
        """Returns the best discount function for order <self.order>"""

        order = self.order

        functions = [self.no_discount(order), self.to_same(order, self.same_numbers, self.same_numbers_percent), \
                     self.to_regular(order, self.regular_percent), self.to_big_sum(order, self.big_summ_percent)]
        # list of all discount functions

        new_sums = [x[0] for x in functions]
        i = new_sums.index(min(new_sums))           # selection of the best discount function

        return functions[i]