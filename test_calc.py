import unittest
from calc import total

class TotalTest(unittest.TestCase):
    def test_total(self):
        self.assertEqual(total(2, 3), 5)

if __name__ == '__main__':
    unittest.main()