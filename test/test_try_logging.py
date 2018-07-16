import pythonic_travis_coveralls.try_logging as try_logging

o1 = try_logging.C1(1)


def test1():
    assert o1.value == 1


def test2():
    assert o1() == 2


