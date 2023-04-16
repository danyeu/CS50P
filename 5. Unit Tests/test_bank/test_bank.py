from bank import value


def test_hello():
    for greeting in ["Hello", "hello, world!", "HELLO DANIEL", "hello 123!", " hELLo "]:
        assert value(greeting) == 0


def test_h():
    for greeting in ["HI!", "hey", "How are you?", " h3Y!!!", " h "]:
        assert value(greeting) == 20


def test_other():
    for greeting in ["", " ", "yo", "Welcome!", "NICE TO SEE YOU!", "5h"]:
        assert value(greeting) == 100