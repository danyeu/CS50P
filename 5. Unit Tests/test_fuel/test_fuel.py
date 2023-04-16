import pytest
from fuel import convert, gauge


def test_convert_pass():
    assert convert("1/2") == 50
    assert convert("1/4") == 25
    assert convert("1/100") == 1
    assert convert("1/1000") == 0
    assert convert ("1/1") == 100
    assert convert("999/1000") == 100


def test_convert_fail():
    with pytest.raises(ValueError):
        for s in ["3/2", "-1/2", "1/-2", "A/B", "1.0/2", "1/2.0", " / ", "/", "1/A", "A/2"]:
            convert(s)
    with pytest.raises(ZeroDivisionError):
        for s in ["1/0", "5/0"]:
            convert(s)


def test_gauge_full():
    for i in [99, 100]:
        assert gauge(i) == "F"


def test_gauge_empty():
    for i in [0, 1]:
        assert gauge(i) == "E"


def test_gauge_pct():
    assert gauge(2) == "2%"
    assert gauge(98) == "98%"
    assert gauge(50) == "50%"
    assert gauge(12) == "12%"