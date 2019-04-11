import unittest
from location import *

class TestLab1(unittest.TestCase):

    def test_repr(self):
        loc = Location('SLO', 35.3, -120.7)
        self.assertEqual(repr(loc),"Location('SLO', 35.3, -120.7)")
    
    # Add more tests!
    def test_eq(self):
        loc1 = Location("Orange", 30, 30)
        loc2 = Location("Raising Canes", 52, 179)
        loc3 = Location("Raising Canes", 52, 179)
        self.assertEqual(loc1 == loc2, False)
        self.assertEqual(loc3 == loc2, True)

if __name__ == "__main__":
        unittest.main()
