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
        input_terms = ['4ab', '2x', 'ab']
        alg_sum = AlgebraicSum(input_terms)
        ordered_terms = alg_sum.order_similar_terms(input_terms)
        self.assertEqual(ordered_terms, ['4ab', 'ab', '2x'])


    def test_algebraic_sum_result_is_ok_with_positive_operands(self):
        expressions = ['4ab', '2xy']
        alg_sum = AlgebraicSum(expressions)
        result = alg_sum.sum()
        self.assertEqual(result, '4ab+2xy')


if __name__ == "__main__":
    unittest.main()