import pytest
from walrus.api import get_capital, get_capital_2


def test_capital_correct():
    assert get_capital("Australia") == "Canberra"
    assert get_capital("Australia", raise_errors=True) == "Canberra"


def test_capital_incorrect():
    assert get_capital("Austraalia") is None
    with pytest.raises(ValueError, match=("No data found for country: Austraalia")):
        get_capital("Austraalia", raise_errors=True)


def test_capital_2_correct():
    assert get_capital_2("Australia") == "Canberra"
    assert get_capital_2("Australia", raise_errors=True) == "Canberra"
    assert get_capital_2(("Australia", "France")) == {"Australia": "Canberra", "France": "Paris"}
    assert get_capital_2(("Australia", "France"), raise_errors=True) == {"Australia": "Canberra", "France": "Paris"}


def test_capital_2_incorrect():
    assert get_capital_2("Austraalia") is None
    assert get_capital_2(("Australia", "Fraance")) == {"Australia": "Canberra", "Fraance": None}
    with pytest.raises(ValueError, match=("No data found for country: Austraalia")):
        get_capital("Austraalia", raise_errors=True)
    with pytest.raises(ValueError, match=("No data found for country: Austraalia")):
        get_capital_2(("Austraalia", "France"), raise_errors=True)
