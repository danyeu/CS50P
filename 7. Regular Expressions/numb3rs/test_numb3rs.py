from numb3rs import validate


def test_valid():
    for ip in ["0.0.0.0",
               "0.1.23.245",
               "233.1.23.255",
               "1.2.3.4",
               "22.22.22.22",
               "222.222.222.222"]:
        assert validate(ip)


def test_invalid():
    for ip in ["1.22.333.4444",
               "255.255.255.256",
               "123-1-1-1",
               "dog",
               "1.2.3.4.5",
               "4.2.3",
               "22.222",
               "333.2.1",
               "1",
               "",
               "A.B.C.D",
               "A-B-C-D",
               ".",
               "...."]:
        assert not validate(ip)