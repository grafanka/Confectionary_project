from collections import Counter


class CounterStr:

    def __init__(self, list):

        self.counter = Counter(list)

    def __repr__(self):

        s = repr(self.counter)
        s = s.replace('})', '')
        s = s.replace('Counter({', '')

        return s
