import unittest
import LeapYear

class test_LeapYear(unittest.TestCase):
    
    def test_LeapYear(self):
        self.assertEqual((LeapYear.LeapYearfunc(4)), "4 Is a leap year.")
        self.assertEqual((LeapYear.LeapYearfunc(400)), "400 Is a leap year.")

if __name__ == '__main__':
    unittest.main()