import unittest

class DietTest(unittest.TestCase):
    def test(self):
        diet = Diet(0.9, 4)
        
        self.assertEqual(diet.unit_price(), 11.85)
        self.assertEqual(diet.total_price(), 47.4)
        self.assertEqual(diet.factor, 0.9)
        
    def test_default_min_and_max(self):
        diet = Diet(0.9, 4, 5, 30)
        
        # Values of object
        self.assertEqual(diet.minimum_price(), 5)
        self.assertEqual(diet.maximum_price, 30)
        
        # Values of class
        self.assertEqual(Diet.minimum_price(), 10)
        self.assertEqual(Diet.maximum_price, 20)

if __name__ == '__main__':
    unittest.main()