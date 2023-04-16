from twttr import shorten

def test_twttr():
    assert shorten("twitter") == "twttr"
    assert shorten("HELLO") == "HLL"
    assert shorten("oh no, what a shame!") == "h n, wht  shm!"
    assert shorten("aeiou") == ""
    assert shorten("CS50P") == "CS50P"
    assert shorten("123") == "123"
    assert shorten("") == ""
