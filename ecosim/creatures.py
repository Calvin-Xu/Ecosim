from resources import Resources

class Creatures(Resources):

    def __init__(self, amount, grow_rate, deplete_rate, hunt_rate):
        self.amount = amount
        self.grow_rate = grow_rate
        self.deplete_rate = deplete_rate
        self.hunt_rate = hunt_rate

    def consume(self, resource, rate):
        self.rate = int(rate) * self.amount

        if resource.amount - self.rate >= 0:
            resource.amount -= self.rate
        else:
            resource.amount = 0

    def hunt(self, prey):
        if prey.amount >= 0:
            self.consume(prey, self.hunt_rate)
            self.grow()
        else:
            pass


class Sheep(Creatures):

    def check(self):
        if self.amount <= 100:
            return 'gone'
        else:
            pass

class Wolf(Creatures):
    pass
