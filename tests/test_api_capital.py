import pytest
from walrus.api import get_capital


def test_capital_correct():
    assert get_capital("Australia") == "Canberra"
    assert get_capital("Australia", raise_errors=True) == "Canberra"


def test_capital_incorrect():
    assert get_capital("Austraalia") is None
    with pytest.raises(ValueError, match=("No data found for country: Austraalia")):
        get_capital("Austraalia", raise_errors=True)
