from plates import is_valid


def test_valid():
    for plate in ["AB", "CDE", "FGHI", "JKLMN", "OPQRST", "UV1", "WXY2", "ZABC3", "DEFGH4", "IJK5", "LMNO6", "PQRST7", "UVWX8", "YZABC9", "DEFGHI", "JK10", "LM999", "NO8765", "PQR123", "STUV44", "WXYZA8", "AB10000"]:
        assert is_valid(plate)


def test_valid():
    for plate in ["B2B", "ABCD02", "2FAST", "GO4IT", "NEVER!", "X", "A B", "WHY?", "294123", "5", "TOOLONG", "FIVE55555", "R4030", "?ER34"]:
        assert not is_valid(plate)