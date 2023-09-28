from walrus.api import get_capital


def test_capital():
    assert get_capital("Australia") == "Canberra"
    assert get_capital("Austraalia") is None
