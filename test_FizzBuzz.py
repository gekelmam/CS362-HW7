import unittest
import FizzBuzz

class test_FizzBuzz(unittest.TestCase):
    
    def test_FizzBuzz(self):
        self.assertEqual((FizzBuzz.FizzBuzzfunc(7)), "12Fizz4BuzzFizz" )
        self.assertEqual((FizzBuzz.FizzBuzzfunc(2)), "1" )

if __name__ == '__main__':
    unittest.main()