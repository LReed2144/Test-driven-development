import math
import unittest

def square(x):
    return x * x

assert square(10) == 100

# include a number of assert statements

# fix bugs and run tests that varifies everything is working

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True 


#unittest
#test library

class Tests(unittest.TestCase):

    def test_1(self):
        #a doc string, special function to access 
 
        """check that 1 is not prime"""
        self.assertFalse(is_prime(1))

    def test_2(self):
        """check that 2 is prime"""
        self.assertTrue(is_prime(2)) 
 
#  runs all the unit tests
if __name__ == "__main__":  
    unittest.main()

