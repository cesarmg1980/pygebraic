from code.monomy import Monomy

def test_monomy_with_no_coefficient_and_no_exponents_is_correctly_build():
    monomy = Monomy('abc')

    assert monomy.monomy_coeficient == 1
    assert monomy.literals_list == ['a', 'b', 'c']
    assert monomy.literal_to_exponent_mapping == {'a': 1, 'b': 1, 'c': 1}

def test_monomy_with_coefficient_is_correctly_build():
    monomy = Monomy('2xyz')

    assert monomy.monomy_coeficient ==  2
    assert monomy.literals_list == ['x', 'y', 'z']
    assert monomy.literal_to_exponent_mapping == {'x': 1, 'y': 1, 'z': 1}

def test_monomy_with_coefficient_and_exponents_is_correctly_build():
    monomy = Monomy('3a^2b^3c')

    assert monomy.monomy_coeficient == 3
    assert monomy.literals_list == ['a', 'b', 'c']
    assert monomy.literal_to_exponent_mapping == {'a': 2, 'b': 3, 'c': 1}

def test_monomy_with_negative_1_coefficient():
    monomy = Monomy('-abc')

    assert monomy.monomy_coeficient == -1
    assert monomy.literals_list == ['a', 'b', 'c']
    assert monomy.literal_to_exponent_mapping == {'a': 1, 'b': 1, 'c': 1}

def test_monomy_with_negative_coefficient_different_than_1():
    monomy = Monomy('-2xyz^2')

    assert monomy.monomy_coeficient == -2
    assert monomy.literals_list == ['x', 'y', 'z']
    assert monomy.literal_to_exponent_mapping == {'x': 1, 'y': 1, 'z': 2}

def test_monomy_sum():
    monomy_1 = Monomy('2a')
    monomy_2 = Monomy('a')

    result = monomy_1 + monomy_2

    assert result == '3a'
