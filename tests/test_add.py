import unittest
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from scripts.add import add

class TestAddFunction(unittest.TestCase):
    def test_positive_integers(self):
        self.assertEqual(add(2, 3), 5)

    def test_negative_and_positive(self):
        self.assertEqual(add(-1, 1), 0)

    def test_zeros(self):
        self.assertEqual(add(0, 0), 0)

    def test_floats(self):
        self.assertAlmostEqual(add(10.5, 4.5), 15.0)

if __name__ == '__main__':
    unittest.main()
