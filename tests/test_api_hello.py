from walrus.api import hello


def test_hello():
    assert hello() == "Hello World"
