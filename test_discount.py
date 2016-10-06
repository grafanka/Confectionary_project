import unittest

from discount import Discount
from confectionaryMSU import ConfectionaryMSU
from person import Person


class TestSelectionDiscount(unittest.TestCase):
    """tests for function <Discount.do_discount>, check that with function selects and makes the best discount"""

    def setUp(self):

        self.conf = ConfectionaryMSU('conf MSU #1')
        self.person_regular = Person('Test person', True)
        self.person_not_regular = Person('Test person')

    def test_do_discount_regular_1(self):

        order = self.person_regular.do_order([self.conf.make_sausage()])
        d = Discount(order)

        self.assertEqual(d.do_discount(), [order.new_summ, 'discount {0}% for regular customer' \
                         .format(d.regular_percent)])

    def test_do_discount_same_1(self):

        order = self.person_regular.do_order([self.conf.make_sausage() for x in range(10)])
        d = Discount(order)

        self.assertEqual(d.do_discount(), [order.new_summ, 'discount {0} % at more than {1} same goods'\
                         .format(d.same_numbers_percent, d.same_numbers)])

    def test_do_discount_no_1(self):

        order = self.person_not_regular.do_order([self.conf.make_sausage() for x in range(9)]+[self.conf.make_tea()])

        d = Discount(order)

        self.assertEqual(d.do_discount(), [order.summ, 'order without discount'])

    def test_do_discount_same_2(self):

        order = self.person_not_regular \
            .do_order([self.conf.make_cake('Cheesecake', []) for x in range(9)]+ \
                      [self.conf.make_cake('Cheesecake', ['Nuts'])])

        d = Discount(order)

        self.assertLessEqual(d.do_discount(), [order.new_summ, 'discount {0} % at more than {1} same goods'\
                             .format(d.same_numbers_percent, d.same_numbers)])

    def test_do_discount_same_3(self):

        order = self.person_regular.do_order([self.conf.make_cake('Cheesecake', []) for x in range(10)])

        d = Discount(order)

        self.assertEqual(d.do_discount(), [order.new_summ, 'discount {0} % at more than {1} same goods'\
                             .format(d.same_numbers_percent, d.same_numbers)])


class TestCalculationDiscount(unittest.TestCase):

    def setUp(self):

        self.conf = ConfectionaryMSU('Test confectionary')
        self.person = Person('Test person')
        self.order = self.person.do_order([])
        # self.discount = Discount(self.order)

    def test_to_all_1(self):

       self.order.summ = 100

       self.assertEqual(Discount.to_all(self.order,0.1), 99.9)

    def test_to_all_2(self):

       self.order.summ = 0

       self.assertEqual(Discount.to_all(self.order,50), 0)

    def test_to_same(self):

        order = self.person.do_order([self.conf.make_sausage() for x in range(10)]+[self.conf.make_caramels(50)])

        self.assertNotEqual(order.new_summ, Discount.to_all(order, order.discount.same_numbers_percent))