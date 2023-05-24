import pytest

from base.base import Monomial, MonomialSign, Polynomial


def test_monomy_with_no_coefficient_and_no_exponents_is_correctly_build():
    monomial = Monomial.from_string("abc")

    assert monomial.coefficient == 1
    assert monomial.variables == {"a": 1, "b": 1, "c": 1}
    assert monomial.sign == MonomialSign.POSITIVE
    assert "abc" == f"{monomial}"


def test_monomial_with_coefficient_is_correctly_build():
    monomial = Monomial.from_string("2xyz")

    assert monomial.coefficient == 2
    assert monomial.variables == {"x": 1, "y": 1, "z": 1}
    assert monomial.sign == MonomialSign.POSITIVE
    assert "2xyz" == f"{monomial}"


def test_monomial_with_coefficient_and_exponents_is_correctly_build():
    monomial = Monomial.from_string("3a^2b^3c")

    assert monomial.coefficient == 3
    assert monomial.variables == {"a": 2, "b": 3, "c": 1}
    assert monomial.sign == MonomialSign.POSITIVE
    assert "3a^2b^3c" == f"{monomial}"


def test_monomial_with_negative_1_coefficient():
    monomial = Monomial.from_string("-abc")

    assert monomial.coefficient == -1
    assert monomial.variables == {"a": 1, "b": 1, "c": 1}
    assert monomial.sign == MonomialSign.NEGATIVE
    assert "-abc" == f"{monomial}"


def test_monomial_with_negative_coefficient_different_than_1():
    monomial = Monomial.from_string("-2xyz^2")

    assert monomial.coefficient == -2
    assert monomial.variables == {"x": 1, "y": 1, "z": 2}
    assert monomial.sign == MonomialSign.NEGATIVE
    assert "-2xyz^2" == f"{monomial}"


def test_two_monomies_are_equal():
    monomial_1 = Monomial.from_string("3xy")
    monomial_2 = Monomial.from_string("3xy")

    assert monomial_1 == monomial_2


@pytest.mark.parametrize(
    "monomial_1,monomial_2,result",
    [
        (
            Monomial.from_string("a"),
            Monomial.from_string("a"),
            Monomial.from_string("2a"),
        ),
        (
            Monomial.from_string("-2ab"),
            Monomial.from_string("-2ab"),
            Monomial.from_string("-4ab"),
        ),
        (
            Monomial.from_string("4xy"),
            Monomial.from_string("-2xy"),
            Monomial.from_string("2xy"),
        ),
        (
            Monomial.from_string("-4zx"),
            Monomial.from_string("2zx"),
            Monomial.from_string("-2zx"),
        ),
        (
            Monomial.from_string("10zx"),
            Monomial.from_string("5zx"),
            Monomial.from_string("15zx"),
        ),
    ],
)
def test_alike_monomial_sum(monomial_1, monomial_2, result):
    assert monomial_1 + monomial_2 == result


@pytest.mark.parametrize(
    "monomial_1,monomial_2,result",
    [
        (
            Monomial.from_string("4a"),
            Monomial.from_string("a"),
            Monomial.from_string("3a"),
        ),
        (
            Monomial.from_string("-4ab"),
            Monomial.from_string("-2ab"),
            Monomial.from_string("-2ab"),
        ),
        (
            Monomial.from_string("4xy"),
            Monomial.from_string("-2xy"),
            Monomial.from_string("6xy"),
        ),
        (
            Monomial.from_string("-4zx"),
            Monomial.from_string("2zx"),
            Monomial.from_string("-6zx"),
        ),
        (
            Monomial.from_string("-10zx"),
            Monomial.from_string("5zx"),
            Monomial.from_string("-15zx"),
        ),
    ],
)
def test_alike_monomial_substraction(monomial_1, monomial_2, result):
    assert monomial_1 - monomial_2 == result


@pytest.mark.parametrize(
    "monomial_1,monomial_2,result",
    [
        (
            Monomial.from_string("a"),
            Monomial.from_string("a"),
            Monomial.from_string("a^2"),
        ),
        (
            Monomial.from_string("b"),
            Monomial.from_string("-b"),
            Monomial.from_string("-b^2"),
        ),
        (
            Monomial.from_string("2b"),
            Monomial.from_string("3b"),
            Monomial.from_string("6b^2"),
        ),
        (
            Monomial.from_string("2x"),
            Monomial.from_string("-4x"),
            Monomial.from_string("-8x^2"),
        ),
        (
            Monomial.from_string("2x^2y"),
            Monomial.from_string("10xy"),
            Monomial.from_string("20x^3y^2"),
        ),
    ],
)
def test_monomial_product(monomial_1, monomial_2, result):
    assert monomial_1 * monomial_2 == result


@pytest.mark.parametrize(
    "monomial_1,monomial_2,result",
    [
        (
            Monomial.from_string("4a^2b^2"),
            Monomial.from_string("2ab"),
            Monomial.from_string("2ab"),
        ),
        (
            Monomial.from_string("4a^2b^2"),
            Monomial.from_string("-2ab"),
            Monomial.from_string("-2ab"),
        ),
        (
            Monomial.from_string("4ab"),
            Monomial.from_string("2a"),
            Monomial.from_string("2b"),
        ),
        (
            Monomial.from_string("4ab"),
            Monomial.from_string("-2ab"),
            Monomial.from_string("-2"),
        ),
        (
            Monomial.from_string("4ab"),
            Monomial.from_string("4ab"),
            Monomial.from_string("1"),
        ),
        (
            Monomial.from_string("4ab"),
            Monomial.from_string("-4ab"),
            Monomial.from_string("-1"),
        ),
    ],
)
def test_monomial_division(monomial_1, monomial_2, result):
    monomial_1 / monomial_2 == result


@pytest.mark.parametrize(
    "monomial_1,monomial_2,result",
    [
        (
            Monomial.from_string("2ab"),
            Monomial.from_string("2cd"),
            Polynomial.from_string("2ab+2cd"),
        ),
        (
            Monomial.from_string("2ab"),
            Monomial.from_string("4a^2b"),
            Polynomial.from_string("2ab+4a^2b"),
        ),
        (
            Monomial.from_string("2a^2b^3"),
            Monomial.from_string("2a^3b^2"),
            Polynomial.from_string("2a^2b^3+2a^3b^2"),
        ),

    ],
)
def test_non_alike_monomial_sum_yields_a_polinomial(monomial_1, monomial_2, result):
    monomial_1 + monomial_2 == result
    assert isinstance(result, Polynomial)

