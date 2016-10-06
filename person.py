from order import Order


class Person:

    name = ''
    reg_cust = False

    def __init__(self, name, reg_cust = False):

        self.name = name

        self.reg_cust = reg_cust


    def do_order(self, list):

        return Order(self.name, list, self.reg_cust)
