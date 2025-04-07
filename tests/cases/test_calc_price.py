import pytest

from cases.calc_price import calc_price


def test_calc_price():
    total, minimum, recommended = calc_price(60, "футбОлкА")

    assert isinstance(total, float)
    assert minimum == round(total * 1.7, 2)
    assert recommended == round(total * 2.5, 2)


def test_calc_price_invalid_cloth_type_raises_key_error():
    with pytest.raises(KeyError):
        calc_price(60, "чфутболка")
