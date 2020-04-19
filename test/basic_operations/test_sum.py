import sys
import unittest
sys.path.insert(0, '/home/cesarmg/my-dev-project/algebra-with-python')
from code.basic_operations.sum import AlgebraicSum
from code.base.base import AlgebraicTerm


class TestAlgebraicTerm(unittest.TestCase):
    def test_algebraic_expression_is_properly_created(self):
        term = AlgebraicTerm('5x2y2j')
        self.assertEqual(str(term), '20xyj')


class TestAlgebraicSum(unittest.TestCase):
    def test_order_similar_terms(self):
        pass


    def test_algebraic_sum_result_is_ok_with_positive_operands(self):
        pass


if __name__ == "__main__":
    unittest.main()