from jar import Jar
import pytest


def test_init():
    jar = Jar()
    assert jar.capacity == 12
    jar = Jar(3)
    assert jar.capacity == 3
    jar = Jar(0)
    assert jar.capacity == 0
    with pytest.raises(ValueError):
        for i in [-1, 1.1, -2.2, "", "cat"]:
            jar = Jar(i)


def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"


def test_deposit():
    jar = Jar()
    jar.deposit(0)
    jar.deposit(1)
    jar.deposit(11)
    with pytest.raises(ValueError):
        jar.deposit(1)
    jar = Jar(1)
    jar.deposit(1)

    with pytest.raises(ValueError):
        for i in [-10, 10, 1.1, -1.1, "1", "", "-1", "cat"]:
            jar = Jar(5)
            jar.deposit(i)


def test_withdraw():
    jar = Jar()
    jar.withdraw(0)
    jar.deposit(12)
    jar.withdraw(1)
    jar.withdraw(2)
    jar.withdraw(3)
    jar.withdraw(6)

    with pytest.raises(ValueError):
        for i in [-10, 10, 1.1, -1.1, "1", "", "-1", "cat"]:
            jar = Jar(5)
            jar.deposit(5)
            jar.withdraw(i)
