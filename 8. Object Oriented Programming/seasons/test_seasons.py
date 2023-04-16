import pytest
from seasons import minutes_alive, minutes_to_words


def test_valid_minutes_alive():
    assert minutes_alive("2023-01-01") == 96480
    assert minutes_alive("2000-01-01") == 12193920


def test_invalid_minutes_alive():
    with pytest.raises(SystemExit) as e:
        for s in ["2050-01-01",
                  "2050-1-1",
                  "cat",
                  "01/01/2020"]:
            minutes_alive(s)
            assert e.type == SystemExit
            assert e.value.code == 1


def test_valid_minutes_to_words():
    assert minutes_to_words(312) == "Three hundred twelve minutes"
    assert minutes_to_words(5125612) == "Five million, one hundred twenty-five thousand, six hundred twelve minutes"


def test_invalid_minutes_to_words():
    assert minutes_to_words(312) != "Three hundred and twelve"
    assert minutes_to_words(312) != "three hundred and twelve"
    assert minutes_to_words(312) != "three hundred and twelve minutes"
    assert minutes_to_words(312) != "Three hundred and twelve minutes"