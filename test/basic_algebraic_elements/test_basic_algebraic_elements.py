import unittest
from code.basic_algebraic_elements.basic_algebraic_elements import Monomy

class TestBasicAlgebraicElements(unittest.TestCase):
    def test_monomy_with_no_coefficient_and_no_exponents_is_correctly_build(self):
        monomy = Monomy('abc')

        self.assertEqual(monomy.monomy_coeficient, 1)
        self.assertEqual(monomy.literals_list, ['a', 'b', 'c'])
        self.assertDictEqual(monomy.literal_to_exponent_mapping, {
            'a': 1,
            'b': 1,
            'c': 1
        })
