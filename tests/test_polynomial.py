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


@pytest.mark.parametrize(
    "polynomial1,polynomial2",
    [
        (
            Polynomial.from_string("ab+a^2b+ab^2"),
            Polynomial.from_string("a^2b+ab^2+ab"),
        ),
    ]
)
def test_two_equal_polynomials_ordered_differently_are_the_same(polynomial1, polynomial2):
    assert polynomial1 == polynomial2


@pytest.mark.parametrize(
    "polynomial,result",
    [
        (
            Polynomial.from_string("a^2b+ab+a^3b^2"),
            Polynomial.from_string("ab+a^2b+a^3b^2"),
        ),
    ]
)
def test_order_polynomial_ascending(polynomial, result):
    assert polynomial.order_on('a', descending=False) == result


@pytest.mark.parametrize(
    "polynomial,result",
    [
        (
            Polynomial.from_string("ab+a^2b+a^3b^2"),
            Polynomial.from_string("a^3b^2+a^2b+ab"),
        ),
    ]
)
def test_order_polynomial_descending(polynomial, result):
    assert polynomial.order_on('a') == result


@pytest.mark.parametrize(
    "polynomial1,polynomial2,result",
    [
        (
            Polynomial.from_string("ab+cd"),
            Polynomial.from_string("ab+cd"),
            Polynomial.from_string("2ab+2cd"),
        ),
        (
            Polynomial.from_string("2ab+3cd+4xy"),
            Polynomial.from_string("3ab+4cd+5xy"),
            Polynomial.from_string("5ab+7cd+9xy"),
        ),
        (
            Polynomial.from_string("2ab+3c^2d^3+4xy"),
            Polynomial.from_string("3ab+4cd+5xy"),
            Polynomial.from_string("5ab+3c^2d^3+4cd+9xy"),
        ),
        (
            Polynomial.from_string("2ab+3a^2b+4ab^2"),
            Polynomial.from_string("ab+a^2b+ab^2+x^2y^2"),
            Polynomial.from_string("3ab+4a^2b+5ab^2+x^2y^2"),
        ),
    ]
)
def test_sum_polynomials(polynomial1, polynomial2, result):
    assert polynomial1 + polynomial2 == result


@pytest.mark.parametrize(
    "polynomial1,polynomial2,result",
    [
        (
            Polynomial.from_string("ab+2cd+3xy"),
            Polynomial.from_string("-ab-cd-xy"),
            Polynomial.from_string("cd+2xy"),
        ),
        (
            Polynomial.from_string("2ab-3cd-4xy"),
            Polynomial.from_string("-ab-4cd+5xy"),
            Polynomial.from_string("ab-7cd+xy"),
        ),
        (
            Polynomial.from_string("2ab-3cd-4xy"),
            Polynomial.from_string("-ab-4c^2d+5xy"),
            Polynomial.from_string("ab-3cd-4c^2d+xy"),
        ),
    ]
)
def test_substract_polynomials(polynomial1, polynomial2, result):
    assert polynomial1 - polynomial2 == result


@pytest.mark.parametrize(
    "polynomial,monomial,result",
    [
        (
            Polynomial.from_string("2ab+3cd+4xy"),
            Monomial.from_string("ab"),
            Polynomial.from_string("2a^2b^2+3abcd+4axyb"),
        ),
        (
            Polynomial.from_string("2ab+3c^2d^3+4xy"),
            Monomial.from_string("c^2d^3"),
            Polynomial.from_string("6abc^4d^6+12c^4d^6+20c^2d^3xy"),
        ),
    ]
)
def test_polynomial_multiplication_by_monomial(polynomial, monomial, result):
    assert polynomial * monomial == result


@pytest.mark.parametrize(
    "polynomial1,polynomial2,result",
    [
        (
            Polynomial.from_string("ab+cd"),
            Polynomial.from_string("ab+cd"),
            Polynomial.from_string("a^2b^2+c^2d^2"),
        ),
        (
            Polynomial.from_string("2ab+3cd+4xy"),
            Polynomial.from_string("3ab+4cd+5xy"),
            Polynomial.from_string("6a^2b^2+12c^2d^2+20x^2y^2"),
        ),
        (
            Polynomial.from_string("2ab+3c^2d^3+4xy"),
            Polynomial.from_string("3ab+4cd+5xy"),
            Polynomial.from_string("6a^2b^2+12c^4d^6+20x^2y^2"),
        ),
    ]
)
def test_polynomial_multiplication(polynomial1, polynomial2, result):
    assert polynomial1 * polynomial2 == result


@pytest.mark.parametrize(
    "polynomial,monomial,quotient,remainder",
    [
        (
            Polynomial.from_string("2ab+3cd+4xy"),
            Monomial.from_string("ab"),
            Polynomial.from_string("2b+3c+4y"),
            Polynomial.from_string("0"),
        ),
        (
            Polynomial.from_string("2ab+3c^2d^3+4xy"),
            Monomial.from_string("c^2d^3"),
            Polynomial.from_string("6ab+12d^6+20xy"),
            Polynomial.from_string("0"),
        ),
    ]
)
def test_polynomial_division_by_monomial(polynomial, monomial, quotient, remainder):
    assert polynomial / monomial == (quotient, remainder)