import unittest
from app import add, sub


class TestMathFunctions(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add(5, 3), 8)
        self.assertEqual(add(-1, 1), 0)
        self.assertEqual(add(0, 0), 0)


    def test_sub(self):
        self.assertEqual(sub(5, 3), 2)
        self.assertEqual(sub(-1, 1), -2)
        self.assertEqual(sub(0, 0), 0)


if __name__ == '__main__':
    unittest.main() 
    