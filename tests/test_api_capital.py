import pytest
from walrus.api import get_capital


def test_capital():
    assert get_capital("Australia") == "Canberra"
    assert get_capital("Austraalia") is None
    with pytest.raises(ValueError, match=(f"No data found for country: Austraalia")):get_capital("Austraalia", True)
