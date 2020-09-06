import unittest
from code.basic_operations.sum import AlgebraicSum


class TestAlgebraicSum(unittest.TestCase):
    def test_algebraic_sum_result_is_ok(self):
        expressions = ['4ab', '2xy']
        alg_sum = AlgebraicSum(expressions)
        result = alg_sum.sum()
        self.assertEqual(result, '4ab+2xy')



if __name__ == "__main__":
    unittest.main()
