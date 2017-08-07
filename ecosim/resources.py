class Resources(object):

    def __init__(self, amount, grow_rate, deplete_rate):
        self.amount = int(amount)
        self.grow_rate = int(grow_rate)
        self.deplete_rate = int(deplete_rate)

    def grow(self):
        if self.amount + self.grow_rate <= 10000:
            self.amount += self.grow_rate
        elif self.amount + self.grow_rate >= 10000 and self.amount + self.grow_rate <= 1500:
            self.amount += int(self.grow_rate * 0.8)
        else:
            self.amount += int(self.grow_rate * 0.5)

    def deplete(self):
        if self.amount - self.deplete_rate >= 0:
            self.amount -= self.deplete_rate
        else:
            pass

    def check(self):
        if self.amount <= 100:
            return 'gone'
        else:
            pass


class Water(Resources):
    pass

class Grass(Resources):
    pass
