import unittest
from scripts.greet import greet


class TestGreet(unittest.TestCase):
    def test_greet_with_name(self):
        self.assertEqual(greet("Alice"), "Hello, ALICE!")
        self.assertEqual(greet("world"), "Hello, WORLD!")

    def test_greet_with_none(self):
        self.assertEqual(greet(None), "Hello, THERE!")


if __name__ == "__main__":
    unittest.main()
