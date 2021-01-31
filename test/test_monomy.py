import unittest
from code.monomy import Monomy

class TestMonomy(unittest.TestCase):
    def test_monomy_with_no_coefficient_and_no_exponents_is_correctly_build(self):
        monomy = Monomy('abc')

        self.assertEqual(monomy.monomy_coeficient, 1)
        self.assertEqual(monomy.literals_list, ['a', 'b', 'c'])
        self.assertDictEqual(monomy.literal_to_exponent_mapping, {
            'a': 1, 'b': 1, 'c': 1
        })

    def test_monomy_with_coefficient_is_correctly_build(self):
        monomy = Monomy('2xyz')

        self.assertEqual(monomy.monomy_coeficient, 2)
        self.assertEqual(monomy.literals_list, ['x', 'y', 'z'])
        self.assertEqual(monomy.literal_to_exponent_mapping, {
            'x': 1, 'y': 1, 'z': 1
        })

    def test_monomy_with_coefficient_and_exponents_is_correctly_build(self):
        monomy = Monomy('3a^2b^3c')

        self.assertEqual(monomy.monomy_coeficient, 3)
        self.assertEqual(monomy.literals_list, ['a', 'b', 'c'])
        self.assertEqual(monomy.literal_to_exponent_mapping, {
            'a': 2, 'b': 3, 'c': 1
        })

    def test_monomy_with_negative_1_coefficient(self):
        monomy = Monomy('-abc')

        self.assertEqual(monomy.monomy_coeficient, -1)
        self.assertEqual(monomy.literals_list, ['a', 'b', 'c'])
        self.assertEqual(monomy.literal_to_exponent_mapping, {
            'a': 1, 'b': 1, 'c': 1
        })

    def test_monomy_with_negative_coefficient_different_than_1(self):
        monomy = Monomy('-2xyz^2')

        self.assertEqual(monomy.monomy_coeficient, -2)
        self.assertEqual(monomy.literals_list, ['x', 'y', 'z'])
        self.assertEqual(monomy.literal_to_exponent_mapping, {
            'x': 1, 'y': 1, 'z': 2
        })

class TestMonomyOperations(unittest.TestCase):
    def test_monomy_sum(self):
        monomy_1 = Monomy('2a')
        monomy_2 = Monomy('a')

        result = monomy_1 + monomy_2

        self.assertEqual(result, '3a')
