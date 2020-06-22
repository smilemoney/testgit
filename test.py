import unittest
from test1 import printhh

class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, False)

    def test_test1(self):
        printhh()

if __name__ == "__main__":
    unittest.main()