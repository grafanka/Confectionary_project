from itertools import groupby

from discount import Discount


class Order:

    def __init__(self, name, list, reg_cust):
        """Creates order with object from <list>"""

        self.group_func = self.group_by_all             # select function defining identity of objects

        self.name = name                                # name of person
        self.reg_cust = reg_cust                        # is he regular customer?

        self.list = self.group_func(list)               # creature list of list with identical objects

        self.dictionary = self.make_price_dictionary(self.list)             # data structure of <self.list> for
                                                                            # visualization

        self.summ = sum([sum([y.price for y in x]) for x in self.list])     # sum of order without discount

        self.discount = Discount(self)

        self.new_summ = self.discount.order_sum         # sum of order with discount


    def __repr__(self):

        s = '# Order by {0}:\n{1}\n'.format(self.name, self.discount.name)
        i = 1

        names = self.dictionary.keys()

        for x in names:

                s += '{0}. {1} - {2} pcs. Price: {3}.\n'.format(str(i), x, len(self.dictionary[x]), \
                                                                sum(self.dictionary[x]))
                i += 1

        s += 'Sum - {0}, with discount - {1}.'.format(str(self.summ), str(self.new_summ))

        return s

    def group_by_all(self, list):
        """Returns list of list with absolute identical objects grouped in sublists"""

        list.sort(key=lambda x: str(x.__dict__))

        one_group = []
        group_list = []

        for key, group in groupby(list, lambda x: str(x.__dict__)):

            for thing in group:
                one_group.append(thing)

            group_list.append(one_group)

            one_group = []

        return group_list

    def group_by_type(self, list):
        """Returns list of list with identical by type objects grouped in sublists"""

        list.sort(key=lambda x: str(type(x)))

        one_group = []
        group_list = []

        for key, group in groupby(list, lambda x: str(type(x))):

            for thing in group:
                one_group.append(thing)

            group_list.append(one_group)

            one_group = []

        return group_list

    def make_price_dictionary(self, list):
        """Returns {name of object: [<price>, <price>, ...}. <list> are list of objects."""

        dictionary = {}

        for x in list:

           dictionary.update({'{0} "{1}"'.format(x[0].class_name, x[0].name): [y.price for y in x]})

        return dictionary

