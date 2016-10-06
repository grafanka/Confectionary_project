class Food:

    name = ''       # name/kind of food
    price = 0       # total coast of object
    disc_mark = False

    def __init__(self, name, price):

        self.name = name
        self.price = price

    def __repr__(self):

        return '# Name: "{0}". Price: {1}.'.format(self.name, self.price)

