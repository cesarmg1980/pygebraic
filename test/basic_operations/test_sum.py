import sys
import unittest
sys.path.insert(0, '/home/cesarmg/my-dev-project/algebra-with-python')
from code.basic_operations.sum import AlgebraicSum
from code.base.base import AlgebraicTerm


class TestAlgebraicTerm(unittest.TestCase):
    def test_algebraic_expression_is_properly_created(self):
        term = AlgebraicTerm('20x^2yj')
        self.assertEqual(term.coeficient, 20)
        self.assertEqual(term.literals['literal_0']['literal'], 'x')
        self.assertEqual(term.literals['literal_0']['exponent'], 2)
        self.assertEqual(term.literals['literal_1']['literal'], 'y')
        self.assertEqual(term.literals['literal_1']['exponent'], 1)
        self.assertEqual(term.literals['literal_2']['literal'], 'j')
        self.assertEqual(term.literals['literal_2']['exponent'], 1)
        self.assertEqual(str(term), '20x^2yj')


class TestAlgebraicSum(unittest.TestCase):
    def test_order_similar_terms(self):
        pass


    def test_algebraic_sum_result_is_ok_with_positive_operands(self):
        pass


if __name__ == "__main__":
    unittest.main()