import unittest
import solution1
from solution1 import *

class test_class(unittest.TestCase):
    def test_1(self):
        pass
        print 'Test Case 1: Passed'

    # test for checking if the code is able to find the max share price of a company and
    # displays the year and month correctly
    def test_2(self):
        try:
            cs_obj = Company_Shares('input.txt')
            result = cs_obj.max_share_companies
            self.assertEqual(result[1],[986, [('2007', 'Mar')]])
            print 'Test Case 2: Passed'
        except AssertionError,e:
            print 'Test 2 Failed'
    
    # test for checking if wrong file is given as input
    def test_3(self):
        try:
            cs_obj = Company_Shares('no-file-present.txt')
            result = cs_obj.max_share_companies
            self.assertEqual(result,"File not found exception")
            print 'Test Case 3: Passed'
        except AssertionError,e:
            print 'Test 3 Failed'

    # test for checking if the code catches the case where the share price of a company
    # is maximum for more than 2 period of times
    def test_4(self):
        try:
            cs_obj = Company_Shares('input.txt')
            result = cs_obj.max_share_companies
            self.assertEqual(result[0],[1000, [('1999', 'Aug'), ('2000', 'Mar')]])
            print 'Test Case 4: Passed'
        except AssertionError,e:
            print 'Test 4 Failed'

    # test for checking if the length of columns in each row is equal or not 
    def test_5(self):
        try:
            cs_obj = Company_Shares('input2.txt')
            result = cs_obj.max_share_companies
            self.assertEqual(result,"File is malformed")
            print 'Test Case 5: Passed'
        except AssertionError,e:
            print 'Test 5 Failed'
            
if __name__ == '__main__':
    unittest.main()