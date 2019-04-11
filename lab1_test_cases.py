import unittest
from lab1 import *

 # A few test cases.  Add more!!!
class TestLab1(unittest.TestCase):

    def test_max_list_iter(self):
        """Tests max_list_iter for ValueError and correct max values"""
        tlist = None
        with self.assertRaises(ValueError):  # used to check for exception
            max_list_iter(tlist)
        
        self.assertEqual(max_list_iter([]), None)
        self.assertEqual(max_list_iter([35,0,-4]), 35)
        self.assertEqual(max_list_iter([5,20,6]), 20)
        self.assertEqual(max_list_iter([5,9,13]), 13)

    def test_reverse_rec(self):
        self.assertEqual(reverse_rec([1,2,3]),[3,2,1])
        self.assertEqual(reverse_rec([1,1,1,1]),[1,1,1,1])
        with self.assertRaises(ValueError):  # used to check for exception
            reverse_rec(None)

    def test_bin_search(self):
        list_val =[0,1,2,3,4,7,8,9,10]
        low = 0
        high = len(list_val)-1
        self.assertEqual(bin_search(4, 0, len(list_val)-1, list_val), 4 )
        list_val3 = [0,1]
        self.assertEqual(bin_search(1, 0, len(list_val3)-1, list_val3), 1 )
        
        list_val2 = [0,5,7,22]
    def test_bin_search_none(self):
        list_val2 = [0,5,7,22]
        #tests if target isnt present
        self.assertEqual(bin_search(4, 0, len(list_val2)-1, list_val2), None )
        self.assertEqual(bin_search(6, 0, len(list_val2)-1, list_val2), None )
        
    def test_bin_search_len(self):
        list_val2 = [0,5,7,22]
        #tests list of even length
        self.assertEqual(bin_search(7, 0, len(list_val2)-1, list_val2), 2 )
        
    def test_bin_search_range(self):
        list_val2 = [0,5,7,22]
        #tests limited range
        self.assertEqual(bin_search(5, 1, len(list_val2)-1, list_val2), 1 )

    def test_bin_search_range_none(self):
        list_val2 = [0,5,7,22]
        #tests limited range and no target present
        self.assertEqual(bin_search(23, 1, len(list_val2)-1, list_val2), None )
        
    def test_bin_search_value_error(self):
        #tests for value error
        tlist = None
        with self.assertRaises(ValueError):  # used to check for exception
            bin_search(14, 0, 5, tlist)

        
if __name__ == "__main__":
        unittest.main()

    
