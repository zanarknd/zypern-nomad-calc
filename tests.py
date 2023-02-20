import pytest

from calculator import calculate_income_tax


@pytest.mark.parametrize(
    "total, expected",
    (
        (19_500, 0),
        (28_000, 1700),
        (36_300, 3775),
        (60_000, 10885),
        (65_000, 10885 + 1750),
    ),
)
def test_calculate_yearly(total, expected):
    result, _ = calculate_income_tax(total)
    assert result == expected


@pytest.mark.parametrize(
    "total, salary, expected",
    (
        (19_500, 100, 0),
        (28_000, 100, 20),
        (36_300, 100, 25),
        (60_000, 100, 30),
        (60_100, 100, 35),
    ),
)
def test_calculate_monthly(total, salary, expected):
    _, result = calculate_income_tax(total, salary)
    assert result == expected
