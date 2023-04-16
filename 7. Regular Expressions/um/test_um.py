from um import count


def test_valid():
    assert count("Um, hi") == 1
    assert count("Hello, um, world!") == 1
    assert count("Um, no, um, thanks") == 2
    assert count("Wrong number, um, sorry") == 1
    assert count("Um, no, um, the umpire said, um, out! Um, sorry.") == 4
    assert count("um") == 1
    assert count("Um um um um") == 4
    assert count("Um, uhhhhhhhm, um, yeah") == 2


def test_invalid():
    for s in ["number",
            "Mum's number is 123",
            "Umpire",
            "uhm, no",
            "ummm, umm, uhm",
            "cat"]:
        assert count(s) == 0