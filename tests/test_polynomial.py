import pytest

from base.base import Monomial, MonomialSign, Polynomial


@pytest.mark.parametrize(
    "polynomial,term1,term2,term3",
    [
        (
            Polynomial.from_string("2ab-2cd+2xy"),
            Monomial.from_string("2ab"),
            Monomial.from_string("-2cd"),
            Monomial.from_string("2xy"),
        ),
        (
            Polynomial.from_string("-2a^2b^3+2cd-2x^4y^5"),
            Monomial.from_string("-2a^2b^3"),
            Monomial.from_string("2cd"),
            Monomial.from_string("-2x^4y^5"),
        ),
    ]
)
def test_polynomial_is_correctly_parsed(polynomial, term1, term2, term3):
    assert polynomial.monomial_list[0] == term1
    assert polynomial.monomial_list[1] == term2
    assert polynomial.monomial_list[2] == term3
