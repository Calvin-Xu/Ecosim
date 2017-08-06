from ecosim.resources import *

test = Resources(100, 10, 10)

def test_grow():
    test.grow()
    assert test.amount == 110

def test_deplete():
    test.deplete()
    assert test.amount == 100

def test_check():
    test.deplete()
    assert test.check() == 'gone'
