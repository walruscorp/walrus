from walrus.api import get_capital


def test_capital():
    assert get_capital("Australia") == "Canberra"
