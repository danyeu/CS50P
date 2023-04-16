import pytest
from working import convert


def test_valid():
    assert convert("12:05 AM to 5:50 AM") == "00:05 to 05:50"
    assert convert("1:01 AM to 2:23 PM") == "01:01 to 14:23"
    assert convert("4:00 PM to 12:11 PM") == "16:00 to 12:11"
    assert convert("1:59 PM to 1:01 PM") == "13:59 to 13:01"
    assert convert("2:42 AM to 7:14 AM") == "02:42 to 07:14"
    assert convert("12 AM to 5 AM") == "00:00 to 05:00"
    assert convert("2 AM to 1 PM") == "02:00 to 13:00"
    assert convert("11 PM to 9 PM") == "23:00 to 21:00"
    assert convert("12 PM to 12 AM") == "12:00 to 00:00"


def test_invalid():
    for s in ["13:05 AM to 1 AM",
            "12:61 AM to 1 AM",
            "cat",
            "111:11 AM to 1 AM",
            "1 AM to 14 PM",
            "0 AM to 1PM",
            "1 AM to 0 PM",
            "-1 AM to 1 PM",
            "1 AM to -2 PM",
            "1 AM - 2 PM",
            "1 AM 2 PM"
            "1 AM  2 PM"]:
        with pytest.raises(ValueError):
            convert(s)