from cake import Cake
from candiesBox import CandiesBox
from sausage import Sausage
from tea import Tea
from caramel import Caramel


class Confectionary:

    name = ''

    cakes = {}          # confectionary can make only kinds of cake from this dictionary {name of cake : price, ...}

    fillings = {}       # confectionary can make any cake with any fillings from this dictionary
                        # {name of filling : price, ...}

    candies = {}        # confectionary can make only kinds of candy from this dictionary {name of candy : price, ...}


    def make_caramels(self, n):
        """Returns CandiesBox object which has list of Caramel objects with random kind.
        CandiesBox object has total price of all elements."""

        box = CandiesBox([],0)

        for i in range(n):

            box.list.append(Caramel(self.candies['Caramel candie']))

        box.price = self.candies['Caramel candie']*n

        return box

    def make_cake(self, cake_name, fillings):
        """Returns cake with fillings and calculated price. If it's impossible returns None and print error message."""

        if cake_name not in self.cakes:

            raise NameError('Confectionary {0} can not made this kind of cake.'.format(self.name))

        for x in fillings:

            if x not in self.fillings:

                raise NameError('Can not add {0} in this cake. '.format(x))

        cake_name = {cake_name: self.cakes[cake_name]}      # create dictionary {name of cake: base price}

        fillings = {x: self.fillings[x] for x in fillings}  # create dictionary for this cake:
                                                            # {filling_1 : price_1, filling_2 : price_2, ...}

        return Cake(cake_name, fillings)

    def make_sausage(self):
        """Returns Sausage object with price"""

        return Sausage(self.sausage['Sausage'])


    def make_tea(self):
        """Returns Tea object with price"""

        return Tea(self.tea['Tea'])

