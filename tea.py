from food import Food


class Tea(Food):

    name = 'Cup of tea'

    def __init__(self, price):

        self.price = price
        self.class_name = 'Tea'
