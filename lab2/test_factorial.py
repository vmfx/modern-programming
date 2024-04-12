import unittest
from factorial import factorial

class TestAdditionalFactorial(unittest.TestCase):
    
    def test_factorial_of_zero(self):
        self.assertEqual(factorial(0), 1)

    def test_factorial_of_positive_number(self):
        self.assertEqual(factorial(5), 120)
        self.assertEqual(factorial(10), 3628800)

    def test_negative_number_raises_error(self):
        with self.assertRaises(ValueError):
            factorial(-1)
            
    def test_factorial_of_one(self):
        self.assertEqual(factorial(1), 1)

    def test_factorial_of_negative_number(self):
        with self.assertRaises(ValueError):
            factorial(-5)
                    
    def test_factorial_of_two(self):
        self.assertEqual(factorial(2), 2)

    def test_factorial_of_large_negative_number(self):
        with self.assertRaises(ValueError):
            factorial(-100)
            
    def test_factorial_of_three(self):
        self.assertEqual(factorial(3), 6)  

    def test_float_input(self):
        with self.assertRaises(ValueError):
            factorial(5.5)

    def test_small_number(self):
        result = factorial(0)
        self.assertEqual(result, 1)

    def test_non_numeric_string_input(self):
        with self.assertRaises(ValueError):
            factorial("abc") 
            
    def test_numeric_string_input(self):
         result = factorial(5)
         self.assertEqual(result, 120)
           
                                       
if __name__ == "__main__":
    unittest.main()



