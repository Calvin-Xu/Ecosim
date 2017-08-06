from ecosim.creatures import *

test = Creatures(1, 10, 10 , 5)
stuff = Sheep(100, 10, 10 , 5)

def test_consume():
    assert stuff.amount == 100
    test.consume(stuff, 10)
    assert stuff.amount == 90

def test_hunt():
    assert stuff.amount == 90
    test.hunt(stuff)
    assert stuff.amount == 85
