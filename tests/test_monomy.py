from code.monomy import Monomy

import pytest


def test_monomy_with_no_coefficient_and_no_exponents_is_correctly_build():
    monomy = Monomy("abc")

    assert monomy.coefficient == 1
    assert monomy.literals_list == ["a", "b", "c"]
    assert monomy.literal_to_exponent_mapping == {"a": 1, "b": 1, "c": 1}
    assert "abc" == f"{monomy}"


def test_monomy_with_coefficient_is_correctly_build():
    monomy = Monomy("2xyz")

    assert monomy.coefficient == 2
    assert monomy.literals_list == ["x", "y", "z"]
    assert monomy.literal_to_exponent_mapping == {"x": 1, "y": 1, "z": 1}
    assert "2xyz" == f"{monomy}"


def test_monomy_with_coefficient_and_exponents_is_correctly_build():
    monomy = Monomy("3a^2b^3c")

    assert monomy.coefficient == 3
    assert monomy.literals_list == ["a", "b", "c"]
    assert monomy.literal_to_exponent_mapping == {"a": 2, "b": 3, "c": 1}
    assert "3a^2b^3c" == f"{monomy}"


def test_monomy_with_negative_1_coefficient():
    monomy = Monomy("-abc")

    assert monomy.coefficient == -1
    assert monomy.literals_list == ["a", "b", "c"]
    assert monomy.literal_to_exponent_mapping == {"a": 1, "b": 1, "c": 1}
    assert "-abc" == f"{monomy}"


def test_monomy_with_negative_coefficient_different_than_1():
    monomy = Monomy("-2xyz^2")

    assert monomy.coefficient == -2
    assert monomy.literals_list == ["x", "y", "z"]
    assert monomy.literal_to_exponent_mapping == {"x": 1, "y": 1, "z": 2}
    assert "-2xyz^2" == f"{monomy}"


def test_two_monomies_are_equal():
    monomy_1 = Monomy("3xy")
    monomy_2 = Monomy("3xy")

    assert monomy_1 == monomy_2


@pytest.mark.skip(reason="Not Implemented Yet")
def test_alike_monomy_sum():
    monomy_1 = Monomy("a")
    monomy_2 = Monomy("a")

    result = monomy_1 + monomy_2

    assert result == "2a"


@pytest.mark.skip(reason="Not Implemented Yet")
def test_not_alike_monomy_sum():
    monomy_1 = Monomy("2a")
    monomy_2 = Monomy("b")

    result = monomy_1 + monomy_2

    assert result == "2a+b"
