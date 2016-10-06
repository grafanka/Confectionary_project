from confectionaryMSU import ConfectionaryMSU
from person import Person
import copy


def main():

    my_conf = ConfectionaryMSU('conf MSU #1')

    box_1 = my_conf.make_caramels(17)

    cake_1 = my_conf.make_cake('Cheesecake', ['Nuts', 'Marzipan topping'])
    cake_2 = my_conf.make_cake('Cheesecake', ['Marzipan topping', 'Nuts'])
    cake_3 = my_conf.make_cake('Cherry Pie', [])
    sausage_1 = my_conf.make_sausage()
    tea_1 = my_conf.make_tea()
    sausages = [my_conf.make_sausage() for x in range(11)]
    cakes = [my_conf.make_cake('Cheesecake', ['Nuts', 'Marzipan topping']) for x in range(10)]

    person_1 = Person('Maria')
    order_1 = person_1.do_order([sausage_1, cake_3, box_1, tea_1, cake_1, cake_2]+sausages+cakes)
    print(repr(order_1))

    print()

    person_2 = Person('Joseph')
    order_2 = person_2.do_order([sausage_1, cake_1, cake_2])
    print(repr(order_2))


if __name__ == '__main__':
        main()
