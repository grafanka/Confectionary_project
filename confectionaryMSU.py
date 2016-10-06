from confectionary import Confectionary


class ConfectionaryMSU(Confectionary):

    def __init__(self, name):
        # Creates ConfectionaryMSU object called <name> with standart lists of foods and prices

            self.name = name

            self.cakes = {'Cheesecake': 500, 'Cherry Pie': 400, 'Strudel': 300}

            self.candies = {'Caramel candie': 10}

            self.fillings = {'Chocolate topping': 200, 'Marzipan topping': 250, 'Nuts': 200}

            self.tea = {'Tea': 30}

            self.sausage = {'Sausage': 60}


