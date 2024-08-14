import unittest
from math_functions import is_even

class TestMathFunctions(unittest.TestCase):

    def test_is_even_true(self):
        self.assertTrue(is_even(4))

    def test_is_even_false(self):
        self.assertFalse(is_even(5))




if __name__ == '__main__':
    unittest.main()