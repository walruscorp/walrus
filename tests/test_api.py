from walrus.api import hello, get_capital


def test_hello():
    assert hello() == "Hello World"


def test_capital():
    assert get_capital("Australia") == "Canberra"
