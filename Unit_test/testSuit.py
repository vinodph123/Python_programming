## This file is created to understand and practice unittest test suite

import unittest




class Example(unittest.TestCase):
    
    def setUp(self):
        print('!!!!!!!!!!!!!!! This is setUp fixture set !!!!!!!!!!!!!')

    def tearDown(self):
        print('$$$$$$$$$$$$ This is tearDown fixture $$$$$$$$$')

    def test_sample(self):
        print('This is sample method used to test the unittest package ')

    def test_sample1(self):
        print('One more sample test function used to test the unittest package ')


if __name__ == '__main__':
    t1 = []
    t1.append(Example.test_sample)
    t1.append(Example.test_sample1)
    #temp = unittest.TestResult('sample.txt',True,0)
    #u = unittest.TestSuite()
    #u.addTest(test=Example.test_sample)
    #u.addTest(test=Example.test_sample1)
    #u.addTests(t1)
    unittest.main()
    
    #print(type(result.))