from food import Food


class Sausage(Food):

    name = 'Tasty sausage'

    def __init__(self, price):

        self.price = price
        self.class_name = 'Sausage'
