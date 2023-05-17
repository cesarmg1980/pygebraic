import pytest

from base.monomial import Monomial


def test_monomy_with_no_coefficient_and_no_exponents_is_correctly_build():
    monomial = Monomial.from_string_expression("abc")

    assert monomial.coefficient == 1
    assert monomial.variables == {"a": 1, "b": 1, "c": 1}
    assert "abc" == f"{monomial}"


def test_monomial_with_coefficient_is_correctly_build():
    monomial = Monomial.from_string_expression("2xyz")

    assert monomial.coefficient == 2
    assert monomial.variables == {"x": 1, "y": 1, "z": 1}
    assert "2xyz" == f"{monomial}"


def test_monomial_with_coefficient_and_exponents_is_correctly_build():
    monomial = Monomial.from_string_expression("3a^2b^3c")

    assert monomial.coefficient == 3
    assert monomial.variables == {"a": 2, "b": 3, "c": 1}
    assert "3a^2b^3c" == f"{monomial}"


def test_monomial_with_negative_1_coefficient():
    monomial = Monomial.from_string_expression("-abc")

    assert monomial.coefficient == -1
    assert monomial.variables == {"a": 1, "b": 1, "c": 1}
    assert "-abc" == f"{monomial}"


def test_monomial_with_negative_coefficient_different_than_1():
    monomial = Monomial.from_string_expression("-2xyz^2")

    assert monomial.coefficient == -2
    assert monomial.variables == {"x": 1, "y": 1, "z": 2}
    assert "-2xyz^2" == f"{monomial}"


def test_two_monomies_are_equal():
    monomial_1 = Monomial.from_string_expression("3xy")
    monomial_2 = Monomial.from_string_expression("3xy")

    assert monomial_1 == monomial_2


@pytest.mark.parametrize(
    "monomial_1,monomial_2,result",
    [
        (
            Monomial.from_string_expression("a"),
            Monomial.from_string_expression("a"),
            Monomial.from_string_expression("2a"),
        ),
        (
            Monomial.from_string_expression("-2ab"),
            Monomial.from_string_expression("-2ab"),
            Monomial.from_string_expression("-4ab"),
        ),
        (
            Monomial.from_string_expression("4xy"),
            Monomial.from_string_expression("-2xy"),
            Monomial.from_string_expression("2xy"),
        ),
        (
            Monomial.from_string_expression("-4zx"),
            Monomial.from_string_expression("2zx"),
            Monomial.from_string_expression("-2zx"),
        ),
        (
            Monomial.from_string_expression("10zx"),
            Monomial.from_string_expression("5zx"),
            Monomial.from_string_expression("15zx"),
        ),
    ],
)
def test_alike_monomial_sum(monomial_1, monomial_2, result):
    assert monomial_1 + monomial_2 == result


@pytest.mark.parametrize(
    "monomial_1,monomial_2,result",
    [
        (
            Monomial.from_string_expression("4a"),
            Monomial.from_string_expression("a"),
            Monomial.from_string_expression("3a"),
        ),
        (
            Monomial.from_string_expression("-4ab"),
            Monomial.from_string_expression("-2ab"),
            Monomial.from_string_expression("-2ab"),
        ),
        (
            Monomial.from_string_expression("4xy"),
            Monomial.from_string_expression("-2xy"),
            Monomial.from_string_expression("6xy"),
        ),
        (
            Monomial.from_string_expression("-4zx"),
            Monomial.from_string_expression("2zx"),
            Monomial.from_string_expression("-6zx"),
        ),
        (
            Monomial.from_string_expression("-10zx"),
            Monomial.from_string_expression("5zx"),
            Monomial.from_string_expression("-15zx"),
        ),
    ],
)
def test_alike_monomial_substraction(monomial_1, monomial_2, result):
    assert monomial_1 - monomial_2 == result


@pytest.mark.parametrize(
    "monomial_1,monomial_2,result",
    [
        (
            Monomial.from_string_expression("a"),
            Monomial.from_string_expression("a"),
            Monomial.from_string_expression("a^2"),
        ),
        (
            Monomial.from_string_expression("b"),
            Monomial.from_string_expression("-b"),
            Monomial.from_string_expression("-b^2"),
        ),
        (
            Monomial.from_string_expression("2b"),
            Monomial.from_string_expression("3b"),
            Monomial.from_string_expression("6b^2"),
        ),
        (
            Monomial.from_string_expression("2x"),
            Monomial.from_string_expression("-4x"),
            Monomial.from_string_expression("-8x^2"),
        ),
        (
            Monomial.from_string_expression("2x^2y"),
            Monomial.from_string_expression("10xy"),
            Monomial.from_string_expression("20x^3y^2"),
        ),
    ],
)
def test_monomial_product(monomial_1, monomial_2, result):
    assert monomial_1 * monomial_2 == result