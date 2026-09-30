import unittest
from scripts.greet import greet

class TestGreetFunction(unittest.TestCase):
    def test_greet_with_valid_name(self):
        self.assertEqual(greet('Alice'), 'Hello, ALICE!')

    def test_greet_with_none(self):
        self.assertEqual(greet(None), 'Hello, THERE!')

    def test_greet_with_empty_string(self):
        self.assertEqual(greet(''), 'Hello, THERE!')

    def test_greet_with_no_arguments(self):
        self.assertEqual(greet(), 'Hello, THERE!')

if __name__ == '__main__':
    unittest.main()
